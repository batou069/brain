---
tags:
  - data_structures
  - algorithms
  - complexity
  - analysis
  - memory
aliases:
  - Memory Complexity
related:
  - "[[Computational_Complexity]]"
  - "[[Time_Complexity]]"
  - "[[Big_O_Notation]]"
  - "[[Algorithm_Analysis]]"
  - "[[50_Data_Structures/Memory_Management]]"
  - "[[Stack_Memory_C]]"
  - "[[Heap_Memory_C]]"
worksheet:
  - WS7
date_created: 2025-04-12
---
# Space Complexity

## Definition

**Space Complexity** is a measure within [[Computational_Complexity|computational complexity analysis]] that quantifies the total amount of **memory space** (memory) required by an algorithm to run as a function of the length or size of its input (`n`). It includes both the space needed for the input data and any auxiliary space used by the algorithm during execution (e.g., for temporary variables, data structures, recursion stack).

## Key Aspects

- **Measures Memory Usage Growth:** Focuses on how memory consumption scales with input size.
- **Components:** Often considered in two parts:
    - **Input Space:** Space required to store the input data itself. Often excluded when comparing algorithms if it's the same for all alternatives.
    - **Auxiliary Space:** Extra space used by the algorithm beyond the input space (e.g., temporary arrays, variables, [[Stack_Memory_C|stack space]] for recursion). This is often the primary focus when analyzing space complexity.
- **Asymptotic Analysis:** Typically expressed using [[Big_O_Notation|asymptotic notation]] (like Big O) to describe the growth rate of memory usage as `n` increases.
- **Worst-Case:** Usually refers to the maximum space needed for any input of size `n`.

## Examples

- **O(1) Space (Constant):** Algorithms using only a fixed number of variables regardless of input size (e.g., iterative in-place array reversal, finding max element iteratively).
- **O(log n) Space:** Recursive binary search (due to [[Stack_Memory_C|stack frames]] for recursion depth).
- **O(n) Space (Linear):** Creating a copy of an input array of size `n`; recursive factorial or Fibonacci (naive versions, due to stack depth); storing counts in a hash map for `n` distinct items.
- **O(n^2) Space (Quadratic):** Creating an `n x n` adjacency matrix for a graph with `n` vertices.

## Time-Space Trade-off

Often, there is a **trade-off** between [[Time_Complexity]] and Space Complexity. An algorithm might be made faster by using more memory (e.g., memoization, lookup tables), or made more memory-efficient by taking more time (e.g., re-computing values instead of storing them). Choosing the right balance depends on the specific constraints of the problem (available memory, required speed).

## Related Concepts
- [[Computational_Complexity]]
- [[Time_Complexity]] (The other main resource measured)
- [[Big_O_Notation]] (Common notation used)
- [[Algorithm_Analysis]]
- [[50_Data_Structures/Memory_Management]], [[Stack_Memory_C]], [[Heap_Memory_C]] (Where space is used)
- In-place Algorithm (An algorithm with O(1) auxiliary space complexity)

---
**Source:** Worksheet WS7