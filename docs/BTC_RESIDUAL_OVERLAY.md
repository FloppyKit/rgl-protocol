# Residual overlay on multi-agent findings (public method note)

**Role:** residual **process** layer on multi-agent finding *report streams*.  
**Not:** red-team replacement · exploit author · disclosure owner for others’ findings.

## Success

Fewer tokens and human-minutes per **high-signal escalation**.  
Not: raw repo count scanned.

## Pipeline (shape)

```text
finding packets (multi-agent drafts)
  → residual Con / Nov / Rel
  → escalate high residual shortlist
  → hard gate: no auto-public disclosure of live vulns
  → hand back ranked process package
```

## Public sample

A **targeted** public-historical sample (not a full corpus scrape) was residual-processed offline for demonstration.

Redacted outcomes (ids + axes only; no full evidence dump):

[`../examples/finding_packets/phist_sample_residual_redacted.json`](../examples/finding_packets/phist_sample_residual_redacted.json)

Typical escalate patterns in that sample:

- severity **overclaim** vs thin evidence  
- **audit finding-count hype** vs informational classes  
- **boilerplate** false positives  
- **stale** critical re-reports of fixed classes  

Well-scoped dual-aligned advisories stay **null_calm** (low residual) — human attention saved.

## Related

- Protocol: [PROTOCOL.md](PROTOCOL.md)  
- Schema: [`../schemas/finding_packet.schema.json`](../schemas/finding_packet.schema.json)  
- Optional pilot framing: [RESIDUAL_OFFER.md](RESIDUAL_OFFER.md)  
