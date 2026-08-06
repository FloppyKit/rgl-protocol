/-!
# Or.comm (example)

`p ∨ q → q ∨ p` — term-mode example for the RGL LEAN0 homework pack.
Not a research result. Kernel check owns correctness.
-/

namespace RGL.Lean0

theorem or_comm (p q : Prop) : p ∨ q → q ∨ p :=
  fun h => h.elim (fun hp => Or.inr hp) (fun hq => Or.inl hq)

end RGL.Lean0
