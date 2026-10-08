# PREREG GO-RGL-PATHB-PROOF-29

Phase A2, 2026-10-08. Re-frozen 2026-10-08T14:11:08-0500 after the design fix below, before any confirmatory seed. clinical_claim: false. Proof / micro-env / model. Barrett/Huberman lineage only. Inverse, null, and inconclusive results are all published. No soft goalposts.

No seed in 30000-30566 has been run.

## Why

P28 (FloppyKit/rgl-protocol prereg `ca3cfcb`, headlines `fd034a6`) found that balanced beat `random_mix`: 0.236 against 0.039, H3 Holm p 2.2e-23. `random_mix` draws a new route at every alive step with balanced's P27 route shares (fight 0.0353, flight 0.4807, freeze 0, capitulate 0.000256, laugh 0, love 0.4838). It matches how often balanced uses each route. It does not match how long balanced stays on one route. Verify's P28 report (N2) says H3 does not show that balanced beats a random policy that also matches dwell times. P29 tests exactly that, with a random policy that matches the route shares and the run lengths of balanced but ignores the state.

## Design

Environment: dm-meltingpot 2.4.1 `predator_prey__orchard_3`, focal prey slot 0, unpaired, 1000-step episodes, pretrained background bots. `src/` and `requirements.lock` are the P28 copies. P27 and P28 are not edited.

Arms, exactly three, n = 567 each (1701 episodes), seeds 30000-30566:

- `balanced_rgl`: unchanged from P28 (base scores, features, mapper, tie-break order, outcome fields).
- `dwell_random`: route sequence from a semi-Markov chain fitted to balanced's route sequences (below). It never reads the route scores or the features. The route-to-action mapper is the same one balanced uses (as `random_mix` does in P28).
- `random_mix`: unchanged from P28 (`src/mix_shares.py` byte-identical, frozen P27 shares). Replication anchor.

Seeds: confirmatory 30000-30566. Calibration 30900-30999 (`balanced_rgl` only, n = 100, not confirmatory, never pooled with confirmatory data). Never use 24000-24999, 26000-26099, 27000-27249, 28000-28199, 29000-29566, 98000-98999. Phase A scratch uses seeds 100-101 only.

Primary success: `food_1000 >= 1` AND `times_eaten <= 2` (identical to P28).

Calibration band for balanced on confirmatory seeds: [0.15, 0.70] (identical to P28). Outside the band the label is OUT-OF-BAND and every comparison is exploratory, still fully reported.

Calibration block, already finished before this prereg: `balanced_rgl` only, seeds 30900-30999, 100 rows, `results/calibration/route_traces.csv` with columns exactly `seed,policy,rerun,route_trace`, and `results/calibration/calib_episodes.csv` for the count cross-check only. `src/freeze_dwell.py` opened the trace file for the tables and indexed `seed`, `policy`, and `count_*` in the episodes file by name. The cross-check matched on all 100 seeds. Stdout is `verify-logs/freeze_dwell.log`.

## dwell_random, exact definition

Terms. A step is alive when the focal prey is alive (P28 `alive[0]`). A run is a maximal block of consecutive alive steps with the same route. A run is complete when it ends by a route switch (the next step is alive with a different route) or by death (the next step is not alive). A run is censored only when the episode ends. A run start is either the first alive step of the episode or the first alive step after a respawn (an "entry start"), or the step after a switch-ended run (a "switch start").

Frozen tables, all fitted from the calibration route traces only:

- `pi0[r]`: share of entry starts that begin with route r.
- `P[r][s]` for s != r: share of switch-ended runs of r followed by a run of s. Diagonal is 0. If route r has share > 0 but no switch-ended run, row r is the pooled switch-start distribution with s = r removed and renormalized (stated in the JSON if it happens).
- `h[r][k]`, k = 1..K_r: discrete Kaplan-Meier hazard, h[r][k] = (complete runs of r with length exactly k) / (runs of r, complete or censored, with length >= k), where complete = ended by switch or death and only episode-end runs are censored. For k > K_r (beyond the longest observed run of r) the hazard is 1.

Sampler, per episode, `rng = numpy.random.default_rng(seed)`:

- On a step where the focal prey is not alive: the sampler resets (no current run).
- On an alive step with no current run: draw r from pi0, run length = 1.
- On an alive step with current run r of length k: with probability h[r][k] end it and draw the next route from P[r], length = 1; otherwise keep r and length = k + 1.

Why this refines the simplest scheme ("on run end, draw the next route from run-start frequencies and a length from the run-length distribution"): (1) a draw that repeats the current route would merge two runs and make realized dwell longer than balanced's; excluding self-transitions keeps the dwell matched; (2) runs cut off by the episode end are censored and handled by the hazard, and the dwell_random arm is cut off the same way at run time; a death ends a run, in balanced and in dwell_random alike (see Design fix before freeze); (3) the switch matrix also matches which route follows which. Route shares are then matched through the chain itself and checked, not forced separately.

The sampler loads `results/dwell_tables_p29.json` and refuses to run unless that file's sha256 equals `DWELL_TABLES_SHA256` in `src/dwell_frozen.py`.

### Frozen dwell summary

From `verify-logs/freeze_dwell.log` (full precision is in the hashed JSON). Share is the calibration share of alive steps.

| route | share mean per episode | share pooled | runs | ended by switch | ended by death | censored (episode end) | mean complete-run length | Kaplan-Meier mean |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| fight | 0.049284 | 0.024597 | 297 | 115 | 182 | 0 | 4.787879 | 4.787879 |
| flight | 0.466088 | 0.501496 | 2076 | 1998 | 40 | 38 | 13.776742 | 14.472906 |
| freeze | 0.000000 | 0.000000 | 0 | 0 | 0 | 0 |  | 1.000000 |
| capitulate | 0.000183 | 0.000069 | 3 | 1 | 2 | 0 | 1.333333 | 1.333333 |
| laugh | 0.000000 | 0.000000 | 0 | 0 | 0 | 0 |  | 1.000000 |
| love | 0.484445 | 0.473837 | 2186 | 2148 | 0 | 38 | 12.391993 | 12.933368 |

Occupation shares implied by the frozen chain with no deaths (embedded jump chain times mean run length): fight 0.0198, flight 0.5164, capitulate 0.0001, love 0.4637, freeze 0, laugh 0. Balanced calibration pooled shares: fight 0.0246, flight 0.5015, capitulate 0.0001, love 0.4738.

No route had share > 0 and zero switch-ended runs, so that fallback did not fire. `freeze` and `laugh` have zero calibration share. Their P rows are the pooled switch-start distribution with the route itself removed and renormalized (`p_row` `zero_share_fill`, `how` `pooled_switch`). Their entry probability is 0. The JSON notes are:

`[{"how": "pooled_switch", "p_row": "zero_share_fill", "route": "freeze"}, {"how": "pooled_switch", "p_row": "zero_share_fill", "route": "laugh"}]`

### Frozen random_mix shares

Float64 constants in `src/mix_shares.py` (P27 balanced mean route shares). They sum to 1.

| route | probability | four decimals |
|---|---:|---:|
| fight | 0.03533432781622072 | 0.0353 |
| flight | 0.4806579129663373 | 0.4807 |
| freeze | 0.0 | 0.0000 |
| capitulate | 0.0002561226358477411 | 0.0003 |
| laugh | 0.0 | 0.0000 |
| love | 0.48375163658159426 | 0.4838 |

## Hypotheses (locked)

One-sided Fisher exact tests. Holm step-down, monotone, family alpha 0.05, family = {H1, H2}.

- H1 (primary): `balanced_rgl` success rate > `dwell_random`. Risk difference = p(balanced_rgl) - p(dwell_random).
- H2: `dwell_random` success rate > `random_mix`. Risk difference = p(dwell_random) - p(random_mix). This asks whether committing to routes helps by itself.
- H3 (gate, not a Fisher test, not in the Holm family): balanced replicates inside the P28 calibration band [0.15, 0.70]. Report balanced's rate and interval next to P28's 0.236.
- Descriptive, outside the family: balanced vs random_mix (the P28 H3 direction), with its one-sided Fisher p, as the replication anchor.
- Each risk difference also gets a two-sided 95% unpaired percentile bootstrap interval, 10,000 resamples, so a reversal is visible. Cohen's h by the arcsine formula, same direction. Bootstrap seeds pinned: per-arm intervals numpy Generator seed 30028; risk differences seed 30029 + index (H1 = 0, H2 = 1, anchor = 2).

## Interpretation, pre-stated (no soft goalposts)

- H1 survives Holm: "Balanced beat a random policy matched on route shares and run lengths."
- H1 does not survive Holm (a tie): the WRITEUP lead must contain, verbatim: "P29 did not show that balanced's state-based route choice beats random choice with matched route persistence. On this test, the P28 advantage over the per-step random mix is explained by route persistence, not by state-based choice." If the H1 point estimate is above 0, the next sentence states the exact-Fisher 80% minimum detectable gap from `power.log`, as a fact about power, not as a rescue.
- dwell_random point estimate >= balanced: also say plainly "Dwell-matched random choice did as well as or better than balanced." If the two-sided H1 interval lies wholly below 0, call it an inverse result.
- H2 survives: "Committing to routes helped by itself: dwell-matched random beat per-step random." H2 does not survive: "P29 did not show that committing to routes helps by itself."
- Inverse and null results publish with the same prominence as a win.

## Manipulation check (descriptive, pre-stated)

The analyzer reads `results/route_traces.csv` from the confirmatory run and reports, per arm: pooled route shares, mean per-episode route shares, and mean run length per route (complete runs only, and Kaplan-Meier mean). Complete means ended by a route switch or by death, the same definition as the fit (`src/dwell_sampler.segment_runs`). The pre-stated match criterion: for every route with balanced share >= 0.01, dwell_random's complete-run mean length is within ±20% of balanced's, and its pooled share is within ±0.05 absolute. A miss is written in the WRITEUP Limitations as "the dwell match missed on confirmatory seeds" with the numbers. It does not change, exclude, or relabel the H1/H2 tests.

## Power

`src/power.py` uses the exact one-sided Fisher test. Power is the sum over x1, x2 of Bin(x1; n, p_hi) Bin(x2; n, p_lo) 1[Fisher one-sided p <= alpha]. Tails below 1e-12 may be dropped; dropped mass is reported. The script does not read an episode file. n = 567 per arm. Numbers below are copied from `power.log` (identical to `verify-logs/power.log`).

P27 ruler: 11285.4 s / 3800 episodes. Confirmatory wall: 1701 episodes, 5051.701421052631 s (1.403250394736842 h). Calibration wall at the same ruler: 100 episodes, 296.98421052631574 s.

H1, p_hi = 0.236 (P28 balanced), p_lo = 0.236 - d:

| d | alpha | power | dropped_mass |
|---:|---:|---:|---:|
| 0.04 | 0.025 | 0.3467592949771286 | 5.413225423467338e-12 |
| 0.04 | 0.05 | 0.4684442680466185 | 5.413225423467338e-12 |
| 0.06 | 0.025 | 0.6808187750631993 | 6.093237026050247e-12 |
| 0.06 | 0.05 | 0.7836563700843386 | 6.093237026050247e-12 |
| 0.08 | 0.025 | 0.9153980765561928 | 5.030420524576584e-12 |
| 0.08 | 0.05 | 0.9544179992602183 | 5.030420524576584e-12 |
| 0.10 | 0.025 | 0.9900864879892691 | 5.147660075977001e-12 |
| 0.10 | 0.05 | 0.9959118234674079 | 5.147660075977001e-12 |
| 0.12 | 0.025 | 0.9995926680628545 | 5.604294806005328e-12 |
| 0.12 | 0.05 | 0.999876173464925 | 5.604294806005328e-12 |

H2, p_lo = 0.039 (P28 random_mix), p_hi = 0.039 + d:

| d | alpha | power | dropped_mass |
|---:|---:|---:|---:|
| 0.04 | 0.025 | 0.7928073188318234 | 3.04911651483053e-12 |
| 0.04 | 0.05 | 0.870594678818211 | 3.04911651483053e-12 |
| 0.06 | 0.025 | 0.9777411466617724 | 2.893685291383008e-12 |
| 0.06 | 0.05 | 0.9899896888286897 | 2.893685291383008e-12 |
| 0.08 | 0.025 | 0.99903308214513 | 3.5823566335579926e-12 |
| 0.08 | 0.05 | 0.9996873291077052 | 3.5823566335579926e-12 |
| 0.10 | 0.025 | 0.9999809190285512 | 2.94408941670099e-12 |
| 0.10 | 0.05 | 0.9999954992377966 | 2.94408941670099e-12 |
| 0.12 | 0.025 | 0.9999998104945804 | 3.7020386756125845e-12 |
| 0.12 | 0.05 | 0.9999999667212243 | 3.7020386756125845e-12 |

Smallest d on a 0.005 grid with exact power >= 0.80 at alpha 0.025:

- H1 MDE: d = 0.07, power 0.8203719728819868, dropped_mass 5.1348925111938115e-12.
- H2 MDE: d = 0.045, power 0.8699915976554443, dropped_mass 2.688738121037204e-12.

P28 reference: +0.08 over 0.25 (p_hi = 0.33, p_lo = 0.25), alpha = 0.05/3, n = 567, exact one-sided Fisher power 0.7829216825011911, dropped_mass 5.774825062587752e-12.

## Analysis (locked)

`src/analyze_p29.py` is hashed below. Holm step-down, monotone. Same estimator and table style as `analyze_p28.py`.

Fail loudly (non-zero exit, no output written) on: duplicate (arm, seed) rows; unknown arms; blank or non-integer seeds; seeds outside the resolved range; a CSV with no `rerun` column (`if "rerun" not in reader.fieldnames: raise SystemExit("no rerun column")`); a `rerun` value other than 0 or 1; any missing (arm, seed) episode (fatal, in confirmatory and scratch roles alike).

Confirmatory range is exactly 30000-30566. A scratch range is accepted only when every seed is below 30000.

random_mix uses the frozen P28 constants. dwell_random uses the frozen tables. Nothing is re-estimated from confirmatory outcomes.

## Reruns

`mp_fit` writes a `rerun` column (0 or 1) on every row and in `route_traces.csv`. If `run_episode` raises, the worker retries once with the same arm and seed and marks that row `rerun = 1`. A second failure is fatal: the run aborts, no CSV is written, BLOCKED.md. No extra seeds, no exclusions.

## Free-rig rule

Orbitty work may be running on this Mac. Light work (cursor-agent authoring, unit tests, a <= 60-step smoke) may run any time. Heavy work (the calibration and Phase B) runs only through `logs/wait_for_free_rig.sh`.

The rig is FREE when all of these hold on two consecutive polls 5 minutes apart:

1. No process whose name is exactly one of: xcodebuild, swift-build, swiftc, swift-frontend, clang, clang++, cargo, rustc (`pgrep -x`).
2. No other RGL episode run (`pgrep -f 'src\.mp_fit'` finds nothing).
3. 5-minute load average (`sysctl -n vm.loadavg`, second number) is below half of `sysctl -n hw.ncpu`.

The waiter polls every 300 s, logs each poll to `logs/rig_wait.log`, and only then execs the given command. `logs/wait_for_free_rig.sh --check` does a single check (exit 0 free, 1 busy). Never kill, pause, or renice an Orbitty process to make the rig free.

## Design fix before freeze

The first draft of this prereg (sha256 `7c548a9e502045d9eb43e10765ba9a19cc6bc7e9bdeaaf994f3fcfb4de9199f6`, never published) used a Kaplan-Meier fit that treated death-ended runs as censored. In balanced, 182 of 297 fight runs end with the focal prey eaten, so death is caused by the route and is not uninformative censoring. That fit inflated the fight dwell to a mean of 19.41 steps against 4.79 observed (all fight runs; 2.06 for switch-ended runs only), and the chain without deaths would have put dwell_random on fight 7.3% of the time against balanced's 2.5%. The fit was replaced before freezing and before any confirmatory seed ran: a death now ends a run, and only runs cut off by the episode end are censored. The analyzer's manipulation check uses the same definition. The calibration was not rerun; the same 100 traces were refitted.

| route | before: KM mean | after: mean run length | before: no-death share | after: no-death share | balanced pooled share |
|---|---:|---:|---:|---:|---:|
| fight | 19.41 | 4.79 | 0.0746 | 0.0198 | 0.0246 |
| flight | 14.91 | 14.47 | 0.4943 | 0.5164 | 0.5015 |
| capitulate | 2.33 | 1.33 | 0.0001 | 0.0001 | 0.0001 |
| love | 12.93 | 12.93 | 0.4309 | 0.4637 | 0.4738 |

pi0 and the switch matrix P are unchanged by the fix (both already used only entry starts and switch-ended runs). Pre-fix copies of the changed files are kept in `verify-logs/pre-death-fix/`. Matt approved the fix on 2026-10-08 at 14:08 CT.

## Disclosure

The calibration traces mark not-alive steps as gaps. The freeze uses gaps only to end runs and to mark entry starts. That is structural; it does not compute any outcome.

## sha256

`src/__pycache__` was absent before these hashes. `DWELL_TABLES_SHA256` equals the dwell-tables hash.

```
b8288e4888cd248ef40cf7378085b2c1eca4393149f7886e2e403ba54edfcfae  src/__init__.py
f0685d8f1a8dfe983b3703cd7fc6ba52ae4f9b769b3afa671a9061e4ea346f03  src/analyze.py
b447636548f361de4357e08493522605157887bc46a5dd0bb02924499e7fea51  src/analyze_p26.py
81f6b2e6ae8536578ac2ab812c3b69e1668372ec3ec06aa310f4245dfbcadc9d  src/analyze_p27.py
79e3346230ed69cb3b11de80a4d784f93903195bbd3031ae9fe180db603e6d9b  src/analyze_p28.py
e7d63b306cdcf2d96686bdc22ae0326892148bdfbe74a2b2cd02eb605bfd061e  src/analyze_p29.py
0276d309c81c33d7d48ca94fc58973667fb68229fde6003410d160f3b9447408  src/calibrate_doses.py
f4498b92cc829c1c96a2f7e065ec46c76b143487fffe1a16ce83b975886f2cd7  src/common.py
e1a8a42e740bdc0a052675d8492c69af867a21001466493221455f1baed25600  src/dwell_frozen.py
064b15856e1c45bd46e5ca73cec117fab5a63b54e42c10c72c91fffb50681218  src/dwell_sampler.py
324cc4ed561eb50cd4bd161d67f3182414d10c7f9028f1a635d14f7fd4305b02  src/freeze_dwell.py
574bf511d143c4ae9d28be61e81e64f3e41e8fb5e8dfc11ca4fe46b59a14e3a0  src/freeze_route_shares.py
157a9bac5089f86d95b34dc067ad62c4ef00c6cb0cceb00509da41ed122a65e3  src/mix_shares.py
a1b15c2b3f8669f8cd17f25847bb2fb0213020855ec78fc61e9ccb5b95132d96  src/mp_fit.py
459bfbf7dfaa21fee7fb44c1389b3daf05cb7b538c41bcd80e58e9f018eaaa91  src/mpe_fit.py
4211dc2ae8cd19f641fbfe82502bebd67cc5bcbf337739671652f1d376be293e  src/p21_port/__init__.py
81186936a8e9be148e753f98477ef48df0f16ff8565634d451e4956778e04d6d  src/p21_port/features.py
d3a01bc7db92c4afca7dd87982a7413395a8156aea1b6c842f6ea48f00f20926  src/p21_port/harness.py
b3774ecab18725ef7a04d8d74c479a35d95ec648abcbb1cb667b457e7b232a06  src/p21_port/policies.py
2d8d17deafa040bd87c80839ca4da945d84d2d9fab61679274f6f3e75d234bec  src/p23_port/__init__.py
25caff971daf0d5468306657762170a5f4f5e4051a025500ade54d7ead1c3277  src/p23_port/features.py
68e3acb2d6406424b571f1e5cc2e7919429c77c081e27159f720c571a3b1691e  src/p23_port/harness.py
dffc85ba9ff5781dde102013fc1e3c7ffb720ade6ab882f184b454fbeccae690  src/p23_port/policies.py
e409c3bcfea1fa95dccfa100c129119205137c9345be4783f513445e3617718b  src/power.py
606305d5bab74f90126f684042a18aff4e9fba659a1bb6f8ff9268177b314cea  src/report_tables.py
db3bd30d4c0d0713e1e36050e073addc82e10ac85fc41a65ed4d762428e46404  requirements.lock
e6e711fd3f05f78be742e92af8689a3388a9e27fc25585761235a77c7bfb87d0  results/dwell_tables_p29.json
6bbe14fc1f953455528a589705c7ae334e4f826580367482348475dc16cfa2c0  results/route_shares_calib_p29.json
c02c08e9cfcaa75d050a66eafbd0035a33d7796997d2b007a4372b1b19fc252c  results/calibration/route_traces.csv
d17fde97ac879f7e7d939fadfe436b8ea0a7cc66a6cfd3acb74820d717e996fa  verify-logs/test_p29_scorer.py
629eb12f4b73e18ad197ba7d8b2537b5eccaef958bf9ed2675ab5446927e0f83  verify-logs/writeup_gate.py
f5a5d21454ec25f3e9b6362ee68febd09217de60662e4a5ea24fc1da8f19c572  logs/wait_for_free_rig.sh
62674d0f902b0cd457d720f87d2d11dcdf55c58d42199987cecd50d793f2a951  logs/launch_B.sh
```

## Footer

clinical_claim: false · proof/micro-env/model
