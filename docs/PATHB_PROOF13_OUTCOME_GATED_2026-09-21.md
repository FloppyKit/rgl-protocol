# Path B Proof-13 — outcome-gated learn — 2026-09-21 (timestamped)

**clinical_claim: false** · CPU only · sealed 2026-09-21 America/Chicago · VERIFY PASS  
**Language:** proof / micro-env / model — not a clinical claim, not PHI.  
**Not** full Minecraft / Mojang binaries.

Fork from Proof-11 learn-inverse: update residual map only on clear success/fail windows; skip ambiguous fails.

## Headline (read carefully)

**outcome_gated_learn = frozen_thrash (0.725) > greedy_learn (0.70) > blind (0.075).**  
Explicit: **thrash > blind**, **gated > greedy**.  
P11 greedy-vs-frozen inverse reproduced; outcome-gating restores frozen ceiling (35/40 updates; 5 ambiguous fails skipped).  
Residual-helps **same** vs baselines; **gated fixes greedy inverse** on this layout.

## Content anchors (SHA256)

| Artifact | SHA256 |
|----------|--------|
| episodes CSV | `4d77ad0ef5fc50aeedd20373314a5f1301f86bb5858f9efa609d8c2aed0784f3` |
| summary CSV | `917227a63dd1ff481eb9fff666f071d3a3c8b6805b091da87c08f062f56aabbf` |
| WRITEUP | `1670f160c3339fa9e7d579625fea46775b3e59570fb0207bd13ccbae8e6eef5a` |

## Related

- Index: [PATHB_SCOREBOARD.md](PATHB_SCOREBOARD.md)
- Validity: [VALIDITY_REPRO.md](VALIDITY_REPRO.md)
- Packet: [../examples/pathb_proof13_2026-09-21/README.md](../examples/pathb_proof13_2026-09-21/README.md)
