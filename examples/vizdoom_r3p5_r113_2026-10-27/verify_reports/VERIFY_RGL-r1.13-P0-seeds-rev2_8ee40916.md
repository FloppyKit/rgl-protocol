# VERIFY RGL-r1.13-P0-seeds-rev2

Pre-registration re-review after FAIL af4b1883 (Gate 8 tie-break). Nothing real was trained or scored. Seed 67150 was not recorded. Real run was not launched. FROZEN was written only after the gates below passed.

Tip = sha256 of `r113/VERIFY_PACKAGE_r1.13.md` (not a git tree): `8ee40916983b083684e963fad62a414d326e5407d1e4d65ad60f4ed7142db467`
Spec sha256 (rev2): `c30174eccd46bc209fc7a36e77fb2492278d377727a2b3b2d15c764ca1189872`
C = `/Users/dude/rgl-proofs/GO-RGL-INTERP-1/scratch/rung_r3p5`
R = `/Volumes/MiniHangar/rgl-artifacts/GO-RGL-INTERP-1/rung_r3p5_runs`
PY = `/Volumes/MiniHangar/rgl-envs/GO-RGL-INTERP-1.venv/bin/python`
Logs: `/Users/dude/Orbitty GOs/verify_logs_RGL-r1.13-P0-seeds-rev2_8ee40916/`

Rig (measured): root avail 20.75 GiB (`df -k /`, avail_kib 21759808) at the end. MiniHangar avail 1677 GiB. RAM 16 GiB (`hw.memsize` 17179869184). Swap at end `used = 4861.62M` of `6144.00M`. No cargo step. Not a RIG BLOCKER.

## Gates

1. **PASS** — live shas of all 16 package files equal the package table. Spec sha `c30174ec…9872`. Package sha `8ee40916…db467`.
   `r113/superseded/af4b1883/` copies match `SHA256SUMS_af4b1883.txt` (12/12), including rev1 spec `e47e8b53…fd05` and rev1 package `af4b1883…1a9e7c`. Claimed-unchanged files are byte-identical to those copies and to the rev1 pins: `r113_fit.py` `a92fc451…`, `r113_score.py` `aa7acbf5…`, `r113_record.py` `0296de70…`, `run_r113.sh` `347064be…`, `DATA_PINS` `cdcc0053…`, `record_fresh_r113.sh` `9f612477…`.
   `r113_common.py` diff vs rev1 is only `test_seed_unseen_refusals` (`rglob`) and `median_fit_of` (replacing `sorted(key=(lr, auc))[1]`). `r113_run.py` diff is the 5-line peak swap/RSS log in `wait_all` (DV-R281).
   Command: `cd $C && shasum -a 256` on the 16 paths, plus sha compare of superseded copies.
   Log: `01_hashes.txt`, `01_pkg_sha.txt`, `01_rev1_diff.txt`, `01_common_diff.txt`.

2. **PASS** — spec line 5 basis is Matt, 2026-10-26 11:38 PM CT: "pre-register it for Verify". Line 7 also supersedes r1.13 card t454s2084. Header states rev2 supersedes rev1 `e47e8b53…fd05`.

3. **PASS** — `r113_fit.py` is byte-identical to the rev1 file already compared to `pm_t1_train.py`. Training step still: `ProbeNet2((120,160), 3)`, Adam `P.LR`, `HalfVisibleSampler` batch/half from `P.BATCH`/`P.HALF_VIS`, mirror p `P.MIRROR_P` + `mirror_left` + `lr_weight`, BCE vis+cen+L/R, `select_epoch`. Differences allowed by the checklist: seed list, early stop, per-fit RNG (`INIT_SEEDS`, A = 67140), report seeds. Pread vs a brief mmap for the offset remains DV-R270 (accepted rev1).

4. **PASS** — `TRAIN_SEEDS` printed from the live module is the 24 seeds in spec order: 67170, 67171, 67173–67189, 67190–67194. None is in `USED_TEST_SEEDS` (67143–67149), none is 67150, none is val 67172. `test_seed_lists_disjoint_and_sized` passed inside the 21.

5. **PASS** — fresh 67190–67194. `R/r113_demos/logs/rec_lanes.log`: all five `rc=0` (23:45–23:47 CDT) then `ALL_DONE`. Each `DEMO_SUMMARY.json`: `recorder` `postmortem_20261026/pm_record.py`, `steps` 20000, `eps` 0.1, `screen_format` RGB24. Scan file sha `764dbddc…` matches. I classified every line in those 30 files that contains `6719[0-9]`: 0 seed-field hits (end_step, n_in_seed counters, colormap decimals, `to-check=`, `range(67170, 67190)`, `67100 <= … <= 67199`). `test_data_pins_match` passed (full pin re-hash inside pytest).
   Log: `05_fresh_summaries.txt`, `05_scan_classify.txt`.

6. **PASS** — val 67172 is not in `TRAIN_SEEDS`. Constants `(EVAL_EVERY, MIN_STEPS, MAX_STEPS, PATIENCE, MIN_DELTA) == (1460, 14600, 58400, 5, 0.002)`. `test_fit_refuses_nondefault_real_args` passed.

7. **PASS** — fits A/B/C = 67140, 1130001, 1130002. Distinct. A equals T1's RNG seed. Spec §4 no longer claims all three sit outside env-seed ranges (DV-R279).

8. **PASS** — `median_fit_of` matches spec §5 (ii): median L/R, then lowest AUC among exact ties, then earliest id. Command 7:
   - `[A .90/.81, B .84/.81, C .90/.90]` → FAIL, `median_fit` B, `rule_ii` false
   - `[A .90/.70, B .84/.85, C .91/.85]` → FAIL, `median_fit` B
   - `[A .86/.81, B .84/.81, C .90/.81]` → FAIL, `median_fit` B
   `test_pass_rule_ties` passed (low-side, 3-way FAIL and PASS, high-side FAIL and PASS, no tie, exact AUC tie → A, input order). Bars inclusive, no rounding, missing fit = FAIL still covered by `test_pass_rule`. CSV columns match the spec (`test_csv_columns`). FAIL consequence (67150 burned, no re-score, BC/PPO blocked) is in spec §5.
   Log: `07_tiebreak.txt`.

9. **PASS** — executed refuses, all before any 67150 touch:
   - `run_r113.sh real` exit 1: `REFUSED preflight: ['no FROZEN file …']`. `R/r113` not created. Log: `05_guard_real.log`.
   - `$PY -B r113_score.py --root $R/r113` exit 1: `REFUSED scoring 67150: ['no FROZEN file …', 'fit A/B/C has no RESULT.json']`. Log: `05_guard_score.log`.
   - `$PY -B r113_record.py --seed 67150 --steps 20 --out /tmp/…` exit 1: `refused: recording 67150: [no FROZEN, not the sealed scoring, no seal marker]`. Output dir not created. Log: `05_guard_record.log`.
   - `pm_record.py --seed 67150` still `AssertionError` on `seed not in PC.RESERVED` before mkdir. Log: `05_guard_pm_record.log`.
   Unseen check is `Path.rglob("*67150*")` (same name set as `find -name '*67150*'`). `test_unseen_matches_find_any_depth` passed. Smoke path hardcodes 77149.

10. **PASS** (code read; not executed on 67150) — `r113_score.py` writes `SEAL_67150_STARTED.json` with `RC.jw` (mode `x`) before `record()`, and only in real mode. A later `score_refusals` sees the marker and refuses. Unit test `test_seal_marker_blocks_rescoring` passed.

11. **PASS** (code read) — `adequacy_counts` uses `probe_labels` / `box_bin` only. `r113_score.py` calls it before `load_state_dict` / `RC.metrics`. `STOP_ADEQUACY` exits before any fit is scored.

12. **PASS** — `RSS_CAP_MIB` 6144, `SWAP_CAP_MIB` 7168, `start_new_session=True`, `os.killpg` only on `self.kids`, `os.pread`, no `mmap_mode` in `r113_common.py`. `test_no_deletes_anywhere` passed. Preflight `live_conflicts` only reads `ps`. `test_memory_settings_present` passed.

13. **PASS** — `cd $C/r113 && $PY -B -m pytest -q -p no:cacheprovider tests/test_r113.py` → `21 passed in 32.23s`, exit 0. Log: `02_pytest.txt`.

14. **PASS** — `$C/r113/run_r113.sh smoke verify_smoke_rev2_20261027_002010` exit 0. `RUN_LOG.jsonl` ends `{"event": "done", "ok": true}` at 2026-10-27 00:20:40 CDT. Fits used train 67170/67171, val 67172, init 67140/1130001/1130002. Score test seed 77149, 1500 steps. Wrote CSV, VERDICT (FAIL, expected at 40 steps), WRITEUP headed SMOKE. 3-way L/R tie `0.47766323024054985`; `median_fit` B (lowest AUC 0.6443). Both `ended` events carry `peak_swap_mib` 4870 and `peak_tree_rss_mib` 65 / 28. No `*67150*` under the smoke tree. CSV sha `cfb25bdc…bf06`.
   Log: `14_smoke_stdout.log`, `14_verdict.json`, `14_scores.csv`, `14_ended.txt`. Tree: `R/r113_smoke/verify_smoke_rev2_20261027_002010/`.

15. **PASS** — `find $R -name '*67150*'` empty before smoke, after smoke, after the refuse checks, and after the RSS remeasure. `find $C -name '*67150*'` empty (FROZEN does not contain 67150 in its name). Logs: `06_find_before.txt`, `06_find_after_R.txt`, `06_find_final_R.txt`, `06_find_final_C.txt`.

16. **PASS** — DV-R261…R282 accepted. In particular: R263 reuses val 67172 (not a test seed, not in train, no path to 67150); R262 drops 67140/67142 as training data (67140 remains RNG only); R273 no RIG_OK (measured-need only; checked here); R269 report-only used-seed scores stay inside the fit and out of `verdict()`. R277 implements the Gate 8 fix. R278 matches `find -name`. R279/R280/R282 are the wording fixes from the prior notes.

17. **PASS** — timing artifacts re-read, not the cook's prose: `timing2_noeval_20261026` wall 103.8 s / 584 steps = 0.1777 s/step. `timing1_20261026` wall 197.1 s, `val_history` length 2 (eval_every 292); delta vs no-eval 93.3 s → 46.7 s/eval. Interval math (about 5.1 min, min about 1.1 h, cap about 3.7 h, expected 2–2.5 h) follows. RSS remeasured this round with `logs/RSS_PROBE_r1.13.py` (never 67150): one fit peak 599 MiB ru_maxrss on 480000 train frames + 20000 val frames; 3 fits ≈ 1797 MiB. Cook's earlier probe was 608 / 1825. Cap 6144. Swap at smoke 4870 MiB used, headroom 2298 MiB under 7168 (~2.2 GiB, DV-R280). 16 GiB RAM. Plausible. Not a spec-bug block.
   Log: `17_timing.txt`, `17_timing_evals.txt`, `17_rss_rerun.log`. New probe: `R/r113_smoke/rss_probe_20261027_0022/RSS_PROBE.json` sha `ebfa7dc9…1065`.

18. **PASS** — wrote `C/r113/FROZEN_r1.13.json` after the gates above. Fields: kind FROZEN, written_by Verify, verdict `PASS-with-notes`, spec_sha256 `c30174ec…9872`, code shas for all 11 `CODE_FILES`, test_seed 67150, train_seeds the 24 above, val_seed 67172. `r113_common.frozen_refusals()` returned `[]`. Did not launch `run_r113.sh real`.
   Log: `18_frozen_write.txt`.

## Notes

N1. Stray `C/r113/__pycache__/r113_common.cpython-312.pyc` (mtime 2026-10-27 00:10:16, 28386 bytes) is unpinned and not in `CODE_FILES`. My `-B` runs did not refresh it. Launcher sets `PYTHONDONTWRITEBYTECODE=1`. Left in place (no deletes).

N2. `ended` peak RSS/swap is the max of 15 s watchdog samples, not `ru_maxrss`. Smoke logged `peak_tree_rss_mib` 65. The cap check has the same grain (already in the spec). Independent peak is the probe in gate 17 (599 MiB / fit).

## DOGFOOD (Matt)

Not driven, neither PASS nor FAIL:

1. Real run. Verify did not start it. After this PASS-with-notes, RGL Lab (not Verify) starts it:
   `/Users/dude/rgl-proofs/GO-RGL-INTERP-1/scratch/rung_r3p5/r113/run_r113.sh real`
   Outputs `R/r113`. That command scores 67150 once. A FAIL burns 67150.

## Left running / on disk

Left running: nothing. No r113/vizdoom/pm_record/RSS probe process after the checks.

Left on disk:

- `C/r113/FROZEN_r1.13.json` (this review; required on PASS)
- `R/r113_smoke/verify_smoke_rev2_20261027_002010/` (this review's smoke; throwaway seeds only)
- `R/r113_smoke/rss_probe_20261027_0022/` (this review's RSS remeasure; never 67150)
- `/Users/dude/Orbitty GOs/verify_logs_RGL-r1.13-P0-seeds-rev2_8ee40916/`
- This report
- Cook artifacts already present: `R/r113_smoke/smoke1_20261026`, `smoke2_rev2_20261027_0015`, `timing1_20261026`, `timing2_noeval_20261026`, `rss_probe_20261027_0013`, and prior Verify smoke `verify_smoke_20261027_0007`
- Unpinned pyc noted in N1 (pre-existing)
- No `R/r113`. No `*67150*` under R or C. Refuse tmp dirs were not created.

## Result
PASS-with-notes
PASS tip: 8ee40916983b083684e963fad62a414d326e5407d1e4d65ad60f4ed7142db467
Fails:
DOGFOOD items:
- Real `run_r113.sh real` not started. RGL Lab launches it after this FROZEN. That scores 67150 once.
Fixes for Ship:
