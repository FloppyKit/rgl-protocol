"""rung_r3p5 r1.13 P0-SEEDS (RUNG_SPEC_r1.13_P0_SEEDS.md): shared constants, seed lists, guards, data stores.
Pre-registered. clinical_claim: false. CPU only. Never deletes; every output file is opened mode "x".
The T1 recipe is unchanged (post-mortem pm_t1_train.py = r111c T1: ProbeNet2 RGB 120x160, Adam 1e-3, batch 64 =
32 visible + 32 any, mirror p 0.5 + label swap + 1-px mask, BCE vis + cen + L/R). Only the training-seed count and the
stopping rule change (spec §2-§4). Seed 67150 is the sealed test seed: it is touched ONLY by r113_score.py in real mode,
after every fit has finished, and only when Verify's FROZEN file exists and matches the live spec and code (spec §5)."""
from __future__ import annotations

import hashlib
import json
import os
import sys
from pathlib import Path

C_DIR = Path("/Users/dude/rgl-proofs/GO-RGL-INTERP-1/scratch/rung_r3p5")
HERE = Path(__file__).resolve().parent
PM_DIR = C_DIR / "postmortem_20261026"
os.environ.setdefault("R110_C_DIR", str(C_DIR))
os.environ.setdefault("R111_C_DIR", str(C_DIR))
for _p in (str(C_DIR), str(C_DIR / "r1_8"), str(C_DIR / "r1_9b"), str(C_DIR / "r1_10b"), str(C_DIR / "r1_12"),
           str(PM_DIR), str(HERE)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

RUNS = Path("/Volumes/MiniHangar/rgl-artifacts/GO-RGL-INTERP-1/rung_r3p5_runs")
PM_OUT = RUNS / "postmortem_20261026"
NEW_DEMOS = RUNS / "r113_demos" / "demos_rgb"
REAL_ROOT = RUNS / "r113"                       # real run outputs (fits/, score/); created by the real run only
SMOKE_ROOTS = RUNS / "r113_smoke"               # smoke outputs: r113_smoke/<tag>
PY = "/Volumes/MiniHangar/rgl-envs/GO-RGL-INTERP-1.venv/bin/python"

SPEC_PATH = C_DIR / "RUNG_SPEC_r1.13_P0_SEEDS.md"
FROZEN_PATH = HERE / "FROZEN_r1.13.json"        # written by Verify ONLY (never by this code or the cook)
SEAL_MARK = "SEAL_67150_STARTED.json"           # written (mode x) under REAL_ROOT/score before 67150 is first touched
CODE_FILES = ("r113/r113_common.py", "r113/r113_fit.py", "r113/r113_score.py", "r113/r113_run.py",
              "r113/run_r113.sh", "r113/tests/test_r113.py", "r113/DATA_PINS_r1.13.json",
              "r113/r113_record.py", "postmortem_20261026/pm_record.py",
              "postmortem_20261026/pm_common.py", "r113/record_fresh_r113.sh")

# ---------------- seeds (spec §2, §3, §5) ----------------
TEST_SEED = 67150                                # sealed; scored once, real mode only
PM_SEEDS = tuple(range(67170, 67190))            # recorded 2026-10-26 by the post-mortem (DV-PM04)
VAL_SEED = 67172                                 # early stopping only (DV-R263)
FRESH_SEEDS = (67190, 67191, 67192, 67193, 67194)   # recorded 2026-10-26/27 for r1.13 (DV-R262)
TRAIN_SEEDS = tuple(s for s in PM_SEEDS if s != VAL_SEED) + FRESH_SEEDS   # 19 + 5 = 24
# every seed ever used to SCORE a P0/P0b/P0c probe, plus excluded/failed scoring seeds (spec §2; none may train)
USED_TEST_SEEDS = (67143, 67144, 67145, 67146, 67147, 67148, 67149)
REPORT_SEEDS = (67149, 67148, 67146)             # used seeds, report-only scoring in the fit phase (not the test)
INIT_SEEDS = {"A": 67140, "B": 1_130_001, "C": 1_130_002}   # torch + numpy + mirror RNG seed per fit (DV-R265)

# ---------------- smoke (spec §8; throwaway / already-used seeds only, never 67150) ----------------
SMOKE_TRAIN = (67170, 67171)
SMOKE_VAL = 67172
SMOKE_TEST_SEED = 77149                          # r1.12 smoke seed (already used); recorded briefly into r113_smoke
SMOKE_TEST_STEPS = 1_500

# ---------------- bars and pass rule (spec §5; frozen values, raw floats, no rounding) ----------------
BAR_AUC, BAR_LR = 0.85, 0.80
N_FITS, MIN_FITS_PASS = 3, 2

# ---------------- early stopping (spec §3) ----------------
EVAL_EVERY = 1_460                               # = one T1 epoch on the r111c split; = H3 eval interval
MIN_STEPS = 14_600                               # never stop before the H3 budget (10 evals)
MAX_STEPS = 58_400                               # hard cap (40 evals; 4x H3, 2x r111c T1's 29,200)
PATIENCE = 5                                     # evals without a qualifying improvement
MIN_DELTA = 0.002                                # val L/R improvement that resets patience

# ---------------- test-seed recording and adequacy (spec §5; labels only, no model) ----------------
TEST_STEPS = (20_000, 30_000, 40_000)            # 20k as every demo seed; extend on the same seed when short
ADEQ_MIN_VISIBLE, ADEQ_LEFT_FRAC, ADEQ_MIN_BOX = 3000, (0.40, 0.60), 1000   # r1.12 floors, no episode floor

# ---------------- resources (spec §6) ----------------
THREADS_PER_FIT = 3
RSS_CAP_MIB = 6_144                              # whole r1.13 process tree
SWAP_CAP_MIB = 7_168                             # system swap used; above = stop
WATCH_EVERY_S = 15
MIN_FREE_GIB = 40                                # MiniHangar free-space floor at launch

FB = 120 * 160 * 3


def sha(p) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def jw(p, obj) -> None:
    with open(p, "x") as f:
        f.write(json.dumps(obj, indent=1, sort_keys=True, default=float) + "\n")


def demo_dir(s: int) -> Path:
    s = int(s)
    if s == TEST_SEED:
        raise RuntimeError("demo_dir(67150) is not a training/val/report path; only r113_score records 67150")
    if s in PM_SEEDS:
        return PM_OUT / "demos_rgb" / f"demo_rgb_{s}"
    if s in FRESH_SEEDS:
        return NEW_DEMOS / f"demo_rgb_{s}"
    return {67146: RUNS / "r110b/demos_rgb/demo_rgb_67146", 67148: RUNS / "r111b/demos_rgb/demo_rgb_67148",
            67149: RUNS / "r112/demos_rgb/demo_rgb_67149"}[s]


# ---------------- seed rules ----------------
def seed_list_refusals(train, val, test=TEST_SEED, report=REPORT_SEEDS, smoke: bool = False) -> list:
    tr, why = [int(s) for s in train], []
    if len(set(tr)) != len(tr):
        why.append("duplicate training seeds")
    if TEST_SEED in tr or int(val) == TEST_SEED or TEST_SEED in [int(s) for s in report]:
        why.append("67150 appears in train / val / report lists")
    if int(val) in tr:
        why.append(f"val seed {val} is also a training seed")
    if set(tr) & set(USED_TEST_SEEDS) or int(val) in USED_TEST_SEEDS:
        why.append("a seed ever used as a test (scoring) seed is in train/val")
    if int(test) in tr or int(test) == int(val):
        why.append(f"test seed {test} is in train/val")
    if not smoke and len(tr) < 20:
        why.append(f"only {len(tr)} training seeds (< 20)")
    if not smoke and (tuple(tr) != TRAIN_SEEDS or int(val) != VAL_SEED or int(test) != TEST_SEED):
        why.append("real-mode seed lists differ from the pre-registered constants")
    if smoke and (int(test) == TEST_SEED or TEST_SEED in tr):
        why.append("smoke may never use 67150")
    return why


# ---------------- FROZEN guard (spec §5, §9) ----------------
def frozen_refusals(frozen: Path = FROZEN_PATH, spec: Path = SPEC_PATH, c_dir: Path = C_DIR) -> list:
    """Every reason the sealed 67150 scoring is refused on the FROZEN file (empty = FROZEN is valid)."""
    frozen = Path(frozen)
    if not frozen.is_file():
        return [f"no FROZEN file ({frozen}); only Verify writes it after Verify PASS"]
    try:
        f = json.loads(frozen.read_text())
    except ValueError:
        return ["FROZEN file is not valid JSON"]
    why = []
    if f.get("kind") != "FROZEN":
        why.append("FROZEN kind is not 'FROZEN'")
    if str(f.get("written_by", "")).strip().lower() != "verify":
        why.append("FROZEN was not written by Verify")
    if f.get("verdict") not in ("PASS", "PASS-with-notes"):
        why.append("FROZEN does not record a Verify PASS")
    if not Path(spec).is_file() or f.get("spec_sha256") != sha(spec):
        why.append("live spec sha differs from FROZEN spec_sha256")
    code = f.get("code") or {}
    missing = [k for k in CODE_FILES if k not in code]
    if missing:
        why.append(f"FROZEN does not name {missing}")
    bad = [k for k, v in code.items() if not (Path(c_dir) / k).is_file() or sha(Path(c_dir) / k) != v]
    if bad:
        why.append(f"live code differs from FROZEN: {bad}")
    if int(f.get("test_seed", -1)) != TEST_SEED:
        why.append("FROZEN does not name test seed 67150")
    if [int(s) for s in f.get("train_seeds", [])] != list(TRAIN_SEEDS) or int(f.get("val_seed", -1)) != VAL_SEED:
        why.append("FROZEN seed lists differ from the code constants")
    return why


def data_pins_refusals(pins: Path = HERE / "DATA_PINS_r1.13.json", seeds=None) -> list:
    """Training/val demo trees must equal the sha256 pins written at build time (DATA_PINS_r1.13.json)."""
    pins = Path(pins)
    if not pins.is_file():
        return [f"{pins.name} missing"]
    doc = json.loads(pins.read_text())
    why = []
    for s in (seeds if seeds is not None else list(TRAIN_SEEDS) + [VAL_SEED]):
        d, want = demo_dir(s), doc.get("seeds", {}).get(str(s))
        if want is None:
            why.append(f"{s} not pinned")
            continue
        have = {p.name: sha(p) for p in sorted(d.iterdir()) if p.is_file() and p.suffix in (".npz", ".npy", ".json")}
        if have != want:
            why.append(f"{s} demo tree differs from its pin")
    return why


def test_seed_unseen_refusals(runs: Path = RUNS) -> list:
    """67150 must have no file or dir anywhere under RUNS whose NAME contains 67150, at any depth (the same set as
    `find RUNS -name '*67150*'`; rglob, DV-R278). Names only; nothing is opened."""
    hits = [str(p) for p in Path(runs).rglob("*67150*")][:5]
    return [f"a 67150 artifact already exists: {hits}"] if hits else []


# ---------------- data (frames read with os.pread; no mmap) ----------------
def _npy_header(p: Path) -> tuple:
    import numpy as np
    with open(p, "rb") as f:
        ver = np.lib.format.read_magic(f)
        rd = np.lib.format.read_array_header_1_0 if ver == (1, 0) else np.lib.format.read_array_header_2_0
        shape, fortran, dtype = rd(f)
        return shape, f.tell(), dtype, fortran


class PreadStore:
    def __init__(self, d, summary):
        import numpy as np
        self.fds, self.offs, self.lens = [], [], []
        for fn in summary["files"]:
            p = Path(d) / fn.replace(".npz", "_frames.npy")
            shape, off, dtype, fortran = _npy_header(p)
            assert tuple(shape[1:]) == (120, 160, 3) and str(dtype) == "uint8" and not fortran
            self.offs.append(int(off)); self.lens.append(int(shape[0]))
            self.fds.append(os.open(p, os.O_RDONLY))
        self.cum = np.cumsum([0] + self.lens)

    def get(self, idx):
        import numpy as np
        idx = np.asarray(idx, np.int64)
        out = np.empty((len(idx), 120, 160, 3), np.uint8)
        pi = np.searchsorted(self.cum, idx, side="right") - 1
        for j, (i, p) in enumerate(zip(idx, pi)):
            b = os.pread(self.fds[p], FB, self.offs[p] + int(i - self.cum[p]) * FB)
            out[j] = np.frombuffer(b, np.uint8).reshape(120, 160, 3)
        return out


class Multi:
    """Several demo dirs concatenated (labels in RAM, frames by os.pread). dirs: {seed: path}."""
    def __init__(self, dirs: dict, limit: int | None = None):
        import numpy as np
        import r18_learn as L
        self.stores, self.cols, self.seeds = [], [], [int(s) for s in dirs]
        for s, d in dirs.items():
            sm = json.loads((Path(d) / "DEMO_SUMMARY.json").read_text())
            assert int(sm["seed"]) == int(s) and sm.get("screen_format", "RGB24").startswith("RGB")
            parts = [np.load(Path(d) / f) for f in sm["files"]]
            cols = {k: np.concatenate([p[k] for p in parts]) for k in ("vis", "err", "box", "episode")}
            if limit:
                cols = {k: v[:limit] for k, v in cols.items()}
            self.stores.append(PreadStore(d, sm)); self.cols.append(cols)
        self.cum = np.cumsum([0] + [len(c["vis"]) for c in self.cols])
        cat = lambda k: np.concatenate([c[k] for c in self.cols])
        self.err, self.box, self.episode = cat("err").astype(np.float64), cat("box"), cat("episode")
        lab = [L.probe_labels(c) for c in self.cols]
        self.lab = {k: np.concatenate([l[k] for l in lab]) for k in ("vis", "left", "cen")}

    def __len__(self):
        return int(self.cum[-1])

    def get(self, idx):
        import numpy as np
        idx = np.asarray(idx, np.int64)
        out = np.empty((len(idx), 120, 160, 3), np.uint8)
        si = np.searchsorted(self.cum, idx, side="right") - 1
        for s in np.unique(si):
            m = si == s
            out[m] = self.stores[s].get(idx[m] - self.cum[s])
        return out


def x_of(store, idx, flip=None):
    import numpy as np
    import torch
    import r111_p0 as P
    f = store.get(idx)
    if flip is not None:
        f = P.mirror_frames(f, flip)
    return torch.as_tensor(np.ascontiguousarray(f.transpose(0, 3, 1, 2), dtype=np.float32) / 255.0)


def predict(net, store, chunk: int = 128):
    import numpy as np
    import torch
    net.eval()
    pv, pl, pc = [], [], []
    with torch.no_grad():
        for i in range(0, len(store), chunk):
            o = net(x_of(store, np.arange(i, min(i + chunk, len(store)))))
            pv.append(o[0].numpy()); pl.append(o[1].numpy()); pc.append(o[2].numpy())
    net.train()
    return np.concatenate(pv), np.concatenate(pl), np.concatenate(pc)


def metrics(net, store) -> tuple:
    import r18_learn as L
    pv, pl, pc = predict(net, store)
    return L.p0_metrics(pv, pl, pc, store.lab, store.box), (pv, pl, pc)


def lr_offcentre(pl, store, deg: float = 9.0) -> tuple:
    import numpy as np
    m = store.lab["vis"] & (np.abs(np.nan_to_num(store.err)) > deg)
    return (float(np.mean((pl[m] > 0) == store.lab["left"][m])) if m.any() else None), int(m.sum())


# ---------------- early stopping (spec §3) ----------------
def qualifies(h) -> bool:
    return h["val"]["visible_auc"] is not None and h["val"]["visible_auc"] >= BAR_AUC


def es_update(state: dict, h: dict, min_delta: float = MIN_DELTA) -> bool:
    """Patience bookkeeping. An eval is an improvement if it is the first to reach val AUC >= 0.85, or (same
    qualification class as the best so far) its val L/R >= best L/R + min_delta. Returns True on improvement."""
    q, lr = qualifies(h), (h["val"]["lr_acc"] if h["val"]["lr_acc"] is not None else -1.0)
    b = state.get("best")
    imp = b is None or (q and not b["q"]) or (q == b["q"] and lr >= b["lr"] + min_delta)
    if imp:
        state["best"] = {"q": q, "lr": lr, "step": h["step"]}
        state["since"] = 0
    else:
        state["since"] = state.get("since", 0) + 1
    return imp


def es_should_stop(state: dict, step: int, min_steps: int = MIN_STEPS, max_steps: int = MAX_STEPS,
                   patience: int = PATIENCE) -> str | None:
    if step >= max_steps:
        return "max_steps"
    if step >= min_steps and state.get("since", 0) >= patience:
        return "patience"
    return None


# ---------------- pass rule (spec §5) ----------------
def fit_pass(auc, lr) -> bool:
    return auc is not None and lr is not None and float(auc) >= BAR_AUC and float(lr) >= BAR_LR


def median_fit_of(ok: list) -> dict:
    """Spec §5 (r1.13 rev2, DV-R277): m = the median of the three 67150 L/R values. Among ALL fits whose L/R equals m
    exactly, the median fit is the one with the LOWEST AUC (a further exact AUC tie goes to the earliest fit id). This
    covers a low-side pair, a high-side pair and a 3-way tie. Exact float equality, no rounding."""
    import statistics
    m = statistics.median(r["lr_acc"] for r in ok)
    tied = [r for r in ok if r["lr_acc"] == m]
    return min(tied, key=lambda r: (r["auc"], r["fit_id"]))


def verdict(rows: list) -> dict:
    """rows: one dict per fit with fit_id, auc, lr_acc. PASS iff (i) >= 2 of 3 fits clear both bars, (ii) the median
    fit (median_fit_of: the lowest-AUC fit among those at the median 67150 L/R) clears both bars, (iii) median AUC >=
    0.85 and median L/R >= 0.80. A missing fit counts as a failed fit; fewer than 3 scored fits = FAIL."""
    import statistics
    ok = [r for r in rows if r.get("auc") is not None and r.get("lr_acc") is not None]
    n_pass = sum(fit_pass(r["auc"], r["lr_acc"]) for r in ok)
    if len(ok) != N_FITS:
        return {"verdict": "FAIL", "n_pass": n_pass, "reason": f"{len(ok)} of {N_FITS} fits scored"}
    med = median_fit_of(ok)
    m_auc, m_lr = statistics.median(r["auc"] for r in ok), statistics.median(r["lr_acc"] for r in ok)
    c1, c2, c3 = n_pass >= MIN_FITS_PASS, fit_pass(med["auc"], med["lr_acc"]), m_auc >= BAR_AUC and m_lr >= BAR_LR
    return {"verdict": "PASS" if (c1 and c2 and c3) else "FAIL", "n_pass": n_pass, "median_fit": med["fit_id"],
            "median_auc": m_auc, "median_lr": m_lr, "rule_i_2of3": c1, "rule_ii_median_fit": c2,
            "rule_iii_medians": c3}


def adequacy_counts(store, seed: int, episodes: int) -> dict:
    import numpy as np
    import r18_learn as L
    vis = store.lab["vis"]
    nv = int(vis.sum())
    bins = np.array([L.box_bin(b) for b in np.asarray(store.box)[vis]]) if nv else np.array([])
    c = {"seed": int(seed), "episodes": int(episodes), "visible": nv,
         "left_frac": float(store.lab["left"][vis].mean()) if nv else None,
         "large": int((bins == "large").sum()), "small": int((bins == "small").sum())}
    why = []
    if nv < ADEQ_MIN_VISIBLE:
        why.append(f"visible {nv} < {ADEQ_MIN_VISIBLE}")
    if c["left_frac"] is None or not (ADEQ_LEFT_FRAC[0] <= c["left_frac"] <= ADEQ_LEFT_FRAC[1]):
        why.append(f"left fraction {c['left_frac']} outside {list(ADEQ_LEFT_FRAC)}")
    if min(c["large"], c["small"]) < ADEQ_MIN_BOX:
        why.append(f"large {c['large']} / small {c['small']}: each must be >= {ADEQ_MIN_BOX}")
    return {"counts": c, "refusals": why, "ok": not why}
