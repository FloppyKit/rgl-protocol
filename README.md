# Resonance Guided Learning (RGL)

RGL is a router: a cost-benefit planner that, at each step, scores a set of options by what each one is expected to cost and gain in survival and picks among them. The main arena is ViZDoom team deathmatch. The first proofs meant to stand at NSF level will come from there. Everything before ViZDoom is preliminary.

This repository publishes the protocol shape, schemas, and redacted examples. It is open science.

| | |
|--|--|
| **What it is** | A router (cost-benefit planner) over six option families, plus an optional residual "rudder" that biases routes |
| **What it is not** | A model with feelings · clinical or diagnostic software · an exploit kit |
| **Main arena** | ViZDoom team deathmatch (stock environment) |
| **Status** | Pre-pilot. See [Current status](#current-status) |

---

## The idea

### A router over six families

An emotions map routes among six families: **fight, flight, freeze, capitulate, laugh, love**. These are family names only. Each one names a set of options that are scored by the same survival calculation. Nothing here claims that an agent has feelings or inner experience.

Two of the names have specific meanings:

- **Love** means serving the team plan. It does not mean staying close to a teammate.
- **Capitulate** means backing off to heal or reload.

The other four keep their plain sense (engage, retreat, hold still, explore).

### The residual triangle: a soft rudder

A separate residual triangle combines three readings: **Affective/relational** (affinity), **Consistency**, and **Novelty**. It acts as a soft rudder that biases which route wins. It is not a hard picker. In ViZDoom it is an add-on arm, tested against the router without it.

### "Sleep": memory compaction

"Sleep" means memory compaction. It is a backlog need, like hunger, and sits outside the six routes. It fires at save-spot moments: points where the state has just changed a lot.

### What counts as success

- **Core metric:** how long the agent survives.
- **Secondary:** team survival, or how far the agent got.

See [docs/NAMES.md](docs/NAMES.md) for the acronym (Resonance Guided Learning; other public readings of "RGL" are listed there).

---

## Environments

Stock environments are preferred.

- **ViZDoom, team mode: the main arena.** Doom-level intensity matches real life. The first NSF-level proofs come from it.
- **Earlier work is preliminary or smoke-level only:** the P-series and Path B micro-environments, Craftax, MiniHack, SMAC-lite, MPE. The documents below are kept as a timestamped record, not as the main evidence. The Craftax v2 prereg is public ([docs/RGL_V2_PROOF1B_CRAFTAX_PREREG_2026-10-10.md](docs/RGL_V2_PROOF1B_CRAFTAX_PREREG_2026-10-10.md), frozen 2026-10-10, before any confirmatory seed); its results are not published and are kept as lab notes.
- **Next after Doom:** Neural MMO (MIT).

### Preliminary record (timestamped, smoke-level)

- [docs/MINIHACK_PROOF_TRILOGY_2026-09-21.md](docs/MINIHACK_PROOF_TRILOGY_2026-09-21.md): MiniHack (residual gate, sleep collapse, interrupt hold). It includes an inverse result: a cool residual is not the same as a win.
- [docs/PATHB_SCOREBOARD.md](docs/PATHB_SCOREBOARD.md): index for the Path B micro-environment runs (RGL as the deciding agent).
- [docs/AFFECT_ROUTE_MAP.md](docs/AFFECT_ROUTE_MAP.md): an earlier write-up of the six-family route map. The family names are labels only.
- [docs/VALIDITY_REPRO.md](docs/VALIDITY_REPRO.md): validity, reproduction, and non-claims.
- [docs/PATHB_METHODS_2026-09.md](docs/PATHB_METHODS_2026-09.md): methods used for those runs.

---

## Method

Care over speed:

- **Preregistration first:** every preregistration revision is written down before the data it affects.
- **Dry runs** use throwaway seeds that are never used for results.
- **Every arm** has a behavioural-difference test plus mutants: deliberate code breaks that the tests must catch.
- **Per-step traces** are kept for every run.
- **An independent Verify pass** is required before anything is frozen.

[docs/PROTOCOL.md](docs/PROTOCOL.md) describes the protocol shape.

---

## Current status

GO-RGL-V3-BUILD-1 is the ViZDoom build of the v3 spec.

- **Next step:** a map_only smoke run, pre-pilot, with λ = 0. Every smoke result will be labelled "pre-pilot, λ=0".
- **Revision r4g** has passed Verify and is waiting for Matt to apply it and launch.
- **No ViZDoom results are published yet.**

---

## Other uses of the residual idea

The residual ranking (Consistency / Novelty / Relational) has also been written up for two streams outside the agent work:

- **Triage of multi-agent finding streams.** The aim is to cut human minutes per high-signal escalation, not to scan more. Hard gate: no automatic public disclosure. See:
  - [docs/RESIDUAL_OFFER.md](docs/RESIDUAL_OFFER.md)
  - [docs/BTC_RESIDUAL_OVERLAY.md](docs/BTC_RESIDUAL_OVERLAY.md)
  - [examples/finding_packets/](examples/finding_packets/)
  - [schemas/finding_packet.schema.json](schemas/finding_packet.schema.json)

  A high residual means attention is needed. It is not a confirmed vulnerability.
- **Ranking open Lean `sorry`s by process attention.** The kernel still owns correctness. See [examples/lean_sorry_triage/](examples/lean_sorry_triage/).

---

## Tools

All apps used are free and open-source, local-first, with no lock-in.

## What is not published here

- full experiment logs;
- controller parameters;
- private corpora;
- operational playbooks.

These stay in the lab's private archive.

## License

Apache-2.0. See [LICENSE](LICENSE).

## Citation

See [CITATION.cff](CITATION.cff).

## Non-claims

- The six family names are labels only. No claim that any model has feelings or inner experience.
- Not a medical device; not clinical or diagnostic software.
- Not a certified cryptocurrency auditor, and not a replacement for any red team.
- Not responsible disclosure of anyone's private findings.

## Footer

clinical_claim: false · proof/micro-env/model
