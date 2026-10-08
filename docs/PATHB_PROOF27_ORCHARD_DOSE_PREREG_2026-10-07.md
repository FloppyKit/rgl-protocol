# PREREG — GO-RGL-PATHB-PROOF-27

Frozen 2026-10-07T22:26:07-0500, before any seed in 28000-28199. clinical_claim: false. No PHI. CPU/headless only, no GPU. proof/micro-env/model. Barrett/Huberman lineage only. Inverse, null and inconclusive results are all reported. No soft goalposts.

## Why
P26 (prereg 001d35c7401b452d1f0f6f39d0d8d454f956a9890d13ee2f3a7c218cddbeb721, public at rgl-protocol 574ca21904fa60f58b0d23565937ed0be1caba15) found balanced RGL beat all six affect-biased arms, all surviving Holm. At bias +2.15 every biased arm collapsed to one route on 100% of steps, so P26 compared single-route policies with a mixed policy. P27 asks the graded question: as one affect's bias grows from none to dominant, does success fall smoothly, stay flat until takeover, or rise first and then fall?

## Design
- Environment, focal slot, horizon, bots, `requirements.lock`, and the copied P26 `src` tree are the P26 stack (dm-meltingpot 2.4.1 `predator_prey__orchard_3`, focal prey slot 0, horizon 1000, pretrained background bots). The same scorer is used. The only independent variable is the bias added to one route.
- Base scores, features, route-to-action mapper, tie-break order, and outcome fields are unchanged. P26 arm names (`fight_biased` and the other `*_biased` arms) still add exactly 2.15 to their own route. Dose arms are named `{prefix}_b{value}` with two decimals, for example `love_autopilot_b0.50`. Bias 0 adds 0 and matches `balanced_rgl`.
- Dose calibration (manipulation check only, not a result): seeds 98000-98019 (n = 20). Each affect was run at bias in {0.05, 0.10, 0.20, 0.30, 0.50, 0.75, 1.00, 1.50}, plus `balanced_rgl` on the same seeds so each affect's no-bias own-route share is known. The recorded metric is that arm's mean own-route share: the mean over episodes of (own-route count / sum of the six route counts). `src/calibrate_doses.py` does not read or print food, eaten, or success fields. The full episode file was deleted after the route-count columns were projected. Seeds 98000-98019 are not used for results.
- Selection rule, applied per affect, targets LOW = 0.25, MID = 0.50, HIGH = 0.75:
  - If the balanced own-route share is already above the target, assign the smallest grid value. This is disclosed.
  - Otherwise assign the grid value whose mean own-route share is closest to the target. If two grid values are equally close, keep the smaller bias. This is disclosed.
  - If two targets map to the same grid value, the higher target takes the next grid value up. Repeat until the three doses differ. Each bump is disclosed.
- Chosen doses (bias, calibration own-route share). Shares below are rounded to 4 decimals; full values are in `results/dose_calibration.json`.

| affect | balanced share | LOW | MID | HIGH | disclosure |
|---|---:|---|---|---|---|
| fight | 0.0336 | 0.20 (0.3723) | 0.30 (0.4862) | 0.50 (0.8515) | none |
| flight | 0.5013 | 0.05 (0.5794) | 0.10 (0.7286) | 0.20 (0.8575) | balanced share already above LOW and MID, so both started at 0.05; MID bumped to 0.10; HIGH's closest was 0.10 and bumped to 0.20 |
| freeze | 0.0000 | 0.30 (0.4691) | 0.50 (0.9433) | 0.75 (0.9989) | MID's closest was 0.30 and bumped to 0.50; HIGH's closest was 0.50 and bumped to 0.75 |
| capitulate | 0.0004 | 0.30 (0.0603) | 0.50 (0.9309) | 0.75 (0.9557) | HIGH's closest was 0.50 and bumped to 0.75 |
| laugh | 0.0000 | 0.50 (0.1223) | 0.75 (0.7353) | 1.00 (0.9531) | HIGH's closest was 0.75 and bumped to 1.00 |
| love_autopilot | 0.4647 | 0.05 (0.5967) | 0.10 (0.6185) | 0.20 (0.7986) | balanced share already above LOW (smallest grid 0.05); MID's closest was 0.05 and bumped to 0.10 |

- Arms (19): `balanced_rgl` (dose 0) plus the 18 dose arms named by the table: `fight_b0.20`, `fight_b0.30`, `fight_b0.50`, `flight_b0.05`, `flight_b0.10`, `flight_b0.20`, `freeze_b0.30`, `freeze_b0.50`, `freeze_b0.75`, `capitulate_b0.30`, `capitulate_b0.50`, `capitulate_b0.75`, `laugh_b0.50`, `laugh_b0.75`, `laugh_b1.00`, `love_autopilot_b0.05`, `love_autopilot_b0.10`, `love_autopilot_b0.20`. These biases are frozen in `src/analyze_p27.py`.
- Result seeds: 28000-28199 (n = 200 per arm, 3800 episodes). Unpaired analysis. Blocks 24000-24999, 26000-26099, 27000-27249, and 98000-98019 are not used for results. No seed in 28000-28199 has been run.
- PRIMARY outcome: success = `food_1000 >= 1 AND times_eaten <= 2` (unchanged).
- SECONDARY (descriptive): food component (`food_1000 >= 1`), safety component (`times_eaten <= 2`), mean `times_eaten`, mean `food_1000`, own-route share (manipulation check), `refuge_frac`.

## Analysis
- Primary family: 6 dose-response tests, one per affect, on success across dose 0 (`balanced_rgl`), LOW, MID, HIGH. Two-sided Cochran-Armitage trend test. The score at each dose is the measured mean own-route share of that affect's route on the analyzed episodes (the result set, not the calibration shares). Holm at family alpha 0.05.
- Cochran-Armitage arithmetic (pinned): group sizes n_i, successes x_i, scores s_i, N = sum n_i, X = sum x_i, sbar = sum n_i s_i / N, T = sum s_i (x_i - n_i X/N), Sss = sum n_i (s_i - sbar)^2, chi^2 = T^2 / ((X/N)(1 - X/N) Sss), p = chi-square survival at 1 df. If X is 0 or N, or Sss is 0, the test is degenerate and p = 1. z = T / sqrt(variance) is reported with the chi-square. A trend survives Holm only if it is not degenerate and its Holm-adjusted p is <= 0.05.
- Shape (secondary, descriptive): per affect, success at each dose with a 95% percentile bootstrap CI (10,000 resamples). Flag a non-monotone pattern when LOW or MID beats balanced and the risk-difference CI lies entirely above 0. If that flag is set and HIGH's success mean is below the flagged dose's mean, label rise-then-fall. Any such pattern is exploratory and may only become a hypothesis for a later prereg.
- Pairwise (secondary): each dosed arm vs balanced, two-sided Fisher exact, risk difference = p_arm - p_balanced with an unpaired 95% percentile bootstrap CI, Cohen's h = 2*arcsin(sqrt(p_arm)) - 2*arcsin(sqrt(p_balanced)). Holm is within each affect (3 tests), not across affects.
- Calibration condition: balanced primary success must land in [0.15, 0.70] (same band as P26). Outside means OUT-OF-BAND and everything is exploratory, still fully reported. In band, the six trend tests are confirmatory and the shape and pairwise results stay secondary.
- No exclusions. A crashed episode is one rerun of that (arm, seed); report the count. No extra seeds for any reason.
- Bootstrap RNG seeds are frozen in `src/analyze_p27.py`: per-arm mean CIs use numpy Generator seed 27027; risk-difference CIs use seed 27028 + affect_index*10 + dose_index, with affects in the order fight, flight, freeze, capitulate, laugh, love_autopilot and dose_index 0 = LOW, 1 = MID, 2 = HIGH. These pins do not add tests.

## Confirmatory data
Seeds 28000-28199 have not been run. Calibration seeds 98000-98019 are not in the result set. The analyzer was exercised on a synthetic scratch CSV with seeds 98100-98101 only (`verify-logs/scratch_episodes.csv`). That file is not a result.

## sha256
Taken after `src/__pycache__` was deleted. `src/analyze_p27.py` is in this list.
```
db3bd30d4c0d0713e1e36050e073addc82e10ac85fc41a65ed4d762428e46404  requirements.lock
b8288e4888cd248ef40cf7378085b2c1eca4393149f7886e2e403ba54edfcfae  src/__init__.py
f0685d8f1a8dfe983b3703cd7fc6ba52ae4f9b769b3afa671a9061e4ea346f03  src/analyze.py
b447636548f361de4357e08493522605157887bc46a5dd0bb02924499e7fea51  src/analyze_p26.py
81f6b2e6ae8536578ac2ab812c3b69e1668372ec3ec06aa310f4245dfbcadc9d  src/analyze_p27.py
0276d309c81c33d7d48ca94fc58973667fb68229fde6003410d160f3b9447408  src/calibrate_doses.py
7077677ae4b1c2cd75331e002d29df26d8032e0dcd126222709915d3897685ed  src/common.py
dd3fcbc207b4a7b52c5dabbde0a42f97e8bfa5264a17177b217abc0a22e68bf6  src/mp_fit.py
459bfbf7dfaa21fee7fb44c1389b3daf05cb7b538c41bcd80e58e9f018eaaa91  src/mpe_fit.py
4211dc2ae8cd19f641fbfe82502bebd67cc5bcbf337739671652f1d376be293e  src/p21_port/__init__.py
81186936a8e9be148e753f98477ef48df0f16ff8565634d451e4956778e04d6d  src/p21_port/features.py
d3a01bc7db92c4afca7dd87982a7413395a8156aea1b6c842f6ea48f00f20926  src/p21_port/harness.py
b3774ecab18725ef7a04d8d74c479a35d95ec648abcbb1cb667b457e7b232a06  src/p21_port/policies.py
2d8d17deafa040bd87c80839ca4da945d84d2d9fab61679274f6f3e75d234bec  src/p23_port/__init__.py
25caff971daf0d5468306657762170a5f4f5e4051a025500ade54d7ead1c3277  src/p23_port/features.py
68e3acb2d6406424b571f1e5cc2e7919429c77c081e27159f720c571a3b1691e  src/p23_port/harness.py
dffc85ba9ff5781dde102013fc1e3c7ffb720ade6ab882f184b454fbeccae690  src/p23_port/policies.py
4e0f2ff069e35387922ffe2840c93497b7ff92b682a39d0dd716d0ff3d765817  src/power.py
606305d5bab74f90126f684042a18aff4e9fba659a1bb6f8ff9268177b314cea  src/report_tables.py
```
