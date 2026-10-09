# 01 — Discrete Math

## Overview

Discrete mathematics studies structures that are countable, separate, and not continuous:
integers, graphs, sets, logic, and functions on finitely many elements. While calculus deals
with continuous change, most of what computers do — compare, branch, count, route, search —
is inherently discrete. Discrete math is the language of computer science itself.

## Why it matters for CS

- **Algorithms** are walks through discrete state spaces; running time depends on counting
  steps and comparing growth rates.
- **Data structures** are discrete objects: linked lists, trees, hash tables, heaps, graphs.
- **Logic** underpins every `if`, loop, and boolean expression; proofs of correctness rest on it.
- **Counting and probability** are needed to analyze average case behaviour, hashing, and randomization.
- **Graphs** model networks, dependency graphs, social graphs, and compiler data-flow.
- Formal verification, databases (relations), and cryptography all draw on discrete structures.

## Core concepts

- Sets, tuples, sequences, and functions on finite domains
- Relations and equivalence relations
- Propositional and predicate logic
- Proof techniques: direct, contrapositive, contradiction, induction
- Counting: product rule, sum rule, permutations, combinations, pigeonhole principle
- Recurrences and closed forms
- Graphs and trees: adjacency, paths, connectivity, spanning trees
- Modular arithmetic and integer representations

## Key formulas & notation

```text
|A ∪ B| = |A| + |B| − |A ∩ B|        inclusion–exclusion (two sets)
P(n, r) = n! / (n − r)!              permutations (ordered)
C(n, r) = n! / (r! · (n − r)!)       combinations (unordered)
T(n) = T(n − 1) + c  implies  T(n) = O(n)      linear recurrence
T(n) = T(n/2) + c   implies  T(n) = O(log n)   logarithmic recurrence
```

Other notation: `∈`, `⊆`, `∅`, `ℕ` `ℤ` `ℚ` `ℝ`, `→` implication, `↔` biconditional, `¬` not,
`∧` and, `∨` or, `∀` for-all, `∃` there-exists, `Σ` summation, `Π` product.

## CS applications

- Complexity classes (`O`, `Ω`, `Θ`) and recurrence analysis
- Binary search trees, heaps, and hash tables backed by counting arguments
- Boolean algebra and circuit design
- Database relational algebra and joins
- Graph traversal (BFS/DFS), shortest paths, and spanning trees
- Cryptography: modular arithmetic, Euler's theorem, RSA foundations
- Proving code correct: loop invariants and induction

## Resources

**Textbooks**

- *Discrete Mathematics and Its Applications*, Kenneth H. Rosen
- *Discrete Mathematics with Applications*, Susanna Epp
- *Concrete Mathematics*, Graham, Knuth, and Patashnik

**Courses / lectures**

- MIT OpenCourseWare — *Mathematics for Computer Science* (Lehman, Leighton, Meyer)
- TrevTutor — Discrete math explained slowly, topic by topic

**Interactive sites**

- Brilliant — problem-driven discrete math practice
- Wolfram Alpha — symbolic computation and check-your-work

**YouTube channels**

- **3Blue1Brown** — superb visual intuition for combinatorics, graph theory, and the math behind computer science.
- **Khan Academy** — discrete math, logic, and comptellations from the ground up.
- **MIT OpenCourseWare** — full lecture series for *Mathematics for Computer Science*.
- **freeCodeCamp** — focused tutorials connecting discrete math to programming.
- **Neso Academy** — clear, structured playlists on discrete structures and logic.
- **TrevTutor** — step-by-step discrete math worked examples.
- **Computerphile** — short videos linking discrete concepts to real computer science problems.
- **Numberphile** — engaging deep dives into counting, primes, and combinatorics.