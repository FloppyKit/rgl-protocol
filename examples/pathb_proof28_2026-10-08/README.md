# Path B Proof 28 — preregistered small-caution doses and a random-mix control on Melting Pot orchard_3

A proof on a micro-environment model (DeepMind Melting Pot `predator_prey__orchard_3`). The preregistration (sha256 `c9054a181cf7b66532d43e573767a48feda5d6565e5c59077c44d81f2cee5b53`) was published byte-identical in commit `ca3cfcb3801bf4ebb5643a560ccb8b5fc900d166` before any confirmatory seed ran.

## Headline

Three one-sided hypotheses, tested once as one Holm family at alpha 0.05. All three survive Holm.

- **H1:** flight at bias 0.05 beats balanced RGL on primary success.
- **H2:** freeze at bias 0.30 beats balanced RGL on primary success.
- **H3:** balanced RGL beats a random mix that draws routes at balanced's frozen average route shares.

| id | comparison | success rates | risk difference [95% CI] | Holm p | survives |
|---|---|---|---|---:|---|
| H1 | flight_b0.05 > balanced_rgl | 0.309 vs 0.236 | 0.072 [0.021, 0.125] | 0.007578 | yes |
| H2 | freeze_b0.30 > balanced_rgl | 0.293 vs 0.236 | 0.056 [0.005, 0.108] | 0.01839 | yes |
| H3 | balanced_rgl > random_mix | 0.236 vs 0.039 | 0.198 [0.160, 0.238] | 2.202e-23 | yes |

Flight at bias 0.05 was the best of 18 dosed arms in P27, so the gap that got noticed was likely larger than a fresh run would show. H2's interval reaches down to 0.005, so the freeze gap could be very small; freeze at 0.30 was also chosen after seeing P27, so the same winner's-curse caution applies.

The random mix draws a new route at every alive step, so it matches balanced's average route shares but not how long balanced stays on one route. H3 shows that balanced's state-based choice beats rate-matched per-step random choice; it does not show that balanced beats a random policy that also matches dwell times.

## Setup

- dm-meltingpot `predator_prey__orchard_3`, focal prey slot 0, pretrained background bots, 1000-step episodes.
- 4 arms (`balanced_rgl`, `flight_b0.05`, `freeze_b0.30`, `random_mix`) × seeds 29000–29566 (n = 567 per arm), 2268 episodes. Analysis is unpaired.
- Primary success: food at least once AND eaten at most 2 times by step 1000.
- Calibration: balanced 0.236, inside the locked [0.15, 0.70] band, so all three tests are confirmatory.
- Tests: one-sided Fisher exact, Holm step-down across three; intervals are two-sided 95% unpaired percentile bootstraps.

## Provenance

- Prereg commit: `ca3cfcb3801bf4ebb5643a560ccb8b5fc900d166`
- Prereg sha256: `c9054a181cf7b66532d43e573767a48feda5d6565e5c59077c44d81f2cee5b53`
- Run folder SHA256_MANIFEST.txt sha256: `06256d26af50f0448f7986cc0c97591896b805809af468625038b544ee77d657` (shasum -c: 0 not OK)
- Full data and logs are held in the project's private nest.

## Footer

Independent VERIFY FR0: PASS with notes (report sha256 `ded649384892299880c4645f8d2f81c29d57b3de9efb21fbf674ba0299fd6dd7`).

clinical_claim: false · proof/micro-env/model
