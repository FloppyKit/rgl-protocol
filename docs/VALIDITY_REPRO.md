# Validity & reproducibility (Path B / RGL micro-env proofs)

**Status:** published with Path B Proof-8 stack · 2026-09-21 America/Chicago  
**clinical_claim: false**

This note states how to read sealed Path B micro-env proofs: what kind of validity they claim, how seals work, and what they do **not** claim.

## Construct / internal / external validity

| Kind | What we mean here | Path B practice |
|------|-------------------|-----------------|
| **Construct** | Does the harness measure the intended residual-steered thrash vs baselines? | Named policies (`blind`, `scripted_kite` / `role_scripted`, `measured_thrash`); battle law explicit (no cool→HOLD while enemy alive); metrics include success, waste, engage_holds, phase stats |
| **Internal** | Within the sealed run, do comparisons support the headline? | Fixed seeds; CSV + SHA256 anchors; VERIFY Bot gates; inverse and thrash>baseline both publishable |
| **External** | Does it generalize outside this micro-env? | **Not claimed.** Ladder is intentional (trash-mob → boss → harder → asymmetric → …). Each GO is a narrow seal |

## Bit-seal vs independent re-run vs sensitivity pack

1. **Bit-seal (default public timestamp):** content SHA256 of episodes/summary/WRITEUP on nest; redacted headline + anchors on this repo. Recomputing hashes on the nest artifacts should match.
2. **Independent re-run:** another machine runs the harness with the same seeds/flags from `VERIFY.md` / README. Expect stochastic ties only where documented; PASS requires gates, not byte-identical CSVs unless seeds and code match exactly.
3. **Sensitivity pack (later GOs):** vary τ, rage/vuln lengths, fog radius; publish only redacted summary deltas. Discovery stays **append-only** — do not rewrite past sealed headlines; add a new GO or an appendix note.

## Discovery append-only

Sealed GO writeups and public timestamp docs are append-only. Language-lock fixes that change WRITEUP SHA are allowed only with VERIFY re-PASS and an updated public WRITEUP anchor (as in Proof-7). Do not silently edit old scores.

## Non-claims

- Not a clinical claim; not therapy; not DSM software  
- Not SOTA RL; not full SMAC/SC2  
- Not proof that residual maps dominate all baselines forever  
- Cool residual ≠ automatic win (Path B battle law)  
- Public buzz ≠ nest full log  

## Related

- Path B scoreboard: [PATHB_SCOREBOARD.md](PATHB_SCOREBOARD.md)  
- Protocol core: [PROTOCOL.md](PROTOCOL.md)
