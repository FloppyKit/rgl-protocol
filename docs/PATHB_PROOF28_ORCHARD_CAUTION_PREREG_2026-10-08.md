# PREREG — GO-RGL-PATHB-PROOF-28

Frozen 2026-10-08T08:39:08-0500, before any seed in 29000-29566. clinical_claim: false. No PHI. CPU/headless only, no GPU. proof/micro-env/model. Barrett/Huberman lineage only. Inverse, null, and inconclusive results are all reported. No soft goalposts.

## Why
P26 found that six single-route policies at bias +2.15 lost to mixed balanced, all six surviving Holm. P27 asked the graded question. Five trend tests show lower success where that route's share is higher, and the per-dose shapes are steps, not a smooth decline. Flight's trend test is null (Holm p 0.885). Flight at bias 0.05 (the P27 LOW dose) had success 0.355 against balanced 0.250, Fisher p 0.029, within-affect Holm 0.088, so it did not survive. Freeze at bias 0.30 stayed above balanced (0.320) and its pairwise test also did not survive. Those two doses were the best-looking cautious arms, and flight LOW was the best of 18 dosed arms. That is winner's curse: the true gap is likely smaller than the gap that got noticed. P28 tests those two doses once, in a three-test family, and adds a random mix so a win is not just "not the balanced scores."

Numbers above are from `GO-RGL-PATHB-PROOF-27/WRITEUP.md` and `nest/box_sync_2026-10-08/VERIFY_GO-RGL-PATHB-PROOF-27.md`. The biases are not retuned.

## Design
- Environment: dm-meltingpot 2.4.1 `predator_prey__orchard_3`, focal prey slot 0, unpaired, 1000-step episodes, pretrained background bots. Same scorer family as P26/P27. `src` was copied from `GO-RGL-PATHB-PROOF-27` and that folder was not modified. `requirements.lock` sha256 is `db3bd30d4c0d0713e1e36050e073addc82e10ac85fc41a65ed4d762428e46404`.
- Base scores, features, route-to-action mapper, tie-break order, and outcome fields are unchanged. `flight_b0.05` adds 0.05 to flight only. `freeze_b0.30` adds 0.30 to freeze only. Bias 0 matches `balanced_rgl`.
- Arms, exactly four: `balanced_rgl`, `flight_b0.05`, `freeze_b0.30`, `random_mix`.
- `random_mix` picks a route at each alive step with the probabilities below. It does not use the route scores. The probabilities are constants in `src/mix_shares.py` and `results/route_shares_p27.json`. They are not re-estimated from P28 outcomes.
- Shares: mean, over the 200 `balanced_rgl` episodes in `GO-RGL-PATHB-PROOF-27/results/episodes.csv`, of `count_route / sum of the six route counts`. The script `src/freeze_route_shares.py` indexes `policy` and `count_*` only. Headers containing food, eaten, or success were not indexed. The six means sum to 1.

| route | frozen share | 4 d.p. check |
|---|---:|---:|
| fight | 0.03533432781622072 | 0.0353 |
| flight | 0.4806579129663373 | 0.4807 |
| freeze | 0.0 | 0.0000 |
| capitulate | 0.0002561226358477411 | 0.0003 |
| laugh | 0.0 | 0.0000 |
| love | 0.48375163658159426 | 0.4838 |

- The 4 d.p. line matches the P27 write-up check (fight 0.0353, flight 0.4807, freeze 0.0000, capitulate 0.0003, laugh 0.0000, love 0.4838). That line was a check, not the source of the shares.
- Seeds: 29000-29566 (n = 567 per arm, 2268 episodes). Blocks 24000-24999, 26000-26099, 27000-27249, 28000-28199, and 98000-98999 are not used. No seed in 29000-29566 has been run.
- n = 567 is the smallest per-arm n with 80% power to detect an absolute gap of +0.08 over p0 = 0.25, one-sided, under Holm. The power calculation uses the strictest step-down threshold, alpha = 0.05/3. It does not read any episode file. Achieved power at n = 567 is 0.8006. At n = 566 it is below 0.80. P27's ruler is 3800 episodes in 11285.4 s with 8 workers (2.9698 s per episode). Four arms at this n are about 6735.6 s (1.87 h). The cap is 6 h (21600 s), which would fit 1818 per arm. The 80% target fits, so n is not cut down. The gap claimed as powered stays +0.08.
- Primary success: `food_1000 >= 1` AND `times_eaten <= 2`.
- Calibration band for balanced: [0.15, 0.70]. Outside that band the label is OUT-OF-BAND and every comparison is exploratory, still fully reported. Inside the band on the confirmatory seeds, the three tests are confirmatory.
- Secondary, descriptive only: food rate (`food_1000 >= 1`), safety rate (`times_eaten <= 2`), mean times eaten, mean food, own-route share. Flight's own route is flight. Freeze's own route is freeze. Balanced and random_mix have no single own route; all six shares are reported.
- No exclusions. A crashed episode gets one rerun of that arm and seed, replacing that row. Report the count. The analyzer rejects a second row for the same arm and seed. No extra seeds.
- `verify-logs/writeup_gate.py` is the P27 file whose sha256 is `629eb12f4b73e18ad197ba7d8b2537b5eccaef958bf9ed2675ab5446927e0f83`.

## Analysis
- Estimator and tests are `src/analyze_p28.py`, hashed below.
- Primary family: three one-sided Fisher exact tests. Holm is step-down and monotone, family alpha 0.05.
  - H1: flight_b0.05 success rate > balanced_rgl. Risk difference = p(flight_b0.05) - p(balanced_rgl).
  - H2: freeze_b0.30 success rate > balanced_rgl. Risk difference = p(freeze_b0.30) - p(balanced_rgl).
  - H3: balanced_rgl success rate > random_mix. Risk difference = p(balanced_rgl) - p(random_mix).
- Each risk difference also has a two-sided 95% unpaired percentile bootstrap interval (10,000 resamples), so a reversal is visible. A reversal is a result.
- Cohen's h = 2*arcsin(sqrt(p_arm)) - 2*arcsin(sqrt(p_baseline)), same direction as the risk difference.
- Bootstrap seeds, pinned: per-arm mean intervals use numpy Generator seed 28028. Risk-difference intervals use seed 28029 + hypothesis index, with H1 = 0, H2 = 1, H3 = 2.
- The analyzer fails on duplicate (arm, seed) rows, unknown arms, and seeds outside the resolved range. It does not keep the last duplicate. The confirmatory range is exactly 29000-29566. A scratch range is accepted only when every seed is below 29000. The phase A scratch file is `verify-logs/scratch_episodes.csv`, seeds 100-101 only. That file is not a result.
- random_mix probabilities used at run time are the frozen constants above, not shares computed from P28 rows.

## Winner's curse
Flight at bias 0.05 was chosen because it was the best of 18 dosed arms. Powering at +0.08 is already a smaller gap than the observed +0.105, and a null is expected to be possible.

## Confirmatory data
Seeds 29000-29566 have not been run. The analyzer was exercised on a synthetic scratch CSV with seeds 100-101 only. That file is not a result.

## sha256
Taken after `src/__pycache__` was deleted. `src/power.py` and `src/analyze_p28.py` are in this list.
```
db3bd30d4c0d0713e1e36050e073addc82e10ac85fc41a65ed4d762428e46404  requirements.lock
b8288e4888cd248ef40cf7378085b2c1eca4393149f7886e2e403ba54edfcfae  src/__init__.py
f0685d8f1a8dfe983b3703cd7fc6ba52ae4f9b769b3afa671a9061e4ea346f03  src/analyze.py
b447636548f361de4357e08493522605157887bc46a5dd0bb02924499e7fea51  src/analyze_p26.py
81f6b2e6ae8536578ac2ab812c3b69e1668372ec3ec06aa310f4245dfbcadc9d  src/analyze_p27.py
79e3346230ed69cb3b11de80a4d784f93903195bbd3031ae9fe180db603e6d9b  src/analyze_p28.py
0276d309c81c33d7d48ca94fc58973667fb68229fde6003410d160f3b9447408  src/calibrate_doses.py
a9eff92347cf675241bc06d7c1dddcdf46b63c8367e3c8f3e63fb46db048a016  src/common.py
574bf511d143c4ae9d28be61e81e64f3e41e8fb5e8dfc11ca4fe46b59a14e3a0  src/freeze_route_shares.py
157a9bac5089f86d95b34dc067ad62c4ef00c6cb0cceb00509da41ed122a65e3  src/mix_shares.py
bff5ce78cabe2f875f18427400c75a80a623b8a3bd4c6553effa955cc8b8c101  src/mp_fit.py
459bfbf7dfaa21fee7fb44c1389b3daf05cb7b538c41bcd80e58e9f018eaaa91  src/mpe_fit.py
4211dc2ae8cd19f641fbfe82502bebd67cc5bcbf337739671652f1d376be293e  src/p21_port/__init__.py
81186936a8e9be148e753f98477ef48df0f16ff8565634d451e4956778e04d6d  src/p21_port/features.py
d3a01bc7db92c4afca7dd87982a7413395a8156aea1b6c842f6ea48f00f20926  src/p21_port/harness.py
b3774ecab18725ef7a04d8d74c479a35d95ec648abcbb1cb667b457e7b232a06  src/p21_port/policies.py
2d8d17deafa040bd87c80839ca4da945d84d2d9fab61679274f6f3e75d234bec  src/p23_port/__init__.py
25caff971daf0d5468306657762170a5f4f5e4051a025500ade54d7ead1c3277  src/p23_port/features.py
68e3acb2d6406424b571f1e5cc2e7919429c77c081e27159f720c571a3b1691e  src/p23_port/harness.py
dffc85ba9ff5781dde102013fc1e3c7ffb720ade6ab882f184b454fbeccae690  src/p23_port/policies.py
30a947a10262a8ef48bd2be54fdfe6f958e0a3cff71a4158ad039e9cb399be7a  src/power.py
606305d5bab74f90126f684042a18aff4e9fba659a1bb6f8ff9268177b314cea  src/report_tables.py
```
