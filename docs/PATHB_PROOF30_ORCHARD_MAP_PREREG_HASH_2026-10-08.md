# Path B Proof 30 — preregistration hash (published before running)

GO-RGL-PATHB-PROOF-30: does the specific emotions map matter beyond any state-reactive switching, and does RGL beat an equally informed controller with no emotion labels? Melting Pot `predator_prey__orchard_3`. Four arms (`rgl_v1`, `shuffled_map`, `heuristic_noaffect`, `random_mix`), seeds 31000–31566 (n = 567 per arm, 2268 episodes).

- PREREG.md sha256: `9bd9215d4821605a2c4b834e354a6068cbc9a0f2c15b2848075fb4cc20c3411a`
- Frozen locally: 2026-10-08 21:47:17 CDT
- Published here: 2026-10-08, before any confirmatory seed (31000–31566) was run
- Full PREREG.md text: `docs/PATHB_PROOF30_ORCHARD_MAP_PREREG_2026-10-08.md`
- RGL spec v1 sha256: `e620509377516858d1d1e3677a14f977c76549608e93702dc5dc7a5735487475`

Disclosures:
- `rgl_v1` is the frozen RGL spec v1 balanced controller, unchanged from P28 and P29 (action-identical to P28 balanced on scratch seeds 100 and 101).
- `shuffled_map` keeps the same features, scores and actions but executes a deranged trigger-to-action pairing: four within-block three-cycle derangements, pooled, assigned to seeds with `numpy.random.default_rng(30030)` (assignment sha256 `541709b8684a6df0344b4e543df6e22c968fa297998807715219f9eef967afbe`).
- `heuristic_noaffect` is a plain rule with no emotion labels (flee within distance d, else deposit acorn, else food). Its setting was chosen by code from a locked 24-setting grid on 100 non-confirmatory calibration seeds (31600–31699, 2400 episodes): d = 6, straight-away flee, no commitment, 37/100 calibration success. That rate is the best of 24 on the same seeds, so it is optimistic.
- How the P21 weights in RGL's scores were chosen is not recorded.
- Primary analysis: one-sided Fisher exact tests, H1 rgl_v1 > shuffled_map (primary) and H2 rgl_v1 > heuristic_noaffect (superiority), Holm at family α 0.05. rgl_v1 must land in the band [0.15, 0.70]. Power is exact Fisher: at n = 567, 80% for a gap of 0.07.
- If the heuristic ties or beats RGL, the write-up will say the emotion structure adds nothing over a plain rule in orchard. Null and inverse results are published.

## Footer

clinical_claim: false · proof/micro-env/model
