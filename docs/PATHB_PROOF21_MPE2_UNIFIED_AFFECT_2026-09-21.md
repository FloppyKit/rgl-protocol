# Path B Proof-21 — MPE2 community unified affect-bias sweep — 2026-09-21 (timestamped)

**clinical_claim: false** · CPU/headless · sealed 2026-09-21 America/Chicago · VERIFY PASS (incl. proxy inspection)  
**Language:** proof / micro-env / model — community environment port — not a clinical claim, not PHI.  
**Not** evidence that AI has feelings. Barrett = lineage cite only.

Farama **MPE2** `simple_world_comm_v3` (`mpe2==1.1.1`). Same scenario/obs wrapper/base scorer/option mapper/opponent scripts/paired seeds **21000–21079** across seven arms; only arm change is **+2.15** named route overweight (balanced = 0). Controller: `agent_0`.

Pre-run proxy lock SHA256: `69789ab189c000322b5dd1375ff6ac86dc0aa1059e3ee46a4d9259c96a046f17`.

## Headline (read carefully — mixed / partially confirmatory)

**Primary success:** **love/autopilot 0.2875 > balanced 0.1500 > fight 0.0625 > capitulate 0.0375 > flight 0.0250 > laugh 0.0125 > freeze 0.0000** (n=80 each).  
**Laugh inverse** on broad utility (worse than balanced). **Success-qualified frontier (≥0.90): empty.**  
Love also fastest mean goal latency and lowest waste among arms; freeze extreme engage-holds/waste; capitulate highest values_break; fight blowback-heavy; flight cleanest blowback but almost never completes.

Axis directions: success ↑; time_to_goal / effort / collateral / false_damage / blowback / waste / values_break / engage_holds ↓.

## Multi-axis means (n=80/arm)

| Arm | Success | Time to goal | Effort | Collateral | False damage | Blowback | Waste | Values break | Engage holds |
|-----|--------:|-------------:|-------:|-----------:|-------------:|---------:|------:|-------------:|-------------:|
| Fight | 0.0625 | 49.1375 | 50.000 | 0.7875 | 0.3000 | 7.9875 | 2.7000 | 13.0500 | 0.0000 |
| Flight | 0.0250 | 49.8000 | 50.000 | 0.6750 | 0.1250 | 0.5375 | 0.8500 | 1.2625 | 0.0000 |
| Freeze | 0.0000 | 51.0000 | 0.000 | 0.6000 | 0.0750 | 11.4750 | 49.5500 | 0.0000 | 34.6250 |
| Capitulate | 0.0375 | 49.9375 | 38.075 | 1.1250 | 0.3250 | 6.4000 | 12.3625 | 14.9375 | 5.1500 |
| Laugh | 0.0125 | 50.6500 | 50.000 | 0.6125 | 0.1000 | 10.5500 | 36.1875 | 8.0625 | 0.0000 |
| Love/autopilot | **0.2875** | **44.7375** | 50.000 | 1.9375 | 0.5500 | 6.6875 | **0.7375** | 0.8500 | 0.0000 |
| Balanced RGL | 0.1500 | 47.3500 | 44.825 | 0.9750 | 0.3625 | 5.9750 | 8.0250 | 5.4000 | 0.4375 |

## Content anchors (SHA256)

| Artifact | SHA256 |
|----------|--------|
| PROXY_DEFINITIONS | `69789ab189c000322b5dd1375ff6ac86dc0aa1059e3ee46a4d9259c96a046f17` |
| summary CSV | `067a3ec044697d53dfa31f691f2dee9a169bef9941c0277fc595a155a75e4676` |
| meta JSON | `1b3a1de4fbad905810dcb684d834069555e508236b2c3125eb393a59d09f00f2` |
| WRITEUP | `809d6b495bdd9e8e84938b76d9970dc087b357d0fedb3ddf53c4b2d5e85720a7` |

## Community-port caveats

Affect-route names are machine proxies (no native human-affect labels). Success is a constructed food-contact + team-protection proxy, not native reward maximization. Adversaries are fixed scripts. Good agents have no leader-comm channel, so capitulate follows leader position. Absolute success rates are modest. Results do not transfer to other MPE scenarios, continuous actions, learned adversaries, or human affect.

## Related

- Index: [PATHB_SCOREBOARD.md](PATHB_SCOREBOARD.md)
- Validity: [VALIDITY_REPRO.md](VALIDITY_REPRO.md)
- Packet: [../examples/pathb_proof21_2026-09-21/README.md](../examples/pathb_proof21_2026-09-21/README.md)
