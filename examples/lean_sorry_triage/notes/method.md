# Method

## Scoring

| Item | Value |
|------|--------|
| Type | Offline deterministic heuristic |
| Axes (internal) | Con / Nov / Rel → `attention` ∈ [0,1] |
| Multi-head LLM residual | **Not used** in this pack |
| Cost | $0 |

High `attention` means the **process features** of the unit (status, goal text richness/thinness, light metadata) look triage-worthy under the heuristic.  
It does **not** mean “mathematically deep” or “should be auto-solved.”

## Corpus

- [SorryDB data](https://github.com/SorryDB/sorrydb-data) — `static_100_varied_recent_deduplicated_sorries.json`
- [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) — small Erdős statement sample

## Dual metrics

| Check | Owns |
|-------|------|
| Lean kernel / CI | Correctness of proofs |
| `attention` | Process triage |

## Seal

- pack_id: `LEAN0_PACK_20260805T234543Z`
- pack_root_sha256: `91863e8dcef9204ddb4745e16565f29199d9aa799661832b98619df39ed8c502`
- proof_manifest_sha256: `9081dd86485d48c46107daeda849eccf8122e128ea58712b99d92fc62bd33a75`

## Norms

Public data only · no automated PRs without maintainer consent · English glosses are informal aids, not formal statements.
