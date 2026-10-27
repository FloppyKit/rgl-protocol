"""r1.13 orchestrator (spec §6, §8): preflight -> 3 fits in parallel (own process groups) -> sealed scoring, with a
watchdog that stops the r1.13 process tree if system swap used > 7,168 MiB or the tree RSS > 6,144 MiB.
Only ever signals its own children's process groups. Never deletes.
  real : r113_run.py --real            (outputs R/r113; scoring refused unless Verify's FROZEN file is valid)
  smoke: r113_run.py --smoke TAG       (outputs R/r113_smoke/TAG; seeds 67170/67171 train, 67172 val, 77149 test)"""
import argparse, json, os, re, signal, subprocess, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import r113_common as RC  # noqa: E402

SMOKE_FIT_ARGS = ["--smoke", "--steps-cap", "40", "--eval-every", "10", "--min-steps", "20", "--patience", "2",
                  "--val-limit", "600"]


def swap_used_mib() -> float:
    out = subprocess.run(["sysctl", "-n", "vm.swapusage"], capture_output=True, text=True).stdout
    m = re.search(r"used = ([\d.]+)([MG])", out)
    return float(m.group(1)) * (1024 if m.group(2) == "G" else 1) if m else 0.0


def tree_rss_mib(root_pid: int) -> float:
    rows = subprocess.run(["ps", "-axo", "pid=,ppid=,rss="], capture_output=True, text=True).stdout.split("\n")
    kids, rss = {}, {}
    for r in rows:
        p = r.split()
        if len(p) == 3:
            kids.setdefault(int(p[1]), []).append(int(p[0])); rss[int(p[0])] = int(p[2])
    tot, todo = 0, [root_pid]
    while todo:
        q = todo.pop(); tot += rss.get(q, 0); todo += kids.get(q, [])
    return tot / 1024.0


def live_conflicts() -> list:
    out = subprocess.run(["ps", "-axo", "pid=,command="], capture_output=True, text=True).stdout
    me = {os.getpid(), os.getppid()}
    keys = ("r113_fit.py", "r113_score.py", "r113_record.py", "pm_record.py", "pm_t1_train.py", "r112_run.py",
            "r111_run.py", "rung_r3p5.py", "shaping_pilot.py", "vizdoom")
    return [l.strip() for l in out.splitlines() if any(k in l for k in keys) and int(l.split()[0]) not in me]


class Run:
    def __init__(self, root: Path):
        self.root, self.kids = root, {}
        (root / "logs").mkdir(parents=True, exist_ok=False)
        self.log = open(root / "logs" / "RUN_LOG.jsonl", "x", buffering=1)

    def note(self, **k):
        k["t"] = time.strftime("%Y-%m-%d %H:%M:%S %Z")
        self.log.write(json.dumps(k) + "\n"); print(json.dumps(k), flush=True)

    def start(self, name, argv):
        lf = open(self.root / "logs" / f"{name}.out", "x")
        env = dict(os.environ, OMP_NUM_THREADS=str(RC.THREADS_PER_FIT), MKL_NUM_THREADS=str(RC.THREADS_PER_FIT),
                   PYTHONDONTWRITEBYTECODE="1")
        p = subprocess.Popen([RC.PY, "-B"] + argv, stdout=lf, stderr=subprocess.STDOUT, env=env, start_new_session=True)
        self.kids[name] = p
        self.note(event="start", name=name, pid=p.pid, argv=argv)
        return p

    def stop_all(self, why):
        self.note(event="stop_all", why=why)
        for p in self.kids.values():
            if p.poll() is None:
                try: os.killpg(p.pid, signal.SIGTERM)
                except ProcessLookupError: pass
        t = time.time()
        while time.time() - t < 30 and any(p.poll() is None for p in self.kids.values()):
            time.sleep(1)
        for p in self.kids.values():
            if p.poll() is None:
                try: os.killpg(p.pid, signal.SIGKILL)
                except ProcessLookupError: pass

    def wait_all(self, names, swap_cap=RC.SWAP_CAP_MIB, rss_cap=RC.RSS_CAP_MIB):
        last, peak = 0.0, {"swap_mib": 0.0, "tree_rss_mib": 0.0}
        while any(self.kids[n].poll() is None for n in names):
            sw, rs = swap_used_mib(), tree_rss_mib(os.getpid())
            peak = {"swap_mib": max(peak["swap_mib"], sw), "tree_rss_mib": max(peak["tree_rss_mib"], rs)}   # DV-R281
            if time.time() - last > 300:
                self.note(event="watch", swap_mib=round(sw), tree_rss_mib=round(rs)); last = time.time()
            if sw > swap_cap or rs > rss_cap:
                self.stop_all(f"watchdog: swap {sw:.0f} MiB (cap {swap_cap}) / tree RSS {rs:.0f} MiB (cap {rss_cap})")
                RC.jw(self.root / "logs" / f"STOP_WATCHDOG_{int(time.time())}.json", {"swap_mib": sw, "tree_rss_mib": rs})
                return False
            time.sleep(RC.WATCH_EVERY_S)
        rcs = {n: self.kids[n].returncode for n in names}
        self.note(event="ended", rcs=rcs, peak_swap_mib=round(peak["swap_mib"]), peak_tree_rss_mib=round(peak["tree_rss_mib"]))
        return all(v == 0 for v in rcs.values())


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--real", action="store_true")
    g.add_argument("--smoke", metavar="TAG")
    a = ap.parse_args()
    smoke = a.smoke is not None
    root = RC.SMOKE_ROOTS / a.smoke if smoke else RC.REAL_ROOT
    pre = []
    if not smoke:
        pre += RC.frozen_refusals()                     # real runs start only after Verify PASS (spec §9)
        pre += RC.data_pins_refusals()
    pre += [f"live conflicting process: {c}" for c in live_conflicts()]
    if root.exists():
        pre.append(f"{root} exists (fresh root required)")
    if swap_used_mib() > RC.SWAP_CAP_MIB:
        pre.append("swap already above the cap")
    st = os.statvfs(RC.RUNS)
    if st.f_bavail * st.f_frsize / 2**30 < RC.MIN_FREE_GIB:
        pre.append(f"MiniHangar free < {RC.MIN_FREE_GIB} GiB")
    if pre:
        sys.exit(f"REFUSED preflight: {pre}")
    R = Run(root)
    R.note(event="preflight_ok", smoke=smoke, train=list(RC.SMOKE_TRAIN if smoke else RC.TRAIN_SEEDS),
           val=RC.SMOKE_VAL if smoke else RC.VAL_SEED, init_seeds=RC.INIT_SEEDS)
    fit = str(RC.HERE / "r113_fit.py")
    for f in sorted(RC.INIT_SEEDS):
        R.start(f"fit_{f}", [fit, "--root", str(root), "--fit", f] + (SMOKE_FIT_ARGS if smoke else []))
    if not R.wait_all([f"fit_{f}" for f in sorted(RC.INIT_SEEDS)]):
        R.note(event="run_stopped", phase="fits", rule="no scoring; 67150 untouched (spec §6)")
        sys.exit(2)
    R.start("score", [str(RC.HERE / "r113_score.py"), "--root", str(root)] + (["--smoke"] if smoke else []))
    ok = R.wait_all(["score"])
    R.note(event="done" if ok else "score_failed_or_refused", ok=ok)
    sys.exit(0 if ok else 3)


if __name__ == "__main__":
    main()
