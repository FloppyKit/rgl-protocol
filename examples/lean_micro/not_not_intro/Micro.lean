/-!
# Not.not_intro (example)

`p → ¬¬p` — term-mode example for the RGL LEAN0 homework pack.
Not a research result. Kernel check owns correctness.
-/

namespace RGL.Lean0

theorem not_not_intro (p : Prop) : p → ¬¬p :=
  fun hp hnp => hnp hp

end RGL.Lean0
