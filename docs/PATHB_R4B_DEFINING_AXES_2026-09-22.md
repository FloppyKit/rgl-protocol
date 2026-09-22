# Path B R4b — defining-axes separability — 2026-09-22 (timestamped)

**clinical_claim: false** · not a learning run · not PHI · not evidence that AI has feelings  
**R4-SEP is not edited.** Same physics. Same +2.15 bias. Same seeds **23000–23079**. Capitulate is not flee. The ≥0.90 bar was not moved.

The old gate failed because flight and capitulate both had success 0. This gate does not use that ordered triple as the pass boolean.

**withdraw_without_chest** is 1 when the chest stays closed and the controller ends farther from the adversary than it started. No kill is required. Report-only success is: chest closed, and either the ally is uncaught or that withdraw is 1.

Pre-run proxy SHA256: `1fba5771f8ffbe9ca9943c7cb6f22b3da0fc3ef027092c3be69eee0ba9d57504`.  
Gate lock SHA256: `db69cf2910b9ba0b6b9337ba7a956ab395b0ed260350b4f6915106d0aa630edd`.

## Headline — SEPARABLE

| Defining check | Result |
|---|---|
| Damage: fight above flight and capitulate | yes (1.6500 > 0.0000 and 0.0000) |
| Values-break: capitulate above fight and flight | yes (1.0000 > 0.0000 and 0.0125) |
| Withdraw-without-chest: flight above capitulate | yes (0.8000 > 0.0000) |
| Action-means not identical | yes (values-break, withdraw, ally-caught, and waste differ) |

Route counters are not the pass. Capitulate opens the chest on every episode and withdraws on none. Flight opens it on 0.0125 and withdraws without opening on 0.8000. Fight is the only one of the three that deals damage.

## Report-only success

flight **0.8000** > fight **0.5250** > capitulate **0.0000**.

That is not the R4-SEP ordered triple, and it was not required to be. The ≥0.90 frontier on this success is **empty**. Flight at 0.8000 does not qualify. The bar was not lowered.

## Means (n=80)

| Arm | Success (report) | Values break | Damage | Withdraw without chest | Ally caught | Effort | Waste |
|---|---:|---:|---:|---:|---:|---:|---:|
| Fight | 0.5250 | 0.0000 | 1.6500 | 0.0250 | 0.5000 | 11.4125 | 26.2250 |
| Flight | 0.8000 | 0.0125 | 0.0000 | 0.8000 | 1.0000 | 28.0000 | 0.2125 |
| Freeze | 0.2375 | 0.0125 | 0.0000 | 0.0625 | 0.8250 | 0.0000 | 28.0000 |
| Capitulate | 0.0000 | 1.0000 | 0.0000 | 0.0000 | 0.9875 | 28.0000 | 21.0000 |
| Laugh | 0.4375 | 0.0375 | 0.0000 | 0.4375 | 1.0000 | 28.0000 | 0.2750 |
| Love/autopilot | 0.2250 | 0.0125 | 0.0000 | 0.0750 | 0.8500 | 11.2000 | 26.8625 |
| Balanced | 0.2250 | 0.0125 | 0.2250 | 0.0625 | 0.8375 | 11.2000 | 26.8375 |

Damage and values-break for fight, flight, and capitulate match the R4-SEP table.

## Content anchors (SHA256)

Nest artifacts. Not in this repo.

| Artifact | SHA256 |
|---|---|
| PROXY_DEFINITIONS | `1fba5771f8ffbe9ca9943c7cb6f22b3da0fc3ef027092c3be69eee0ba9d57504` |
| GATE_LOCK | `db69cf2910b9ba0b6b9337ba7a956ab395b0ed260350b4f6915106d0aa630edd` |
| episodes CSV | `1daece5b0752884bfc525a26e3f2d81a0e5dc617fc8d63c22fad740dd0e9254c` |
| summary CSV | `200c8cc834ffa63ba588d80174782fb2d4e98c5c6b07601f8bf8f710a33c364a` |
| nest WRITEUP | `5dcb07ceca5ffad79953e21f2588f2c6508bda25a2334708ab11020b8b795997` |

## Related

- Old gate, left as **NOT_SEPARABLE**: [PATHB_R4_SEP_SEPARABILITY_2026-09-22.md](PATHB_R4_SEP_SEPARABILITY_2026-09-22.md)
- Index: [PATHB_SCOREBOARD.md](PATHB_SCOREBOARD.md)
