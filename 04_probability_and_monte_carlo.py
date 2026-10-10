#!/usr/bin/env python3
"""
04_probability_and_monte_carlo.py
=================================
Probability Theory, Bayesian Inference & Randomized Algorithms:
  1. Bayes' Theorem: Medical / Spam Filter Posterior Probability
  2. Monte Carlo Simulation: Estimating Pi via Random Sampling
  3. Linearity of Expectation: The Coupon Collector's Problem (Server Shard Coverage)
"""

import math
import random


def bayes_theorem(prior_h: float, prob_e_given_h: float, prob_e_given_not_h: float) -> float:
    """
    Computes P(H | E) = P(E | H) * P(H) / P(E)
    where P(E) = P(E | H)*P(H) + P(E | ~H)*(1 - P(H)).
    """
    prob_e = prob_e_given_h * prior_h + prob_e_given_not_h * (1.0 - prior_h)
    return (prob_e_given_h * prior_h) / prob_e


def monte_carlo_pi(num_samples: int = 100_000, seed: int = 42) -> float:
    """Estimates Pi by sampling random points in [0, 1]^2 and checking x^2 + y^2 <= 1."""
    rng = random.Random(seed)
    inside_circle = sum(
        1 for _ in range(num_samples) if rng.random() ** 2 + rng.random() ** 2 <= 1.0
    )
    return 4.0 * inside_circle / num_samples


def coupon_collector_theoretical(n: int) -> float:
    """
    Expected number of random draws needed to hit all n buckets at least once.
    By Linearity of Expectation on Geometric RVs: E[T] = n * H_n = n * sum_{i=1}^n (1/i).
    """
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
    # Base rate of actual attack = 1%, True Positive Rate = 99%, False Positive Rate = 2%
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
    exact_expected = coupon_collector_theoretical(shards)
    sim_expected = coupon_collector_simulation(shards)
    print(f"Collecting all {shards} hash buckets:")
    print(f"  Exact Theoretical E[T] = n * H_n = {exact_expected:.2f} requests")
    print(f"  Simulated Average (2000 trials)  = {sim_expected:.2f} requests")
