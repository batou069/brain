---
tags:
  - mathematics
  - linear_algebra
  - vector
  - dot_product
  - inner_product
  - scalar_product
  - concept
aliases:
  - Inner Product
  - Scalar Product
  - Vector Dot Product
related:
  - "[[Vector]]"
  - "[[Row_Vector]]"
  - "[[Column_Vector]]"
  - "[[Matrix_Product]]"
  - "[[p-norm]]"
  - "[[Cosine_Similarity]]"
  - "[[Orthogonal_Vectors]]"
worksheet:
  - WS_Math_Foundations_1
date_created: 2025-05-30
---
# Dot Product (Inner Product)

## Definition
The **dot product**, also known as the **scalar product** or **inner product** (in Euclidean spaces), is an algebraic operation that takes two equal-length sequences of numbers (usually coordinate [[Vector|vectors]]) and returns a single [[Scalar|number]].

For two vectors $\mathbf{a} = (a_1, a_2, \dots, a_n)$ and $\mathbf{b} = (b_1, b_2, \dots, b_n)$, their dot product is defined as:
$$ \mathbf{a} \cdot \mathbf{b} = \sum_{i=1}^{n} a_i b_i = a_1 b_1 + a_2 b_2 + \dots + a_n b_n $$

If vectors are represented as a [[Row_Vector|row vector]] $\mathbf{a}$ and a [[Column_Vector|column vector]] $\mathbf{b}_{\text{col}}$ (or vice-versa, with one transposed), the dot product can also be expressed as a [[Matrix_Product|matrix product]]:
$$ \mathbf{a} \cdot \mathbf{b} = \mathbf{a} \mathbf{b}_{\text{col}} = \begin{bmatrix} a_1 & a_2 & \dots & a_n \end{bmatrix} \begin{pmatrix} b_1 \\ b_2 \\ \vdots \\ b_n \end{pmatrix} $$
Alternatively, if both are column vectors $\mathbf{a}_{\text{col}}$ and $\mathbf{b}_{\text{col}}$:
$$ \mathbf{a} \cdot \mathbf{b} = \mathbf{a}_{\text{col}}^T \mathbf{b}_{\text{col}} $$

## Geometric Interpretation

>[!question] What is the geometric interpretation of a dot product?
>Geometrically, the dot product of two Euclidean vectors $\mathbf{a}$ and $\mathbf{b}$ is related to the angle $\theta$ between them and their magnitudes (lengths):
>$$ \mathbf{a} \cdot \mathbf{b} = \|\mathbf{a}\| \|\mathbf{b}\| \cos \theta $$
>where:
>- $\|\mathbf{a}\|$ is the magnitude (L2 norm) of vector $\mathbf{a}$.
>- $\|\mathbf{b}\|$ is the magnitude (L2 norm) of vector $\mathbf{b}$.
>- $\theta$ is the angle between vectors $\mathbf{a}$ and $\mathbf{b}$.

This formula provides several key insights:
1.  **Projection:** The term $\|\mathbf{b}\| \cos \theta$ is the scalar projection of vector $\mathbf{b}$ onto vector $\mathbf{a}$. So, the dot product $\mathbf{a} \cdot \mathbf{b}$ is the magnitude of $\mathbf{a}$ multiplied by the scalar projection of $\mathbf{b}$ onto $\mathbf{a}$ (or vice-versa).
   It tells us "how much" of one vector points in the direction of the other.
   
   ```mermaid
   graph TD
    subgraph AngleTheta["Angle theta between vectors a and b"]
        O[Origin 0 0] ---|Vector a| A[Point A]
        O ---|Vector b| B[Point B]
        B ---|Projection of b on a| POnA[Projection Point P]
        A --- POnA
        A -->|Label a| O
        O -->|Label b| B
        NoteTheta[theta is angle AOB] --> B
        NoteProjection[OP = norm b * cos theta] --> POnA
        DotProduct[a . b = norm a * norm b * cos theta] --> O
    end

    style O fill:#ddd,stroke:#333,stroke-width:2px
    style A fill:#afa,stroke:#333,stroke-width:2px
    style B fill:#aaf,stroke:#333,stroke-width:2px
    style POnA fill:#faa,stroke:#333,stroke-width:1px,stroke-dasharray:3,3
    style NoteTheta fill:#fff,stroke:#333,stroke-width:1px
    style NoteProjection fill:#fff,stroke:#333,stroke-width:1px
    style DotProduct fill:#fff,stroke:#333,stroke-width:1px
    linkStyle 0 stroke:#333,stroke-width:2px
    linkStyle 1 stroke:#333,stroke-width:2px
    linkStyle 2 stroke:#333,stroke-width:1px,stroke-dasharray:3,3
    linkStyle 3 stroke:#333,stroke-width:1px
    linkStyle 4 stroke:#333,stroke-width:1px
    linkStyle 5 stroke:#333,stroke-width:1px
    linkStyle 6 stroke:#333,stroke-width:1px
    linkStyle 7 stroke:#333,stroke-width:1px
   ```
2.  **Angle Between Vectors:** The formula can be rearranged to find the angle between two non-zero vectors:
   $$ \cos \theta = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\| \|\mathbf{b}\|} $$
   This is the basis for [[Cosine_Similarity|cosine similarity]].
3.  **Orthogonality:**
   - If $\mathbf{a} \cdot \mathbf{b} = 0$, and neither $\mathbf{a}$ nor $\mathbf{b}$ is the zero vector, then $\cos \theta = 0$, which means $\theta = 90^\circ$ (or $\pi/2$ radians). The vectors are **[[Orthogonal_Vectors|orthogonal]]** (perpendicular).
   - If $\mathbf{a} \cdot \mathbf{b} > 0$, then $\cos \theta > 0$, so $0 \le \theta < 90^\circ$. The angle is acute (vectors point in a generally similar direction).
   - If $\mathbf{a} \cdot \mathbf{b} < 0$, then $\cos \theta < 0$, so $90^\circ < \theta \le 180^\circ$. The angle is obtuse (vectors point in generally opposite directions).
4.  **Alignment:**
   - If $\mathbf{a}$ and $\mathbf{b}$ point in the exact same direction ($\theta = 0^\circ$, $\cos \theta = 1$), then $\mathbf{a} \cdot \mathbf{b} = \|\mathbf{a}\| \|\mathbf{b}\|$.
   - If $\mathbf{a}$ and $\mathbf{b}$ point in exact opposite directions ($\theta = 180^\circ$, $\cos \theta = -1$), then $\mathbf{a} \cdot \mathbf{b} = -\|\mathbf{a}\| \|\mathbf{b}\|$.
5.  **Magnitude Squared:** The dot product of a vector with itself gives the square of its magnitude:
   $$ \mathbf{a} \cdot \mathbf{a} = \|\mathbf{a}\| \|\mathbf{a}\| \cos 0^\circ = \|\mathbf{a}\|^2 $$
   Algebraically: $\mathbf{a} \cdot \mathbf{a} = a_1^2 + a_2^2 + \dots + a_n^2 = (\|\mathbf{a}\|_2)^2$.

## Properties
- **Commutative:** $\mathbf{a} \cdot \mathbf{b} = \mathbf{b} \cdot \mathbf{a}$
- **Distributive over vector addition:** $\mathbf{a} \cdot (\mathbf{b} + \mathbf{c}) = \mathbf{a} \cdot \mathbf{b} + \mathbf{a} \cdot \mathbf{c}$
- **Bilinear:** It is linear in each of its arguments.
- **Scalar multiplication:** $(k\mathbf{a}) \cdot \mathbf{b} = \mathbf{a} \cdot (k\mathbf{b}) = k(\mathbf{a} \cdot \mathbf{b})$, where $k$ is a scalar.
- **Non-negative:** $\mathbf{a} \cdot \mathbf{a} \ge 0$, and $\mathbf{a} \cdot \mathbf{a} = 0$ if and only if $\mathbf{a} = \mathbf{0}$ (zero vector).

## Applications
- **Calculating Angle / [[Cosine_Similarity|Cosine Similarity]]:** Measuring similarity between vectors.
- **Checking for [[Orthogonal_Vectors|Orthogonality]]:** Fundamental in many areas, e.g., orthogonal bases, signal processing.
- **Projections:** Projecting one vector onto another.
- **Work in Physics:** If $\mathbf{F}$ is force and $\mathbf{d}$ is displacement, work $W = \mathbf{F} \cdot \mathbf{d}$.
- **Machine Learning:**
    - Calculating similarity scores in recommendation systems.
    - Core operation in neural network layers (weighted sum of inputs).
    - In Support Vector Machines (SVMs) for kernel calculations.
    - Loss function components.

---