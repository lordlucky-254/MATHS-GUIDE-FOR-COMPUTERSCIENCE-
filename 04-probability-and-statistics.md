# Cheat Sheet 04: Probability Theory & Statistics for CS

[🔙 Back to Main README](../README.md)

---

## 1. Core Axioms & Bayes' Theorem

* **Axioms:** $0 \le P(A) \le 1$, $P(\Omega) = 1$, and for disjoint events, $P(\bigcup_i A_i) = \sum_i P(A_i)$.
* **Inclusion-Exclusion:** $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.
* **Conditional Probability & Chain Rule:**
  $$P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \qquad P(A_1 \cap A_2 \cap \dots \cap A_n) = \prod_{i=1}^n P(A_i \mid A_1, \dots, A_{i-1})$$
* **Law of Total Probability:** If $B_1, \dots, B_k$ partition the sample space $\Omega$:
  $$P(A) = \sum_{i=1}^k P(A \mid B_i) P(B_i)$$
* **Bayes' Theorem:**
  $$\underbrace{P(H \mid E)}_{\text{Posterior}} = \frac{\overbrace{P(E \mid H)}^{\text{Likelihood}} \cdot \overbrace{P(H)}^{\text{Prior}}}{\underbrace{P(E)}_{\text{Evidence}}}$$

---

## 2. Expectation, Variance & Indicator Random Variables

* **Expectation:** $E[X] = \sum_x x P(X=x)$ (discrete) or $\int_{-\infty}^\infty x f(x)\,dx$ (continuous).
* **Linearity of Expectation (Superpower for CS):** For **any** random variables $X_1, \dots, X_n$ (even if strongly dependent!):
  $$E\left[\sum_{i=1}^n c_i X_i\right] = \sum_{i=1}^n c_i E[X_i]$$
* **Indicator Random Variable Trick:** If $I_A = 1$ when event $A$ occurs and $0$ otherwise, then:
  $$E[I_A] = P(A)$$
* **Variance:** $\text{Var}(X) = E[(X - E[X])^2] = E[X^2] - (E[X])^2$.
  * $\text{Var}(aX + b) = a^2 \text{Var}(X)$.
  * If $X$ and $Y$ are independent: $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$.

---

## 3. Essential Distributions in Computer Science

| Distribution | PMF / PDF | Mean $E[X]$ | Variance $\text{Var}(X)$ | Classic CS Application |
| :--- | :--- | :---: | :---: | :--- |
| **Bernoulli($p$)** | $p^x (1-p)^{1-x}$ for $x \in \{0,1\}$ | $p$ | $p(1-p)$ | Single coin flip, bit flip, packet drop |
| **Binomial($n, p$)** | $\binom{n}{k} p^k (1-p)^{n-k}$ | $np$ | $np(1-p)$ | Number of successes in $n$ independent trials |
| **Geometric($p$)** | $(1-p)^{k-1} p$ for $k \ge 1$ | $\frac{1}{p}$ | $\frac{1-p}{p^2}$ | Expected trials until first hash/pivot hit |
| **Poisson($\lambda$)** | $\frac{\lambda^k e^{-\lambda}}{k!}$ | $\lambda$ | $\lambda$ | Server request arrivals per second |
| **Uniform($a, b$)** | $\frac{1}{b-a}$ on $[a,b]$ | $\frac{a+b}{2}$ | $\frac{(b-a)^2}{12}$ | Random number generators (`random.random()`) |
| **Exponential($\lambda$)** | $\lambda e^{-\lambda x}$ for $x \ge 0$ | $\frac{1}{\lambda}$ | $\frac{1}{\lambda^2}$ | Time between server requests / hardware failure |
| **Normal $\mathcal{N}(\mu, \sigma^2)$** | $\frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$ | $\mu$ | $\sigma^2$ | Noise modeling, CLT averages, weight init |

---

## 4. Concentration Inequalities (Randomized Algorithms)

* **Markov's Inequality** (for non-negative $X$ and $a > 0$):
  $$P(X \ge a) \le \frac{E[X]}{a}$$
* **Chebyshev's Inequality:**
  $$P(|X - E[X]| \ge k\sigma) \le \frac{1}{k^2}$$
* **Chernoff Bound (Multiplicative):** For $X = \sum_{i=1}^n X_i$ of independent Bernoulli trials with $\mu = E[X]$ and $\delta \in (0, 1)$:
  $$P(|X - \mu| \ge \delta \mu) \le 2 e^{-\mu \delta^2 / 3}$$
