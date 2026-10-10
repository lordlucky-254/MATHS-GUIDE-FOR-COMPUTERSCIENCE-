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
    """O(h) numerical derivative approximation."""
    return (f(x + h) - f(x)) / h


def central_difference(f: Callable[[float], float], x: float, h: float = 1e-5) -> float:
    """O(h^2) numerical derivative approximation using symmetric Taylor cancellation."""
    return (f(x + h) - f(x - h)) / (2.0 * h)


def newton_raphson(
    f: Callable[[float], float],
    df: Callable[[float], float],
    x0: float,
    tol: float = 1e-12,
    max_iter: int = 20,
) -> Tuple[float, int]:
    """Finds root f(x) = 0 using x_{t+1} = x_t - f(x_t)/f'(x_t) (quadratic convergence)."""
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
    """
    Fits y = w * x + b by minimizing Mean Squared Error:
      L(w, b) = (1/N) * sum((w*x_i + b - y_i)^2)
    using exact partial derivatives dL/dw and dL/db.
    """
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
    # f(x) = sin(x) at x = pi/4 -> exact derivative cos(pi/4) = sqrt(2)/2
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
