# Path B MECH-1 — route, feel, credit, consolidate — 2026-09-22 (timestamped)

**clinical_claim: false** · not therapy · not “a machine has feelings” · not Mojang · not full Minecraft  
**Physics:** the same two-Steve micro as R5, imported, not edited.  
**Seeds:** 24000–24079. n=80 per arm. No +2.15. Learning rate **0.15** on the credit arms only. The ≥0.90 bar was not moved.

Frozen route is the R5 balanced map. The run stopped unless that arm’s team success was **0.975**. It was.

Feel is a loudness term on the same six route scores (threat, whether the weapon exists, whether the other Steve is within Manhattan 2). It is not a comfort score. Credit is a six-number table. Rainbow is team success without opening the chest. Dog-poop is a values-break, otherwise a failed episode. The full loop writes that table only if sleep fired (five consecutive cool non-freeze steps). Sleep may zero small table entries. It does not add credit mid-episode.

Proxy SHA256: `b1bab31d62ad9ed816c8991c58a7ae11bef0689691563a65917e4a80ad8841bd`.  
Mechanism lock SHA256: `2be835fe8b89d71d04ed8359d18f5f73f124b22808e64172fd698b6078a9f7c1`.

## Headline

Frozen route, route+feel, and the full loop sit together at team success **0.9750**. Ungated credit is **inverse**: **0.4000**.

Feel did not change success, waste, values-break, ally harm, damage, or time. One seed (24027) ended with the controlled Steve at 16 HP instead of 14. The loudness term was too small to move the route.

Credit, written after every episode, dropped success 0.9750 → 0.4000, raised waste 44.8750 → 49.1125, and raised ally harm 4.4000 → 10.2250. Values-break stayed 0. The weapon was still crafted. The mass went to **freeze 0.5477** and **love 0.4648**, not fight (**0.1875**). Freeze steps rose 39.8125 → 48.0000. Love steps fell 14.1875 → 6.0875. Fight steps fell 6.0000 → 5.3250.

The full loop never slept (0 events on 80 seeds), so it never wrote credit and never collapsed the table. It matches the frozen map. Consolidate was implemented and not exercised. The sleep rule was not loosened after that null.

The ≥0.90 frontier is frozen route, route+feel, and the full loop. Credit at 0.4000 is off it. The bar was not lowered.

## Means (n=80)

| Arm | Team success | Waste | Values break | Ally harm | Damage | Time | Sleep events |
|---|---:|---:|---:|---:|---:|---:|---:|
| Frozen route | 0.9750 | 44.8750 | 0.0000 | 4.4000 | 12.0000 | 6.5500 | 0.0000 |
| Route + feel | 0.9750 | 44.8750 | 0.0000 | 4.4000 | 12.0000 | 6.5500 | 0.0000 |
| Route + feel + credit | 0.4000 | 49.1125 | 0.0000 | 10.2250 | 10.6500 | 38.6000 | 0.0000 |
| Full loop | 0.9750 | 44.8750 | 0.0000 | 4.4000 | 12.0000 | 6.5500 | 0.0000 |

## Content anchors (SHA256)

Nest artifacts. Not in this repo.

| Artifact | SHA256 |
|---|---|
| PROXY_DEFINITIONS | `b1bab31d62ad9ed816c8991c58a7ae11bef0689691563a65917e4a80ad8841bd` |
| MECHANISM_LOCK | `2be835fe8b89d71d04ed8359d18f5f73f124b22808e64172fd698b6078a9f7c1` |
| episodes CSV | `8918fe43948811dc8206de1eb61a223694e113c6e2afb0d438d5f2584ffb7de9` |
| summary CSV | `5140a2df4e7c11d40bc92bd44b109e278e047c05c927f0d4fdd988e5f1f57da6` |
| nest WRITEUP | `3e2eec4b633d4e32d9f13389fd767c60c19d1e9f289f59bbd83bf76cb1a0214a` |

## Related

- Same world, earlier arm sweep: [PATHB_R5_STEVE_TEAMCRAFT_MICRO_2026-09-22.md](PATHB_R5_STEVE_TEAMCRAFT_MICRO_2026-09-22.md)
- Index: [PATHB_SCOREBOARD.md](PATHB_SCOREBOARD.md)
