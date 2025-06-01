Questions 

- "Are vectors just 1×n (or n×1) matrices?" -> Answered in [[Vector]].
- "What are the common names for the 1-norm, 2-norm, and ∞-norm? Why are they called like that?" -> Answered in [[p-norm]].
- "Two points lie at distance d from one another on a 2D plane. They are both transformed with some matrix M. What is the maximum possible distance between the two points after the transformation?" -> This would go into a new note [[Matrix_Transformations_and_Distance]].
- "What is the time complexity of multiplying two matrices of different sizes?" -> This would go into [[Matrix_Multiplication_Complexity]].
- "What is the time complexity of inverting a matrix?" -> This would go into [[Matrix_Inversion_Complexity]].
- "Given matrices A, B, and C with respective sizes 10×100, 100×1000, 1000×1000, when calculating the product ABC would you rather start with calculating AB and then multiply with C, or would you start with BC and then multiply it with A? (matrix multiplication is associative)" -> This would go into [[Matrix_Multiplication_Associativity]].
- "Why is there more than one Gamma function?" -> Answered in [[Gamma_Function]].
- "How are Gamma functions useful in combinatorics?" -> Answered in [[Gamma_Function]].
- "Is argmax a function? How would you define its signature (with type hints)?" -> This would go into [[argmax_argmin]].
- "What are odds and how do they relate to the logit function?" -> This would go into [[Logit_Function]].
- "Why does the exponential function (with base e) show up in so many places?" -> This would go into [[Exponential_Function_Significance]] (created this new note).
- "Does the softmax function return a distribution?" -> Answered in [[Softmax_Function]].
- "If tanh can be expressed as a sigmoid - why do we need both of them?" -> Answered in [[Hyperbolic_Functions]] (under tanh).
- "What is the geometric interpretation of a dot product?" -> Answered in [[Dot_Product]].
- "Should the keyword "Optimization" appear under "Calculus"? List different types of optimization problems." -> Answered in [[Calculus_Optimization]].
- "One may say that the sigmoid function is the relaxation of the step function..." -> Answered in [[Sigmoid_Function]].

It seems most questions are covered or planned. I will create the specific notes for the remaining questions next.Okay, I will now create the notes for the remaining specific questions and concepts from your list, ensuring they are placed in the appropriate subfolders within `150_Mathematics`.

`````markdown

Filename: 150_Mathematics/Linear_Algebra/Matrix_Transformations_and_Distance.md
````markdown
---
tags: [mathematics, linear_algebra, matrix, transformation, distance, singular_values, concept]
aliases: [Effect of Matrix Transformation on Distance]
related:
  - "[[Transformation_Matrix]]"
  - "[[Matrix]]"
  - "[[Vector]]"
  - "[[p-norm]]" # L2-norm for Euclidean distance
  - "[[Singular_Values]]"
  - "[[Eigenvalues_Eigenvectors]]"
worksheet: [WS_Math_Foundations_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Effect of Matrix Transformations on Distance Between Points

When a [[Transformation_Matrix|linear transformation]] represented by a [[Matrix|matrix]] $\mathbf{M}$ is applied to two points in a space, the distance between these points generally changes. Understanding how this distance changes is crucial in various applications, including geometry, computer graphics, and machine learning.

Let $\mathbf{p}_1$ and $\mathbf{p}_2$ be two points (represented as [[Column_Vector|column vectors]]) in an $n$-dimensional space. The initial distance vector between them is $\mathbf{d} = \mathbf{p}_2 - \mathbf{p}_1$. The initial Euclidean distance (L2-norm) is $D = \|\mathbf{d}\|_2 = \|\mathbf{p}_2 - \mathbf{p}_1\|_2$.

After applying a linear transformation $\mathbf{M}$ (an $m \times n$ matrix), the new points are $\mathbf{p}'_1 = \mathbf{M}\mathbf{p}_1$ and $\mathbf{p}'_2 = \mathbf{M}\mathbf{p}_2$.
The new distance vector is $\mathbf{d}' = \mathbf{p}'_2 - \mathbf{p}'_1 = \mathbf{M}\mathbf{p}_2 - \mathbf{M}\mathbf{p}_1 = \mathbf{M}(\mathbf{p}_2 - \mathbf{p}_1) = \mathbf{M}\mathbf{d}$.
The new Euclidean distance is $D' = \|\mathbf{d}'\|_2 = \|\mathbf{M}\mathbf{d}\|_2$.

>[!question] Two points lie at distance $D$ from one another on a 2D plane. They are both transformed with some matrix $\mathbf{M}$. What is the maximum possible distance between the two points after the transformation?

The question asks for the maximum possible value of $D' = \|\mathbf{M}\mathbf{d}\|_2$, given that $\|\mathbf{d}\|_2 = D$.

We are looking to maximize $\frac{\|\mathbf{M}\mathbf{d}\|_2}{\|\mathbf{d}\|_2}$ over all non-zero vectors $\mathbf{d}$. The maximum value of this ratio is, by definition, the **spectral norm** (or L2-norm) of the matrix $\mathbf{M}$, denoted $\|\mathbf{M}\|_2$.
The spectral norm of a matrix $\mathbf{M}$ is equal to its largest [[Singular_Values|singular value]], $\sigma_{\text{max}}(\mathbf{M})$.

$$ \max_{\mathbf{d} \neq \mathbf{0}} \frac{\|\mathbf{M}\mathbf{d}\|_2}{\|\mathbf{d}\|_2} = \|\mathbf{M}\|_2 = \sigma_{\text{max}}(\mathbf{M}) $$

Therefore, the maximum possible new distance $D'_{\text{max}}$ is:
$$ D'_{\text{max}} = \sigma_{\text{max}}(\mathbf{M}) \cdot \|\mathbf{d}\|_2 = \sigma_{\text{max}}(\mathbf{M}) \cdot D $$

**Answer:** The maximum possible distance between the two points after the transformation is $D \cdot \sigma_{\text{max}}(\mathbf{M})$, where $D$ is the original distance and $\sigma_{\text{max}}(\mathbf{M})$ is the largest singular value of the transformation matrix $\mathbf{M}$.

This maximum stretching occurs when the original distance vector $\mathbf{d}$ is aligned with the right-singular vector of $\mathbf{M}$ corresponding to $\sigma_{\text{max}}(\mathbf{M})$.

## Factors Affecting Distance Change
[list2tab|#Transformation Effects]
- **Scaling Transformation**
    - If $\mathbf{M} = \begin{pmatrix} s_x & 0 \\ 0 & s_y \end{pmatrix}$, then $\mathbf{M}\mathbf{d} = \begin{pmatrix} s_x d_x \\ s_y d_y \end{pmatrix}$.
    - The distance changes anisotropically. If $s_x = s_y = s$ (uniform scaling), then $D' = |s|D$. The largest singular value is $|s|$.
- **Rotation Transformation**
    - If $\mathbf{M}$ is an [[Orthogonal_Matrix|orthogonal matrix]] (representing a rotation or reflection), it preserves lengths (and angles).
    - For an orthogonal matrix, all singular values are 1. So $\sigma_{\text{max}}(\mathbf{M}) = 1$.
    - Therefore, $D' = \|\mathbf{M}\mathbf{d}\|_2 = \|\mathbf{d}\|_2 = D$. Distances are preserved.
- **Shear Transformation**
    - A shear transformation will generally change distances. The amount of change depends on the direction of the distance vector relative to the shear direction. The largest singular value will be $>1$.
- **Projection Transformation**
    - If $\mathbf{M}$ is a projection matrix (e.g., projecting onto a line or plane), it generally reduces distances (unless the distance vector is already in the subspace being projected onto). Some singular values will be 1 (for directions within the subspace) and others will be 0 (for directions orthogonal to the subspace). The largest singular value will be 1. $D' \le D$.

## General Case and Singular Values
The [[Singular_Value_Decomposition|Singular Value Decomposition (SVD)]] of $\mathbf{M} = \mathbf{U}\mathbf{\Sigma}\mathbf{V}^T$ provides insight.
$\|\mathbf{M}\mathbf{d}\|_2 = \|\mathbf{U}\mathbf{\Sigma}\mathbf{V}^T\mathbf{d}\|_2$.
Since $\mathbf{U}$ is orthogonal, it preserves norms: $\|\mathbf{U}\mathbf{y}\|_2 = \|\mathbf{y}\|_2$.
So, $\|\mathbf{M}\mathbf{d}\|_2 = \|\mathbf{\Sigma}(\mathbf{V}^T\mathbf{d})\|_2$.
Let $\mathbf{z} = \mathbf{V}^T\mathbf{d}$. Since $\mathbf{V}^T$ is orthogonal, $\|\mathbf{z}\|_2 = \|\mathbf{d}\|_2 = D$.
The vector $\mathbf{\Sigma}\mathbf{z}$ has components $(\sigma_1 z_1, \sigma_2 z_2, \dots, \sigma_r z_r, 0, \dots, 0)$, where $\sigma_i$ are the singular values.
So, $\|\mathbf{\Sigma}\mathbf{z}\|_2^2 = \sum_{i=1}^{r} (\sigma_i z_i)^2$.

To maximize this subject to $\sum z_i^2 = D^2$:
The sum $\sum (\sigma_i z_i)^2$ is maximized when the component $z_k$ corresponding to the largest singular value $\sigma_k = \sigma_{\text{max}}$ is non-zero, and ideally, all "energy" of $\mathbf{z}$ is concentrated in that component. This happens if $\mathbf{d}$ is aligned with the right-singular vector $\mathbf{v}_k$ corresponding to $\sigma_{\text{max}}$. In this case, $\mathbf{V}^T\mathbf{d}$ will be a vector with $D$ in the $k$-th position and zeros elsewhere (if $\mathbf{d} = D \mathbf{v}_k$).
Then $\|\mathbf{\Sigma}\mathbf{z}\|_2 = \sqrt{(\sigma_{\text{max}}D)^2} = \sigma_{\text{max}}D$.
150_Mathematics/Linear_Algebra/Singular_Value_Decomposition
````markdown
[[Singular_Value_Decomposition]]
````

150_Mathematics/Functions/Polynomials.md
````markdown
[[Polynomials]]
````

Filename: 150_Mathematics/Functions/Exponential_Function.md
````markdown
[[Exponential_Function]]
````

Filename: 150_Mathematics/Functions/Logarithmic_Function.md
````markdown
[[Logarithmic_Function]]
````

Filename: 150_Mathematics/Functions/Trigonometric_Functions.md
````markdown
[[Trigonometric_Functions]]
````

Filename: 150_Mathematics/Functions/Hyperbolic_Functions.md
````markdown
[[Hyperbolic_Functions]]````

Filename: 150_Mathematics/Functions/Sigmoid_Function.md
````markdown
[[Sigmoid_Function]]
````

Filename: 150_Mathematics/Functions/Softmax_Function.md
````markdown
[[Softmax_Function]]
````

Filename: 150_Mathematics/Functions/Gamma_Function.md
````markdown
[[Gamma_Function]]
````


Similarly, the **minimum possible non-zero distance** $D'_{\text{min}}$ (if $\mathbf{M}$ has full column rank and $\mathbf{d} \neq \mathbf{0}$) would be $\sigma_{\text{min}}(\mathbf{M}) \cdot D$, where $\sigma_{\text{min}}(\mathbf{M})$ is the smallest non-zero singular value. This occurs when $\mathbf{d}$ is aligned with the right-singular vector corresponding to $\sigma_{\text{min}}$. If $\mathbf{M}$ is rank-deficient, some non-zero $\mathbf{d}$ can be mapped to $\mathbf{0}$, making $D'=0$.

## Application Example
In machine learning, if features are transformed by a matrix $\mathbf{M}$, understanding how this transformation affects distances can be important for distance-based algorithms like k-Nearest Neighbors (k-NN) or clustering algorithms. If $\mathbf{M}$ scales some directions much more than others, those directions will dominate distance calculations unless further normalization is applied.

---````

Filename: 150_Mathematics/Linear_Algebra/Matrix_Multiplication_Complexity.md
````markdown
---
tags: [mathematics, linear_algebra, matrix_product, complexity, algorithm_analysis, concept]
aliases: [Time Complexity of Matrix Multiplication]
related:
  - "[[Matrix_Product]]"
  - "[[Matrix]]"
  - "[[Computational_Complexity]]"
  - "[[Matrix_Multiplication_Associativity]]" # Relevant for chain multiplication
worksheet: [WS_Math_Foundations_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Time Complexity of Matrix Multiplication

The time complexity of multiplying two matrices depends on their dimensions and the algorithm used.

## Standard (Naive) Matrix Multiplication

Consider two matrices:
- $\mathbf{A}$ of dimensions $m \times n$
- $\mathbf{B}$ of dimensions $n \times p$

Their [[Matrix_Product|product]] $\mathbf{C} = \mathbf{A}\mathbf{B}$ will be an $m \times p$ matrix.
Each element $C_{ij}$ of the resulting matrix $\mathbf{C}$ is calculated as the [[Dot_Product|dot product]] of the $i$-th row of $\mathbf{A}$ and the $j$-th column of $\mathbf{B}$:
$$ C_{ij} = \sum_{k=1}^{n} A_{ik} B_{kj} $$
To calculate one element $C_{ij}$:
- There are $n$ multiplications ($A_{ik} B_{kj}$).
- There are $n-1$ additions.
So, roughly $2n-1$ floating-point operations (flops), or $O(n)$ operations per element.

The resulting matrix $\mathbf{C}$ has $m \times p$ elements.
Therefore, the total number of operations for the standard algorithm is approximately:
$$ (m \times p \text{ elements}) \times (2n \text{ operations per element}) = 2mpn \text{ flops} $$
The time complexity is thus $O(mpn)$.

>[!question] What is the time complexity of multiplying two matrices of different sizes?
>As derived above, for multiplying an $m \times n$ matrix by an $n \times p$ matrix using the standard algorithm, the time complexity is $O(mpn)$.

**Special Case: Square Matrices**
If both matrices are square of size $n \times n$ (i.e., $m=n=p$), the complexity becomes $O(n \cdot n \cdot n) = O(n^3)$.

## Advanced Matrix Multiplication Algorithms
While the standard $O(n^3)$ algorithm (for square matrices) is commonly taught and implemented for its simplicity, more advanced algorithms exist with better asymptotic complexity, although they may have larger constant factors and are often more complex to implement, making them practical only for very large matrices.

- **Strassen's Algorithm (1969):**
    - Complexity: Approximately $O(n^{\log_2 7}) \approx O(n^{2.807})$.
    - It uses a divide-and-conquer approach, reducing the number of multiplications needed for $2 \times 2$ block matrices from 8 to 7, at the cost of more additions/subtractions.
- **Coppersmith–Winograd Algorithm (1990):**
    - Complexity: Approximately $O(n^{2.375477})$.
    - More theoretical, very complex, and not practically used due to large hidden constants.
- **Recent Developments (e.g., Alman and Williams, 2020s):**
    - Further slight improvements, e.g., $O(n^{2.3728596})$. These are primarily of theoretical interest.

The "exponent of matrix multiplication," denoted $\omega$, is the smallest real number such that two $n \times n$ matrices can be multiplied in $O(n^\omega)$ operations. It's known that $2 \le \omega < 2.37286$. Proving $\omega = 2$ (i.e., matrix multiplication can be done as fast as matrix addition, asymptotically) is a major open problem.

## Practical Considerations
- For most practical purposes and moderately sized matrices, the standard $O(mpn)$ algorithm (or $O(n^3)$ for square matrices) is what is implemented in libraries like NumPy (often using highly optimized BLAS - Basic Linear Algebra Subprograms - routines written in Fortran or C).
- These optimized libraries also take into account memory access patterns, caching, and parallelization, which can significantly impact real-world performance beyond just the flop count.
- The overhead of more complex algorithms like Strassen's means they only outperform naive multiplication for very large $n$. Some libraries might switch to Strassen's algorithm or similar for matrices above a certain size threshold.

## Impact on Chain Multiplication
The $O(mpn)$ complexity is critical when considering the optimal order for multiplying a chain of matrices. See [[Matrix_Multiplication_Associativity]].

---
````

Filename: 150_Mathematics/Linear_Algebra/Matrix_Inversion_Complexity.md
````markdown
---
tags: [mathematics, linear_algebra, matrix_inversion, complexity, algorithm_analysis, concept]
aliases: [Time Complexity of Matrix Inversion, Inverse Matrix Complexity]
related:
  - "[[Matrix_Inversion]]"
  - "[[Matrix]]"
  - "[[Gaussian_Elimination]]"
  - "[[Matrix_Multiplication_Complexity]]" # Inversion is related to multiplication complexity
  - "[[Determinant_Matrix]]"
worksheet: [WS_Math_Foundations_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Time Complexity of Matrix Inversion

The time complexity of inverting an $n \times n$ square [[Matrix|matrix]] is closely related to the complexity of [[Matrix_Product|matrix multiplication]].

## Standard Methods for Matrix Inversion

1.  **Gaussian Elimination (Gauss-Jordan Elimination):**
    - This method involves augmenting the matrix $\mathbf{A}$ with the identity matrix $\mathbf{I}$ to form $[\mathbf{A} | \mathbf{I}]$.
    - Row operations are then performed to transform $\mathbf{A}$ into $\mathbf{I}$. The same operations applied to $\mathbf{I}$ will transform it into $\mathbf{A}^{-1}$, resulting in $[\mathbf{I} | \mathbf{A}^{-1}]$.
    - The number of arithmetic operations required for Gaussian elimination on an $n \times n$ matrix is $O(n^3)$.
    - This is a common and practical method for matrix inversion.

2.  **Using Adjugate Matrix (Cramer's Rule based):**
    - The inverse can be calculated as $\mathbf{A}^{-1} = \frac{1}{\det(\mathbf{A})} \text{adj}(\mathbf{A})$, where $\text{adj}(\mathbf{A})$ is the adjugate (or classical adjoint) of $\mathbf{A}$, which is the transpose of the cofactor matrix.
    - Calculating the [[Determinant_Matrix|determinant]] using cofactor expansion takes $O(n!)$ operations, which is highly inefficient for $n > 3$ or $4$.
    - Calculating all $n^2$ cofactors (each an $(n-1) \times (n-1)$ determinant) is also very costly.
    - While theoretically important, this method is not used for numerical computation of inverses for larger matrices due to its prohibitive complexity. Determinants are usually computed via LU decomposition, which is $O(n^3)$.

## Relationship to Matrix Multiplication Complexity
It has been shown that matrix inversion has the same asymptotic time complexity as matrix multiplication.
Let $\omega$ be the exponent of matrix multiplication, such that two $n \times n$ matrices can be multiplied in $O(n^\omega)$ time (see [[Matrix_Multiplication_Complexity]]). Currently, $2 \le \omega < 2.37286$.

- If matrix multiplication can be done in $O(n^\omega)$ time, then matrix inversion can also be done in $O(n^\omega)$ time.
    - This can be shown using block matrix inversion techniques (e.g., Strassen's algorithm for inversion based on his multiplication algorithm).

>[!question] What is the time complexity of inverting a matrix?
>For an $n \times n$ matrix:
>- Using standard algorithms like **Gaussian elimination**, the time complexity is $O(n^3)$.
>- Theoretically, matrix inversion has the same asymptotic complexity as matrix multiplication. If matrix multiplication is $O(n^\omega)$, then inversion is also $O(n^\omega)$. Since the best known $\omega < 3$ (e.g., Strassen's algorithm gives $\omega \approx 2.807$), matrix inversion can theoretically be done faster than $O(n^3)$ for very large matrices.

## Practical Considerations
- For most practical applications and matrix sizes encountered, algorithms with $O(n^3)$ complexity (like those based on LU decomposition or Gaussian elimination, often implemented in highly optimized BLAS/LAPACK libraries) are used.
- The constant factors hidden in the "big O" notation for faster theoretical algorithms (like Strassen's for inversion) can make them slower than $O(n^3)$ methods for all but extremely large matrices.
- **Numerical Stability:** Besides time complexity, numerical stability is a major concern. Direct computation of the inverse is often avoided if possible in numerical linear algebra. For example, to solve $\mathbf{A}\mathbf{x} = \mathbf{b}$, it's generally more stable and often faster to solve the system directly (e.g., using LU decomposition and forward/backward substitution) rather than computing $\mathbf{A}^{-1}$ and then $\mathbf{x} = \mathbf{A}^{-1}\mathbf{b}$.
- **Condition Number:** The accuracy of the computed inverse is highly dependent on the condition number of the matrix. Ill-conditioned matrices (matrices close to singular) are difficult to invert accurately.

In summary, while theoretically linked to $O(n^\omega)$, the practical complexity for matrix inversion is typically considered $O(n^3)$.

---
````

Filename: 150_Mathematics/Linear_Algebra/Matrix_Multiplication_Associativity.md
````markdown
---
tags: [mathematics, linear_algebra, matrix_product, associativity, optimization, complexity, concept]
aliases: [Associativity of Matrix Multiplication, Optimal Matrix Chain Multiplication]
related:
  - "[[Matrix_Product]]"
  - "[[Matrix]]"
  - "[[Matrix_Multiplication_Complexity]]"
  - "[[Dynamic_Programming]]" # Used to find optimal parenthesization
worksheet: [WS_Math_Foundations_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Associativity of Matrix Multiplication and Optimal Order

## Associativity
One of the fundamental properties of [[Matrix_Product|matrix multiplication]] is that it is **associative**. This means that for any three matrices $\mathbf{A}$, $\mathbf{B}$, and $\mathbf{C}$ whose products are defined, the order in which the multiplications are performed does not affect the final result:
$$ (\mathbf{A}\mathbf{B})\mathbf{C} = \mathbf{A}(\mathbf{B}\mathbf{C}) $$
Provided that the dimensions are compatible for the products involved:
- If $\mathbf{A}$ is $m \times n$, $\mathbf{B}$ is $n \times p$, and $\mathbf{C}$ is $p \times q$.
- Then $\mathbf{A}\mathbf{B}$ is $m \times p$, and $(\mathbf{A}\mathbf{B})\mathbf{C}$ is $m \times q$.
- And $\mathbf{B}\mathbf{C}$ is $n \times q$, and $\mathbf{A}(\mathbf{B}\mathbf{C})$ is $m \times q$.

While the result is the same, the **number of scalar multiplications** (and thus the computational cost) can vary significantly depending on the parenthesization (order of operations).

## Optimizing Chain Matrix Multiplication

>[!question] Given matrices $\mathbf{A}$, $\mathbf{B}$, and $\mathbf{C}$ with respective sizes $10 \times 100$, $100 \times 1000$, and $1000 \times 1000$, when calculating the product $\mathbf{A}\mathbf{B}\mathbf{C}$ would you rather start with calculating $(\mathbf{A}\mathbf{B})\mathbf{C}$ or $\mathbf{A}(\mathbf{B}\mathbf{C})$? (matrix multiplication is associative)

Let's analyze the number of scalar multiplications for each case, using the standard [[Matrix_Multiplication_Complexity|complexity of $O(mpn)$]] for multiplying an $m \times n$ matrix by an $n \times p$ matrix.

**Dimensions:**
- $\mathbf{A}: 10 \times 100$
- $\mathbf{B}: 100 \times 1000$
- $\mathbf{C}: 1000 \times 1000$

**Option 1: Calculate $(\mathbf{A}\mathbf{B})\mathbf{C}$**
1.  **Calculate $\mathbf{P_1} = \mathbf{A}\mathbf{B}$:**
    - $\mathbf{A}$ is $10 \times 100$. $\mathbf{B}$ is $100 \times 1000$.
    - Dimensions of $\mathbf{P_1}$: $(10 \times \underline{100}) \cdot (\underline{100} \times 1000) \rightarrow 10 \times 1000$.
    - Number of scalar multiplications for $\mathbf{P_1}$: $10 \times 100 \times 1000 = 1,000,000$.
2.  **Calculate $\mathbf{P_1}\mathbf{C}$:**
    - $\mathbf{P_1}$ is $10 \times 1000$. $\mathbf{C}$ is $1000 \times 1000$.
    - Dimensions of result: $(10 \times \underline{1000}) \cdot (\underline{1000} \times 1000) \rightarrow 10 \times 1000$.
    - Number of scalar multiplications for $\mathbf{P_1}\mathbf{C}$: $10 \times 1000 \times 1000 = 10,000,000$.
3.  **Total scalar multiplications for Option 1:** $1,000,000 + 10,000,000 = 11,000,000$.

**Option 2: Calculate $\mathbf{A}(\mathbf{B}\mathbf{C})$**
1.  **Calculate $\mathbf{P_2} = \mathbf{B}\mathbf{C}$:**
    - $\mathbf{B}$ is $100 \times 1000$. $\mathbf{C}$ is $1000 \times 1000$.
    - Dimensions of $\mathbf{P_2}$: $(100 \times \underline{1000}) \cdot (\underline{1000} \times 1000) \rightarrow 100 \times 1000$.
    - Number of scalar multiplications for $\mathbf{P_2}$: $100 \times 1000 \times 1000 = 100,000,000$.
2.  **Calculate $\mathbf{A}\mathbf{P_2}$:**
    - $\mathbf{A}$ is $10 \times 100$. $\mathbf{P_2}$ is $100 \times 1000$.
    - Dimensions of result: $(10 \times \underline{100}) \cdot (\underline{100} \times 1000) \rightarrow 10 \times 1000$.
    - Number of scalar multiplications for $\mathbf{A}\mathbf{P_2}$: $10 \times 100 \times 1000 = 1,000,000$.
3.  **Total scalar multiplications for Option 2:** $100,000,000 + 1,000,000 = 101,000,000$.

**Comparison:**
- Option 1 ($(\mathbf{A}\mathbf{B})\mathbf{C}$): $11,000,000$ scalar multiplications.
- Option 2 ($\mathbf{A}(\mathbf{B}\mathbf{C})$): $101,000,000$ scalar multiplications.

**Conclusion for the question:**
You would rather start with calculating $(\mathbf{A}\mathbf{B})$ and then multiply by $\mathbf{C}$, as this requires significantly fewer scalar multiplications ($11 \text{ million vs } 101 \text{ million}$).

## Matrix Chain Multiplication Problem
The problem of finding the optimal parenthesization for multiplying a chain of $N$ matrices $\mathbf{A}_1 \mathbf{A}_2 \dots \mathbf{A}_N$ is a classic optimization problem.
If matrix $\mathbf{A}_i$ has dimensions $d_{i-1} \times d_i$.
The number of ways to parenthesize $N$ matrices is given by the $(N-1)$-th Catalan number, which grows very rapidly. Exhaustive search is not feasible.

This problem can be solved efficiently using **[[Dynamic_Programming|dynamic programming]]**.
Let $m[i,j]$ be the minimum number of scalar multiplications needed to compute the product $\mathbf{A}_i \mathbf{A}_{i+1} \dots \mathbf{A}_j$.
The recurrence relation is:
$$ m[i,j] = \min_{i \le k < j} (m[i,k] + m[k+1,j] + d_{i-1} d_k d_j) $$
The base cases are $m[i,i] = 0$ (cost of multiplying a single matrix is zero).
The algorithm fills a table of $m[i,j]$ values, typically bottom-up, considering chains of increasing length.

## Importance
- **Computational Efficiency:** Choosing the optimal order can lead to dramatic savings in computation time, especially for large matrices or long chains.
- **Numerical Stability:** While associativity guarantees the same mathematical result, different orders of operations might lead to slightly different results in finite-precision floating-point arithmetic due to rounding errors. However, the primary concern for associativity is usually computational cost.
- **Algorithm Design:** Understanding this property is important when designing algorithms that involve sequences of matrix operations, such as in graphics rendering pipelines or complex scientific computations.

---
````

Filename: 150_Mathematics/Functions/Exponential_Function_Significance.md
````markdown
---
tags: [mathematics, functions, exponential, euler_number, significance, applications, concept]
aliases: [Why is e^x important, Importance of Euler's Number]
related:
  - "[[Exponential_Function]]"
  - "[[Euler_Number_e]]"
  - "[[Logarithmic_Function]]"
  - "[[Calculus_Derivatives]]"
  - "[[Differential_Equations]]"
  - "[[Probability_Distribution]]"
  - "[[Complex_Numbers_Euler_Formula]]"
worksheet: [WS_Math_Foundations_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Significance of the Exponential Function (Base $e$)

>[!question] Why does the exponential function (with base $e$) show up in so many places?

The [[Exponential_Function|natural exponential function]] $f(x) = e^x$, where $e \approx 2.71828$ is [[Euler_Number_e|Euler's number]], is arguably one of the most important functions in mathematics, science, engineering, and finance. Its ubiquity stems from several unique mathematical properties and its ability to model fundamental processes of growth and decay.

[list2card|addClass(ab-col1)|#Reasons for Significance]
- **1. Own Derivative and Integral:**
    - The most defining characteristic of $e^x$ is that it is its own [[Calculus_Derivatives|derivative]]:
      $$ \frac{d}{dx} e^x = e^x $$
    - Consequently, it is also its own [[Calculus_Integrals|indefinite integral]] (up to a constant):
      $$ \int e^x \,dx = e^x + C $$
    - **Implication:** This means $e^x$ naturally describes processes where the **rate of change of a quantity is directly proportional to the quantity itself**. Many natural phenomena exhibit this behavior (e.g., population growth with unlimited resources, radioactive decay, continuous compound interest).

- **2. Solutions to [[Differential_Equations|Differential Equations]]:**
    - Because of its derivative property, $e^{kx}$ is a fundamental solution to the simple linear first-order differential equation $\frac{dy}{dx} = ky$.
    - More generally, exponential functions appear in the solutions of many linear ordinary differential equations (ODEs) and partial differential equations (PDEs) that model a vast range of physical systems.

- **3. Taylor Series Expansion:**
    - The Taylor series (Maclaurin series) for $e^x$ is remarkably simple and elegant:
      $$ e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots $$
    - This series converges for all real and complex $x$. This representation connects $e^x$ to [[Polynomials|polynomials]] and [[Factorial|factorials]], and is useful for approximations and theoretical derivations. Setting $x=1$ provides a way to define $e$.

- **4. Connection to Compound Interest and [[Euler_Number_e|Euler's Number $e$]]:**
    - [[Euler_Number_e|Euler's number $e$]] arises naturally from the concept of continuous compounding of interest.
    - The formula for compound interest is $A = P(1 + \frac{r}{n})^{nt}$. As $n \to \infty$ (compounding continuously), this becomes $A = Pe^{rt}$.
    - $e = \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n$.

- **5. [[Complex_Numbers_Euler_Formula|Euler's Formula]] (Connection to Trigonometry):**
    - For any real number $x$, Euler's formula states:
      $$ e^{ix} = \cos x + i \sin x $$
      where $i$ is the imaginary unit ($i^2 = -1$).
    - This profound identity links the exponential function to [[Trigonometric_Functions|trigonometric functions]] through complex numbers. It allows trigonometric functions to be expressed using complex exponentials:
      $$ \cos x = \frac{e^{ix} + e^{-ix}}{2} $$
      $$ \sin x = \frac{e^{ix} - e^{-ix}}{2i} $$
    - This connection is fundamental in signal processing (Fourier analysis), physics (wave mechanics), and engineering.
    - **Euler's Identity:** A special case of Euler's formula ($x=\pi$) gives $e^{i\pi} + 1 = 0$, linking five fundamental mathematical constants.

- **6. [[Probability_Distribution|Probability Distributions]]:**
    - The exponential function is a core component of many important probability distributions:
        - **Normal (Gaussian) Distribution:** $f(x) \propto e^{-(x-\mu)^2 / (2\sigma^2)}$. The "bell curve" is ubiquitous in statistics and natural sciences due to the Central Limit Theorem.
        - **Exponential Distribution:** $f(x) = \lambda e^{-\lambda x}$, models time between events in a Poisson process.
        - **Poisson Distribution:** (Probability mass function) $P(k) = \frac{\lambda^k e^{-\lambda}}{k!}$.
        - **Gamma Distribution, Chi-squared Distribution, Log-normal Distribution, etc.**

- **7. [[Logarithmic_Function|Inverse Relationship with the Natural Logarithm]]:**
    - The natural logarithm $\ln(x)$ is the inverse of $e^x$. Logarithms transform multiplicative processes into additive ones and are essential for scaling, measuring information (entropy), and solving exponential equations. The naturalness of $e$ makes $\ln(x)$ a "natural" logarithm.

- **8. Basis for Other Exponential Functions:**
    - Any exponential function $a^x$ (where $a > 0$) can be written as $a^x = (e^{\ln a})^x = e^{x \ln a}$. This means that understanding $e^x$ allows understanding all exponential functions.

- **9. Optimization and Machine Learning:**
    - The [[Sigmoid_Function|sigmoid function]] ($\sigma(x) = \frac{1}{1+e^{-x}}$) and [[Softmax_Function|softmax function]] (which heavily uses exponentials) are crucial in logistic regression and neural networks for classification tasks, mapping raw scores to probabilities.
    - Exponential terms appear in various loss functions and regularization techniques.

In essence, $e^x$ is fundamental because it represents the "natural" rate of growth or decay and possesses unique analytical properties that simplify calculus and connect diverse areas of mathematics and science.

---
````

Filename: 150_Mathematics/Functions/argmax_argmin.md
````markdown
---
tags: [mathematics, functions, optimization, argmax, argmin, concept]
aliases: [Argument of the Maximum, Argument of the Minimum]
related:
  - "[[_Functions_MOC]]"
  - "[[Calculus_Optimization]]"
  - "[[Set_Theory_Notation]]" # Notation for sets
worksheet: [WS_Math_Foundations_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Argmax and Argmin

## Definition
$\text{argmax}$ (argument of the maximum) and $\text{argmin}$ (argument of the minimum) are mathematical operators that return the input value(s) (arguments) at which a function achieves its maximum or minimum value, respectively.

They are different from $\max$ and $\min$, which return the maximum or minimum value of the function itself.

- **$\text{argmax}_x f(x)$:** Returns the value(s) of $x$ from the domain of $f$ for which $f(x)$ is maximized.
  $$ \underset{x}{\text{argmax}} \, f(x) = \{ x \in \text{Domain}(f) \mid f(x) = \max_{x' \in \text{Domain}(f)} f(x') \} $$
  Often, if the maximum is unique, $\text{argmax}$ is treated as returning a single value rather than a set.

- **$\text{argmin}_x f(x)$:** Returns the value(s) of $x$ from the domain of $f$ for which $f(x)$ is minimized.
  $$ \underset{x}{\text{argmin}} \, f(x) = \{ x \in \text{Domain}(f) \mid f(x) = \min_{x' \in \text{Domain}(f)} f(x') \} $$
  Similarly, if the minimum is unique, $\text{argmin}$ is often treated as returning a single value.

The subscript under $\text{arg max}$ or $\text{arg min}$ indicates the variable(s) over which the optimization is performed. The domain can be continuous (e.g., $\mathbb{R}$) or discrete (e.g., a finite set of indices).

## Is argmax/argmin a function? How would you define its signature?

>[!question] Is argmax a function? How would you define its signature (with type hints)?
>Yes, $\text{argmax}$ (and $\text{argmin}$) can be considered a **higher-order function** or an **operator** that takes a function as input and returns element(s) from the domain of that input function.
>
>Defining a precise signature with standard type hints can be a bit nuanced because:
>1.  The domain of the input function $f$ can vary (e.g., real numbers, integers, discrete sets, vectors).
>2.  The output can be a single value or a set of values if the maximum/minimum is achieved at multiple points.
>
>Let's try to define a general signature, assuming Python-like type hints for illustration.
>
>Let $S$ be the type of the domain of $f$, and $T$ be the type of the codomain of $f$ (where $T$ must be orderable to find a max/min).
>
>**Signature for $\text{argmax}$ (returning a single value, assuming unique max or a rule for ties):**
>```python
>from typing import Callable, TypeVar, Set, Union
>
>S = TypeVar('S') # Type of the domain elements
>T = TypeVar('T') # Type of the codomain elements (must be comparable)
>
>def argmax(f: Callable[[S], T], domain: Set[S]) -> S:
>    # Implementation would find x in domain such that f(x) is maximized.
>    # Handling of ties (e.g., return first one found, or raise error) would be part of impl.
>    pass
>```
>
>**Signature for $\text{argmax}$ (returning a set of values):**
>```python
>def argmax_set(f: Callable[[S], T], domain: Set[S]) -> Set[S]:
>    # Implementation would find all x in domain such that f(x) is maximized.
>    pass
>```
>
>**Contextual Usage (More Common):**
>Often, $\text{argmax}$ is used in a specific context where the domain is implicit or clearly defined. For example, if $f$ is a function of a real variable $x$, $\text{argmax}_x f(x)$ implies the domain is $\mathbb{R}$ or a relevant subset. If applied to a discrete list or array, the domain is the set of indices.
>
>Example for a list of numbers (returning the index):
>```python
>from typing import List, TypeVar
>
>ComparableT = TypeVar('ComparableT') # Any comparable type
>
>def argmax_list_index(values: List[ComparableT]) -> int:
>    if not values:
>        raise ValueError("Cannot find argmax of an empty list")
>    max_val = values[0]
>    max_idx = 0
>    for i in range(1, len(values)):
>        if values[i] > max_val:
>            max_val = values[i]
>            max_idx = i
>    return max_idx
>```
>In this case, the function $f$ is implicitly $f(i) = \text{values}[i]$, and the domain is $\{0, 1, \dots, \text{len(values)-1}\}$.
>
>So, while it is a function/operator, its precise "type signature" in a universal sense depends on how strictly one defines the input domain and output (single value vs. set). The concept, however, is clear: it returns the *input argument(s)* that lead to the extremum, not the extremum value itself.

## Examples
1.  **Continuous Function:**
    Let $f(x) = -(x-2)^2 + 5$. This is a parabola opening downwards with a vertex at $(2,5)$.
    - $\max_x f(x) = 5$
    - $\underset{x}{\text{argmax}} \, f(x) = 2$

2.  **Discrete Set (List):**
    Let $L =$.
    - $\max(L) = 50$
    - $\underset{i}{\text{argmax}} \, L_i = \{1, 3\}$ (if using 0-based indexing, assuming $L_i$ is the $i$-th element).
      Often, one might just return the first index found, e.g., $1$.

3.  **Probability Distribution:**
    Let $P(C_k | X)$ be the posterior probability of class $C_k$ given data $X$. The classification rule is often:
    $$ \hat{C} = \underset{k}{\text{argmax}} \, P(C_k | X) $$
    This assigns the class $\hat{C}$ that has the highest posterior probability. Here, the "function" is $P(\cdot | X)$ and the "argument" is the class index $k$.

## Applications
- **Machine Learning:**
    - **Classification:** Assigning an input to the class with the highest predicted probability or score (as shown above). The output of a [[Softmax_Function|softmax layer]] in a neural network is a probability distribution, and $\text{argmax}$ is used to select the predicted class.
    - **Reinforcement Learning:** Selecting the action that maximizes the expected future reward (Q-value).
      $a^* = \underset{a}{\text{argmax}} \, Q(s,a)$
    - **Model Selection:** Choosing model parameters that maximize a likelihood function or minimize a loss function (though here we often seek the parameters themselves, which is an $\text{argmin}$ or $\text{argmax}$ problem).
- **Optimization:** Finding the input parameters that optimize an objective function is inherently an $\text{argmin}$ or $\text{argmax}$ problem (see [[Calculus_Optimization]]).
- **Statistics:**
    - **Maximum Likelihood Estimation (MLE):** $\hat{\theta}_{MLE} = \underset{\theta}{\text{argmax}} \, \mathcal{L}(\theta | \text{data})$, where $\mathcal{L}$ is the likelihood function.
    - **Mode of a Distribution:** For a discrete probability distribution, the mode is the value with the highest probability: $\text{mode} = \underset{x}{\text{argmax}} \, P(X=x)$.
- **Signal Processing:** Finding the time or frequency at which a signal has maximum power.
- **Computer Vision:** Finding the location of an object or feature with the highest response from a detector.

## Note on Uniqueness and Sets
If the maximum (or minimum) value is achieved at multiple input points, $\text{argmax}$ (or $\text{argmin}$) technically refers to the set of all such points. In practice, especially in computational contexts, a single value from this set might be returned (e.g., the first one encountered, or the smallest index). The precise behavior depends on the implementation or convention.

---
````

Filename: 150_Mathematics/Functions/Logit_Function.md
````markdown
---
tags: [mathematics, functions, logit, log_odds, probability, statistics, machine_learning, concept]
aliases: [Log-odds Function]
related:
  - "[[_Functions_MOC]]"
  - "[[Logarithmic_Function]]" # Uses natural logarithm
  - "[[Sigmoid_Function]]" # Inverse of logit
  - "[[Odds]]"
  - "[[Probability]]"
  - "[[Logistic_Regression]]"
worksheet: [WS_Math_Foundations_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Logit Function (Log-odds)

## Definition
The **logit function**, also known as the **log-odds function**, is the logarithm of the [[Odds|odds]]. It maps a probability $p$ (which is in the range $$) to the entire real number line $(-\infty, \infty)$.

The logit function is defined as:
$$ \text{logit}(p) = \ln\left(\frac{p}{1-p}\right) $$
where:
- $p$ is a probability, $0 < p < 1$.
- $\ln$ is the [[Logarithmic_Function|natural logarithm]].
- $\frac{p}{1-p}$ are the **[[Odds|odds]]** in favor of the event with probability $p$.

The function is undefined for $p=0$ and $p=1$ (as it would involve $\ln(0)$ or division by zero).

## Relationship to Odds

>[!question] What are odds and how do they relate to the logit function?
>
>**[[Odds|Odds]]:**
>In probability theory, the **odds** of an event occurring are the ratio of the probability of the event occurring to the probability of the event not occurring.
>If $p$ is the probability of an event, then the odds in favor of the event are:
>$$ \text{Odds}(p) = \frac{p}{1-p} $$
>
>- If $p = 0.5$ (50% chance), Odds = $\frac{0.5}{1-0.5} = \frac{0.5}{0.5} = 1$ (often expressed as "1 to 1" or "even odds").
>- If $p = 0.8$ (80% chance), Odds = $\frac{0.8}{1-0.8} = \frac{0.8}{0.2} = 4$ (often "4 to 1 in favor").
>- If $p = 0.2$ (20% chance), Odds = $\frac{0.2}{1-0.2} = \frac{0.2}{0.8} = 0.25$ (often "1 to 4 in favor", or "4 to 1 against").
>
>The range of odds is $(0, \infty)$ for $0 < p < 1$.
>
>**Relationship to Logit:**
>The logit function is simply the natural logarithm of the odds:
>$$ \text{logit}(p) = \ln(\text{Odds}(p)) = \ln\left(\frac{p}{1-p}\right) $$
>Taking the logarithm transforms the odds (which range from $0$ to $\infty$) to the log-odds (which range from $-\infty$ to $\infty$).
>
>- If $p = 0.5$, Odds = 1, $\text{logit}(0.5) = \ln(1) = 0$.
>- If $p > 0.5$, Odds > 1, $\text{logit}(p) = \ln(\text{Odds}) > 0$.
>- If $p < 0.5$, Odds < 1, $\text{logit}(p) = \ln(\text{Odds}) < 0$.

## Properties
- **Domain:** $(0, 1)$ (probabilities, excluding 0 and 1)
- **Range:** $(-\infty, \infty)$ (all real numbers)
- **Symmetry:** The logit function is antisymmetric about $p=0.5$ in the sense that $\text{logit}(1-p) = \ln\left(\frac{1-p}{p}\right) = -\ln\left(\frac{p}{1-p}\right) = -\text{logit}(p)$.
- **Inverse Function:** The inverse of the logit function is the **[[Sigmoid_Function|standard logistic sigmoid function]]** $\sigma(x) = \frac{1}{1+e^{-x}}$.
  If $L = \text{logit}(p)$, then $p = \sigma(L) = \frac{1}{1+e^{-L}}$.
  Proof:
  $L = \ln\left(\frac{p}{1-p}\right)$
  $e^L = \frac{p}{1-p}$
  $e^L(1-p) = p$
  $e^L - e^L p = p$
  $e^L = p(1 + e^L)$
  $p = \frac{e^L}{1 + e^L} = \frac{1}{e^{-L} + 1} = \sigma(L)$.

## Graph of $y = \text{logit}(p)$

```mermaid
graph TD
    subgraph LogitGraph["Graph of y = logit(p)"]
        XAxis["p (probability, 0 to 1)"] --- YAxis["y (log-odds, -∞ to +∞)"]
        P0_5((0.5, 0))
        P0_1((0.1, "$logit(0.1) \approx -2.2$"))
        P0_9((0.9, "$logit(0.9) \approx 2.2$"))
        
        Asymptote0["p=0 (y → -∞)"] -.-> P0_1
        P0_1 --- P0_5 --- P0_9 % Curve path
        Asymptote1["p=1 (y → +∞)"] -.-> P0_9
    end
    P0_5 -->|logit(0.5) = 0| P0_5
    
    style P0_5 fill:#afa,stroke:#333,stroke-width:2px
    style P0_1 fill:#aaf,stroke:#333,stroke-width:2px
    style P0_9 fill:#aaf,stroke:#333,stroke-width:2px
    linkStyle 3 stroke-width:2px,fill:none,stroke:blue;
    linkStyle 4 stroke-width:2px,fill:none,stroke:blue,stroke-dasharray: 5 5;
    linkStyle 6 stroke-width:2px,fill:none,stroke:blue,stroke-dasharray: 5 5;
```

## Applications
- **[[Logistic_Regression|Logistic Regression]]:**
    - This is the primary application. Logistic regression models the logit of the probability of a binary outcome as a linear combination of predictor variables:
      $$ \text{logit}(P(Y=1|\mathbf{X})) = \ln\left(\frac{P(Y=1|\mathbf{X})}{1-P(Y=1|\mathbf{X})}\right) = \beta_0 + \beta_1 X_1 + \dots + \beta_k X_k $$
    - By modeling the log-odds as linear, the probability $P(Y=1|\mathbf{X})$ is constrained to be between 0 and 1 via the sigmoid function (which is the inverse of logit).
- **Statistics:**
    - Used in the analysis of binomial data.
    - Transformation for data that represents proportions or probabilities to make them suitable for linear modeling or to stabilize variance.
- **Information Theory:** Related to log-likelihood ratios.
- **Measurement Theory (Rasch model):** Used in psychometrics to model the probability of a correct response based on person ability and item difficulty.

## Advantages of Using Logit Transformation
- **Maps Probability to Real Line:** Transforms a variable bounded in $(0,1)$ to one that can take any real value. This is useful because linear models predict values across the entire real line.
- **Interpretable Coefficients (in Logistic Regression):** Exponentiating a coefficient $\beta_j$ from a logistic regression model, $e^{\beta_j}$, gives the **odds ratio** associated with a one-unit increase in the predictor $X_j$, holding other predictors constant. An odds ratio indicates how the odds of the outcome change.
    - If $\beta_j > 0 \implies e^{\beta_j} > 1 \implies$ odds increase.
    - If $\beta_j < 0 \implies 0 < e^{\beta_j} < 1 \implies$ odds decrease.
    - If $\beta_j = 0 \implies e^{\beta_j} = 1 \implies$ no change in odds.
- **Symmetry:** Treats probabilities symmetrically around 0.5 (e.g., logit(0.2) = -logit(0.8)).

## Example Calculation
If probability $p = 0.8$:
- Odds = $\frac{0.8}{1-0.8} = \frac{0.8}{0.2} = 4$.
- $\text{logit}(0.8) = \ln(4) \approx 1.386$.

If log-odds $L = -1.0$:
- Probability $p = \sigma(-1.0) = \frac{1}{1+e^{-(-1.0)}} = \frac{1}{1+e^1} = \frac{1}{1+2.71828} = \frac{1}{3.71828} \approx 0.2689$.

---````

Filename: 150_Mathematics/Linear_Algebra/Orthogonal_Matrix.md
````markdown
---
tags: [mathematics, linear_algebra, matrix, orthogonal_matrix, orthonormal_basis, concept]
aliases: [Orthonormal Matrix] # Technically, columns/rows are orthonormal
related:
  - "[[Matrix]]"
  - "[[Vector]]"
  - "[[Dot_Product]]"
  - "[[p-norm]]" # L2 norm
  - "[[Transpose_Matrix]]"
  - "[[Matrix_Inversion]]"
  - "[[Transformation_Matrix]]" # Represents rotations, reflections
  - "[[Singular_Value_Decomposition]]" # U and V are orthogonal
  - "[[Eigenvalues_Eigenvectors]]" # Eigenvectors of symmetric matrices can form an orthogonal matrix
worksheet: [WS_Math_Foundations_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Orthogonal Matrix

## Definition
A **square [[Matrix|matrix]]** $\mathbf{Q}$ with real entries is called an **orthogonal matrix** if its columns (and rows) are [[Orthogonal_Vectors|orthogonal]] unit [[Vector|vectors]] (i.e., an orthonormal set of vectors). Equivalently, a matrix $\mathbf{Q}$ is orthogonal if its [[Transpose_Matrix|transpose]] is equal to its [[Matrix_Inversion|inverse]]:

$$ \mathbf{Q}^T = \mathbf{Q}^{-1} $$

This defining property can also be expressed as:
$$ \mathbf{Q}^T \mathbf{Q} = \mathbf{Q} \mathbf{Q}^T = \mathbf{I} $$
where $\mathbf{I}$ is the identity matrix.

## Properties
Let $\mathbf{Q}$ be an $n \times n$ orthogonal matrix.
1.  **Inverse is Transpose:** $\mathbf{Q}^{-1} = \mathbf{Q}^T$. This makes computing the inverse of an orthogonal matrix very easy.
2.  **Orthonormal Columns:** The columns of $\mathbf{Q}$ form an orthonormal basis for $\mathbb{R}^n$. This means:
    - Each column vector has an L2 [[p-norm|norm]] (length) of 1: $\|\mathbf{q}_j\|_2 = 1$.
    - Any two distinct column vectors $\mathbf{q}_i, \mathbf{q}_j$ (where $i \neq j$) are [[Orthogonal_Vectors|orthogonal]], meaning their [[Dot_Product|dot product]] is zero: $\mathbf{q}_i \cdot \mathbf{q}_j = \mathbf{q}_i^T \mathbf{q}_j = 0$.
3.  **Orthonormal Rows:** Similarly, the rows of $\mathbf{Q}$ also form an orthonormal basis for $\mathbb{R}^n$.
4.  **Preserves Dot Products (and Angles):** For any vectors $\mathbf{x}, \mathbf{y} \in \mathbb{R}^n$:
    $$ (\mathbf{Q}\mathbf{x}) \cdot (\mathbf{Q}\mathbf{y}) = (\mathbf{Q}\mathbf{x})^T (\mathbf{Q}\mathbf{y}) = \mathbf{x}^T \mathbf{Q}^T \mathbf{Q} \mathbf{y} = \mathbf{x}^T \mathbf{I} \mathbf{y} = \mathbf{x}^T \mathbf{y} = \mathbf{x} \cdot \mathbf{y} $$
    Since dot products are preserved, angles between vectors are also preserved.
5.  **Preserves Lengths (L2 Norms):** A special case of preserving dot products (let $\mathbf{y}=\mathbf{x}$):
    $$ \|\mathbf{Q}\mathbf{x}\|_2^2 = (\mathbf{Q}\mathbf{x}) \cdot (\mathbf{Q}\mathbf{x}) = \mathbf{x} \cdot \mathbf{x} = \|\mathbf{x}\|_2^2 $$
    So, $\|\mathbf{Q}\mathbf{x}\|_2 = \|\mathbf{x}\|_2$. Orthogonal transformations are isometries; they preserve distances.
6.  **[[Determinant_Matrix|Determinant]]:** $\det(\mathbf{Q}) = \pm 1$.
    - If $\det(\mathbf{Q}) = 1$, $\mathbf{Q}$ represents a **rotation** (a proper orthogonal transformation).
    - If $\det(\mathbf{Q}) = -1$, $\mathbf{Q}$ represents a **reflection** or an improper rotation (a rotation followed by a reflection).
7.  **[[Eigenvalues_Eigenvectors|Eigenvalues]]:** The eigenvalues of an orthogonal matrix all have an absolute value (modulus) of 1 (i.e., $|\lambda|=1$). They can be real ($\pm 1$) or complex (on the unit circle in the complex plane).
8.  **Product of Orthogonal Matrices:** If $\mathbf{Q}_1$ and $\mathbf{Q}_2$ are orthogonal matrices, then their product $\mathbf{Q}_1\mathbf{Q}_2$ is also an orthogonal matrix.
    $(\mathbf{Q}_1\mathbf{Q}_2)^T (\mathbf{Q}_1\mathbf{Q}_2) = \mathbf{Q}_2^T \mathbf{Q}_1^T \mathbf{Q}_1 \mathbf{Q}_2 = \mathbf{Q}_2^T \mathbf{I} \mathbf{Q}_2 = \mathbf{Q}_2^T \mathbf{Q}_2 = \mathbf{I}$.

## Examples
1.  **2D Rotation Matrix:**
    $$ \mathbf{R}(\theta) = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix} $$
    Check: $\mathbf{R}^T\mathbf{R} = \begin{pmatrix} \cos \theta & \sin \theta \\ -\sin \theta & \cos \theta \end{pmatrix} \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix} = \begin{pmatrix} \cos^2\theta+\sin^2\theta & 0 \\ 0 & \sin^2\theta+\cos^2\theta \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \mathbf{I}$.
    $\det(\mathbf{R}(\theta)) = \cos^2\theta - (-\sin^2\theta) = \cos^2\theta + \sin^2\theta = 1$. (Rotation)

2.  **Reflection Matrix (across y-axis in 2D):**
    $$ \mathbf{F}_y = \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix} $$
    $\mathbf{F}_y^T\mathbf{F}_y = \mathbf{F}_y\mathbf{F}_y = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \mathbf{I}$. (Since $\mathbf{F}_y$ is symmetric, $\mathbf{F}_y^T = \mathbf{F}_y$).
    $\det(\mathbf{F}_y) = (-1)(1) - (0)(0) = -1$. (Reflection)

3.  **Permutation Matrix:** A matrix obtained by permuting the rows/columns of an identity matrix. It is orthogonal.
    Example: $\mathbf{P} = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{pmatrix}$. $\det(\mathbf{P})$ can be $\pm 1$.

## Applications
- **[[Transformation_Matrix|Geometric Transformations]]:** Representing rotations and reflections in computer graphics, robotics, and physics.
- **[[Singular_Value_Decomposition|Singular Value Decomposition (SVD)]]:** The matrices $\mathbf{U}$ and $\mathbf{V}$ in $\mathbf{A} = \mathbf{U}\mathbf{\Sigma}\mathbf{V}^T$ are orthogonal.
- **QR Decomposition:** Any real square matrix $\mathbf{A}$ can be decomposed as $\mathbf{A} = \mathbf{Q}\mathbf{R}$, where $\mathbf{Q}$ is an orthogonal matrix and $\mathbf{R}$ is an upper triangular matrix. Used in solving linear systems and eigenvalue problems.
- **Change of Basis:** Orthogonal matrices are used to change from one orthonormal basis to another. If $\mathbf{q}_1, \dots, \mathbf{q}_n$ is an orthonormal basis, data represented in this basis can be easily transformed back to the standard basis using the matrix $\mathbf{Q} = [\mathbf{q}_1 | \dots | \mathbf{q}_n]$.
- **[[Principal_Component_Analysis_PCA|Principal Component Analysis (PCA)]]:** The transformation matrix in PCA (formed by principal component eigenvectors) is orthogonal.
- **Signal Processing:** Used in various transforms like Discrete Cosine Transform (DCT), which is related to orthogonal matrices.
- **Numerical Stability:** Orthogonal transformations are numerically stable because they do not amplify errors (they preserve norms). This makes them desirable in many numerical algorithms.

## Unitary Matrix (Complex Analogue)
For complex matrices, the analogue of an orthogonal matrix is a **unitary matrix** $\mathbf{U}$, which satisfies $\mathbf{U}^* \mathbf{U} = \mathbf{U} \mathbf{U}^* = \mathbf{I}$, where $\mathbf{U}^*$ is the conjugate transpose (Hermitian transpose) of $\mathbf{U}$.

---
````

Filename: 150_Mathematics/Functions/Unit_Circle.md
````markdown
---
tags: [mathematics, trigonometry, geometry, unit_circle, concept]
aliases: [Trigonometric Circle]
related:
  - "[[Trigonometric_Functions]]" # Sine, Cosine defined using unit circle
  - "[[Angles_Radians_Degrees]]"
  - "[[Complex_Numbers_Euler_Formula]]" # Points on unit circle in complex plane
worksheet: [WS_Math_Foundations_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Unit Circle

## Definition
The **unit circle** is a circle of radius 1 centered at the origin $(0,0)$ in the Cartesian coordinate system. Its equation is:
$$ x^2 + y^2 = 1 $$

The unit circle is fundamental in trigonometry for defining the [[Trigonometric_Functions|trigonometric functions]] (sine, cosine, tangent, etc.) for all real-numbered angles.

## Defining Trigonometric Functions using the Unit Circle
Consider a point $P(x,y)$ on the unit circle. Let $\theta$ be the angle measured in [[Angles_Radians_Degrees|radians]] (or degrees) counter-clockwise from the positive x-axis to the line segment connecting the origin $O$ to the point $P$.

Then, the trigonometric functions are defined as:
- **Cosine ($\cos \theta$):** The x-coordinate of the point $P$.
  $$ \cos \theta = x $$
- **Sine ($\sin \theta$):** The y-coordinate of the point $P$.
  $$ \sin \theta = y $$
- **Tangent ($\tan \theta$):** The ratio of the y-coordinate to the x-coordinate.
  $$ \tan \theta = \frac{y}{x} = \frac{\sin \theta}{\cos \theta} \quad (\text{provided } x = \cos \theta \neq 0) $$

Other trigonometric functions can also be defined:
- **Secant ($\sec \theta$):** $\sec \theta = \frac{1}{x} = \frac{1}{\cos \theta}$
- **Cosecant ($\csc \theta$):** $\csc \theta = \frac{1}{y} = \frac{1}{\sin \theta}$
- **Cotangent ($\cot \theta$):** $\cot \theta = \frac{x}{y} = \frac{\cos \theta}{\sin \theta}$

## Visualization

```mermaid
graph LR
    subgraph CartesianPlane ["Unit Circle in Cartesian Plane"]
        direction LR
        Origin((0,0)) --- XPosAxis((" "))
        Origin --- YPosAxis((" "))
        
        P([P(cos θ, sin θ)])
        CirclePath{"x²+y²=1"} -- forms --- P
        
        Origin -- "radius=1" --- P
        
        subgraph AngleTheta
            direction TB
            XPosAxis -- "θ" --- P
        end

        P -- "y = sin θ" --> XProjection((cos θ, 0))
        XProjection -- "x = cos θ" --> Origin
        
        note right of P : Angle θ is measured<br/>counter-clockwise<br/>from positive x-axis.
    end

    style Origin fill:#ccc,stroke:#333,stroke-width:1px
    style P fill:#afa,stroke:#000,stroke-width:2px
    style XPosAxis stroke-dasharray: 5 5
    style YPosAxis stroke-dasharray: 5 5
    style CirclePath fill:none,stroke:#369,stroke-width:3px,interpolate:basis
    style XProjection fill:#ccc,stroke:#333,stroke-width:1px
```

## Key Values and Quadrants
The signs of sine, cosine, and tangent depend on the quadrant in which the angle $\theta$ terminates:

| Quadrant | Angle Range (Radians) | Angle Range (Degrees) | $\cos \theta$ (x) | $\sin \theta$ (y) | $\tan \theta$ (y/x) | Mnemonic |
|----------|-----------------------|-----------------------|-------------------|-------------------|---------------------|------------|
| I        | $0 < \theta < \pi/2$  | $0^\circ < \theta < 90^\circ$   | $+$               | $+$               | $+$                 | **A**ll    |
| II       | $\pi/2 < \theta < \pi$| $90^\circ < \theta < 180^\circ$ | $-$               | $+$               | $-$                 | **S**ine   |
| III      | $\pi < \theta < 3\pi/2$|$180^\circ < \theta < 270^\circ$| $-$               | $-$               | $+$                 | **T**angent|
| IV       | $3\pi/2 < \theta < 2\pi$|$270^\circ < \theta < 360^\circ$| $+$               | $-$               | $-$                 | **C**osine |
(Mnemonic: "All Students Take Calculus" or "ASTC" tells which functions are positive in each quadrant).

**Common Angles and Coordinates:**
[list2mdtable|#Common Angle Coordinates on Unit Circle]
- Angle ($\theta$)
    - $x = \cos \theta$
        - $y = \sin \theta$
- $0 \text{ rad } (0^\circ)$
    - $1$
        - $0$
- $\pi/6 \text{ rad } (30^\circ)$
    - $\frac{\sqrt{3}}{2} \approx 0.866$
        - $\frac{1}{2} = 0.5$
- $\pi/4 \text{ rad } (45^\circ)$
    - $\frac{\sqrt{2}}{2} \approx 0.707$
        - $\frac{\sqrt{2}}{2} \approx 0.707$
- $\pi/3 \text{ rad } (60^\circ)$
    - $\frac{1}{2} = 0.5$
        - $\frac{\sqrt{3}}{2} \approx 0.866$
- $\pi/2 \text{ rad } (90^\circ)$
    - $0$
        - $1$
- $\pi \text{ rad } (180^\circ)$
    - $-1$
        - $0$
- $3\pi/2 \text{ rad } (270^\circ)$
    - $0$
        - $-1$
- $2\pi \text{ rad } (360^\circ)$
    - $1$
        - $0$

## Pythagorean Identity
Since $(x,y)$ is on the unit circle $x^2+y^2=1$, substituting $x=\cos\theta$ and $y=\sin\theta$ gives the fundamental Pythagorean identity:
$$ \cos^2 \theta + \sin^2 \theta = 1 $$

## Periodicity
Trigonometric functions are periodic because angles "wrap around" the unit circle. Adding $2\pi$ radians ($360^\circ$) to an angle results in the same point $P(x,y)$ on the unit circle.
- $\sin(\theta + 2k\pi) = \sin \theta$
- $\cos(\theta + 2k\pi) = \cos \theta$
- $\tan(\theta + k\pi) = \tan \theta$ (tangent has period $\pi$)
(where $k$ is an integer).

## Applications
- **Foundation of Trigonometry:** Provides a comprehensive definition for trigonometric functions for all angles, not just acute angles in triangles.
- **Understanding Periodic Phenomena:** Visualizing oscillations, waves (e.g., [[Fourier_Series_Transforms|Fourier analysis]]).
- **[[Complex_Numbers_Euler_Formula|Complex Numbers]]:** A complex number $z = x + iy$ with modulus 1 can be written as $z = \cos\theta + i\sin\theta = e^{i\theta}$, representing a point on the unit circle in the complex plane.
- **Geometry and Navigation:** Used in coordinate transformations, rotations.
- **Physics and Engineering:** Analyzing circular motion, oscillations, AC circuits.

The unit circle provides a powerful visual and conceptual tool for understanding the behavior and relationships of trigonometric functions.

---
````

Filename: 150_Mathematics/Functions/Angles_Radians_Degrees.md
````markdown
---
tags: [mathematics, trigonometry, geometry, angles, radians, degrees, measurement, concept]
aliases: [Angle Measurement, Radian Measure, Degree Measure, Angle Conversion]
related:
  - "[[Unit_Circle]]"
  - "[[Trigonometric_Functions]]"
worksheet: [WS_Math_Foundations_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Angle Measurement: Radians and Degrees

Angles are a fundamental concept in geometry and trigonometry, quantifying the amount of rotation between two intersecting lines or rays. There are two primary units for measuring angles: **degrees** and **radians**.

## Degrees ($^\circ$)
- **Definition:** A degree is a unit of angle measure defined such that a full rotation (a complete circle) is $360$ degrees.
- **Symbol:** $^\circ$
- **Subdivisions:**
    - 1 degree ($1^\circ$) = 60 minutes ($60'$)
    - 1 minute ($1'$) = 60 seconds ($60''$)
- **Common Angles in Degrees:**
    - Right angle: $90^\circ$
    - Straight angle: $180^\circ$
    - Full circle: $360^\circ$
- **Origin:** The choice of $360$ degrees for a full circle dates back to ancient Babylonians, possibly due to its divisibility by many small integers (1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 60, 72, 90, 120, 180, 360) or its approximation to the number of days in a year.

## Radians (rad)
- **Definition:** A radian is the standard unit of angular measure used in many areas of mathematics. An angle's measurement in radians is numerically equal to the length of a corresponding arc of a [[Unit_Circle|unit circle]] (a circle with radius 1).
- More generally, for any circle, an angle of 1 radian subtends an arc whose length is equal to the radius of the circle.
  $$ \theta_{\text{radians}} = \frac{\text{arc length } (s)}{\text{radius } (r)} $$
- **Symbol:** rad (often omitted when context is clear, especially in formulas).
- **Common Angles in Radians:**
    - Right angle: $\frac{\pi}{2}$ rad
    - Straight angle: $\pi$ rad
    - Full circle: $2\pi$ rad
- **Why Radians?**
    - Radians are the "natural" unit for angles in calculus and higher mathematics because they simplify many formulas, particularly involving [[Trigonometric_Functions|trigonometric functions]] and their [[Calculus_Derivatives|derivatives]] and [[Calculus_Integrals|integrals]].
    - For example, $\frac{d}{dx} \sin x = \cos x$ only holds if $x$ is in radians. If $x$ were in degrees, a conversion factor would appear.
    - Series expansions for trigonometric functions (e.g., Taylor series) are simpler when using radians.

## Conversion Between Degrees and Radians
Since a full circle is $360^\circ$ and also $2\pi$ radians:
$$ 360^\circ = 2\pi \text{ rad} $$
$$ 180^\circ = \pi \text{ rad} $$

From this, we get the conversion factors:
- **Degrees to Radians:**
  Multiply the angle in degrees by $\frac{\pi}{180^\circ}$.
  $$ \text{Angle in radians} = \text{Angle in degrees} \times \frac{\pi}{180} $$
  Example: Convert $60^\circ$ to radians: $60 \times \frac{\pi}{180} = \frac{60\pi}{180} = \frac{\pi}{3}$ radians.

- **Radians to Degrees:**
  Multiply the angle in radians by $\frac{180^\circ}{\pi}$.
  $$ \text{Angle in degrees} = \text{Angle in radians} \times \frac{180}{\pi} $$
  Example: Convert $\frac{3\pi}{4}$ radians to degrees: $\frac{3\pi}{4} \times \frac{180}{\pi} = \frac{3 \times 180}{4} = 3 \times 45 = 135^\circ$.

## Table of Common Angle Conversions
[list2mdtable|#Common Angle Conversions]
- Degrees
    - Radians (Exact)
        - Radians (Approx.)
- $0^\circ$
    - $0$
        - $0$
- $30^\circ$
    - $\frac{\pi}{6}$
        - $0.5236$
- $45^\circ$
    - $\frac{\pi}{4}$
        - $0.7854$
- $60^\circ$
    - $\frac{\pi}{3}$
        - $1.0472$
- $90^\circ$
    - $\frac{\pi}{2}$
        - $1.5708$
- $120^\circ$
    - $\frac{2\pi}{3}$
        - $2.0944$
- $135^\circ$
    - $\frac{3\pi}{4}$
        - $2.3562$
- $150^\circ$
    - $\frac{5\pi}{6}$
        - $2.6180$
- $180^\circ$
    - $\pi$
        - $3.14159$
- $270^\circ$
    - $\frac{3\pi}{2}$
        - $4.7124$
- $360^\circ$
    - $2\pi$
        - $6.28318$

## Usage Context
- **Degrees:** Commonly used in everyday applications, navigation, surveying, and some engineering fields due to historical reasons and easy subdivision.
- **Radians:** Preferred in mathematics (especially calculus), physics, computer science (for trigonometric function implementations in libraries), and engineering fields where mathematical analysis is intensive. Most scientific calculators and programming languages use radians by default for trigonometric functions.

When working with trigonometric functions in code (e.g., `math.sin()` in Python), it's crucial to know whether the function expects its argument in degrees or radians (Python's `math` module functions expect radians).

---
````

Filename: 150_Mathematics/Functions/Complex_Numbers_Euler_Formula.md
````markdown
---
tags: [mathematics, complex_numbers, euler_formula, exponential_function, trigonometric_functions, concept]
aliases: [Euler's Formula, Euler's Identity]
related:
  - "[[Complex_Numbers]]"
  - "[[Exponential_Function]]"
  - "[[Trigonometric_Functions]]"
  - "[[Unit_Circle]]"
  - "[[Euler_Number_e]]"
worksheet: [WS_Math_Foundations_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Complex Numbers and Euler's Formula

## Complex Numbers (Brief Recap)
A **[[Complex_Numbers|complex number]]** $z$ is a number of the form $z = a + bi$, where $a$ and $b$ are real numbers, and $i$ is the imaginary unit, satisfying $i^2 = -1$.
- $a = \text{Re}(z)$ is the real part.
- $b = \text{Im}(z)$ is the imaginary part.

Complex numbers can be represented on a 2D plane called the **complex plane** (or Argand diagram), where the x-axis represents the real part and the y-axis represents the imaginary part.

A complex number $z = a+bi$ can also be represented in **polar form**:
$$ z = r(\cos \theta + i \sin \theta) $$
where:
- $r = |z| = \sqrt{a^2 + b^2}$ is the **modulus** (or magnitude) of $z$.
- $\theta = \text{arg}(z)$ is the **argument** (or angle, phase) of $z$, measured counter-clockwise from the positive real axis.

## Euler's Formula

Euler's formula, named after Leonhard Euler, establishes a fundamental relationship between the [[Exponential_Function|natural exponential function]] (with an imaginary argument) and the [[Trigonometric_Functions|trigonometric functions]] sine and cosine.

For any real number $x$ (representing an angle in radians), Euler's formula states:
$$ e^{ix} = \cos x + i \sin x $$
where:
- $e$ is [[Euler_Number_e|Euler's number]], the base of the natural logarithm.
- $i$ is the imaginary unit.
- $\cos x$ and $\sin x$ are the trigonometric functions cosine and sine, with $x$ in radians.

**Geometric Interpretation:**
The complex number $e^{ix}$ represents a point on the [[Unit_Circle|unit circle]] in the complex plane. Its real part is $\cos x$ and its imaginary part is $\sin x$. The angle this point makes with the positive real axis is $x$ radians.

```mermaid
graph TD
    subgraph ComplexPlane["e^(ix) on Unit Circle in Complex Plane"]
        Origin((0,0 Real/Imaginary)) --- RealAxisEnd((1,0))
        P(("cos x + i sin x"))
        
        Origin -- "modulus |e^(ix)| = 1" --- P
        
        subgraph Angle_x
            direction TB
            RealAxisEnd -- "angle x" --- P
        end

        P -- "Im(e^(ix)) = sin x" --> ProjReal((cos x, 0))
        ProjReal -- "Re(e^(ix)) = cos x" --> Origin
    end
    note right of P : e^(ix) is a point on<br/>the unit circle.
    style P fill:#afa,stroke:#000,stroke-width:2px
    style ProjReal fill:#ccc
```

## Derivations from Euler's Formula
Euler's formula can be used to express sine and cosine in terms of complex exponentials:
From $e^{ix} = \cos x + i \sin x$ and $e^{-ix} = \cos(-x) + i \sin(-x) = \cos x - i \sin x$:

1.  **Cosine:**
    Adding the two equations:
    $e^{ix} + e^{-ix} = (\cos x + i \sin x) + (\cos x - i \sin x) = 2 \cos x$
    $$ \cos x = \frac{e^{ix} + e^{-ix}}{2} $$

2.  **Sine:**
    Subtracting the second equation from the first:
    $e^{ix} - e^{-ix} = (\cos x + i \sin x) - (\cos x - i \sin x) = 2i \sin x$
    $$ \sin x = \frac{e^{ix} - e^{-ix}}{2i} $$

These expressions are crucial in fields like signal processing (Fourier analysis) and quantum mechanics.

## Euler's Identity
A famous special case of Euler's formula occurs when $x = \pi$:
$$ e^{i\pi} = \cos \pi + i \sin \pi $$
Since $\cos \pi = -1$ and $\sin \pi = 0$:
$$ e^{i\pi} = -1 + i(0) = -1 $$
Rearranging this gives **Euler's identity**:
$$ e^{i\pi} + 1 = 0 $$
This remarkable equation links five of the most important constants in mathematics:
- $e$ (Euler's number, base of natural logarithms)
- $i$ (imaginary unit)
- $\pi$ (pi, ratio of a circle's circumference to its diameter)
- $1$ (multiplicative identity)
- $0$ (additive identity)

## Applications
- **Representing Complex Numbers:** Any complex number $z = a+bi$ with polar form $z = r(\cos\theta + i\sin\theta)$ can be written compactly as:
  $$ z = r e^{i\theta} $$
  This exponential form simplifies multiplication and division of complex numbers:
    - $z_1 z_2 = (r_1 e^{i\theta_1})(r_2 e^{i\theta_2}) = r_1 r_2 e^{i(\theta_1 + \theta_2)}$ (multiply moduli, add arguments)
    - $\frac{z_1}{z_2} = \frac{r_1 e^{i\theta_1}}{r_2 e^{i\theta_2}} = \frac{r_1}{r_2} e^{i(\theta_1 - \theta_2)}$ (divide moduli, subtract arguments)
  It also simplifies finding powers (De Moivre's formula: $(re^{i\theta})^n = r^n e^{in\theta} = r^n(\cos n\theta + i\sin n\theta)$) and roots of complex numbers.
- **Fourier Analysis and Signal Processing:**
    - Sinusoidal signals (waves) can be represented using complex exponentials, simplifying analysis of their amplitude and phase. The Fourier transform heavily relies on $e^{i\omega t}$ or $e^{-j\omega t}$.
- **Electrical Engineering:**
    - Analyzing AC circuits using phasors, which are complex numbers representing sinusoidal voltages and currents. $e^{i\omega t}$ is fundamental.
- **Quantum Mechanics:**
    - Wave functions, which describe the state of quantum systems, are often complex-valued and involve terms like $e^{i(kx - \omega t)}$.
- **Differential Equations:**
    - Solutions to certain linear differential equations can be expressed using complex exponentials, which can then be converted back to real-valued solutions involving sines and cosines.
- **Deriving Trigonometric Identities:** Many trigonometric identities can be derived more easily using the exponential forms of sine and cosine.

Euler's formula provides a deep and powerful connection between exponential functions and trigonometry, unifying these concepts through the realm of complex numbers.

---
````

Filename: 150_Mathematics/Functions/Odds.md
````markdown
---
tags: [mathematics, probability, statistics, odds, concept]
aliases: [Odds Ratio] # Odds ratio is related but compares two odds
related:
  - "[[Probability]]"
  - "[[Logit_Function]]" # Logarithm of odds
  - "[[Logistic_Regression]]"
worksheet: [WS_Math_Foundations_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Odds

## Definition
In [[Probability|probability theory]] and statistics, the **odds** of an event occurring is a way of expressing the likelihood of that event. It is defined as the ratio of the probability of the event occurring to the probability of the event not occurring.

If $p$ is the probability of an event $E$ occurring, i.e., $P(E) = p$, then the probability of the event not occurring is $P(\text{not } E) = 1-p$.
The **odds in favor** of event $E$ are:
$$ \text{Odds}(E) = \text{Odds}(p) = \frac{P(E)}{P(\text{not } E)} = \frac{p}{1-p} $$

Odds can also be expressed "against" an event, which would be the reciprocal: $\frac{1-p}{p}$. However, "odds" usually refers to "odds in favor" unless specified.

## Interpretation
- If $p = 0.5$ (50% probability):
  $\text{Odds}(0.5) = \frac{0.5}{1-0.5} = \frac{0.5}{0.5} = 1$.
  This is often stated as "1 to 1" or "even odds".
- If $p = 0.8$ (80% probability):
  $\text{Odds}(0.8) = \frac{0.8}{1-0.8} = \frac{0.8}{0.2} = 4$.
  This is "4 to 1 in favor". For every 4 times the event occurs, it fails to occur 1 time (on average, out of 5 trials).
- If $p = 0.2$ (20% probability):
  $\text{Odds}(0.2) = \frac{0.2}{1-0.2} = \frac{0.2}{0.8} = 0.25 = \frac{1}{4}$.
  This is "0.25 to 1 in favor", or more commonly "1 to 4 in favor" (meaning for every 1 time it occurs, it fails 4 times), or "4 to 1 against".

## Range of Values
- If $p=0$, Odds = $\frac{0}{1} = 0$. (Event never occurs)
- If $0 < p < 0.5$, then $0 < \text{Odds} < 1$. (Event is less likely than not)
- If $p=0.5$, Odds = $1$. (Event is equally likely as not)
- If $0.5 < p < 1$, then $1 < \text{Odds} < \infty$. (Event is more likely than not)
- As $p \to 1$, Odds $\to \infty$. (Event is almost certain)
The odds are always non-negative.

## Relationship to Probability
Given the odds, one can convert back to probability:
If $\text{Odds} = O = \frac{p}{1-p}$:
$O(1-p) = p$
$O - Op = p$
$O = p + Op = p(1+O)$
$$ p = \frac{O}{1+O} $$

Example: If odds are 4 (i.e., 4 to 1 in favor):
$p = \frac{4}{1+4} = \frac{4}{5} = 0.8$.

## Log-Odds (Logit)
The natural logarithm of the odds is called the **[[Logit_Function|logit]]**:
$$ \text{logit}(p) = \ln(\text{Odds}(p)) = \ln\left(\frac{p}{1-p}\right) $$
The logit transforms probabilities from the range $(0,1)$ to the entire real number line $(-\infty, \infty)$, which is a key reason for its use in [[Logistic_Regression|logistic regression]].

## Odds Ratio
The **odds ratio (OR)** is a statistic that quantifies the strength of association between two events, A and B. It is the ratio of the odds of A occurring in the presence of B, to the odds of A occurring in the absence of B. Or, equivalently, the ratio of the odds of B in the presence of A to the odds of B in the absence of A.

If $p_1$ is the probability of an event in group 1 (e.g., exposed group) and $p_0$ is the probability of the event in group 0 (e.g., unexposed group):
Odds for group 1: $O_1 = \frac{p_1}{1-p_1}$
Odds for group 0: $O_0 = \frac{p_0}{1-p_0}$
Odds Ratio: $OR = \frac{O_1}{O_0} = \frac{p_1/(1-p_1)}{p_0/(1-p_0)}$

- $OR = 1$: Exposure does not affect odds of outcome.
- $OR > 1$: Exposure associated with higher odds of outcome.
- $OR < 1$: Exposure associated with lower odds of outcome.

In [[Logistic_Regression|logistic regression]], the exponentiated regression coefficients ($e^\beta$) correspond to odds ratios.

## Applications
- **Gambling and Betting:** Odds are the traditional way of expressing payouts and likelihoods in betting.
- **Epidemiology and Medical Statistics:**
    - Odds ratios are widely used in case-control studies to compare the odds of exposure to a risk factor among cases (those with a disease) versus controls (those without).
    - Interpreting results from [[Logistic_Regression|logistic regression]] models.
- **[[Logistic_Regression|Logistic Regression]]:** This statistical model directly models the log-odds of an event as a linear function of predictor variables.
- **Everyday Language:** People often use the term "odds" informally to discuss likelihoods.

## Example: Medical Study
Suppose a drug is tested.
- Probability of recovery with drug: $p_{\text{drug}} = 0.75$
- Probability of recovery with placebo: $p_{\text{placebo}} = 0.50$

Odds of recovery with drug:
$\text{Odds}_{\text{drug}} = \frac{0.75}{1-0.75} = \frac{0.75}{0.25} = 3$ (3 to 1 in favor)

Odds of recovery with placebo:
$\text{Odds}_{\text{placebo}} = \frac{0.50}{1-0.50} = \frac{0.50}{0.50} = 1$ (1 to 1, even odds)

Odds Ratio (OR) for recovery (drug vs. placebo):
$OR = \frac{\text{Odds}_{\text{drug}}}{\text{Odds}_{\text{placebo}}} = \frac{3}{1} = 3$.
This means the odds of recovery are 3 times higher for patients taking the drug compared to those taking the placebo.

---
````

Filename: 150_Mathematics/Probability/Probability_Distribution.md
````markdown
---
tags: [mathematics, probability, statistics, distribution, random_variable, concept]
aliases: [Probability Distributions, Probabilistic Distribution]
related:
  - "[[Probability]]"
  - "[[Random_Variable]]"
  - "[[Expected_Value]]"
  - "[[Variance_Standard_Deviation]]"
  - "[[Probability_Mass_Function_PMF]]"
  - "[[Probability_Density_Function_PDF]]"
  - "[[Cumulative_Distribution_Function_CDF]]"
  - "[[Normal_Distribution]]"
  - "[[Binomial_Distribution]]"
  - "[[Poisson_Distribution]]"
  - "[[Exponential_Distribution_Probability]]"
  - "[[Gamma_Function]]" # Appears in many distributions
  - "[[Softmax_Function]]" # Outputs a probability distribution
worksheet: [WS_Math_Foundations_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Probability Distribution

## Definition
A **probability distribution** is a mathematical function that describes the likelihood of different possible outcomes for a [[Random_Variable|random variable]]. It provides the probabilities of occurrence of different possible values that a random variable can take.

Probability distributions are fundamental to [[Probability|probability theory]] and statistics and are used to model random phenomena.

## Types of Random Variables and Distributions
The type of probability distribution depends on whether the random variable is discrete or continuous:

1.  **Discrete Random Variable:**
    - A random variable that can take on a finite number of values or a countably infinite number of values (e.g., the number of heads in 3 coin flips, the number of cars passing a point in an hour).
    - Its distribution is described by a **[[Probability_Mass_Function_PMF|Probability Mass Function (PMF)]]**, denoted $P(X=x)$ or $p(x)$.
    - **Properties of a PMF $p(x)$:**
        - $p(x) \ge 0$ for all possible values $x$.
        - $\sum_{\text{all } x} p(x) = 1$ (The sum of probabilities for all possible outcomes is 1).

2.  **Continuous Random Variable:**
    - A random variable that can take on any value within a given range or interval (e.g., height of a person, temperature of a room).
    - Its distribution is described by a **[[Probability_Density_Function_PDF|Probability Density Function (PDF)]]**, denoted $f(x)$ or $p(x)$.
    - **Properties of a PDF $f(x)$:**
        - $f(x) \ge 0$ for all $x$.
        - $\int_{-\infty}^{\infty} f(x) \,dx = 1$ (The total area under the curve of the PDF is 1).
        - The probability that $X$ falls within an interval $[a,b]$ is given by the integral: $P(a \le X \le b) = \int_{a}^{b} f(x) \,dx$.
    - >[!note] For a continuous random variable, the probability of $X$ taking on any single specific value is zero, i.e., $P(X=x) = 0$. Probabilities are only defined over intervals.

## Describing a Probability Distribution
Besides the PMF or PDF, distributions are also characterized by:

- **[[Cumulative_Distribution_Function_CDF|Cumulative Distribution Function (CDF)]]:**
    - Denoted $F(x)$ or $F_X(x)$, it gives the probability that the random variable $X$ takes on a value less than or equal to $x$:
      $$ F(x) = P(X \le x) $$
    - For discrete RVs: $F(x) = \sum_{k \le x} p(k)$.
    - For continuous RVs: $F(x) = \int_{-\infty}^{x} f(t) \,dt$.
    - **Properties of a CDF:**
        - $0 \le F(x) \le 1$.
        - $F(x)$ is non-decreasing.
        - $\lim_{x \to -\infty} F(x) = 0$.
        - $\lim_{x \to \infty} F(x) = 1$.

- **Parameters:** Many common distributions are part of a family characterized by one or more parameters that define their specific shape, location, and scale.
    - Example: A [[Normal_Distribution|Normal distribution]] is defined by its mean $\mu$ and standard deviation $\sigma$ (or variance $\sigma^2$).
    - Example: A [[Binomial_Distribution|Binomial distribution]] is defined by the number of trials $n$ and the probability of success $p$.

- **Moments:**
    - **[[Expected_Value|Expected Value (Mean, $\mu$, $E[X]$)]]:** The average value of the random variable.
      - Discrete: $E[X] = \sum x \cdot p(x)$.
      - Continuous: $E[X] = \int x \cdot f(x) \,dx$.
    - **[[Variance_Standard_Deviation|Variance ($\sigma^2$, $\text{Var}(X)$)]]:** Measures the spread or dispersion of the distribution around the mean. $\text{Var}(X) = E[(X - \mu)^2]$.
    - **[[Variance_Standard_Deviation|Standard Deviation ($\sigma$)]]:** The square root of the variance, also a measure of spread.
    - Higher moments like Skewness (asymmetry) and Kurtosis (tailedness/peakedness).

## Common Probability Distributions
[list2tab|#Common Distributions]
- **Discrete Distributions**
    - **Bernoulli Distribution:** Outcome of a single trial (success/failure). Param: $p$ (prob of success).
    - **[[Binomial_Distribution|Binomial Distribution]]:** Number of successes in $n$ independent Bernoulli trials. Params: $n, p$.
    - **[[Poisson_Distribution|Poisson Distribution]]:** Number of events occurring in a fixed interval of time or space, given an average rate. Param: $\lambda$ (average rate).
    - **Geometric Distribution:** Number of trials until the first success in a sequence of Bernoulli trials. Param: $p$.
    - **Hypergeometric Distribution:** Number of successes in $n$ draws (without replacement) from a finite population.
    - **Uniform Discrete Distribution:** All $k$ outcomes are equally likely.
- **Continuous Distributions**
    - **[[Normal_Distribution|Normal (Gaussian) Distribution]]:** The "bell curve," ubiquitous due to the Central Limit Theorem. Params: $\mu$ (mean), $\sigma^2$ (variance).
    - **Uniform Continuous Distribution:** All values in an interval $[a,b]$ are equally likely. Params: $a, b$.
    - **[[Exponential_Distribution_Probability|Exponential Distribution]]:** Time between events in a Poisson process. Param: $\lambda$ (rate) or $\beta=1/\lambda$ (scale).
    - **Gamma Distribution:** Generalization of exponential and Chi-squared distributions, often models waiting times. Params: $k$ (shape), $\theta$ (scale).
    - **Chi-squared ($\chi^2$) Distribution:** Sum of squared standard normal variables. Param: $k$ (degrees of freedom).
    - **Student's t-distribution:** Used for inference about means when sample size is small and population variance is unknown. Param: $\nu$ (degrees of freedom).
    - **F-distribution:** Ratio of two Chi-squared variables, used in ANOVA. Params: $d_1, d_2$ (degrees of freedom).
    - **Beta Distribution:** Models random variables that take values between 0 and 1, such as proportions or probabilities. Params: $\alpha, \beta$ (shape parameters).

## Applications
- **Statistical Inference:** Drawing conclusions about populations from samples (e.g., hypothesis testing, confidence intervals).
- **Machine Learning:**
    - Modeling data (e.g., assuming features or errors follow a certain distribution).
    - Generative models aim to learn the underlying probability distribution of the data.
    - Classification (e.g., Naive Bayes uses conditional probability distributions).
    - [[Softmax_Function|Softmax function]] output is a probability distribution over classes.
- **Risk Management and Finance:** Modeling asset returns, default probabilities.
- **Operations Research:** Modeling arrival rates, service times in queuing theory.
- **Physics and Engineering:** Describing random errors, particle behavior, signal noise.
- **Bioinformatics:** Modeling gene expression levels, sequence alignments.

Understanding probability distributions allows us_to quantify uncertainty, make predictions, and build models of real-world phenomena.

---
````

Filename: 150_Mathematics/Functions/Unit_Hyperbola.md
````markdown
---
tags: [mathematics, geometry, hyperbola, conic_section, concept]
aliases: [Rectangular Hyperbola, Equilateral Hyperbola]
related:
  - "[[Hyperbolic_Functions]]" # sinh, cosh parametrize it
  - "[[Conic_Sections]]"
worksheet: [WS_Math_Foundations_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Unit Hyperbola

## Definition
A **unit hyperbola** is a hyperbola described by the Cartesian equation:
$$ x^2 - y^2 = 1 $$
It is a specific type of [[Conic_Sections|conic section]]. The term "unit" refers to the fact that its semi-major axis (distance from the center to a vertex) is 1. It is also sometimes called a **rectangular hyperbola** or **equilateral hyperbola** because its asymptotes are perpendicular and its transverse and conjugate axes are of equal length (though for $x^2 - y^2 = 1$, the standard form implies $a=1, b=1$).

## Key Features
- **Center:** $(0,0)$
- **Vertices:** The points where the hyperbola intersects its transverse axis. For $x^2 - y^2 = 1$:
    - $(1,0)$
    - $(-1,0)$
- **Transverse Axis:** The line segment connecting the vertices (in this case, along the x-axis, length $2a=2$).
- **Conjugate Axis:** Perpendicular to the transverse axis, passing through the center (in this case, along the y-axis). Length $2b=2$.
- **Asymptotes:** Lines that the hyperbola approaches as it extends to infinity. For $x^2 - y^2 = 1$, the asymptotes are:
    - $y = x$
    - $y = -x$
    These can be found by setting the constant term to 0: $x^2 - y^2 = 0 \implies (x-y)(x+y)=0 \implies y=x$ or $y=-x$.
- **Foci:** Two fixed points such that for any point $P$ on the hyperbola, the absolute difference of the distances from $P$ to the two foci is constant ($2a$). For $x^2 - y^2 = 1$:
    - $c^2 = a^2 + b^2$. Here $a=1, b=1$, so $c^2 = 1^2 + 1^2 = 2 \implies c = \sqrt{2}$.
    - Foci are at $(\sqrt{2}, 0)$ and $(-\sqrt{2}, 0)$.

## Parametrization with Hyperbolic Functions
The right branch of the unit hyperbola ($x \ge 1$) can be parametrized using [[Hyperbolic_Functions|hyperbolic functions]]:
$$ x = \cosh t $$
$$ y = \sinh t $$
for $t \in (-\infty, \infty)$.
This is analogous to how the [[Unit_Circle|unit circle]] $x^2+y^2=1$ is parametrized by $x=\cos\theta, y=\sin\theta$.
We can verify this:
$x^2 - y^2 = \cosh^2 t - \sinh^2 t$.
Using the fundamental hyperbolic identity $\cosh^2 t - \sinh^2 t = 1$, we get $x^2 - y^2 = 1$.
The parameter $t$ is called the **hyperbolic angle**. It is equal to twice the area of the hyperbolic sector from the x-axis to the point $(\cosh t, \sinh t)$ and the origin, analogous to how a circular angle is twice the area of a circular sector in a unit circle.

The left branch ($x \le -1$) can be parametrized by $x = -\cosh t, y = \sinh t$.

## Visualization

```mermaid
graph TD
    subgraph HyperbolaGraph["Unit Hyperbola x² - y² = 1"]
        XAxis["x-axis"] --- YAxis["y-axis"]
        
        Origin((0,0))

        V1((1,0)) % Vertex 1
        V2((-1,0)) % Vertex 2

        F1(("(sqrt(2), 0) Focus 1"))
        F2(("(-sqrt(2), 0) Focus 2"))

        %% Right Branch
        RP1((cosh(t1), sinh(t1)))
        RP2((cosh(t2), sinh(t2)))
        V1 --- RP1
        V1 --- RP2
        
        %% Left Branch
        LP1((-cosh(t1), sinh(t1)))
        LP2((-cosh(t2), sinh(t2)))
        V2 --- LP1
        V2 --- LP2

        %% Asymptotes
        Asymptote1["y = x"] -.-> Origin
        Asymptote2["y = -x"] -.-> Origin
        
        Origin --- V1
        Origin --- V2
        Origin --- F1
        Origin --- F2
    end

    note right of RP1 : Right branch: x = cosh(t), y = sinh(t)
    note left of LP1 : Left branch: x = -cosh(t), y = sinh(t)

    style V1 fill:#afa,stroke:#000,stroke-width:2px
    style V2 fill:#afa,stroke:#000,stroke-width:2px
    style F1 fill:#faa,stroke:#000,stroke-width:1px
    style F2 fill:#faa,stroke:#000,stroke-width:1px
    style RP1 fill:#aaf,stroke:#000,stroke-width:1px
    style RP2 fill:#aaf,stroke:#000,stroke-width:1px
    style LP1 fill:#aaf,stroke:#000,stroke-width:1px
    style LP2 fill:#aaf,stroke:#000,stroke-width:1px
    linkStyle 6 stroke:blue,stroke-width:2px,interpolate:basis;
    linkStyle 7 stroke:blue,stroke-width:2px,interpolate:basis;
    linkStyle 8 stroke:blue,stroke-width:2px,interpolate:basis;
    linkStyle 9 stroke:blue,stroke-width:2px,interpolate:basis;
    linkStyle 10 stroke:red,stroke-width:1px,stroke-dasharray: 5 5;
    linkStyle 11 stroke:red,stroke-width:1px,stroke-dasharray: 5 5;
```

## Applications and Significance
- **Geometry:** A fundamental [[Conic_Sections|conic section]] with distinct properties.
- **Physics:**
    - **Special Relativity:** The geometry of Minkowski spacetime (which describes special relativity) is hyperbolic. Lorentz transformations, which relate coordinates between inertial frames, can be expressed using hyperbolic rotations (related to hyperbolic angles and functions). The equation $x^2 - (ct)^2 = s^2$ (where $s^2$ is the spacetime interval) is hyperbolic.
    - Orbits of celestial bodies under an inverse-square force law can be hyperbolic (if the body has enough energy to escape).
- **Navigation:** Hyperbolic navigation systems (like LORAN-C, though largely obsolete) used the time difference of signals from multiple transmitters to determine position along hyperbolas.
- **Mathematics:** The unit hyperbola is central to the definition and understanding of [[Hyperbolic_Functions|hyperbolic functions]], which have applications in calculus, differential equations, and engineering.

The unit hyperbola $x^2 - y^2 = 1$ is a canonical form. Another common form of a rectangular hyperbola is $xy=k$ (e.g., $xy=1$), which is the $x^2-y^2=1$ hyperbola rotated by $45^\circ$ and scaled.

---
````

Filename: 150_Mathematics/Geometry/Conic_Sections.md
````markdown
---
tags: [mathematics, geometry, conic_section, circle, ellipse, parabola, hyperbola, concept]
aliases: [Conics]
related:
  - "[[Circle]]"
  - "[[Ellipse]]"
  - "[[Parabola]]"
  - "[[Hyperbola]]"
  - "[[Unit_Circle]]"
  - "[[Unit_Hyperbola]]"
worksheet: [WS_Math_Foundations_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Conic Sections

## Definition
A **conic section** (or simply **conic**) is a curve obtained as the intersection of the surface of a cone with a plane. The type of conic section depends on the angle at which the plane intersects the cone relative to the cone's axis and generator lines.

There are three main types of non-degenerate conic sections:
1.  **[[Ellipse|Ellipse]]** (of which the [[Circle|circle]] is a special case)
2.  **[[Parabola|Parabola]]**
3.  **[[Hyperbola|Hyperbola]]**

Degenerate conic sections include a point, a line, or a pair of intersecting lines.

## Geometric Generation

[d2]
```d2
# Conic Sections Generation from a Double Cone

# Define styles
styles: {
  cone: {
    fill: "#E0E0E0"
    stroke: "#A0A0A0"
    stroke-width: 1
  }
  plane: {
    fill: "#ADD8E6" # Light blue
    opacity: 0.6
    stroke: "#00008B" # Dark blue
    stroke-width: 2
  }
  intersection_curve: {
    stroke: "#FF0000" # Red
    stroke-width: 3
    font-size: 14
    bold: true
  }
  label: {
    font-size: 16
    fill: "#333333"
  }
}

# Double Cone (simplified representation)
cone_top: {
  shape: triangle
  width: 150
  height: 200
  style: $styles.cone
}
cone_bottom: {
  shape: triangle
  width: 150
  height: 200
  rotate: 180 # Flip it
  style: $styles.cone
}
cone_top.y: 0
cone_bottom.y: 200 # Positioned below cone_top, vertices touching

# Plane for Ellipse (less steep than cone side)
plane_ellipse: {
  shape: rectangle
  width: 250
  height: 50
  x: -200
  y: 50
  rotate: -20
  style: $styles.plane
}
ellipse_label: "Ellipse" {style: $styles.label; x: -200; y: -20}
intersection_ellipse: " " { style: $styles.intersection_curve; shape: ellipse; width: 80; height: 40; x: -200; y: 50; opacity: 0.8}


# Plane for Parabola (parallel to cone side)
plane_parabola: {
  shape: rectangle
  width: 250
  height: 50
  x: 100
  y: 75
  rotate: -45 # Approximate angle for visual parallel
  style: $styles.plane
}
parabola_label: "Parabola" {style: $styles.label; x: 100; y: 0}
# Parabola intersection is harder to draw simply, this is a placeholder
intersection_parabola: " " { style: $styles.intersection_curve; shape: path; data: "M 80 50 Q 100 100 120 50"; x:100; y:75; opacity: 0.8}


# Plane for Hyperbola (steeper than cone side, or parallel to axis for two branches)
plane_hyperbola: {
  shape: rectangle
  width: 50
  height: 300
  x: 400
  y: 100 # Centered vertically on the double cone
  style: $styles.plane
  # No rotation for vertical cut
}
hyperbola_label: "Hyperbola" {style: $styles.label; x: 400; y: -20}
# Hyperbola intersection is two curves, placeholder
intersection_hyperbola_top: " " { style: $styles.intersection_curve; shape: path; data: "M 390 50 C 400 80 400 120 390 150"; opacity: 0.8}
intersection_hyperbola_bottom: " " { style: $styles.intersection_curve; shape: path; data: "M 390 250 C 400 220 400 180 390 150"; opacity: 0.8}


# Connections for clarity (optional)
# plane_ellipse -> intersection_ellipse: {style.stroke: none}
# plane_parabola -> intersection_parabola: {style.stroke: none}
# plane_hyperbola -> intersection_hyperbola_top: {style.stroke: none}
# plane_hyperbola -> intersection_hyperbola_bottom: {style.stroke: none}

# Grouping elements visually (layout hints)
direction: right
# (cone_top; cone_bottom)
# (plane_ellipse; ellipse_label; intersection_ellipse)
# (plane_parabola; parabola_label; intersection_parabola)
# (plane_hyperbola; hyperbola_label; intersection_hyperbola_top; intersection_hyperbola_bottom)
```
> The diagram above illustrates how different conic sections are formed by the intersection of a plane with a double cone.
> - **[[Ellipse|Ellipse]]/[[Circle|Circle]]:** Formed when the plane intersects one nappe of the cone at an angle to the axis less steep than the generator line. A circle is a special case where the plane is perpendicular to the cone's axis.
> - **[[Parabola|Parabola]]:** Formed when the plane is parallel to one of the generator lines of the cone.
> - **[[Hyperbola|Hyperbola]]:** Formed when the plane intersects both nappes of the cone (typically when the plane is steeper than the generator line or parallel to the cone's axis).

## General Quadratic Equation
All non-degenerate conic sections can be described by a second-degree polynomial equation in two variables $x$ and $y$:
$$ Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0 $$
where $A, B, C, D, E, F$ are constants, and not all of $A, B, C$ are zero.

The type of conic is determined by the **discriminant** $B^2 - 4AC$:
- If $B^2 - 4AC < 0$: The conic is an **[[Ellipse|ellipse]]** (or a [[Circle|circle]] if $A=C$ and $B=0$, or a point, or no curve).
- If $B^2 - 4AC = 0$: The conic is a **[[Parabola|parabola]]** (or a line, two parallel lines, or no curve).
- If $B^2 - 4AC > 0$: The conic is a **[[Hyperbola|hyperbola]]** (or two intersecting lines).

## Eccentricity ($e$)
Another way to define conic sections is using a property called **eccentricity ($e$)**. A conic section is the locus of points $P$ such that the ratio of the distance from $P$ to a fixed point (the **focus** $F$) to the distance from $P$ to a fixed line (the **directrix** $L$) is a constant $e$.
$$ \frac{d(P,F)}{d(P,L)} = e $$
- If $0 \le e < 1$: Ellipse (for $e=0$, it's a circle, assuming focus is at the center and directrix is at infinity).
- If $e = 1$: Parabola.
- If $e > 1$: Hyperbola.

## Standard Forms (Centered at Origin, Axes Aligned with Coordinate Axes)
[list2tab|#Standard Forms of Conics]
- **[[Circle|Circle]]**
    - Equation: $x^2 + y^2 = r^2$
    - Eccentricity: $e=0$
- **[[Ellipse|Ellipse]]**
    - Equation: $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ (where $a, b > 0$)
    - $a$: semi-major axis, $b$: semi-minor axis.
    - Eccentricity: $e = \sqrt{1 - \frac{b^2}{a^2}}$ (if $a>b$) or $e = \sqrt{1 - \frac{a^2}{b^2}}$ (if $b>a$). ($0 < e < 1$)
- **[[Parabola|Parabola]]**
    - Equation: $y^2 = 4px$ (opens right/left) or $x^2 = 4py$ (opens up/down)
    - $p$: distance from vertex to focus and from vertex to directrix.
    - Eccentricity: $e=1$
- **[[Hyperbola|Hyperbola]]**
    - Equation: $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$ (opens left/right, [[Unit_Hyperbola|unit hyperbola]] if $a=b=1$) or $\frac{y^2}{a^2} - \frac{x^2}{b^2} = 1$ (opens up/down)
    - $a$: semi-transverse axis, $b$: semi-conjugate axis.
    - Eccentricity: $e = \sqrt{1 + \frac{b^2}{a^2}}$. ($e > 1$)

## Applications
Conic sections appear in numerous scientific and engineering fields:
- **Astronomy and Physics:**
    - Orbits of planets, comets, and satellites under gravity are ellipses, parabolas, or hyperbolas (Kepler's laws of planetary motion).
    - Trajectories of projectiles (under constant gravity, neglecting air resistance) are parabolas.
    - Reflecting properties: Parabolic reflectors focus parallel rays to a single point (used in satellite dishes, telescopes). Elliptical reflectors focus rays from one focus to the other. Hyperbolic mirrors/lenses are also used in optical systems.
- **Engineering and Architecture:**
    - Design of arches, bridges (parabolic or catenary shapes, though catenary is not a conic).
    - Cooling towers often have a hyperbolic shape.
    - Gears can have elliptical shapes for specific motion requirements.
- **Optics:** Lenses and mirrors are often shaped as conic sections to manipulate light.
- **Aerodynamics:** Shapes of wings or nose cones can involve conic sections.
- **Mathematics:** They are fundamental objects in geometry, calculus, and linear algebra (quadratic forms).

---
````

Filename: 150_Mathematics/Geometry/Circle.md
````markdown
---
tags: [mathematics, geometry, conic_section, circle, concept]
aliases: [Circular Shape]
related:
  - "[[Conic_Sections]]"
  - "[[Unit_Circle]]"
  - "[[Ellipse]]" # Circle is a special ellipse
  - "[[Angles_Radians_Degrees]]"
  - "[[Pi_π]]"
worksheet: [WS_Math_Foundations_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Circle

## Definition
A **circle** is a two-dimensional geometric shape consisting of all points in a plane that are at a given constant distance (the **radius**) from a given fixed point (the **center**). It is a special type of [[Ellipse|ellipse]] where the two foci coincide with the center and the eccentricity is 0. It is one of the fundamental [[Conic_Sections|conic sections]].

## Equations of a Circle

1.  **Standard Equation (Center at Origin):**
    For a circle centered at the origin $(0,0)$ with radius $r$, the equation is:
    $$ x^2 + y^2 = r^2 $$
    This is derived from the Pythagorean theorem, where any point $(x,y)$ on the circle forms a right triangle with the origin and projections on the x and y axes, with hypotenuse $r$.
    The [[Unit_Circle|unit circle]] is a special case where $r=1$, so $x^2+y^2=1$.

2.  **General Equation (Center at $(h,k)$):**
    For a circle centered at a point $(h,k)$ with radius $r$, the equation is:
    $$ (x-h)^2 + (y-k)^2 = r^2 $$

3.  **Parametric Equations:**
    A circle centered at $(h,k)$ with radius $r$ can be described parametrically using [[Trigonometric_Functions|trigonometric functions]]:
    $$ x(t) = h + r \cos t $$
    $$ y(t) = k + r \sin t $$
    where $t$ is a parameter that varies from $0$ to $2\pi$ radians (or $0^\circ$ to $360^\circ$). As $t$ varies, the point $(x(t), y(t))$ traces out the circle.

## Key Properties and Terminology
[list2tab|#Circle Properties]
- **Center:** The fixed point from which all points on the circle are equidistant.
- **Radius ($r$):** The constant distance from the center to any point on the circle. Also, any line segment connecting the center to a point on the circle.
- **Diameter ($d$):** The distance across the circle passing through the center. It is twice the radius ($d = 2r$). Also, any chord that passes through the center.
- **Circumference ($C$):** The distance around the circle (its perimeter).
  $$ C = 2 \pi r = \pi d $$
  where $\pi$ ([[Pi_π|pi]]) is a mathematical constant approximately equal to $3.14159$.
- **Area ($A$):** The region enclosed by the circle.
  $$ A = \pi r^2 $$
- **Chord:** A line segment whose endpoints both lie on the circle.
- **Secant:** A line that intersects the circle at two distinct points.
- **Tangent:** A line that touches the circle at exactly one point (the point of tangency). A tangent line is always perpendicular to the radius drawn to the point of tangency.
- **Arc:** A portion of the circumference of a circle.
- **Sector:** A region bounded by two radii and the arc between them (like a slice of pie).
- **Segment:** A region bounded by a chord and the arc subtended by the chord.

## Visualization

```mermaid
graph TD
    subgraph CircleDiagram["Circle with Center (h,k) and Radius r"]
        Center((h,k))
        PointOnCircle(("P(x,y)"))
        
        Center -- "Radius r" --- PointOnCircle
        
        XAxis["x-axis"]
        YAxis["y-axis"]
        Center --- XProj((h,0))
        Center --- YProj((0,k))
        
        note right of PointOnCircle : (x-h)² + (y-k)² = r²
    end

    style Center fill:#afa,stroke:#000,stroke-width:2px
    style PointOnCircle fill:#aaf,stroke:#000,stroke-width:1px
    style XAxis stroke-dasharray: 3 3
    style YAxis stroke-dasharray: 3 3
    CirclePath{"Circle"}:::pathStyle
    classDef pathStyle fill:none,stroke:#369,stroke-width:3px

    %% This mermaid diagram doesn't easily draw a perfect circle shape
    %% The note represents the equation of the circle.
```
> The diagram illustrates a circle with center $(h,k)$ and radius $r$. Any point $P(x,y)$ on the circle satisfies the equation $(x-h)^2 + (y-k)^2 = r^2$.

## Applications
- **Geometry and Trigonometry:** The [[Unit_Circle|unit circle]] is fundamental for defining trigonometric functions.
- **Engineering and Design:** Wheels, gears, pipes, lenses, and many other mechanical and optical components are circular.
- **Physics:** Circular motion, orbits (as a first approximation or in specific cases), wave fronts spreading from a point source.
- **Computer Graphics:** Drawing circular shapes, collision detection involving circular objects.
- **Cartography and Navigation:** Representing circular search areas or ranges.
- **Art and Architecture:** Circles are common design elements.

The circle is one of the most basic and perfect geometric shapes, characterized by its complete symmetry.

---
````

Filename: 150_Mathematics/Geometry/Ellipse.md
````markdown
---
tags: [mathematics, geometry, conic_section, ellipse, concept]
aliases: [Elliptical Shape]
related:
  - "[[Conic_Sections]]"
  - "[[Circle]]" # Special case of an ellipse
  - "[[Foci_of_Ellipse_Hyperbola]]"
  - "[[Eccentricity_Conic]]"
worksheet: [WS_Math_Foundations_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Ellipse

## Definition
An **ellipse** is a two-dimensional geometric shape that is a generalization of a [[Circle|circle]]. It can be defined in several ways:
1.  **As a [[Conic_Sections|Conic Section]]:** An ellipse is the curve obtained by intersecting a cone with a plane that is not parallel or perpendicular to the cone's base and does not intersect the base (or intersects it in a way that still forms a closed curve).
2.  **Locus of Points Definition:** An ellipse is the set of all points $P$ in a plane such that the sum of the distances from $P$ to two fixed points, called the **[[Foci_of_Ellipse_Hyperbola|foci]]** (plural of focus), is constant. If the foci are $F_1$ and $F_2$, and $P$ is any point on the ellipse, then $d(P,F_1) + d(P,F_2) = \text{constant} = 2a$ (where $2a$ is the length of the major axis).
3.  **Eccentricity Definition:** An ellipse can be defined as the locus of points $P$ such that the ratio of the distance from $P$ to a focus $F$ to the distance from $P$ to a fixed line (the **directrix** $L$) is a constant $e$ (the [[Eccentricity_Conic|eccentricity]]), where $0 \le e < 1$. For an ellipse, $e < 1$. (If $e=0$, it's a circle).

## Standard Equation (Center at Origin, Axes Aligned)
If an ellipse is centered at the origin $(0,0)$ and its major and minor axes are aligned with the coordinate axes, its equation is:
$$ \frac{x^2}{a^2} + \frac{y^2}{b^2} = 1 $$
where:
- $a$ is the length of the **semi-major axis**.
- $b$ is the length of the **semi-minor axis**.
- By convention, if $a > b$, the major axis is horizontal along the x-axis. If $b > a$, the major axis is vertical along the y-axis. If $a=b$, the ellipse is a circle of radius $a$.

## Key Properties and Terminology
[list2tab|#Ellipse Properties]
- **Center:** The midpoint of the major and minor axes.
- **Major Axis:** The longest diameter of the ellipse, passing through both foci and the center. Length = $2a$.
- **Minor Axis:** The shortest diameter of the ellipse, passing through the center and perpendicular to the major axis. Length = $2b$.
- **Semi-major Axis ($a$):** Half the length of the major axis.
- **Semi-minor Axis ($b$):** Half the length of the minor axis.
- **[[Foci_of_Ellipse_Hyperbola|Foci ($F_1, F_2$)]]:** Two fixed points inside the ellipse used in its locus definition.
    - If the major axis is horizontal ($a>b$), the foci are at $(\pm c, 0)$, where $c^2 = a^2 - b^2$.
    - If the major axis is vertical ($b>a$), the foci are at $(0, \pm c)$, where $c^2 = b^2 - a^2$.
- **Vertices:** The endpoints of the major axis. If major axis is horizontal, vertices are $(\pm a, 0)$. If vertical, $(0, \pm b)$ (assuming $b>a$ then $a$ is semi-major in $y$ direction). Conventionally, $a$ is always semi-major.
- **[[Eccentricity_Conic|Eccentricity ($e$)]]:** A measure of how "elongated" the ellipse is. It is the ratio of the distance from the center to a focus ($c$) to the distance from the center to a vertex ($a$).
  $$ e = \frac{c}{a} = \frac{\sqrt{a^2 - b^2}}{a} \quad (\text{assuming } a \text{ is semi-major axis}) $$
  For an ellipse, $0 \le e < 1$.
    - If $e=0$, $c=0$, so $a^2=b^2 \implies a=b$. The ellipse is a circle.
    - As $e$ approaches 1, the ellipse becomes more elongated.
- **Area ($A$):** The region enclosed by the ellipse.
  $$ A = \pi a b $$
- **Circumference (Perimeter):** There is no simple exact formula for the circumference of an ellipse. It involves elliptic integrals. Approximations exist, e.g., Ramanujan's approximation.

## Parametric Equations
An ellipse centered at $(h,k)$ with semi-major axis $a$ and semi-minor axis $b$ (assuming major axis is horizontal for this parametrization):
$$ x(t) = h + a \cos t $$
$$ y(t) = k + b \sin t $$
where $t$ varies from $0$ to $2\pi$.

## Visualization (Major Axis Horizontal)

```mermaid
graph TD
    subgraph EllipseDiagram["Ellipse: x²/a² + y²/b² = 1 (a>b)"]
        Center((0,0))
        
        V1((a,0)) % Vertex 1
        V2((-a,0)) % Vertex 2
        CV1((0,b)) % Co-vertex 1
        CV2((0,-b)) % Co-vertex 2
        
        F1((c,0) Focus 1)
        F2((-c,0) Focus 2)
        
        P(("P(x,y) on ellipse"))

        Center -- "Semi-major axis a" --- V1
        Center -- "Semi-minor axis b" --- CV1
        Center --- F1
        
        EllipsePath{"Ellipse"} -- forms --- P
        P --- F1
        P --- F2
        
        note right of P : d(P,F1) + d(P,F2) = 2a
        note top of Center : c² = a² - b²
    end

    style Center fill:#ccc
    style V1 fill:#afa; style V2 fill:#afa
    style CV1 fill:#aaf; style CV2 fill:#aaf
    style F1 fill:#faa; style F2 fill:#faa
    style P fill:#ddd
    style EllipsePath fill:none,stroke:#369,stroke-width:3px
```

## Applications
- **Astronomy:**
    - **Kepler's First Law of Planetary Motion:** The orbit of every planet is an ellipse with the Sun at one of the two foci. This also applies to moons, comets, and artificial satellites.
- **Physics and Engineering:**
    - **Whispering Galleries:** Rooms with elliptically shaped ceilings or walls. Sound produced at one focus is reflected to the other focus, allowing whispers to be heard across the room.
    - **Lithotripsy:** A medical procedure that uses an elliptical reflector to focus shock waves to break up kidney stones (the stone is placed at one focus, the shock wave generator at the other).
    - Elliptical gears can be used to produce variable speed or torque.
- **Optics:** Elliptical mirrors and lenses are used to focus light or other electromagnetic radiation.
- **Architecture and Design:** Elliptical arches and domes.
- **Statistics and Data Analysis:**
    - Confidence ellipses are used to visualize the uncertainty in estimates of two parameters.
    - Ellipsoids (3D generalization) can represent data distributions or decision boundaries in machine learning.

The ellipse is a versatile and important shape found throughout nature and technology.

---
````

Filename: 150_Mathematics/Geometry/Parabola.md
````markdown
---
tags: [mathematics, geometry, conic_section, parabola, quadratic_function, concept]
aliases: [Parabolic Shape]
related:
  - "[[Conic_Sections]]"
  - "[[Quadratic_Function]]" # Graph of a quadratic function is a parabola
  - "[[Focus_Directrix_Parabola]]"
  - "[[Eccentricity_Conic]]"
worksheet: [WS_Math_Foundations_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Parabola

## Definition
A **parabola** is a U-shaped two-dimensional curve. It can be defined in several ways:
1.  **As a [[Conic_Sections|Conic Section]]:** A parabola is the curve obtained by intersecting a cone with a plane that is parallel to one of the generator lines of the cone.
2.  **Locus of Points Definition:** A parabola is the set of all points $P$ in a plane that are equidistant from a fixed point, called the **[[Focus_Directrix_Parabola|focus]]** ($F$), and a fixed line, called the **[[Focus_Directrix_Parabola|directrix]]** ($L$).
    $$ d(P,F) = d(P,L) $$
3.  **[[Eccentricity_Conic|Eccentricity]] Definition:** A parabola is a conic section with an eccentricity $e=1$.

## Standard Equations (Vertex at Origin)

1.  **Parabola Opening Right or Left (Axis of Symmetry is x-axis):**
    The standard equation is:
    $$ y^2 = 4px $$
    - **Vertex:** $(0,0)$
    - **Focus:** $(p,0)$
    - **Directrix:** $x = -p$
    - If $p > 0$, the parabola opens to the right.
    - If $p < 0$, the parabola opens to the left.
    - The quantity $|p|$ is the distance from the vertex to the focus, and also from the vertex to the directrix.
    - **Latus Rectum:** A chord through the focus perpendicular to the axis of symmetry. Its length is $|4p|$.

2.  **Parabola Opening Up or Down (Axis of Symmetry is y-axis):**
    The standard equation is:
    $$ x^2 = 4py $$
    - **Vertex:** $(0,0)$
    - **Focus:** $(0,p)$
    - **Directrix:** $y = -p$
    - If $p > 0$, the parabola opens upwards.
    - If $p < 0$, the parabola opens downwards.
    This form $y = \frac{1}{4p}x^2$ is directly related to the graph of a [[Quadratic_Function|quadratic function]] $y = ax^2$ (where $a = \frac{1}{4p}$).

## General Equation (Vertex at $(h,k)$)
- **Opening Right/Left (Axis $y=k$):** $(y-k)^2 = 4p(x-h)$
- **Opening Up/Down (Axis $x=h$):** $(x-h)^2 = 4p(y-k)$

## Key Properties and Terminology
[list2tab|#Parabola Properties]
- **Vertex:** The point on the parabola where the curve changes direction; it lies on the axis of symmetry, midway between the focus and the directrix.
- **[[Focus_Directrix_Parabola|Focus ($F$)]]:** The fixed point used in the locus definition.
- **[[Focus_Directrix_Parabola|Directrix ($L$)]]:** The fixed line used in the locus definition.
- **Axis of Symmetry:** A line passing through the vertex and the focus, about which the parabola is symmetric.
- **Latus Rectum:** The chord through the focus parallel to the directrix (or perpendicular to the axis of symmetry). Its length is $4|p|$. The endpoints of the latus rectum are $(p, \pm 2p)$ for $y^2=4px$.
- **Reflective Property:** Rays parallel to the axis of symmetry are reflected by the parabola to pass through the focus. Conversely, rays emanating from the focus are reflected by the parabola into a beam parallel to the axis of symmetry.

## Visualization (Opening Right, $y^2 = 4px$ with $p>0$)

```mermaid
graph TD
    subgraph ParabolaDiagram["Parabola y² = 4px (p>0)"]
        Vertex((0,0))
        Focus((p,0) Focus F)
        DirectrixLine["x = -p (Directrix L)"]
        
        P(("P(x,y) on parabola"))

        Vertex --- Focus
        
        %% Parabola curve - upper half
        PathUpper{Curve} -- forms --- P
        %% Parabola curve - lower half
        PathLower{Curve} -- forms --- P
        
        P -- "d(P,F)" --- Focus
        P -- "d(P,L)" --- ProjDirectrix(((-p,y) on Directrix))
        DirectrixLine --- ProjDirectrix
        
        note right of P : d(P,F) = d(P,L)
        note top of Vertex : Vertex
    end

    style Vertex fill:#afa,stroke:#000,stroke-width:2px
    style Focus fill:#faa,stroke:#000,stroke-width:1px
    style DirectrixLine stroke:#00f,stroke-width:1px,stroke-dasharray:5 5
    style P fill:#ddd,stroke:#000,stroke-width:1px
    style ProjDirectrix fill:#ddd,stroke:#000,stroke-width:1px
    style PathUpper fill:none,stroke:#369,stroke-width:3px
    style PathLower fill:none,stroke:#369,stroke-width:3px
```
> The diagram illustrates a parabola opening to the right. For any point $P(x,y)$ on the parabola, its distance to the focus $F$ is equal to its perpendicular distance to the directrix $L$.

## Applications
- **Physics and Engineering:**
    - **Projectile Motion:** The path of a projectile launched in a uniform gravitational field (neglecting air resistance) is a parabola.
    - **Reflectors (Antennas, Headlights, Solar Concentrators):** The reflective property of parabolas is used in satellite dishes (parabolic antennas) to collect signals at the focus, in car headlights and searchlights to project a beam from a light source at the focus, and in solar concentrators to focus sunlight.
    - **Suspension Bridges:** The main cables of a suspension bridge, if uniformly loaded horizontally, take the shape of a parabola (though a freely hanging cable forms a catenary, which is similar for shallow curves).
- **Optics:** Parabolic mirrors are used in telescopes (reflecting telescopes) to focus light from distant objects.
- **Mathematics:** The graph of any [[Quadratic_Function|quadratic function]] $y = ax^2 + bx + c$ is a parabola.
- **Architecture:** Parabolic arches are sometimes used for their structural properties or aesthetic appeal.

The parabola's unique geometric and reflective properties make it important in many practical applications.

---
````

Filename: 150_Mathematics/Geometry/Hyperbola.md
````markdown
---
tags: [mathematics, geometry, conic_section, hyperbola, concept]
aliases: [Hyperbolic Shape]
related:
  - "[[Conic_Sections]]"
  - "[[Unit_Hyperbola]]" # Special case
  - "[[Foci_of_Ellipse_Hyperbola]]"
  - "[[Eccentricity_Conic]]"
  - "[[Asymptotes_Hyperbola]]"
worksheet: [WS_Math_Foundations_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Hyperbola

## Definition
A **hyperbola** is a type of smooth curve lying in a plane, defined by its geometric properties or by equations for it. It is one of the three main types of [[Conic_Sections|conic sections]].
1.  **As a Conic Section:** A hyperbola is formed by intersecting a double cone with a plane that is steeper than the generator line of the cone (or parallel to the cone's axis), so it intersects both nappes (halves) of the cone, resulting in two separate, unbounded curves called branches.
2.  **Locus of Points Definition:** A hyperbola is the set of all points $P$ in a plane such that the absolute difference of the distances from $P$ to two fixed points, called the **[[Foci_of_Ellipse_Hyperbola|foci]]** ($F_1$ and $F_2$), is constant. If $P$ is any point on the hyperbola, then $|d(P,F_1) - d(P,F_2)| = \text{constant} = 2a$ (where $2a$ is the length of the transverse axis).
3.  **[[Eccentricity_Conic|Eccentricity]] Definition:** A hyperbola can be defined as the locus of points $P$ such that the ratio of the distance from $P$ to a focus $F$ to the distance from $P$ to a fixed line (the **directrix** $L$) is a constant $e$ (the eccentricity), where $e > 1$.

## Standard Equations (Center at Origin, Axes Aligned)

1.  **Hyperbola Opening Left and Right (Transverse Axis is x-axis):**
    The standard equation is:
    $$ \frac{x^2}{a^2} - \frac{y^2}{b^2} = 1 $$
    - **Center:** $(0,0)$
    - **Vertices:** $(\pm a, 0)$
    - **Foci:** $(\pm c, 0)$, where $c^2 = a^2 + b^2$.
    - **[[Asymptotes_Hyperbola|Asymptotes]]:** $y = \pm \frac{b}{a} x$

2.  **Hyperbola Opening Up and Down (Transverse Axis is y-axis):**
    The standard equation is:
    $$ \frac{y^2}{a^2} - \frac{x^2}{b^2} = 1 $$
    - **Center:** $(0,0)$
    - **Vertices:** $(0, \pm a)$
    - **Foci:** $(0, \pm c)$, where $c^2 = a^2 + b^2$.
    - **[[Asymptotes_Hyperbola|Asymptotes]]:** $y = \pm \frac{a}{b} x$

The [[Unit_Hyperbola|unit hyperbola]] $x^2 - y^2 = 1$ is a special case of the first form where $a=1$ and $b=1$.

## Key Properties and Terminology
[list2tab|#Hyperbola Properties]
- **Center:** The midpoint of the line segment connecting the foci. Also the intersection of the asymptotes.
- **Transverse Axis:** The line segment connecting the two vertices. Its length is $2a$.
- **Conjugate Axis:** The line segment perpendicular to the transverse axis, passing through the center. Its length is $2b$. (Note: The hyperbola does not intersect its conjugate axis).
- **Semi-transverse Axis ($a$):** Half the length of the transverse axis.
- **Semi-conjugate Axis ($b$):** Half the length of the conjugate axis.
- **[[Foci_of_Ellipse_Hyperbola|Foci ($F_1, F_2$)]]:** Two fixed points used in the locus definition.
- **Vertices:** The points where the hyperbola intersects its transverse axis.
- **[[Eccentricity_Conic|Eccentricity ($e$)]]:** A measure of how "open" or "spread out" the hyperbola's branches are.
  $$ e = \frac{c}{a} = \frac{\sqrt{a^2 + b^2}}{a} $$
  For a hyperbola, $e > 1$. As $e$ gets closer to 1, the branches become "sharper". As $e$ increases, the branches become "flatter".
- **[[Asymptotes_Hyperbola|Asymptotes]]:** Two straight lines that the branches of the hyperbola approach as they extend to infinity. They intersect at the center of the hyperbola. The rectangle formed by lines $x=\pm a, y=\pm b$ (for the first standard form) can help sketch the asymptotes (they pass through the corners of this rectangle and the center).
- **Latus Rectum:** A chord through a focus perpendicular to the transverse axis. Its length is $\frac{2b^2}{a}$.

## Visualization (Opening Left/Right, $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$)

```mermaid
graph TD
    subgraph HyperbolaDiagram["Hyperbola: x²/a² - y²/b² = 1"]
        Center((0,0))
        
        V1((a,0) Vertex)
        V2((-a,0) Vertex)
        
        F1((c,0) Focus 1)
        F2((-c,0) Focus 2)
        
        P(("P(x,y) on right branch"))
        P2L(("P'(x',y') on left branch"))

        Asymptote1["y = (b/a)x"] -.-> Center
        Asymptote2["y = -(b/a)x"] -.-> Center
        
        %% Branches - simplified representation
        BranchR{Curve} -- forms --- P
        BranchL{Curve} -- forms --- P2L
        V1 --- BranchR
        V2 --- BranchL
        
        P --- F1
        P --- F2
        
        note right of P : |d(P,F1) - d(P,F2)| = 2a
        note top of Center : c² = a² + b²
    end

    style Center fill:#ccc
    style V1 fill:#afa; style V2 fill:#afa
    style F1 fill:#faa; style F2 fill:#faa
    style P fill:#ddd; style P2L fill:#ddd
    style Asymptote1 stroke:red,stroke-width:1px,stroke-dasharray:5 5
    style Asymptote2 stroke:red,stroke-width:1px,stroke-dasharray:5 5
    style BranchR fill:none,stroke:#369,stroke-width:3px
    style BranchL fill:none,stroke:#369,stroke-width:3px
```

## Applications
- **Astronomy and Physics:**
    - **Orbits:** Some comets that pass through the solar system once and then escape have hyperbolic orbits (if their energy is positive relative to the Sun's gravity).
    - **Scattering Trajectories:** The path of a particle scattered by a repulsive force (e.g., Rutherford scattering of alpha particles by a nucleus) can be hyperbolic.
- **Navigation Systems:**
    - **LORAN (Long Range Navigation) and GPS:** Hyperbolic navigation systems determine position by measuring the difference in arrival times of signals from synchronized transmitters. Lines of constant time difference form hyperbolas, and the intersection of two such hyperbolas gives the receiver's location.
- **Optics and Acoustics:**
    - Hyperbolic mirrors and lenses are used in some telescope designs (e.g., Cassegrain reflector uses a parabolic primary mirror and a hyperbolic secondary mirror).
    - The shape of some shock waves (e.g., sonic boom from a supersonic aircraft) can be approximated by a hyperbola.
- **Engineering and Architecture:**
    - **Cooling Towers:** Many large cooling towers have a hyperbolic shape (hyperboloid of one sheet). This structure is strong and uses material efficiently.
    - Some gear designs.
- **Mathematics:**
    - The [[Unit_Hyperbola|unit hyperbola]] is fundamental to defining [[Hyperbolic_Functions|hyperbolic functions]].

The hyperbola, with its two distinct branches and asymptotes, has unique properties that make it important in various scientific and practical contexts.

---
````

Filename: 150_Mathematics/Geometry/Foci_of_Ellipse_Hyperbola.md
````markdown
---
tags: [mathematics, geometry, conic_section, ellipse, hyperbola, focus, foci, concept]
aliases: [Focal Points, Ellipse Foci, Hyperbola Foci]
related:
  - "[[Ellipse]]"
  - "[[Hyperbola]]"
  - "[[Conic_Sections]]"
  - "[[Eccentricity_Conic]]"
worksheet: [WS_Math_Foundations_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Foci of an Ellipse and Hyperbola

The **foci** (plural of **focus**) are special fixed points associated with [[Conic_Sections|conic sections]] like the [[Ellipse|ellipse]] and [[Hyperbola|hyperbola]]. They play a crucial role in the geometric definition and reflective properties of these curves. The [[Parabola|parabola]] has only one focus.

## Foci of an Ellipse

**Definition:** An ellipse is the set of all points $P$ in a plane such that the sum of the distances from $P$ to two fixed points (the foci, $F_1$ and $F_2$) is constant. This constant sum is equal to the length of the major axis, $2a$.
$$ d(P,F_1) + d(P,F_2) = 2a $$

**Location:**
Consider an ellipse centered at the origin $(0,0)$ with its standard equation:
- If the major axis is horizontal (along the x-axis, $a > b$): $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$
    - The foci are located at $(\pm c, 0)$, where $c = \sqrt{a^2 - b^2}$.
- If the major axis is vertical (along the y-axis, $b > a$): $\frac{x^2}{b^2} + \frac{y^2}{a^2} = 1$ (assuming $a$ is always semi-major)
    - The foci are located at $(0, \pm c)$, where $c = \sqrt{a^2 - b^2}$.
    (Note: It's common to always let $a$ be the semi-major axis length. If $a$ is associated with $y^2$, then major axis is vertical).

The distance from the center to each focus is $c$.
The [[Eccentricity_Conic|eccentricity]] $e = \frac{c}{a}$. For an ellipse, $0 \le e < 1$.
- If $e=0$, then $c=0$, so $a=b$. The foci coincide at the center, and the ellipse is a [[Circle|circle]].

**Reflective Property:** A ray of light or sound originating at one focus of an ellipse will be reflected off the ellipse to pass through the other focus. This is the principle behind "whispering galleries."

## Foci of a Hyperbola

**Definition:** A hyperbola is the set of all points $P$ in a plane such that the absolute difference of the distances from $P$ to two fixed points (the foci, $F_1$ and $F_2$) is constant. This constant absolute difference is equal to the length of the transverse axis, $2a$.
$$ |d(P,F_1) - d(P,F_2)| = 2a $$

**Location:**
Consider a hyperbola centered at the origin $(0,0)$ with its standard equation:
- If the transverse axis is horizontal (hyperbola opens left/right): $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$
    - The foci are located at $(\pm c, 0)$, where $c = \sqrt{a^2 + b^2}$.
- If the transverse axis is vertical (hyperbola opens up/down): $\frac{y^2}{a^2} - \frac{x^2}{b^2} = 1$
    - The foci are located at $(0, \pm c)$, where $c = \sqrt{a^2 + b^2}$.

The distance from the center to each focus is $c$.
The [[Eccentricity_Conic|eccentricity]] $e = \frac{c}{a}$. For a hyperbola, $e > 1$.

**Reflective Property:** A ray of light or sound originating at one focus of a hyperbola will be reflected off the hyperbola as if it came from the other focus. This property is used in some telescope designs (e.g., Cassegrain).

## Comparison

[list2mdtable|#Foci Comparison: Ellipse vs. Hyperbola (Centered at Origin)]
- Property
    - Ellipse ($\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$, assume $a>b$)
        - Hyperbola ($\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$)
- Definition based on foci
    - $d(P,F_1) + d(P,F_2) = 2a$
        - $|d(P,F_1) - d(P,F_2)| = 2a$
- Relationship for $c$
    - $c^2 = a^2 - b^2$
        - $c^2 = a^2 + b^2$
- Location of foci (if horizontal major/transverse axis)
    - $(\pm c, 0)$ (inside the ellipse)
        - $(\pm c, 0)$ (outside the "central box", on the transverse axis)
- Eccentricity $e = c/a$
    - $0 \le e < 1$
        - $e > 1$

## Visualization of Foci

**Ellipse:**
```mermaid
graph TD
    subgraph EllipseFoci
        Center((0,0))
        F1((c,0) Focus1)
        F2((-c,0) Focus2)
        V1((a,0) Vertex)
        V2((-a,0) Vertex)
        P(("P(x,y) on ellipse"))
        EllipsePath{" "} -- forms --- P
        P --- F1
        P --- F2
        note right of P : d(P,F1) + d(P,F2) = 2a
    end
    style EllipsePath fill:none,stroke:#369,stroke-width:2px
```

**Hyperbola:**
```mermaid
graph TD
    subgraph HyperbolaFoci
        Center((0,0))
        F1((c,0) Focus1)
        F2((-c,0) Focus2)
        V1((a,0) Vertex)
        V2((-a,0) Vertex)
        P(("P(x,y) on right branch"))
        HyperbolaPath{" "} -- forms --- P
        P --- F1
        P --- F2
        note right of P : |d(P,F1) - d(P,F2)| = 2a
    end
    style HyperbolaPath fill:none,stroke:#369,stroke-width:2px
```

The concept of foci is central to understanding the geometric nature and many practical applications of ellipses and hyperbolas.

---
````

Filename: 150_Mathematics/Geometry/Eccentricity_Conic.md
````markdown
---
tags: [mathematics, geometry, conic_section, eccentricity, ellipse, parabola, hyperbola, concept]
aliases: [Conic Eccentricity, e]
related:
  - "[[Conic_Sections]]"
  - "[[Ellipse]]"
  - "[[Parabola]]"
  - "[[Hyperbola]]"
  - "[[Circle]]"
  - "[[Focus_Directrix_Parabola]]"
  - "[[Foci_of_Ellipse_Hyperbola]]"
worksheet: [WS_Math_Foundations_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Eccentricity of Conic Sections

## Definition
The **eccentricity** of a [[Conic_Sections|conic section]], denoted by $e$, is a non-negative real number that uniquely characterizes its shape. It measures how much the conic section deviates from being circular.

The eccentricity can be defined in two main ways:

1.  **Focus-Directrix Definition:**
    For any conic section other than a circle, the eccentricity $e$ is the ratio of the distance from any point $P$ on the conic to one of its **foci** ($F$) to the perpendicular distance from $P$ to a corresponding line called the **directrix** ($L$).
    $$ e = \frac{d(P,F)}{d(P,L)} $$
    - The focus is a fixed point.
    - The directrix is a fixed line not containing the focus.

2.  **For Ellipses and Hyperbolas (using $a$ and $c$):**
    - For an [[Ellipse|ellipse]] and a [[Hyperbola|hyperbola]], the eccentricity $e$ can also be defined as the ratio of the distance from the center to a focus ($c$) to the distance from the center to a vertex ($a$ along the major/transverse axis).
      $$ e = \frac{c}{a} $$
      - For an ellipse: $c = \sqrt{a^2 - b^2}$, so $e = \frac{\sqrt{a^2 - b^2}}{a}$.
      - For a hyperbola: $c = \sqrt{a^2 + b^2}$, so $e = \frac{\sqrt{a^2 + b^2}}{a}$.
      (Here, $a$ is the semi-major/semi-transverse axis and $b$ is the semi-minor/semi-conjugate axis.)

## Values of Eccentricity and Corresponding Conic Sections

The value of $e$ determines the type of conic section:

[list2mdtable|#Eccentricity Values and Conic Types]
- Eccentricity ($e$)
    - Type of Conic Section
        - Description
- $e = 0$
    - [[Circle|Circle]]
        - A special case of an ellipse. Foci coincide at the center. Directrix is at infinity.
- $0 < e < 1$
    - [[Ellipse|Ellipse]]
        - A closed, bounded curve. The smaller $e$ is (closer to 0), the more circular the ellipse. As $e$ approaches 1, the ellipse becomes more elongated.
- $e = 1$
    - [[Parabola|Parabola]]
        - An unbounded curve. All parabolas are similar in shape, differing only in size.
- $e > 1$
    - [[Hyperbola|Hyperbola]]
        - An unbounded curve with two distinct branches. As $e$ increases, the branches become "flatter" or more open.

## Interpretation
- **$e \approx 0$:** The conic is very "circular."
- **$e \approx 1$ (but $e<1$):** The ellipse is very "elongated" or "flat."
- **$e \approx 1$ (but $e>1$):** The hyperbola's branches are relatively "sharp" or "narrow."
- **Large $e$:** The hyperbola's branches are very "open" or "flat."

## Calculating Eccentricity from Standard Equations

1.  **[[Ellipse|Ellipse]]:** $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ (assume $a \ge b$, so $a$ is semi-major axis)
    $c^2 = a^2 - b^2$
    $$ e = \frac{c}{a} = \frac{\sqrt{a^2 - b^2}}{a} = \sqrt{1 - \left(\frac{b}{a}\right)^2} $$

2.  **[[Parabola|Parabola]]:**
    By definition, $e=1$.

3.  **[[Hyperbola|Hyperbola]]:** $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$ ($a$ is semi-transverse axis)
    $c^2 = a^2 + b^2$
    $$ e = \frac{c}{a} = \frac{\sqrt{a^2 + b^2}}{a} = \sqrt{1 + \left(\frac{b}{a}\right)^2} $$

## Applications
- **Astronomy:** The eccentricity of the orbit of a planet or comet determines the shape of its path around the Sun.
    - $e \approx 0$ for nearly circular orbits (e.g., Venus, Earth).
    - $0 < e < 1$ for elliptical orbits (most planets, Halley's Comet).
    - $e = 1$ for parabolic escape trajectories (some comets that make a single pass).
    - $e > 1$ for hyperbolic escape trajectories (interstellar objects or comets with enough energy to escape the solar system).
- **Optics:** The design of lenses and mirrors can be related to the eccentricity of the conic shapes used.
- **Engineering:** Understanding the shape and properties of conic sections is important in structural design and mechanical systems.

Eccentricity provides a single numerical parameter that elegantly classifies and describes the "non-circularity" of all conic sections.

---
````

Filename: 150_Mathematics/Geometry/Asymptotes_Hyperbola.md
````markdown
[[Asymptotes_Hyperbola]]
````

Filename: 150_Mathematics/Calculus/Focus_Directrix_Parabola.md
````markdown
[[Focus_Directrix_Parabola]]
````

Filename: 150_Mathematics/Functions/Linear_Function.md
````markdown
[[Linear_Function]]
`````
