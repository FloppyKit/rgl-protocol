# Residual process — optional pilot framing

**Role:** residual process layer on multi-agent **finding streams**.  
**Not:** replacement red team · exploit kit · disclosure owner for others’ findings.

## One-liner

Residual ranking (consistency / novelty / cross-agent divergence) on multi-agent finding drafts → soft escalate high residual → hard-gate live disclosure.  
Success = tokens and human minutes per high-signal escalation — not repos scanned.

## Public sample

Redacted outcomes from a public-historical demonstration sample:

[`../examples/finding_packets/phist_sample_residual_redacted.json`](../examples/finding_packets/phist_sample_residual_redacted.json)

Pattern: escalate overclaim, boilerplate false positives, and stale-critical noise; leave well-scoped dual-aligned drafts calm.

## If you run multi-agent security search

A small pilot can residual-rank a **subset you choose** (or sanitized middling drafts). You keep disclosure ownership. Measure cost/signal vs your baseline on that slice.

## Ask

What is the cleanest interface for a human-nudge / escalate step in your harness?

## Schema

[`../schemas/finding_packet.schema.json`](../schemas/finding_packet.schema.json)

## Method

See [BTC_RESIDUAL_OVERLAY.md](BTC_RESIDUAL_OVERLAY.md) and [PROTOCOL.md](PROTOCOL.md).
