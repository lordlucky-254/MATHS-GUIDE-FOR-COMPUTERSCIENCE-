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
import math
from collections import deque
from typing import Callable, Dict, List, Set, Tuple


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
    """
    Computes exact probability that at least 2 people share a birthday
    using the complement rule: P(collision) = 1 - P(all distinct).
    """
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
