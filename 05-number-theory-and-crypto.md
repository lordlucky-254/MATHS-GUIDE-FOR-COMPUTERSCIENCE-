# Cheat Sheet 05: Number Theory, Abstract Algebra & Cryptography

[🔙 Back to Main README](../README.md)

---

## 1. Divisibility, GCD & Modular Arithmetic

* **Division Algorithm:** For any integer $a$ and $d > 0$, there exist unique integers $q$ (quotient) and $r$ (remainder) such that:
  $$a = dq + r \quad \text{with } 0 \le r < d$$
* **Euclidean Algorithm:** $\gcd(a, b) = \gcd(b, a \bmod b)$, with base case $\gcd(a, 0) = a$. Runs in $O(\log(\min(a,b)))$ steps.
* **Bézout's Identity (Extended GCD):** For any integers $a, b$, there exist integers $x, y$ such that:
  $$ax + by = \gcd(a, b)$$
* **Modular Inverse:** $a^{-1} \bmod m$ exists **if and only if** $\gcd(a, m) = 1$. Found via Extended GCD ($ax + my = 1 \implies ax \equiv 1 \pmod m$).

---

## 2. Essential Theorems for Cryptography

### Fermat's Little Theorem
If $p$ is prime and $p \nmid a$:
$$a^{p-1} \equiv 1 \pmod p \quad \implies \quad a^{-1} \equiv a^{p-2} \pmod p$$

### Euler's Totient Function $\phi(n)$
Counts positive integers $\le n$ that are coprime to $n$:
* If $p$ is prime: $\phi(p) = p - 1$ and $\phi(p^k) = p^k - p^{k-1}$.
* If $n = p_1^{k_1} \cdots p_r^{k_r}$: $\phi(n) = n \prod_{i=1}^r \left(1 - \frac{1}{p_i}\right)$.
* **Euler's Theorem:** For any $a$ with $\gcd(a, n) = 1$:
  $$a^{\phi(n)} \equiv 1 \pmod n$$

### Chinese Remainder Theorem (CRT)
If $m_1, m_2, \dots, m_k$ are pairwise coprime ($\gcd(m_i, m_j) = 1$ for $i \neq j$), then the system:
$$x \equiv a_1 \pmod{m_1}, \quad x \equiv a_2 \pmod{m_2}, \quad \dots, \quad x \equiv a_k \pmod{m_k}$$
has a **unique solution modulo $M = m_1 m_2 \cdots m_k$**:
$$x = \left(\sum_{i=1}^k a_i M_i y_i\right) \bmod M \quad \text{where } M_i = \frac{M}{m_i} \text{ and } y_i = M_i^{-1} \bmod m_i$$

---

## 3. RSA Public-Key Cryptosystem Summary

1. **Key Generation:**
   * Choose two large distinct primes $p$ and $q$.
   * Compute modulus $n = pq$ and totient $\phi(n) = (p-1)(q-1)$ (or Carmichael's $\lambda(n) = \text{lcm}(p-1, q-1)$).
   * Choose public exponent $e$ (commonly $e = 65537$) such that $\gcd(e, \phi(n)) = 1$.
   * Compute private key $d \equiv e^{-1} \pmod{\phi(n)}$ via Extended Euclidean Algorithm.
2. **Encryption (of message $m \in [0, n-1]$):**
   $$c = m^e \bmod n$$
3. **Decryption (of ciphertext $c$):**
   $$m = c^d \bmod n$$

---

## 4. Abstract Algebra Hierarchy

| Structure | Operations | Axioms Required | Examples in CS |
| :--- | :---: | :--- | :--- |
| **Monoid** | $(S, \cdot)$ | Closure, Associativity, Identity element | String concatenation, `reduce()` operations |
| **Group** | $(G, \cdot)$ | Monoid + Inverse for every element | $\mathbb{Z}_n$, Elliptic curve points, permutations ($S_n$) |
| **Abelian Group** | $(G, +)$ | Group + Commutativity ($a+b = b+a$) | $(\mathbb{Z}, +)$, XOR on $n$-bit words |
| **Ring** | $(R, +, \times)$ | Abelian group under $+$, Monoid under $\times$, Distributive | Integers $\mathbb{Z}$, Polynomials $\mathbb{F}[x]$, $n \times n$ matrices |
| **Field** | $(\mathbb{F}, +, \times)$ | Commutative Ring + Multiplicative inverse for all $a \neq 0$ | $\mathbb{R}$, $\mathbb{Z}_p$ ($p$ prime), Galois Field $GF(2^8)$ in AES |
