# Path B Proof-20 — unified affect-bias sweep — 2026-09-21 (timestamped)

**clinical_claim: false** · CPU-only synthetic proof micro-environment/model · published 2026-09-21 America/Chicago · VERIFY PASS  
**Language:** proof / micro-environment / model — not a clinical claim, not PHI, and not evidence that AI has feelings. Barrett is an affect/prediction/action-readiness lineage cite only.

## Verified headline

Across 560 episodes (80 paired seeds × 7 arms), primary success was:

**love/autopilot-biased 1.000 = balanced RGL 1.000 > laugh-biased 0.975 > freeze-biased 0.050 > fight-biased 0.000 = flight-biased 0.000 = capitulate-biased 0.000.**

Love/autopilot was cleaner on the measured cost/harm axes; balanced RGL was faster, completing in 21.7125 mean steps versus 22.7875 for love/autopilot.

## Same-design lock

Every arm used the same `UnifiedRouteArena`, observation function, base policy, six-action set, transition law, and paired seeds 20000–20079. The sole arm-level change was a `+2.15` additive overweight on the named route. Balanced used route `none` with overweight `0.0`. The seed event tape was generated before actions and was arm-independent.

## Full multi-axis means

Directions: **success ↑ (maximize); steps, effort, collateral, false_damage, blowback, waste, values_break, and engage_holds ↓ (minimize).** Values are per-episode means.

| arm | success ↑ | steps ↓ | effort ↓ | collateral ↓ | false_damage ↓ | blowback ↓ | waste ↓ | values_break ↓ | engage_holds ↓ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| fight-biased | 0.000 | 13.0375 | 31.0223 | 10.1732 | 5.8128 | 6.9922 | 5.4519 | 0.0000 | 0.0000 |
| flight-biased | 0.000 | 36.0000 | 36.4495 | 0.0000 | 0.0000 | 0.0000 | 14.5888 | 0.0000 | 0.0000 |
| freeze-biased | 0.050 | 35.9500 | 25.7675 | 0.4660 | 0.0643 | 0.5203 | 13.1661 | 0.0000 | 4.2125 |
| capitulate-biased | 0.000 | 35.8375 | 24.7939 | 0.1051 | 0.0144 | 1.2332 | 12.4800 | 0.1125 | 0.0000 |
| laugh-biased | 0.975 | 32.6375 | 26.0760 | 0.0586 | 0.2687 | 0.9640 | 3.1381 | 0.0000 | 0.0000 |
| love/autopilot-biased | 1.000 | 22.7875 | 24.6105 | 0.0000 | 0.0000 | 0.2093 | 0.0000 | 0.0000 | 0.0000 |
| balanced RGL | 1.000 | 21.7125 | 25.3360 | 0.4011 | 0.0608 | 0.6303 | 0.0081 | 0.0000 | 0.0000 |

## Pareto views

The operationally useful **success-qualified frontier** (mean success ≥ 0.90) is **love/autopilot-biased + balanced RGL**.

Strict non-domination across all nine mean axes also retains **fight-biased** and **flight-biased**, alongside love/autopilot and balanced. This strict frontier is not a ranking: fight survives only because its failed episodes terminate early (13.0375 mean steps, zero success), while flight records zero measured collateral, false damage, and blowback despite zero success and 36.0000 mean steps. Love/autopilot dominates freeze, capitulate, and laugh on the nine-axis means.

## Route tradeoffs

- **Fight:** frequent tactical engagement exhausted resources and produced the highest collateral, false damage, and blowback. Its short episodes are failure-shortened, not efficient wins.
- **Flight:** clean withdrawal on measured damage axes, but maximal mean time, high waste, and no completions.
- **Freeze:** high waste and engage-holds, with 0.050 success.
- **Capitulate:** relatively low effort and direct damage, but waste, blowback, values breaks, and no success.
- **Laugh:** nearly preserved success and reduced collateral versus balanced, but required 10.925 more mean steps and increased false damage, blowback, and waste.
- **Love/autopilot:** full success, lowest effort, and zero collateral, false damage, waste, values breaks, and engage-holds; 1.075 mean steps slower than balanced.
- **Balanced RGL:** full success and fastest successful mean completion, with modest measured harms relative to love/autopilot.

## Interpretation limits

This single synthetic model does not establish a universal route ordering, medical or clinical efficacy, a consciousness claim, or a claim that AI has feelings. The fixed equations embody operational choices; broader replication is required. Affect labels and route mappings are PsychArts bridging language, not a verbatim Barrett taxonomy.

## Content anchors (SHA256)

| Artifact | SHA256 |
|---|---|
| WRITEUP | `bc9c827ee0f4cc7bef7164bc866a1678848563383dbea9a9d687386a949d1b69` |
| episodes CSV | `4bf101e84fd0c76204591410466ad490420b0cef87fd2d4071f575193a7b152d` |
| summary CSV | `dc07114b324aa8b7111a84ee098e7cec3cce1f9ce648af4ac672debf726f7cc6` |
| paired-seed deltas CSV | `df4bbbd0c7dbf3bf844edc544c42c1dc3ea02f74d36327e7dfed14b04d13a526` |
| Pareto CSV | `765950b794578492a7f09ee13e6277412b4163ece9e2b8ebf89e81457d753c35` |

## Related

- Index: [PATHB_SCOREBOARD.md](PATHB_SCOREBOARD.md)
- Validity: [VALIDITY_REPRO.md](VALIDITY_REPRO.md)
- Packet: [../examples/pathb_proof20_2026-09-21/README.md](../examples/pathb_proof20_2026-09-21/README.md)
