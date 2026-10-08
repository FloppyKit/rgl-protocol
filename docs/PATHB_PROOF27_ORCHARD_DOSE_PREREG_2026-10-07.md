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
