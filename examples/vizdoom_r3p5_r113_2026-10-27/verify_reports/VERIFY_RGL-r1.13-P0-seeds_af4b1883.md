# VERIFY RGL-r1.13-P0-seeds

Pre-registration review only. Nothing real was trained or scored. Seed 67150 was not recorded. FROZEN was not written (verdict FAIL). Real run was not launched.

Tip = sha256 of `r113/VERIFY_PACKAGE_r1.13.md` (not a git tree): `af4b188332d7fe9fedeeb40020dff8024f3a92998b97e3d89f1089e3411a9e7c`
Spec sha256: `e47e8b533ea0d011be98504d9753033b142e252c026013787f405971a322fd05`
C = `/Users/dude/rgl-proofs/GO-RGL-INTERP-1/scratch/rung_r3p5`
R = `/Volumes/MiniHangar/rgl-artifacts/GO-RGL-INTERP-1/rung_r3p5_runs`
PY = `/Volumes/MiniHangar/rgl-envs/GO-RGL-INTERP-1.venv/bin/python`
Logs: `/Users/dude/Orbitty GOs/verify_logs_RGL-r1.13-P0-seeds_af4b1883/`

Rig (measured, not count-only): root avail 20.75 GiB (`df -k /`, avail_kib 21762992) after the smoke; MiniHangar avail 1677 GiB; RAM 16 GiB; swap at end `used = 4909.62M` of `6144.00M`. No cargo step. Not a RIG BLOCKER.

## Gates

1. **PASS** — live shas of the 14 package files equal the package. Spec sha `e47e8b53…fd05`. Package sha `af4b1883…1a9e7c`.
   Command: `cd $C && shasum -a 256` on the 14 paths in VERIFY_PACKAGE §Exact commands.
   Log: `verify_logs_…/shasum_spec_pkg.log` (spec + package). Full 14-file shasum was re-run in session and matched the package table byte for byte (including `r113_common.py` `b27f16fa…`, `r113_score.py` `aa7acbf5…`, `test_r113.py` `9c1a7639…`).

2. **PASS** — `RUNG_SPEC_r1.13_P0_SEEDS.md` line 6 supersedes r1.13 card t454s2084. Line 5 basis is Matt, 2026-10-26 11:38 PM CT: "pre-register it for Verify".

3. **PASS** — training step in `r113_fit.py` matches `postmortem_20261026/pm_t1_train.py`: ProbeNet2 `(120,160), 3`, Adam `P.LR` 1e-3, `HalfVisibleSampler` batch 64 / half 32, mirror p 0.5 + `mirror_left` + `lr_weight`, BCE vis+cen+L/R, `select_epoch` (ties to earlier epoch; `r19b_p0.py` `lr(h) > lr(best)`). Differences are the ones the checklist allows: seed list, early stop, per-fit RNG (`INIT_SEEDS`, A = `P.TRAIN_RNG_SEED` 67140), report seeds (chosen checkpoint only, not the post-mortem final checkpoint). Pread header parse vs a brief mmap for the offset is DV-R270; frames 0 and 1000 of 67170 were byte-equal to `np.load` (offset 128).

4. **PASS** — `TRAIN_SEEDS` is the 24 seeds in the spec order. None is in `USED_TEST_SEEDS` (67143–67149), none is 67150, none is val 67172. Lists disjoint. `test_seed_lists_disjoint_and_sized` passed.

5. **PASS** — fresh 67190–67194. Lane log `R/r113_demos/logs/rec_lanes.log`: all five `rc=0` (23:45–23:47 CDT). Each `DEMO_SUMMARY.json` has `recorder: postmortem_20261026/pm_record.py`, `steps: 20000`, `eps: 0.1`, `screen_format: RGB24`. Scan file sha matches (`764dbddc…`). I re-read every hit: no env seed field for 67190–67194 (counters, `end_step`, `n_in_seed` under other seeds, colormap decimals, `to-check=`, `range(67170, 67190)`, `67100 <= … <= 67199`). `test_data_pins_match` and `test_fresh_seeds_registry_and_scan` passed (pin re-hash). Pin counts: train frames 480000, visible 100061, per-seed visible 3059–5417, val 67172 visible 4950. All match the spec.

6. **PASS** — val 67172 is not in `TRAIN_SEEDS`. Constants `(EVAL_EVERY, MIN_STEPS, MAX_STEPS, PATIENCE, MIN_DELTA) == (1460, 14600, 58400, 5, 0.002)`. `test_fit_refuses_nondefault_real_args` passed (refused before `fits/` mkdir).

7. **PASS** — fits A/B/C = 67140, 1130001, 1130002. Distinct. A equals `P.TRAIN_RNG_SEED`.

8. **FAIL** — pass rule tie-break does not match the spec / DV-R268. Spec §5 and `verdict()` docstring: median fit is the fit with the median 67150 L/R; a tie goes to the lower AUC (DV-R268: conservative). Code does `sorted(ok, key=(lr_acc, auc))[1]`. When two fits share the lower L/R (that value is the median) and the third is higher, index 1 is the higher-AUC of the tied pair, not the lower. That can turn a spec FAIL into a code PASS.
   Repro (`verify_logs_…/tiebreak_repro.log`):
   `verdict([A auc 0.90 lr 0.81, B auc 0.84 lr 0.81, C auc 0.90 lr 0.90])` → code `PASS`, `median_fit A`. Conservative rule: median fit B (fails AUC) → FAIL.
   3-way L/R tie: code picks middle AUC (`median_fit C`, PASS) not lowest AUC (B, FAIL).
   Smoke `verify_smoke_20261027_0007` had a 3-way L/R tie (all `0.47766323024054985`); code set `median_fit C` (middle AUC), not B (lowest AUC). All three failed the bars, so that smoke verdict did not flip. Bars, inclusive `>=`, raw floats, and missing-fit = FAIL match the spec (`test_pass_rule` passed; it has no tie case).
   Command: `$PY` one-liner importing `r113_common.verdict` (log above).

9. **PASS** (note N1) — executed refuses, all before any 67150 touch:
   - `$C/r113/run_r113.sh real` exit 1: `REFUSED preflight: ['no FROZEN file …']`. `R/r113` not created. Log: `guard_real.log`.
   - `$PY -B r113_score.py --root $R/r113` exit 1: `REFUSED scoring 67150: ['no FROZEN file …', 'fit A/B/C has no RESULT.json']`. Log: `guard_score.log`.
   - `$PY -B r113_record.py --seed 67150 --steps 20 --out <tmp>` exit 1: `refused: recording 67150: [no FROZEN, not the sealed scoring, no seal marker]`. No output dir created. Log: `guard_record.log`.
   - `pm_record.py --seed 67150` still `AssertionError` on `seed not in PC.RESERVED` before mkdir. Log: `guard_pm_record.log`.
   - Pytest: seal marker blocks re-score; smoke refuses 67150; real scoring refuses a non-`R/r113` root. Guard in `r113_record.py` is before `out.mkdir` and `EV.EnvB35`. Smoke path hardcodes 77149.

10. **PASS** (code read; not executed on 67150) — `r113_score.py` writes `SEAL_67150_STARTED.json` with `RC.jw` (mode `x`) before `record()`. A later `score_refusals` sees the marker and refuses. Unit test `test_seal_marker_blocks_rescoring` passed.

11. **PASS** (code read) — `adequacy_counts` uses `probe_labels` / box bins only. Model `load_state_dict` and `RC.metrics` run only after the adequacy loop. `STOP_ADEQUACY` exits before any fit is scored.

12. **PASS** — `RSS_CAP_MIB` 6144, `SWAP_CAP_MIB` 7168, `WATCH_EVERY_S` 15, `THREADS_PER_FIT` 3, `start_new_session=True`, `os.killpg` only on `self.kids`, `os.pread`, no `mmap_mode` in `r113_common.py`. `test_no_deletes_anywhere` passed. Preflight `live_conflicts` only reads `ps` and does not signal. `test_memory_settings_present` passed.

13. **PASS** — `cd $C/r113 && $PY -B -m pytest -q -p no:cacheprovider tests/test_r113.py` → `19 passed in 32.37s`, exit 0. Log: `pytest_test_r113.log`.

14. **PASS** — `$C/r113/run_r113.sh smoke verify_smoke_20261027_0007` exit 0. `RUN_LOG.jsonl` ends `{"event": "done", "ok": true}` at 2026-10-27 00:07:47 CDT. Fits used train 67170/67171, val 67172, init 67140/1130001/1130002 (stops max_steps/patience/max_steps). Score test seed 77149, 1500 steps. Wrote `SCORES_r1.13.csv`, `VERDICT_r1.13.json` (FAIL, expected at 40 steps), `WRITEUP_r1.13.md` headed SMOKE. CSV columns match the spec. No `*67150*` under the smoke tree. Log: `smoke_stdout.log`. Tree: `R/r113_smoke/verify_smoke_20261027_0007/`.

15. **PASS** — `find $R -name '*67150*'` empty before smoke, after smoke, and after the refuse checks. `find $C -name '*67150*'` empty. Logs: `find_67150_before.txt`, `find_67150_after_R.txt`, `find_67150_after_C.txt`.

16. **PASS** — DV-R261…R276 accepted. In particular: R263 reuses val 67172 (not a test seed, not in train, no path to 67150); R262 drops 67140/67142 as training data (different length/recorder; 67140 remains RNG only); R273 no RIG_OK (Chuck: measured-need only; checked here); R269 report-only used-seed scores stay inside the fit and out of `verdict()`. Wording notes: N3, N4.

17. **PASS** (notes N2, N5) — timing artifacts, not the cook's prose: `timing2_noeval_20261026` RESULT wall 103.8 s / 584 steps = 0.1777 s/step (spec 0.178). `timing1_20261026` wall 197.1 s with 2 full-val evals; delta 93.3 s → ~46.7 s/eval (spec ~47 s). Interval math (5.1 min, min ~1.1 h, cap ~3.7 h, expected 2–2.5 h) follows from those rates. Live swap at smoke start was 4950 MiB (cap 7168; headroom 2218 MiB), tighter than the spec's ~3 GB. Watchdog still stops the fit tree before scoring if the cap is hit. 16 GiB RAM; claimed 1144 MiB peak was not in any log I could find (N5). Plausible. Not a spec-bug block.

18. **Not done** — FROZEN is written only on PASS / PASS-with-notes. This round is FAIL. `C/r113/FROZEN_r1.13.json` is absent. `run_r113.sh real` was not launched after any freeze (there is none).

## Notes

N1. `test_seed_unseen_refusals` uses `Path.glob("*/**/*67150*")`. That misses a depth-1 name directly under R (`top_67150.txt`, `demo_rgb_67150/`). Depth ≥2 matches, including `r113/score/demo_rgb_67150_s20000`. `find -name '*67150*'` is empty today, and the score writer never places 67150 at depth 1. Read-only check; not the blocking fail. Fix it before the next freeze so a PASS does not pin the hole. (`rglob("*67150*")` matches `find -name`.)

N2. Swap during this smoke: watch line `swap_mib: 4950` at 00:07:17 CDT. Cap 7168. Headroom ~2.2 GiB, not ~3 GiB. End of verify: used 4909.62M / total 6144.00M.

N3. DV-R266 says the new `sys.path` makes `pm_common` import from `C/r113`. The diff inserts `postmortem_20261026`, which is where `pm_common.py` lives. Import is correct. Prose is wrong.

N4. Spec §4 says the three RNG seeds "sit outside every env-seed range". 67140 is an old env/demo seed (r110). DV-R265 is the accurate line: A is T1's RNG seed; B and C are outside env ranges. Not used as an env seed here.

N5. Spec's "peak tree RSS 1,144 MiB" is not in `R/r113_smoke/*/logs`. timing1/timing2 have fit RESULT.json but no `RUN_LOG.jsonl`. I did not re-run a 24-seed fit to measure RSS.

## DOGFOOD (Matt)

Not driven, neither PASS nor FAIL:

1. Real run. Do not start it on this FAIL. After a later PASS writes `C/r113/FROZEN_r1.13.json`, RGL Lab (not Verify) starts it:
   `/Users/dude/rgl-proofs/GO-RGL-INTERP-1/scratch/rung_r3p5/r113/run_r113.sh real`
   Outputs `R/r113`. That command scores 67150 once. A FAIL burns 67150.
2. 24-seed RSS peak (spec 1,144 MiB) was not remeasured. A measurement is a partial fit, not this review.

## Left running / on disk

Left running: nothing. No r113/vizdoom/pm_record process after the checks.

Left on disk:

- `R/r113_smoke/verify_smoke_20261027_0007/` (this review's smoke; throwaway seeds only)
- `/Users/dude/Orbitty GOs/verify_logs_RGL-r1.13-P0-seeds_af4b1883/` (pytest, smoke stdout, guard logs, tie-break repro, find logs)
- This report
- Cook smokes already present: `R/r113_smoke/smoke1_20261026`, `timing1_20261026`, `timing2_noeval_20261026`
- No `C/r113/FROZEN_r1.13.json`. No `R/r113`. No `*67150*` under R or C. My `/tmp` refuse dir and glob temp were removed.

## Result
FAIL
PASS tip: af4b188332d7fe9fedeeb40020dff8024f3a92998b97e3d89f1089e3411a9e7c
Fails:
- Gate 8: `r113_common.verdict` tie-break is not the conservative lower-AUC median fit (DV-R268 / spec §5). Low-side L/R tie (two fits at the median L/R, one higher) selects the higher-AUC fit and can PASS when the written rule FAILs. Repro: `verify_logs_RGL-r1.13-P0-seeds_af4b1883/tiebreak_repro.log`.
DOGFOOD items:
- Real `run_r113.sh real` not started (must wait for a later PASS + FROZEN).
- 24-seed RSS peak not remeasured.
Fixes for Ship:
- Fix `verdict()` so a tie on the median 67150 L/R picks the lower-AUC fit, including the low-side pair and the 3-way tie. Add a gate test for `[A 0.90/0.81, B 0.84/0.81, C 0.90/0.90]` → FAIL, `median_fit` B, and for the 3-way L/R tie → lowest AUC. Do not treat `sorted(key=(lr, auc))[1]` as that rule.
- Before the next freeze, make `test_seed_unseen_refusals` match `find -name '*67150*'` (N1). A PASS would pin the current glob.
