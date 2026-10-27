# ViZDoom rung_r3p5 r1.13 — P0 perception probe on a fresh sealed seed (PASS, 3 of 3 fits)

GO-RGL-INTERP-1, rung_r3p5, ViZDoom map KD05. A pre-registered perception probe ("P0") asks whether a small convolutional probe trained on recorded demo frames can tell, from the RGB frame alone, whether an enemy is visible (visible AUC) and on which side of the screen it is (left/right accuracy). This is a gate: a P0 PASS unblocks the next step of the rung (behaviour cloning / PPO), which runs under its own spec.

**In short: PASS on the fresh sealed test seed 67150, scored once.** All three repeat fits cleared both bars (visible AUC ≥ 0.85 AND L/R ≥ 0.80); the median fit (C) gave AUC 0.9657 and L/R 0.8222. The L/R margin is modest (0.8098–0.8241) and L/R on small (distant) enemies stayed below 0.80 in every fit (0.696–0.726; report-only).

## Headline

| fit | RNG seed | stop | chosen step | visible AUC | L/R | small L/R (report-only) | large L/R (report-only) | pass |
|---|---|---|---|---:|---:|---:|---:|---|
| A | 67140 | patience @ 23,360 | 16,060 | 0.9657 | 0.8241 | 0.7197 | 0.8984 | yes |
| B | 1,130,001 | patience @ 27,740 | 20,440 | 0.9649 | 0.8098 | 0.6959 | 0.8907 | yes |
| C (median) | 1,130,002 | patience @ 21,900 | 18,980 | 0.9668 | 0.8222 | 0.7259 | 0.8907 | yes |

- Run rule (all must hold): ≥ 2 of 3 fits pass; the median fit passes; median AUC ≥ 0.85 and median L/R ≥ 0.80. Result: 3/3, median fit C passes, medians 0.9657 / 0.8222. Verdict **PASS**.
- Test seed 67150: 20,000 steps, 4,663 visible frames (1,937 small, 2,726 large; left fraction 0.490); adequacy floors met on the first try.

## Setup

- Recipe unchanged from the r111c T1 probe recipe (`r19b_p0.ProbeNet2`, Adam 1e-3, batch 64 half-visible, mirror augmentation). Two pre-registered changes only: 24 training seeds (67170–67194 minus 67172) and early stopping on a separate validation seed (67172; patience 5 evals of 1,460 steps, min 14,600, cap 58,400).
- Three fits differ only in their RNG seed. Scoring on 67150 happened once, after Verify wrote `FROZEN_r1.13.json`; the seal marker was written before 67150 was first recorded.
- CPU only. Peak RGL process-tree RSS 1,289 MiB during fits (cap 6,144 MiB). Fits ran 00:24–01:53 CDT and scoring 01:53–01:56 CDT on 2026-10-27.

## What is in this folder

Proof only. The run code, tests, data pins, deviation log, Verify package, Verify reports and run log are held in the lab's private archive. `SHA256SUMS.txt` lists the sha256 of every one of those files as published proof; anyone given the private copies can check them with `shasum -a 256 -c`.

- `rung_r3p5/RUNG_SPEC_r1.13_P0_SEEDS.md`: the pre-registration (rev2), sha256 `c30174eccd46bc209fc7a36e77fb2492278d377727a2b3b2d15c764ca1189872`.
- `rung_r3p5/r113/FROZEN_r1.13.json`: Verify's freeze record (spec sha, code file hashes, seeds). Hashes only.
- `results/score/`: VERDICT, SCORES csv (sha256 `184e05bd49d1df41ef2cf48b521f19075f3f2fa68696700502cb6b5aebb69fd2`), WRITEUP, ADEQUACY and the seal marker.
- `SHA256SUMS.txt`: hashes for every file of the r1.13 package, public and held back.

## Disclosures

- Held back (private archive, hashes in `SHA256SUMS.txt`): source code and tests, data pins, the deviation log (DV-R261 to DV-R282, part of the spec), the Verify package, both Verify reports and the run log. An earlier commit (21852a1) published these by mistake; they were removed from the tree in the next commit, but they remain in git history.
- The pre-registration was frozen by Verify before the sealed seed was recorded, but unlike the Path B preregs it was not published here before the run; this folder is the first public copy.
- Not published: demo recordings, per-frame predictions, model checkpoints and per-fit logs.
- A P0 PASS is a perception gate, not a result about RGL's routing. No ViZDoom routing results are published yet.
- Family and route names elsewhere in this repo are labels only. Nothing here is a clinical result.

## Footer

Independent VERIFY rev2: PASS with notes (report sha256 `cb382a5da25d16beacf643461c479aad27ef5fa2fd57d8aa8f67b7983b118948`).

clinical_claim: false · proof/micro-env/model
