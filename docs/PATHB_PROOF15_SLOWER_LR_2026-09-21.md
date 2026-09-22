# Path B Proof-15 — slower LR learn — 2026-09-21 (timestamped)

**clinical_claim: false** · CPU only · sealed 2026-09-21 America/Chicago · VERIFY PASS  
**Language:** proof / micro-env / model — not a clinical claim, not PHI.  
**Not** full Minecraft / Mojang binaries.

Same P11 greedy update rule with smaller step size (SLOW_LR_SCALE=0.25).

## Headline (read carefully)

**slow_learn = frozen_thrash (0.725) > greedy_learn (0.70) > blind (0.075).**  
Explicit: **thrash > blind**, **slow_learn > greedy**.  
Both learn arms applied 40/40 updates; slow vs frozen differ **0/40**.  
Residual-helps **same** vs baselines; slow LR restores frozen ceiling vs greedy inverse.

## Content anchors (SHA256)

| Artifact | SHA256 |
|----------|--------|
| episodes CSV | `d4e99219a6ac6440fdb18845dabfd652abc436c802e57fe7cc61ed570a01fdd7` |
| summary CSV | `d2bdbb1ab1b24dd52e89c8cef5a5405011f4513bcb52b5670539a3e71214f2f0` |
| WRITEUP | `298a46c0ee4f84d3b5d721c75f0db961333df48fc134740fc83ffb3b40267cd9` |

## Related

- Index: [PATHB_SCOREBOARD.md](PATHB_SCOREBOARD.md)
- Validity: [VALIDITY_REPRO.md](VALIDITY_REPRO.md)
- Packet: [../examples/pathb_proof15_2026-09-21/README.md](../examples/pathb_proof15_2026-09-21/README.md)
