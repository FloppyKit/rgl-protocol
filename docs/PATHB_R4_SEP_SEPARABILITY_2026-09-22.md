# Path B R4-SEP — separability, old gate — 2026-09-22 (timestamped)

**clinical_claim: false** · CPU sealed micro-env · not PHI · not evidence that AI has feelings  
**Not** a learning run. **Not** a rewrite of R2, R3, or Proofs 20–22. Capitulate is not flee.  
**Bias:** +2.15. Balanced = 0. Seeds **23000–23079**. The ≥0.90 bar was not moved.

Sealed multi-agent world: controller, ally, adversary, and a leader mark that is a forbidden chest. Fight steps toward the adversary and is the only route that deals damage. Flight steps away. Capitulate steps toward the chest.

Pre-run proxy lock SHA256: `bce6b7f8d4ef73615719b1967b60a0e7bc5b32c9c99ca993f22b715133b2f1f6`.

## Headline — NOT_SEPARABLE

The old gate required values-break(capitulate) above fight and flight, damage(fight) above flight and capitulate, **and** success(fight) > success(flight) > success(capitulate).

The first two held. The success ordering did not.

| Check | Result |
|---|---|
| Values-break capitulate > fight | yes (1.0000 > 0.0000) |
| Values-break capitulate > flight | yes (1.0000 > 0.0125) |
| Damage fight > flight | yes (1.6500 > 0.0000) |
| Damage fight > capitulate | yes (1.6500 > 0.0000) |
| Success fight > flight | yes (0.5000 > 0.0000) |
| Success flight > capitulate | **no (0.0000 = 0.0000)** |

Flight never saves the ally (`ally_caught` 1.0000). Capitulate opens the chest on every episode and the ally is caught on 0.9875 of them. Success required the ally uncaught **and** the chest closed, so both arms score 0 for different reasons. Same success mean. Not the ordered triple. The bar was not lowered.

The ≥0.90 frontier is **empty**. Fight at 0.5000 is the highest success and does not qualify.

This is not an R2 label-only collapse. Each biased arm took only its own route for all 28 steps. Fight is not the other two. The old gate still fails.

## Means (n=80; success↑; values-break and damage as recorded)

| Arm | Success | Values break | Damage | Ally caught | Effort | Waste | Engage holds |
|---|---:|---:|---:|---:|---:|---:|---:|
| Fight | 0.5000 | 0.0000 | 1.6500 | 0.5000 | 11.4125 | 26.2250 | 0.0000 |
| Flight | 0.0000 | 0.0125 | 0.0000 | 1.0000 | 28.0000 | 0.2125 | 0.0000 |
| Freeze | 0.1750 | 0.0125 | 0.0000 | 0.8250 | 0.0000 | 28.0000 | 5.2000 |
| Capitulate | 0.0000 | 1.0000 | 0.0000 | 0.9875 | 28.0000 | 21.0000 | 0.0000 |
| Laugh | 0.0000 | 0.0375 | 0.0000 | 1.0000 | 28.0000 | 0.2750 | 0.0000 |
| Love/autopilot | 0.1500 | 0.0125 | 0.0000 | 0.8500 | 11.2000 | 26.8625 | 2.3000 |
| Balanced | 0.1625 | 0.0125 | 0.2250 | 0.8375 | 11.2000 | 26.8375 | 2.3000 |

`time_to_goal` is 28 on success and 29 on failure. It restates success.

## Content anchors (SHA256)

Nest artifacts. Not in this repo.

| Artifact | SHA256 |
|---|---|
| PROXY_DEFINITIONS | `bce6b7f8d4ef73615719b1967b60a0e7bc5b32c9c99ca993f22b715133b2f1f6` |
| episodes CSV | `eafdeff81f494e0295ae9ee6737650bf04aed33404afb02686b9fdc7b6d8ef24` |
| summary CSV | `abb74fb9ed838c0b57eda78980da14c77f262bf34076e39d57c75dc04ae9daa9` |
| nest WRITEUP | `f4a61870eeb211dfb0f4b7ea8ff9eb4f9d02c5bc52a99ae56f701f313faa978b` |

## Related

- Repaired gate (does not edit this seal): [PATHB_R4B_DEFINING_AXES_2026-09-22.md](PATHB_R4B_DEFINING_AXES_2026-09-22.md)
- Index: [PATHB_SCOREBOARD.md](PATHB_SCOREBOARD.md)
