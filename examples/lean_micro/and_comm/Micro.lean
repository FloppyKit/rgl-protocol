/-!
# And.comm (example)

`p ∧ q → q ∧ p` — term-mode example for the RGL LEAN0 homework pack.
Not a research result. Kernel check owns correctness.
-/

namespace RGL.Lean0

theorem and_comm (p q : Prop) : p ∧ q → q ∧ p :=
  fun h => And.intro h.right h.left

end RGL.Lean0
