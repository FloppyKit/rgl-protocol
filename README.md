# Resonance Guided Learning (RGL)

**Open science protocol** for residual-guided multi-agent / multi-head process work.

This repository publishes **protocol shape, schemas, and redacted examples**.  
It is **not** clinical software and **not** a security exploit toolkit.

| | |
|--|--|
| **What it is** | Protocol shape, schemas, synthetic examples, redacted metrics |
| **What it is not** | Therapy product · DSM claims · red-team replacement · private research dumps |
| **Status** | Early open science · v0.1 |

## Core idea

RGL treats **residual process signal** as first-class — not only a final score.

- **Axes (ops names on reports):** consistency (**Con**), novelty (**Nov**), relational / cross-agent divergence (**Rel**)
- **Dual metrics:** residual trajectory ≠ “cool score wins.” High residual can mean *attention needed*, not victory.
- **Gates:** soft escalate when residual is high; **hard gate** when disclosure or safety requires stop.

**Use cases (examples):** multi-agent report triage, agent process science, open residual overlays.  
Security finding-streams are one **worked example**, not the whole protocol.

## Quick start

1. [`docs/PROTOCOL.md`](docs/PROTOCOL.md) — protocol shape  
2. [`schemas/finding_packet.schema.json`](schemas/finding_packet.schema.json) — residual-on-**reports** packet shape  
3. [`examples/finding_packets/`](examples/finding_packets/) — synthetic + redacted public sample  
4. [`docs/BTC_RESIDUAL_OVERLAY.md`](docs/BTC_RESIDUAL_OVERLAY.md) — residual on finding streams
5. [`examples/lean_sorry_triage/`](examples/lean_sorry_triage/) — residual attention on public Lean `sorry`s  

## Applied example: residual on multi-agent findings

A thin residual layer on multi-agent security *finding streams*:

- rank by Con / Nov / Rel  
- escalate high residual shortlist  
- hard-gate live disclosure  

Success metric: **tokens / human minutes per high-signal escalation**, not repos scanned.

Redacted public-historical sample outcomes:  
[`examples/finding_packets/phist_sample_residual_redacted.json`](examples/finding_packets/phist_sample_residual_redacted.json)

Pilot interest (optional): [`docs/RESIDUAL_OFFER.md`](docs/RESIDUAL_OFFER.md)

## What is not published here

Controller parameters, private corpora, unredacted logs, and operational playbooks stay out of this repository. See non-claims below.

## License

Apache-2.0 — see [`LICENSE`](LICENSE).

## Citation

See [`CITATION.cff`](CITATION.cff).

## Non-claims

- Not a medical device; not DSM / clinical diagnosis software.  
- Not a certified cryptocurrency auditor.  
- Not responsible disclosure of any third party’s private findings.  
- Residual escalation is **not** the same as a confirmed vulnerability.

## Worked example: Lean `sorry` triage

Rank public open Lean obligations by process **attention** (where to look next).  
Kernel still owns correctness. No auto-PRs.

**[`examples/lean_sorry_triage/`](examples/lean_sorry_triage/)** — README + Zulip blurb + data

