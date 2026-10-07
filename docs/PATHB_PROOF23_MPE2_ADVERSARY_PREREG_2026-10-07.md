# Path B Proof-23: preregistered MPE2 simple_adversary_v3 replication (inconclusive), 2026-10-07

Not evidence that AI has feelings. Barrett and Huberman are lineage citations only.

Same unified affect-route bias design as Proof-21/22 (laugh = P22 fixed-chirality), ported to Farama **MPE2** `simple_adversary_v3` (`mpe2==1.1.1`). The environment was chosen because it keeps a native goal, a goal-competing adversary and an ally. The preregistration was frozen with SHA256 before the run. There are **1000 fresh paired seeds** per arm (23000–23999), and the success proxy (goal + protection) is unchanged.

## Headline: INCONCLUSIVE

**The result is inconclusive.** The P21 love-above-balanced result did not replicate in this environment, and it did not invert either.

- **Love vs balanced:** RD **+0.001** [−0.005, +0.007] (love 0.031 [0.021, 0.042], balanced 0.030 [0.020, 0.041]); Cohen's h 0.006; exact McNemar Holm p **1.00**.
- **Freeze < balanced** is the only comparison that survives Holm (RD −0.029, Holm p 2e-08).
- **All arms are near the floor** (success ≤ 0.050). In `simple_adversary` the scripted adversary infers the hidden goal by following the good agents, so a goal-seeking agent leads the threat to the goal (descriptive, not a tested mechanism). This is an **environment fit limitation**: the scenario leaves little room to separate arms on the frozen success proxy.
- **Post-hoc Holm makes P21's love headline inconclusive:** re-analysed with the same statistics, P21 love vs balanced has Holm p **0.087**.
- **The prereg SHA256 was frozen locally** (2026-10-07 12:34 CDT, before the run) **with no external timestamp**. This publication is the first public record of the hash.
- Fight and laugh had the highest point estimates (0.050), but neither survived Holm. The P21 ranking was not recovered (Kendall τ-b 0.55, p 0.125). The success-qualified frontier (≥ 0.90) is empty.

## Per-arm success (n = 1000)

| Arm | Success | 95% CI |
|---|---:|---|
| Fight | 0.050 | [0.037, 0.064] |
| Flight | 0.029 | [0.019, 0.040] |
| Freeze | 0.001 | [0.000, 0.003] |
| Capitulate | 0.025 | [0.016, 0.035] |
| Laugh | 0.050 | [0.037, 0.064] |
| Love/autopilot | 0.031 | [0.021, 0.042] |
| Balanced RGL | 0.030 | [0.020, 0.041] |

## Content anchors (SHA256)

| Artifact | SHA256 |
|---|---|
| PREREG | `486361837f872e1bdab7f0dcc95a68a48c5c29f037f141564c66407023a3c6b7` |
| PROXY_DEFINITIONS | `a35f63bb117fe6b3dca5797733e1f672fa25a847e774ddb90cf597f6e8a41226` |
| summary CSV | `ccb137b0563885b3d22259086caa94c17f982d32f9f06081cf9f9a50728d14c4` |
| WRITEUP | `42cb821cb3c82edd0f5358374e3d2d848f572e48d0152a72eae698886b06b1e7` |

## Related
- [PATHB_PROOF21_MPE2_UNIFIED_AFFECT_2026-09-21.md](PATHB_PROOF21_MPE2_UNIFIED_AFFECT_2026-09-21.md) · [PATHB_PROOF22_MPE2_LAUGH_REPAIR_2026-09-21.md](PATHB_PROOF22_MPE2_LAUGH_REPAIR_2026-09-21.md) · [PATHB_SCOREBOARD.md](PATHB_SCOREBOARD.md)

## Footer

clinical_claim: false · no PHI · CPU/headless · VERIFY PASS (FR4, incl. proxy inspection) · public timestamp 2026-10-07  
Language: proof / micro-env / model; community environment port; not a clinical claim; no PHI.
