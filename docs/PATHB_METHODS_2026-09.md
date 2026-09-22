# Path B methods — residual routing under opacity (through Proof-22)

**Status:** public methods narrative · tracks [PATHB_SCOREBOARD.md](PATHB_SCOREBOARD.md) through Proof-22 · 2026-09-21 America/Chicago  
**clinical_claim: false** · not PHI · not a medical device · not therapy · not DSM software  
Not evidence that a machine has feelings.

This note says what the sealed Path B series is for, which instruments it actually ran, and which results are allowed to stay ugly. Headlines and tables below are copied from the public timestamp docs and the scoreboard. Each proof doc carries its own SHA256 anchors. Full logs are not in this repository.

## 1. What Path B is, and what it is not

Path B treats RGL as a deciding agent under opaque next-state: local observations and teammate actions change outcomes the agent does not fully see. The object under test is an **external residual-updated salience / routing map**. It ranks or gates actions. It does not fine-tune a network.

```text
sense (local fog or partial obs) → residual signal → RGL map (update + read) → gate / route → act
                                         ↑________ sleep / collapse _________|
```

Shared MiniHack proofs (1–3) exercise that same map shape on a different instrument. They are not Path B. Path B starts at Proof-4, when the map is the policy under fog rather than a gate on a room task.

| Claim | Status |
|-------|--------|
| External residual salience / routing map | What the harness implements |
| PEFT / LoRA, or any rewrite of a frozen weight stack | Not this |
| "AI has feelings," consciousness, or a clinical emotion model | Not this (`clinical_claim: false`) |
| SOTA reinforcement learning, full SMAC, StarCraft II, or Minecraft / Mojang | Not this |
| Proof that residual maps beat every baseline in every environment | Not this |

Protocol language elsewhere in this repo (report-stream residuals, soft escalate, hard safety gate) is a different face of the same name. Path B does not inherit clinical meaning from that face. Cool residual is not a comfort score and not a win. See the battle law in §4.

## 2. Name stack and citations

RGL is an overloaded public name. [NAMES.md](NAMES.md) locks three faces of one program:

| Expansion | Face |
|-----------|------|
| Resonance Guided Learning | Process / control plane: a residual signal steers what gets attention and action |
| Residual Geometry Loosening | Geometry: coefficients or gates loosen or retighten under leftovers and sleep, not always-on weight mutation |
| Robert Galatzer-Levy | Intellectual rhyme: nonlinear, discontinuous change. Residual is process energy, not a comfort score |

Cite the third face as:

> Galatzer-Levy, R. M. (2017). *Nonlinear psychoanalysis: Notes from forty years of chaos and complexity theory*. Routledge. https://doi.org/10.4324/9781315266473

That citation is a rhyme, not a claim that Path B implements Galatzer-Levy's model, a psychoanalysis, or a clinical method.

Affect labels in this series follow [AFFECT_ROUTE_MAP.md](AFFECT_ROUTE_MAP.md). The lineage cite is Lisa Feldman Barrett's program as discussed on Huberman Lab (*How to Understand Emotions*) and in *How Emotions Are Made*: emotions as constructed multimodal summaries involving body, prediction, and concepts, including movement, sensation, prediction, and learning.

The six cluster names and the impulse glosses are PsychArts bridging language for residual routing. They are not a Barrett taxonomy, not a one-to-one implementation of her model, and not a clinical protocol. Machine routes are allowed to rhyme or invert the human gloss. An inverse is a result.

## 3. Ladder of sealed instruments

The ladder is intentional and narrow. External validity is not claimed at any rung. Each GO is one sealed comparison. Discovery is append-only: a later proof does not rewrite an earlier headline.

| Rung | Proofs | Instrument | What changed |
|------|--------|------------|--------------|
| Shared mechanisms (not Path B) | 1–3 | MiniHack MiniHack-Room-5x5-v0, NLE WAIT | Residual gate, sleep/collapse, interrupt hold vs STOP |
| Opaque battle | 4–8 | Sealed SMAC-lite (no SC2) | Trash fog → measured thrash → boss phases → harder boss + scripted kite → tank/striker |
| Craft under fog | 9–15 | Minecraft-shaped micro-env (not Minecraft) | Gather/craft/mob → harder layout → learn-on map → interrupt → outcome gate, sleep, slow step size |
| Affect trilogy on prior arenas | 16–18 | MC-shaped values conflict; SMAC-lite laugh; SMAC-lite love | One cluster per GO, against its own baselines |
| Beat a frozen recipe | 19 | Proof-10 arena, byte-identical | Intra-episode option/habit, not a learning-rate retune |
| Unified affect sweep | 20 | Custom UnifiedRouteArena | Seven arms, one design, one overweight |
| Community port | 21–22 | Farama MPE2 `simple_world_comm_v3` (`mpe2==1.1.1`) | Same sweep shape on a community env; Proof-22 changes only the laugh mapper |

**MiniHack, in one paragraph.** Proof-1 was inverse: success tied at 1.0, but the gated policy took 7.0 mean steps against blind 4.0 (hold_rate≈0.43). Cool residual was not a win. Proof-2 was same: sleep/collapse cut thrash 25.4→3.5 and end-of-episode map mass 5.0→2.5, the goal residual survived, and success moved 0.92→1.0. Proof-3 was same on interrupts: the gate held chatter, honored STOP, and recorded false_merges=0; blind always-abort recorded high false merges and success 0.0.

**SMAC-lite through asymmetric roles.** Proof-4 put the map in the engage loop and it failed (§4). Proof-5 removed engage-HOLD. Proofs 6–8 left the trash-mob ceiling, where thrash could not pull away from always-commit, and required a boss, then a scripted kite, then asymmetric roles, before residual-guided measured thrash beat both blind and a strong script. Proof-6 waste was about half of blind (35.64 vs 74.62) with divergence on 50/50 seeds. That waste gap is not the Proof-5 result. Proof-5 waste matched blind. Public wording for that tie is only: **Proof-5 thrash≈blind ceiling**.

**Minecraft-shaped learn arms.** Proof-9's thrash-versus-scripted gap was small (0.85 vs 0.80). Proof-10 widened it to +0.225 (0.725 vs 0.50) by a tighter period, farther materials, and harsher rage/wrong-craft penalties. Proof-11 turned on a tiny tabular map update. The map moved (fight bias up, kite down) and late-window success got worse. Proofs 13–15 did not chase a new arena. They changed only the update rule: outcome-gated writes, sleep-gated writes, or a 0.25× step size. Each restored the frozen ceiling. Proof-12 added mid-plan CHATTER versus STOP on the Proof-10 family: thrash and scripted false_merges=0, merge-blind false_merges=20, success 0.35 / 0.30 / 0.00.

**Affect trilogy, then one narrow beat.** Proofs 16–18 are the first sealed cluster routes (§5). Proof-19 is not an affect sweep. Both arms started from the fixed Proof-10 ranker. Beat added an intra-episode dual-timescale SAFE_PRECRAFT option: a fast threat-residual average could replace a grid-boundary bump with an in-bounds sweep while the agent was unarmed and still gathering. No cross-episode map write. SAFE_PRECRAFT fired 12 times. Success 0.750 / 0.725 / 0.500 / 0.075 (beat / frozen thrash / scripted / blind). Waste 0.975 vs 1.250. The arms differed on 6/40 paired seeds: one success win, lower waste on 5/40, higher waste on 0/40. That is a one-seed success edge on one layout. Proof-20 was verified and published out of numerical order relative to Proof-19. Both are public. Proofs 21–22 followed after proxy inspection.

## 4. Battle laws

These are harness laws, read off the early SMAC-lite seals. They are not personality claims.

**Cool residual is not a win.** Low residual can be calm or a stuck false peace. Proof-1 already showed a cooler gate that was slower at the same success. Proof-4 showed a cooler gate that died.

**Cool→HOLD while engaged is death.** In Proof-4 the blind always-commit policy cleared the enemy with the ally alive (success 1.0). The residual gate held (hold_rate≈0.21), interrupted finishing commits, left the enemy alive, and lost the ally (success 0.0). Verdict: **inverse**. Path A's "cool down after a match" rule is an operator-nag policy. It is not a Path B engage policy.

**Measured thrash.** Proof-5 forbids HOLD after a hit while the enemy is alive. The map may rank which commit to make. It may not idle-latch. On that trash-mob layout, measured thrash recovered success from 0.0 to 1.0 and landed on the **Proof-5 thrash≈blind ceiling** (engage-holds 0; waste identical to blind). From Proof-6 onward, where the public docs say thrash beats a baseline, the scoreboard language is **thrash > …** and the residual-helps hypothesis is **same**. Where thrash loses, or where learning hurts a frozen recipe, the word is **inverse**, and it is publishable.

**Route credit can dig its own hole.** Proof-11's greedy cross-episode update overweight a fight-like commit and slightly lost to the frozen thrash it started from: frozen 0.725 > learn 0.70 (early window both 0.80; late 0.65 vs 0.60). Residual-helps stayed **same** against scripted (0.50) and blind (0.075). The inverse is the learn-versus-frozen question. Outcome gating (35/40 updates, 5 ambiguous fails skipped), sleep (fired 12/40), and the slower step size (40/40 updates, slow vs frozen differ on 0/40) each print the same restoration: 0.725 = 0.725 > 0.70 > 0.075. They stop the dig. They do not beat the frozen recipe. Proof-19 is the first public exceedance, and it is the narrow paired-seed edge above, from a different mechanism.

## 5. Affect-route map

Locked glosses (PsychArts, not Barrett):

| Cluster | Impulse gloss | What the series actually ran |
|---------|---------------|------------------------------|
| Fight | Engage / commit pressure | Thrash, attack, measured commit. Easy to overweight (Proof-11) |
| Flight | Withdraw / distance / kite | Kite, scout away |
| Freeze | Stop / HOLD / cool-latch | HOLD. Cool→HOLD in engage = death (Proof-4) |
| Capitulate | Go along even when it does not align with morals or values | Proof-16 values-conflict; later sweep arms |
| Laugh | Thrash without malice (playful / non-hostile pressure) | Proof-17 foe-only vs ally-splash; sweep arms; Proof-22 mapper repair |
| Love / compassion / faith | Proceed as you typically would when strange variables are not firing — effortless autopilot | Proof-18 vs panic; sweep arms |

The route-map file still says, in its "machine rhyme so far" column, that capitulate, laugh, and love were mostly unsealed at lock time, and that Proofs 4–15 mostly probed fight, flight, and freeze-ish recipes. That sentence is the pre-trilogy status. The scoreboard, updated the same day through Proof-22, is the index: Proofs 16–18 sealed the three open clusters on their own arenas; Proofs 20–22 put all six, plus a balanced arm, on one sweep. Read the glosses from the map. Read what has been run from the scoreboard.

**Cluster seals before the unified sweep:**

- **Capitulate (Proof-16), inverse on success.** Forbidden chest; opening it is a values break. Blind 0.90 > scripted refuse 0.75 > residual route 0.70 (n=40). Values breaks ran the other way: scripted 0.00 < residual 0.40 < blind 0.75. The greedy capitulate made more progress and broke the constraint. The residual route beat blind only on the values axis, and it still carried fight-thrash. Engage-holds were 0.
- **Laugh (Proof-17), same.** Foe-only pressure versus malice (foe pressure plus ally splash). Scripted laugh 1.000 = laugh residual 1.000 > blind 0.825 > malice 0.475 (n=40). False damage 0 / 0.51 / 2.23 / 4.86 in that order. Laugh beat malice. Residual beat blind on success and false damage on 40/40 seeds. Engage-holds were 0.
- **Love / autopilot (Proof-18), same.** Low-salience care route versus panic thrash. Scripted autopilot 1.000 = love residual 1.000 > blind 0.825 > panic 0.000 (n=40). False damage 0 / 0.34 / 2.23 / 5.63. Waste 1.00 / 2.00 / 9.85 / 14.48. Residual beat blind on success, false damage, and waste on 40/40. Engage-holds were 0.

Proof-17 and Proof-18 show a residual route matching a good script and beating blind and a harmful thrash. They do not show that the label "love" or "laugh" is an emotion in the controller.

## 6. Key results

### Proof-20 — custom hierarchy, one design

Every arm used the same UnifiedRouteArena, observation, base policy, six-action set, transition law, and paired seeds 20000–20079 (80 seeds × 7 arms = 560 episodes). The event tape was generated before actions and did not depend on the arm. The only arm-level change was a +2.15 additive overweight on one named route. Balanced used route none and overweight 0.

**Primary success:**

love/autopilot 1.000 = balanced 1.000 > laugh 0.975 > freeze 0.050 > fight 0.000 = flight 0.000 = capitulate 0.000.

Directions: success up; steps, effort, collateral, false damage, blowback, waste, values breaks, and engage-holds down.

| Arm | Success | Steps | Effort | Collateral | False damage | Blowback | Waste | Values break | Engage holds |
|-----|---------|-------|--------|------------|--------------|----------|-------|--------------|--------------|
| Fight | 0.000 | 13.0375 | 31.0223 | 10.1732 | 5.8128 | 6.9922 | 5.4519 | 0.0000 | 0.0000 |
| Flight | 0.000 | 36.0000 | 36.4495 | 0.0000 | 0.0000 | 0.0000 | 14.5888 | 0.0000 | 0.0000 |
| Freeze | 0.050 | 35.9500 | 25.7675 | 0.4660 | 0.0643 | 0.5203 | 13.1661 | 0.0000 | 4.2125 |
| Capitulate | 0.000 | 35.8375 | 24.7939 | 0.1051 | 0.0144 | 1.2332 | 12.4800 | 0.1125 | 0.0000 |
| Laugh | 0.975 | 32.6375 | 26.0760 | 0.0586 | 0.2687 | 0.9640 | 3.1381 | 0.0000 | 0.0000 |
| Love/autopilot | 1.000 | 22.7875 | 24.6105 | 0.0000 | 0.0000 | 0.2093 | 0.0000 | 0.0000 | 0.0000 |
| Balanced | 1.000 | 21.7125 | 25.3360 | 0.4011 | 0.0608 | 0.6303 | 0.0081 | 0.0000 | 0.0000 |

The success-qualified frontier (mean success ≥ 0.90) is love/autopilot and balanced only. Love was cleaner on the cost and harm axes. Balanced was faster (21.7125 vs 22.7875 mean steps). Laugh kept almost all of the success and cut collateral relative to balanced, at a cost of 10.925 more mean steps and higher false damage, blowback, and waste.

A strict nine-axis non-domination frontier also keeps fight and flight. That is not a ranking. Fight survives because failed episodes end early (13.0375 mean steps, success 0). Flight survives because measured collateral, false damage, and blowback are zero, despite success 0, 36.0000 mean steps, and high waste. Love dominates freeze, capitulate, and laugh on the nine means. This ordering is one synthetic model with fixed equations. It is not a universal route order.

### Proof-21 — community port, mixed

Same seven-arm overweight (+2.15; balanced = 0), now on Farama MPE2 `simple_world_comm_v3`, controller `agent_0`, paired seeds 21000–21079, n=80 per arm. Adversaries are fixed scripts. Good agents have no leader-comm channel, so the capitulate proxy follows the leader's position. Success is a constructed food-contact + team-protection proxy, not native reward, and not a human affect label. The proxy definition was locked before the run (SHA256 `69789ab189c000322b5dd1375ff6ac86dc0aa1059e3ee46a4d9259c96a046f17`).

**Primary success:**

love/autopilot 0.2875 > balanced 0.1500 > fight 0.0625 > capitulate 0.0375 > flight 0.0250 > laugh 0.0125 > freeze 0.0000.

| Arm | Success | Time to goal | Effort | Collateral | False damage | Blowback | Waste | Values break | Engage holds |
|-----|---------|--------------|--------|------------|--------------|----------|-------|--------------|--------------|
| Fight | 0.0625 | 49.1375 | 50.0000 | 0.7875 | 0.3000 | 7.9875 | 2.7000 | 13.0500 | 0.0000 |
| Flight | 0.0250 | 49.8000 | 50.0000 | 0.6750 | 0.1250 | 0.5375 | 0.8500 | 1.2625 | 0.0000 |
| Freeze | 0.0000 | 51.0000 | 0.0000 | 0.6000 | 0.0750 | 11.4750 | 49.5500 | 0.0000 | 34.6250 |
| Capitulate | 0.0375 | 49.9375 | 38.0750 | 1.1250 | 0.3250 | 6.4000 | 12.3625 | 14.9375 | 5.1500 |
| Laugh | 0.0125 | 50.6500 | 50.0000 | 0.6125 | 0.1000 | 10.5500 | 36.1875 | 8.0625 | 0.0000 |
| Love/autopilot | 0.2875 | 44.7375 | 50.0000 | 1.9375 | 0.5500 | 6.6875 | 0.7375 | 0.8500 | 0.0000 |
| Balanced | 0.1500 | 47.3500 | 44.8250 | 0.9750 | 0.3625 | 5.9750 | 8.0250 | 5.4000 | 0.4375 |

**Official verdict: mixed / partially confirmatory.** What confirms Proof-20 is the top of the success order: love ahead of balanced, freeze at the bottom with extreme engage-holds (34.6250) and waste (49.5500), capitulate with the highest values breaks (14.9375), fight blowback-heavy (7.9875), flight with the cleanest blowback (0.5375) and almost no completions. Love is also the fastest mean goal latency (44.7375) and the lowest waste (0.7375).

What does **not** confirm Proof-20:

- Absolute success is modest. Nobody is near the custom arena's ceiling of 1.0.
- The success-qualified frontier at ≥ 0.90 is empty. Love's 0.2875 does not qualify.
- Laugh is **inverse** relative to balanced: success 0.0125 vs 0.1500, with waste 36.1875 and blowback 10.5500. On this port, laugh is worse than balanced, not a near-tie at 0.975.
- Love is not the clean arm. It leads success, time, and waste, and it also posts the highest collateral (1.9375) and the highest false damage (0.5500).

Nothing here transfers, on the proof's own statement, to other MPE scenarios, continuous actions, learned adversaries, or human affect.

### Proof-22 — laugh mapper repair, still mixed

Proof-21's laugh inverse was tested as a possible mapper artifact. Proof-22 keeps the Proof-21 scenario, seeds 21000–21079, food+protection success proxy, and pins. The only intentional change is the laugh option mapper: from a cycle-alternating perpendicular feint to fixed-chirality non-hostile pressure. New proxy-definition lock: SHA256 `10addd6a2a4419b9a65f4bc176f6215adc47e7b14d53c5b052178f6011198d3c`. The proof doc states that non-laugh arms matched Proof-21 means.

**Headline deltas for laugh:**

| | Proof-21 laugh | Proof-22 laugh |
|--|----------------|----------------|
| Success | 0.0125 | 0.1500 (= balanced) |
| Waste | 36.1875 | 2.0625 |
| Blowback | 10.55 | 4.00 |

Love still leads at 0.2875. The ≥ 0.90 frontier is still empty. Repaired laugh is no longer inverse against balanced on success. It also does not beat balanced or love. That is the scoreboard's repair verdict: **mapper-conditioned inverse, not a new winner**.

The repair is not uniformly cleaner. The published Proof-22 laugh row (rounded as printed in that doc) is success 0.1500, time to goal 47.65, effort 50.00, collateral 1.44, false damage 0.29, blowback 4.00, waste 2.06, values break 7.28, engage-holds 0.00. Against the Proof-21 laugh row, collateral (0.6125→1.44) and false damage (0.1000→0.29) went up while waste and blowback collapsed. Proof-22's own table rounds the non-laugh arms; use Proof-21's four-decimal table for those cells. The held-constant check is the proof doc's statement, not a second independent arithmetic claim in this note.

Proof-22 does not move the ≥ 0.90 rule, the success proxy, or the Proof-21 headline. It is a new GO. Proof-21 stays as published, laugh inverse included.

### How to read the three sweeps together

On the custom arena, a +2.15 route overweight was enough to separate a full-success pair (love, balanced) from a near-success laugh and from three zero-success biases. On one community scenario, under one predeclared food+protection proxy, the same overweight separates love from balanced by 0.2875 vs 0.1500, and separates nothing from a 0.90 bar. The custom hierarchy is real inside UnifiedRouteArena. It is not a community-env result. The community result is real inside this MPE2 scenario and this proxy. It is not a failed replication of the 1.0 ceiling, because the ceiling was never the predeclared community claim. The predeclared community claim was the sweep, the proxy, and the frontier rule. Under that rule the frontier is empty, before and after the laugh repair.

## 7. Validity and reproducibility

[VALIDITY_REPRO.md](VALIDITY_REPRO.md) is the stance. Short form:

| Kind | Path B practice |
|------|-----------------|
| Construct | Named policies and named route arms; battle law explicit; metrics include success plus waste, holds, damage, values breaks. A proxy that does not match the words in the arm name is a construct problem, which is why Proof-22 exists and why its mixed result stays |
| Internal | Fixed seeds, CSV, SHA256, VERIFY gates. Inverse and thrash-beats-baseline are both publishable |
| External | Not claimed. Trash-mob, boss, craft, custom sweep, and MPE2 are different instruments |

Three grades of check, in the order the validity note gives them:

1. **Bit-seal** (what a public timestamp is). Content SHA256 of episodes, summary, and WRITEUP lives on the nest. This repo publishes the redacted headline and the anchors. Recomputing the hashes on the nest artifacts should match.
2. **Independent re-run.** Another machine, same seeds and flags from the proof's VERIFY.md or packet README. Pass means the gates, not a byte-identical CSV, unless code and seeds match exactly. Stochastic ties only where a proof already documents them.
3. **Sensitivity pack** (later, not these headlines). Vary thresholds, phase lengths, fog radius. Publish redacted deltas. Do not edit the sealed headline.

**Append-only.** Sealed writeups stay. A language-lock fix that changes a WRITEUP hash is allowed only with a new VERIFY pass and an updated public anchor (as with Proof-7). Proof-20's out-of-order publication did not replace Proof-19. Proof-22 did not replace Proof-21. Silent score edits are out.

Custom micro-envs (SMAC-lite, Minecraft-shaped, UnifiedRouteArena) buy internal control and can inflate absolute success. The community port buys a third-party transition law and, here, much lower success. Both are allowed. Only the second supports a sentence about a community environment, and only for `simple_world_comm_v3` under the locked proxy.

## 8. Non-claims, and what would increase trust

This series does **not** show:

- a clinical effect, a therapy protocol, or a diagnostic category
- that any arm "has" fight, fear, laughter, or love
- that Barrett's theory predicts these tables, or that Galatzer-Levy's book is being tested as a clinical method
- that residual routing dominates blind or scripted policies in general (Proof-4, Proof-11, and Proof-16 are published counterexamples; Proof-5 is a tie at the ceiling)
- that Proof-20's order is the Proof-21 order (it is not: laugh inverts, the 0.90 frontier is empty, love leads a modest rate and leads collateral)
- that Proof-22 vindicates laugh as a superior route (it ties balanced on one proxy and still trails love)
- SOTA learning, full SMAC/SC2, or Minecraft

**Trust would go up by replication and new instruments, not by retuning the bar:**

- An independent re-run of Proofs 20–22 from the public seeds, flags, and proxy locks, with gates rather than a demand for byte-identical CSVs.
- The same seven-arm overweight, the same +2.15, and the same ≥ 0.90 success-qualified rule on additional MPE2 scenarios, reported even when the frontier is empty and even when laugh or love inverts.
- A sensitivity pack that varies the overweight and the proxy thresholds in a new GO, leaving 20–22 untouched.
- Keeping construct and headline in the same sentence: if success is food-contact plus team protection, say that every time the number appears.

**What would not increase trust:** moving the 0.90 cutoff after seeing 0.2875, swapping the success proxy until love looks like Proof-20, or deleting the Proof-21 laugh row because Proof-22 repaired the mapper.

## How to cite, and where the seals live

Cite this narrative as the methods overview, and cite the proof timestamp next to any number. Example:

> PsychArts RGL Path B methods (through Proof-22), 2026-09-21. Resonance Guided Learning protocol (public). `clinical_claim: false`. Numbers from `docs/PATHB_PROOF21_MPE2_UNIFIED_AFFECT_2026-09-21.md` and `docs/PATHB_PROOF22_MPE2_LAUGH_REPAIR_2026-09-21.md`, indexed by `docs/PATHB_SCOREBOARD.md`.

| Layer | What a reader can check |
|-------|-------------------------|
| Public buzz feed | This GitHub repo. Redacted headlines, method notes, scoreboard, SHA256 anchors, example-packet READMEs. Commits are the timestamp |
| Nest | Full episode logs, harness trees, VERIFY bundles. Not in the public tree. A bit-seal check recomputes the published SHA256 against those artifacts |
| Not either | A claim that the public table is the raw log, or that a nest log changes a headline without a new public GO |

Preferred entry points: [PATHB_SCOREBOARD.md](PATHB_SCOREBOARD.md), [AFFECT_ROUTE_MAP.md](AFFECT_ROUTE_MAP.md), [VALIDITY_REPRO.md](VALIDITY_REPRO.md), [NAMES.md](NAMES.md), [MINIHACK_PROOF_TRILOGY_2026-09-21.md](MINIHACK_PROOF_TRILOGY_2026-09-21.md).
