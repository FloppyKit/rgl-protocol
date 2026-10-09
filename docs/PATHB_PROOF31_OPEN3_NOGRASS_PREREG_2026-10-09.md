# PREREG — GO-RGL-PATHB-PROOF-31

Frozen RGL v1 on `predator_prey__open_3` (W1). The locked no-grass variant (W2) was dropped by its pre-stated feasibility gate (F4 failed), so P31 runs W1 only.

clinical_claim: false. Proof / micro-env / model. CPU/headless. No PHI. This document does not claim that a model has feelings. Route names are machine option labels. Inverse, null, and inconclusive results are published with the same prominence as wins. No soft goalposts. No confirmatory seed has been run.

## Spec binding

- RGL spec v1, `RGL-SPEC-v1/RGL_SPEC_v1.md`, frozen 2026-10-08 18:06 CT, sha256 `e620509377516858d1d1e3677a14f977c76549608e93702dc5dc7a5735487475`. Test T1 re-checks the digest and every section-3 source sha. P31 does not edit the spec.
- RGL v2 pre-statement, `RGL-SPEC-v2-PRESTATEMENT/V2_PRESTATEMENT.md`, frozen 2026-10-09 07:58 CT, sha256 `32b70b13a7cfd64cb836e84aa4be1072ded796e381f4c97a5cc085ce1cd4e13d`. It is cited, not used. P31 is a v1 study.
- GO: `GO.md` (GREENLIT 2026-10-09 07:58 CT), sha256 listed below.
- No retune (spec prediction e). No constant in spec sections 5–8 changes.

## Approval

At 2026-10-09 07:58 CT Matt selected a pre-written option worded by RGL Lab, reading exactly: "yes, greenlight P31 with your defaults and freeze the v2 pre-statement". The choice is Matt's; the wording is RGL Lab's. Approved defaults, binding here:

1. W1 and W2 greenlit as drafted, with W2 as a sha-locked config override behind the F1–F5 feasibility gate and the W1-only fallback.
2. `heuristic_retuned` OFF. `heuristic_noaffect` is config 18 unchanged. Seeds 32600–32699 stay unused.
3. H3 non-inferiority margin 0.10, with the UNINFORMATIVE label if `flight_forced` primary success ≤ 0.05. (Moot after the W2 drop; recorded.)
4. Band (0.05, 0.90).
5. H4 inside the Holm family (one-sided Welch on the episode count).
6. W2 `rgl_v1` vs `shuffled_map` descriptive only (moot after the W2 drop).
7. W2 `random_mix` and W2 `heuristic_noaffect` kept (moot after the W2 drop).
8. Seed blocks as drafted.

## Feasibility result for W2 and the fallback

Pre-stated in GO.md ("Phase A feasibility check for W2"). Run 2026-10-09 08:51–08:59 CT through the free-rig waiter (two FREE polls 300 s apart, 8 workers), seeds 32900–32929, arms `rgl_v1` (outcome-free, allow-list writer), `flight_forced`, `heuristic_noaffect`, `random_mix`; 120 episodes, `EXIT:0`, 455.5 s. Report: `FEASIBILITY.md`, `results/feasibility/feasibility.json`.

- F1 PASS. 120/120 episodes, 0 fatal, 0 reruns.
- F2 PASS. Grass tiles at reset 0, `max_forest_access` 0.0 and on-grass steps 0 on every episode. `rgl_v1` flight count 0 on all 30 episodes.
- F3 PASS. Mean `ally_prey_eaten` per episode: `heuristic_noaffect` 43.07, `random_mix` 42.73 (`flight_forced` 42.90). Baseline focal food sum 557.
- F4 FAIL. Primary success `heuristic_noaffect` 0/30 = 0.000, `random_mix` 0/30 = 0.000 (rule: at least one above 0.05). Without grass, the focal prey was eaten 3–6 times per baseline episode (median 4; `times_eaten` ≤ 2 in 0 of 60), although it foraged.
- F5 PASS (route shares only; no `rgl_v1` outcome was written or computed). Pooled `rgl_v1` shares: love 0.8205, fight 0.1783, capitulate 0.0012, flight 0, freeze 0, laugh 0.

Fallback applied as written (`FEASIBILITY_FAIL.md`): W2 is dropped from P31. P31 runs W1 only (H1, H2, H4, band). H3 / prediction (c) is deferred to a later GO (the GO's candidate is MPE2 simple_tag prey role with curriculum slow prey, which needs Matt's port ruling). No W2 seed outside 32900–32929 has been or will be touched. 33000–33566 stay unused. The W2 derangement file was not drawn. In code, `src/p31_frozen.py` sets `W2_DROPPED = True`, `src/p31_fit.py` then builds no W2 Phase B task and refuses W2 confirmatory seeds, and the analysis runs with `--drop-w2`. This is a failed world, not a retune.

## World (W1)

dm-meltingpot 2.4.1, scenario `predator_prey__open_3`, substrate `predator_prey__open`, focal prey in slot 0, 9 background prey slots (bots from `basic_prey_0/1/2`) and 3 predator slots (bots from `basic_predator_0/1`), 1000-step episodes. The substrate is built with its debug position/orientation observers enabled (observation only), as in P30 and the screen. Melting Pot is not seed-reproducible, so all comparisons are unpaired. Seeds are bookkeeping.

## Arms (W1), n = 567 each, 2835 episodes

- `rgl_v1`. `BalancedRGLGrid("balanced_rgl")`, `rgl.choose(rgl.scores(feats))`, imported unchanged from P30 `src/mp_fit.py` (sha256 `3250c743e9ea496eba712ba1e91e84d7fb7ea5257c579e3df41e7a70e206b007`). Tie order fight > flight > freeze > capitulate > laugh > love within 1e-12.
- `shuffled_map`. Same features, scores, `choose`, and tie order. The winning label r is executed with the mapper of pi(r). P30 D0–D3 (F = {fight, flight, love}, S = {freeze, capitulate, laugh}, forward/backward cycles). Assignment: seeds 32000–32566 ascending, labels 142×D0, 142×D1, 142×D2, 141×D3, `numpy.random.default_rng(31031).shuffle`. File `results/derangements_p31_open3.json`, canonical-JSON sha256 `bfa5bc139a03d218522c6c4e8a0af50ec607809cd949d3e2e0d5b25cd767187f`.
- `heuristic_noaffect`. P30 locked config_id 18: d = 6 Euclidean, straight-away flee, commit_k 0. `results/heuristic_locked_p30.json` sha256 `f50c7340ed7a24784b108920d5c4db3f623bbda9a51aa04661d5e1224eea6a5a`. Not tuned on open_3.
- `random_mix`. P27 frozen shares, `src/mix_shares.py` sha256 `157a9bac5089f86d95b34dc067ad62c4ef00c6cb0cceb00509da41ed122a65e3`. Descriptive.
- `love_noally`. Ablation for H4. Identical to `rgl_v1` except that the love mapper skips the ally branch: the line `if not skip_ally and ally_xy is not None and ally_risk > 0.75` (step toward the ally) is not taken, and love goes to the acorn/food branches. Scores, features, `choose`, and every other mapper line are unchanged (T15). A non-balanced arm under spec section 11, like `random_mix`.

Phase B interleaves the five arms round-robin by seed. 8 workers.

## Primary success

From the world's design, locked since P26. Prey: `food_1000 >= 1` AND `times_eaten <= 2`.

## Hypotheses (locked)

One family. Holm step-down, monotone, family alpha 0.05, three tests (W2 dropped): first step 0.05/3, then 0.05/2, then 0.05.

- H1 (prediction f). `p(rgl_v1) > p(shuffled_map)`. One-sided Fisher exact.
- H2 (prediction e). Superiority, `p(rgl_v1) > p(heuristic_noaffect config 18)`. One-sided Fisher exact. P30 H2 failed inverse (0.199 vs 0.263, interval −0.111 to −0.014). The plain rule scored 0.667 (20/30) in the open_3 screen. H2 is at real risk.
- H3 (prediction c, W2). Dropped with W2 by the pre-stated F4 fallback. Not tested in P31. Deferred to a later GO.
- H4 (prediction d, ally-protect branch). Mean `ally_prey_eaten` per episode, `love_noally` > `rgl_v1`. One-sided Welch t-test on episode counts. Its p-value enters Holm.

Band check (gate, not in Holm). `rgl_v1` primary success on W1 strictly above 0.05 and strictly below 0.90. Out of band makes H1, H2, and H4 exploratory; they are still reported in full. The band was set before any RGL success number existed for open_3.

Descriptive, outside Holm (one-sided Fisher, no adjustment): `rgl_v1` vs `random_mix`; `heuristic_noaffect` vs `shuffled_map`; per-derangement shuffled success; `love_noally` vs `rgl_v1` primary success.

Every risk difference gets a two-sided 95% unpaired percentile bootstrap interval (10,000 resamples) and Cohen's h (arcsine formula, arm minus baseline). Generator seeds:

- W1 risk differences, seed `34100 + index`: H1 = 0, H2 = 1, rgl vs random_mix = 2, heuristic vs shuffled = 3, D0–D3 minus rgl = 4, 5, 6, 7, love_noally vs rgl primary = 8.
- H4 mean difference, seed `34300`.
- Per-arm rate intervals: seed `34140 + arm_index` in arm order rgl_v1, shuffled_map, heuristic_noaffect, random_mix, love_noally.
- The W2 seeds (34200+, 34240+) are unused after the drop.

## Interpretation, pre-stated

The WRITEUP pastes the matching sentence. Each sentence has both clauses. "The manipulation check" means the check in the next section for that arm. A miss is written under Limitations. It does not change, exclude, or relabel any H. The 80% MDE is a fact about power, never a rescue. With the W1-only family the first Holm step is 0.05/3; at that alpha and n = 567 the superiority 80% MDE is 0.090 at bases 0.50 and 0.667 (`power.log`; 0.095 at the GO's four-test alpha 0.0125).

- H1 survives Holm. If the manipulation check passed, RGL beat a state-reactive controller with the same features, the same scores, and the same action repertoire, whose trigger-to-action pairing had been deranged, on open_3. If the manipulation check missed, H1 survived Holm and the shuffled-map check failed, so this is not read as evidence that the pairing did the work.
- H1 does not survive Holm, point estimate above 0. If the manipulation check passed, the map is not what raised success on open_3 at this n. The next sentence states the 80% MDE 0.090. If the manipulation check missed, H1 did not survive Holm and the shuffled-map check failed, so that sentence about the map does not apply.
- H1 point estimate at or below 0, interval wholly below 0. If the manipulation check passed, this is an inverse result: the deranged map beat RGL on open_3. If the manipulation check missed, the H1 interval lies wholly below 0 and the shuffled-map check failed, so the inverse sentence does not apply.
- H1 point estimate at or below 0, interval includes 0. Use the does-not-survive sentence, and add: the point estimate does not favor RGL. Both manipulation clauses still apply.
- H2 survives Holm. If the manipulation check passed, RGL beat the locked plain rule (config 18, not retuned on open_3). If the manipulation check missed, H2 survived Holm and the heuristic check failed, so this is not read as evidence that the route structure beat a working plain rule.
- H2 does not survive Holm, point estimate above 0. If the manipulation check passed, the route structure adds nothing over the locked plain rule on open_3 at this n. The next sentence states the 80% MDE 0.090. H2's power is the issue only if the gap is under about 0.09. If the manipulation check missed, H2 did not survive Holm and the heuristic check failed, so that sentence does not apply.
- H2 interval wholly below 0. If the manipulation check passed, this is an inverse result: the plain rule beat RGL on open_3, the same direction as P30. If the manipulation check missed, the H2 interval lies wholly below 0 and the heuristic check failed, so the inverse sentence does not apply.
- H2 point estimate at or below 0, interval includes 0. Use the H2 does-not-survive sentence, and add: the point estimate does not favor RGL. Both manipulation clauses still apply.
- H3. Not tested: W2 was dropped by the pre-stated F4 feasibility fallback (baselines floored at 0/30 without grass). The WRITEUP states this and that prediction (c) is deferred to a later GO. No H3 sentence is pasted.
- H4 survives Holm (branch cost shown). If the manipulation check passed, skipping the ally line cost more allies eaten. If the manipulation check missed, H4 survived Holm and the ablation check failed, so this is not read as evidence that the ally line protected allies.
- H4 does not survive Holm, point estimate in the predicted direction. If the manipulation check passed, a cost of the ally branch is not shown at this n. The next sentence states the H4 80% MDE: 0.395 allies/episode at SD 2.24, 0.456 at SD 2.58 (alpha 0.05/3). If the manipulation check missed, that sentence does not apply.
- H4 inverse (`love_noally` loses fewer allies; interval wholly on that side). If the manipulation check passed, the branch does not protect. That counts against (d). If the manipulation check missed, the inverse sentence does not apply.
- H4 point estimate at or below 0 and the interval includes 0. Use the does-not-survive sentence, and add: the point estimate does not favor the ally branch. Both manipulation clauses still apply.
- Band, W1 inside (0.05, 0.90) (W2 dropped). If the manipulation checks passed, H1, H2, and H4 stay confirmatory. If a manipulation check missed, the band label still stands and the missed check is a limitation, not a relabel.
- Band, W1 outside (0.05, 0.90). Label OUT-OF-BAND. H1, H2, and H4 are exploratory and are still reported in full. If the manipulation check missed, say that too. The band was set before any RGL success number existed.

## Manipulation checks

Descriptive. A miss goes to Limitations. It does not relabel any H.

- Shuffled: executed route ≠ trigger label on every alive step (fraction exactly 1.0). TV distance between shuffled executed shares and `rgl_v1` shares ≥ 0.10.
- `rgl_v1` pooled shares within ±0.05 of the screen means (fight 0.1197, flight 0.1513, love 0.7290; others 0). Screen n = 30, so this is a loose sanity bar.
- Heuristic: flee fraction strictly between 0.05 and 0.95.
- `love_noally`: ally-branch count exactly 0 on every alive step. Its route on each step is the `rgl_v1` choice for that step's features (same scorer; T15). Its pooled route shares are within ±0.05 of `rgl_v1` pooled shares (a loose bar; states drift).

## Power

`power.log` (from `src/power.py`; exact one-sided Fisher by hypergeometric enumeration; n = 567/arm). Superiority 80% MDE at the W1-only first Holm step 0.05/3: base 0.20: 0.070; 0.30: 0.080; 0.40: 0.090; 0.50: 0.090; 0.60: 0.090; 0.667: 0.090; 0.75: 0.085. At 0.0125 (the GO's four-test step): 0.095 at bases 0.50–0.667. Example power at base 0.667, alpha 0.05/3: d = 0.08, 0.727; d = 0.10, 0.901. H4 80% MDE (normal approximation): 0.395 allies/episode at SD 2.24, 0.456 at SD 2.583 (alpha 0.05/3). H1 against a shuffled rate near P30's 0.016 is very likely well powered.

## Seeds

- Confirmatory W1: 32000–32566 (the only Phase B seeds).
- W2 confirmatory 33000–33566: unused (W2 dropped).
- W2 feasibility: 32900–32929, used in Phase A, burned, never confirmatory. 32930–32999 reserved, unused.
- 32600–32699 (W1 tuning) and 33600–33699 (W2 tuning): reserved, unused.
- Scratch: 100–102 (smokes and replay tests).
- Burned, refused for every role: 24000–24999, 26000–26099, 27000–27249, 28000–28199, 29000–29566, 30000–30566, 30900–30999, 31000–31566, 31600–31699, 40000–40099, 98000–98999.

Proof of unused: `logs/seed_scan_draft.log` (2026-10-09 07:29 CT; 265 CSVs, 140 with a seed column, zero integer cells in 32000–33999) and test T13 at freeze (no integer cell in 32000–33999 outside this folder).

## Analysis and reruns

`src/analyze_p31.py` (sha256 below), run as `python -m src.analyze_p31 --episodes results/episodes.csv --traces results/traces.csv --role confirmatory --drop-w2`. It fails loudly (non-zero exit, no output) on a duplicate (arm, seed), an unknown arm or world, a W2 row, a blank or non-integer seed, a seed outside 32000–32566, a missing `rerun` column, a `rerun` other than 0 or 1, or any missing (arm, seed) episode. Nothing is re-estimated from confirmatory outcomes.

`src/p31_fit.py` writes `rerun` (0 or 1) on every row. If an episode raises, the worker retries once with the same arm and seed and marks `rerun = 1`. A second failure is fatal: the run aborts, BLOCKED.md. No extra seeds. No exclusions. Each finished episode is also appended (fsync) to `results/checkpoint_phaseB.jsonl`, so a crash loses only episodes in flight and a restart resumes the same task list; `results/episodes.csv` and `results/traces.csv` are written at the end.

A guard refuses any confirmatory seed unless `P31_PHASE_B=1` is set and `PREREG_PUBLISHED.txt` exists, refuses burned and reserved blocks, and refuses W2 confirmatory seeds while `W2_DROPPED` is true.

## Free-rig rule and launcher

All heavy work runs behind `logs/wait_for_free_rig.sh`: two consecutive FREE polls 300 s apart. FREE = no process named exactly xcodebuild, swift-build, swiftc, swift-frontend, clang, clang++ (escaped `clang\+\+`), cargo, or rustc (`pgrep -x`); no other RGL run (`pgrep -f 'src\.(mp_fit|p31_fit|screen_mp)'`); load5 below hw.ncpu/2 (10/2 = 5). Never kill, pause, or renice anything. No bypass. The waiter and launcher argv never contain the episode module name (`logs/run_B.sh` holds it), so the waiter does not count itself as busy (P30 lesson).

Phase B: `tmux new-session -d -s p31-B "logs/wait_for_free_rig.sh logs/launch_B.sh"`. `logs/launch_B.sh` refuses unless STATUS is READY_FOR_HASH_PUBLISH and `PREREG_PUBLISHED.txt` has a commit line, re-checks the rig, verifies `verify-logs/writeup_gate.py` (copied from P28, sha256 `629eb12f4b73e18ad197ba7d8b2537b5eccaef958bf9ed2675ab5446927e0f83`; never opened or quoted), runs `logs/run_B.sh` (which appends `EXIT:<rc>` to `logs/run.log`), and only after that EXIT line: boots out the check-in LaunchAgent (it appends inside the tree), deletes `__pycache__`, writes `SHA256_MANIFEST.txt` (every file except `.venv`, `__pycache__`, and the manifest; `LC_ALL=C sort`; `shasum -a 256`), runs `shasum -a 256 -c`, records the result in `/Users/dude/rgl-proofs/nest/manifest_checks/P31_B.txt`, and stops the P31 caffeinate (logged outside the tree). Progress goes to `logs/progress.log` every 25 episodes (N/total and per arm, CT timestamp) and the first line of `STATUS.md`.

A separator-agnostic banned-token grep (`verify-logs/banned_token_grep.py`; lower-cases and strips every non-alphanumeric character; tokens built at runtime) runs over every authored file before hash and before seal. It refers to them only as the two banned Proof-5 ceiling tokens. Raw agent streams that trip it are moved unedited to `/Users/dude/rgl-proofs/_agent-logs/P31/` with sha before and after.

## Disclosures and deviations

- W2 dropped by the pre-stated F4 fallback (above). The design shrinks from 10 arms / 5670 episodes to 5 arms / 2835 episodes and from a four-test to a three-test Holm family, both exactly as the GO pre-stated for a W2 drop.
- The GO's Phase A step 1 named copying the screen runner `P31-SCREEN-2026-10-09/src/screen_mp.py`. It was not copied. `src/p31_fit.py` is a fork of P30 `src/mp_fit.py` that imports `BalancedRGLGrid` and the grid helpers from the byte-identical P30 copy; T2 and T12 bind it to P30/P28 balanced.
- T12 was run on scratch seeds 100, 101, 102 on W1 (and 100 on W2) against P30's `rgl_v1` path by action-shadow replay, for 1000 steps each.
- RGL Lab review edits after the A1 agent (pre-edit copies in `logs/pre-edit/`): per-episode checkpoint in `src/p31_fit.py`; the `W2_DROPPED` switch in `src/p31_frozen.py` and `src/p31_fit.py`; alpha 0.05/3 added to `src/power.py`'s printed table. Tests re-run to `EXIT:0` after each.
- Scratch `shuffled_map` smokes on seeds 100–101 use D0 from the sha-checked file (the frozen assignment labels only 32000–32566).
- The F3 background-food check uses the summed focal `food_1000` on `heuristic_noaffect` and `random_mix` (the row schema has no separate background-prey food column).
- Melting Pot is not seed-reproducible; comparisons are unpaired. Config 18 was the best of 24 on orchard calibration (P30), so P30's maximum-over-configs inflation applies to its orchard rate, not to open_3. Screen seeds 40000–40099 are burned. Allies are pretrained bots. Spec section 13 limits apply (freeze, laugh, and capitulate barely fire; ambiguity ≡ 0).
- No RGL success number exists for open_3 or the no-grass variant at freeze. None was computed from screen or feasibility files.

## Tests at freeze

`verify-logs/test_p31.py`, last run in `verify-logs/tests.log` (from line 297): 56 PASS, 0 FAIL, final line `EXIT:0`. T7's nograss half is SKIPPED (W2 dropped). T1 spec and source digests, T2 `BalancedRGLGrid` text identical to P30 and P28, T3 `mix_shares`, T5/T6 heuristic, T7 open3 derangements, T8 seed guards, T9 rerun rule, T10 banned-token grep, T11 outcome-free writer, T12 action-identical replays, T13 seed scan, T14 nograss prefab sha, T15 `love_noally` one-line difference, T16 analyzer and feasibility probes, T17 waiter.

Banned-token grep at freeze: `verify-logs/banned_token_grep.py` over the tree (raw agent streams excluded and moved as stated), 0 hits.

## sha256

Computed 2026-10-09 09:10:58 CDT with `shasum -a 256`, paths relative to `GO-RGL-PATHB-PROOF-31/`.

```
a6a0f30c10639e11b56131e36036fe5dff9b682429145023dbe067643e5100fa  FEASIBILITY.md
ebf7f6a6a6a14e417f73197ccbfbf1013885c3db8f1131375bce9353fca02a9e  FEASIBILITY_FAIL.md
4c3ed197788c23f80947756e680fb4a3cb82d295b6617cbe46dd81e5a1e8505f  GO.md
34a6e6ebcaff0dfa4894fa81012165ed5a2ed8f1876b45d9f76800b3c85e9999  logs/build_prereg.sh
42471ae29b7ed13c85219bed63b496c9f76245205a202c8de4e835dc1fe0a7c1  logs/launch_B.sh
7e234e99752bebf864e88bbf3a059dbfd75921be4c9c4e89e890c88dacae88e7  logs/power_draft.log
cdebb53438ed4968e56989e8e1c3a5e96140a7043f072cd22c7ab905a50b281f  logs/run_B.sh
c446071ce50009cf3d4bab910ee19ba3148caf05fff90703ffc3452eef083a61  logs/run_feasibility.sh
b356a6f0068b8baebacc7e3403c64d136712b14761264a0b2f5f878c012d4bb7  logs/seed_scan_draft.log
3d579a4a92c2806a7ca633825af961246a2e65427df3e7d1185a283fd4fafd72  logs/wait_for_free_rig.sh
3b98410ba4a12fca42f30907da35c863d26ae77e86a6dce56b2b5d7d12cf0a09  power.log
db3bd30d4c0d0713e1e36050e073addc82e10ac85fc41a65ed4d762428e46404  requirements.lock
541709b8684a6df0344b4e543df6e22c968fa297998807715219f9eef967afbe  results/derangements_p30.json
bfa5bc139a03d218522c6c4e8a0af50ec607809cd949d3e2e0d5b25cd767187f  results/derangements_p31_open3.json
080fa817e53d2ef71c6c2f61aebb49674dd3f14c34aea1a37fb77e292f5c98ef  results/feasibility/baselines.csv
99a1b810aa12f6a15db3ba84bd96c2b48346eb95d251dbcef0083a82e1dfb78f  results/feasibility/checkpoint_feasibility.jsonl
33a5377151f6a8b9fe1d836e71c01fd7c92f676b6addd75696d444dcba6a866d  results/feasibility/feasibility.json
3c996623bdaab112a6faf6267f7ffb7c6483bb438fcb7afea0f6f231c74ef7c3  results/feasibility/rgl_routes.csv
f50c7340ed7a24784b108920d5c4db3f623bbda9a51aa04661d5e1224eea6a5a  results/heuristic_locked_p30.json
b8288e4888cd248ef40cf7378085b2c1eca4393149f7886e2e403ba54edfcfae  src/__init__.py
f0685d8f1a8dfe983b3703cd7fc6ba52ae4f9b769b3afa671a9061e4ea346f03  src/analyze.py
b447636548f361de4357e08493522605157887bc46a5dd0bb02924499e7fea51  src/analyze_p26.py
81f6b2e6ae8536578ac2ab812c3b69e1668372ec3ec06aa310f4245dfbcadc9d  src/analyze_p27.py
79e3346230ed69cb3b11de80a4d784f93903195bbd3031ae9fe180db603e6d9b  src/analyze_p28.py
04560b8b50aeb4e1ff65d5cea2457d72f4b8d8643646662afad08b0a66499f5a  src/analyze_p30.py
5f07d0a6cd647516845f87287679223bc19d10fb776533bf526351c93e475fc7  src/analyze_p31.py
13e43ccdaa239075c34f9d3a165824dbfddd42e186840da93de7d1164b027f0b  src/assign_derangements.py
ae452942c744696c093e5c781facf0e5c7fa3191b1bcbb77c6a38e5128124ef6  src/assign_derangements_p31.py
0276d309c81c33d7d48ca94fc58973667fb68229fde6003410d160f3b9447408  src/calibrate_doses.py
c9e1cc750ca5cd2a8741fd2bac85377c072b8690bb2ffc5fddd9a9d0018c9abf  src/common.py
484e6d56da774ba71fb9af3b6c382ab6bf658c7bf2c9f2ff587ce951cb46885f  src/feasibility_p31.py
574bf511d143c4ae9d28be61e81e64f3e41e8fb5e8dfc11ca4fe46b59a14e3a0  src/freeze_route_shares.py
cf0f07863c7cc38a9e91829d2f03f4032256d249f07dfb8d899afbc0bc3aaccf  src/heuristic_noaffect.py
157a9bac5089f86d95b34dc067ad62c4ef00c6cb0cceb00509da41ed122a65e3  src/mix_shares.py
3250c743e9ea496eba712ba1e91e84d7fb7ea5257c579e3df41e7a70e206b007  src/mp_fit.py
459bfbf7dfaa21fee7fb44c1389b3daf05cb7b538c41bcd80e58e9f018eaaa91  src/mpe_fit.py
4211dc2ae8cd19f641fbfe82502bebd67cc5bcbf337739671652f1d376be293e  src/p21_port/__init__.py
81186936a8e9be148e753f98477ef48df0f16ff8565634d451e4956778e04d6d  src/p21_port/features.py
d3a01bc7db92c4afca7dd87982a7413395a8156aea1b6c842f6ea48f00f20926  src/p21_port/harness.py
b3774ecab18725ef7a04d8d74c479a35d95ec648abcbb1cb667b457e7b232a06  src/p21_port/policies.py
2d8d17deafa040bd87c80839ca4da945d84d2d9fab61679274f6f3e75d234bec  src/p23_port/__init__.py
25caff971daf0d5468306657762170a5f4f5e4051a025500ade54d7ead1c3277  src/p23_port/features.py
68e3acb2d6406424b571f1e5cc2e7919429c77c081e27159f720c571a3b1691e  src/p23_port/harness.py
dffc85ba9ff5781dde102013fc1e3c7ffb720ade6ab882f184b454fbeccae690  src/p23_port/policies.py
509db3aed2351cb5cfc5ef375ff283bd278ab0d1d265d12425eca1e5ee80fa39  src/p30_frozen.py
1c9365fd8ea68b52301ab8bf1584ff218de402b7fab6ceb780d12e467736394f  src/p31_fit.py
d7c8330d8158b0a028aaae568703a719cc690c85723ed44bc198fd1db9d24c02  src/p31_frozen.py
4508a247306808276db4fd3bd3f18f23ff3af607409337a59584f497c42da108  src/power.py
606305d5bab74f90126f684042a18aff4e9fba659a1bb6f8ff9268177b314cea  src/report_tables.py
1d7c6510bee9df57c2f347f1c338fe2ee54914d4ff7eb8609689f95c7e821359  src/select_heuristic.py
e95edcdf87be0ce401617518e67bd6e6aa66650842e76ec88dbfc61072975976  src/trace_codec.py
1ddcdc7905f9888ed46508d6056784bb57de16b817fb5f921cdc755add8dbf8c  verify-logs/banned_token_grep.py
82738ffd32826afded934d16f62c4f10f2264a3a878f729a0ba36c14992a2aef  verify-logs/test_p31.py
2c28b80c711ed71bcf5e942a2b044f5ba85c51cae3a49ccbe28e8c462b41f3be  verify-logs/tests.log
629eb12f4b73e18ad197ba7d8b2537b5eccaef958bf9ed2675ab5446927e0f83  verify-logs/writeup_gate.py
```

Also cited: spec `e620509377516858d1d1e3677a14f977c76549608e93702dc5dc7a5735487475`; v2 pre-statement `32b70b13a7cfd64cb836e84aa4be1072ded796e381f4c97a5cc085ce1cd4e13d`; nograss `char_prefab_map` canonical JSON `8bdfafff00af3eff6d6ae1293ecc43ce61123493c357c077b9ebedc4d11c0a62` (W2, dropped); P30 `src/mp_fit.py` `3250c743e9ea496eba712ba1e91e84d7fb7ea5257c579e3df41e7a70e206b007`.

## Footer

clinical_claim: false · proof/micro-env/model · No confirmatory seed has been run.
