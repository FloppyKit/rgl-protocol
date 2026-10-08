# Path B Proof 29 — preregistration hash (published before running)

GO-RGL-PATHB-PROOF-29: does balanced RGL still beat a random policy that matches both its route shares and how long it stays on each route (dwell)? Melting Pot `predator_prey__orchard_3`. Three arms (`balanced_rgl`, `dwell_random`, `random_mix`), seeds 30000–30566 (n = 567 per arm, 1701 episodes).

- PREREG.md sha256: `6d05a6639964eaf7ec60183045c18325e1b77699df5f4a142bd64af2a67f0edb`
- Frozen locally: 2026-10-08 14:11:08 CDT
- Published here: 2026-10-08, before any confirmatory seed (30000–30566) was run
- Full PREREG.md text: `docs/PATHB_PROOF29_ORCHARD_DWELL_PREREG_2026-10-08.md` (this commit)

Disclosures:
- `dwell_random` is a semi-Markov chain fitted to balanced's per-step route traces from a calibration run on non-confirmatory seeds 30900–30999 (balanced only, 100 episodes). It never reads the state. Only route-trace columns were used to fit it.
- Before freezing, the dwell fit was corrected: a first draft treated death-ended runs as censored, which inflated fight dwell to 19.4 steps against 4.79 observed. A death now ends a run. The before/after numbers are in the prereg. No confirmatory seed had run.
- `random_mix` is unchanged from P28 (per-step draw from P27 balanced route shares), kept as a replication anchor.
- Primary analysis: one-sided Fisher exact tests, H1 balanced > dwell_random (primary) and H2 dwell_random > random_mix, Holm at family α 0.05. Balanced must land in the P28 band [0.15, 0.70]. Power is exact Fisher: at n = 567, 80% for an H1 gap of 0.07.
- If dwell_random ties or beats balanced, the write-up will say the P28 advantage over the random mix is explained by route persistence, not by state-based choice. Null and inverse results are published.

## Footer

clinical_claim: false · proof/micro-env/model
