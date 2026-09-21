# Path B Proof-4 — SMAC-lite opaque next-state — 2026-09-21 (timestamped)

**clinical_claim: false** · CPU only · sealed 2026-09-21 America/Chicago · VERIFY PASS  
**Language:** proof / micro-env / model — not a clinical claim, not PHI.

This note timestamps a sealed Path B micro-env: **RGL as the deciding agent** under opaque next-state (partial obs + teammate actions change unseen outcomes). Inverse outcomes are publishable.

## Stack slot (one line)

RGL here = an **external residual-updated salience / routing map** that gates commit/HOLD under fog — **not** PEFT/LoRA, **not** rewriting a frozen soul/identity freeze.

```text
sense (local fog) → residual signal → RGL map (update + read) → gate commit/HOLD → act
```

## Scoreboard

| GO | Question | Verdict | Headline (public) |
|----|----------|---------|-------------------|
| PATHB-PROOF-4 | residual-gated commit vs always-commit under opaque next-state | **inverse** | blind success **1.0** (ally alive, enemy cleared) vs residual_gate success **0.0** (hold_rate≈0.21; cool HOLDs interrupt finishing commits; ally dies, enemy survives) — cool residual ≠ win under opacity |

Instrument (public): sealed **SMAC-lite** micro-env (2 controllable allies + 1 scripted foe, fog-of-war local obs, discrete move/attack/hold). **Not** full SMAC / StarCraft II.

## Content anchors (SHA256)

| Artifact | SHA256 |
|----------|--------|
| episodes CSV | `b567290120a4cd0aadc218d8c243a159e0761655c3f728214b378fc723669476` |
| summary CSV | `44daab55a8cf7106bf8c45827b7201301827c809115797a25754a8290db876ba` |
| WRITEUP | `45bc74af359fb097b59b69a0ac9ac267749e6ce93996a5b7b37f830e7ee7c7ff` |

## What this proves / does not prove

**Proves (narrow):** under this SMAC-lite harness, residual-gated commit did not beat always-commit; inverse result is logged and timestamped.

**Does not prove:** that residual maps never help under opacity, or that these micro-env results generalize outside the sealed harness.

## Nest vs public

| Public (this repo) | Nest (private) |
|--------------------|----------------|
| Protocol shape, redacted scores, method note, content SHA anchors | Full experiment logs, harness trees, VERIFY evidence bundles |

## Related

- MiniHack shared-mechanism trilogy: [MINIHACK_PROOF_TRILOGY_2026-09-21.md](MINIHACK_PROOF_TRILOGY_2026-09-21.md)
- Protocol core: [PROTOCOL.md](PROTOCOL.md)
- Example packet: [../examples/pathb_proof4_2026-09-21/README.md](../examples/pathb_proof4_2026-09-21/README.md)
