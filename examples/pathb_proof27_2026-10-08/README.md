# Path B Proof 27 — preregistered dose-response of affect bias on Melting Pot orchard_3

A proof on a micro-environment model (DeepMind Melting Pot `predator_prey__orchard_3`), in the Barrett/Huberman lineage only. The preregistration (sha256 `b48ae50cf679ed349c2a3a4303276eb1ee106cd4ea8cd53f6885b8ff6cadf344`) was published byte-identical in commit `f7bc40a40d2d4da1f4867985c564954efd7f1363` before any confirmatory seed ran. An earlier push (`919aa46`) was not byte-identical and was superseded before any confirmatory seed ran. Independent VERIFY: PASS.

## Headline

P26 compared balanced RGL with arms pushed all the way to one route. P27 asks what happens at smaller, graded doses. For five of the six affects (fight, freeze, capitulate, laugh, love_autopilot), success is lower where that affect takes a larger share of the policy's choices, and all five trend tests survive Holm. Flight's trend test is null.

A significant trend test shows a downward trend, not a smooth decline, and the per-dose rates are mostly steps. Fight drops to near zero at its first dose. Laugh drops at its first dose and is near zero from the second. Capitulate drops at its first dose, while its own-route share is still about 0.05, and then changes little. Freeze stays near or above balanced through MID and falls only at HIGH. Love_autopilot is lower at each dose.

Exploratory only: the smallest flight dose (0.355) and the smallest freeze dose (0.320) came out above balanced (0.250). Neither difference survives Holm (flight LOW Fisher p 0.029, Holm p 0.088), and flight LOW was the best of 18 dosed arms, so the true effect is likely smaller. It is a candidate hypothesis for a new preregistration, not a finding.

## Setup

- dm-meltingpot 2.4.1 `predator_prey__orchard_3`, focal prey slot 0, pretrained background bots, 1000-step episodes, CPU only.
- 19 arms (balanced plus 6 affects × 3 doses) × 200 episodes (seeds 28000–28199), 3800 total, 0 crashes, 0 missing, 0 reruns. Analysis is unpaired (episodes are not seed-reproducible).
- Primary success: got food at least once AND eaten at most 2 times by step 1000 (unchanged from P25/P26).
- Doses were chosen before the run from route-share calibration on burned seeds 98000–98019 only, targeting own-route shares near 0.25 / 0.50 / 0.75. Several picks were moved one grid step by the preregistered collision rule, and capitulate LOW landed at a share of about 0.05; all are disclosed in the prereg.
- Calibration: balanced 0.250 [0.190, 0.310], inside the locked 15–70% band.
- Primary analysis: Cochran-Armitage trend on success, scored by measured own-route share, one test per affect, Holm across the six.

## Primary results: trend tests (Holm across 6)

| affect | own-route share (bal / LOW / MID / HIGH) | z | Holm p | survives |
|---|---|---:|---:|---|
| fight | 0.035 / 0.370 / 0.642 / 0.843 | −10.49 | 5.9×10⁻²⁵ | yes |
| laugh | 0.000 / 0.136 / 0.793 / 0.954 | −9.30 | 7.3×10⁻²⁰ | yes |
| love_autopilot | 0.484 / 0.607 / 0.675 / 0.789 | −5.16 | 1.0×10⁻⁶ | yes |
| capitulate | 0.000 / 0.048 / 0.938 / 0.971 | −3.77 | 4.9×10⁻⁴ | yes |
| freeze | 0.000 / 0.447 / 0.958 / 0.997 | −3.27 | 0.0021 | yes |
| flight | 0.481 / 0.591 / 0.677 / 0.850 | −0.14 | 0.885 | no |

## Success by dose (95% bootstrap CIs; balanced = 0.250 [0.190, 0.310])

| affect | LOW | MID | HIGH |
|---|---|---|---|
| fight | 0.005 [0.000, 0.015] | 0.000 | 0.000 |
| laugh | 0.130 [0.085, 0.180] | 0.000 | 0.005 [0.000, 0.015] |
| capitulate | 0.145 [0.100, 0.195] | 0.115 [0.070, 0.160] | 0.095 [0.055, 0.140] |
| freeze | 0.320 [0.255, 0.385] | 0.275 [0.215, 0.340] | 0.055 [0.025, 0.090] |
| love_autopilot | 0.170 [0.120, 0.225] | 0.155 [0.105, 0.210] | 0.060 [0.030, 0.095] |
| flight | 0.355 [0.290, 0.420] | 0.320 [0.255, 0.385] | 0.265 [0.205, 0.330] |

Success moves for different reasons. Fight and laugh keep finding food (about 0.69–0.76) but stop staying safe, with safety near 0 from fight's first dose and laugh's second. Love_autopilot gets more food with each dose (0.610, 0.740, 0.825) while safety falls (0.445, 0.290, 0.155). Freeze and flight trade the other way: more dose means more safety and less food.

## Limitations

One environment; unpaired analysis; pretrained background bots; 200 episodes per arm; the trend test checks a linear component in own-route share, not the shape; dose targets were met only approximately (capitulate LOW especially); the success definition originated post-hoc in the P24 pilot (locked before P25 and unchanged since). Full data and logs are held in the project's private nest.

## Footer

clinical_claim: false · proof/micro-env/model
