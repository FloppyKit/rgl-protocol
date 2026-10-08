# Path B Proof 27 — preregistration hash (published before running)

clinical_claim: false · proof/micro-env/model

GO-RGL-PATHB-PROOF-27: dose-response of affect bias on Melting Pot `predator_prey__orchard_3`. Balanced plus 18 dosed arms (6 affects × LOW/MID/HIGH), seeds 28000–28199 (n = 200 per arm).

- PREREG.md sha256: `b48ae50cf679ed349c2a3a4303276eb1ee106cd4ea8cd53f6885b8ff6cadf344`
- Frozen locally: 2026-10-07 22:26:53 CDT
- Published here: 2026-10-07, before any confirmatory seed (28000–28199) was run
- Full PREREG.md text: `docs/PATHB_PROOF27_ORCHARD_DOSE_PREREG_2026-10-07.md` (this commit)
- Note: an earlier push of this prereg (commit 919aa46) was not byte-identical to the frozen file and was superseded by this commit before any confirmatory seed ran. No seed in 28000–28199 has been run.

Disclosures:
- Dose levels were chosen from route-share calibration on burned seeds 98000–98019 only; food/eaten/success were never read during calibration.
- Flight and love_autopilot already used their own route at >25% under balanced, so their LOW doses start at the smallest grid bias; several MID/HIGH picks were bumped up the grid so the three doses differ.
- Primary analysis: Cochran-Armitage trend on success across dose 0 / LOW / MID / HIGH, one test per affect, Holm at family α 0.05.

## Footer

clinical_claim: false · proof/micro-env/model