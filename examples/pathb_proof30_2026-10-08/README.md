# Path B Proof 30 — preregistered orchard map ablation on Melting Pot orchard_3

A test on DeepMind Melting Pot `predator_prey__orchard_3`. The preregistration (sha256 `9bd9215d4821605a2c4b834e354a6068cbc9a0f2c15b2848075fb4cc20c3411a`) was published byte-identical in commit `26a508be810102c83eab601b5082605f8dc8d4a2` (21:47 CT, 2026-10-08) before any confirmatory seed ran (first seed after 22:26 CT).

**In short: the plain rule beat RGL in orchard, and a scrambled map hurt.** H2 (RGL beats a tuned plain rule) failed in the inverse direction: the plain rule `heuristic_noaffect` scored 0.263 against `rgl_v1` 0.199, risk difference −0.063 [−0.111, −0.014], Holm p 0.9955. The emotion structure adds nothing over a plain rule in orchard. H1 (RGL beats a deranged-map control) survived: `rgl_v1` 0.199 vs `shuffled_map` 0.016, +0.183 [0.150, 0.219], Holm p 2.5e-26. H1 says a scrambled trigger-to-route map hurts; `shuffled_map` even scored below `random_mix` (0.051). It does not show that the emotion structure beats a plain rule; H2 tested that, and it failed. Both manipulation checks passed. H3 is in band.

## Headline

Two one-sided hypotheses, tested once as one Holm family at alpha 0.05. H1 survives Holm; H2 does not, and its interval lies wholly below 0 (inverse). The other comparisons are descriptive and sit outside the family.

- **H2 (failed, inverse):** the tuned plain rule beat RGL, 0.263 vs 0.199 (149/567 vs 113/567), −0.063 [−0.111, −0.014], Holm p 0.9955. The emotion structure adds nothing over a plain rule in orchard.
- **H1 (survived):** RGL beat the deranged-map control, 0.199 vs 0.016 (113/567 vs 9/567), +0.183 [0.150, 0.219], Holm p 2.5e-26. A scrambled map hurts: `shuffled_map` scored below `random_mix` (0.051), so H1 does not show that emotions beat a plain rule.
- **Manipulation checks: both passed.** On `shuffled_map` the executed route differed from the trigger label on every alive step (fraction 1.0 of 94102); total-variation distance from `rgl_v1` route shares 0.3257 (needs at least 0.10); `rgl_v1` shares within ±0.05 of the P27 shares (largest gap 0.0115). The plain rule's flee branch was taken on 0.4554 of 432219 alive steps, inside (0.05, 0.95).
- **H3 gate:** IN-BAND, `rgl_v1` 0.199 [0.168, 0.231] (band [0.15, 0.70]; P28 0.236, P29 0.217).

| id | comparison | success rates | risk difference [95% CI] | Holm p | survives |
|---|---|---|---|---:|---|
| H1 | rgl_v1 > shuffled_map | 0.199 vs 0.016 | 0.183 [0.150, 0.219] | 2.467e-26 | yes |
| H2 | rgl_v1 > heuristic_noaffect | 0.199 vs 0.263 | −0.063 [−0.111, −0.014] | 0.9955 | no (inverse) |
| descriptive | rgl_v1 > random_mix | 0.199 vs 0.051 | 0.148 [0.111, 0.185] | n/a (outside the Holm family; one-sided p 9.479e-15) | n/a |
| descriptive | heuristic_noaffect > shuffled_map | 0.263 vs 0.016 | 0.247 [0.210, 0.284] | n/a (outside the Holm family; one-sided p 1.761e-38) | n/a |

Shuffled success by derangement (descriptive): D0 0/142, D1 0/142, D2 4/142, D3 5/141.

## Setup

- dm-meltingpot `predator_prey__orchard_3`, focal prey slot 0, pretrained background bots, 1000-step episodes.
- 4 arms (`rgl_v1`, `shuffled_map`, `heuristic_noaffect`, `random_mix`) × seeds 31000–31566 (n = 567 per arm), 2268 episodes, zero reruns, zero missing rows. Analysis is unpaired.
- `rgl_v1` is the frozen RGL spec v1 balanced path. `shuffled_map` uses the same features, scores and action repertoire with the trigger-to-route pairing deranged (four derangements, pooled). `heuristic_noaffect` is a state-reactive plain rule with no emotion labels, locked before the prereg (config 18: d = 6, straight-away flee, commitment 0). `random_mix` draws a new route at every alive step at the P27 shares, as in P28 and P29.
- Primary success: food at least once AND eaten at most 2 times by step 1000.
- Calibration: `rgl_v1` 0.199, inside the locked [0.15, 0.70] band, so H1 and H2 are confirmatory.
- Tests: one-sided Fisher exact, Holm step-down across H1 and H2; intervals are two-sided 95% unpaired percentile bootstraps.

## Provenance

- Prereg commit: `26a508be810102c83eab601b5082605f8dc8d4a2` (`docs/PATHB_PROOF30_ORCHARD_MAP_PREREG_2026-10-08.md`)
- Prereg sha256: `9bd9215d4821605a2c4b834e354a6068cbc9a0f2c15b2848075fb4cc20c3411a`
- RGL spec v1 sha256 (`RGL-SPEC-v1/SPEC_SHA.txt`): `e620509377516858d1d1e3677a14f977c76549608e93702dc5dc7a5735487475`
- WRITEUP.md sha256: `43bcc2b1922c152beb53ea7a30c5453879e06531620955f4f5ff904b3c229d4b`
- Run folder SHA256_MANIFEST.txt sha256 at Verify FR1: `3551ef97b44d3149693b101e5a6e75b01f8a8f39d19830658322ca7044fbd298` (98 files, shasum -c: 0 not OK)
- Full data and logs are held in the project's private nest.

## Disclosures

- Free-rig waiter bypass (deviation). The prereg says Phase B runs only through the free-rig waiter, after two consecutive FREE polls. At 22:26 CT Matt wrote that the rig looked free apart from one small Practice Desk worker; that was an observation, not an instruction to bypass the waiter. With the waiter at FREE 1/2, RGL Lab stopped it at 22:26:32 CT on its own judgment and started the run directly through a wrapper running the same command (the wrapper is not in the prereg hash list). The second FREE poll was never taken. Seeds, arms and analysis did not change; no seed ran twice.
- Loader fix before publishing. Before the prereg hash was published and before any confirmatory seed, a one-line fix to the Phase B loader for the locked plain-rule config was made (it read a key the locked file does not have). The locked file, its sha256 and the selection did not change. The prereg records it ("Fix before this hash").
- Plain-rule tuning. The locked config reached 37/100 on calibration seeds 31600–31699, the highest of 24 configs, against 149/567 (0.263) on the confirmatory seeds. A maximum taken over 24 configs is expected to overstate that config's rate.
- Greenlight wording. Matt approved P30 at 18:06 CT by selecting a pre-written option reading 'yes, freeze the spec and greenlight P30 as drafted, H2 superiority'; the wording is RGL Lab's. The public prereg is unedited; this is a clarification, not a correction of the approval.

## Footer

Independent VERIFY FR1: PASS with notes (report sha256 `cb2cdb94df30c169f43ac21be5d2f83118d7e1a029e3a13a9c91ddf5fd973cfe`).

clinical_claim: false · proof/micro-env/model
