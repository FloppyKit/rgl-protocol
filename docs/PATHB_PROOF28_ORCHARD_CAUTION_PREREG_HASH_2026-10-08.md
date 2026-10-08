# Path B Proof 28 — preregistration hash (published before running)

GO-RGL-PATHB-PROOF-28: does a small dose of caution beat balanced RGL, and does balanced beat a random mix of routes at the same rates? Melting Pot `predator_prey__orchard_3`. Four arms (`balanced_rgl`, `flight_b0.05`, `freeze_b0.30`, `random_mix`), seeds 29000–29566 (n = 567 per arm, 2268 episodes).

- PREREG.md sha256: `c9054a181cf7b66532d43e573767a48feda5d6565e5c59077c44d81f2cee5b53`
- Frozen locally: 2026-10-08 08:39:08 CDT
- Published here: 2026-10-08, before any confirmatory seed (29000–29566) was run
- Full PREREG.md text: `docs/PATHB_PROOF28_ORCHARD_CAUTION_PREREG_2026-10-08.md` (this commit)

Disclosures:
- The two caution doses are the P27 LOW doses for flight and freeze, chosen after seeing P27. Flight LOW was the best of 18 dosed arms there, so winner's curse applies and a null is a live outcome.
- `random_mix` probabilities are balanced's measured route shares from P27, frozen before this run.
- Primary analysis: three one-sided Fisher exact tests (H1 flight > balanced, H2 freeze > balanced, H3 balanced > random_mix), Holm at family α 0.05. n chosen for 80% power at +0.08 over p0 = 0.25.

## Footer

clinical_claim: false · proof/micro-env/model
