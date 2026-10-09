# Path B Proof 31 — preregistered map and ally ablation on Melting Pot open_3

A test on DeepMind Melting Pot `predator_prey__open_3` (world W1, focal prey role). The preregistration (sha256 `51457170183d66df38c18f03d92f36828bd9927bb5cb2555ed8b9614d1ef0eef`) was published byte-identical in commit `245334e25fad0089a813676dafc492e96b0e17e9` (09:11 CT, 2026-10-09) before any confirmatory seed ran (first seed 09:21:41 CT).

**In short: two results cut against RGL and lead here with equal weight.** First, H2 (RGL beats a locked plain rule) failed in the inverse direction: the plain rule `heuristic_noaffect` succeeded on 328/567 (0.578) against `rgl_v1` 117/567 (0.206), risk difference −0.372 [−0.423, −0.319], Holm p 1.0. Second, removing RGL's ally branch raised success: `love_noally` succeeded on 242/567 (0.427) against `rgl_v1` 0.206, risk difference +0.220 [0.168, 0.273], one-sided p 7.5e-16 (descriptive, outside the Holm family). H4 (removing the ally branch costs allies) did not survive: allies eaten per episode 42.757 (`love_noally`) vs 42.642 (`rgl_v1`), difference +0.115 [−0.159, 0.379], Holm p 0.402, so a cost of the ally branch is not shown. H1 survived, and what it shows is that a scrambled map hurts: `rgl_v1` 0.206 vs the deranged-map control `shuffled_map` 0.014, Holm p 2.6e-28. `shuffled_map` (0.014) also scored below `random_mix` (0.106); that comparison is descriptive and was not tested. H1 does not show that emotions beat a plain rule; H2 tested that, and it failed.

## Headline

Three one-sided hypotheses (H1, H2, H4), tested once as one Holm family at alpha 0.05 (first step 0.05/3). The no-grass world W2 was dropped at its feasibility gate, so H3 was not tested. The other comparisons are descriptive and sit outside the family.

- **H2 (failed, inverse):** the locked plain rule beat RGL, 0.578 vs 0.206 (328/567 vs 117/567), −0.372 [−0.423, −0.319], Holm p 1.0. The interval lies wholly below 0. Same direction as P30, by a wider margin.
- **`love_noally` (descriptive, same prominence):** removing the ally branch raised primary success, 0.427 vs 0.206 (242/567 vs 117/567), +0.220 [0.168, 0.273], one-sided p 7.5e-16. This counts against the ally branch's value for the focal prey on open_3.
- **H4 (null):** allies eaten per episode 42.757 vs 42.642, difference +0.115 [−0.159, 0.379], Holm p 0.402. Point estimate in the predicted direction; a cost of the ally branch is not shown at this n.
- **H1 (survived; a scrambled map hurts):** 0.206 vs 0.014 (117/567 vs 8/567), +0.192 [0.159, 0.228], Holm p 2.6e-28. `shuffled_map` (0.014) also scored below `random_mix` (0.106), descriptive and untested. H1 does not show that emotions beat a plain rule.
- **Band:** IN-BAND, `rgl_v1` 0.206 [0.173, 0.240] (band (0.05, 0.90)).
- **Manipulation checks: three of four passed; the `rgl_v1` share check missed.** On `shuffled_map` the executed route differed from the trigger label on every alive step (fraction 1.0 of 151,139); total-variation distance from `rgl_v1` shares 0.6989 (needs at least 0.10). The plain rule's flee branch was taken on 0.3796 of 391,892 alive steps, inside (0.05, 0.95). `love_noally` never took the ally line (`count_love_ally` 0 on all 567 episodes) and its shares stayed within ±0.05 of `rgl_v1` (largest gap 0.0430). The `rgl_v1` route shares missed the ±0.05 sanity bar against the n = 30 screen (fight gap 0.0706, flight gap 0.0576). Per the prereg, that miss is a limitation, not a relabel: the band label stands and H1, H2 and H4 stay confirmatory. It does not trigger H1's "missed" clause, which is keyed to the shuffled-map check.

| id | comparison | rates / means | difference [95% CI] | Holm p | survives |
|---|---|---|---|---:|---|
| H2 | rgl_v1 > heuristic_noaffect | 0.206 vs 0.578 | −0.372 [−0.423, −0.319] | 1.0 | no (inverse) |
| descriptive | love_noally vs rgl_v1 (primary success) | 0.427 vs 0.206 | +0.220 [0.168, 0.273] | n/a (outside the Holm family; one-sided p 7.487e-16) | n/a |
| H4 | love_noally loses more allies than rgl_v1 | 42.757 vs 42.642 allies/episode | +0.115 [−0.159, 0.379] | 0.4021 | no |
| H1 | rgl_v1 > shuffled_map | 0.206 vs 0.014 | +0.192 [0.159, 0.228] | 2.564e-28 | yes |
| descriptive | rgl_v1 > random_mix | 0.206 vs 0.106 | +0.101 [0.058, 0.143] | n/a (outside the Holm family; one-sided p 1.974e-06) | n/a |
| descriptive | heuristic_noaffect > shuffled_map | 0.578 vs 0.014 | +0.564 [0.524, 0.605] | n/a (outside the Holm family; one-sided p 7.543e-115) | n/a |

Shuffled success by derangement (descriptive): D0 0/142, D1 0/142, D2 3/142, D3 5/141.

## Setup

- dm-meltingpot `predator_prey__open_3`, focal prey role, pretrained background bots, 1000-step episodes.
- 5 arms (`rgl_v1`, `shuffled_map`, `heuristic_noaffect`, `random_mix`, `love_noally`) × seeds 32000–32566 (n = 567 per arm), 2835 episodes, zero reruns, zero missing rows. Analysis is unpaired.
- `rgl_v1` is the frozen RGL spec v1 path. `shuffled_map` uses the same features, scores and action repertoire with the trigger-to-route pairing deranged (four derangements, pooled). `heuristic_noaffect` is the state-reactive plain rule locked in P30 (config 18), with no emotion labels. `random_mix` draws a route at every alive step at the P27 shares. `love_noally` is `rgl_v1` with the ally line of the love branch removed.
- Primary success: food at least once AND eaten at most 2 times by step 1000.
- Tests: one-sided Fisher exact for H1 and H2, one-sided Welch t-test for H4, Holm step-down across H1, H2, H4; intervals are two-sided 95% unpaired percentile bootstraps (10,000 resamples).

## Provenance

- Prereg commit: `245334e25fad0089a813676dafc492e96b0e17e9` (`docs/PATHB_PROOF31_OPEN3_NOGRASS_PREREG_2026-10-09.md`)
- Prereg sha256: `51457170183d66df38c18f03d92f36828bd9927bb5cb2555ed8b9614d1ef0eef`
- RGL spec v1 sha256 (`RGL-SPEC-v1/SPEC_SHA.txt`): `e620509377516858d1d1e3677a14f977c76549608e93702dc5dc7a5735487475`
- RGL v2 pre-statement sha256 (`RGL-SPEC-v2-PRESTATEMENT/PRESTATEMENT_SHA.txt`, frozen 08:00 CT 2026-10-09): `32b70b13a7cfd64cb836e84aa4be1072ded796e381f4c97a5cc085ce1cd4e13d`
- WRITEUP.md sha256: `fe89156d5c5df9a0ae1c94e0c4478f8b75f50c549c9e6e117f3c273e5b25371e`
- Run folder SHA256_MANIFEST.txt sha256 at Verify FR1: `26dc3947b845c1bddaa44b0aeb0cfc151930f9774b8b874d04379b27421c02dd` (141 files, shasum -c: 0 not OK)
- Full data and logs are held in the project's private nest.

## Disclosures

- W2 dropped at the F4 gate. The no-grass world W2 failed the pre-stated feasibility gate: both baselines scored 0/30 on primary success (`heuristic_noaffect` and `random_mix`; rule: at least one above 0.05). The pre-stated fallback was applied as written: W2 dropped, P31 ran W1 only, Holm over H1, H2, H4 with a first step of 0.05/3. H3 (prediction c) is deferred to a later GO. This is a failed world, not a retune.
- Unpaired comparisons. Melting Pot is not seed-reproducible, so all comparisons are unpaired; seeds are bookkeeping.
- Plain-rule screen. The plain rule (config 18) scored 0.667 (20/30) in the open_3 screen (burned seeds 40000–40029), against 0.578 (328/567) on the confirmatory seeds. Config 18 was chosen on orchard calibration in P30, not tuned on open_3.
- Post-review code edits. After reviewing the Phase A1 agent's work and before the prereg hash, RGL Lab edited code: a per-episode checkpoint in the fit script, the W2-drop switch (with the matching test change), and the alpha 0.05/3 row in the power table. Pre-edit copies are kept in the run folder; the edited files are in the prereg hash list. None touches scoring or analysis.
- Greenlight wording. Matt approved P31 at 07:58 CT on 2026-10-09 by selecting a pre-written option reading "yes, greenlight P31 with your defaults and freeze the v2 pre-statement"; the choice is Matt's, the wording is RGL Lab's.
- This is a proof on a micro-environment with a model policy. Route names are machine option labels, not claims that a model has feelings, and nothing here is a clinical result.

## Footer

Independent VERIFY FR1: PASS with notes (report sha256 `82c32e9afee024d1637a85ab31c225db063f3aca8f96a9cbc97dc4d989ac4200`).

clinical_claim: false · proof/micro-env/model
