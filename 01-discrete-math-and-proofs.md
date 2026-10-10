# Cheat Sheet 01: Discrete Mathematics, Logic & Proof Templates

[🔙 Back to Main README](../README.md)

---

## 1. Propositional Logic Equivalences

| Law Name | Equivalence |
| :--- | :--- |
| **Implication Law** | $P \implies Q \;\equiv\; \neg P \lor Q$ |
| **Contrapositive** | $P \implies Q \;\equiv\; \neg Q \implies \neg P$ |
| **Biconditional** | $P \iff Q \;\equiv\; (P \implies Q) \land (Q \implies P)$ |
| **De Morgan's Laws** | $\neg(P \land Q) \equiv \neg P \lor \neg Q$ <br> $\neg(P \lor Q) \equiv \neg P \land \neg Q$ |
| **Distributive Laws** | $P \land (Q \lor R) \equiv (P \land Q) \lor (P \land R)$ <br> $P \lor (Q \land R) \equiv (P \lor Q) \land (P \lor R)$ |
| **Negating Quantifiers** | $\neg(\forall x \, P(x)) \equiv \exists x \, \neg P(x)$ <br> $\neg(\exists x \, P(x)) \equiv \forall x \, \neg P(x)$ |

---

## 2. Standard Proof Templates for CS Exams & Algorithms

### A. Direct Proof ($P \implies Q$)
> **Template:**
> 1. Assume $P$ is true.
> 2. Unpack definitions of terms in $P$.
> 3. Use algebraic/logical steps to derive $Q$.
> 4. Conclude $P \implies Q$. $\blacksquare$

### B. Proof by Contrapositive ($P \implies Q$)
Use when $\neg Q$ gives you cleaner information than $P$.
> **Template:**
> 1. We prove the contrapositive: $\neg Q \implies \neg P$.
> 2. Assume $\neg Q$ is true.
> 3. Deduce $\neg P$.
> 4. Since the contrapositive is logically equivalent to the original statement, $P \implies Q$. $\blacksquare$

### C. Proof by Contradiction
Use for proving uniqueness, irrationality ($\sqrt{2}$), or impossibility (Halting problem, infinitude of primes).
> **Template:**
> 1. Suppose for the sake of contradiction that the claim $S$ is false (i.e., $\neg S$ holds).
> 2. Derive a logical contradiction $C \land \neg C$.
> 3. Therefore, our assumption $\neg S$ must be false, so $S$ is true. $\blacksquare$

### D. Mathematical Induction ($\forall n \ge n_0, \, P(n)$)
Essential for proving correctness and time complexity of recursive functions.
> **Template:**
> 1. **Predicate:** Define $P(n)$ clearly as a statement about $n$.
> 2. **Base Case ($n = n_0$):** Verify that $P(n_0)$ holds directly.
> 3. **Inductive Hypothesis (IH):** Assume $P(k)$ holds for an arbitrary integer $k \ge n_0$ *(or for Strong Induction: assume $P(j)$ holds for all $n_0 \le j \le k$)*.
> 4. **Inductive Step:** Prove $P(k+1)$ using the Inductive Hypothesis.
> 5. **Conclusion:** By the Principle of Mathematical Induction, $P(n)$ holds for all $n \ge n_0$. $\blacksquare$

---

## 3. Set Theory & Relations Quick Reference

* **Power Set:** $\mathcal{P}(A)$ is the set of all subsets of $A$. $|\mathcal{P}(A)| = 2^{|A|}$.
* **Cartesian Product:** $A \times B = \{(a, b) \mid a \in A \land b \in B\}$. $|A \times B| = |A| \cdot |B|$.
* **Properties of a Binary Relation $R \subseteq A \times A$:**
  * **Reflexive:** $\forall a \in A, \, (a, a) \in R$
  * **Symmetric:** $\forall a, b \in A, \, (a, b) \in R \implies (b, a) \in R$
  * **Antisymmetric:** $\forall a, b \in A, \, (a, b) \in R \land (b, a) \in R \implies a = b$
  * **Transitive:** $\forall a, b, c \in A, \, (a, b) \in R \land (b, c) \in R \implies (a, c) \in R$
* **Equivalence Relation:** Reflexive + Symmetric + Transitive (partitions $A$ into disjoint equivalence classes).
* **Partial Order (Poset):** Reflexive + Antisymmetric + Transitive (can be topologically sorted if finite!).

---

## 4. Combinatorics: The Four-Way Counting Table

How many ways to choose $k$ items from $n$ distinct options?

| Order Matters? | Repetition Allowed? | Formula | CS Example |
| :---: | :---: | :---: | :--- |
| **Yes** (Sequence) | **Yes** | $n^k$ | Number of $k$-character strings from an alphabet of size $n$ (e.g., $2^k$ bitstrings) |
| **Yes** (Permutation) | **No** | $P(n, k) = \frac{n!}{(n-k)!}$ | Assigning $k$ distinct tasks to $k$ out of $n$ servers |
| **No** (Combination) | **No** | $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ | Choosing a subset of $k$ nodes from an $n$-node cluster |
| **No** (Multiset / Stars & Bars) | **Yes** | $\binom{n + k - 1}{k}$ | Distributing $k$ identical jobs across $n$ distinct workers |

---

## 5. Graph Theory Cheat Sheet

* **Handshaking Lemma:** In any undirected graph $G = (V, E)$, $\sum_{v \in V} \deg(v) = 2|E|$.
* **Trees (Equivalent Definitions for $G$ with $n = |V|$ vertices):**
  1. $G$ is connected and acyclic.
  2. $G$ is connected and has $n - 1$ edges.
  3. $G$ is acyclic and has $n - 1$ edges.
  4. There is a unique simple path between every pair of vertices in $G$.
* **Cayley's Formula:** The number of labeled trees on $n$ vertices is $n^{n-2}$.
* **Euler's Planar Graph Formula:** For a connected planar graph drawn with $V$ vertices, $E$ edges, and $F$ faces:
  $$V - E + F = 2 \quad \text{and (for } V \ge 3\text{)} \quad E \le 3V - 6$$
