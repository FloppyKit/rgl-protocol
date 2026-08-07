---
title: "Residual weighting + hormetic contact (public stub)"
status: hypothesis-stub
clinical_claim: false
version: "0.1"
created: 2026-08-07
---

# Residual weighting + hormetic contact (public stub)

**Status:** conceptual open-science note · **not** an implementation · **not** clinical guidance.

This documents a *process* idea for multi-agent residual systems: raw residual magnitude is underdetermined; **context weights** what residual should move the system, and **controlled residual contact** can be high-value only when a **clearance** condition holds.

## Problem

Δ residual alone does not say whether residual is:

- informative update signal,
- noise / weather,
- false quiet (cool via freeze),
- productive thrash,
- or hard-stop chaos.

## Sketch

```text
residual_path     → sensor trajectory
object_family     → what kind of unresolved process residual evidences
binding_context   → which priority stratum currently binds attention
weight            → how much residual may update the system
clearance         → whether deliberate elevated residual is allowed
```

**Priority stack (illustrative, not a therapy model):**

| Binding context | Preferentially weight | Defer “growth” residual until secure |
|-----------------|----------------------|--------------------------------------|
| Safety / hard gate | collapse, harm language, pure chaos | novelty thrash |
| Coordination / alignment | mismatch, rupture-like divergence | pure score noise |
| Task agency | stuck thrash vs productive thrash | background weather |
| Edge exploration | coherent elevated residual with later structure gain | low-stakes mismatch |

## Hormetic contact (lab process)

**Hormetic residual contact** means: intentionally allow elevated residual *briefly* when:

1. coherence remains holdable (hard gate does not fire),
2. residual later settles to a **better** process baseline,
3. cool-down is not achieved by silencing / freezing the signal.

When those fail, elevated residual is just **burn** or **false peace**, not learning.

**Maxwell-demon framing (metaphor):** selectively open a gate on a residual gradient only for informative, recoverable trajectories — not for noise, exile-without-integration, or unsecured base conditions.

## What this repo does *not* claim

- No clinical Maslow validation  
- No therapy protocol  
- No automatic “more residual is better”  
- No replacement for hard safety / disclosure gates (hard gate always wins)

## Related public docs

- [PROTOCOL.md](./PROTOCOL.md) — residual axes, soft/hard gates, thrash labels  
- [RESIDUAL_OFFER.md](./RESIDUAL_OFFER.md) — pilot framing for finding streams  
- [BTC_RESIDUAL_OVERLAY.md](./BTC_RESIDUAL_OVERLAY.md) — worked method shape  

Private research may extend object families (pointers) and offline scoreboards; those are out of scope for this repository.
