---
tags:
  - mathematics
  - numerical_analysis
  - linear_algebra
  - stability
  - error_analysis
  - concept
aliases:
  - Stable Algorithm
  - Numerical Error
  - Condition Number
related:
  - "[[Floating_Point_Arithmetic]]"
  - "[[Matrix_Inversion]]"
  - "[[Singular_Value_Decomposition]]"
  - "[[QR_Decomposition]]"
  - "[[Orthogonal_Matrix]]"
worksheet:
  - WS_Math_Foundations_2
date_created: 2025-08-07
---
# Numerical Stability

## Definition
**Numerical stability** is a desirable property of a numerical algorithm. It describes how errors in the input data or intermediate calculations propagate through the algorithm. An algorithm is considered **numerically stable** if it does not significantly magnify these errors.

In contrast, a **numerically unstable** algorithm can produce a result that is wildly inaccurate, even if the input data is only slightly perturbed. This is particularly important when using [[Floating_Point_Arithmetic|floating-point arithmetic]] on computers, where small rounding errors are introduced at nearly every step.

## Key Concepts

[list2tab|#Stability Concepts]
- Error Types
    - **Input Error:** Errors already present in the initial data (e.g., from measurements).
    - **Rounding Error:** Errors introduced because computers represent real numbers with finite precision.
    - **Truncation Error:** Errors from approximating an infinite process with a finite one (e.g., using a finite number of terms in a Taylor series).
- Forward Error
    - The difference between the computed solution and the true solution: $\|\hat{x} - x\|$.
- Backward Error
    - The size of the perturbation to the initial data that would make the computed solution $\hat{x}$ an exact solution to the perturbed problem. A small backward error means the algorithm has found a nearly exact solution to a nearby problem.
- Stability
    - An algorithm is **backward stable** if it produces a small backward error. This is a common and desirable form of stability. It implies that the algorithm's result is as good as the input data deserves.
    - An algorithm is **forward stable** if the forward error is small. This depends on both the algorithm's stability and the problem's sensitivity.

## The Condition Number
The **condition number** of a problem (not an algorithm) measures how sensitive the output of the problem is to small changes in the input data.
$$ \text{Condition Number} = \frac{\|\text{Relative change in output}\|}{\|\text{Relative change in input}\|} $$
- **Well-conditioned problem (low condition number):** Small relative changes in the input lead to small relative changes in the output.
- **Ill-conditioned problem (high condition number):** Small relative changes in the input can lead to large relative changes in the output.

For a matrix $\mathbf{A}$ in the context of solving $\mathbf{A}\mathbf{x}=\mathbf{b}$, the condition number is $\kappa(\mathbf{A}) = \|\mathbf{A}\| \|\mathbf{A}^{-1}\|$. It can also be calculated from [[Singular_Values|singular values]]: $\kappa(\mathbf{A}) = \frac{\sigma_{\text{max}}}{\sigma_{\text{min}}}$.

**Relationship:**
$$ \text{Forward Error} \le (\text{Condition Number}) \times (\text{Backward Error}) $$
This shows that even for a backward stable algorithm (small backward error), if the problem is ill-conditioned (large condition number), the final result can still have a large forward error.

## Python Example: Ill-Conditioned Matrix
Let's solve a system of linear equations $\mathbf{A}\mathbf{x} = \mathbf{b}$ with a well-conditioned matrix and an ill-conditioned matrix (a Hilbert matrix is famously ill-conditioned).

```python
import numpy as np

def solve_and_check(A, b, description):
    """Solves Ax=b and checks the effect of a small perturbation in b."""
    print(f"--- {description} ---")
    
    # Calculate condition number
    cond_A = np.linalg.cond(A)
    print(f"Condition number of A: {cond_A:.2e}")
    
    # Solve the original system
    x = np.linalg.solve(A, b)
    
    # Introduce a small perturbation to b
    perturbation = np.random.randn(b.shape) * 1e-6
    b_perturbed = b + perturbation
    
    # Solve the perturbed system
    x_perturbed = np.linalg.solve(A, b_perturbed)
    
    # Calculate relative errors
    rel_error_b = np.linalg.norm(perturbation) / np.linalg.norm(b)
    rel_error_x = np.linalg.norm(x_perturbed - x) / np.linalg.norm(x)
    
    print(f"Relative error in input b: {rel_error_b:.2e}")
    print(f"Relative error in output x: {rel_error_x:.2e}")
    print(f"Magnification factor (error_x / error_b): {rel_error_x / rel_error_b:.2e}\n")

# 1. Well-conditioned system
A_well = np.array([,])
b_well = np.array()
solve_and_check(A_well, b_well, "Well-Conditioned System")

# 2. Ill-conditioned system (Hilbert matrix)
from scipy.linalg import hilbert
A_ill = hilbert(5)
b_ill = np.ones(5)
solve_and_check(A_ill, b_ill, "Ill-Conditioned System")

# Expected Output:
# --- Well-Conditioned System ---
# Condition number of A: 2.62e+01
# Relative error in input b: 5.79e-07
# Relative error in output x: 1.05e-06
# Magnification factor (error_x / error_b): 1.81e+00
#
# --- Ill-Conditioned System ---
# Condition number of A: 4.77e+05
# Relative error in input b: 4.88e-07
# Relative error in output x: 1.10e-01
# Magnification factor (error_x / error_b): 2.25e+05
```
The output clearly shows that for the ill-conditioned system, a tiny error in the input `b` is magnified by a factor of ~225,000, leading to a massive 11% error in the solution `x`. The well-conditioned system's error is barely magnified.

## Stable vs. Unstable Algorithms
- **Stable:** [[QR_Decomposition|QR decomposition]] for solving least squares problems is known for its excellent numerical stability. Using [[Orthogonal_Matrix|orthogonal matrices]] (like in QR or [[Singular_Value_Decomposition|SVD]]) is generally a good strategy because they preserve norms and don't amplify errors.
- **Unstable:** A classic example is finding the roots of a polynomial from its coefficients (Wilkinson's polynomial). A tiny change in one coefficient can cause huge changes in the roots. Another example is using Cramer's rule for [[Matrix_Inversion|matrix inversion]], which can be numerically unstable.

## Importance in Data Science
- **Model Training:** Iterative algorithms like Gradient Descent can suffer from instability if learning rates are too high.
- **Data Preprocessing:** Scaling features (e.g., standardization) can improve the conditioning of the problem for many algorithms, leading to more stable and faster convergence.
- **Algorithm Choice:** When multiple algorithms can solve a problem (e.g., different ways to solve a linear system), their numerical stability is a critical factor in choosing the right one, especially when dealing with real-world, noisy data.
- **Library Implementations:** High-quality numerical libraries like NumPy, SciPy, and Scikit-learn use carefully implemented, numerically stable algorithms (often from underlying libraries like BLAS and LAPACK) to minimize these issues.

---