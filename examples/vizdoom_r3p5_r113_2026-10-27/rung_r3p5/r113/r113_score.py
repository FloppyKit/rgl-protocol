"""r1.13 sealed scoring (spec §5). Real mode: refuses unless Verify's FROZEN file exists and matches the live spec and
code, all 3 fits finished, 67150 is unseen and no seal marker exists. Then, once: write the seal marker (mode x), record
67150 (r113_record.py, 20,000 steps; extended to 30,000 / 40,000 on the same seed only if the label-only adequacy floors
fail), score each fit's chosen checkpoint once, write SCORES_r1.13.csv, VERDICT_r1.13.json, WRITEUP_r1.13.md.
Smoke mode: the same path on the already-used smoke seed 77149 (1,500 steps); 67150 is refused outright.
Never re-scores. Never deletes. Usage (via r113_run.py only): r113_score.py --root DIR [--smoke]"""
import argparse, csv, json, os, subprocess, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import r113_common as RC  # noqa: E402

CSV_COLS = ("run_tag", "mode", "fit_id", "init_seed", "n_train_seeds", "val_seed", "stop_reason", "stop_step",
            "chosen_step", "val_auc_chosen", "val_lr_chosen", "test_seed", "test_steps_recorded", "n_frames",
            "n_visible", "auc", "lr_acc", "centred_auc", "lr_small", "n_small", "lr_large", "n_large",
            "lr_offcentre9", "n_offcentre9", "fit_pass", "model_sha256")


def fits_refusals(root: Path, smoke: bool) -> list:
    why = []
    for f in sorted(RC.INIT_SEEDS):
        p = Path(root) / "fits" / f / "RESULT.json"
        if not p.is_file():
            why.append(f"fit {f} has no RESULT.json")
            continue
        r = json.loads(p.read_text())
        if bool(r.get("smoke")) != smoke or r.get("init_seed") != RC.INIT_SEEDS[f]:
            why.append(f"fit {f} RESULT mode/init seed mismatch")
        if not smoke and (r.get("train_seeds") != list(RC.TRAIN_SEEDS) or r.get("val_seed") != RC.VAL_SEED):
            why.append(f"fit {f} trained on other seeds than pre-registered")
        if RC.sha(Path(root) / "fits" / f / "model_chosen.pt") != r.get("model_sha256"):
            why.append(f"fit {f} checkpoint sha differs from its RESULT")
    return why


def score_refusals(root: Path, test_seed: int, smoke: bool, frozen: Path = RC.FROZEN_PATH, runs: Path = RC.RUNS,
                   unseen=RC.test_seed_unseen_refusals) -> list:
    """Every reason scoring is refused (empty = may score). THE GUARD: 67150 needs a valid Verify FROZEN file."""
    root, s = Path(root), int(test_seed)
    if smoke:
        why = [] if s == RC.SMOKE_TEST_SEED else [f"smoke test seed must be {RC.SMOKE_TEST_SEED}"]
        if s == RC.TEST_SEED:
            why.append("67150 is never used by a smoke")
        if root.resolve() == RC.REAL_ROOT.resolve():
            why.append("smoke may not write into the real root")
        return why + fits_refusals(root, True)
    why = RC.frozen_refusals(frozen)
    if s != RC.TEST_SEED:
        why.append(f"real test seed must be {RC.TEST_SEED}")
    if root.resolve() != RC.REAL_ROOT.resolve():
        why.append(f"real scoring must use {RC.REAL_ROOT}")
    if (root / "score" / RC.SEAL_MARK).exists():
        why.append("67150 was already opened (seal marker exists): no re-scoring, ever")
    why += RC.seed_list_refusals(RC.TRAIN_SEEDS, RC.VAL_SEED, s)
    why += fits_refusals(root, False)
    if not why:
        why += unseen(runs)
    return why


def record(seed: int, steps: int, out: Path, env: dict) -> dict:
    log = out.parent / f"rec_{seed}_s{steps}.log"
    with open(log, "x") as lf:
        rc = subprocess.run([RC.PY, "-B", str(RC.HERE / "r113_record.py"), "--seed", str(seed), "--steps", str(steps),
                             "--out", str(out)], stdout=lf, stderr=subprocess.STDOUT, env=env,
                            cwd=str(RC.PM_DIR)).returncode
    if rc != 0:
        raise RuntimeError(f"recording {seed} ({steps} steps) failed rc={rc}; see {log}")
    return json.loads((out / "DEMO_SUMMARY.json").read_text())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--smoke", action="store_true")
    a = ap.parse_args()
    root, smoke = Path(a.root), a.smoke
    seed = RC.SMOKE_TEST_SEED if smoke else RC.TEST_SEED
    why = score_refusals(root, seed, smoke)
    if why:
        sys.exit(f"REFUSED scoring {seed}: {why}")
    sd = root / "score"
    sd.mkdir(parents=True, exist_ok=smoke)
    t0 = time.time()
    if not smoke:                                         # the seal: written once, before 67150 is first touched
        RC.jw(sd / RC.SEAL_MARK, {"started": time.strftime("%Y-%m-%d %H:%M:%S %Z"), "frozen_sha256": RC.sha(RC.FROZEN_PATH),
                                  "rule": "one scoring of 67150, ever; a crash after this point is not retried (spec §5)"})
    env = dict(os.environ, R113_SEALED_SCORE="0" if smoke else "1", PYTHONDONTWRITEBYTECODE="1")
    import numpy as np, torch  # noqa: E401
    import r19b_p0 as P9
    torch.set_num_threads(RC.THREADS_PER_FIT)
    steps_list = (RC.SMOKE_TEST_STEPS,) if smoke else RC.TEST_STEPS
    adeq_log, store, used_steps, summ = [], None, None, None
    for n in steps_list:
        d = sd / f"demo_rgb_{seed}_s{n}"
        summ = record(seed, n, d, env)
        st = RC.Multi({seed: d})
        ad = RC.adequacy_counts(st, seed, summ["episodes"])
        ad["steps"] = n
        adeq_log.append(ad)
        store, used_steps = st, n
        if ad["ok"] or smoke:
            break
    RC.jw(sd / "ADEQUACY.json", {"tries": adeq_log, "smoke": smoke})
    if not adeq_log[-1]["ok"] and not smoke:
        RC.jw(sd / "VERDICT_r1.13.json", {"verdict": "STOP_ADEQUACY", "detail": adeq_log,
                                          "rule": "no fit is scored; 67150 is burned; Matt decides (spec §5)"})
        sys.exit("STOP: 67150 failed the adequacy floors at 40,000 steps; nothing scored")
    rows = []
    for f in sorted(RC.INIT_SEEDS):
        r = json.loads((root / "fits" / f / "RESULT.json").read_text())
        net = P9.ProbeNet2((120, 160), 3)
        net.load_state_dict(torch.load(root / "fits" / f / "model_chosen.pt", map_location="cpu"))
        m, (pv, pl, pc) = RC.metrics(net, store)
        with open(sd / f"PRED_{seed}_{f}.npz", "xb") as fh:
            np.savez(fh, pv=pv, pl=pl, pc=pc)
        off, n_off = RC.lr_offcentre(pl, store)
        rows.append({"run_tag": root.name, "mode": "smoke" if smoke else "real", "fit_id": f, "init_seed": r["init_seed"],
                     "n_train_seeds": len(r["train_seeds"]), "val_seed": r["val_seed"], "stop_reason": r["stop_reason"],
                     "stop_step": r["stop_step"], "chosen_step": r["chosen_step"], "val_auc_chosen": r["val_auc_chosen"],
                     "val_lr_chosen": r["val_lr_chosen"], "test_seed": seed, "test_steps_recorded": used_steps,
                     "n_frames": m["n"], "n_visible": m["n_visible"], "auc": m["visible_auc"], "lr_acc": m["lr_acc"],
                     "centred_auc": m["centred_auc"], "lr_small": m["by_box"]["small"]["lr_acc"],
                     "n_small": m["by_box"]["small"]["n_visible"], "lr_large": m["by_box"]["large"]["lr_acc"],
                     "n_large": m["by_box"]["large"]["n_visible"], "lr_offcentre9": off, "n_offcentre9": n_off,
                     "fit_pass": RC.fit_pass(m["visible_auc"], m["lr_acc"]), "model_sha256": r["model_sha256"]})
        print("scored", f, m["visible_auc"], m["lr_acc"], flush=True)
    with open(sd / "SCORES_r1.13.csv", "x", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=CSV_COLS)
        w.writeheader()
        w.writerows(rows)
    v = RC.verdict(rows)
    v.update(smoke=smoke, test_seed=seed, bars={"auc": RC.BAR_AUC, "lr": RC.BAR_LR}, wall_s=round(time.time() - t0, 1),
             csv_sha256=RC.sha(sd / "SCORES_r1.13.csv"), clinical_claim=False)
    RC.jw(sd / "VERDICT_r1.13.json", v)
    lines = [f"# r1.13 P0-SEEDS {'SMOKE (not a result)' if smoke else 'sealed result'}: {v['verdict']}", "",
             f"Test seed {seed} ({used_steps} steps, {rows[0]['n_visible']} visible frames). Bars: visible AUC >= "
             f"{RC.BAR_AUC} AND L/R >= {RC.BAR_LR}. Rule: >= 2 of 3 fits pass, the median fit passes, medians clear both.",
             "", "| fit | init seed | stop | chosen step | AUC | L/R | small L/R | large L/R | pass |", "|---|---|---|---|---|---|---|---|---|"]
    lines += [f"| {r['fit_id']} | {r['init_seed']} | {r['stop_reason']} @ {r['stop_step']} | {r['chosen_step']} | "
              f"{r['auc']:.4f} | {r['lr_acc']:.4f} | {r['lr_small'] if r['lr_small'] is None else round(r['lr_small'], 4)} | "
              f"{r['lr_large'] if r['lr_large'] is None else round(r['lr_large'], 4)} | {r['fit_pass']} |" for r in rows]
    lines += ["", f"n_pass {v['n_pass']}/3; median fit {v.get('median_fit')}; median AUC {v.get('median_auc')}; "
              f"median L/R {v.get('median_lr')}.", "",
              "PASS -> BC/PPO may proceed under its own spec. FAIL -> 67150 is burned: no re-scoring, no bar or rule change, "
              "no new fit scored on 67150; any next step needs a new pre-registration and a new fresh seed (spec §5).",
              "clinical_claim: false."]
    with open(sd / "WRITEUP_r1.13.md", "x") as fh:
        fh.write("\n".join(lines) + "\n")
    print("VERDICT", v["verdict"], flush=True)


if __name__ == "__main__":
    main()
