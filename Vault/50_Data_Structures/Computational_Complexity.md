---
tags:
  - data_structures
  - algorithms
  - concept
  - analysis
  - performance
aliases:
  - Complexity Analysis
  - Big O Notation
  - Asymptotic Analysis
related:
  - "[[Algorithm]]"
  - "[[Data_Structure]]"
  - "[[Time_Complexity]]"
  - "[[Space_Complexity]]"
  - "[[Amortized_Complexity]]"
  - "[[O_1]]"
  - "[[O_log_n]]"
  - "[[O_n]]"
  - "[[O_n_log_n]]"
  - "[[O_n_c]]"
  - "[[O_c_n]]"
worksheet:
  - WS7
date_created: 2025-04-12
---
# Computational Complexity

## Definition

**Computational Complexity** is a field in theoretical computer science and mathematics that focuses on classifying computational problems according to their inherent difficulty and relating those classes to each other. In the context of [[Algorithm|algorithms]] and [[Data_Structure|data structures]], complexity analysis typically refers to **Asymptotic Analysis**, which describes the resource usage (usually [[Time_Complexity|execution time]] or [[Space_Complexity|memory space]]) of an algorithm or operation as the input size (`n`) grows towards infinity. **Big O notation** is the most common notation used.

## Key Aspects / Characteristics

- **Resource Measurement:** Quantifies the amount of resources (time, space) an algorithm consumes.
- **Input Size Dependence:** Expresses resource usage as a function of the size of the input (`n`).
- **Asymptotic Behavior:** Focuses on the growth rate of resource usage as `n` becomes very large, ignoring constant factors and lower-order terms. This provides a high-level understanding of scalability.
- **Big O Notation (`O`):** Describes the **upper bound** on the growth rate (worst-case complexity). `f(n) = O(g(n))` means `f(n)` grows no faster than `g(n)`.
- **Other Notations:**
    - **Omega (`Ω`):** Describes the **lower bound** (best-case complexity).
    - **Theta (`Θ`):** Describes a **tight bound** (both upper and lower bound are the same; average-case or exact complexity). Big O is often used informally even when Theta might be more precise.
- **Common Complexity Classes:** (See individual files like [[O_1]], [[O_log_n]], etc.)
    - `O(1)`: Constant time/space.
    - `O(log n)`: Logarithmic time/space.
    - `O(n)`: Linear time/space.
    - `O(n log n)`: Log-linear or linearithmic time/space.
    - `O(n^c)` (for c > 1): Polynomial time/space (e.g., `O(n^2)` quadratic, `O(n^3)` cubic).
    - `O(c^n)` (for c > 1): Exponential time/space (e.g., `O(2^n)`). Generally considered intractable for large `n`.
    - `O(n!)`: Factorial time/space (even worse than exponential).
- **Worst-Case, Average-Case, Best-Case:** Complexity can be analyzed for different scenarios, with worst-case (Big O) being the most common focus for guarantees.
- **[[Amortized_Complexity]]:** Analyzes the average cost of operations over a sequence of operations, smoothing out occasional expensive operations.

## Purpose

- **Algorithm Comparison:** Allows comparing the efficiency and scalability of different algorithms or data structure operations.
- **Performance Prediction:** Helps predict how performance will degrade as input size increases.
- **Feasibility Assessment:** Determines if an algorithm is practical for the expected input size (e.g., exponential algorithms are usually infeasible for large inputs).
- **Guiding Choices:** Informs the selection of appropriate data structures and algorithms for a given problem.

## Related Concepts
- [[Algorithm]], [[Data_Structure]] (Complexity analyzes their performance)
- [[Time_Complexity]], [[Space_Complexity]] (The resources measured)
- [[Amortized_Complexity]] (Averaged complexity over sequences)
- Big O, Omega, Theta notations
- Specific complexity classes: [[O_1]], [[O_log_n]], [[O_n]], [[O_n_log_n]], [[O_n_c]], [[O_c_n]]

---
**Source:** Worksheet WS7, Wikipedia: Computational complexity theory, Big O notation