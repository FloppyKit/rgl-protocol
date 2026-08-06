/-!
# And.assoc (left) (example)

`(p ∧ q) ∧ r → p ∧ (q ∧ r)` — term-mode example for the RGL LEAN0 homework pack.
Not a research result. Kernel check owns correctness.
-/

namespace RGL.Lean0

theorem and_assoc_left (p q r : Prop) : (p ∧ q) ∧ r → p ∧ (q ∧ r) :=
  fun h => And.intro h.left.left (And.intro h.left.right h.right)

end RGL.Lean0
