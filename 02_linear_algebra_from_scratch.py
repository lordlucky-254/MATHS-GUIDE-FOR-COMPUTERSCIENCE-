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


def matmul(A: Matrix, B: Matrix) -> Matrix:
    rows_a, cols_a = len(A), len(A[0])
    rows_b, cols_b = len(B), len(B[0])
    if cols_a != rows_b:
        raise ValueError(f"Dimension mismatch: {rows_a}x{cols_a} vs {rows_b}x{cols_b}")
    return [
        [sum(A[i][k] * B[k][j] for k in range(cols_a)) for j in range(cols_b)]
        for i in range(rows_a)
    ]


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

    # Back-substitution
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (aug[i][n] - sum(aug[i][j] * x[j] for j in range(i + 1, n))) / aug[i][i]
    return x


def pagerank_power_iteration(
    adj_matrix: Matrix, damping: float = 0.85, iterations: int = 50
) -> Vector:
    """
    Computes PageRank scores (dominant eigenvector of the Google matrix)
    for a directed graph where adj_matrix[i][j] = 1 if page i links to page j.
    """
    n = len(adj_matrix)
    # Build column-stochastic transition matrix M
    M = [[0.0] * n for _ in range(n)]
    for j in range(n):
        out_degree = sum(adj_matrix[j])
        for i in range(n):
            if out_degree > 0:
                M[i][j] = adj_matrix[j][i] / out_degree
            else:
                M[i][j] = 1.0 / n

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
    # 2x +  y - z =  8
    # -3x - y + 2z = -11
    # -2x + y + 2z = -3
    A = [[2.0, 1.0, -1.0], [-3.0, -1.0, 2.0], [-2.0, 1.0, 2.0]]
    b = [8.0, -11.0, -3.0]
    solution = gaussian_elimination(A, b)
    print(f"Solution x = {[round(val, 4) for val in solution]} (Expected: [2.0, 3.0, -1.0])\n")

    print("=== 3. Eigenvectors in Action: Google PageRank via Power Iteration ===")
    # 4 webpages: Page 0 is linked by everyone; Page 3 only links to Page 0
    links = [
        [0, 1, 1, 0],  # Page 0 links to 1, 2
        [1, 0, 0, 0],  # Page 1 links to 0
        [1, 1, 0, 1],  # Page 2 links to 0, 1, 3
        [1, 0, 0, 0],  # Page 3 links to 0
    ]
    scores = pagerank_power_iteration(links)
    for idx, score in enumerate(scores):
        print(f"  Page {idx}: PageRank = {score:.4f}")
