---
tags:
  - algorithms
  - paradigms
  - dynamic_programming
  - optimization
  - concept
aliases:
  - DP
related:
  - "[[Recursion]]"
  - "[[Memoization]]"
  - "[[Tabulation]]"
  - "[[Computational_Complexity]]"
worksheet:
  - WS_Math_Foundations_2
date_created: 2025-08-20
---
# Dynamic Programming

## Definition
**Dynamic Programming (DP)** is a powerful algorithmic technique for solving complex problems by breaking them down into a collection of simpler subproblems, solving each of those subproblems just once, and storing their solutions. The next time the same subproblem occurs, instead of recomputing its solution, one simply looks up the previously computed solution.

This approach is particularly useful for optimization problems that exhibit two key properties:
1.  **Overlapping Subproblems:** The problem can be broken down into subproblems that are reused several times.
2.  **Optimal Substructure:** The optimal solution to the overall problem can be constructed from the optimal solutions of its subproblems.

## Main Approaches
There are two main ways to implement a dynamic programming algorithm:

[list2tab|#DP Approaches]
- Memoization (Top-Down)
    - **Description:** This is a recursive approach. The main function is written recursively to solve the problem in a natural way. The results of the subproblems are stored in a lookup table (e.g., a dictionary or array). Before computing a subproblem, the algorithm first checks if the solution is already in the table. If it is, it's returned directly. If not, it's computed and then stored in the table before being returned.
    - **Analogy:** Solving a problem by breaking it down, and writing down the answer to any smaller problem you solve so you don't have to solve it again.
- Tabulation (Bottom-Up)
    - **Description:** This is an iterative approach. The algorithm starts by solving the smallest possible subproblems and builds up to the solution of the main problem. It fills a table (the "DP table") in a specific order, ensuring that when it needs to solve a subproblem, the solutions to all its prerequisite subproblems are already available in the table.
    - **Analogy:** Building a solution from the ground up, starting with the simplest cases and using them to construct solutions to bigger and bigger cases.

## Example: Fibonacci Sequence
The Fibonacci sequence is a classic example to illustrate DP. The naive recursive solution is $F(n) = F(n-1) + F(n-2)$, which has exponential time complexity $O(2^n)$ due to recomputing the same subproblems many times.

### Python Implementation (with DP)

```python
# 1. Naive Recursive (for comparison - very slow)
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

# 2. DP with Memoization (Top-Down)
memo = {}
def fib_memo(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    result = fib_memo(n - 1) + fib_memo(n - 2)
    memo[n] = result
    return result

# 3. DP with Tabulation (Bottom-Up)
def fib_tab(n):
    if n <= 1:
        return n
    # DP table (array)
    dp = * (n + 1)
    dp = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# Example usage
n = 35
# print(f"Naive Fib({n}): {fib_naive(n)}") # This would be very slow
print(f"Memoized Fib({n}): {fib_memo(n)}")
print(f"Tabulated Fib({n}): {fib_tab(n)}")

# Expected Output:
# Memoized Fib(35): 9227465
# Tabulated Fib(35): 9227465
```
Both DP approaches reduce the time complexity from $O(2^n)$ to $O(n)$ and space complexity to $O(n)$ (or $O(1)$ if we only store the last two values in the tabulation method).

## Common DP Problems
- **Fibonacci Sequence**
- **Longest Common Subsequence (LCS):** Finding the longest subsequence common to two sequences.
- **Longest Increasing Subsequence (LIS):** Finding the length of the longest subsequence of a given sequence such that all elements of the subsequence are sorted in increasing order.
- **Edit Distance (Levenshtein Distance):** Finding the minimum number of edits (insertions, deletions, substitutions) to change one word into another.
- **Knapsack Problem (0/1):** Given items with weights and values, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.
- **Matrix Chain Multiplication:** Finding the most efficient way to multiply a chain of matrices (see [[Matrix_Multiplication_Associativity]]).
- **Shortest Path in a DAG:** Finding the shortest path from a source to all other vertices in a Directed Acyclic Graph.

Dynamic programming is a powerful technique for solving a wide range of optimization and counting problems in computer science.

---