---
tags:
  - mathematics
  - linear_algebra
  - vector
  - norm
  - p_norm
  - L1_norm
  - L2_norm
  - manhattan_distance
  - euclidean_distance
  - concept
aliases:
  - Vector Norm
  - Lp Norm
  - L1 Norm
  - L2 Norm
  - L-infinity Norm
  - Manhattan Norm
  - Euclidean Norm
  - Max Norm
related:
  - "[[Vector]]"
  - "[[Dot_Product]]"
  - "[[Distance_Metrics]]"
worksheet:
  - WS_Math_Foundations_1
date_created: 2025-05-30
---
# p-norm (Vector Norms)

## Definition
In linear algebra, a **norm** is a function that assigns a strictly positive length or size to each [[Vector|vector]] in a vector space—except for the zero vector, which is assigned a length of zero. A norm on a vector space $V$ is a function $\| \cdot \|: V \to \mathbb{R}$ that satisfies the following properties for all scalars $k$ and all vectors $\mathbf{u}, \mathbf{v} \in V$:
1.  $\|\mathbf{v}\| \ge 0$ (Non-negativity)
2.  $\|\mathbf{v}\| = 0$ if and only if $\mathbf{v} = \mathbf{0}$ (zero vector) (Definiteness)
3.  $\|k\mathbf{v}\| = |k| \|\mathbf{v}\|$ (Absolute homogeneity or Absolute scalability)
4.  $\|\mathbf{u} + \mathbf{v}\| \le \|\mathbf{u}\| + \|\mathbf{v}\|$ (Triangle inequality or Subadditivity)

The **$L_p$-norm** (or **p-norm**) of a vector $\mathbf{x} = (x_1, x_2, \dots, x_n)$ is a specific class of vector norms defined as:
$$ \|\mathbf{x}\|_p = \left( \sum_{i=1}^{n} |x_i|^p \right)^{1/p} $$
for a real number $p \ge 1$.

## Common p-norms

>[!question] What are the common names for the 1-norm, 2-norm, and ∞-norm? Why are they called like that?

[list2tab|#Common p-norms]
- **L1-norm ($p=1$)**
    - **Formula:** $\|\mathbf{x}\|_1 = \sum_{i=1}^{n} |x_i| = |x_1| + |x_2| + \dots + |x_n|$
    - **Common Names:**
        - **Manhattan Norm:** This name comes from the grid-like path a taxi would take in Manhattan (where streets are often in a grid). The L1 distance between two points $(x_1, y_1)$ and $(x_2, y_2)$ is $|x_1-x_2| + |y_1-y_2|$, which is the distance traveled along grid lines.
        - **Taxicab Norm:** Similar to Manhattan norm.
        - Sum Absolute Deviations (SAD) is related when comparing to a zero vector or between two vectors.
    - **Why these names?** They reflect the idea of summing absolute differences along axes, akin to moving along a city grid.
    - **Use Cases:** Promotes sparsity in machine learning (e.g., L1 regularization like Lasso), robust to outliers in some contexts, feature selection.

- **L2-norm ($p=2$)**
    - **Formula:** $\|\mathbf{x}\|_2 = \sqrt{\sum_{i=1}^{n} |x_i|^2} = \sqrt{x_1^2 + x_2^2 + \dots + x_n^2}$
    - **Common Names:**
        - **Euclidean Norm:** This is the ordinary "straight-line" distance from the origin to the point represented by the vector in Euclidean space. It's derived from the Pythagorean theorem.
        - (Sometimes just called "the norm" or "magnitude" if context is clear).
    - **Why these names?** It corresponds to our intuitive notion of distance in Euclidean geometry. It's also related to the [[Dot_Product|dot product]]: $\|\mathbf{x}\|_2 = \sqrt{\mathbf{x} \cdot \mathbf{x}}$.
    - **Use Cases:** Most common norm, used in many geometric calculations, distance measurements (Euclidean distance), L2 regularization (Ridge regression, weight decay), least squares.

- **L$\infty$-norm ($p \to \infty$)**
    - **Formula:** $\|\mathbf{x}\|_\infty = \max_{i} |x_i| = \max(|x_1|, |x_2|, \dots, |x_n|)$
    - **Common Names:**
        - **Maximum Norm (Max Norm):** This name directly describes what it calculates – the maximum absolute value among the vector's components.
        - **Uniform Norm:** Related to the concept of uniform convergence.
        - Chebyshev Norm (related to Chebyshev distance).
    - **Why these names?** As $p$ approaches infinity in the $L_p$ formula, the term with the largest absolute value $|x_i|$ dominates the sum, leading to the maximum absolute component.
      Consider $(\sum |x_i|^p)^{1/p}$. Let $|x_k|$ be $\max_i |x_i|$. Then $\|\mathbf{x}\|_p = |x_k| (\sum (|x_i|/|x_k|)^p)^{1/p}$. As $p \to \infty$, $(|x_i|/|x_k|)^p \to 0$ if $|x_i| < |x_k|$, and $\to 1$ if $|x_i| = |x_k|$. If there's a unique maximum, the sum inside parenthesis approaches 1.
    - **Use Cases:** Useful when the largest component is of primary interest, error analysis (maximum error), some types of regularization, feature scaling to a max value.

- **L0-norm (Pseudo-norm)**
    - **Definition:** Although not strictly a norm (it violates the homogeneity property $\|k\mathbf{v}\| = |k| \|\mathbf{v}\|$ for $k \neq \pm 1$), the "L0-norm" is often used to denote the number of non-zero elements in a vector.
    - **Formula:** $\|\mathbf{x}\|_0 = \sum_{i=1}^{n} \mathbb{I}(x_i \neq 0)$, where $\mathbb{I}$ is the indicator function.
    - **Use Cases:** Sparsity measure in compressed sensing and feature selection. Computationally hard to optimize directly, often approximated by L1-norm.

## Geometric Interpretation (Unit Circles in 2D)
The set of all vectors $\mathbf{x}$ such that $\|\mathbf{x}\|_p = 1$ forms the "unit circle" for that norm.
- **L1-norm:** A diamond (rotated square).
- **L2-norm:** A standard circle.
- **L$\infty$-norm:** A square aligned with axes.

```mermaid
graph TD
    subgraph L1_Norm_Unit_Circle ["L1 Unit Circle: ||x||_1 = 1"]
        P1((1,0)) --- P2((0,1)) --- P3((-1,0)) --- P4((0,-1)) --- P1
    end
    subgraph L2_Norm_Unit_Circle ["L2 Unit Circle: ||x||_2 = 1"]
        C[Circle center 0,0 radius 1]
    end
    subgraph Linf_Norm_Unit_Circle ["L-inf Unit Circle: ||x||_inf = 1"]
        S1((1,1)) --- S2((-1,1)) --- S3((-1,-1)) --- S4((1,-1)) --- S1
    end

    style P1 fill:#afa
    style P2 fill:#afa
    style P3 fill:#afa
    style P4 fill:#afa
    style C fill:#aaf,stroke:#333,stroke-width:4px,r:50
    style S1 fill:#faa
    style S2 fill:#faa
    style S3 fill:#faa
    style S4 fill:#faa
```

## Applications
- **Distance Metrics:** The norm of the difference between two vectors, $\|\mathbf{a} - \mathbf{b}\|_p$, defines the $L_p$ distance.
- **Regularization in Machine Learning:**
    - L1 regularization (Lasso) adds $\|\mathbf{w}\|_1$ to the loss function, promoting sparse weight vectors (feature selection).
    - L2 regularization (Ridge/Weight Decay) adds $\|\mathbf{w}\|_2^2$ to the loss function, penalizing large weights and preventing overfitting.
- **Error Measurement:** Different norms can be used to measure the error between a predicted vector and a true vector.
- **Signal Processing & Image Analysis:** Various norms are used for noise reduction and feature extraction.

---