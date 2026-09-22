# Path B Proof-19 — beat frozen — 2026-09-21 (timestamped)

**clinical_claim: false** · CPU-only synthetic proof micro-environment/model · published 2026-09-21 America/Chicago · VERIFY PASS
**Language:** proof / micro-environment / model — not a clinical claim, not PHI, and not evidence that AI has feelings. Barrett is an affect/prediction/action-readiness lineage cite only.

## Verified headline

Across 160 episodes (40 paired seeds × 4 conditions), mean success was:

**beat_residual 0.750 > frozen_thrash 0.725 > scripted 0.500 > blind 0.075.**

Mean waste was **0.975 for beat_residual versus 1.250 for frozen_thrash**.

## Paired beat-versus-frozen result

The two arms differed on 6/40 paired seeds. Beat had a success win on **1/40** seeds, lower waste on **5/40**, and higher waste on **0/40**. The success improvement is therefore narrow: one paired-seed outcome, moving the mean from 0.725 to 0.750. It should not be generalized beyond this sealed micro-environment and seed set.

## Mechanism and environment lock

Both arms began from the same fixed Proof-10 residual ranker. Beat added an intra-episode dual-timescale **SAFE_PRECRAFT option/habit**: a fast threat-residual EMA could replace a proposed grid-boundary bump with an in-bounds sweep while the agent was unarmed and still gathering. This was **not an LR retune** and made no cross-episode ResidualMap writes.

The environment was byte-identical to Proof-10. The run used CPU only. SAFE_PRECRAFT fired 12 times total; frozen and beat each recorded zero engage holds.

## Interpretation limits

This result is a narrow machine proof in one synthetic Minecraft-shaped micro-environment. It does not establish a universal policy advantage, medical or clinical efficacy, consciousness, or that AI has feelings. Barrett is cited only as lineage for the affect/prediction/action-readiness framing. The proof is not full Minecraft or a Mojang product.

## Content anchors (SHA256)

| Artifact | SHA256 |
|---|---|
| Proof-10 environment | `ac52ecc98dfd907ae7c9c56ba89f6ce33283956a67e08be3dc521aa1f0d3d518` |
| episodes CSV | `f022970622f16b4685f73fdfa30ac4187b8d05e55a525fbac518160947ec3dc6` |
| summary CSV | `31d5f90c620ec34828df4d7affc54a63f221aa5978ca584a90b0126741bf3eff` |
| WRITEUP | `b87d90ccf15cf05804debfd02573bcfa1efa99d6539c82ddd5a8e2bdc7fac025` |
| policies | `f615ce7065c4afe4ee2e1feb0e67d0a281d21fff18d9a7e046858a8c91a1fd6e` |

## Related

- Index: [PATHB_SCOREBOARD.md](PATHB_SCOREBOARD.md)
- Validity: [VALIDITY_REPRO.md](VALIDITY_REPRO.md)
- Packet: [../examples/pathb_proof19_2026-09-21/README.md](../examples/pathb_proof19_2026-09-21/README.md)
