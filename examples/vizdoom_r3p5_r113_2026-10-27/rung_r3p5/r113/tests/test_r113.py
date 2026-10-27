"""r1.13 gate tests (spec §8). Engine-free: no ViZDoom is started, nothing is recorded or trained, 67150 is never read,
recorded or scored (it appears only as a constant in list/guard checks). Run:
  cd C/r113 && $PY -B -m pytest -q -p no:cacheprovider tests/test_r113.py"""
import json, os, re, subprocess, sys
from pathlib import Path
import pytest

H = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(H))
import r113_common as RC  # noqa: E402
import r113_score as RS  # noqa: E402
import r113_run as RR  # noqa: E402


# ---------------- 1. seed lists ----------------
def test_seed_lists_disjoint_and_sized():
    tr = set(RC.TRAIN_SEEDS)
    assert len(RC.TRAIN_SEEDS) == len(tr) == 24 >= 20
    assert RC.VAL_SEED not in tr
    assert RC.TEST_SEED not in tr and RC.TEST_SEED != RC.VAL_SEED
    assert RC.TEST_SEED not in RC.REPORT_SEEDS and RC.TEST_SEED not in RC.SMOKE_TRAIN
    assert RC.TEST_SEED not in (RC.SMOKE_VAL, RC.SMOKE_TEST_SEED)
    assert not tr & set(RC.USED_TEST_SEEDS) and RC.VAL_SEED not in RC.USED_TEST_SEEDS
    assert not tr & set(RC.REPORT_SEEDS)
    assert RC.TEST_SEED == 67150
    assert RC.TRAIN_SEEDS == (67170, 67171) + tuple(range(67173, 67195))


def test_seed_list_refusals():
    assert RC.seed_list_refusals(RC.TRAIN_SEEDS, RC.VAL_SEED) == []
    assert RC.seed_list_refusals(RC.SMOKE_TRAIN, RC.SMOKE_VAL, RC.SMOKE_TEST_SEED, smoke=True) == []
    assert RC.seed_list_refusals(RC.TRAIN_SEEDS[:-1] + (RC.TEST_SEED,), RC.VAL_SEED)
    assert RC.seed_list_refusals(RC.TRAIN_SEEDS, RC.TEST_SEED)
    assert RC.seed_list_refusals(RC.TRAIN_SEEDS + (67149,), RC.VAL_SEED)
    assert RC.seed_list_refusals(RC.TRAIN_SEEDS[:19], RC.VAL_SEED)
    assert RC.seed_list_refusals(RC.TRAIN_SEEDS, RC.TRAIN_SEEDS[0])
    assert RC.seed_list_refusals(RC.SMOKE_TRAIN, RC.SMOKE_VAL, RC.TEST_SEED, smoke=True)
    with pytest.raises(RuntimeError):
        RC.demo_dir(RC.TEST_SEED)


def test_demo_dirs_exist_and_match():
    for s in list(RC.TRAIN_SEEDS) + [RC.VAL_SEED]:
        sm = json.loads((RC.demo_dir(s) / "DEMO_SUMMARY.json").read_text())
        assert int(sm["seed"]) == s and sm["steps"] == 20000 and sm["screen_format"].startswith("RGB")


def test_data_pins_match():
    assert RC.data_pins_refusals() == []


def test_fresh_seeds_registry_and_scan():
    sys.path.insert(0, str(RC.C_DIR))
    from diag.common import check_seeds
    check_seeds(list(RC.FRESH_SEEDS))       # not registered/spent/forbidden
    assert (RC.C_DIR / "logs" / "SEED_SCAN_r1.13_67190_67199_hits.txt").is_file()


# ---------------- 2. the guard ----------------
def test_no_frozen_means_refused(tmp_path):
    why = RC.frozen_refusals(tmp_path / "FROZEN_r1.13.json")
    assert why and "no FROZEN" in why[0]
    why = RS.score_refusals(RC.REAL_ROOT, RC.TEST_SEED, False, frozen=tmp_path / "nope.json", unseen=lambda r: [])
    assert any("no FROZEN" in w for w in why)


def _fake_tree(tmp_path):
    c = tmp_path / "C"
    (c / "r113").mkdir(parents=True)
    spec = c / "SPEC.md"; spec.write_text("spec")
    code = {}
    for k in RC.CODE_FILES:
        p = c / k; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(k); code[k] = RC.sha(p)
    doc = {"kind": "FROZEN", "written_by": "Verify", "verdict": "PASS", "spec_sha256": RC.sha(spec), "code": code,
           "test_seed": RC.TEST_SEED, "train_seeds": list(RC.TRAIN_SEEDS), "val_seed": RC.VAL_SEED}
    return c, spec, doc


def test_frozen_valid_and_each_tamper(tmp_path):
    c, spec, doc = _fake_tree(tmp_path)
    fz = tmp_path / "FROZEN.json"
    fz.write_text(json.dumps(doc))
    assert RC.frozen_refusals(fz, spec, c) == []
    for k, bad in (("kind", "CANDIDATE"), ("written_by", "cook"), ("verdict", "FAIL"), ("spec_sha256", "0" * 64),
                   ("test_seed", 67149), ("val_seed", 67171), ("train_seeds", list(RC.TRAIN_SEEDS[:-1]))):
        p = tmp_path / f"F_{k}.json"; p.write_text(json.dumps(dict(doc, **{k: bad}))); assert RC.frozen_refusals(p, spec, c)
    (c / RC.CODE_FILES[0]).write_text("edited")
    assert any("live code differs" in w for w in RC.frozen_refusals(fz, spec, c))


def test_score_guard_real_and_smoke(tmp_path):
    assert any("real scoring must use" in w for w in RS.score_refusals(tmp_path, RC.TEST_SEED, False, unseen=lambda r: []))
    assert any("real test seed" in w for w in RS.score_refusals(RC.REAL_ROOT, 67149, False, unseen=lambda r: []))
    assert any("never used by a smoke" in w for w in RS.score_refusals(tmp_path, RC.TEST_SEED, True))
    assert any("fit A" in w for w in RS.score_refusals(tmp_path, RC.SMOKE_TEST_SEED, True))


def test_seal_marker_blocks_rescoring(tmp_path, monkeypatch):
    monkeypatch.setattr(RC, "REAL_ROOT", tmp_path)
    (tmp_path / "score").mkdir()
    (tmp_path / "score" / RC.SEAL_MARK).write_text("{}")
    why = RS.score_refusals(tmp_path, RC.TEST_SEED, False, frozen=tmp_path / "x.json", unseen=lambda r: [])
    assert any("seal marker" in w for w in why)


def test_unseen_check(tmp_path):
    assert RC.test_seed_unseen_refusals(tmp_path) == []
    (tmp_path / "run" / "demos").mkdir(parents=True)
    (tmp_path / "run" / "demos" / f"demo_rgb_{RC.TEST_SEED}").mkdir()
    assert RC.test_seed_unseen_refusals(tmp_path)


def test_recorder_guard_block():
    """r113_record.py: the reserved-seed guard sits before any output dir or engine, and refuses without the seal."""
    src = (H / "r113_record.py").read_text()
    i_guard, i_mkdir, i_env = src.index("if seed in PC.RESERVED:"), src.index("out.mkdir("), src.index("EV.EnvB35(")
    assert i_guard < i_mkdir < i_env
    m = re.search(r"if seed in PC\.RESERVED:.*?raise SystemExit\([^\n]*\n", src, re.S)
    block = m.group(0)
    class PCs: RESERVED = (RC.TEST_SEED,)
    env = dict(os.environ); env.pop("R113_SEALED_SCORE", None)
    ns = {"seed": RC.TEST_SEED, "PC": PCs, "os": os, "Path": Path, "__file__": str(H / "r113_record.py")}
    old = os.environ.pop("R113_SEALED_SCORE", None)
    try:
        with pytest.raises(SystemExit) as e:
            exec(block, ns)
        assert "refused" in str(e.value)
    finally:
        if old is not None:
            os.environ["R113_SEALED_SCORE"] = old
    pm = (RC.PM_DIR / "pm_record.py").read_text()
    assert "assert seed not in PC.RESERVED" in pm and RC.TEST_SEED in __import__("pm_common").RESERVED


def test_fit_refuses_nondefault_real_args(tmp_path):
    p = subprocess.run([RC.PY, "-B", str(H / "r113_fit.py"), "--root", str(tmp_path), "--fit", "A", "--steps-cap", "10"],
                       capture_output=True, text=True)
    assert p.returncode != 0 and "refused" in (p.stderr + p.stdout)
    assert not (tmp_path / "fits").exists()


def test_frozen_absent_or_valid():
    assert not RC.FROZEN_PATH.exists() or RC.frozen_refusals() == []


# ---------------- 3. memory / resource settings ----------------
def test_memory_settings_present():
    assert RC.RSS_CAP_MIB == 6144 and RC.SWAP_CAP_MIB == 7168 and RC.THREADS_PER_FIT == 3 and RC.WATCH_EVERY_S <= 30
    cs = (H / "r113_common.py").read_text()
    assert "os.pread(" in cs and "mmap_mode" not in cs
    rs = (H / "r113_run.py").read_text()
    assert "swap_cap=RC.SWAP_CAP_MIB" in rs and "rss_cap=RC.RSS_CAP_MIB" in rs and "killpg" in rs
    assert "OMP_NUM_THREADS" in rs and "start_new_session=True" in rs
    assert "torch.set_num_threads(RC.THREADS_PER_FIT)" in (H / "r113_fit.py").read_text()
    sh = (H / "run_r113.sh").read_text()
    assert "OMP_NUM_THREADS=3" in sh and "rm " not in sh
    assert RR.swap_used_mib() >= 0 and RR.tree_rss_mib(os.getpid()) > 0


def test_no_deletes_anywhere():
    for p in list(H.glob("*.py")) + list(H.glob("*.sh")):
        t = p.read_text()
        assert not re.search(r"\b(os\.remove|os\.unlink|shutil\.rmtree|rmdir\(|unlink\(|\brm -)", t), p.name


# ---------------- 4. recipe, bars, rules ----------------
def test_recipe_and_bars_unchanged():
    import r18_learn as L, r19b_p0 as P9, r111_p0 as P
    assert (P.LR, P.BATCH, P.HALF_VIS, P.MIRROR_P, P.MASK_PX) == (1e-3, 64, 32, 0.5, 1.0)
    assert RC.BAR_AUC == L.P0_PASS_AUC == P9.P0B_PASS_AUC == 0.85
    assert RC.BAR_LR == L.P0_PASS_LR == P9.P0B_PASS_LR == 0.80
    assert RC.INIT_SEEDS["A"] == P.TRAIN_RNG_SEED and len(set(RC.INIT_SEEDS.values())) == 3


def _h(step, auc, lr):
    return {"epoch": step // 10, "step": step, "val": {"visible_auc": auc, "lr_acc": lr}}


def test_early_stopping_rule():
    assert (RC.EVAL_EVERY, RC.MIN_STEPS, RC.MAX_STEPS, RC.PATIENCE, RC.MIN_DELTA) == (1460, 14600, 58400, 5, 0.002)
    st = {}
    assert RC.es_update(st, _h(1460, 0.80, 0.70))
    assert RC.es_update(st, _h(2920, 0.86, 0.69))          # first to qualify on AUC = improvement
    assert not RC.es_update(st, _h(4380, 0.86, 0.6915))    # < min_delta
    assert RC.es_update(st, _h(5840, 0.86, 0.692))
    assert not RC.es_update(st, _h(7300, 0.80, 0.99))      # non-qualifying never beats a qualifying best
    for k in range(5):
        RC.es_update(st, _h(8760 + k * 1460, 0.86, 0.60))
    assert st["since"] == 6
    assert RC.es_should_stop(st, 13140) is None             # before MIN_STEPS
    assert RC.es_should_stop(st, 14600) == "patience"
    assert RC.es_should_stop({"since": 0}, 58400) == "max_steps"
    assert RC.es_should_stop({"since": 4}, 20000) is None


def test_pass_rule():
    r = lambda f, a, l: {"fit_id": f, "auc": a, "lr_acc": l}
    assert RC.verdict([r("A", .9, .82), r("B", .9, .81), r("C", .9, .83)])["verdict"] == "PASS"
    assert RC.verdict([r("A", .85, .80), r("B", .85, .80), r("C", .5, .5)])["verdict"] == "PASS"   # bars inclusive
    assert RC.verdict([r("A", .9, .82), r("B", .9, .79), r("C", .9, .78)])["verdict"] == "FAIL"   # 1 of 3
    v = RC.verdict([r("A", .86, .82), r("B", .84, .81), r("C", .90, .80)])                     # median fit B fails AUC
    assert v["verdict"] == "FAIL" and v["median_fit"] == "B" and v["n_pass"] == 2
    assert RC.verdict([r("A", .9, .82), r("B", .9, .82)])["verdict"] == "FAIL"                 # a missing fit
    assert RC.verdict([r("A", .9, .82), r("B", .9, .82), r("C", None, None)])["verdict"] == "FAIL"
    assert RC.verdict([r("A", .8499999, .9), r("B", .8499999, .9), r("C", .9, .9)])["verdict"] == "FAIL"   # no rounding


def test_pass_rule_ties():
    """DV-R277 (Verify af4b1883 Gate 8): among fits tied at the median L/R, the LOWEST AUC is the median fit."""
    r = lambda f, a, l: {"fit_id": f, "auc": a, "lr_acc": l}
    v = RC.verdict([r("A", .90, .81), r("B", .84, .81), r("C", .90, .90)])       # low-side pair
    assert v["verdict"] == "FAIL" and v["median_fit"] == "B" and v["n_pass"] == 2 and not v["rule_ii_median_fit"]
    v = RC.verdict([r("A", .86, .81), r("B", .84, .81), r("C", .90, .81)])       # 3-way tie: lowest AUC
    assert v["median_fit"] == "B" and v["verdict"] == "FAIL"
    v = RC.verdict([r("A", .95, .81), r("B", .86, .81), r("C", .87, .81)])       # 3-way tie, all pass
    assert v["median_fit"] == "B" and v["verdict"] == "PASS"
    v = RC.verdict([r("A", .90, .70), r("B", .84, .85), r("C", .91, .85)])       # high-side pair: lower AUC
    assert v["median_fit"] == "B" and v["verdict"] == "FAIL"
    v = RC.verdict([r("A", .90, .70), r("B", .91, .85), r("C", .88, .85)])
    assert v["median_fit"] == "C" and v["verdict"] == "PASS"
    v = RC.verdict([r("A", .90, .83), r("B", .84, .82), r("C", .90, .81)])       # no tie: unchanged (B = median L/R)
    assert v["median_fit"] == "B" and v["n_pass"] == 2 and v["verdict"] == "FAIL"
    v = RC.verdict([r("A", .90, .82), r("B", .88, .81), r("C", .80, .83)])
    assert v["median_fit"] == "A" and v["verdict"] == "PASS"
    v = RC.verdict([r("C", .86, .81), r("A", .86, .81), r("B", .99, .90)])       # exact AUC tie too: earliest id
    assert v["median_fit"] == "A"
    for perm in ([0, 1, 2], [2, 1, 0], [1, 2, 0]):                               # order-independent
        rows = [r("A", .90, .81), r("B", .84, .81), r("C", .90, .90)]
        assert RC.verdict([rows[i] for i in perm])["median_fit"] == "B"


def test_unseen_matches_find_any_depth(tmp_path):
    """DV-R278 (Verify N1): same set as `find R -name '*67150*'`, including depth 1."""
    for rel in (f"top_{RC.TEST_SEED}.txt", f"demo_rgb_{RC.TEST_SEED}", f"a/b/c/x{RC.TEST_SEED}y.json"):
        d = tmp_path / rel.replace("/", "_") / "root"
        d.mkdir(parents=True)
        p = d / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        (p.mkdir() if "." not in p.name else p.write_text("x"))
        assert RC.test_seed_unseen_refusals(d), rel
        out = subprocess.run(["find", str(d), "-name", f"*{RC.TEST_SEED}*"], capture_output=True, text=True).stdout.split()
        assert out
    e = tmp_path / "empty"; (e / "r" / "demos").mkdir(parents=True)
    assert RC.test_seed_unseen_refusals(e) == [] and subprocess.run(
        ["find", str(e), "-name", f"*{RC.TEST_SEED}*"], capture_output=True, text=True).stdout == ""


def test_csv_columns():
    assert RS.CSV_COLS == ("run_tag", "mode", "fit_id", "init_seed", "n_train_seeds", "val_seed", "stop_reason",
                           "stop_step", "chosen_step", "val_auc_chosen", "val_lr_chosen", "test_seed",
                           "test_steps_recorded", "n_frames", "n_visible", "auc", "lr_acc", "centred_auc", "lr_small",
                           "n_small", "lr_large", "n_large", "lr_offcentre9", "n_offcentre9", "fit_pass", "model_sha256")
