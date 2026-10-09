# Path B Proof 31 — preregistration hash (published before running)

GO-RGL-PATHB-PROOF-31: on Melting Pot `predator_prey__open_3`, does frozen RGL v1 beat a deranged route map and the locked plain rule, and does skipping its ally branch cost allies? Five arms (`rgl_v1`, `shuffled_map`, `heuristic_noaffect`, `random_mix`, `love_noally`), seeds 32000–32566 (n = 567 per arm, 2835 episodes).

- PREREG.md sha256: `51457170183d66df38c18f03d92f36828bd9927bb5cb2555ed8b9614d1ef0eef`
- Frozen locally: 2026-10-09 09:11:05 CDT
- Published here: 2026-10-09, before any confirmatory seed (32000–32566) was run
- Full PREREG.md text: `docs/PATHB_PROOF31_OPEN3_NOGRASS_PREREG_2026-10-09.md`
- RGL spec v1 sha256: `e620509377516858d1d1e3677a14f977c76549608e93702dc5dc7a5735487475`
- RGL v2 pre-statement sha256 (cited, not used): `32b70b13a7cfd64cb836e84aa4be1072ded796e381f4c97a5cc085ce1cd4e13d`

Disclosures:
- A second world, a locked no-grass variant of open_3, was greenlit behind a pre-stated feasibility gate. It failed check F4 on feasibility seeds 32900–32929: both baseline arms scored 0/30 on primary success (the focal prey was eaten 3–6 times per episode without cover). By the pre-stated fallback it is dropped, H3 (prediction c) is deferred to a later GO, and no seed in 33000–33566 is run. No RGL success number was computed in the feasibility block.
- `rgl_v1` is the frozen RGL spec v1 balanced controller, action-identical to P30's `rgl_v1` on scratch seeds.
- `shuffled_map` executes P30's four within-block derangements, assigned to seeds with `numpy.random.default_rng(31031)` (assignment sha256 `bfa5bc139a03d218522c6c4e8a0af50ec607809cd949d3e2e0d5b25cd767187f`).
- `heuristic_noaffect` is P30's locked plain rule (config 18: d = 6, straight-away flee, no commitment), not retuned on open_3. It scored 20/30 in the open_3 screen.
- `love_noally` differs from `rgl_v1` by one mapper line (the step-toward-ally branch is skipped).
- Primary analysis: H1 rgl_v1 > shuffled_map and H2 rgl_v1 > heuristic_noaffect (one-sided Fisher exact), H4 love_noally > rgl_v1 on allies eaten per episode (one-sided Welch), Holm over three tests at family α 0.05. rgl_v1 must land in the band (0.05, 0.90). 80% power for a success gap of about 0.09 at n = 567.
- Null and inverse results are published.

## Footer

clinical_claim: false · proof/micro-env/model
