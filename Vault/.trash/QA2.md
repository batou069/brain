*Calculus**
---

**1. Derivatives**
*   **Concise explanation:** A derivative measures the instantaneous rate of change of a function with respect to one of its variables. It represents the slope of the tangent line to the function's graph at a specific point.
*   **Illustrative examples:** If $f(x) = x^2$, its derivative $f'(x) = 2x$. At $x=3$, the slope is $2 \times 3 = 6$.
*   **Syntax and real example (Notation):** Leibniz notation: $\frac{df}{dx}$. Lagrange notation: $f'(x)$.
*   **Exceptions, variations, and alternative approaches:** Partial derivatives ($\frac{\partial f}{\partial x}$) for functions of multiple variables. Higher-order derivatives ($f''(x)$, $\frac{d^2f}{dx^2}$).
*   **Key takeaway:** Measures rate of change or slope.

**2. Integrals**
*   **Concise explanation:** An integral can be interpreted as the area under the curve of a function. Indefinite integrals find the antiderivative of a function, while definite integrals calculate the net area over a specific interval.
*   **Illustrative examples:** The indefinite integral of $f(x) = 2x$ is $F(x) = x^2 + C$. The definite integral $\int_0^2 x^2 dx = \frac{x^3}{3} \Big|_0^2 = \frac{8}{3}$.
*   **Syntax and real example (Notation):** Indefinite: $\int f(x) dx$. Definite: $\int_a^b f(x) dx$.
*   **Exceptions, variations, and alternative approaches:** Multiple integrals (for volumes), line integrals, surface integrals. Numerical integration methods (e.g., Riemann sums, trapezoidal rule) approximate integrals.
*   **Key takeaway:** Represents accumulated quantity or area.

**3. Optimization**
*   **Concise explanation:** The process of finding the input values (arguments) that result in the minimum or maximum output (value) of a function, possibly subject to constraints.
*   **Illustrative examples:** Finding the dimensions of a rectangular fence that maximize area for a fixed perimeter. Training a machine learning model by minimizing a loss function.
*   **Syntax and real example (Conceptual):** For $f(x)=x^2-4x+5$, find $x$ where $f'(x)=2x-4=0 \Rightarrow x=2$ (minimum).
*   **Exceptions, variations, and alternative approaches:** Constrained vs. unconstrained optimization. Convex vs. non-convex optimization. Algorithms like Gradient Descent, Newton's method, Linear Programming.
*   **Key takeaway:** Finding the best possible solution (min/max).

---
**Vectors And Matrices**
---

**1. Row vector vs. column vector**
*   **Concise explanation:** A row vector is a $1 \times n$ matrix (one row, n columns). A column vector is an $n \times 1$ matrix (n rows, one column).
*   **Illustrative examples:** Row vector: $[1, 2, 3]$. Column vector: $\begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}$.
*   **Syntax and real example (Notation):** Row: $\mathbf{v} = [v_1, v_2, \dots, v_n]$. Column: $\mathbf{u} = \begin{pmatrix} u_1 \\ \vdots \\ u_n \end{pmatrix} = [u_1, \dots, u_n]^T$.
*   **Exceptions, variations, and alternative approaches:** The distinction is crucial for matrix multiplication. By default, in many texts, "vector" implies a column vector.
*   **Key takeaway:** Orientation of a 1D array of numbers.

**2. Dot product/inner product**
*   **Concise explanation:** An algebraic operation that takes two equal-length sequences of numbers (usually vectors) and returns a single scalar. It's the sum of the products of corresponding entries.
*   **Illustrative examples:** For $\mathbf{a} = [1, 2, 3]$ and $\mathbf{b} = [4, 5, 6]$, $\mathbf{a} \cdot \mathbf{b} = (1 \times 4) + (2 \times 5) + (3 \times 6) = 4 + 10 + 18 = 32$.
*   **Syntax and real example (Formula):** $\mathbf{a} \cdot \mathbf{b} = \sum_{i=1}^n a_i b_i = ||\mathbf{a}|| \ ||\mathbf{b}|| \cos(\theta)$.
*   **Exceptions, variations, and alternative approaches:** For complex vectors, the definition involves a conjugate. Inner product is a more general concept.
*   **Key takeaway:** Measures similarity or projection; related to the angle between vectors.

**3. Cosine similarity**
*   **Concise explanation:** A measure of similarity between two non-zero vectors of an inner product space. It is the cosine of the angle between them, calculated from their dot product and magnitudes.
*   **Illustrative examples:** Used in text analysis to measure document similarity (vectors representing word counts). If vectors point in the same direction, similarity is 1; opposite, -1; orthogonal, 0.
*   **Syntax and real example (Formula):** Cosine Similarity$(\mathbf{a}, \mathbf{b}) = \frac{\mathbf{a} \cdot \mathbf{b}}{||\mathbf{a}|| \ ||\mathbf{b}||} = \frac{\sum_{i=1}^n a_i b_i}{\sqrt{\sum_{i=1}^n a_i^2} \sqrt{\sum_{i=1}^n b_i^2}}$.
*   **Exceptions, variations, and alternative approaches:** Ranges from -1 to 1. Sensitive to orientation, not magnitude.
*   **Key takeaway:** Normalized measure of vector orientation similarity.

**4. Matrix product**
*   **Concise explanation:** An operation producing a single matrix from two matrices. For product $C = AB$, element $C_{ij}$ is the dot product of the $i$-th row of $A$ and the $j$-th column of $B$. Number of columns in $A$ must equal number of rows in $B$.
*   **Illustrative examples:** If $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ and $B = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}$, then $AB = \begin{pmatrix} 1\cdot5+2\cdot7 & 1\cdot6+2\cdot8 \\ 3\cdot5+4\cdot7 & 3\cdot6+4\cdot8 \end{pmatrix} = \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}$.
*   **Syntax and real example (Dimensions):** If $A$ is $m \times k$ and $B$ is $k \times n$, then $AB$ is $m \times n$.
*   **Exceptions, variations, and alternative approaches:** Not commutative ($AB \neq BA$ generally). Associative ($(AB)C = A(BC)$).
*   **Key takeaway:** Combines matrices, representing composite linear transformations.

**5. Transformation matrix**
*   **Concise explanation:** A matrix used to apply a linear transformation (e.g., rotation, scaling, shearing, reflection) to vectors in a vector space. A vector $\mathbf{v}$ is transformed to $\mathbf{v}'$ by $M\mathbf{v} = \mathbf{v}'$.
*   **Illustrative examples:** Rotation matrix in 2D: $R(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$. Scaling matrix: $S = \begin{pmatrix} s_x & 0 \\ 0 & s_y \end{pmatrix}$.
*   **Syntax and real example (Application):** $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} -y \\ x \end{pmatrix}$ (90-degree counter-clockwise rotation).
*   **Exceptions, variations, and alternative approaches:** Affine transformations (including translation) can be represented using homogeneous coordinates and $(n+1) \times (n+1)$ matrices.
*   **Key takeaway:** Matrix that systematically changes geometric vectors.

**6. Element-wise functions**
*   **Concise explanation:** A function that operates on each element of a matrix or vector independently, producing a new matrix/vector of the same shape where each element is the result of applying the function to the corresponding input element.
*   **Illustrative examples:** If $A = \begin{pmatrix} 1 & 4 \\ 9 & 16 \end{pmatrix}$ and $f(x) = \sqrt{x}$, then $f(A) = \begin{pmatrix} \sqrt{1} & \sqrt{4} \\ \sqrt{9} & \sqrt{16} \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$. Sigmoid or ReLU applied to a layer's output in neural networks.
*   **Syntax and real example (Notation):** Often implicit from context, e.g., $\sigma(Z)$ where $\sigma$ is sigmoid and $Z$ is a matrix.
*   **Exceptions, variations, and alternative approaches:** Different from matrix functions like matrix exponential $e^A$.
*   **Key takeaway:** Applies a scalar function to every entry of an array.

**7. Eigenvalues / Singular Values**
*   **Eigenvalues ($\lambda$):** Scalars associated with a square matrix $A$ such that for a non-zero vector $\mathbf{v}$ (eigenvector), $A\mathbf{v} = \lambda\mathbf{v}$. Eigenvectors are only scaled by the transformation $A$.
    *   Example: For $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$, $\lambda_1=3$ with $\mathbf{v}_1=\begin{pmatrix} 1 \\ 1 \end{pmatrix}$ ($A\mathbf{v}_1 = \begin{pmatrix} 3 \\ 3 \end{pmatrix} = 3\mathbf{v}_1$).
*   **Singular Values ($\sigma$):** Non-negative scalars associated with any $m \times n$ matrix $A$. They are the square roots of the eigenvalues of $A^T A$ (or $A A^T$). Used in Singular Value Decomposition (SVD).
    *   Example: Conceptually, in SVD $A = U\Sigma V^T$, $\Sigma$ is a diagonal matrix of singular values.
*   **Key takeaway:** Eigenvalues describe scaling factors for directions unchanged by a square matrix; Singular values describe scaling factors in principal component directions for any matrix.

**8. Eigenvectors**
*   **Concise explanation:** A non-zero vector $\mathbf{v}$ that, when multiplied by a given square matrix $A$, results in a scalar multiple of itself ($\lambda\mathbf{v}$). The direction of an eigenvector is unchanged by the linear transformation $A$.
*   **Illustrative examples:** For $A = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}$, $\mathbf{v}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$ is an eigenvector with eigenvalue $\lambda_1=2$, because $A\mathbf{v}_1 = \begin{pmatrix} 2 \\ 0 \end{pmatrix} = 2\mathbf{v}_1$.
*   **Syntax and real example (Defining equation):** $A\mathbf{v} = \lambda\mathbf{v}$. Eigenvectors are found by solving $(A - \lambda I)\mathbf{v} = \mathbf{0}$.
*   **Exceptions, variations, and alternative approaches:** Eigenvectors are not unique; any scalar multiple is also an eigenvector. A matrix may not have a full set of linearly independent eigenvectors.
*   **Key takeaway:** Directions that are only scaled by a linear transformation.

**9. p-norm**
*   **Concise explanation:** A function that assigns a strictly positive length or size to each vector in a vector space (except for the zero vector). The p-norm ($L_p$-norm) is a specific class of vector norms.
*   **Illustrative examples:**
    *   $L_1$-norm (Manhattan norm): $||\mathbf{x}||_1 = \sum_i |x_i|$.
    *   $L_2$-norm (Euclidean norm): $||\mathbf{x}||_2 = \sqrt{\sum_i x_i^2}$.
    *   $L_\infty$-norm (Max norm): $||\mathbf{x}||_\infty = \max_i |x_i|$.
*   **Syntax and real example (General Formula):** For a vector $\mathbf{x} = (x_1, \dots, x_n)$, the p-norm is $||\mathbf{x}||_p = (\sum_{i=1}^n |x_i|^p)^{1/p}$ for $p \ge 1$.
*   **Exceptions, variations, and alternative approaches:** $L_0$-"norm" (counts non-zero elements, not truly a norm). Matrix norms (e.g., Frobenius norm).
*   **Key takeaway:** Generalizes the concept of vector length.

**10. Hadamard product**
*   **Concise explanation:** An element-wise product of two matrices (or vectors) of the same dimensions. Each element $(C)_{ij}$ of the resulting matrix $C$ is the product of the corresponding elements $(A)_{ij}$ and $(B)_{ij}$.
*   **Illustrative examples:** If $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ and $B = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}$, then $A \circ B = \begin{pmatrix} 1\cdot5 & 2\cdot6 \\ 3\cdot7 & 4\cdot8 \end{pmatrix} = \begin{pmatrix} 5 & 12 \\ 21 & 32 \end{pmatrix}$.
*   **Syntax and real example (Notation):** $A \circ B$ or $A \odot B$. In NumPy/Python, it's often the `*` operator for `ndarray`s.
*   **Exceptions, variations, and alternative approaches:** Distinct from the standard matrix product.
*   **Key takeaway:** Element-by-element multiplication.

**11. Matrix calculus**
*   **Concise explanation:** A specialized notation and collection of rules for differentiating functions involving matrices and vectors. It extends single-variable calculus to higher dimensions.
*   **Illustrative examples (Focus Combinations):**
    *   **Scalar by vector (Gradient):** $\nabla_{\mathbf{x}} f(\mathbf{x})$ for scalar $f$ and vector $\mathbf{x}$. E.g., if $f(\mathbf{x}) = \mathbf{a}^T \mathbf{x}$, then $\nabla_{\mathbf{x}} f(\mathbf{x}) = \mathbf{a}$.
    *   **Scalar by matrix:** $\frac{\partial f(X)}{\partial X}$ for scalar $f$ and matrix $X$. E.g., if $f(X) = \text{tr}(AX)$, then $\frac{\partial f(X)}{\partial X} = A^T$.
    *   **Vector by vector (Jacobian):** $\frac{\partial \mathbf{f}(\mathbf{x})}{\partial \mathbf{x}}$ for vector function $\mathbf{f}$ and vector $\mathbf{x}$. (See Jacobian keyword).
*   **Syntax and real example (Notation):** Various notations exist (numerator layout vs. denominator layout). Key is understanding input and output shapes.
*   **Exceptions, variations, and alternative approaches:** Complex rules for different layouts and operations like trace, determinant.
*   **Key takeaway:** Rules for differentiating expressions containing matrices/vectors, essential for ML optimization.

**12. Hessian**
*   **Concise explanation:** For a scalar-valued function of multiple variables $f(\mathbf{x})$, the Hessian matrix is the square matrix of its second-order partial derivatives.
*   **Illustrative examples:** For $f(x,y) = x^2 + xy + y^2$, $H = \begin{pmatrix} \frac{\partial^2 f}{\partial x^2} & \frac{\partial^2 f}{\partial x \partial y} \\ \frac{\partial^2 f}{\partial y \partial x} & \frac{\partial^2 f}{\partial y^2} \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$.
*   **Syntax and real example (Formula):** $(H(f))_{ij}(\mathbf{x}) = \frac{\partial^2 f}{\partial x_i \partial x_j}(\mathbf{x})$.
*   **Exceptions, variations, and alternative approaches:** The Hessian is symmetric if second partial derivatives are continuous (Clairaut's theorem). Used in optimization (e.g., Newton's method) to determine concavity/convexity.
*   **Key takeaway:** Matrix of second derivatives, describes local curvature.

**13. Jacobian**
*   **Concise explanation:** For a vector-valued function $\mathbf{f}: \mathbb{R}^n \to \mathbb{R}^m$, the Jacobian matrix $J$ is the matrix of all its first-order partial derivatives. If $m=1$, it's the gradient.
*   **Illustrative examples:** If $\mathbf{f}(x,y) = \begin{pmatrix} x^2y \\ 5x + \sin y \end{pmatrix}$, then $J = \begin{pmatrix} \frac{\partial f_1}{\partial x} & \frac{\partial f_1}{\partial y} \\ \frac{\partial f_2}{\partial x} & \frac{\partial f_2}{\partial y} \end{pmatrix} = \begin{pmatrix} 2xy & x^2 \\ 5 & \cos y \end{pmatrix}$.
*   **Syntax and real example (Formula):** $(J_{\mathbf{f}})_{ij} = \frac{\partial f_i}{\partial x_j}$.
*   **Exceptions, variations, and alternative approaches:** The determinant of the Jacobian is used in change of variables for multiple integrals.
*   **Key takeaway:** Best linear approximation of a vector-valued function near a point.

---
**Functions**
---

**1. Polynomials**
*   **Concise explanation:** An expression consisting of variables (indeterminates) and coefficients, involving only operations of addition, subtraction, multiplication, and non-negative integer exponents of variables.
*   **Illustrative examples:** $3x^2 - 5x + 2$ (quadratic), $x^3 + 7$ (cubic), $4$ (constant polynomial).
*   **Syntax and real example (General Form):** $P(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0$.
*   **Exceptions, variations, and alternative approaches:** Polynomials in multiple variables (e.g., $x^2y + y^3$). Degree of a polynomial is its highest exponent.
*   **Key takeaway:** Sum of terms with variables raised to non-negative integer powers.

**2. Gamma function**
*   **Concise explanation:** An extension of the factorial function to real and complex numbers. For a positive integer $n$, $\Gamma(n) = (n-1)!$.
*   **Illustrative examples:** $\Gamma(1) = 0! = 1$, $\Gamma(4) = 3! = 6$, $\Gamma(1/2) = \sqrt{\pi}$.
*   **Syntax and real example (Definition):** $\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}dt$ for Re(z) > 0.
*   **Exceptions, variations, and alternative approaches:** Undefined for non-positive integers. Incomplete Gamma functions (lower, upper).
*   **Key takeaway:** Generalizes factorial to non-integer and complex numbers.

**3. argmax/argmin**
*   **Concise explanation:** `argmax` (argument of the maximum) is the input value (argument) from a function's domain at which the function's value is maximized. `argmin` is the input value for the minimum.
*   **Illustrative examples:** For $f(x) = -(x-2)^2+5$, $\text{argmax}_x f(x) = 2$. For a list `L = [10, 50, 20]`, $\text{argmax}_i L_i = 1$ (0-indexed).
*   **Syntax and real example (Notation):** $\operatorname*{arg\,max}_x f(x)$, $\operatorname*{arg\,min}_x f(x)$.
*   **Exceptions, variations, and alternative approaches:** The argmax/argmin may not be unique. If the function is constant, any point is an argmax/argmin.
*   **Key takeaway:** Returns the input that produces the extreme output, not the extreme output itself.

**4. Sigmoid function**
*   **Concise explanation:** A mathematical function having a characteristic "S"-shaped curve or sigmoid curve. A common example is the logistic function.
*   **Illustrative examples:** Maps any real input to the range (0, 1). Used as an activation function in neural networks for binary classification. $\sigma(0) = 0.5$, $\sigma(x) \to 1$ as $x \to \infty$, $\sigma(x) \to 0$ as $x \to -\infty$.
*   **Syntax and real example (Logistic Formula):** $\sigma(x) = \frac{1}{1 + e^{-x}}$.
*   **Exceptions, variations, and alternative approaches:** Other sigmoid-like functions include tanh, Gompertz curve. Generalized logistic function.
*   **Key takeaway:** S-shaped curve squashing inputs to (0,1), often for probabilities.

**5. Softmax function**
*   **Concise explanation:** A function that takes a vector of $K$ real numbers as input and normalizes it into a probability distribution consisting of $K$ probabilities proportional to the exponentials of the input numbers.
*   **Illustrative examples:** Input: $[1, 2, 0]$. Output (approx): $[0.24, 0.67, 0.09]$. The outputs sum to 1. Used in multi-class classification.
*   **Syntax and real example (Formula):** For a vector $\mathbf{z} = (z_1, \dots, z_K)$, $\text{softmax}(\mathbf{z})_j = \frac{e^{z_j}}{\sum_{i=1}^K e^{z_i}}$.
*   **Exceptions, variations, and alternative approaches:** Can be numerically unstable for large input values (log-sum-exp trick helps).
*   **Key takeaway:** Converts a vector of scores into a probability distribution.

**6. Logit function**
*   **Concise explanation:** The logarithm of the odds $p/(1-p)$, where $p$ is a probability. It's the inverse of the standard logistic (sigmoid) function.
*   **Illustrative examples:** If $p=0.5$, odds are 1, $\text{logit}(0.5) = \log(1) = 0$. If $p=0.8$, odds are $0.8/0.2 = 4$, $\text{logit}(0.8) = \log(4) \approx 1.386$.
*   **Syntax and real example (Formula):** $\text{logit}(p) = \log\left(\frac{p}{1-p}\right)$ for $p \in (0,1)$.
*   **Exceptions, variations, and alternative approaches:** Undefined for $p=0$ or $p=1$. Maps probabilities from (0,1) to the entire real line $(-\infty, \infty)$.
*   **Key takeaway:** Inverse of sigmoid, transforms probabilities to log-odds.

**7. Trigonometric functions**
*   **Concise explanation:** Functions of an angle, important for studying triangles and modeling periodic phenomena. Common examples are sine (sin), cosine (cos), and tangent (tan).
*   **Illustrative examples:** $\sin(0) = 0$, $\cos(0) = 1$, $\tan(\pi/4) = 1$. $\sin(\pi/2) = 1$, $\cos(\pi/2) = 0$.
*   **Syntax and real example (Unit Circle):** For an angle $\theta$ on the unit circle, $\cos\theta$ is the x-coordinate and $\sin\theta$ is the y-coordinate.
*   **Exceptions, variations, and alternative approaches:** Inverse trigonometric functions (arcsin, arccos), secant, cosecant, cotangent. Radian vs. degree measure.
*   **Key takeaway:** Relate angles to ratios of sides in right triangles or coordinates on unit circle; model periodic behavior.

**8. Hyperbolic functions**
*   **Concise explanation:** Analogs of trigonometric functions but defined using the hyperbola rather than the circle. Common examples are hyperbolic sine (sinh), cosine (cosh), and tangent (tanh).
*   **Illustrative examples:** $\cosh(x) = \frac{e^x + e^{-x}}{2}$, $\sinh(x) = \frac{e^x - e^{-x}}{2}$. $\cosh(0)=1$, $\sinh(0)=0$.
*   **Syntax and real example (Exponential definitions):** See above. $\tanh(x) = \frac{\sinh(x)}{\cosh(x)} = \frac{e^x - e^{-x}}{e^x + e^{-x}}$.
*   **Exceptions, variations, and alternative approaches:** Inverse hyperbolic functions (arsinh, arcosh). Used in physics (e.g., catenary curve) and as activation functions in neural networks (tanh).
*   **Key takeaway:** Similar to trigonometric functions but based on $e^x$ and $e^{-x}$, often related to hyperbolas.

---
**Questions**
---

**1. Are vectors just 1×n (or n×1) matrices?**
Yes, mathematically, vectors can be considered special cases of matrices: a row vector is a $1 \times n$ matrix, and a column vector is an $n \times 1$ matrix. This interpretation is essential for defining matrix-vector products.

**2. What are the common names for the 1-norm, 2-norm, and ∞-norm? Why are they called like that?**
The $L_1$-norm is called the **Manhattan norm** or Taxicab norm (distance if moving along grid lines). The $L_2$-norm is the **Euclidean norm** (standard straight-line distance). The $L_\infty$-norm is the **Maximum norm** or Chebyshev norm (greatest component magnitude).

**3. Two points lie at distance d from one another on a 2D plane. They are both transformed with some matrix M. What is the maximum possible distance between the two points after the transformation?**
Let the points be $\mathbf{p}_1, \mathbf{p}_2$, so $\mathbf{v} = \mathbf{p}_2 - \mathbf{p}_1$ with $||\mathbf{v}||_2 = d$. After transformation $M$, the new vector is $M\mathbf{v}$. The maximum possible distance is $d \times \sigma_{max}(M)$, where $\sigma_{max}(M)$ is the largest singular value of $M$ (also known as the operator norm or spectral norm).

**4. What is the time complexity of multiplying two matrices of different sizes?**
For matrices $A (m \times k)$ and $B (k \times n)$, the standard algorithm for $AB$ has a time complexity of $O(m \cdot k \cdot n)$. More advanced algorithms like Strassen's can reduce this, but $O(mkn)$ is typical.

**5. What is the time complexity of inverting a matrix?**
For an $n \times n$ matrix, standard methods like Gaussian elimination or LU decomposition for inversion have a time complexity of $O(n^3)$. Algorithms similar to matrix multiplication (e.g., Coppersmith-Winograd) can theoretically achieve $O(n^{2.373})$.

**6. Given matrices A, B, and C with respective sizes 10×100, 100×1000, 1000×1000, when calculating the product ABC would you rather start with calculating AB and then multiply with C, or would you start with BC and then multiply it with A? (matrix multiplication is associative)**
Calculate $(AB)C$: $(10 \times 100 \times 1000) + (10 \times 1000 \times 1000) = 10^6 + 10^7 = 1.1 \times 10^7$ operations.
Calculate $A(BC)$: $(100 \times 1000 \times 1000) + (10 \times 100 \times 1000) = 10^8 + 10^6 = 1.01 \times 10^8$ operations.
You would start with $(AB)C$ as it requires fewer scalar multiplications.

**7. Why is there more than one Gamma function?**
The term "Gamma function" usually refers to $\Gamma(z)$. However, related functions like the **incomplete Gamma functions** (lower $\gamma(s,x)$ and upper $\Gamma(s,x)$) also exist, which are definite integrals of the same integrand but with varying limits, making them useful in different contexts like probability distributions.

**8. How are Gamma functions useful in combinatorics?**
The Gamma function generalizes the factorial function ($n! = \Gamma(n+1)$) to non-integer values. This is useful in generalizing combinatorial formulas and in probability distributions (like the Gamma distribution) that involve factorial-like terms for continuous variables.

**9. Is argmax a function? How would you define its signature (with type hints)?**
Yes, `argmax` is a function. Its signature could be (for a simple 1D case): `def argmax(f: Callable[[Any], Comparable], domain: Iterable[Any]) -> Any:`, where it returns an element from the `domain` that maximizes `f`. For NumPy arrays, it's often `np.argmax(a: np.ndarray, axis: Optional[int] = None) -> Union[int, np.ndarray]`.

**10. What are odds and how do they relate to the logit function?**
Odds are the ratio of the probability of an event occurring to the probability of it not occurring: $\text{Odds} = p / (1-p)$. The logit function is the natural logarithm of the odds: $\text{logit}(p) = \log(\text{Odds}) = \log(p/(1-p))$.

**11. Why does the exponential function (with base e) show up in so many places?**
The exponential function $e^x$ is unique because its derivative is itself ($\frac{d}{dx}e^x = e^x$), making it fundamental in calculus and differential equations modeling natural growth/decay. Its properties simplify many mathematical expressions and connect to complex numbers via Euler's formula.

**12. Does the softmax function return a distribution?**
Yes, the softmax function takes a vector of arbitrary real scores and transforms it into a vector whose elements are non-negative and sum to 1. This output can be interpreted as a probability distribution over a set of discrete outcomes.

**13. If tanh can be expressed as a sigmoid - why do we need both of them?**
While $\tanh(x) = 2 \sigma(2x) - 1$ (a scaled and shifted sigmoid), $\tanh$ is often preferred because its output range is $(-1, 1)$ (zero-centered), which can be beneficial for optimization in some neural network architectures. Sigmoid's range is $(0,1)$.

**14. What is the geometric interpretation of a dot product?**
The dot product $\mathbf{a} \cdot \mathbf{b}$ is $||\mathbf{a}|| \ ||\mathbf{b}|| \cos(\theta)$. Geometrically, it's the product of the magnitude of one vector and the scalar projection of the second vector onto the first, indicating how much one vector points in the direction of the other.

**15. Should the keyword "Optimization" appear under "Calculus"? List different types of optimization problems.**
Yes, optimization heavily relies on calculus (especially derivatives for finding minima/maxima). Types include: Linear Programming, Quadratic Programming, Convex Optimization, Non-linear Optimization, Integer Programming, Stochastic Optimization, Combinatorial Optimization.

**16. One may say that the sigmoid function is the relaxation of the step function.**
    **- What does that mean?**
    It means the sigmoid is a smooth, continuous, and differentiable approximation of the discontinuous step function (0 for $x<0$, 1 for $x \ge 0$). This smoothness is crucial for gradient-based optimization.
    **- How can we make it closer to a step function? How close can we get?**
    We can make $\sigma(kx) = \frac{1}{1+e^{-kx}}$ closer to a step function by increasing $k > 0$. As $k \to \infty$, $\sigma(kx)$ approaches the step function at $x=0$. We can get arbitrarily close but it remains differentiable for finite $k$.
    **- What if we want the step to happen around $x \neq 0$ rather than $x=0$?**
    We can use $\sigma(k(x-c))$, where $c$ is the desired center of the step. For example, $\sigma(k(x-x_0))$ will make the transition around $x=x_0$.
