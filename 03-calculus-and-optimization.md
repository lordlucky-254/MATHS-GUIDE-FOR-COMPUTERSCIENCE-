# Cheat Sheet 03: Calculus, Automatic Differentiation & Optimization

[🔙 Back to Main README](../README.md)

---

## 1. Essential Derivatives & Asymptotic Limits

| Function $f(x)$ | Derivative $f'(x)$ | CS Relevance |
| :--- | :--- | :--- |
| $x^n$ | $n x^{n-1}$ | Polynomial loss functions |
| $e^x$ | $e^x$ | Softmax & exponential growth |
| $a^x$ | $a^x \ln(a)$ | Branching factor analysis |
| $\ln(x)$ | $\frac{1}{x}$ | Log-likelihood & cross-entropy loss |
| $\log_2(x)$ | $\frac{1}{x \ln(2)}$ | Information entropy & binary trees |
| $\sigma(x) = \frac{1}{1 + e^{-x}}$ | $\sigma(x)(1 - \sigma(x))$ | Logistic sigmoid activation |
| $\tanh(x)$ | $1 - \tanh^2(x)$ | RNN / neural activation |
| $\text{ReLU}(x) = \max(0, x)$ | $1 \text{ if } x > 0 \text{ else } 0$ | Standard deep learning activation |

### L'Hôpital's Rule for Comparing Big-O Complexity
If $\lim_{n \to \infty} f(n) = \infty$ and $\lim_{n \to \infty} g(n) = \infty$:
$$\lim_{n \to \infty} \frac{f(n)}{g(n)} = \lim_{n \to \infty} \frac{f'(n)}{g'(n)}$$
* **Result $= 0$:** $f(n) = o(g(n))$ ($f$ grows strictly slower than $g$, e.g., $\ln n$ vs $n^\epsilon$).
* **Result $= c \in (0, \infty)$:** $f(n) = \Theta(g(n))$.
* **Result $= \infty$:** $f(n) = \omega(g(n))$ ($f$ grows strictly faster than $g$, e.g., $n^2$ vs $n \log n$).

---

## 2. Multivariable Calculus & Matrix Calculus

For a scalar function $f: \mathbb{R}^n \to \mathbb{R}$ and vector function $F: \mathbb{R}^n \to \mathbb{R}^m$:

* **Gradient Vector ($\nabla f \in \mathbb{R}^n$):** Points in the direction of **steepest ascent**:
  $$\nabla f(x) = \begin{bmatrix} \frac{\partial f}{\partial x_1} & \frac{\partial f}{\partial x_2} & \dots & \frac{\partial f}{\partial x_n} \end{bmatrix}^T$$
* **Jacobian Matrix ($J \in \mathbb{R}^{m \times n}$):** First-order partial derivatives of a vector-valued function:
  $$J_{ij} = \frac{\partial F_i}{\partial x_j}$$
* **Hessian Matrix ($H \in \mathbb{R}^{n \times n}$):** Symmetric matrix of second-order partial derivatives (measures local curvature):
  $$H_{ij} = \frac{\partial^2 f}{\partial x_i \partial x_j}$$
* **Common Matrix Gradients (Used in Linear Regression & Neural Nets):**
  * $\nabla_x (a^T x) = a$
  * $\nabla_x (x^T A x) = (A + A^T)x$ (or $2Ax$ if $A$ is symmetric)
  * $\nabla_x \|Ax - b\|_2^2 = 2A^T(Ax - b)$

---

## 3. Optimization Algorithms

### Gradient Descent (First-Order)
$$\theta_{t+1} = \theta_t - \eta \nabla L(\theta_t)$$
where $\eta > 0$ is the learning rate (step size).

### Momentum
$$v_{t+1} = \beta v_t + \nabla L(\theta_t), \qquad \theta_{t+1} = \theta_t - \eta v_{t+1}$$

### Newton's Method (Second-Order)
Uses the Hessian inverse to jump directly toward critical points of quadratic approximations:
$$\theta_{t+1} = \theta_t - [H(\theta_t)]^{-1} \nabla L(\theta_t)$$
*(In 1D root-finding for $g(x) = 0$: $x_{t+1} = x_t - \frac{g(x_t)}{g'(x_t)}$).*
