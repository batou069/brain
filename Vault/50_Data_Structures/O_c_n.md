---
tags:
  - data_structures
  - algorithms
  - complexity
  - big_o
  - intractable
aliases:
  - Exponential Time
  - O(c^n)
  - O(2^n)
related:
  - "[[Computational_Complexity]]"
  - "[[Time_Complexity]]"
  - "[[Space_Complexity]]"
  - "[[O_n_factorial]]"
  - "[[Traveling_Salesperson_Problem]]"
  - "[[Subset_Sum_Problem]]"
worksheet:
  - WS7
date_created: 2025-04-12
---
# O(c^n) - Exponential Complexity

## Definition

**O(c^n)**, where `c` is a constant greater than 1 (often `c=2`, i.e., `O(2^n)`), denotes **exponential complexity**. An algorithm or operation takes exponential time or space if its resource usage grows exponentially with the size of the input `n`. Adding just one element to the input can potentially double (or multiply by `c`) the resource usage.

## Key Aspects

- **Rapid Growth:** Resource usage grows extremely quickly as `n` increases.
- **Intractable:** Exponential time algorithms are generally considered **intractable** or infeasible for all but the smallest input sizes. Even moderate values of `n` can lead to computation times longer than the age of the universe.
- **Common Causes:** Often arise from brute-force algorithms that explore all possible combinations or subsets of the input (e.g., checking all `2^n` subsets of `n` items).

## Examples

- **Time Complexity O(2^n):**
    - Finding the exact solution to the [[Traveling_Salesperson_Problem]] using a naive brute-force approach (checking all possible tours).
    - Solving the [[Subset_Sum_Problem]] using a simple recursive or brute-force approach.
    - Generating all possible subsets of a set of size `n`.
    - Calculating Fibonacci numbers using a naive recursive implementation without memoization.

## Related Concepts
- [[Computational_Complexity]]
- [[Time_Complexity]], [[Space_Complexity]]
- [[O_n_factorial|Factorial Complexity O(n!)]] (Even worse growth rate)
- [[O_n_c|Polynomial Complexity]] (Much more desirable/tractable than exponential)
- NP-Hard Problems (Many problems for which only exponential time exact algorithms are known fall into this category)

---
**Source:** Worksheet WS7