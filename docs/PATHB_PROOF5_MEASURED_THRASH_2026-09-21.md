# Path B Proof-5 — measured thrash (engage) — 2026-09-21 (timestamped)

**clinical_claim: false** · CPU only · sealed 2026-09-21 America/Chicago · VERIFY PASS  
**Language:** proof / micro-env / model — not a clinical claim, not PHI.

Alpha from Proof-4 **inverse** (cool→HOLD in engage = death). Battle law: cool residual ≠ win; residual may steer *which* commits (cut waste), but must **not** idle-latch after a hit while the enemy is alive. Path A cool-after-match (stop nagging the operator) is **not** Path B engage policy.

## Stack slot (one line)

RGL here = residual-updated salience that **ranks / steers commits under fog** — never cool→HOLD while enemy alive.

```text
sense (local fog) → residual → rank commits (measured thrash) → always commit in engage → act
```

## Scoreboard

| GO | Question | Verdict | Headline (public) |
|----|----------|---------|-------------------|
| PATHB-PROOF-5 | measured thrash (no cool→HOLD in engage) vs always-commit blind | **same** | both success **1.0** (ally alive, enemy cleared); engage_holds **0**; recovers Proof-4 residual_gate collapse (0.0→1.0); waste identical to blind on this layout |

Instrument (public): sealed **SMAC-lite** micro-env reused from Proof-4 (2 allies + 1 scripted foe, fog-of-war, no SC2).

## Content anchors (SHA256)

| Artifact | SHA256 |
|----------|--------|
| episodes CSV | `d707b6e7145af6ad7a95e220dde9df5fda65f5be19d78af1c37bc2d43b8babd7` |
| summary CSV | `9417c1b30d2e561588b1dc45ef011a359fe56c38a0114ead8b1d67dd8580a2dc` |
| WRITEUP | `7a61a28321326b9b32aad5f5e40460d5c4eb6c849806d89dbd92315eab7ccba5` |

## What this proves / does not prove

**Proves (narrow):** forbidding cool→HOLD in engage recovers from the Proof-4 inverse failure mode; measured thrash matches blind success on this harness.

**Does not prove:** that residual ranking beats blind on waste in every layout, or that results generalize outside this sealed micro-env.

## Nest vs public

| Public (this repo) | Nest (private) |
|--------------------|----------------|
| Protocol shape, redacted scores, method note, content SHA anchors | Full experiment logs, harness trees, VERIFY evidence bundles |

## Related

- Proof-4 (inverse cool→HOLD): [PATHB_PROOF4_SMAC_LITE_2026-09-21.md](PATHB_PROOF4_SMAC_LITE_2026-09-21.md)
- MiniHack shared-mechanism trilogy: [MINIHACK_PROOF_TRILOGY_2026-09-21.md](MINIHACK_PROOF_TRILOGY_2026-09-21.md)
- Example packet: [../examples/pathb_proof5_2026-09-21/README.md](../examples/pathb_proof5_2026-09-21/README.md)
