# PREREG — GO-RGL-PATHB-PROOF-30

This preregistration freezes the orchard map ablation before any confirmatory episode. It names RGL spec v1, sha256 `e620509377516858d1d1e3677a14f977c76549608e93702dc5dc7a5735487475`. clinical_claim: false. No PHI. This document does not claim that a model has feelings. H2 is superiority. The H3 band is [0.15, 0.70]. No seed in 31000-31566 has been run.

Phase A2, 2026-10-08. The heuristic calibration on seeds 31600–31699 has been run and locked by code. Confirmatory seeds have not been run. This file is published, byte-identical, before any confirmatory seed.

## Spec binding

RGL spec v1 is `/Users/dude/rgl-proofs/RGL-SPEC-v1/RGL_SPEC_v1.md`, frozen 2026-10-08 18:06 CT, approved by Matt, file mode read-only. The same sha256 is in `RGL-SPEC-v1/SPEC_SHA.txt` and `RGL-SPEC-v1/RGL_SPEC_v1.sha256`. Phase A checked that the sha256 file equals `shasum -a 256` of `RGL_SPEC_v1.md`. T1 passed: the spec digest matches, and every source sha256 in the spec section "Source of truth" matches the file it names (32 files).

This proof binds to spec sections "3. Source of truth", "9. The emotions map", and "12. Pre-stated predictions". P30 is the orchard test of spec prediction (f): a shuffled trigger-to-route map loses to the true map wherever at least two routes fire. Spec prediction (j), that balanced choice is a pure function of the feature dict, is unit test T2, which passed.

## Why

P28 (four arms, seeds 29000–29566, n = 567) found balanced success 0.236 (134/567), inside [0.15, 0.70]. Flight at bias 0.05 succeeded at 0.309 (175/567), risk difference 0.072, Holm p 0.00758, survives. Freeze at bias 0.30 succeeded at 0.293 (166/567), risk difference 0.056, Holm p 0.0184, survives. Balanced beat `random_mix` 0.039 (22/567), risk difference 0.198, Holm p 2.20e-23. `random_mix` draws a new route every alive step from the frozen P27 shares. It matches how often balanced uses each route. It does not match how long balanced stays on one route, and it does not ask whether the particular pairing of appraisal pattern to action is doing the work.

P29 (three arms, seeds 30000–30566, n = 567) found balanced 0.217 (123/567), dwell-matched random 0.049 (28/567), and `random_mix` 0.016 (9/567). H1 risk difference 0.168, interval 0.131 to 0.206, Holm p 2.174e-17. H2 risk difference 0.034, interval 0.014 to 0.055, Holm p 0.00109. The dwell match missed on love run length (8.878 against 11.793, outside ±20%). State-based route choice beat a random policy matched on shares and, except for love, on run lengths. That still leaves two questions: whether the specific emotions map (which appraisal pattern triggers which action route) matters beyond any state-reactive switching among the same actions, and whether RGL beats an equally informed controller that has no emotion labels.

Question. Does the specific emotions map matter beyond any state-reactive switching, and does RGL beat an equally informed controller with no emotion labels?

## Design

Environment: dm-meltingpot 2.4.1 `predator_prey__orchard_3`, focal prey slot 0, unpaired, 1000-step episodes, pretrained background bots. Identical to P28 and P29. `src/` and `requirements.lock` were copied from `../GO-RGL-PATHB-PROOF-28` in Phase A1 and were not edited in P27, P28, or P29. P29 was not opened. P29's read-only reference copy is `/Users/dude/rgl-proofs/RGL-SPEC-v1/logs/ref-snapshot-P29-readonly/`.

Arms, exactly four, n = 567 each on the confirmatory block (2268 episodes):

1. `rgl_v1`
2. `shuffled_map`
3. `heuristic_noaffect`
4. `random_mix` (descriptive anchor, not in the Holm family)

Confirmatory seeds: 31000–31566. Heuristic calibration seeds: 31600–31699 (100 seeds). Calibration is never confirmatory and never pooled with confirmatory data.

Burned or already used, refused for every role: 24000–24999, 26000–26099, 27000–27249, 28000–28199, 29000–29566, 30000–30566, 30900–30999, 98000–98999. Phase A scratch uses seeds 100–101 only. T4 also used seed 100 for one smoke of at most 60 steps. T12 used seeds 100 and 101 for full 1000-step episodes. No seed in 31000-31566 has been run.

Primary success: `food_1000 >= 1` AND `times_eaten <= 2`.

Calibration band for `rgl_v1` on confirmatory seeds: [0.15, 0.70]. Outside the band the label is OUT-OF-BAND and every comparison is exploratory, still fully reported. Report `rgl_v1`'s rate and interval next to P28's 0.236 and P29's 0.217.

`rgl_v1` is the frozen spec: the balanced path. `BalancedRGLGrid` source text in `src/mp_fit.py` stays identical to P28 (T2 passed). The arm name in the CSV is `rgl_v1`. It constructs the balanced scorer with bias 0. It does not add a new score, feature, or mapper.

Balanced decision, as in P28 `BalancedRGLGrid`. `base_scores` is six linear scores of the appraisal features threat, goal, forest_access, leader_salience, ally_risk, social, ambiguity, low_speed, and boundary_pressure. In orchard, ambiguity is always 0 because every alive predator is treated as visible, and boundary_pressure is the constant 0. `choose` walks `ROUTE_ORDER` = (fight, flight, freeze, capitulate, laugh, love) and keeps a route only when its score exceeds the current best by more than 1e-12. Ties within that margin stay with the earlier route. The decision is per alive step. There is no dwell and no hysteresis. The winning route is then passed to the per-route action mapper inside `run_episode`.

Frozen P27 shares, the constants in `src/mix_shares.py` (4 d.p. check in parentheses): fight 0.03533432781622072 (0.0353), flight 0.4806579129663373 (0.4807), freeze 0.0 (0), capitulate 0.0002561226358477411 (0.000256), laugh 0.0 (0), love 0.48375163658159426 (0.4838). T3 passed: `mix_shares.py` is byte-identical to P28, and the probabilities equal these values and sum to 1.

## shuffled_map

Same features, same six score formulas, same `choose`, same tie order as `rgl_v1`. The winning score label `r` is not the route that is executed. It is executed with the action mapper of `pi(r)`.

Blocks, from the frozen P27 shares, threshold 0.01:

- Fired block F = {fight, flight, love}.
- Silent block S = {freeze, capitulate, laugh}.

Allowed shuffles are derangements inside each block: the 2 three-cycles on F times the 2 three-cycles on S. That is 4 derangements of the six routes, and every route moves.

Order the cycles on the `ROUTE_ORDER` spelling of each block. Forward cycle sends each route to the next, and the last back to the first. Backward cycle sends each route to the previous.

- F forward: fight→flight, flight→love, love→fight.
- F backward: fight→love, love→flight, flight→fight.
- S forward: freeze→capitulate, capitulate→laugh, laugh→freeze.
- S backward: freeze→laugh, laugh→capitulate, capitulate→freeze.

The four derangements:

- D0: F forward, S forward. fight→flight, flight→love, love→fight, freeze→capitulate, capitulate→laugh, laugh→freeze.
- D1: F forward, S backward. fight→flight, flight→love, love→fight, freeze→laugh, laugh→capitulate, capitulate→freeze.
- D2: F backward, S forward. fight→love, love→flight, flight→fight, freeze→capitulate, capitulate→laugh, laugh→freeze.
- D3: F backward, S backward. fight→love, love→flight, flight→fight, freeze→laugh, laugh→capitulate, capitulate→freeze.

All four are used. They are one arm. Each confirmatory seed is assigned one derangement. The assignment was drawn in Phase A2 and then frozen:

- Seeds in ascending order, 31000 through 31566.
- A length-567 vector of labels: 142 times D0, 142 times D1, 142 times D2, 141 times D3, in that order (567 = 142×3 + 141).
- `numpy.random.default_rng(30030).shuffle` on that vector.
- Zip the shuffled labels with the seeds.

`src/assign_derangements.py` drew that table with the Phase A interpreter. Numpy version 2.5.3. Counts are D0 142, D1 142, D2 142, D3 141. The canonical JSON sha256 of `results/derangements_p30.json` (sort_keys, compact separators, trailing newline) is `541709b8684a6df0344b4e543df6e22c968fa297998807715219f9eef967afbe`. That sha equals the draft value. The file records `numpy_version` 2.5.3. This file is what the run uses. `src/p30_frozen.py` pins `DERANGEMENT_SHA256` to that digest. T7 passed.

On every alive step the trace logs the trigger label and the executed route. `rgl_v1` logs both as the chosen route (they are equal). `shuffled_map` logs the chosen label and `pi(label)`.

A derangement of all six routes would mostly send flight and love triggers to freeze, capitulate, and laugh actions. Balanced almost never selects those three (frozen shares 0, 0.000256, and 0). That mix would change the pairing and the action repertoire in the same arm. A within-block derangement keeps the executed repertoire of the routes that actually fire inside {fight, flight, love}, and changes only which of those actions follows which winning score. The silent three-cycle runs only when a silent route wins, which the frozen shares say is rare.

## heuristic_noaffect

A plain rule controller. No route names, no route scores, no affect labels. It may read the same observation channels the balanced branch reads (POSITION, ORIENTATION, WORLD.RGB, and the same alive/dead events) and the same feature primitives: nearest-predator distance, BFS distance to food, BFS distance to grass/cover, holding_acorn, on-grass. It may use the same movement primitives: `bfs_from`, `step_toward`, `step_away`. It must not call `BalancedRGLGrid`, `base_scores`, `choose`, or `mix_shares`. T5 passed on `src/heuristic_noaffect.py`.

Distance to the nearest alive predator is Euclidean, `numpy.linalg.norm`.

Template rule, evaluated on alive steps:

- If the nearest alive predator is within distance `d`, flee. Cover-first flee: step toward grass when that step also increases distance from the predator; if already on grass, step away inside grass; otherwise step away. Straight-away flee: `step_away` from that predator, ignoring grass.
- Else if holding an acorn, go to grass and INTERACT (INTERACT on grass, else step toward grass).
- Else step toward the nearest food by BFS.

Commitment `k`: after the flee branch is taken, keep executing that same flee mode for `k` further alive steps even if the predator leaves the radius. Death clears it. `k = 0` re-evaluates every alive step.

Locked tuning grid, 24 configs: `d` in {2, 3, 4, 5, 6, 8} × flee mode {cover-first, straight-away} × commitment {0, 3}.

Calibration: each of the 24 configs on seeds 31600–31699 only (2400 episodes). The tuning CSV `results/tuning/tuning_episodes.csv` has 2400 rows, the `rerun` column (every value 0), policy `heuristic_noaffect` only, and 24 configs × 100 seeds, each config on seeds 31600–31699. Those seeds are never confirmatory and never pooled.

Selection, applied by `src/select_heuristic.py`, not by hand: highest primary-success count; ties go to smaller `d`, then cover-first, then commitment 0. The locked config is config_id 18: `d` = 6, flee mode straight-away, commitment 0. Calibration success count 37 out of 100. Calibration success rate 0.37. The count 37 is the unique maximum in the table, so the tie-break keys were not the decider; the script still applied the rule. Canonical JSON sha256 of `results/heuristic_locked_p30.json` is `f50c7340ed7a24784b108920d5c4db3f623bbda9a51aa04661d5e1224eea6a5a`. `src/p30_frozen.py` pins `HEURISTIC_SHA256` to that digest. T6 passed. Phase B reads that file and refuses to run unless the sha matches.

| config_id | d | flee_mode | commit_k | n | success_count |
|---:|---:|---|---:|---:|---:|
| 0 | 2 | cover-first | 0 | 100 | 9 |
| 1 | 2 | cover-first | 3 | 100 | 8 |
| 2 | 2 | straight-away | 0 | 100 | 5 |
| 3 | 2 | straight-away | 3 | 100 | 3 |
| 4 | 3 | cover-first | 0 | 100 | 17 |
| 5 | 3 | cover-first | 3 | 100 | 17 |
| 6 | 3 | straight-away | 0 | 100 | 10 |
| 7 | 3 | straight-away | 3 | 100 | 10 |
| 8 | 4 | cover-first | 0 | 100 | 19 |
| 9 | 4 | cover-first | 3 | 100 | 21 |
| 10 | 4 | straight-away | 0 | 100 | 15 |
| 11 | 4 | straight-away | 3 | 100 | 22 |
| 12 | 5 | cover-first | 0 | 100 | 27 |
| 13 | 5 | cover-first | 3 | 100 | 27 |
| 14 | 5 | straight-away | 0 | 100 | 24 |
| 15 | 5 | straight-away | 3 | 100 | 26 |
| 16 | 6 | cover-first | 0 | 100 | 23 |
| 17 | 6 | cover-first | 3 | 100 | 23 |
| 18 | 6 | straight-away | 0 | 100 | 37 |
| 19 | 6 | straight-away | 3 | 100 | 26 |
| 20 | 8 | cover-first | 0 | 100 | 16 |
| 21 | 8 | cover-first | 3 | 100 | 15 |
| 22 | 8 | straight-away | 0 | 100 | 19 |
| 23 | 8 | straight-away | 3 | 100 | 20 |

The trace for this arm records the branch taken on each alive step (`flee`, `deposit`, or `food`). It does not record a route name.

## Fairness of the heuristic

The heuristic gets a declared search. The map it is compared with also has a history. Counted from P16–P23 GO/PREREG/WRITEUP, the P24 fit pilot, and P26–P27 calibration. UNKNOWN means the record does not say.

How the P21 weights (the six linear score formulas in `base_scores`) were chosen is not recorded.

The six linear weights in `base_scores` are the same text from P21 through P28. P20 used a different feature set and different coefficients, on a different arena, 80 seeds × 7 arms = 560 episodes. P20's GO says those parameters were fixed before the first full run and were not tuned after it. How many weight vectors were tried before that lock: UNKNOWN. How many episodes informed the numerical change from P20's equations to P21's equations: UNKNOWN. P21's own run (560 episodes, seeds 21000–21079) held the new equations fixed; the only arm factor was +2.15 on one route.

One documented mapper change: P22 replaced the laugh mapper after P21's laugh result. The other five route mappers were held. P21's 560 episodes are the episode count named in that write-up as the reason for the change. P22 then ran another 560 episodes. Its write-up says no post-run retune of the success proxy. P23 ran the P22 laugh mapper on a second MPE environment, 7 × 1000 = 7000 episodes, and did not change the weights.

Grid scales in P24 through P28 `mp_fit.py` match each other: `S_THREAT = 5.0`, `S_GOAL = 7.5`, `S_ALLY_RISK = 5.0`. Three distance bands are commented as the P23 values times 10 (a unit change onto tiles): laugh pressure 3.5, laugh ally splash 4.0, capitulate deference 3.5. No GO in P24–P28 records a search over those numbers. Whether any other scale was tried at the port: UNKNOWN. The action-mapper text from the freeze branch through the love branch is identical from P24 through P28. Orchard episodes did not edit weights, scales, or the mapper.

P24's fit pilot ran balanced on orchard for 120 episodes (random 120, noop 40), plus smaller runs on other candidates. No affect-route arm. The success rule used here was chosen after seeing those burned seeds. P25 ran 100 balanced and 100 random on fresh seeds and failed its own band. P26 revised the band to [0.15, 0.70] before P26 data, then ran 7 × 250 = 1750 episodes with bias +2.15 only. P27's dose calibration was 6 affects × 8 biases × 20 seeds, plus balanced on those 20 seeds: 980 episodes, route shares only, not food or success. It chose bias levels. `rgl_v1` uses bias 0, so those 980 episodes did not set a constant inside `rgl_v1`. P27 confirmatory was 3800 episodes. P28 did not retune (2268 episodes).

P16–P19 are the residual/thrash ladder, a different controller. This prereg does not count their episodes as edits to these six weights. Whether any of them informed the P21 coefficients: UNKNOWN.

What `rgl_v1` actually had, on the record: one laugh-mapper redesign after 560 episodes, one coefficient rewrite whose search size is UNKNOWN and which was not fit on orchard, a unit rescaling at the grid port with no recorded scale search, and no orchard edit of weights, scales, or the mapper. The endpoint was chosen after the P24 pilot. Keeping the controller across later proofs is selection of a surviving instrument. It is not a 24-cell search on primary success.

The heuristic's budget is 24 configs × 100 seeds = 2400 episodes, selected on the same primary success the confirmatory test uses. That is larger than the one documented mapper edit (560 episodes) and larger than P27's 980-episode dose calibration, and unlike that calibration it is allowed to see success. It is the budget this prereg locks. It is not a claim that 2400 episodes equal the whole history of the instrument.

## random_mix

P28 `src/mix_shares.py`, byte-identical, frozen P27 shares above. Descriptive anchor. Not in the Holm family. It does not read the route scores. The route it draws is passed through the same action mapper as `rgl_v1`.

## Hypotheses (locked)

One-sided Fisher exact tests. Holm step-down, monotone, family alpha 0.05, family = {H1, H2}.

- H1 (primary): `p(rgl_v1) > p(shuffled_map)`. Risk difference = p(rgl_v1) − p(shuffled_map).
- H2: superiority, `p(rgl_v1) > p(heuristic_noaffect)`. Risk difference = p(rgl_v1) − p(heuristic_noaffect). The non-inferiority alternative is written under Power, with its n. It is not the locked test.
- H3 (gate, not a Fisher test, not in the Holm family): `rgl_v1` replicates inside [0.15, 0.70]. Report the rate and interval next to P28's 0.236 and P29's 0.217.
- Descriptive, outside the family: `rgl_v1` vs `random_mix`; `heuristic_noaffect` vs `shuffled_map`; `shuffled_map` success by derangement (D0–D3). Each reported risk difference gets a one-sided Fisher p with no Holm adjustment.
- Each risk difference also gets a two-sided 95% unpaired percentile bootstrap interval, 10,000 resamples, so a reversal is visible. Cohen's h by the arcsine formula, same direction: `2*arcsin(sqrt(p_arm)) - 2*arcsin(sqrt(p_baseline))`. Bootstrap seeds, pinned: risk-difference intervals use numpy Generator seed `30031 + index`, with H1 = 0, H2 = 1, rgl vs random_mix = 2, heuristic vs shuffled = 3, and the four derangement-minus-rgl descriptive differences = 4, 5, 6, 7. Per-arm rate intervals use seed `30041 + arm_index` with arm order rgl_v1, shuffled_map, heuristic_noaffect, random_mix. Derangement-only rate intervals use seed `30051 + derangement index`.

## Interpretation, pre-stated

The WRITEUP pastes the matching sentence verbatim. A sentence that depends on a manipulation check is conditional. It must not assume the check passed. "The manipulation check" in a map sentence means all of: (i) in `shuffled_map`, the executed route differs from the trigger label on every alive step (fraction exactly 1.0; anything else is an implementation fault); (ii) the total-variation distance between `shuffled_map` pooled executed-route shares and `rgl_v1` pooled route shares is at least 0.10 (the shuffle changed behavior); (iii) `rgl_v1` pooled shares are within ±0.05 of the P27 frozen shares. Shuffled trigger-label shares are reported descriptively and are not part of the check, because the shuffled agent visits different states, so its trigger mix is expected to drift and that drift is not a reason to set a sentence aside. "The manipulation check" in a heuristic sentence means all of: the heuristic flee fraction of alive steps strictly between 0.05 and 0.95, and `rgl_v1` shares within ±0.05 of the P27 frozen shares. A miss is also written under Limitations. It does not change, exclude, or relabel H1 or H2.

- H1 survives Holm. If the manipulation check passed, RGL beat a state-reactive controller with the same features, the same scores, and the same action repertoire, whose trigger-to-action pairing had been deranged. If the manipulation check missed, H1 survived Holm and the shuffled-map check failed, so this is not read as evidence that the pairing did the work.
- H1 does not survive Holm. If the manipulation check passed, the map isn't what's doing the work in orchard. If the manipulation check missed, H1 did not survive Holm and the shuffled-map check failed, so that sentence about the map does not apply.
- H1 point estimate above 0, and H1 does not survive Holm. The next sentence states the exact-Fisher 80% minimum detectable gap from `logs/power_draft.log`: at n = 567 and alpha 0.025 the gap is 0.07 absolute at either planning base, 0.217 or 0.236. That is a fact about power, not a rescue of H1.
- H1 point estimate at or below 0, and the two-sided H1 interval lies wholly below 0. If the manipulation check passed, this is an inverse result: the deranged map beat RGL in orchard. If the manipulation check missed, the H1 interval lies wholly below 0 and the shuffled-map check failed, so the inverse sentence does not apply.
- H1 point estimate at or below 0, and the interval includes 0. Use the H1-does-not-survive sentence, and add: the point estimate does not favor RGL.
- H2 survives Holm. If the manipulation check passed, RGL beat a plain rule that used the same observations and the same movement primitives and had no emotion labels. If the manipulation check missed, H2 survived Holm and the heuristic check failed, so this is not read as evidence that the emotion structure beat a working plain rule.
- H2 does not survive Holm (the heuristic ties or beats RGL), whatever the sign of the point estimate. If the manipulation check passed: "The emotion structure adds nothing over a plain rule in orchard." If the manipulation check missed: "H2 did not survive Holm and the heuristic check failed, so P30 did not show that the emotion structure adds anything over a plain rule in orchard." If the H2 point estimate is above 0, the next sentence states the same 0.07 minimum detectable gap, as a fact about power, not as a rescue.
- H2 interval wholly below 0. If the manipulation check passed, this is an inverse result: the plain rule beat RGL in orchard. If the manipulation check missed, the H2 interval lies wholly below 0 and the heuristic check failed, so the inverse sentence does not apply.
- H3 in band: rgl_v1 is inside [0.15, 0.70], so H1 and H2 stay confirmatory. The write-up places the rate beside P28 0.236 and P29 0.217.
- H3 out of band: rgl_v1 is outside [0.15, 0.70]. The label is OUT-OF-BAND. Every comparison is exploratory and is still reported in full.
- Inverse and null results publish with the same prominence as a win.

The claim RGL wants from this proof is that the emotion structure adds something on orchard: the particular pairing of appraisal pattern to action, and not only "a rule that looks at the world and switches." H1 is that pairing. H2 is the labels and the scores against a plain rule that sees the same things.

If H1 holds and the check holds, the pairing is doing work that a deranged pairing of the same actions does not. If H1 does not hold and the check holds, the map isn't what's doing the work in orchard: switching on these features can be enough, and the emotions map is not the part that raised success. If the check misses, we have a number and we do not have that sentence.

If H2 holds and the check holds, the frozen structure beat a tuned plain rule. If the heuristic ties or beats RGL and the check holds, the emotion structure adds nothing over a plain rule in orchard. That result is publishable. Superiority will likely fail if a tuned plain rule is as good. The failure is the result, not a broken run.

Non-inferiority was not locked. It could only show that RGL is not much worse than a plain rule. It cannot show that the emotion structure adds something. It also needs a margin we would have chosen. At margin 0.05 and the Holm first-step alpha 0.025, equal true rates of 0.22 need n = 1022 per arm for 80% exact power, about 1.80 times 567. At margin 0.08 the same alpha is already past 80% at n = 567. The margin moves the claim.

H3 only says whether this orchard run still sits in the band where the comparisons were meant to be confirmatory. A rate next to 0.236 and 0.217 is a replication check. It is not evidence about the map.

## Manipulation check

The analyzer reads the confirmatory traces. A miss is written in the WRITEUP Limitations with the numbers. It does not change, exclude, or relabel H1 or H2.

- Shuffled executed route versus trigger label: the fraction of alive steps where they differ must be exactly 1.0 (every route moves under each of D0–D3). Anything else is an implementation fault.
- Shuffled executed-route shares against `rgl_v1` route shares: total-variation distance (half the sum of absolute share gaps over the six routes) at least 0.10. This asks whether the shuffle changed behavior. On the frozen P27 shares, every fired-block three-cycle moves about 0.44 of share on paper, so a value under 0.10 means something is wrong.
- Shuffled trigger-label shares against `rgl_v1` route shares: reported per route and per derangement, descriptive only, not part of the check.
- Heuristic flee fraction: among alive steps, the fraction on which the flee branch was taken is strictly greater than 0.05 and strictly less than 0.95. Outside that, the tuned rule collapsed to always flee or almost never flee.
- `rgl_v1` pooled route shares against the P27 frozen shares above. For every route, the absolute gap is at most 0.05.

## Power

n = 567 per arm is fixed by design. `src/power.py` recomputed `power.log` with the same exact one-sided Fisher enumeration as `logs/power_draft.py` (scipy 1.18.1, numpy 2.5.3). The grid powers match `logs/power_draft.log`. Dropped mass on every row is about 1e-12 to 6e-12. These are per-test powers at the Holm thresholds alpha 0.025 (first step of a two-test family) and alpha 0.05. They are not the power of the step-down procedure jointly. H1 and H2 superiority use the same grid: p_hi in {0.217, 0.236}, p_lo = p_hi − d.

| base | d | alpha 0.025 | alpha 0.05 |
|---|---:|---:|---:|
| 0.217 | 0.04 | 0.366956 | 0.489659 |
| 0.217 | 0.06 | 0.712869 | 0.809582 |
| 0.217 | 0.08 | 0.934789 | 0.966227 |
| 0.217 | 0.10 | 0.994223 | 0.997771 |
| 0.217 | 0.12 | 0.999853 | 0.999959 |
| 0.236 | 0.04 | 0.346759 | 0.468444 |
| 0.236 | 0.06 | 0.680819 | 0.783656 |
| 0.236 | 0.08 | 0.915398 | 0.954418 |
| 0.236 | 0.10 | 0.990086 | 0.995912 |
| 0.236 | 0.12 | 0.999593 | 0.999876 |

Minimum detectable gap at 80% exact power, step 0.005, alpha 0.025, n = 567: d = 0.07 at both bases (power 0.848558 at base 0.217, power 0.820372 at base 0.236). A gap of 0.04 is not what this n can reliably detect. A gap of 0.06 is under 80% at alpha 0.025.

H2 non-inferiority, not locked. True difference 0, both rates 0.22. Power is the exact superiority power at p_hi = 0.22 and p_lo = 0.22 − margin.

| margin | alpha | power at n = 567 | smallest n with power ≥ 0.80 | power at that n | power at n−1 |
|---|---:|---:|---:|---:|---:|
| 0.05 | 0.025 | 0.537124 | 1022 | 0.800014 | 0.799554 |
| 0.05 | 0.05 | 0.658133 | 814 | 0.800413 | 0.799891 |
| 0.08 | 0.025 | 0.931752 | 383 | 0.800477 | 0.799209 |
| 0.08 | 0.05 | 0.964396 | 306 | 0.800212 | 0.798769 |

H2 stays superiority at n = 567. The claim RGL wants is that the emotion structure adds something. Non-inferiority can only show that RGL is not much worse than a plain rule. At the margin 0.05 and alpha 0.025 it needs 1022 per arm, about 1.80 times 567. The cost of superiority is that it will likely fail if the tuned plain rule is as good. That failure is publishable.

Planning clocks, episode time only, 8 workers. Confirmatory work is 4 × 567 = 2268 episodes. Heuristic tuning was 2400 episodes and has already finished (wall 9502.3 s in `logs/tuning.log`).

| clock | s/episode | confirmatory | tuning | heavy total |
|---|---:|---:|---:|---:|
| P27 ruler | 2.969842 | 6735.6 s (1.87 h) | 7127.6 s (1.98 h) | 13863.2 s (3.85 h) |
| P29 lab-lead 1.5 h | 3.174603 | 7200.0 s (2.00 h) | 7619.0 s (2.12 h) | 14819.0 s (4.12 h) |
| P28 measured | 3.338404 | 7571.5 s (2.10 h) | 8012.2 s (2.23 h) | 15583.7 s (4.33 h) |

## Analysis

`src/analyze_p30.py` is hashed below. Holm step-down, monotone. Same estimator and table style as `analyze_p29.py`.

Fail loudly (non-zero exit, no output written) on: duplicate (arm, seed) rows; unknown arms; blank or non-integer seeds; seeds outside the resolved range; a CSV with no `rerun` column; a `rerun` value other than 0 or 1; any missing (arm, seed) episode (fatal, in confirmatory and scratch roles alike).

Confirmatory range is exactly 31000–31566. A scratch range is accepted only when every seed is below 31000. Calibration seeds 31600–31699 are not a confirmatory input and not a scratch input. The confirmatory analyzer never reads the tuning table.

`random_mix` uses the frozen P28 constants. `shuffled_map` uses the frozen derangement table. `heuristic_noaffect` uses the frozen locked config. Nothing is re-estimated from confirmatory outcomes.

Phase A2 reran the analyzer on `verify-logs/scratch_episodes.csv` (seeds 100–101, scratch role, exit 0) and on the seven probe CSVs under `verify-logs/analyzer_probes/`. Each probe exited 1 and wrote no output: missing rerun column, missing episode, duplicate, unknown arm, out-of-range seed, blank seed, rerun = 2. Log: `verify-logs/scratch-analyze.log`.

## Reruns

`mp_fit` writes a `rerun` column (0 or 1) on every row and in the trace CSV. If `run_episode` raises, the worker retries once with the same arm and seed and marks that row `rerun = 1`. A second failure is fatal: the run aborts, no CSV is written, BLOCKED.md. No extra seeds, no exclusions. T9 passed.

## Free-rig rule

Orbitty work may be running on this Mac. Light work (cursor-agent authoring, unit tests, a <= 60-step smoke) may run any time. Heavy work (the heuristic calibration and Phase B) runs only through `logs/wait_for_free_rig.sh`.

The rig is FREE when all of these hold on two consecutive polls 5 minutes apart:

1. No process whose name is exactly one of: xcodebuild, swift-build, swiftc, swift-frontend, clang, clang++, cargo, rustc (`pgrep -x`).
2. No other RGL episode run (`pgrep -f 'src\.mp_fit'` finds nothing).
3. 5-minute load average (`sysctl -n vm.loadavg`, second number) is below half of `sysctl -n hw.ncpu`.

The waiter polls every 300 s, logs each poll to `logs/rig_wait.log`, and only then execs the given command. `logs/wait_for_free_rig.sh --check` does a single check (exit 0 free, 1 busy). Never kill, pause, or renice an Orbitty process to make the rig free. The script never kills, pauses, or renices anything. Orbitty processes are only observed. The free-rig waiter escapes `clang++` for macOS `pgrep -x` (`clang\+\+`).

## Seed scan

T13, in `verify-logs/tests.log`: `csv_files=235`, `seed_header_files=110`, `integer_hits_31000_31566=0`. The scan covered CSV files under `/Users/dude/rgl-proofs` outside this folder and did not open `GO-RGL-PATHB-PROOF-29`. No seed in 31000-31566 has been run.

## Tests at freeze

`verify-logs/test_p30_scorer.py` was rerun to `verify-logs/tests.log`. T1 through T13 each PASS. No PENDING. Final line `EXIT:0`.

Fix before this hash (RGL Lab review, 2026-10-08, before publishing and before any confirmatory seed): the Phase B loader `load_locked_heuristic` in `src/mp_fit.py` read a `locked` key that `results/heuristic_locked_p30.json` does not have (the file stores the locked config at the top level), so every confirmatory `heuristic_noaffect` episode would have failed. The loader now reads `config_id`, `d`, `flee_mode`, and `commit_k` from the top level. The locked file, its sha256, and the selection did not change. T6 and T7 now also call the Phase B loaders on the frozen files (T7 over all 567 seeds). The full test file was rerun after the fix: every test PASS, `EXIT:0`. Pre-fix copies are in `verify-logs/pre-lockload-fix/`.

## Greenlight decisions (Matt, 2026-10-08 18:06 CT)

1. Spec frozen as v1. sha256 `e620509377516858d1d1e3677a14f977c76549608e93702dc5dc7a5735487475`, in `RGL-SPEC-v1/SPEC_SHA.txt` and `RGL-SPEC-v1/RGL_SPEC_v1.sha256`; `RGL_SPEC_v1.md` is chmod a-w. Freeze edits were the status lines, title, freeze sentences, two section-13 status words, and the changelog. No balanced-path content changed. The prereg cites this sha256.
2. H2 = superiority (`rgl_v1` > `heuristic_noaffect`), one-sided exact Fisher, Holm with H1. Non-inferiority is not run.
3. Shuffled map as drafted: the four within-block derangements D0–D3, pooled as one arm, assigned to seeds by `numpy.random.default_rng(30030)`. No six-way derangement arm.
4. Heuristic flee distance `d` is straight-line (Euclidean, `numpy.linalg.norm`), as drafted.
5. Heuristic tuning budget as drafted: 24 configs × seeds 31600–31699 (2400 episodes), best config locked by the code rule before the prereg hash. The fairness section states that how the P21 weights were chosen is not recorded.
6. The draft-time raw agent stream `logs/cursor-agent-draft.jsonl` was moved, unedited, to `/Users/dude/rgl-proofs/_agent-logs/P30/cursor-agent-draft.jsonl` (sha256 `0c1234c73b59f1e8b66bb58264ca00802ecc6800286e8ed0747ce5510141cb6f` before and after). The pointer is `logs/cursor-agent-draft.MOVED.txt`. T10 keeps the P29 T7 exclusions: `verify-logs/writeup_gate.py` and the live raw cursor-agent streams `logs/*.jsonl`. Authored files, including this prereg and the later WRITEUP, get no exclusion.
7. The GO status moved from DRAFT to GREENLIT 2026-10-08 18:06 CT.

Operator notes at greenlight do not change the design. Python is `/Volumes/MiniHangar/rgl-envs/GO-RGL-PATHB-PROOF-27.venv/bin/python` with `PYTHONDONTWRITEBYTECODE=1`. No P30-local `.venv`. T12 and T13 are in the saved test file and passed at this freeze. Publishing this prereg is later, and it is not done in Phase A2.

## sha256

`src/__pycache__` was deleted before these hashes. Digests are sha256 of the file bytes.

RGL spec v1:

```
e620509377516858d1d1e3677a14f977c76549608e93702dc5dc7a5735487475  RGL_SPEC_v1.md
```

Source of truth, spec section 3. Port files are byte-identical across P27, P28, and the P29 snapshot. `src/mix_shares.py` is byte-identical in P28 and the P29 snapshot (P27 has no such file). The balanced-path copies that differ are listed per tree.

```
4211dc2ae8cd19f641fbfe82502bebd67cc5bcbf337739671652f1d376be293e  src/p21_port/__init__.py
81186936a8e9be148e753f98477ef48df0f16ff8565634d451e4956778e04d6d  src/p21_port/features.py
b3774ecab18725ef7a04d8d74c479a35d95ec648abcbb1cb667b457e7b232a06  src/p21_port/policies.py
d3a01bc7db92c4afca7dd87982a7413395a8156aea1b6c842f6ea48f00f20926  src/p21_port/harness.py
2d8d17deafa040bd87c80839ca4da945d84d2d9fab61679274f6f3e75d234bec  src/p23_port/__init__.py
25caff971daf0d5468306657762170a5f4f5e4051a025500ade54d7ead1c3277  src/p23_port/features.py
dffc85ba9ff5781dde102013fc1e3c7ffb720ade6ab882f184b454fbeccae690  src/p23_port/policies.py
68e3acb2d6406424b571f1e5cc2e7919429c77c081e27159f720c571a3b1691e  src/p23_port/harness.py
157a9bac5089f86d95b34dc067ad62c4ef00c6cb0cceb00509da41ed122a65e3  src/mix_shares.py
bff5ce78cabe2f875f18427400c75a80a623b8a3bd4c6553effa955cc8b8c101  GO-RGL-PATHB-PROOF-28/src/mp_fit.py
dd3fcbc207b4a7b52c5dabbde0a42f97e8bfa5264a17177b217abc0a22e68bf6  GO-RGL-PATHB-PROOF-27/src/mp_fit.py
a1b15c2b3f8669f8cd17f25847bb2fb0213020855ec78fc61e9ccb5b95132d96  RGL-SPEC-v1/logs/ref-snapshot-P29-readonly/src/mp_fit.py
a9eff92347cf675241bc06d7c1dddcdf46b63c8367e3c8f3e63fb46db048a016  GO-RGL-PATHB-PROOF-28/src/common.py
7077677ae4b1c2cd75331e002d29df26d8032e0dcd126222709915d3897685ed  GO-RGL-PATHB-PROOF-27/src/common.py
f4498b92cc829c1c96a2f7e065ec46c76b143487fffe1a16ce83b975886f2cd7  RGL-SPEC-v1/logs/ref-snapshot-P29-readonly/src/common.py
```

Every file in this folder's `src/`:

```
b8288e4888cd248ef40cf7378085b2c1eca4393149f7886e2e403ba54edfcfae  src/__init__.py
f0685d8f1a8dfe983b3703cd7fc6ba52ae4f9b769b3afa671a9061e4ea346f03  src/analyze.py
b447636548f361de4357e08493522605157887bc46a5dd0bb02924499e7fea51  src/analyze_p26.py
81f6b2e6ae8536578ac2ab812c3b69e1668372ec3ec06aa310f4245dfbcadc9d  src/analyze_p27.py
79e3346230ed69cb3b11de80a4d784f93903195bbd3031ae9fe180db603e6d9b  src/analyze_p28.py
04560b8b50aeb4e1ff65d5cea2457d72f4b8d8643646662afad08b0a66499f5a  src/analyze_p30.py
13e43ccdaa239075c34f9d3a165824dbfddd42e186840da93de7d1164b027f0b  src/assign_derangements.py
0276d309c81c33d7d48ca94fc58973667fb68229fde6003410d160f3b9447408  src/calibrate_doses.py
c9e1cc750ca5cd2a8741fd2bac85377c072b8690bb2ffc5fddd9a9d0018c9abf  src/common.py
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
5ebe051c69ccc6b4a9212e07a3fc2a5ca65195d760af0c0cc477679db76c57e8  src/power.py
606305d5bab74f90126f684042a18aff4e9fba659a1bb6f8ff9268177b314cea  src/report_tables.py
1d7c6510bee9df57c2f347f1c338fe2ee54914d4ff7eb8609689f95c7e821359  src/select_heuristic.py
e95edcdf87be0ce401617518e67bd6e6aa66650842e76ec88dbfc61072975976  src/trace_codec.py
```

Other locked files:

```
db3bd30d4c0d0713e1e36050e073addc82e10ac85fc41a65ed4d762428e46404  requirements.lock
541709b8684a6df0344b4e543df6e22c968fa297998807715219f9eef967afbe  results/derangements_p30.json
f50c7340ed7a24784b108920d5c4db3f623bbda9a51aa04661d5e1224eea6a5a  results/heuristic_locked_p30.json
0cfc89742cc6ca936611f68b8b01d930d4b82f0aec1166c761769c233091d296  verify-logs/test_p30_scorer.py
629eb12f4b73e18ad197ba7d8b2537b5eccaef958bf9ed2675ab5446927e0f83  verify-logs/writeup_gate.py
c41cc3c410f8c2478e1e1c72aadd786f327ce31b410c6f22392c45a47da6a89c  logs/wait_for_free_rig.sh
f4abd2396e1c63a64cfe6c896353961d330af24625464ea69fea0a38e91ae841  logs/launch_B.sh
2e6eb950649bcc193104a4f5c518b794526d3130e0bfd6eb062070b8fc56d485  logs/run_tuning.sh
676ad839e172215bc1c3a0025d3d3a2132b4eefd5b190cbdcc0435333494b61c  logs/tune_then_A2.sh
199b424c2a0697a071148f97246070b2f8ead4f4a2f4dbbafb96814251f8ed24  logs/PROMPT_B.md
```

## Footer

clinical_claim: false · proof/micro-env/model
