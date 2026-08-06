# lean_sorry_triage

> **Experiment:** rank *public* open Lean `sorry`s by a cheap process **attention** score  
> so a human (or ATP queue) can ask *where to look next*.  
> **Not** a proof, **not** a difficulty ranking, **not** auto-PRs.

If you maintain [SorryDB](https://github.com/SorryDB/SorryDB), a blueprint project, or
[Formal Conjectures](https://github.com/google-deepmind/formal-conjectures): this is a
**“hey, what about this?”** note with data attached. Ignore freely.

---

## TL;DR

| | |
|--|--|
| **Input** | [SorryDB](https://github.com/SorryDB/sorrydb-data) `static_100_varied_recent_deduplicated_sorries.json` (+ a few FC Erdős *statement* files) |
| **Output** | Ranked list: `repo` · `path` · `line` · `goal` · `attention` |
| **Truth** | Still owned by the **Lean kernel** / `lake build` |
| **Scoring** | Offline heuristic only (`$0`). No multi-head LLM residual in this pack |
| **PRs** | We will **not** open automated PRs (SorryDB norm) |

**Start:** skim [§ Top 10](#top-10-by-attention) → open one upstream link → decide if triage like this helps your queue.

Paste-ready Zulip blurb: [`ZULIP.md`](ZULIP.md)

---

## Two columns (please keep separate)

```text
  lake build / kernel          attention score (this pack)
  ─────────────────            ───────────────────────────
  “Is the proof correct?”      “Where look next?”
```

Same split you already feel on a blueprint dep graph: a red node is *unfinished work*,
not “wrong math.” We only score unfinishedness features on public metadata + pretty-printed goals.

---

## Top 10 by attention

| # | att. | class | repo | location | in English |
|--:|-----:|-------|------|----------|------------|
| 1 | 0.5565 | `surface_gap` | [frenzymath/jixia](https://github.com/frenzymath/jixia/blob/e6d1448771f53b540a450fdf5180f1217efaaab8/Example.lean#L82) | `Example.lean:82` | prove that Option.none is not a 'some' value (basic Option fact). |
| 2 | 0.5565 | `surface_gap` | [lean-ja/lean-by-example](https://github.com/lean-ja/lean-by-example/blob/3ebe85bea550147ea661babd12b968bf8e97a7ed/LeanByExample/Tactic/Plausible.lean#L67) | `LeanByExample/Tactic/Plausible.lea` | in a teaching natural-number type, prove the stated equality (tutoria… |
| 3 | 0.552 | `rich_open` | [emilyriehl/infinity-cosmos](https://github.com/emilyriehl/infinity-cosmos/blob/bf1885e46ff0fde2a1cde218001d9b90307f4224/InfinityCosmos/ForMathlib/InfinityCosmos/Isofibrations.lean#L70) | `InfinityCosmos/ForMathlib/Infinity` | assume a suitable infinity-cosmos setting and two maps that are alrea… |
| 4 | 0.525 | `surface_gap` | [lean-ja/lean-by-example](https://github.com/lean-ja/lean-by-example/blob/3ebe85bea550147ea661babd12b968bf8e97a7ed/LeanByExample/Attribute/Aesop.lean#L88) | `LeanByExample/Attribute/Aesop.lean` | prove a teaching-list value is nonempty (example file obligation). |
| 5 | 0.4845 | `surface_gap` | [FormalizedFormalLogic/Foundation](https://github.com/FormalizedFormalLogic/Foundation/blob/2d0d958822ddfb22e58f2cb6266a52f3bb219fff/Foundation/ProvabilityLogic/Grz/Completeness.lean#L34) | `Foundation/ProvabilityLogic/Grz/Co` | finish an intermediate lemma inside a modal / provability-logic devel… |
| 6 | 0.4845 | `surface_gap` | [FormalizedFormalLogic/Foundation](https://github.com/FormalizedFormalLogic/Foundation/blob/2d0d958822ddfb22e58f2cb6266a52f3bb219fff/Foundation/ProvabilityLogic/Grz/Completeness.lean#L251) | `Foundation/ProvabilityLogic/Grz/Co` | finish an intermediate lemma inside a modal / provability-logic devel… |
| 7 | 0.4845 | `surface_gap` | [FormalizedFormalLogic/Foundation](https://github.com/FormalizedFormalLogic/Foundation/blob/a2cbf6a6c08a4e59a8ac27e0e85e5c562af7bb32/Foundation/ProvabilityLogic/S/Completeness.lean#L253) | `Foundation/ProvabilityLogic/S/Comp` | finish an intermediate lemma inside a modal / provability-logic devel… |
| 8 | 0.4845 | `surface_gap` | [FormalizedFormalLogic/Foundation](https://github.com/FormalizedFormalLogic/Foundation/blob/d773e9c193bd4782c94b32ea63ede4aae696573a/Foundation/ProvabilityLogic/S/Completeness.lean#L375) | `Foundation/ProvabilityLogic/S/Comp` | finish an intermediate lemma inside a modal / provability-logic devel… |
| 9 | 0.4584 | `surface_gap` | [leanprover-community/duper](https://github.com/leanprover-community/duper/blob/e28c4e11389116ccb6a48ff0fe9c3d1a9d7642e4/Duper/Tests/test_continuity.lean#L18) | `Duper/Tests/test_continuity.lean:1` | prove that the distance from a point to itself is zero (basic metric … |
| 10 | 0.4584 | `surface_gap` | [leanprover-community/batteries](https://github.com/leanprover-community/batteries/blob/e119df7e78d94b18b34067db93e8fc0d448d696f/BatteriesTest/lint_unreachableTactic.lean#L23) | `BatteriesTest/lint_unreachableTact` | prove 1 = 1 (trivial test/linter obligation, not research math). |

<details>
<summary><b>Same rows with pretty-printed Lean goals</b> (for people who live in the infoview)</summary>


### 1. `frenzymath/jixia` — `Example.lean`:82

In English: prove that Option.none is not a 'some' value (basic Option fact).

```lean
-- pretty-printed goal (from SorryDB / public file)
α : Type u ⊢ ¬none.IsSome
```


### 2. `lean-ja/lean-by-example` — `LeanByExample/Tactic/Plausible.lean`:67

In English: in a teaching natural-number type, prove the stated equality (tutorial obligation).

```lean
-- pretty-printed goal (from SorryDB / public file)
⊢ ∀ (a b : MyNat), a = b
```


### 3. `emilyriehl/infinity-cosmos` — `InfinityCosmos/ForMathlib/InfinityCosmos/Isofibrations.lean`:70

In English: assume a suitable infinity-cosmos setting and two maps that are already isofibrations; prove that the map obtained by taking their product is also an isofibration. (A 'stability under products' property for those maps.)

```lean
-- pretty-printed goal (from SorryDB / public file)
K : Type u inst✝¹ : Category.{v, u} K inst✝ : InfinityCosmos K X Y X' Y' : K f : X ↠ Y g : X' ↠ Y' ⊢ IsIsofibration (prod.map ↑f ↑g)
```


### 4. `lean-ja/lean-by-example` — `LeanByExample/Attribute/Aesop.lean`:88

In English: prove a teaching-list value is nonempty (example file obligation).

```lean
-- pretty-printed goal (from SorryDB / public file)
⊢ NonEmpty (MyList.cons 1 MyList.nil)
```


### 5. `FormalizedFormalLogic/Foundation` — `Foundation/ProvabilityLogic/Grz/Completeness.lean`:34

In English: finish an intermediate lemma inside a modal / provability-logic development (technical context above the goal; not a one-line slogan theorem).

```lean
-- pretty-printed goal (from SorryDB / public file)
case intro α : Type u_1 inst✝² : DecidableEq α R : α → α → Prop inst✝¹ : DecidableEq α inst✝ : IsTrans α R l : List α i j : Fin l.length h : Chain' R l eij : i ≠ j nRij : ¬R (l.get i) (l.get j) nRji :
```


</details>

---

## Worked example (bilingual)

**Repo:** [emilyriehl/infinity-cosmos](https://github.com/emilyriehl/infinity-cosmos)  
**File:** [`Isofibrations.lean:70`](https://github.com/emilyriehl/infinity-cosmos/blob/bf1885e46ff0fde2a1cde218001d9b90307f4224/InfinityCosmos/ForMathlib/InfinityCosmos/Isofibrations.lean#L70)  
**Attention:** `0.552` · class `rich_open`

**In English**  
Assume an ∞-cosmos and two maps that are already isofibrations; prove that their **product map** is still an isofibration (stability under products).

**Lean goal (pretty-printed)**

```text
K : Type u
inst✝¹ : Category.{v, u} K
inst✝ : InfinityCosmos K
X Y X' Y' : K
f : X ↠ Y
g : X' ↠ Y'
⊢ IsIsofibration (prod.map ↑f ↑g)
```

| Fragment | Reading |
|----------|---------|
| above `⊢` | context (*given*) |
| `⊢ …` | goal (*show*) |
| `IsIsofibration (prod.map ↑f ↑g)` | the property to prove of that map |

We claim **only** that this open `sorry` scored relatively high on a process-attention heuristic.

---

## Labels

| Label | Meaning here |
|-------|----------------|
| `sorry` | Open proof obligation (SorryDB) |
| `statement_only` | Formalised statement / conjecture file, no completed proof in this pack |
| `rich_open` | Open unit with richer goal/domain signal under the heuristic |
| `surface_gap` | Score driven more by thin/packaging features than deep novelty |
| `routine_open` | Ordinary open obligation |
| `low_signal` | Thin process signal (≠ mathematically unimportant) |
| `high_priority` / `mid_priority` / … | Triage buckets only |

---

## Layout

```text
examples/lean_sorry_triage/
  README.md          ← you are here
  ZULIP.md           ← short post you can paste
  data/
    top15.json       ← machine table (repo, path, line, goal, goal_en, attention)
    sample.jsonl     ← enriched packets
  notes/
    method.md        ← scoring honesty
    table.md         ← longer commentary

examples/lean_micro/           ← four tiny term-mode lemmas (format demos only)
schemas/proof_packet.schema.json
```

### Example lemmas (not research)

```bash
lean examples/lean_micro/and_comm/Micro.lean   # needs Lean 4
```

`and_comm`, `or_comm`, `not_not_intro`, `and_assoc_left` — term mode, no Mathlib intended.
They exist so the repo has **checkable Lean**, not only rankings.

---

## Method (honest)

- Deterministic offline scores on public goal text + light metadata → internal axes → `attention`.
- **Not** multi-head LLM residual (that is a different instrument in our lab stack).
- Corpus: SorryDB static-100 list; small Formal Conjectures Erdős sample.
- Cost: **$0**.

Seal (reproducibility):

| | |
|--|--|
| pack | `{exist.get('pack_id', '')}` |
| pack_root_sha256 | `{exist.get('pack_root_sha256', '')}` |

Details: [`notes/method.md`](notes/method.md)

---

## What we hope you do

1. Skim the top 10.  
2. Click one link into a real upstream `sorry`.  
3. Decide whether an attention ranking would help *your* queue / blueprint / benchmark.  
4. Optionally say which rows are nonsense.

You do not need our jargon. You do not need to reply.

---

## Non-goals

- Filling SorryDB sorries / leaderboard entry  
- Mathlib PRs  
- “Solved an Erdős problem”  
- Automated PRs without consent  
- Replacing the kernel with a score  

---

*Nerds rule. Kernel still owns truth.*
