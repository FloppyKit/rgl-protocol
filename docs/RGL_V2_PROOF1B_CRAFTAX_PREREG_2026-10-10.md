FROZEN 2026-10-10 08:41:22 CT. Matt approved 2026-10-10 08:00 CT. clinical_claim: false.

# PREREG: GO-RGL-V2-PROOF-1b, first v2 confirmatory test on Craftax

This is the frozen preregistration for GO-RGL-V2-PROOF-1b. Where it differs from `GO.md` sections 4–8, this document governs. Frozen spec under test: `/Users/dude/rgl-proofs/RGL-SPEC-v2/RGL_SPEC_v2.md`, sha256 `855ae5572ac55d0cab3eb2f4ca40a9197080cbc150094629847028b3680b80d2`. Route names are machine option labels for route families; nothing here claims or implies inner experience in a model. Inverse, null and inconclusive results are published with the same prominence as wins. v1 losses (P30, P31) stay on the record and are not revised by any v2 result.

## 0. Status of the record at drafting

- Phase A (determinism 60200–60209, smoke 60210–60219) and the A2 pilot (60300–60399) ran on 2026-10-09 under code bundle `3514c979…`. Rows: `results/episodes.jsonl` (300). Pilot report, unchanged: `logs/A2_PILOT_REPORT.md` (plain_flee_eat 0/100 and shelter_night 0/100 alive at step 10,000; ceiling switch not tripped).
- Pre-freeze re-run on the final code (bundle in logs/CODE_SHA.txt), 2026-10-10 08:25–08:37 CT: determinism 60220–60229 passed (`rgl_v2` and `shelter_night`, both worlds, two cold processes each, 20 of 20 trajectory hashes identical, separate processes); smoke 60230–60239 passed (every arm, both worlds, 360 episodes, 0 errors, 0 conformance violations, 0 stalls). Rows in results_rerun/; not analysed.
- No confirmatory seed (61000–61416 Classic, 62000–63199 dark) and no stage-2 seed (61500–61707 Classic, 63200–63799 dark) has been stepped.
- The design below was revised on 2026-10-10 before the freeze (see the changelog). The code was changed in the same revision (shelter_night flee branch, stall rule, stock terminal flag); Phase A determinism and a scratch rehearsal must pass again on the new code before Phase B (section 10).

## 1. Worlds and start states

- Classic: Craftax-Classic symbolic, craftax 1.6.1, default `EnvParams`, horizon 10,000 steps (the world's `max_timesteps`).
- Dark floor: full Craftax symbolic, craftax 1.6.1, default `EnvParams`, evaluation horizon 3,000 steps (an evaluation censor inside the world's 100,000 limit; D12).
- Every arm starts from the same stock start state for a given seed. On Classic that is the default reset for the seed's reset key. On the dark floor it is the default reset plus the declared D2 START-STATE EDIT and nothing else: `player_level` = 2 and the player position = the up-ladder cell that the world's own generator placed on that floor. Levels are stock Craftax procedural generation; no map, mob, light, inventory or parameter edit. The edit's conformance check (GO section 1.2) stays.
- Pairing: same reset key and same step-key stream per seed for every arm (common random numbers).

## 2. Outcomes

### 2.1 Primary (both arenas): steps survived

Steps survived per episode, capped at the horizon (Classic 10,000; dark floor 3,000).

- Death is the world's stock terminal signal: `done` returned by `step_env`, which is `env.is_terminal(state, params)` → `is_game_over`. In craftax 1.6.1 Classic (`craftax_classic/game_logic.py` `is_game_over`) that is `timestep >= max_timesteps` OR the player stands on lava OR `player_health <= 0`. In full Craftax (`craftax/game_logic.py` `is_game_over`) it is `timestep >= max_timesteps` OR `player_health <= 0` OR the final boss is beaten. A `done` before the world's step limit is a death at that step, except a beaten-boss end (not a death; scored as survival to the horizon; not expected on floor 2 within 3,000 steps).
- Stall: no change in player position AND no change in any inventory field AND no change in the achievement flags for K = 300 consecutive steps. A stall is a death at the stall step, defined as the last step on which anything changed (the start of the frozen run). The episode ends at the stall.
- Why K = 300: it is the world's `day_length` (K14), so a full day-night cycle passes with nothing changing; it is below the zero-intake death time `H_max` (ADAPTER_FREEZE.md), so a genuinely frozen agent is scored as stalled before starvation would end it; and a legitimate night of sleep or sheltering wakes on energy refill or changes the inventory well inside 300 steps. A shorter K (for example 100) would score a long sleep as a stall; a longer K would let freeze-lock count as life.
- The cap is scored only if the agent is alive (no stock death) and not stalled at the horizon. A harness timeout is not a success; it is an incomplete episode and follows the rerun rule (GO section 10).

### 2.2 Co-primary (both arenas): achievements

Stock achievements unlocked per episode: the sum of the boolean array `EnvState.achievements` at episode end, set only by the world's own game logic. Source field, craftax 1.6.1: `craftax_classic/envs/craftax_state.py` line 68 (`achievements: jnp.ndarray`, 22 flags indexed by `craftax_classic/constants.py` `Achievement`) and `craftax/craftax_state.py` line 102 (67 flags indexed by `craftax/constants.py` `Achievement`). Counted over the episode up to its end (death, stall, or horizon).

### 2.3 Team survival

Not applicable in single-player Craftax: the state has one player and no ally, so `r = 0` and CARE is ineligible. Team survival and principle 3 are deferred to the ViZDoom confirmation GO (GO section 12). No zero team score is reported as a result.

### 2.4 Reported secondary, not tested

- Achievements per 100 steps alive: `100 × achievements / steps survived`.

### 2.5 Exploratory, reported, not tested

- Classic day-window fraction (old GO section 4.1).
- Survival to the cap (binary), Classic and dark.
- Dark binary survival at 3,000 with stall as failure (old GO section 4.3).
- Zombie damage per 1,000 alive steps; route shares; flee, sleep and place-stone counts.
- The ceiling switch is removed (no pilot-triggered change of primary).
- Equivalence (section 4.4).

## 3. Arms

As GO section 3, with one change: `shelter_night` now has a flee branch (Matt approved 2026-10-10 07:30 CT). When a visible threat is within the zombie chase radius (Manhattan < 10, K12/K29), it takes the same flee step as `plain_flee_eat`; otherwise it follows its shelter logic (K28 light cut → `PLACE_STONE` then `SLEEP`; else most-depleted need). On the dark floor "visible" is the world's mask `light_map > 0.05`. Note for the reader: the two baselines now differ only once the K28 night cut is true (`shelter_night` walls in and sleeps; `plain_flee_eat` keeps foraging), so by day they act the same and their results are expected to be close.

Confirmatory arms: Classic `rgl_v2`, `planner_ei`, `plain_flee_eat`, `v1-port`, `abl_no_urgency`; dark `rgl_v2`, `planner_ei`, `abl_no_freeze`. Descriptive arms: the rest of GO section 3.1.

## 4. Hypotheses and tests

### 4.1 Contrasts (unchanged from GO section 5, re-expressed)

| id | arena | contrast | direction |
|---|---|---|---|
| H1 | Classic | `rgl_v2` vs `planner_ei` | `rgl_v2` survives longer |
| H2 | Classic | `rgl_v2` vs `plain_flee_eat` | `rgl_v2` survives longer |
| H3 | Classic | `rgl_v2` vs `v1-port` | `rgl_v2` survives longer |
| H4 | Classic | `rgl_v2` vs `abl_no_urgency` | `rgl_v2` survives longer |
| H5 | dark | `rgl_v2` vs `planner_ei` | `rgl_v2` survives longer |
| H6 | dark | `rgl_v2` vs `abl_no_freeze` | `rgl_v2` survives longer |

If `v1-port` cannot bind (port items 1–9), H3 is removed before any confirmatory seed and the family has five tests.

### 4.2 Test

For each contrast: per-seed difference `d_s = Y(rgl_v2, s) − Y(comparator, s)` on the same seeds. Statistic: mean of `d_s`. One-sided paired sign-flip permutation test (each seed's sign flipped with probability 1/2), 10,000 permutations, p = (1 + #{T* ≥ T}) / 10,001. Two-sided 95% paired percentile bootstrap interval, 10,000 resamples of seeds.

Generator seeds (inside 64000–64099): primary permutation H1–H4 64000–64003, H5 64005, H6 64007; primary bootstrap = permutation seed + 10; co-primary permutation = primary permutation seed + 30, bootstrap + 40; stage-2 permutation = primary permutation seed + 50 (co-primary stage 2 + 60). 64080 stays the derangement seed.

### 4.3 Multiplicity

Family 1: H1–H6 on the primary. Family 2: H1–H6 on the co-primary. Each family uses Holm step-down at family alpha 0.05, one-sided. Within a family, Holm is applied to each hypothesis's overall two-stage p-value (section 5), which is valid because each hypothesis's two-stage test is a level-α test for every α (closed testing with Bonferroni intersections). The two families are separate pre-stated claims; the co-primary is not used to rescue the primary.

### 4.4 Equivalence (exploratory, outside Holm)

The old ±0.05 margin was on a proportion and no longer fits a step count. It is replaced by an exploratory equivalence test on the standardized paired mean difference `d_z = mean(d) / sd(d)`, margin ±0.15, TOST at α = 0.05 each side (normal approximation, SE ≈ sqrt(1/n + d_z²/(2n))). Kept because H1 and H5 ask whether route grouping matters against an equally informed planner, and "equivalent" is an informative answer there. Margin 0.15 is about two thirds of the minimum effect in standardized units (Classic 0.229, dark 0.172), and at n = 417 a true d_z of 0 gives roughly 84% probability of declaring equivalence. It is reported for every contrast, used in a sentence only for H1 and H5, and never changes a Holm label.

### 4.5 Minimum effect and n

Minimum effect, pre-stated (Matt, 2026-10-10 07:30 CT): 15% longer mean survival than the comparator. In steps, from the pilot and determinism data (variance only):

- Classic: 15% × 237.1 (pilot `plain_flee_eat` mean, the strongest observed baseline) = 35.6 steps.
- Dark: 15% × 130 (uncensored dark determinism means: `rgl_v2` 142.1, `shelter_night` 129.5; the lower one) = 19.5 steps (planning value). The scratch rehearsal (throwaway seeds 69040–69059, 20 per arm, new code) showed lower dark means, 93–115 steps, and an SD up to 105; at a baseline of 95 the 15% effect is 14.2 steps.
- In the conclusion sentences, "15% of the baseline" is 0.15 × the comparator's observed mean steps survived in the confirmatory data (reported as `min_effect_15pct` by the analysis).

Variance (no contrast of interest is computed): per-arm SD of steps survived, Classic 110 (pilot `plain_flee_eat` 103.3, determinism `rgl_v2` 98.1, determinism `shelter_night` 113.4, n = 10), dark 80 (determinism `rgl_v2` 78.6, `shelter_night` 56.1). Smoke rows are censored at 200 and are not used for SD. Paired SD is taken conservatively as if the within-seed correlation were 0: SD(d) = √2 × SD, so 155.6 (Classic) and 113.1 (dark). Standardized effect d_z = 0.229 (Classic), 0.172 (dark).

Single-look requirement at one-sided α = 0.05/6 = 0.00833, 80% power: n = (z_α + z_β)² / d_z² with (2.3940 + 0.8416)² = 10.469: Classic 200, dark 352. n = 417 is kept for Classic (single-look power 0.99). Dark n is raised to 1,200 per arm (Matt, 2026-10-10 08:00 CT, before the freeze), because the scratch rehearsal variance (baseline about 95, SD about 105, SD(d) about 148.5) gives d_z = 0.096 at the 15% effect, which needs about 1,140 seeds single-look; single-look power at 1,200 is 0.82.

Under the two-stage design (section 5) at the first Holm level, simulated power at the minimum effect (2,000,000 draws): Classic 1.00 (stage 1 alone 0.95, n1 = 417, n2 = 208). Dark at n1 = 1,200, n2 = 600, using the scratch variance (d_z = 0.096): 0.95 (stage 1 alone 0.62; stage 2 triggered with probability 0.38); using the earlier planning variance (d_z = 0.172): 1.00. Type-I error of the two-stage rule under the null: Classic 0.00833, dark 0.00833 (target 0.00833).

Co-primary minimum effect: 0.25 achievements per episode (about 10% of the observed baseline 2.6). Per-arm SD ≈ 1.0, SD(d) ≈ 1.44; n for 80% at 0.05/6 = 349, below 417. Detectable at 417: 0.23 achievements.

## 5. Two-stage sample-size extension (Matt requested before the freeze, 2026-10-10 07:32 CT)

Stage 1: Classic n1 = 417 seeds per arm (61000–61416); dark n1 = 1,200 seeds per arm (62000–63199). All arms that survive the time rule.

Stage 2: at most ONE fixed batch of fresh seeds per confirmatory arm, half of stage 1 in each arena: Classic n2 = 208 (61500–61707), dark n2 = 600 (63200–63799). Stage 2 runs only the confirmatory arms (Classic `rgl_v2`, `planner_ei`, `plain_flee_eat`, `v1-port` if H3 is in the family, `abl_no_urgency`; dark `rgl_v2`, `planner_ei`, `abl_no_freeze`), both arenas together. Seed check 2026-10-10: zero cells in seed columns of 338 episode CSV/JSONL files under `/Users/dude/rgl-proofs` (P4–P31, V2-PROOF-1, V2-PROOF-1b); no mention in any GO, PREREG or WRITEUP (the only text match is a hex fragment in P29 sha lines); no overlap with 61000–61416, 64000–64099, 60200–60399 or 69000–69099. Dark blocks 62000–63199 and 63200–63799 re-checked 2026-10-10 08:12 CT: zero seed-column cells in 343 episode CSV/JSONL files under `/Users/dude/rgl-proofs`, no text mention in any prior GO, PREREG or WRITEUP (the only matches are this GO's own old block endpoints 62417, 62500, 62707), no overlap with Classic 61000–61416 or 61500–61707, 60200–60399, 64000–64099 or 69000–69099. The earlier dark stage-2 block 62500–62707 is withdrawn (inside the new stage 1), never stepped.

Method: inverse-normal combination test with pre-fixed weights per arena, Classic w1 = √(417/625) = 0.8168, w2 = √(208/625) = 0.5769 (information fraction t = 0.6672), dark w1 = √(1200/1800) = 0.8165, w2 = √(600/1800) = 0.5774 (t = 0.6667), stage-wise one-sided permutation p-values p1, p2 converted by Z_k = Φ⁻¹(1 − p_k), combined Z = w1·Z1 + w2·Z2. Efficacy bounds follow a 2-look Lan-DeMets O'Brien-Fleming-type spending function, α1(α) = 2 − 2Φ(z_{1−α/2}/√t), with the final bound c2 set so the total one-sided level is α. Futility is non-binding: Z1 ≤ 0 (estimate does not favor `rgl_v2`) contributes no stage-2 rejection.

Bounds at each Holm level, Classic (t = 0.6672; Z scale; stage-1 bound b1, final combined bound c2):

| Holm level α | α1 | b1 | c2 |
|---|---|---|---|
| 0.05/6 = 0.00833 | 0.00124 | 3.0262 | 2.4119 |
| 0.05/5 = 0.0100 | 0.00161 | 2.9453 | 2.3461 |
| 0.05/4 = 0.0125 | 0.00223 | 2.8437 | 2.2638 |
| 0.05/3 = 0.0167 | 0.00338 | 2.7084 | 2.1543 |
| 0.05/2 = 0.0250 | 0.00607 | 2.5081 | 1.9930 |
| 0.05/1 = 0.0500 | 0.01642 | 2.1341 | 1.6943 |

Dark (t = 0.6667):

| Holm level α | α1 | b1 | c2 |
|---|---|---|---|
| 0.05/6 = 0.00833 | 0.00123 | 3.0275 | 2.4118 |
| 0.05/5 = 0.0100 | 0.00161 | 2.9466 | 2.3460 |
| 0.05/4 = 0.0125 | 0.00222 | 2.8450 | 2.2637 |
| 0.05/3 = 0.0167 | 0.00337 | 2.7097 | 2.1542 |
| 0.05/2 = 0.0250 | 0.00605 | 2.5093 | 1.9929 |
| 0.05/1 = 0.0500 | 0.01637 | 2.1351 | 1.6942 |

Decision rules, exactly:

1. After stage 1 is complete (every confirmatory arm, every stage-1 seed, both arenas), compute p1 for H1–H6 on the primary.
2. Promising zone: a primary contrast is promising if Z1 is below its arena's stage-1 bound at the first Holm level 0.05/6 (Classic 3.0262, dark 3.0275) and p1 < 0.5 (its estimate favors `rgl_v2`). An effect-size zone is not used; the p-value zone is the whole rule.
3. If at least one primary contrast is promising, run the single stage-2 batch above. Otherwise stop: no stage 2.
4. For each hypothesis compute the overall p-value: the smallest α at which the two-stage test rejects (stage 1: Z1 ≥ b1(α); stage 2, if run: Z1 > 0 and w1·Z1 + w2·Z2 ≥ c2(α)). Without a stage 2 only the stage-1 bound can reject.
5. Apply Holm (section 4.3) to the six overall p-values of family 1. The co-primary family uses the same stage-2 data if stage 2 ran, with the same rules; it never triggers stage 2 by itself.
6. The stage-2 decision is taken only by `src/analyze_v2p1.py` from stage-1 rows, recorded in `logs/STAGE2_DECISION.md` with the six p1 values before any stage-2 seed is stepped. No other look at outcomes occurs between stages. Descriptive arms do not enter stage 2.

Run time for stage 2: Classic 5 arms × 208 = 1,040 episodes, dark 3 × 600 = 1,800; at the measured per-episode cost (section 6) about 0.5 h + 0.8 h ≈ 1.4 h on 6 workers (worst case if every episode reached its horizon: Classic 1,040 × 104 s / 6 ≈ 5.0 h, dark 1,800 × 37.6 s / 6 ≈ 3.1 h).

## 6. Time and drop rule

Measured (logs/SPEED_TEST.md, 1b Phase A, pinned workers): step-loop rate per worker Classic `rgl_v2` 125.9 and `planner_ei` 105.0 steps/s, dark 104.3 and 117.8 steps/s; per-episode fresh-process setup 8.72 s; 6 workers (one worker measured 1.78 cores, below the 2-core cap rule). Measured mean episode length (steps survived, uncensored rows): Classic 130–237, dark 130–142; max seen 541.

Pre-freeze re-run on the final code (logs/rerun/SPEED_TEST.md, 2026-10-10 08:28–08:37 CT, seeds 60230–60239, every arm both worlds, 200 steps): step-loop rate per pinned worker Classic `rgl_v2` 124.1, `planner_ei` 103.3 steps/s; dark `rgl_v2` 91.7, `planner_ei` 97.8 steps/s; setup 7.59 s per episode; max 1.84 cores per worker; 6 workers. Mean episode length from the scratch rehearsal on the same code: Classic up to 275 steps (`plain_flee_eat`), dark up to 115 (`rgl_v2`).

Planning projection (slower arm rate, longest arm mean): Classic 275 / 103.3 + 7.59 = 10.3 s per episode; dark 115 / 91.7 + 7.59 = 8.8 s.

- Classic, 17 arms × 417 = 7,089 episodes: 7,089 × 10.3 / 6 ≈ 3.4 h.
- Dark, 11 arms × 1,200 = 13,200 episodes: 13,200 × 8.8 / 6 ≈ 5.4 h.
- Stage 2 if it runs: Classic 1,040 × 10.3 / 6 ≈ 0.5 h, dark 1,800 × 8.8 / 6 ≈ 0.7 h.
- Expected total ≈ 8.8 h for stage 1, ≈ 10 h with stage 2. The two arenas run in one queue on the same 6 workers, so the wall clock is the sum.

Drop-rule projection (mean episode length × 2, as the rule below states): Classic 550 / 103.3 + 7.59 = 12.9 s → stage 1 4.2 h, + stage 2 0.6 h; dark 230 / 91.7 + 7.59 = 10.1 s → stage 1 6.2 h, + stage 2 0.8 h. Both arenas are under the 24 h cap: no arm is dropped. For the record only (not the rule): if every episode ran to its horizon, Classic 17 arms would be 34.3 h and dark 11 arms at n = 1,200 about 24.6 h; the observed maximum episode length so far is 589 steps.

Drop rule, pre-stated and applied before any confirmatory seed: rerun the speed smoke on the new code (section 10). If a projection at the smoked rate, smoked mean episode length × 2, and 6 workers exceeds 24 h for an arena, drop descriptive arms in this order until it fits, and write the drop into this file before the freeze: (1) the six one-route drops (`drop_forage`, `drop_flee`, `drop_fight`, `drop_freeze`, `drop_rest`, `drop_explore`), (2) `shuffled_map`, (3) `rgl_v2delta` if it is action-identical to `v1-port` on the fixture, (4) `abl_gain_only`, (5) `abl_no_dwell`. Never dropped: `rgl_v2`, `planner_ei`, `plain_flee_eat`, `abl_no_urgency` (Classic), `abl_no_freeze` (dark), `v1-port` when H3 is in the family. n is not cut. If the mandatory arms alone exceed 24 h, the arena is BLOCKED. If an arm in the running batch reaches its horizon often, the run is not stopped to save time; the 24 h cap is a planning rule only.

## 7. Seeds

| role | seeds | notes |
|---|---|---|
| Determinism | 60200–60209 | Stepped 2026-10-09 (old code). Not confirmatory. |
| Smoke and speed | 60210–60219 | Stepped 2026-10-09 (old code). Speed only. |
| Pilot | 60300–60399 | Stepped 2026-10-09. Variance input only. |
| Scratch | 69000–69099 | Throwaway, never analysed. |
| Classic stage 1 | 61000–61416 | Never stepped. |
| Dark stage 1 | 62000–63199 | n = 1,200. Never stepped. |
| Classic stage 2 | 61500–61707 | Only if section 5 rule fires. Never stepped. |
| Dark stage 2 | 63200–63799 | n = 600, only if section 5 rule fires. Never stepped. (62500–62707 withdrawn.) |
| Generators | 64000–64099 | Section 4.2. |

Burned in GO-RGL-V2-PROOF-1, never reused: 60000–60029. Retired, never stepped: 60100–60199. Re-running determinism and smoke on the new code (section 10) uses fresh pre-listed seeds 60220–60239 (determinism 60220–60229, smoke 60230–60239), checked 2026-10-10 against the same files (no hit).

## 8. Pre-stated conclusion sentences

Notation: "survives Holm" = rejected in family 1 after the two-stage rule; "interval" = the 95% paired bootstrap interval of the mean difference in steps survived (pooled over the stages that ran); "minimum effect" = 15% of the comparator's observed mean steps survived (section 4.5). The manipulation checks are those of GO section 9. A manipulation miss selects the refusal sentence; it never changes a Holm label. No sentence may claim inner experience in a model. The matched sentence is pasted, not softened.

For every H the six outcomes are:

- (A) Survives Holm, manipulation passed, point estimate ≥ the minimum effect.
- (B) Survives Holm, manipulation passed, point estimate below the minimum effect.
- (C) Survives Holm, manipulation missed.
- (D) Does not survive Holm, point estimate > 0.
- (E) Point estimate ≤ 0 and the interval includes 0.
- (F) Interval wholly below 0 (inverse result).

H1 (Classic, vs `planner_ei`, the honest test):
- A: "On Craftax-Classic, route-family grouping added survival time over the equally informed planner: `rgl_v2` survived longer by at least 15% of the baseline, and the difference survives Holm."
- B: "`rgl_v2` survived longer than the equally informed planner and the difference survives Holm, but it is smaller than the pre-stated 15% minimum effect."
- C: "The difference survives Holm, but the feature-record or route-share check failed, so it is not read as evidence that grouping did the work."
- D: "Grouping is not shown to lengthen survival over the equally informed planner on Classic at this n." Add the equivalence sentence if TOST passed: "The two are equivalent within ±0.15 standardized units."
- E: as D, plus: "The point estimate does not favor `rgl_v2`."
- F: "Inverse result: the equally informed planner survived longer than `rgl_v2` on Classic; route grouping cost survival time."

H2 (Classic, vs `plain_flee_eat`, flee-or-eat):
- A: "`rgl_v2` survived longer than the ported flee-or-eat rule on Classic by at least 15% of the baseline, with the flee radius fixed at the chase radius and not retuned."
- B: "`rgl_v2` survived longer than flee-or-eat and the difference survives Holm, but by less than the pre-stated 15%."
- C: "The difference survives Holm, but the flee-branch check failed, so it is not read as evidence against a working plain rule."
- D: "`rgl_v2` is not shown to outlive the flee-or-eat rule on Classic at this n."
- E: as D, plus: "The point estimate does not favor `rgl_v2`."
- F (v2 loses to flee-or-eat): "Inverse result: the plain flee-or-eat rule survived longer than `rgl_v2` on Classic. v2 lost to the simple rule, as v1 did in P30 and P31. This is a failed prediction and is reported as the headline if it occurs."

H3 (Classic, vs `v1-port`):
- A: "`rgl_v2` survived longer than the frozen v1 port on Classic by at least 15% of the baseline. This is a v2-versus-port result; it does not revise P30 or P31."
- B: "`rgl_v2` survived longer than the v1 port and the difference survives Holm, but by less than the pre-stated 15%."
- C: "The difference survives Holm, but the port check failed (constants, ambiguity held at 0, adapter hash), so it is not read as evidence against frozen v1."
- D: "A survival gain over the v1 port is not shown on Classic at this n."
- E: as D, plus: "The point estimate does not favor `rgl_v2`."
- F: "Inverse result: the frozen v1 port survived longer than `rgl_v2` on Classic."
- Port not run: "H3 was not tested; port-rule item N failed. No v1 score was invented."

H4 (Classic, vs `abl_no_urgency`):
- A: "Turning off the non-health drains shortened survival on Classic by at least 15% of the baseline: the body budget earned its keep on survival time."
- B: "Turning off the drains shortened survival and the difference survives Holm, but by less than the pre-stated 15%."
- C: "The difference survives Holm, but the ablation check failed (the drain term was still present), so it is not read as evidence for principle 2."
- D: "A survival cost of removing urgency is not shown on Classic at this n."
- E: as D, plus: "The point estimate does not favor `rgl_v2`; the body budget did not earn its keep on this primary."
- F: "Inverse result: the router without urgency survived longer than `rgl_v2` on Classic."

H5 (dark floor, vs `planner_ei`):
- A: "On the dark floor, route-family grouping added survival time over the equally informed planner by at least 15% of the baseline."
- B: "`rgl_v2` survived longer than the planner on the dark floor and the difference survives Holm, but by less than the pre-stated 15%."
- C: "The difference survives Holm, but the dark ambiguity check or the feature-record check failed, so it is not read as evidence that grouping did the work in the dark."
- D: "Grouping is not shown to lengthen survival on the dark floor at this n." Add the equivalence sentence if TOST passed.
- E: as D, plus: "The point estimate does not favor `rgl_v2`."
- F: "Inverse result: the equally informed planner survived longer than `rgl_v2` on the dark floor."

H6 (dark floor, vs `abl_no_freeze`, the freeze test):
- A: "On the dark floor, where the world hides threats by light, removing freeze-from-uncertainty shortened survival by at least 15% of the baseline."
- B: "Removing freeze-from-uncertainty shortened survival and the difference survives Holm, but by less than the pre-stated 15%."
- C: "The difference survives Holm, but the freeze or ambiguity check failed, so it is not read as evidence that location uncertainty did the work."
- D: "A survival gain from freeze-from-uncertainty is not shown on the dark floor at this n."
- E: as D, plus: "The point estimate does not favor `rgl_v2`."
- F: "Inverse result: the router without freeze-from-uncertainty survived longer than `rgl_v2` on the dark floor."

Co-primary (family 2), every H: replace "survived longer" with "unlocked more stock achievements per episode", "survival time" with "achievements", and the minimum effect with 0.25 achievements. Inverse sentence: "Inverse result: [comparator] unlocked more stock achievements per episode than `rgl_v2` on [arena]." H2-F on the co-primary: "The plain flee-or-eat rule unlocked more achievements than `rgl_v2` on Classic; v2 lost to the simple rule on progress as well." If family 1 and family 2 disagree, both sentences are reported; neither is dropped.

Stage-2 sentence, always stated: "Stage 2 [was / was not] run; the decision was taken from the stage-1 p-values listed in logs/STAGE2_DECISION.md under the pre-stated rule."

## 9. Analysis code

`src/analyze_v2p1.py` (hashed at the freeze) computes the primary, co-primary and secondary, the permutation tests, bootstrap intervals, the two-stage bounds and overall p-values, Holm, and the exploratory TOST. It does not import the router. It exits nonzero and writes nothing on a duplicate `(arena, arm, seed)`, an unknown arm, a seed outside its role, a missing episode, a `rerun` other than 0 or 1, or a confirmatory or stage-2 seed while `V2P1_PHASE_B` is unset. `src/test_analyze_v2p1.py` recomputes the primary on the 200 pilot rows and checks the test machinery, bounds and type-I error; it prints `EXIT:0`. `src/run_phase_b.py` (hashed at the freeze) runs stage 1 (Classic 17 arms, dark 11 arms), calls `analyze_v2p1.py --stage1`, writes `logs/STAGE2_DECISION.md` before any stage-2 seed, runs stage 2 only if the rule fires, then `--final` into `results_b/ANALYSIS.json`. It checks `PREREG.md` against `PREREG_SHA.txt` and every source file against `logs/CODE_SHA.txt` before stepping, appends each episode as it finishes, resumes without repeating a done episode, and writes BLOCKED.md and stops on a repeated error or a conformance failure.

## 10. Before Phase B

1. Saved tests EXIT:0 on the final code; determinism 60220–60229 and smoke 60230–60239 passed (section 0); the drop rule of section 6 applied: no drop.
2. Matt approved the freeze, the publication and Phase B (2026-10-10 08:00 CT). This file's sha256 is in PREREG_SHA.txt; the code bundle is in logs/CODE_SHA.txt.
3. Published byte-identical to FloppyKit/rgl-protocol and checked by raw URL. Phase B runs only with `V2P1_PHASE_B=1` through `src/run_phase_b.py`.

## Changelog

- 2026-10-10 08:17:19 CDT: Matt raised dark n to 1,200 before freeze, based on scratch rehearsal variance (Matt approved 2026-10-10 08:00 CT). Dark stage 1 62000–63199, dark stage 2 n2 = 600 on 63200–63799 (proportional; the earlier dark stage-2 block 62500–62707 is withdrawn, never stepped). Dark weights, O'Brien-Fleming-type bounds, power and run time recomputed; no arm dropped. Analysis made per-arena in n; Phase B driver `src/run_phase_b.py` added before the freeze. Pre-freeze re-run on 60220–60239 on the final code.
- 2026-10-10 (Matt agreed 07:26 CT; additions approved 07:30 and 07:32 CT): primary changed from the Classic day-window fraction and the dark binary survival to steps survived (capped, stock terminal flag, stall = death at stall step), with stock achievements as co-primary, achievements per 100 steps alive as a reported secondary, and team survival deferred to ViZDoom. Reason: the pilot showed a floor effect: both baselines were 0/100 alive at 10,000 and every pilot episode ended between step 34 and step 541, so the window fraction was near 0 for every arm and could not separate them. This matches Matt's original intent that survival time is primary and progress is secondary. The ceiling switch is removed. H1–H6 keep their contrasts and become one-sided paired permutation tests in two Holm families. The ±0.05 equivalence margin is replaced by an exploratory d_z ±0.15 TOST. Minimum effect 15% longer mean survival; n = 417 kept. `shelter_night` gains a flee branch; the stall rule is made concrete (K = 300). A pre-stated two-stage sample-size extension (one fixed stage-2 batch of 208 seeds per confirmatory arm, inverse-normal combination, O'Brien-Fleming-type Lan-DeMets spending) was added at Matt's request before the freeze. All of this is made BEFORE any confirmatory seed was stepped and BEFORE this prereg was frozen.

clinical_claim: false · proof/micro-env/model
