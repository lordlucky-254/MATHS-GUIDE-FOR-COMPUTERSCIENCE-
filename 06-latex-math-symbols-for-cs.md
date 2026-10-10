# Cheat Sheet 06: LaTeX Math Symbols & Notation for CS Students

[🔙 Back to Main README](../README.md)

Use this lookup table when writing CS homework, research papers, or Markdown notes (GitHub natively supports `$inline$` and `$$block$$` LaTeX math!).

---

## 1. Logic & Set Theory

| Symbol | Meaning | LaTeX Command |
| :---: | :--- | :--- |
| $\forall$ | For all (Universal quantifier) | `\forall` |
| $\exists$ | There exists (Existential quantifier) | `\exists` |
| $\nexists$ | There does not exist | `\nexists` |
| $\neg$ | Logical NOT | `\neg` or `\lnot` |
| $\land$ | Logical AND (Conjunction) | `\land` or `\wedge` |
| $\lor$ | Logical OR (Disjunction) | `\lor` or `\vee` |
| $\oplus$ | Logical XOR (Exclusive OR) | `\oplus` |
| $\implies$ | Implies (If... then...) | `\implies` |
| $\iff$ | If and only if (Biconditional) | `\iff` |
| $\equiv$ | Logically equivalent / Congruent | `\equiv` |
| $\in, \notin$ | Element of / Not element of | `\in`, `\notin` |
| $\subseteq, \subset$ | Subset / Proper subset | `\subseteq`, `\subset` |
| $\cup, \cap$ | Set Union / Set Intersection | `\cup`, `\cap` |
| $\setminus$ | Set Difference | `\setminus` |
| $\emptyset$ | Empty set | `\emptyset` or `\varnothing` |
| $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}, \mathbb{C}$ | Number sets | `\mathbb{N}`, `\mathbb{Z}`, `\mathbb{Q}`, `\mathbb{R}`, `\mathbb{C}` |

---

## 2. Algorithms, Sums, Floors & Asymptotics

| Symbol | Meaning | LaTeX Command |
| :---: | :--- | :--- |
| $\lfloor x \rfloor$ | Floor of $x$ (greatest integer $\le x$) | `\lfloor x \rfloor` |
| $\lceil x \rceil$ | Ceiling of $x$ (smallest integer $\ge x$) | `\lceil x \rceil` |
| $\sum_{i=1}^{n} a_i$ | Summation | `\sum_{i=1}^{n} a_i` |
| $\prod_{i=1}^{n} a_i$ | Product | `\prod_{i=1}^{n} a_i` |
| $\binom{n}{k}$ | Binomial coefficient ($n$ choose $k$) | `\binom{n}{k}` |
| $O(n), \Omega(n), \Theta(n)$ | Asymptotic bounds | `O(n)`, `\Omega(n)`, `\Theta(n)` |
| $a \equiv b \pmod m$ | Modular congruence | `a \equiv b \pmod m` |
| $a \mid b, \; a \nmid b$ | $a$ divides $b$ / $a$ does not divide $b$ | `a \mid b`, `a \nmid b` |

---

## 3. Linear Algebra, Calculus & Probability

| Symbol | Meaning | LaTeX Command |
| :---: | :--- | :--- |
| $\vec{v}, \mathbf{v}$ | Vector | `\vec{v}` or `\mathbf{v}` |
| $\|x\|_2$ | Vector norm | `\|x\|_2` |
| $\nabla f$ | Gradient of $f$ | `\nabla f` |
| $\frac{\partial f}{\partial x}$ | Partial derivative | `\frac{\partial f}{\partial x}` |
| $\int_{a}^{b} f(x)\,dx$ | Definite integral | `\int_{a}^{b} f(x)\,dx` |
| $\mathbb{E}[X]$ | Expected value | `\mathbb{E}[X]` |
| $\text{Var}(X)$ | Variance | `\text{Var}(X)` |
| $X \sim \mathcal{N}(\mu, \sigma^2)$ | Distributed as Normal | `X \sim \mathcal{N}(\mu, \sigma^2)` |
| $\begin{bmatrix} a & b \\ c & d \end{bmatrix}$ | Matrix | `\begin{bmatrix} a & b \\ c & d \end{bmatrix}` |
