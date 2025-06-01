---
tags:
  - mathematics
  - calculus
  - matrix_calculus
  - hessian
  - second_derivative
  - optimization
  - concept
aliases:
  - Hessian Matrix
related:
  - "[[Matrix_Calculus]]"
  - "[[Gradient]]"
  - "[[Jacobian]]"
  - "[[Calculus_Derivatives]]"
  - "[[Calculus_Optimization]]"
  - "[[Convex_Optimization]]"
worksheet:
  - WS_Math_Foundations_1
date_created: 2025-05-30
---
# Hessian Matrix

## Definition
In multivariable calculus, the **Hessian matrix** (or simply the **Hessian**) of a scalar-valued function $f(\mathbf{x})$ of $n$ variables $\mathbf{x} = (x_1, x_2, \dots, x_n)$ is the square $n \times n$ [[Matrix|matrix]] of its second-order partial [[Calculus_Derivatives|derivatives]].

If all second partial derivatives of $f$ exist and are continuous, the Hessian matrix $\mathbf{H}$ (or $\nabla^2 f$) is defined as:
$$ \mathbf{H}_{ij} = \frac{\partial^2 f}{\partial x_i \partial x_j} $$
So, the Hessian matrix looks like this:
$$ \mathbf{H} = \nabla^2 f(\mathbf{x}) =
\begin{pmatrix}
\frac{\partial^2 f}{\partial x_1^2} & \frac{\partial^2 f}{\partial x_1 \partial x_2} & \dots & \frac{\partial^2 f}{\partial x_1 \partial x_n} \\
\frac{\partial^2 f}{\partial x_2 \partial x_1} & \frac{\partial^2 f}{\partial x_2^2} & \dots & \frac{\partial^2 f}{\partial x_2 \partial x_n} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial^2 f}{\partial x_n \partial x_1} & \frac{\partial^2 f}{\partial x_n \partial x_2} & \dots & \frac{\partial^2 f}{\partial x_n^2}
\end{pmatrix}
$$

Under the condition of continuity of second partial derivatives (Clairaut's theorem on equality of mixed partials), the Hessian matrix is a **symmetric matrix**, i.e., $\frac{\partial^2 f}{\partial x_i \partial x_j} = \frac{\partial^2 f}{\partial x_j \partial x_i}$, so $\mathbf{H} = \mathbf{H}^T$.

The Hessian can also be seen as the [[Jacobian|Jacobian matrix]] of the [[Gradient|gradient]] vector $\nabla f$:
$$ \mathbf{H}(f)(\mathbf{x}) = \mathbf{J}(\nabla f)(\mathbf{x}) $$
(Assuming gradient is a column vector, and Jacobian $J_{ij} = \frac{\partial (\nabla f)_i}{\partial x_j}$).

## Role in Optimization
The Hessian matrix plays a crucial role in [[Calculus_Optimization|optimization]] problems for multivariable functions, similar to how the second derivative is used in single-variable calculus:

1.  **Second-Order Test for Local Extrema:**
    Let $\mathbf{x}_0$ be a critical point of $f$ (i.e., $\nabla f(\mathbf{x}_0) = \mathbf{0}$). Let $\mathbf{H}_0$ be the Hessian evaluated at $\mathbf{x}_0$.
    - If $\mathbf{H}_0$ is **positive definite** (all its [[Eigenvalues_Eigenvectors|eigenvalues]] are positive), then $f$ has a local minimum at $\mathbf{x}_0$.
    - If $\mathbf{H}_0$ is **negative definite** (all its eigenvalues are negative), then $f$ has a local maximum at $\mathbf{x}_0$.
    - If $\mathbf{H}_0$ has both positive and negative eigenvalues (indefinite), then $\mathbf{x}_0$ is a **saddle point**.
    - If $\mathbf{H}_0$ is singular (at least one eigenvalue is zero) and semi-definite (but not definite), the test is inconclusive.

2.  **Convexity:**
    For a twice-differentiable function $f$ defined on a convex set:
    - $f$ is a [[Convex_Optimization|convex function]] if and only if its Hessian matrix $\mathbf{H}$ is positive semi-definite for all $\mathbf{x}$ in the domain.
    - $f$ is a strictly convex function if its Hessian matrix $\mathbf{H}$ is positive definite for all $\mathbf{x}$ in the domain.
    - Similar conditions apply for concave functions (Hessian being negative semi-definite or negative definite).
    Convexity is highly desirable in optimization because any local minimum of a convex function is also a global minimum.

3.  **Newton's Method for Optimization:**
    Newton's method is a second-order optimization algorithm that uses the Hessian matrix to find the minimum (or maximum) of a function. The update rule is:
    $$ \mathbf{x}_{k+1} = \mathbf{x}_k - [\mathbf{H}(f)(\mathbf{x}_k)]^{-1} \nabla f(\mathbf{x}_k) $$
    This method converges quickly near the optimum if the function is well-behaved and the Hessian is positive definite, but computing and inverting the Hessian can be computationally expensive for high-dimensional problems.

## Example
Let $f(x, y) = x^2 + y^2 + xy$.
Partial derivatives:
- $\frac{\partial f}{\partial x} = 2x + y$
- $\frac{\partial f}{\partial y} = 2y + x$

Second-order partial derivatives:
- $\frac{\partial^2 f}{\partial x^2} = 2$
- $\frac{\partial^2 f}{\partial y^2} = 2$
- $\frac{\partial^2 f}{\partial x \partial y} = 1$
- $\frac{\partial^2 f}{\partial y \partial x} = 1$

The Hessian matrix is:
$$ \mathbf{H} = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} $$
To check for definiteness, we can look at eigenvalues or leading principal minors.
Determinant: $(2)(2) - (1)(1) = 4 - 1 = 3 > 0$.
Trace (sum of diagonal elements, also sum of eigenvalues): $2+2 = 4 > 0$.
Since the determinant is positive and the first leading principal minor ($H_{11}=2$) is positive, the matrix is positive definite.
Thus, $f(x,y)$ is a convex function.
The critical point is where $\nabla f = \mathbf{0}$:
$2x+y=0$ and $x+2y=0$. Solving this system gives $x=0, y=0$.
Since the Hessian is positive definite everywhere, the point $(0,0)$ is a local (and global) minimum.

## Computational Cost
For a function of $n$ variables, the Hessian matrix has $n^2$ elements. Computing all these second derivatives can be expensive. For very high-dimensional problems (common in deep learning where $n$ can be millions or billions), explicitly forming and storing the Hessian is often infeasible. Quasi-Newton methods (like L-BFGS) approximate the Hessian or its inverse.

---