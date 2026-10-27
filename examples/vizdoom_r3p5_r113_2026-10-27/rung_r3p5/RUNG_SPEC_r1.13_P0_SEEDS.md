# RUNG SPEC r1.13 P0-SEEDS: rung_r3p5 P0 perception probe, more training seeds + early stopping. PRE-REGISTERED for Verify

Status: pre-registration for Verify, **rev2** (2026-10-27 ~12:15–12:40 AM CT). Not frozen. Nothing in this spec has been trained or scored. Seed 67150 is untouched. No RIG_OK. clinical_claim: false. No PHI. CPU only. RGL proofs / micro-envs (ViZDoom KD05).
Written 2026-10-26, about 11:40 PM to 12:10 AM CT, by the RGL Lab cook (Grok Bot) for Matt Brown.
**Basis (verbatim):** Matt, 2026-10-26 11:38 PM CT: "pre-register it for Verify".
**Supersedes rev1** (sha256 e47e8b533ea0d011be98504d9753033b142e252c026013787f405971a322fd05, Verify FAIL on Gate 8: ~/Orbitty GOs/VERIFY_RGL-r1.13-P0-seeds_af4b1883.md). rev1 is kept unedited at C/r113/superseded/af4b1883/. rev2 changes: the median-fit tie-break (§5, DV-R277), the 67150-unseen check (§5, DV-R278), RNG-seed wording (§4, DV-R279), swap/RSS numbers (§6, DV-R280/R281), launcher wording (§9, DV-R282). No change to seeds, recipe, early stopping, bars or outputs.
**Also supersedes:** the earlier r1.13 card t454s2084. That card was never built or run; this file replaces it in full. Where an older spec disagrees with this one, this one applies to r1.13.
**Evidence (read only, not edited):** R/postmortem_20261026/POSTMORTEM.md 1a2c5db0f7c59e410cb8ab25671a355ced8a29af3c48eccf25df8f591b81d8d0; R/postmortem_20261026/tables/H3_H5_fits.csv 49e1659e845d3b212ed629c595342cf7998faf333aa886850794581f2e930718; C/logs/DEVIATIONS_postmortem_20261026.md e0fd7f9f110acfcdba5ce5dfc0f50d9b5c3ba76b980cf47dcc22afa8e0db6fac; code C/postmortem_20261026/ (pm_t1_train.py = the recipe, pm_record.py = the recorder).
**Paths:** C = /Users/dude/rgl-proofs/GO-RGL-INTERP-1/scratch/rung_r3p5; R = /Volumes/MiniHangar/rgl-artifacts/GO-RGL-INTERP-1/rung_r3p5_runs. Code is in C/r113/. Deviations are in C/logs/DEVIATIONS_r1.13.md (DV-R261 to DV-R282). The Verify package is C/r113/VERIFY_PACKAGE_r1.13.md.

## 1. Hypothesis and the unchanged recipe
**H-SEEDS (primary; decides whether BC/PPO may start):** the unchanged T1 probe recipe, trained on 24 recorded demo seeds and early-stopped on a separate validation seed, meets the P0 bars on the fresh sealed seed **67150** under the §5 rule. The bars are visible AUC ≥ 0.85 AND left/right accuracy ≥ 0.80 on visible frames, computed by the frozen `r18_learn.p0_metrics`.
**Falsified if** the §5 verdict is FAIL. No near-miss rule, no subset, no re-score and no bar change can turn a FAIL into a PASS.
Why we expect it (post-mortem H3, one fit per arm, scored on used seed 67149): with the same recipe, going from 2 to 4, 8 and 16 training seeds took L/R from 0.705 to 0.708, 0.777 and 0.817, and AUC from 0.885 to 0.955. The 16-seed fit was still improving when its fixed 14,600-step budget ran out. Because 67149 is a used seed, that result is a report, not a pass.

**Recipe: identical to post-mortem `pm_t1_train.py`, which is the r111c T1 recipe, except for the two changes listed below.**
- Model: `r19b_p0.ProbeNet2((120,160), 3)`. RGB 120x160 input, the sealed c3 trunk, 3 linear heads (vis, L/R, cen).
- Optimiser: Adam, lr 1e-3 (`r111_p0.LR`). Batch 64 = 32 visible + 32 any frames (`HalfVisibleSampler`, `BATCH`, `HALF_VIS`).
- Augmentation: mirror with p 0.5, the left label swapped, and the L/R loss masked within 1 px of the mirror axis (`r111_p0.mirror_frames`, `mirror_left`, `lr_weight`, `MIRROR_P` 0.5, `MASK_PX` 1.0). All are imported unchanged.
- Loss: BCE(vis) + BCE(cen) + BCE(L/R) on visible frames with weight > 0. Labels come from `r18_learn.probe_labels`.
- Checkpoint choice: the frozen `r19b_p0.select_epoch` rule. It picks the highest validation L/R among evals with validation AUC ≥ 0.85, falls back to the highest validation L/R if no eval qualifies, and gives ties to the earlier eval.
- Frames are read with `os.pread` (post-mortem DV-PM07).

**The only two changes:** (a) the training-seed set (§2); (b) the stopping rule (§3). These replace the post-mortem's fixed 14,600 steps. The three repeat fits (§4) differ only in their RNG seed.

## 2. Training seeds (24; none of them has ever been a test seed)
`TRAIN_SEEDS` = **67170, 67171, 67173, 67174, 67175, 67176, 67177, 67178, 67179, 67180, 67181, 67182, 67183, 67184, 67185, 67186, 67187, 67188, 67189, 67190, 67191, 67192, 67193, 67194**.
- 67170–67189 except 67172 (19 seeds): recorded 2026-10-26 by the post-mortem recorder `pm_record.py` (DV-PM04). Each is 20,000 steps, eps 0.1, KD05, RGB.
- 67190–67194 (5 seeds): **recorded fresh for r1.13** on 2026-10-26 between 11:43 and 11:47 PM CDT. They used the same unchanged `pm_record.py` and settings (`C/r113/record_fresh_r113.sh`; outputs R/r113_demos/demos_rgb/). Only 19 usable non-test seeds existed, so fresh ones were needed (DV-R262). The range 67190–67199 was checked first:
  - registry: `diag.common.check_seeds` accepted all 10 seeds (real/dry/probe/spent/reserved_map all False);
  - word scan: `rg -lw` over the four standard roots found 30 files. None had a seed field: they were counters, decimals, wide-count tables, `range(67170, 67190)` and a `67100 <= … <= 67199` test bound. Raw list: C/logs/SEED_SCAN_r1.13_67190_67199_hits.txt 764dbddcf38c9cf9fdf1f535e3e0e45ed99f87bd7145742292dab0ef5ce1cf1d;
  - `find` for `*6719[0-9]*` under R: nothing.
  
  67195–67199 are still unused and are not reserved by this spec.
- No training seed is in `USED_TEST_SEEDS` = 67143, 67144, 67145, 67146, 67147, 67148, 67149. That list covers every seed ever used, or chosen and then excluded, as a P0/P0b/P0c scoring seed. None is 67150, none is the val seed and none is a report seed.
- Size: 480,000 frames, of which 100,061 are visible. Per-seed visible counts run from 3,059 to 5,417, and every seed passes the r1.12 adequacy floors (see DATA_PINS counts). The 16-seed H3 arm had 68,042 visible frames. Seed count and frame count still rise together (DV-R276).
- Data pins: every .npz/.npy/.json in the 24 training dirs and the val dir is sha256-pinned in C/r113/DATA_PINS_r1.13.json. The real run refuses to start if any pin differs.
- 67140/67142 (r110 recordings) are not used (DV-R262).

## 3. Validation seed and the early-stopping rule (predeclared)
- `VAL_SEED` = **67172**: 20,000 steps, 4,950 visible frames. It is used only for early stopping and checkpoint choice. It is not a training seed, not 67150 and has never been a test seed. It was the H3/H5 validation seed (DV-R263).
- **Metric:** validation L/R accuracy on all visible 67172 frames, gated by validation visible AUC ≥ 0.85, the same as `select_epoch`.
- **Eval interval:** every 1,460 Adam steps. This is the H3 interval and one T1 epoch on the r111c split.
- **Improvement:** an eval counts as an improvement if it is the first eval with validation AUC ≥ 0.85, or if it is in the same AUC class as the best eval so far and its validation L/R ≥ best L/R + **0.002** (`MIN_DELTA`).
- **Patience:** stop after **5** consecutive evals (7,300 steps) without an improvement, and only once step ≥ **14,600** (`MIN_STEPS`). No fit stops before the H3 budget.
- **Max step cap:** **58,400** steps (40 evals). That is 4x the H3 budget and 2x r111c T1's 29,200 steps. Reaching the cap ends the fit with stop_reason "max_steps".
- **Checkpoint used for scoring:** the `select_epoch` choice over the full validation history, not the last eval. Stop reason, stop step, chosen step and the full history are written to each fit's RESULT.json.
- Code: `r113_common.es_update`, `es_should_stop`. A real fit refuses any non-default early-stopping argument.

## 4. Three repeat fits
Fits A, B and C share the same data, recipe and rule. Each fit's single RNG seed drives torch init, the batch sampler and the mirror RNG, as T1 did with 67140:
- **A = 67140** (T1's own seed)
- **B = 1,130,001**
- **C = 1,130,002**

These are RNG seeds only and are never used as env seeds in r1.13. A = 67140 is T1's RNG seed (67140 is also an old r110 demo env seed, which r1.13 does not train on); B and C are outside every env-seed range (DV-R265, DV-R279). The three fits run in parallel with 3 threads each. Each fit also scores **report-only** on the already-used seeds 67149, 67148 and 67146 after training and before 67150 is opened. Those scores are not part of the pass rule (DV-R269).

## 5. Sealed scoring on 67150 (once) and the pass rule
**When:** only after all three fits have finished with RESULT.json and checkpoints whose shas match, and only in real mode. `r113_score.py` refuses unless all of these hold:
- (i) Verify's FROZEN file C/r113/FROZEN_r1.13.json exists with kind "FROZEN", written_by "Verify" and verdict PASS or PASS-with-notes. Its spec_sha256 must equal this file's live sha, its code shas must equal every live file in `CODE_FILES`, and its test_seed, train_seeds and val_seed must equal the code constants;
- (ii) the root is R/r113;
- (iii) no seal marker exists;
- (iv) no file or dir whose name contains 67150 exists anywhere under R, at any depth (the same set as `find R -name '*67150*'`; DV-R278).

The recorder copy `r113_record.py` refuses 67150 on its own unless FROZEN is valid, the seal marker exists and the env flag for sealed scoring is set.
**How:**
1. Write `R/r113/score/SEAL_67150_STARTED.json` (mode x) before 67150 is first touched.
2. Record 67150 with the unchanged recorder loop: 20,000 steps, eps 0.1, KD05, RGB, the same as every training seed.
3. Run the label-only adequacy floors: visible ≥ 3,000; left fraction in [0.40, 0.60]; small ≥ 1,000 and large ≥ 1,000; no episode floor (r1.12). If any floor fails, re-record the same seed at 30,000 and then 40,000 steps into new dirs. These checks use labels only and no model output (DV-R267). If 40,000 steps still fail: VERDICT STOP_ADEQUACY, no fit is scored, and Matt decides.
4. Score each fit's chosen checkpoint on all 67150 frames, once, with `r18_learn.p0_metrics` (raw floats, no rounding).

**Per-fit pass:** visible AUC ≥ 0.85 AND L/R ≥ 0.80.
**Run PASS rule (all three must hold; otherwise FAIL):**
- (i) at least 2 of the 3 fits pass;
- (ii) the **median fit** passes. Definition (exact): let m = the median of the three 67150 L/R values. Every fit whose 67150 L/R equals m exactly is a candidate. The median fit is the candidate with the **lowest** 67150 AUC; if candidates also tie exactly on AUC, the earliest fit id (A, then B, then C). This one rule covers no tie (one candidate), a low-side pair, a high-side pair and a 3-way tie (`r113_common.median_fit_of`; DV-R277);
- (iii) median AUC ≥ 0.85 and median L/R ≥ 0.80 across the three fits.

A fit that is missing or unscored counts as failed, and fewer than 3 scored fits means FAIL. All three fits are reported whatever the verdict (DV-R268).

**Reported:**
- `R/r113/score/SCORES_r1.13.csv`, one row per fit, with columns: run_tag, mode, fit_id, init_seed, n_train_seeds, val_seed, stop_reason, stop_step, chosen_step, val_auc_chosen, val_lr_chosen, test_seed, test_steps_recorded, n_frames, n_visible, auc, lr_acc, centred_auc, lr_small, n_small, lr_large, n_large, lr_offcentre9, n_offcentre9, fit_pass, model_sha256;
- `VERDICT_r1.13.json`: verdict, n_pass, median_fit, median_auc, median_lr, rule_i/ii/iii, bars, csv sha, clinical_claim false;
- `ADEQUACY.json`;
- `PRED_67150_<fit>.npz` (per-frame logits);
- `WRITEUP_r1.13.md`, a short table plus the verdict;
- each fit's RESULT.json, including the report-only 67149/67148/67146 scores.

The small/large/off-centre columns are report-only.
**On PASS:** BC/PPO may proceed, each under its own spec.
**On FAIL:** 67150 is burned. There is no re-scoring on 67150, no change to the bars, rule, subset or metric, no other checkpoint and no new fit scored on 67150. Any next step needs a new pre-registration, a new fresh seed and Verify. BC/PPO stay blocked.
**Crash or stop after the seal marker:** no automatic retry. 67150 counts as opened, and Matt decides, with a new DV if anything is rerun.

## 6. Resource plan
- RGL process tree ≤ ~6 GB. The orchestrator `r113_run.py` checks every 15 s and stops its own process groups (SIGTERM, then SIGKILL after 30 s) if the r1.13 tree RSS goes over **6,144 MiB** or system swap used goes over **7,168 MiB**. It then writes logs/STOP_WATCHDOG_*.json. A stop during the fits means no scoring and 67150 untouched; a relaunch needs Matt's word and a DV, because the run needs a fresh root.
- Measured (logged): one fit process on the real 24-seed training set + full 67172 val (load, 100 T1 steps, one full val eval) peaked at **608 MiB** ru_maxrss (R/r113_smoke/rss_probe_*/RSS_PROBE.json; DV-R281), so 3 parallel fits ≈ **1.8 GiB**. The score phase adds one ViZDoom recorder (about 400 MB). The orchestrator now logs peak swap and peak tree RSS at the end of each phase. System swap used by other processes was 3.8–4.95 GiB in the last day (4,950 MiB at Verify's smoke), so headroom under the 7,168 MiB cap is about **2.2 GiB** (DV-R280); swap growth from the run itself is expected to be small (tree ≈ 2.2 GiB of 16 GiB RAM), and the watchdog stops the fits before any scoring if the cap is hit.
- Frames are read with `os.pread`. The npy header is parsed with `np.lib.format`, so there is no mmap at all (DV-R270). Threads: OMP/MKL 3 and torch 3 per fit, so 9 of the 10 cores. CPU only. MiniHangar must have at least 40 GiB free at launch (it had 1.6 TiB free).
- Preflight refuses if any other rung/recorder/ViZDoom process is live, but never signals one. It only reads `ps`.
- **Estimated wall time** (measured: 0.178 s per Adam step and about 47 s per 20k-frame validation eval, with 3 fits in parallel):
  - per 1,460-step eval interval: about 5.1 min;
  - each fit: at least 10 intervals (about 51 min) and at most 40 (about 3.4 h);
  - report-only scoring: about 2.5 min;
  - score phase: about 8 min, or up to about 25 min if 67150 needs to be extended.
  
  **Total: about 1.1 h minimum and about 3.7 h at the cap. The expected total is about 2–2.5 h**, if fits stop after about 20–25 evals, as the n16 curve suggests.

## 7. Deviations
DV-R261 … DV-R282 are in C/logs/DEVIATIONS_r1.13.md and are part of this spec.

## 8. Code, gates and smoke
- Code (C/r113/):
  - `r113_common.py`: constants, guards, data, early stopping, pass rule;
  - `r113_fit.py`: one fit;
  - `r113_score.py`: the sealed scoring;
  - `r113_record.py`: a cp -n of pm_record.py plus the 67150 guard;
  - `r113_run.py`: orchestrator and watchdog;
  - `run_r113.sh`: launcher;
  - `record_fresh_r113.sh`: the 67190–67194 recording;
  - `DATA_PINS_r1.13.json`;
  - `tests/test_r113.py`.
- Gates (`tests/test_r113.py`, engine-free, 21 tests) cover:
  - seed lists are disjoint and the training list has 24 seeds (≥ 20); 67150 is not in train, val, report or smoke;
  - no used test seed is in train or val; data pins match; the fresh seeds pass the registry;
  - the FROZEN guard refuses a missing file and refuses each tampered field or file; the score guard refuses in real and smoke mode; the seal marker blocks re-scoring; the unseen check matches `find R -name '*67150*'` at any depth, including depth 1;
  - the recorder guard comes before any mkdir or engine start and refuses without the seal;
  - a real fit refuses non-default early-stopping arguments;
  - the memory settings are present; the code contains no delete calls;
  - the recipe and bars equal the frozen constants; early stopping and the pass rule behave as specified, including inclusive bars, no rounding, a median fit that fails, and every tie case (low-side pair, high-side pair, 3-way, exact AUC tie, input order); the CSV columns are as listed.
- Smoke (already-used or throwaway seeds only, never 67150): `run_r113.sh smoke <TAG>` trains on 67170 and 67171, validates on the first 600 frames of 67172, and runs 40 steps with an eval every 10. It then records the r1.12 smoke seed 77149 for 1,500 steps into R/r113_smoke/<TAG> and scores it, producing the CSV, verdict and writeup marked SMOKE.

## 9. Order of operations
1. Verify reviews this spec and package, then runs the gates and a smoke under a new tag.
2. If Verify passes, Verify writes C/r113/FROZEN_r1.13.json. The cook never writes FROZEN or RIG_OK.
3. After a Verify PASS and FROZEN, RGL Lab (the cook) launches the run with `run_r113.sh real`. Verify does not launch it.
4. The fits run, then the val early stop, then one sealed 67150 scoring, then the CSV and writeup.

Nothing here launches the real run.
