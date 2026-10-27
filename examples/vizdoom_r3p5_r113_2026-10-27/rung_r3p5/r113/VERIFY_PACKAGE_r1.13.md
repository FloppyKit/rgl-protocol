# VERIFY PACKAGE r1.13 P0-SEEDS rev2: pre-registration re-review (rung_r3p5, KD05, GO-RGL-INTERP-1)

Prepared 2026-10-27 at about 12:20 AM CT (rev2, after Verify FAIL af4b1883) by the RGL Lab cook (Grok Bot) for Matt Brown. Previous package af4b188332d7fe9fedeeb40020dff8024f3a92998b97e3d89f1089e3411a9e7c is kept at C/r113/superseded/af4b1883/. clinical_claim: false. RGL proofs / micro-envs.
Basis: Matt, 2026-10-26 11:38 PM CT: "pre-register it for Verify".
State: nothing real has been trained or scored. **Seed 67150 is untouched** (`find R -name '*67150*'` returns nothing). The cook has written no FROZEN and no RIG_OK. Only Verify writes C/r113/FROZEN_r1.13.json, and only after PASS. After that, RGL Lab launches the run.
C = /Users/dude/rgl-proofs/GO-RGL-INTERP-1/scratch/rung_r3p5 · R = /Volumes/MiniHangar/rgl-artifacts/GO-RGL-INTERP-1/rung_r3p5_runs · PY = /Volumes/MiniHangar/rgl-envs/GO-RGL-INTERP-1.venv/bin/python

## Spec
C/RUNG_SPEC_r1.13_P0_SEEDS.md rev2 **sha256 c30174eccd46bc209fc7a36e77fb2492278d377727a2b3b2d15c764ca1189872** (supersedes rev1 e47e8b53…fd05 and the r1.13 card t454s2084)

## Files (sha256)
| file (relative to C) | sha256 | role |
|---|---|---|
| RUNG_SPEC_r1.13_P0_SEEDS.md | c30174eccd46bc209fc7a36e77fb2492278d377727a2b3b2d15c764ca1189872 | spec (rev2) |
| logs/DEVIATIONS_r1.13.md | 3498e5784bc5c5ffc87e1554621d71aadde4e7311ebfb56607b6f92edf3587bf | DV-R261…R282 |
| logs/SEED_SCAN_r1.13_67190_67199_hits.txt | 764dbddcf38c9cf9fdf1f535e3e0e45ed99f87bd7145742292dab0ef5ce1cf1d | raw rg hits for the fresh range |
| r113/r113_common.py | 23386dd334a944e73e0a874d898be145d6cbfd481a6717ea2ed2952a08b2d260 | constants, seeds, FROZEN guard, pins, pread data, early stop, pass rule |
| r113/r113_fit.py | a92fc451f28c9628351922207afdd87c440554ee98c3dce05fc32d086d0b99d8 | one fit |
| r113/r113_score.py | aa7acbf542a74b871f728d2881dfc3c6b7395a001dcf1f571b5798b079df042d | sealed 67150 scoring + CSV/verdict/writeup |
| r113/r113_run.py | bb46972c5b5b06870aa79d73535e77f60c0a25cd351f084afd68b56571933ad5 | orchestrator + watchdog |
| r113/run_r113.sh | 347064bebc30a29782f44c66b6926234618be171208ecfd5fccbd07813f79f5d | launcher (smoke TAG / real) |
| r113/r113_record.py | 0296de707f206dddefef2fb9bef13969a7837ab71c2e0cc36d0d6693fcb74d71 | cp -n of pm_record.py + 67150 guard (DV-R266) |
| r113/tests/test_r113.py | 90367936ba296a73cac708f730238345e74e3d17307f0ff5de2552880402489b | 21 gate tests |
| r113/DATA_PINS_r1.13.json | cdcc0053b647413c000599374359e4e1849c7b1c898b82da6898c68ffcddd64e | sha256 of every train/val demo file + per-seed counts |
| r113/record_fresh_r113.sh | 9f612477f34736721c1f434e5aab48fb18e97899e7f069a24eee145f3c82d850 | records 67190–67194 (already run, all rc=0) |
| postmortem_20261026/pm_record.py | c879dc8eddb6f21e6cc16aa0b888a4ae6a9e805819de02c2e85f2c0d441c6688 | unchanged recorder (still refuses 67150) |
| postmortem_20261026/pm_common.py | 03b28e2b6c17de0481c0d9a2ab0a51e174ea1d4397c297da14e51353f764ecc8 | unchanged (RESERVED = (67150,)) |
| logs/RSS_PROBE_r1.13.py | de3e74eda5630754d2fd233fe7113adc5ed50e88e11b3ea61d26eb437ad6545c | RSS evidence script (not run-path code; not in CODE_FILES; DV-R281) |
| r113/superseded/af4b1883/SHA256SUMS_af4b1883.txt | 500e1eda6a28844f80833d042b3c60d530e6748579dda9a05642ff0909b4cb05 | shas of the cp -n copies of every rev1 file |

Unchanged frozen imports used: r1_8/r18_learn.py (probe_labels, p0_metrics, box_bin), r1_9b/r19b_p0.py (ProbeNet2, HalfVisibleSampler, select_epoch), r1_12/r111_p0.py (LR/BATCH/HALF_VIS/MIRROR_P/MASK_PX, mirror_*, lr_weight), all the same files pm_t1_train.py imported.

## Key content (see the spec for full text)
- Train (24): 67170, 67171, 67173–67189, 67190–67194. Val: 67172. Test (sealed): 67150. Report-only (used): 67149, 67148, 67146.
- Early stop: val L/R gated by val AUC ≥ 0.85; eval every 1,460 steps; patience 5 evals; min_delta 0.002; minimum 14,600 steps; cap 58,400 steps; checkpoint = frozen select_epoch.
- Fits: A 67140, B 1,130,001, C 1,130,002 (in parallel, 3 threads each).
- PASS iff ≥ 2 of 3 fits clear AUC ≥ 0.85 AND L/R ≥ 0.80 on 67150, AND the median fit clears both, AND median AUC/L/R clear the bars. Median fit (rev2): among all fits whose L/R equals the median L/R exactly, the one with the LOWEST AUC (then earliest fit id). Otherwise FAIL, and 67150 is burned (no re-score).
- Resources: watchdog stops if tree RSS > 6,144 MiB or swap > 7,168 MiB. Measured on the real 24-seed data: 608 MiB per fit, so about 1.8 GiB for 3 (RSS_PROBE.json). Swap headroom about 2.2 GiB. Estimated wall about 2–2.5 h (min about 1.1 h, cap about 3.7 h).

## Exact commands for Verify
```bash
C=/Users/dude/rgl-proofs/GO-RGL-INTERP-1/scratch/rung_r3p5; PY=/Volumes/MiniHangar/rgl-envs/GO-RGL-INTERP-1.venv/bin/python
# 1. hashes
cd $C && shasum -a 256 logs/RSS_PROBE_r1.13.py r113/superseded/af4b1883/SHA256SUMS_af4b1883.txt RUNG_SPEC_r1.13_P0_SEEDS.md logs/DEVIATIONS_r1.13.md logs/SEED_SCAN_r1.13_67190_67199_hits.txt r113/r113_common.py r113/r113_fit.py r113/r113_score.py r113/r113_run.py r113/run_r113.sh r113/r113_record.py r113/tests/test_r113.py r113/DATA_PINS_r1.13.json r113/record_fresh_r113.sh postmortem_20261026/pm_record.py postmortem_20261026/pm_common.py
# 2. gates (engine-free, 21 tests, ~35 s; includes the full data-pin re-hash)
cd $C/r113 && $PY -B -m pytest -q -p no:cacheprovider tests/test_r113.py
# 3. recorder diff (only the guard + sys.path + docstring/recorder-name lines may differ)
diff $C/postmortem_20261026/pm_record.py $C/r113/r113_record.py
# 4. smoke under a NEW tag (~30 s; seeds 67170/67171/67172 + 77149 only; never 67150)
$C/r113/run_r113.sh smoke verify_smoke_$(date +%Y%m%d_%H%M)
#    then read R/r113_smoke/<tag>/score/{SCORES_r1.13.csv,VERDICT_r1.13.json,WRITEUP_r1.13.md} and logs/RUN_LOG.jsonl
#    (smoke fits tie 3-way on L/R; rev2 must report median_fit B = the lowest AUC)
# 7. tie-break repro (Verify af4b1883 cases; expect FAIL/B, FAIL/B, FAIL/B)
cd $C/r113 && $PY -B -c "import r113_common as RC; r=lambda f,a,l:{'fit_id':f,'auc':a,'lr_acc':l}; print(RC.verdict([r('A',.90,.81),r('B',.84,.81),r('C',.90,.90)])); print(RC.verdict([r('A',.90,.70),r('B',.84,.85),r('C',.91,.85)])); print(RC.verdict([r('A',.86,.81),r('B',.84,.81),r('C',.90,.81)]))"
# 5. guard checks (must REFUSE; neither touches 67150: both stop before any recording)
$C/r113/run_r113.sh real            # expect "REFUSED preflight: ['no FROZEN file ...']"
cd $C/r113 && $PY -B r113_score.py --root /Volumes/MiniHangar/rgl-artifacts/GO-RGL-INTERP-1/rung_r3p5_runs/r113   # expect "REFUSED scoring 67150: ['no FROZEN file ...', ...]"
# 6. 67150 still unseen (the same set the guard now checks: rglob any depth)
find /Volumes/MiniHangar/rgl-artifacts/GO-RGL-INTERP-1/rung_r3p5_runs -name '*67150*'   # expect nothing
```
Cook's own results, rev2 (2026-10-27 CDT):
- Gates: **21 passed** (32.3 s). New: `test_pass_rule_ties`, `test_unseen_matches_find_any_depth`.
- Tie-break repro (Verify's cases): low-side pair → FAIL, median_fit B; high-side pair → FAIL, median_fit B; 3-way tie → FAIL, median_fit B (rev1 gave PASS/A, FAIL/B, PASS/C).
- Smoke `R/r113_smoke/smoke2_rev2_20261027_0015` (12:15:01–12:15:31 AM CDT): fits 67170/67171, val 67172 (600 frames), test 77149 recorded for 1,500 steps. RUN_LOG ends "done" and the `ended` events now carry peak_swap_mib 4886 / peak_tree_rss_mib 59. VERDICT FAIL (expected at 40 steps). It had the 3-way L/R tie (0.47766…), and rev2 reports **median_fit B** (lowest AUC 0.644; rev1 and Verify's smoke reported C). CSV sha e2b5278a19769993331a1f3bd162341ba4481aaac5a1ba37918348d883f6ea5c.
- RSS probe `R/r113_smoke/rss_probe_20261027_0013/RSS_PROBE.json` (sha 03f2a205…1117): one fit on 24 seeds + full val peaked at 608 MiB; 3 fits ≈ 1,825 MiB.
- `find R -name '*67150*'` and `find C -name '*67150*'`: empty after all of the above.
- Note: `C/r113/__pycache__/r113_common.cpython-312.pyc` (00:10:16 CDT) predates this rev2 work and was not created by the cook's -B runs. It is not in CODE_FILES and was left in place (no deletes).

## Changes since af4b1883
- **Gate 8 fix (DV-R277).** `r113_common.verdict` now calls `median_fit_of`: m = median L/R; candidates = fits with L/R == m exactly; pick the lowest AUC, then the earliest id. This replaces `sorted(key=(lr, auc))[1]`. Spec §5 (ii) now states this rule word for word. `+test_pass_rule_ties` covers the low-side pair, 3-way tie (FAIL and PASS variants), high-side pair (both outcomes), no tie (both outcomes), exact AUC tie and input order.
- **N1 (DV-R278).** `test_seed_unseen_refusals` uses `rglob("*67150*")`, the same set as `find R -name '*67150*'` at any depth. Spec §5 (iv) reworded to match. `+test_unseen_matches_find_any_depth`.
- **N3/N4 (DV-R279).** DV-R266 prose now says the sys.path line inserts postmortem_20261026. Spec §4 RNG-seed sentence corrected (67140 is also an old r110 env seed).
- **N2 (DV-R280).** Swap headroom stated as about 2.2 GiB.
- **N5 (DV-R281).** Logged 24-seed RSS probe (608 MiB per fit). `r113_run.wait_all` logs peak swap and peak tree RSS in each `ended` event (r113_run.py: 5 lines).
- **DV-R282.** Spec §9 and checklist item 18: RGL Lab launches after a PASS, not Matt or Verify.
- Unchanged: seeds, recipe, early stopping, bars, CSV columns, guard logic other than the unseen glob, r113_fit.py, r113_score.py, r113_record.py, run_r113.sh, DATA_PINS, the recordings.
- Diff size against superseded/af4b1883: r113_common.py 22 changed lines, r113_run.py 5, tests 40, spec 25, deviations 12 (+6 rows).

## FROZEN file Verify writes on PASS (C/r113/FROZEN_r1.13.json; fields the guard requires)
`{"kind": "FROZEN", "written_by": "Verify", "verdict": "PASS" | "PASS-with-notes", "spec_sha256": "<sha of RUNG_SPEC_r1.13_P0_SEEDS.md>", "code": {<every CODE_FILES path relative to C>: "<sha256>"}, "test_seed": 67150, "train_seeds": [24 seeds in the order above], "val_seed": 67172}`.
CODE_FILES = r113/r113_common.py, r113/r113_fit.py, r113/r113_score.py, r113/r113_run.py, r113/run_r113.sh, r113/tests/test_r113.py, r113/DATA_PINS_r1.13.json, r113/r113_record.py, postmortem_20261026/pm_record.py, postmortem_20261026/pm_common.py, r113/record_fresh_r113.sh.

## Checklist for Verify (numbered)
1. Live shas of all 16 files above equal this package. Spec sha = c30174ec…9872. superseded/af4b1883 holds unedited rev1 copies matching the af4b1883 package.
2. The spec states that it supersedes the r1.13 card t454s2084. Its basis quote is Matt's "pre-register it for Verify" (11:38 PM CT, Oct 26).
3. The recipe is unchanged against postmortem `pm_t1_train.py`: same model, Adam 1e-3, batch 64 (32 vis + 32 any), mirror p 0.5 + label swap + 1-px mask, BCE vis+cen+L/R, select_epoch. The only differences are the seed list, early stopping, the RNG seed per fit and the report seeds. Compare r113_fit.py's training loop line by line with pm_t1_train.py.
4. There are ≥ 20 training seeds (24). Each is listed explicitly. None is in USED_TEST_SEEDS (67143–67149), none is 67150 and none is val 67172. Lists are disjoint (test_seed_lists_disjoint_and_sized).
5. Fresh seeds 67190–67194: registry accepted. Read the scan raw list and confirm no hit is a seed field. Each was recorded with the unchanged pm_record.py (DEMO_SUMMARY "recorder": postmortem_20261026/pm_record.py, 20,000 steps). DATA_PINS re-hash matches.
6. Val seed 67172 is separate. The early-stop rule (metric, interval 1,460, patience 5, min_delta 0.002, minimum 14,600, cap 58,400) is predeclared in the spec and equals the code constants. A real fit refuses non-default arguments.
7. There are 3 fits with distinct predeclared RNG seeds (67140, 1,130,001, 1,130,002).
8. The pass rule is as written (≥ 2 of 3, median fit passes, medians clear the bars, inclusive bars, raw floats, missing fit = fail). The median fit is exactly as defined in spec §5 (ii): the lowest AUC among all fits at the median L/R, then the earliest id. Code `median_fit_of` matches the text in every tie case. Run command 7 and `test_pass_rule_ties`. The CSV columns and outputs are predeclared. The FAIL consequence (67150 burned, no re-score, no goal-post change, BC/PPO blocked) is stated.
9. Guard: r113_score refuses 67150 without a valid FROZEN, refuses outside R/r113, refuses once the seal marker exists, and refuses if any file or dir whose name contains 67150 exists under R at any depth (the same set as `find R -name '*67150*'`). r113_record refuses 67150 before any mkdir or engine start unless FROZEN, the seal marker and R113_SEALED_SCORE=1 are all present. Smoke can never use 67150. The real run refuses to start without FROZEN.
10. The seal marker is written before 67150 is first touched. A crash after it means no retry.
11. Test-seed adequacy (DV-R267) uses labels only: 20k steps, extended to 30k/40k on the same seed, then STOP_ADEQUACY. It never reads model outputs before the decision.
12. Resources: RSS cap 6,144 MiB and swap cap 7,168 MiB in the watchdog; killpg only on its own children's new sessions; os.pread with no mmap; 3 threads per fit; no rm or delete anywhere (test_no_deletes_anywhere); preflight reads ps only.
13. Gates pass on your run (21/21).
14. Smoke under a new tag ends with "done", writes CSV, VERDICT and WRITEUP, and uses only 67170/67171/67172/77149. On the 3-way smoke L/R tie, median_fit is B (lowest AUC). The `ended` events carry peak swap/RSS.
15. `find R -name '*67150*'` is empty, both before and after your smoke.
16. DV-R261…R282 are acceptable; flag any you reject. In particular: reusing val 67172 (R263); excluding 67140/67142 (R262); no RIG_OK gate (R273); report-only used-seed scores inside the fits (R269).
17. The runtime estimate (about 2–2.5 h expected, about 3.7 h cap) and the memory plan (608 MiB per fit logged, about 1.8 GiB for 3, swap headroom about 2.2 GiB) are plausible on ElM4.
18. On PASS: write C/r113/FROZEN_r1.13.json with the fields above. Do not launch the run; RGL Lab launches it after the PASS.
