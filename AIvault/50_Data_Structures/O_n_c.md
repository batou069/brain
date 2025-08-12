---
tags:
  - data_structures
  - algorithms
  - complexity
  - big_o
aliases:
  - Polynomial Time
  - O(n^c)
  - O(n^2)
  - O(n^3)
  - Quadratic Time
  - Cubic Time
related:
  - "[[Computational_Complexity]]"
  - "[[Time_Complexity]]"
  - "[[Space_Complexity]]"
  - "[[Sorting_Algorithms]]"
  - "[[Bubble_Sort]]"
  - "[[Insertion_Sort]]"
  - "[[Selection_Sort]]"
  - "[[Matrix_Multiplication]]"
worksheet:
  - WS7
date_created: 2025-04-12
---
# O(n^c) - Polynomial Complexity

## Definition

**O(n^c)**, where `c` is a constant greater than 1, denotes **polynomial complexity**. An algorithm or operation takes polynomial time or space if its resource usage grows proportionally to the input size `n` raised to a constant power `c`. Common examples include `O(n^2)` (quadratic) and `O(n^3)` (cubic).

## Key Aspects

- **Growth Rate:** Grows significantly faster than linear (`O(n)`) or log-linear (`O(n log n)`) as `n` increases.
- **Feasibility:** Generally considered feasible or tractable for reasonably sized inputs, especially for small values of `c` (like 2 or 3). Algorithms with very high polynomial degrees can become impractical quickly.
- **Nested Loops:** Often arises from algorithms with nested loops iterating over the input data (e.g., two nested loops might lead to `O(n^2)`, three might lead to `O(n^3)`).

## Examples

- **Time Complexity O(n^2):**
    - Simple [[Sorting_Algorithms]]: [[Bubble_Sort]], [[Insertion_Sort]], [[Selection_Sort]] (in their typical implementations).
    - Finding the closest pair of points among `n` points (naive approach).
    - Iterating through all pairs of elements in a list of size `n`.
- **Time Complexity O(n^3):**
    - Standard [[Matrix_Multiplication]] algorithm for two `n x n` matrices.

## Related Concepts
- [[Computational_Complexity]]
- [[Time_Complexity]], [[Space_Complexity]]
- Nested Loops
- Comparison with [[O_c_n|Exponential Complexity]] (Polynomial is much better)