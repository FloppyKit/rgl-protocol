# Extended table

See [../README.md](../README.md) for the main writeup.

## 1. `frenzymath/jixia`

- **File:** `Example.lean:82`
- **URL:** https://github.com/frenzymath/jixia/blob/e6d1448771f53b540a450fdf5180f1217efaaab8/Example.lean#L82
- **Commit:** `e6d1448771f5`
- **Attention:** 0.5565 · `surface_gap` · `mixed_priority`

**English:** In English: prove that Option.none is not a 'some' value (basic Option fact).

<details><summary>pretty-printed goal</summary>

```text
α : Type u ⊢ ¬none.IsSome
```

</details>

## 2. `lean-ja/lean-by-example`

- **File:** `LeanByExample/Tactic/Plausible.lean:67`
- **URL:** https://github.com/lean-ja/lean-by-example/blob/3ebe85bea550147ea661babd12b968bf8e97a7ed/LeanByExample/Tactic/Plausible.lean#L67
- **Commit:** `3ebe85bea550`
- **Attention:** 0.5565 · `surface_gap` · `mixed_priority`

**English:** In English: in a teaching natural-number type, prove the stated equality (tutorial obligation).

<details><summary>pretty-printed goal</summary>

```text
⊢ ∀ (a b : MyNat), a = b
```

</details>

## 3. `emilyriehl/infinity-cosmos`

- **File:** `InfinityCosmos/ForMathlib/InfinityCosmos/Isofibrations.lean:70`
- **URL:** https://github.com/emilyriehl/infinity-cosmos/blob/bf1885e46ff0fde2a1cde218001d9b90307f4224/InfinityCosmos/ForMathlib/InfinityCosmos/Isofibrations.lean#L70
- **Commit:** `bf1885e46ff0`
- **Attention:** 0.552 · `rich_open` · `high_priority`

**English:** In English: assume a suitable infinity-cosmos setting and two maps that are already isofibrations; prove that the map obtained by taking their product is also an isofibration. (A 'stability under products' property for those maps.)

<details><summary>pretty-printed goal</summary>

```text
K : Type u inst✝¹ : Category.{v, u} K inst✝ : InfinityCosmos K X Y X' Y' : K f : X ↠ Y g : X' ↠ Y' ⊢ IsIsofibration (prod.map ↑f ↑g)
```

</details>

## 4. `lean-ja/lean-by-example`

- **File:** `LeanByExample/Attribute/Aesop.lean:88`
- **URL:** https://github.com/lean-ja/lean-by-example/blob/3ebe85bea550147ea661babd12b968bf8e97a7ed/LeanByExample/Attribute/Aesop.lean#L88
- **Commit:** `3ebe85bea550`
- **Attention:** 0.525 · `surface_gap` · `mid_priority`

**English:** In English: prove a teaching-list value is nonempty (example file obligation).

<details><summary>pretty-printed goal</summary>

```text
⊢ NonEmpty (MyList.cons 1 MyList.nil)
```

</details>

## 5. `FormalizedFormalLogic/Foundation`

- **File:** `Foundation/ProvabilityLogic/Grz/Completeness.lean:34`
- **URL:** https://github.com/FormalizedFormalLogic/Foundation/blob/2d0d958822ddfb22e58f2cb6266a52f3bb219fff/Foundation/ProvabilityLogic/Grz/Completeness.lean#L34
- **Commit:** `2d0d958822dd`
- **Attention:** 0.4845 · `surface_gap` · `mid_priority`

**English:** In English: finish an intermediate lemma inside a modal / provability-logic development (technical context above the goal; not a one-line slogan theorem).

<details><summary>pretty-printed goal</summary>

```text
case intro α : Type u_1 inst✝² : DecidableEq α R : α → α → Prop inst✝¹ : DecidableEq α inst✝ : IsTrans α R l : List α i j : Fin l.length h : Chain' R l eij : i ≠ j nRij : ¬R (l.get i) (l.get j) nRji :
```

</details>

## 6. `FormalizedFormalLogic/Foundation`

- **File:** `Foundation/ProvabilityLogic/Grz/Completeness.lean:251`
- **URL:** https://github.com/FormalizedFormalLogic/Foundation/blob/2d0d958822ddfb22e58f2cb6266a52f3bb219fff/Foundation/ProvabilityLogic/Grz/Completeness.lean#L251
- **Commit:** `2d0d958822dd`
- **Attention:** 0.4845 · `surface_gap` · `mid_priority`

**English:** In English: finish an intermediate lemma inside a modal / provability-logic development (technical context above the goal; not a one-line slogan theorem).

<details><summary>pretty-printed goal</summary>

```text
M : Model inst✝¹ : IsTrans M.World M.Rel inst✝ : IsIrrefl M.World M.Rel l : List M.World n : ℕ+ l_length : l.length = ↑n + 1 l_chain : List.Chain' (fun x1 x2 => x1 ≺ x2) l Γ : Finset (Formula ℕ) Γ_len
```

</details>

## 7. `FormalizedFormalLogic/Foundation`

- **File:** `Foundation/ProvabilityLogic/S/Completeness.lean:253`
- **URL:** https://github.com/FormalizedFormalLogic/Foundation/blob/a2cbf6a6c08a4e59a8ac27e0e85e5c562af7bb32/Foundation/ProvabilityLogic/S/Completeness.lean#L253
- **Commit:** `a2cbf6a6c08a`
- **Attention:** 0.4845 · `surface_gap` · `mid_priority`

**English:** In English: finish an intermediate lemma inside a modal / provability-logic development (technical context above the goal; not a one-line slogan theorem).

<details><summary>pretty-printed goal</summary>

```text
L : Language inst✝⁸ : Semiterm.Operator.GoedelNumber L (Sentence L) inst✝⁷ : L.DecidableEq T₀ T : Theory ℒₒᵣ inst✝⁶ : T₀ ⪯ T inst✝⁵ : Diagonalization T₀ 𝔅 : ProvabilityPredicate T₀ T inst✝⁴ : 𝔅.HBL in
```

</details>

## 8. `FormalizedFormalLogic/Foundation`

- **File:** `Foundation/ProvabilityLogic/S/Completeness.lean:375`
- **URL:** https://github.com/FormalizedFormalLogic/Foundation/blob/d773e9c193bd4782c94b32ea63ede4aae696573a/Foundation/ProvabilityLogic/S/Completeness.lean#L375
- **Commit:** `d773e9c193bd`
- **Attention:** 0.4845 · `surface_gap` · `mid_priority`

**English:** In English: finish an intermediate lemma inside a modal / provability-logic development (technical context above the goal; not a one-line slogan theorem).

<details><summary>pretty-printed goal</summary>

```text
T : Theory ℒₒᵣ inst✝³ : ℕ ⊧ₘ* T A : Modal.Formula ℕ inst✝² : T.Delta1Definable inst✝¹ : 𝐈𝚺₁ ⪯ T inst✝ : SoundOn T (Hierarchy 𝚷 2) tfae_1_to_2 : Finset.conj A.rflSubformula ➝ A ∈ Logic.GL → A ∈ Logic.S
```

</details>

## 9. `leanprover-community/duper`

- **File:** `Duper/Tests/test_continuity.lean:18`
- **URL:** https://github.com/leanprover-community/duper/blob/e28c4e11389116ccb6a48ff0fe9c3d1a9d7642e4/Duper/Tests/test_continuity.lean#L18
- **Commit:** `e28c4e113891`
- **Attention:** 0.4584 · `surface_gap` · `mid_priority`

**English:** In English: prove that the distance from a point to itself is zero (basic metric fact in a test file).

<details><summary>pretty-printed goal</summary>

```text
a : Real ⊢ dist a a = zero
```

</details>

## 10. `leanprover-community/batteries`

- **File:** `BatteriesTest/lint_unreachableTactic.lean:23`
- **URL:** https://github.com/leanprover-community/batteries/blob/e119df7e78d94b18b34067db93e8fc0d448d696f/BatteriesTest/lint_unreachableTactic.lean#L23
- **Commit:** `e119df7e78d9`
- **Attention:** 0.4584 · `surface_gap` · `mid_priority`

**English:** In English: prove 1 = 1 (trivial test/linter obligation, not research math).

<details><summary>pretty-printed goal</summary>

```text
⊢ 1 = 1
```

</details>

## 11. `leanprover-community/aesop`

- **File:** `AesopTest/ExtScript.lean:103`
- **URL:** https://github.com/leanprover-community/aesop/blob/dd78c1426f5fc783ec1ba23ad769471cc69bb8b4/AesopTest/ExtScript.lean#L103
- **Commit:** `dd78c1426f5f`
- **Attention:** 0.4584 · `surface_gap` · `mid_priority`

**English:** In English: likely a test-suite or linter obligation rather than a research theorem.

<details><summary>pretty-printed goal</summary>

```text
case a α β γ δ ι : Type x y : T ⊢ u = v
```

</details>

## 12. `leanprover-community/duper`

- **File:** `Duper/Tests/test_continuity.lean:20`
- **URL:** https://github.com/leanprover-community/duper/blob/e28c4e11389116ccb6a48ff0fe9c3d1a9d7642e4/Duper/Tests/test_continuity.lean#L20
- **Commit:** `e28c4e113891`
- **Attention:** 0.4584 · `surface_gap` · `mid_priority`

**English:** In English: likely a test-suite or linter obligation rather than a research theorem.

<details><summary>pretty-printed goal</summary>

```text
a : Real ⊢ lt zero one
```

</details>
