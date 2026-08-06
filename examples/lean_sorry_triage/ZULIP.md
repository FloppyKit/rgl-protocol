# Zulip / GitHub — paste-ready (live URLs)

Repo is public on `main`.

**Landing:** https://github.com/FloppyKit/rgl-protocol/tree/main/examples/lean_sorry_triage  
**README:** https://github.com/FloppyKit/rgl-protocol/blob/main/examples/lean_sorry_triage/README.md

---

## Option A — ultra short (recommended)

```text
hey — tiny experiment on the public SorryDB static-100 list:
rank open `sorry`s by a cheap process "attention" score (where look next),
not difficulty, not proofs, no auto-PRs.

https://github.com/FloppyKit/rgl-protocol/tree/main/examples/lean_sorry_triage

Example: infinity-cosmos product-of-isofibrations sorry ranked relatively high;
English gloss + pretty-printed goal in the README.

curious if triage like this is useful for anyone — fine if not
```

---

## Option B — one notch more context

```text
**lean_sorry_triage** (homework / experiment)

We ranked public open Lean obligations (SorryDB static-100 + a few
Formal Conjectures statement files) by an offline process-attention score.

- kernel / `lake build` still owns correctness
- `attention` only means "maybe look here next"
- no multi-head LLM scoring in this pack ($0 heuristic)
- will not open automated PRs (SorryDB norm)

https://github.com/FloppyKit/rgl-protocol/blob/main/examples/lean_sorry_triage/README.md

If the ranking is silly for your repo, that feedback is gold.
If useless entirely, ignore — no FOMO.
```

---

## Option C — GitHub Discussion title

```text
Experiment: process-attention ranking over public SorryDB sorries
(not solutions; feedback welcome)
```
