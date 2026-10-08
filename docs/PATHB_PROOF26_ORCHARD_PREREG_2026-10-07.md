# PREREG — GO-RGL-PATHB-PROOF-26

Frozen 2026-10-07T18:50:59-0500, before any seed in 27000-27249. clinical_claim: false. No PHI. CPU/headless only, no GPU. proof/micro-env/model. Barrett/Huberman lineage only. Inverse, null and inconclusive results are all reported. No soft goalposts.

## Background
- P21 (MPE2 simple_world_comm_v3) ran the unified affect-bias sweep: one shared route scorer; arms differ ONLY by a +2.15 additive bias on one route.
- P23 (simple_adversary_v3) was a poor environment fit (adversary follows our agent) and came out inconclusive.
- P24 fit-piloted candidate environments against five fairness checks. Melting Pot `predator_prey__orchard_3` passed checks 1-3. Success definition E(1, <=2) was chosen post-hoc on burned seeds 24000-24999 (balanced 0.292).
- P25 re-piloted that locked definition on fresh seeds 26000-26099: balanced 0.22 [0.14, 0.30], random 0.02 [0.00, 0.05]. It failed the original 30-70% calibration band.
- Band revision (disclosed): the 30-70% band was a rule of thumb meant to leave room for arms to move both up and down. At 0.22 with random at 0.02, there is room both ways. The calibration band for P26 is therefore revised to 15-70%, decided after P25 and before any P26 data. P25 itself stays a FAIL against its own rule.

## Design
- Environment: dm-meltingpot 2.4.1 `predator_prey__orchard_3`, focal prey = slot 0, 1000-step episodes, pretrained background bots, same pinned `requirements.lock` as P24/P25.
- Arms (7): `balanced_rgl` (no bias) and `fight_biased`, `flight_biased`, `freeze_biased`, `capitulate_biased`, `laugh_biased`, `love_autopilot_biased`. Each biased arm adds BIAS_VALUE = 2.15 to exactly one route's base score before route choice. Everything else (base scores, route→action mapper, features, tie-break order) is identical across arms. Bias is the sole independent variable.
- Seeds: 27000-27249 (n = 250 per arm, 1750 episodes). Every arm runs the same seed list. Melting Pot episodes are not seed-reproducible, so analysis is UNPAIRED. Seed blocks 24000-24999 and 26000-26099 are burned and must not be used.
- Power (unpaired two-proportion, p_balanced = 0.22, alpha = 0.05/6): n = 250 detects an absolute drop of 0.15 with ~90% power and a rise of 0.15 with ~83% power.

## Outcomes
- PRIMARY: success = `food_1000 >= 1 AND times_eaten <= 2` (unchanged from P25).
- SECONDARY (descriptive, no multiplicity correction): food component (`food_1000 >= 1`), safety component (`times_eaten <= 2`), mean `times_eaten`, mean `food_1000`, route-choice shares (`count_*`), refuge_frac, and a food-vs-safety Pareto frontier across arms.

## Analysis
- Primary family: 6 comparisons, each biased arm vs balanced on primary success. Two-sided Fisher exact test. Holm correction at family alpha = 0.05.
- Effect sizes for every comparison: risk difference with a 95% percentile bootstrap CI (10,000 resamples, unpaired), and Cohen's h.
- Per-arm success rates with 95% bootstrap CIs.
- Calibration condition: if balanced's primary success on P26 falls outside [0.15, 0.70], the results are labeled OUT-OF-BAND and every comparison is reported as exploratory. They are still reported in full.
- No exclusions. If an episode crashes, rerun that exact (arm, seed) once; report the count of reruns and any still-missing episodes. No extra seeds are added for any reason.
- Hypotheses are tested, not assumed. No directional predictions are claimed as findings without passing Holm.

## Analysis implementation constants (pinned by src/analyze_p26.py)
These do not add tests. They fix the arithmetic the locked analysis left unnamed.
- Risk difference = p_arm - p_balanced. Cohen's h = 2*arcsin(sqrt(p_arm)) - 2*arcsin(sqrt(p_balanced)).
- Unpaired percentile bootstrap, 10,000 resamples. Per-arm mean CIs use numpy Generator seed 26026. Risk-difference CIs use seed 26027 + arm index in the order fight, flight, freeze, capitulate, laugh, love_autopilot.
- Holm is step-down on the six Fisher p-values, monotonic, family alpha 0.05. A comparison survives Holm only if its adjusted p is <= 0.05. If calibration is OUT-OF-BAND, the role of every comparison is exploratory.
- Pareto frontier: an arm is dominated when another arm has food rate >= and safety rate >= and is strictly greater on at least one. Higher is better on both. Frontier arms are the non-dominated set.
- `random_uniform` and `noop_still` stay allowed by the policy guard and are not part of the seven-arm family.

## Confirmatory data
Seeds 27000-27249 have not been run. Scratch smoke seed 99998 is not in the result set.

## sha256
```
db3bd30d4c0d0713e1e36050e073addc82e10ac85fc41a65ed4d762428e46404  requirements.lock
b8288e4888cd248ef40cf7378085b2c1eca4393149f7886e2e403ba54edfcfae  src/__init__.py
f0685d8f1a8dfe983b3703cd7fc6ba52ae4f9b769b3afa671a9061e4ea346f03  src/analyze.py
b447636548f361de4357e08493522605157887bc46a5dd0bb02924499e7fea51  src/analyze_p26.py
d1d87bb1454280b2eaed6bf6c1005a09fdb1c3bbadb87be8dfd60585355a4fe0  src/common.py
d7beb5cf33ca8ed6f69d7f0f894884a84a9c2a98834221068d3ce5bb807170d8  src/mp_fit.py
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
