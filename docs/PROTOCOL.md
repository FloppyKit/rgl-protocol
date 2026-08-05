# RGL protocol shape (public)

**Version:** 0.1  
**Scope:** conceptual + schema-level. Not a full implementation runbook.

## 1. Residual first

RGL optimizes for **process residual** — signal that something is unresolved, inconsistent, novel, or diverging across observers — rather than maximizing a single comfort score.

| Term | Meaning |
|------|---------|
| **Residual** | Unresolved process energy / divergence worth attention |
| **Cool ≠ win** | Low residual can mean calm *or* stuck false peace; context matters |
| **ΔR** | Change in residual over cycles (one metric family among others) |

```text
report / draft stream
  → residual axes
  → soft escalate when high
  → hard gate when disclosure / safety requires stop
```

## 2. Axes (on multi-agent report streams)

| Axis | High residual suggests |
|------|-------------------------|
| **Con** | Claim↔evidence drift; severity / confidence inconsistency |
| **Nov** | New class vs boilerplate template noise |
| **Rel** | Cross-agent or cross-model draft divergence |

Other head geometries may exist in private research; exact stacks and weights are not published here.

## 3. Gates

| Gate | Behavior |
|------|----------|
| **Soft** | Soft escalate or short domain-style inject; continue |
| **Hard** | Stop auto-public path; no auto-disclose live vulns; safety stop |

Hard gate always wins over residual curiosity when disclosure or harm risk is present.

## 4. Finding packet (report stream unit)

```text
finding_id, source_repo_or_doc, agent_or_model, severity_claim,
evidence_excerpt, confidence, timestamp, parent_scan_id
+ optional drafts[]  → Rel residual
```

Machine schema: [`../schemas/finding_packet.schema.json`](../schemas/finding_packet.schema.json).

## 5. Dual metrics discipline

- Report residual trajectories + thrash labels + cost alongside any preference score.  
- Do not claim clinical outcomes from residual labels.  
- Do not treat escalated residual as “confirmed vulnerability.”

## 6. Thrash labels (process labels, not clinical)

| Label | Rough meaning |
|-------|----------------|
| `null_calm` | Aligned, well-scoped, low residual |
| `growth_thrash` | Productive disagreement / motion |
| `growth_novel` | Novel class with aligned drafts |
| `stuck_thrash` | Severity war + thin evidence — human attention |
| `claim_drift` | Severity / evidence mismatch dominant |

## 7. Proof without dump

Public materials may include schemas, method shape, redacted aggregates, and content hashes — without private free-association text or private disclosure streams.
