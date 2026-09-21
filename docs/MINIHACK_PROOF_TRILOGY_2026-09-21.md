# MiniHack proof trilogy — 2026-09-21 (timestamped)

**clinical_claim: false** · CPU only · sealed 2026-09-21 America/Chicago · all gates VERIFY PASS

This note timestamps a sealed micro-env series. Goal is not “make a demo look good.” Goal is **show and prove** residual-map behavior under named questions, including **inverse** outcomes (cool residual ≠ automatic win).

## Stack slot (one line)

RGL here = an **external residual-updated salience / routing map** that gates act/ignore — **not** PEFT/LoRA, **not** rewriting a frozen soul/identity freeze.

```text
sense → residual signal → RGL map (update + read) → gate/route → act
                              ↑________ sleep / collapse _________|
```

## Scoreboard

| GO | Question | Verdict | Headline (public) |
|----|----------|---------|-------------------|
| PROOF-1 | residual gate vs blind policy | **inverse** | success tied at 1.0; gated mean steps 7.0 vs blind 4.0; hold_rate≈0.43 — cool residual ≠ win |
| PROOF-2 | sleep collapse leftovers | **same** | thrash 25.4→3.5; map_end 5.0→2.5; goal residual survived; success 0.92→1.0 |
| PROOF-3 | interrupt hold vs STOP | **same** | gate: chatter held, STOP honored, false_merges=0; blind always-abort: false_merges high, success 0.0 |

Instrument (public): MiniHack `MiniHack-Room-5x5-v0` + NLE WAIT action.

## What this proves / does not prove

**Proves (narrow):** under this micro-env and harness, residual gating, sleep collapse, and interrupt policy behave as logged; inverse results are publishable, not buried.

**Does not prove:** clinical outcomes, production Orbitty/Practice Desk performance, or that residual maps dominate all baselines forever.

## Nest vs public

| Public (this repo) | Nest (private) |
|--------------------|----------------|
| Protocol shape, schemas, redacted scores, method notes | Controller parameters, full free-association logs, operational playbooks, unredacted corpora |

## Related

- Protocol core: [PROTOCOL.md](PROTOCOL.md)
- Name stack: [NAMES.md](NAMES.md)
- Repo root: [../README.md](../README.md)
