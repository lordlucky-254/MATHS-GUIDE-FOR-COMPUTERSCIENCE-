# Cheat Sheet 02: Linear Algebra for Computer Science

[🔙 Back to Main README](../README.md)

---

## 1. Vectors, Norms & Inner Products

Given $u, v \in \mathbb{R}^n$:
* **Dot Product (Algebraic):** $u \cdot v = u^T v = \sum_{i=1}^n u_i v_i$
* **Dot Product (Geometric):** $u \cdot v = \|u\|_2 \|v\|_2 \cos\theta$
* **Cosine Similarity (used in NLP embeddings & vector search):**
  $$\text{sim}(u, v) = \cos\theta = \frac{u \cdot v}{\|u\|_2 \|v\|_2} \in [-1, 1]$$
* **Vector Norms:**
  * **$L_1$ (Manhattan / Lasso):** $\|x\|_1 = \sum_{i=1}^n |x_i|$
  * **$L_2$ (Euclidean / Ridge):** $\|x\|_2 = \sqrt{\sum_{i=1}^n x_i^2} = \sqrt{x^T x}$
  * **$L_\infty$ (Max Norm):** $\|x\|_\infty = \max_i |x_i|$

---

## 2. Matrix Properties & Fundamental Subspaces

For $A \in \mathbb{R}^{m \times n}$:
* **Matrix Multiplication:** $(AB)_{ij} = \sum_{k=1}^n A_{ik} B_{kj}$. Note: $(AB)^T = B^T A^T$ and $(AB)^{-1} = B^{-1} A^{-1}$.
* **Trace:** $\text{Tr}(A) = \sum_{i=1}^n A_{ii} = \sum_{i=1}^n \lambda_i$ (sum of eigenvalues). Also $\text{Tr}(AB) = \text{Tr}(BA)$.
* **Determinant:** $\det(A) = \prod_{i=1}^n \lambda_i$ (product of eigenvalues; measures volume scaling factor).
* **Rank-Nullity Theorem:**
  $$\text{rank}(A) + \text{dim}(\text{Null}(A)) = n \quad (\text{number of columns})$$
* **Invertibility (Equivalent Conditions for $n \times n$ matrix $A$):**
  1. $A$ is invertible ($A^{-1}$ exists).
  2. $\det(A) \neq 0$ (no zero eigenvalues).
  3. $\text{rank}(A) = n$ (columns and rows are linearly independent).
  4. $Ax = 0$ has only the trivial solution $x = 0$.

---

## 3. Eigenvalues, Eigenvectors & Decompositions

### Eigendecomposition ($n \times n$ square matrix)
* **Definition:** $Av = \lambda v$ where $v \neq 0$ is an eigenvector and $\lambda$ is its eigenvalue.
* **Characteristic Equation:** $\det(A - \lambda I) = 0$.
* **Diagonalization:** $A = P \Lambda P^{-1} \implies A^k = P \Lambda^k P^{-1}$ (fast computation of matrix powers for Markov chains & recurrences!).
* **Spectral Theorem:** Every real symmetric matrix ($A = A^T$) has purely real eigenvalues and orthogonal eigenvectors:
  $$A = Q \Lambda Q^T \quad \text{where } Q^T Q = I$$

### Singular Value Decomposition (SVD — works for ANY $m \times n$ matrix!)
$$A = U \Sigma V^T$$
* $U \in \mathbb{R}^{m \times m}$: Orthogonal matrix (columns are eigenvectors of $AA^T$, "left singular vectors").
* $\Sigma \in \mathbb{R}^{m \times n}$: Diagonal matrix of non-negative singular values $\sigma_1 \ge \sigma_2 \ge \dots \ge 0$ where $\sigma_i = \sqrt{\lambda_i(A^T A)}$.
* $V \in \mathbb{R}^{n \times n}$: Orthogonal matrix (columns are eigenvectors of $A^T A$, "right singular vectors").
* **Eckart-Young Theorem (Low-Rank Approximation):** Truncating SVD to the top $k$ singular values gives the optimal rank-$k$ approximation of $A$ (used in image compression, LoRA fine-tuning of LLMs, and PCA).

---

## 4. 2D & 3D Graphics Transformation Matrices

* **2D Counter-Clockwise Rotation by angle $\theta$:**
  $$R(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$$
* **2D Homogeneous Transformation (Rotation + Scaling + Translation $(t_x, t_y)$):**
  $$\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} = \begin{bmatrix} s_x \cos\theta & -s_y \sin\theta & t_x \\ s_x \sin\theta & s_y \cos\theta & t_y \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}$$
