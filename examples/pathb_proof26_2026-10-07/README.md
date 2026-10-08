# Path B Proof 26 — preregistered 7-arm affect-bias sweep on Melting Pot orchard_3

A proof on a micro-environment model (DeepMind Melting Pot `predator_prey__orchard_3`), in the Barrett/Huberman lineage only. The preregistration (sha256 `001d35c7401b452d1f0f6f39d0d8d454f956a9890d13ee2f3a7c218cddbeb721`) was published byte-identical in commit `574ca21904fa60f58b0d23565937ed0be1caba15` before any confirmatory seed ran. Independent VERIFY: PASS.

## Headline

The balanced RGL policy had higher primary success than every one of the six affect-biased arms, and all six differences survive Holm correction. At the +2.15 bias, each biased arm chose its own route on 100% of steps, so this compares single-route policies with a mixed balanced policy. It is not a graded affect effect.

## Setup

- dm-meltingpot 2.4.1 `predator_prey__orchard_3`, focal prey slot 0, pretrained background bots, 1000-step episodes, CPU only.
- 7 arms × 250 episodes (seeds 27000–27249), 1750 total, 0 crashes, 0 missing. Analysis is unpaired (episodes are not seed-reproducible).
- Primary success: got food at least once AND eaten at most 2 times by step 1000.
- Calibration: balanced 0.228 [0.180, 0.280], inside the locked 15–70% band (revised from 30–70% after the P25 re-pilot and before P26; disclosed in the prereg).

## Results (95% bootstrap CIs; Fisher exact vs balanced, Holm at family α 0.05)

| arm | success | food | safety | RD vs balanced | Holm p |
|---|---|---|---|---|---|
| balanced_rgl | 0.228 [0.180, 0.280] | 0.632 | 0.488 | — | — |
| flight_biased | 0.136 [0.096, 0.180] | 0.140 | 0.996 | −0.092 [−0.160, −0.024] | 0.0105 |
| capitulate_biased | 0.088 [0.056, 0.124] | 0.448 | 0.404 | −0.140 [−0.204, −0.076] | 4.8×10⁻⁵ |
| fight_biased | 0.000 | 0.700 | 0.004 | −0.228 [−0.280, −0.176] | 2.3×10⁻¹⁸ |
| freeze_biased | 0.000 | 0.000 | 0.992 | −0.228 [−0.280, −0.176] | 2.3×10⁻¹⁸ |
| laugh_biased | 0.000 | 0.724 | 0.000 | −0.228 [−0.280, −0.176] | 2.3×10⁻¹⁸ |
| love_autopilot_biased | 0.000 | 0.932 | 0.008 | −0.228 [−0.280, −0.176] | 2.3×10⁻¹⁸ |

Each single-route arm fails a different way: love_autopilot, fight and laugh find food but are eaten far too often; freeze and flight stay safe but rarely or never eat. On food vs safety, the non-dominated set is balanced_rgl, flight_biased and love_autopilot_biased, and balanced has the highest joint success.

## Limitations

One environment; unpaired analysis; pretrained background bots; the success definition originated post-hoc in the P24 pilot (locked before P25 and unchanged since); at +2.15 every biased arm collapsed to one route, so P26 says nothing about smaller, graded biases (planned as a follow-up). Full data and logs are held in the project's private nest.

## Footer

clinical_claim: false · proof/micro-env/model
