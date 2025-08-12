---
tags:
  - math
  - linear_algebra
  - concept
  - vector_operations
  - data_structures
aliases:
  - Scalar Product
  - Inner Product
related:
  - "[[Vector_Math]]"
  - "[[Linear_Algebra]]"
  - "[[Matrix_Operations]]"
  - "[[Norm]]"
  - "[[Orthogonality]]"
worksheet:
  - WS11
date_created: 2025-04-12
---
# Dot Product

## Definition

The **Dot Product** (also known as the **Scalar Product** or sometimes Inner Product in Euclidean space) is an algebraic operation that takes two equal-length sequences of numbers (usually coordinate [[Vector_Math|vectors]]) and returns a single **scalar** number. It is calculated by multiplying corresponding entries and summing those products.

## Calculation

For two vectors `a = [a1, a2, ..., an]` and `b = [b1, b2, ..., bn]`, the dot product `a · b` is calculated as:

`a · b = Σ (ai * bi) = a1*b1 + a2*b2 + ... + an*bn`

Using [[Matrix_Multiplication]] notation, if `a` and `b` are [[Column_Vector|column vectors]], the dot product is equivalent to `a^T * b` (transpose of `a` multiplied by `b`).

## Geometric Interpretation

Geometrically, the dot product is related to the angle (`θ`) between the two vectors and their magnitudes (lengths, `||a||` and `||b||`):

`a · b = ||a|| * ||b|| * cos(θ)`

This implies:
- If `a · b = 0`, the vectors are orthogonal (perpendicular), assuming non-zero vectors.
- If `a · b > 0`, the angle between them is acute (< 90°).
- If `a · b < 0`, the angle between them is obtuse (> 90°).
- `a · a = ||a||^2` (The dot product of a vector with itself is the square of its magnitude).

## Properties

- **Commutative:** `a · b = b · a`
- **Distributive over vector addition:** `a · (b + c) = a · b + a · c`
- **Bilinear:** `(c*a) · b = a · (c*b) = c * (a · b)` for scalar `c`.

## Example Calculation

Let `a = [1, 2, 3]` and `b = [4, -5, 6]`

`a · b = (1 * 4) + (2 * -5) + (3 * 6)`
`a · b = 4 - 10 + 18`
`a · b = 12`

## Use Cases

- Calculating the angle between two vectors.
- Projecting one vector onto another.
- Checking for orthogonality (perpendicularity).
- Used extensively in physics (e.g., calculating work: Work = Force · Displacement).
- Core operation in machine learning (e.g., calculating weighted sums in neural networks, similarity measures like cosine similarity).
- Fundamental to [[Matrix_Multiplication]].

## Related Concepts
- [[Vector_Math]]
- [[Linear_Algebra]]
- [[Matrix_Operations]]
- [[Matrix_Multiplication]]
- Vector Magnitude (Norm)
- [[Orthogonality]]
---
**Source:** Worksheet WS11
