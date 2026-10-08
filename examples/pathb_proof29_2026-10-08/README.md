# Path B Proof 29 — preregistered dwell-matched random control on Melting Pot orchard_3

A test on DeepMind Melting Pot `predator_prey__orchard_3`. The preregistration (sha256 `6d05a6639964eaf7ec60183045c18325e1b77699df5f4a142bd64af2a67f0edb`) was published byte-identical in commit `1d3e1029ada9cd9946b8718317cdd778ec8129b7` (14:11 CT, 2026-10-08) before any confirmatory seed ran (first seed 14:43 CT).

## Headline

Two one-sided hypotheses, tested once as one Holm family at alpha 0.05. Both survive Holm. The anchor comparison is descriptive and sits outside the family.

- **H1 (primary):** balanced beat a dwell-matched random control (love dwell undershot), 0.217 vs 0.049, +0.168 [0.131, 0.206], Holm p 2.2e-17.
- **Manipulation check: Matched False.** dwell_random's love runs averaged 8.88 steps against balanced's 11.79 (about 25% shorter, outside the pre-stated ±20%); love share 0.431 vs 0.481 (gap 0.0499, inside ±0.05); fight and flight matched. As pre-stated, the miss does not change, exclude or relabel H1/H2.
- **H2:** dwell-matched random beat per-step random, 0.049 vs 0.016, +0.034 [0.014, 0.055], Holm p 0.0011. Both rates are low.
- **H3 gate:** IN-BAND, balanced 0.217 [0.183, 0.250] (P28 0.236).
- **Descriptive (outside the Holm family):** balanced vs random_mix +0.201 [0.166, 0.236].

| id | comparison | success rates | risk difference [95% CI] | Holm p | survives |
|---|---|---|---|---:|---|
| H1 | balanced_rgl > dwell_random (love dwell undershot) | 0.217 vs 0.049 | 0.168 [0.131, 0.206] | 2.174e-17 | yes |
| H2 | dwell_random > random_mix | 0.049 vs 0.016 | 0.034 [0.014, 0.055] | 0.00109 | yes |
| anchor (descriptive) | balanced_rgl > random_mix | 0.217 vs 0.016 | 0.201 [0.166, 0.236] | n/a (outside the Holm family; one-sided p 7.964e-30) | n/a |

The manipulation check missed: dwell_random's love runs averaged 8.88 steps against balanced's 11.79, outside the pre-stated ±20% band. So H1 is a win over a dwell-matched random control whose love dwell undershot, not over a perfect match.

Exploratory (Verify, not preregistered): the love undershoot cannot plausibly explain H1. Within dwell_random, success is associated with longer love dwell, but even a naive extrapolation over the 2.9-step gap accounts for at most about +0.043 (upper +0.068) of the +0.168 gap. dwell_random episodes whose love dwell reached 11.79 steps still succeeded only 0.156 of the time (n = 77), against 0.217 for balanced. Most of the shortfall is a consequence of being eaten rather than a cause: 18% of dwell_random love runs end in a death (1551 of 8653), against 3 of 12,205 in balanced, and a death ends a run.

## Setup

- dm-meltingpot `predator_prey__orchard_3`, focal prey slot 0, pretrained background bots, 1000-step episodes.
- 3 arms (`balanced_rgl`, `dwell_random`, `random_mix`) × seeds 30000–30566 (n = 567 per arm), 1701 episodes, zero reruns, zero missing rows. Analysis is unpaired.
- `dwell_random` was built to match balanced's frozen calibration route shares, run lengths and switch order, but not when a run starts relative to the state; on confirmatory seeds it matched the shares and the fight and flight run lengths, not the love run length. `random_mix` draws a new route at every alive step at P27 shares, as in P28.
- Primary success: food at least once AND eaten at most 2 times by step 1000.
- Calibration: balanced 0.217, inside the locked [0.15, 0.70] band, so H1 and H2 are confirmatory.
- Tests: one-sided Fisher exact, Holm step-down across H1 and H2; intervals are two-sided 95% unpaired percentile bootstraps.
- **Design fix before freeze:** death ends a dwell run (was censored); refit on the same 100 calibration traces before the prereg push (1d3e102, 14:11 CT) and before any confirmatory seed (14:43 CT).

## Provenance

- Prereg commit: `1d3e1029ada9cd9946b8718317cdd778ec8129b7`
- Prereg sha256: `6d05a6639964eaf7ec60183045c18325e1b77699df5f4a142bd64af2a67f0edb`
- Run folder SHA256_MANIFEST.txt sha256: `29fc9802307456c0cdc5e00fcc631a5d3718fbff2865fa158ebbf4f642a38b9e` (shasum -c: 0 not OK)
- Full data and logs are held in the project's private nest.

## Disclosures

- Erratum (prereg 1d3e102, line 183): the prereg says Matt approved the death-as-run-end design fix at 14:08 CT on 2026-10-08. RGL Lab approved it itself at 14:08 CT, inside the P29 greenlight and before the prereg freeze and push; Matt confirmed it afterward, at 17:13 CT. The prereg stays unedited because its hash is published.

## Footer

Independent VERIFY FR1b: PASS with notes (report sha256 `a7a871805d14ad6c1bace11f56e9b398dccce6bd6a65f2b318ff4d14870be5da`).

clinical_claim: false · proof/micro-env/model
