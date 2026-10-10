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
    """Returns all prime numbers <= limit in O(n log log n) time."""
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(limit**0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False
    return [i for i, prime in enumerate(is_prime) if prime]


def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """
    Returns (g, x, y) such that a*x + b*y = g = gcd(a, b).
    """
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y


def mod_inverse(a: int, m: int) -> int:
    """Computes a^(-1) mod m using the Extended Euclidean Algorithm."""
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError(f"Modular inverse does not exist since gcd({a}, {m}) = {g} != 1")
    return x % m


def mod_exp(base: int, exp: int, mod: int) -> int:
    """Computes (base^exp) % mod in O(log exp) multiplications (Square-and-Multiply)."""
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
    p, q = 1009, 2741  # Two distinct primes
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 65537  # Standard public exponent
    d = mod_inverse(e, phi_n)  # Private key d = e^(-1) mod phi(n)

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
