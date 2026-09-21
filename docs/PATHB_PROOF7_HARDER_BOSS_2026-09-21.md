# Path B Proof-7 — harder boss + scripted kite — 2026-09-21 (timestamped)

**clinical_claim: false** · CPU only · sealed 2026-09-21 America/Chicago · VERIFY PASS  
**Language:** proof / micro-env / model — not a clinical claim, not PHI.

Fork from Proof-6 (thrash beat blind on boss). Harder boss + strong scripted-kite baseline so residual thrash must beat more than dumb always-commit.

## Headline (read carefully)

**Thrash > scripted_kite > blind.** Success **0.725 / 0.425 / 0.05**; engage_holds **0**.  
Explicit: **thrash > blind**. Also **thrash > scripted_kite**.  
Verdict vs residual-helps / battle-law hypothesis: **same** (not a Proof-5-style tie to blind).

## Stack slot (one line)

RGL = residual+phase salience that ranks kite vs window-attack vs fog re-acquire — never cool→HOLD while boss alive.

## Scoreboard

| GO | Question | Result | Public headline |
|----|----------|--------|-----------------|
| PATHB-PROOF-7 | measured thrash vs blind vs scripted kite on harder boss | thrash beats both baselines; residual-helps **same** | success 0.725 > 0.425 > 0.05 |

Harder boss vs Proof-6: period 10 / rage 5 / vuln 5 / rage_damage 3.5. Instrument: sealed SMAC-lite (no SC2).

## Content anchors (SHA256)

| Artifact | SHA256 |
|----------|--------|
| episodes CSV | `2d0021d804242cbc057d8675747babf41b010dd4ffb20674dd694ace3a344ef0` |
| summary CSV | `4eb85c43b823c959fe748576fd3e029b419ac0cbce4db1f19d8b878cffbe4d68` |
| WRITEUP | `9502f46ef0d867753e05fd8c575c4ec2f878a36d56f7bdb625ea9becc2ae31a7` |

## What this proves / does not prove

**Proves (narrow):** on this harder boss, residual-guided measured thrash beats blind and a strong fixed kite script.

**Does not prove:** generalization beyond this harness, or role-asymmetric thrash (Proof-8).

## Nest vs public

| Public (this repo) | Nest (private) |
|--------------------|----------------|
| Redacted scores, method note, content SHA anchors | Full logs, harness trees, VERIFY bundles |

## Related

- Proof-6 boss: [PATHB_PROOF6_BOSS_2026-09-21.md](PATHB_PROOF6_BOSS_2026-09-21.md)
- Example packet: [../examples/pathb_proof7_2026-09-21/README.md](../examples/pathb_proof7_2026-09-21/README.md)
