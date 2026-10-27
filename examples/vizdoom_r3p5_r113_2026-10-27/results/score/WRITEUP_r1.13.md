# r1.13 P0-SEEDS sealed result: PASS

Test seed 67150 (20000 steps, 4663 visible frames). Bars: visible AUC >= 0.85 AND L/R >= 0.8. Rule: >= 2 of 3 fits pass, the median fit passes, medians clear both.

| fit | init seed | stop | chosen step | AUC | L/R | small L/R | large L/R | pass |
|---|---|---|---|---|---|---|---|---|
| A | 67140 | patience @ 23360 | 16060 | 0.9657 | 0.8241 | 0.7197 | 0.8984 | True |
| B | 1130001 | patience @ 27740 | 20440 | 0.9649 | 0.8098 | 0.6959 | 0.8907 | True |
| C | 1130002 | patience @ 21900 | 18980 | 0.9668 | 0.8222 | 0.7259 | 0.8907 | True |

n_pass 3/3; median fit C; median AUC 0.9657069506167051; median L/R 0.8222174565730217.

PASS -> BC/PPO may proceed under its own spec. FAIL -> 67150 is burned: no re-scoring, no bar or rule change, no new fit scored on 67150; any next step needs a new pre-registration and a new fresh seed (spec §5).
clinical_claim: false.
