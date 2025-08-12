---
tags:
  - data_structures
  - algorithms
  - complexity
  - big_o
aliases:
  - Log-linear Time
  - Linearithmic Time
  - O(n log n)
related:
  - "[[Computational_Complexity]]"
  - "[[Time_Complexity]]"
  - "[[Space_Complexity]]"
  - "[[Sorting_Algorithms]]"
  - "[[Merge_Sort]]"
  - "[[Heap_Sort]]"
  - "[[Quick_Sort]]"
worksheet:
  - WS7
date_created: 2025-04-12
---
# O(n log n) - Log-linear Complexity

## Definition

**O(n log n)** denotes **log-linear** or **linearithmic complexity**. An algorithm or operation takes O(n log n) time or space if its resource usage grows by a factor of `n` multiplied by the logarithm of `n`. This complexity often arises in algorithms that use a "divide and conquer" strategy, breaking the problem into smaller subproblems, solving them independently (often involving logarithmic steps), and then combining the results (often involving linear steps).

## Key Aspects

- **Efficiency:** Generally considered quite efficient, especially for comparison-based [[Sorting_Algorithms]]. Grows faster than O(n) but much slower than polynomial complexities like O(n^2).
- **Divide and Conquer:** Common pattern leading to this complexity.

## Examples

- **Time Complexity O(n log n):**
    - Efficient comparison-based sorting algorithms:
        - [[Merge_Sort]] (Worst-case and average-case)
        - [[Heap_Sort]] (Worst-case and average-case)
        - [[Quick_Sort]] (Average-case, but worst-case is O(n^2))
    - Building a balanced [[Binary_Search_Tree_DS]] from `n` elements.
    - Fast Fourier Transform (FFT).

## Related Concepts
- [[Computational_Complexity]]
- [[Time_Complexity]], [[Space_Complexity]]
- [[Sorting_Algorithms]]
- Divide and Conquer paradigm