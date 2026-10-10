# Practice Problems & Step-by-Step Solutions

[🔙 Back to Main README](../README.md)

Test your understanding across all core Computer Science mathematics topics. Click on any **Show Solution** dropdown to reveal the complete proof or derivation.

---

## 1. Discrete Mathematics & Proofs

### Problem 1.1 (Mathematical Induction & Loop Invariants)
Prove by induction that for all integers $n \ge 1$:
$$\sum_{i=1}^{n} i \cdot 2^{i-1} = (n - 1)2^n + 1$$

<details>
<summary><b>💡 Show Solution</b></summary>

* **Base Case ($n = 1$):**
  * Left-hand side: $1 \cdot 2^{1-1} = 1$.
  * Right-hand side: $(1 - 1)2^1 + 1 = 0 + 1 = 1$. Base case holds.
* **Inductive Hypothesis:** Suppose $\sum_{i=1}^{k} i \cdot 2^{i-1} = (k - 1)2^k + 1$ holds for an arbitrary integer $k \ge 1$.
* **Inductive Step:** Consider $n = k + 1$:
  $$\sum_{i=1}^{k+1} i \cdot 2^{i-1} = \left(\sum_{i=1}^{k} i \cdot 2^{i-1}\right) + (k + 1)2^k$$
  By the Inductive Hypothesis:
  $$= (k - 1)2^k + 1 + (k + 1)2^k = ((k - 1) + (k + 1))2^k + 1 = 2k \cdot 2^k + 1 = k \cdot 2^{k+1} + 1$$
  This matches $((k+1) - 1)2^{k+1} + 1$. By Mathematical Induction, the identity holds for all $n \ge 1$. $\blacksquare$
</details>

---

## 2. Asymptotics & Recurrence Relations

### Problem 2.1 (Master Theorem)
Solve the following recurrence relations for their asymptotic tight bound $\Theta(\cdot)$:
1. $T(n) = 4T(n/2) + n$
2. $T(n) = 2T(n/2) + n \log n$
3. $T(n) = 3T(n/4) + n^2$

<details>
<summary><b>💡 Show Solution</b></summary>

1. **$T(n) = 4T(n/2) + n$:** Here $a=4, b=2 \implies c_{\text{crit}} = \log_2 4 = 2$. Since $f(n) = n^1 = O(n^{2-\epsilon})$, Case 1 applies: **$T(n) = \Theta(n^2)$**.
2. **$T(n) = 2T(n/2) + n \log n$:** Here $a=2, b=2 \implies c_{\text{crit}} = \log_2 2 = 1$. Since $f(n) = \Theta(n^1 \log^1 n)$, Case 2 ($k=1$) applies: **$T(n) = \Theta(n \log^2 n)$**.
3. **$T(n) = 3T(n/4) + n^2$:** Here $a=3, b=4 \implies c_{\text{crit}} = \log_4 3 \approx 0.792$. Since $f(n) = n^2 = \Omega(n^{0.792 + \epsilon})$ and $3(n/4)^2 = \frac{3}{16}n^2 \le c n^2$, Case 3 applies: **$T(n) = \Theta(n^2)$**.
</details>

---

## 3. Graph Theory & Combinatorics

### Problem 3.1 (Degree Sequence & Handshaking Lemma)
Can a simple undirected graph with $7$ vertices have each vertex of degree $3$? Why or why not?

<details>
<summary><b>💡 Show Solution</b></summary>

**No.** By the **Handshaking Lemma**, the sum of degrees of all vertices in any undirected graph equals twice the number of edges:
$$\sum_{v \in V} \deg(v) = 2|E|$$
If there were $7$ vertices each of degree $3$, the sum of degrees would be $7 \times 3 = 21$, which is odd and cannot equal $2|E|$. (Corollary: Every undirected graph has an even number of vertices of odd degree).
</details>

---

## 4. Linear Algebra

### Problem 4.1 (Eigenvalues & Matrix Powers)
Find the eigenvalues and eigenvectors of $A = \begin{bmatrix} 4 & 1 \\ 2 & 3 \end{bmatrix}$.

<details>
<summary><b>💡 Show Solution</b></summary>

* **Characteristic polynomial:**
  $$\det(A - \lambda I) = (4 - \lambda)(3 - \lambda) - (1)(2) = \lambda^2 - 7\lambda + 10 = (\lambda - 5)(\lambda - 2) = 0$$
* **Eigenvalues:** $\lambda_1 = 5$ and $\lambda_2 = 2$.
  *(Sanity check: $\text{Tr}(A) = 4 + 3 = 7 = 5 + 2$, and $\det(A) = 12 - 2 = 10 = 5 \times 2$.)*
* **Eigenvectors:**
  * For $\lambda_1 = 5$: $(A - 5I)v = \begin{bmatrix} -1 & 1 \\ 2 & -2 \end{bmatrix} v = 0 \implies v_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$.
  * For $\lambda_2 = 2$: $(A - 2I)v = \begin{bmatrix} 2 & 1 \\ 2 & 1 \end{bmatrix} v = 0 \implies v_2 = \begin{bmatrix} 1 \\ -2 \end{bmatrix}$.
</details>

---

## 5. Probability & Randomized Algorithms

### Problem 5.1 (Hash Table Collisions via Linearity of Expectation)
Suppose $n$ keys are hashed uniformly and independently into a hash table with $m$ slots. What is the **expected number of collisions** (pairs of distinct keys $(i, j)$ with $i < j$ that hash to the same slot)?

<details>
<summary><b>💡 Show Solution</b></summary>

For each pair $(i, j)$ with $1 \le i < j \le n$, define the indicator random variable:
$$X_{ij} = \begin{cases} 1 & \text{if } h(i) = h(j) \\ 0 & \text{otherwise} \end{cases}$$
Since keys are hashed uniformly and independently into $m$ slots, $P(h(i) = h(j)) = \frac{1}{m}$, so $E[X_{ij}] = \frac{1}{m}$.
There are $\binom{n}{2} = \frac{n(n-1)}{2}$ pairs in total. By **Linearity of Expectation**:
$$E[\text{Total Collisions}] = \sum_{1 \le i < j \le n} E[X_{ij}] = \binom{n}{2} \frac{1}{m} = \frac{n(n-1)}{2m}$$
*(Notice that when $n \approx \sqrt{2m}$, the expected number of collisions reaches $1$ — the Birthday Bound!)*
</details>

---

## 6. Number Theory & Cryptography

### Problem 6.1 (Modular Inverse & Extended GCD)
Find the multiplicative inverse of $17 \pmod{43}$.

<details>
<summary><b>💡 Show Solution</b></summary>

Run the Euclidean Algorithm on $43$ and $17$:
1. $43 = 2 \times 17 + 9$
2. $17 = 1 \times 9 + 8$
3. $9 = 1 \times 8 + 1$

Now back-substitute to express $1$ as a linear combination of $43$ and $17$:
$$1 = 9 - 1 \times 8 = 9 - 1 \times (17 - 1 \times 9) = 2 \times 9 - 17$$
$$1 = 2 \times (43 - 2 \times 17) - 17 = 2 \times 43 - 5 \times 17$$
Taking modulo $43$:
$$(-5) \times 17 \equiv 1 \pmod{43} \implies 17^{-1} \equiv -5 \equiv 38 \pmod{43}$$
Check: $17 \times 38 = 646 = 15 \times 43 + 1 \equiv 1 \pmod{43}$.
</details>
