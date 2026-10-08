# Path B Proof 26 — preregistration hash (published before running)

clinical_claim: false · proof/micro-env/model

GO-RGL-PATHB-PROOF-26: preregistered 7-arm unified affect-bias sweep on DeepMind Melting Pot `predator_prey__orchard_3`, seeds 27000–27249 (n = 250 per arm).

- PREREG.md sha256: `001d35c7401b452d1f0f6f39d0d8d454f956a9890d13ee2f3a7c218cddbeb721`
- Frozen locally: 2026-10-07 18:50:59 CDT
- Published here: 2026-10-07, before any confirmatory seed (27000–27249) was run
- Full PREREG.md text: `docs/PATHB_PROOF26_ORCHARD_PREREG_2026-10-07.md` (this commit)

Disclosures:
- The 30–70% calibration band was revised to 15–70% after the P25 re-pilot (balanced 0.22) and before any P26 data. P25 stays a FAIL against its own rule.
- The primary success definition (food ≥1 AND eaten ≤2 times by step 1000) originated post-hoc in the P24 pilot; it was locked before P25 and is unchanged for P26.
- An earlier local freeze (sha 0c6cb04b…11a8, 18:50:32 CDT) was superseded 27 seconds later after removing Python bytecode caches from the hashed file list; no design text changed in between.
