---
tags:
  - data_structures
  - algorithms
  - complexity
  - big_o
aliases:
  - Logarithmic Time
  - O(log n)
  - Linear Time
  - O(n)
related:
  - "[[Computational_Complexity]]"
  - "[[Time_Complexity]]"
  - "[[Space_Complexity]]"
  - "[[Binary_Search]]"
  - "[[Balanced_Binary_Search_Tree_DS]]"
  - "[[Heap_DS]]"
  - "[[Array_C]]"
  - "[[Linked_List_ADT]]"
worksheet:
  - WS7
date_created: 2025-04-21
---
# O(log n) - Logarithmic Complexity

## Definition

**O(log n)** denotes **logarithmic complexity**. An algorithm or operation takes O(log n) time or space if its resource usage grows logarithmically with the input size (`n`). This typically occurs when the algorithm repeatedly divides the problem size by a constant fraction (e.g., halves it) in each step. The base of the logarithm (e.g., log base 2, log base 10) is usually ignored in Big O notation as it only differs by a constant factor.

## Key Aspects

- **Efficiency:** Very efficient. The time/space required grows very slowly as the input size increases. Doubling the input size only adds a constant amount of work/space.
- **Divide and Conquer:** Often associated with algorithms that eliminate a large portion of the search space in each step.

## Examples

- **Time Complexity O(log n):**
    - Binary Search in a sorted array.
    - Finding an element in a balanced [[Binary_Search_Tree_DS]] (like AVL tree, Red-Black tree).
    - Inserting/deleting elements in a balanced [[Binary_Search_Tree_DS]].
    - Inserting/deleting elements (heapify up/down) in a [[Heap_DS]].
    - Calculating `x^n` using exponentiation by squaring.

- **Space Complexity O(log n):**
    - Recursive algorithms where the recursion depth is logarithmic (e.g., recursive binary search uses O(log n) stack space).

## Related Concepts
- [[Computational_Complexity]]
- [[Time_Complexity]], [[Space_Complexity]]
- Binary Search Algorithm
- Balanced Trees, Heaps

# O(n) - Linear Complexity

## Definition

**O(n)** denotes **linear complexity**. An algorithm or operation takes O(n) time or space if its resource usage grows **linearly** and in direct proportion to the size of the input (`n`). If the input size doubles, the time or space required roughly doubles.

## Key Aspects

- **Proportional Growth:** Resource usage scales directly with input size.
- **Common:** Many fundamental algorithms involve iterating through the input once.
- **Generally Efficient:** Considered efficient for many problems, especially when the entire input must be processed.

## Examples

- **Time Complexity O(n):**
    - Finding an element in an unsorted [[Array_C]] or [[Linked_List_ADT]] (linear search).
    - Traversing all elements of an array or linked list once.
    - Calculating the sum or average of all elements in an array.
    - Finding the minimum or maximum element in an unsorted array.
    - [[Hash_Table_DS]] operations (insert, delete, search) in the worst case (e.g., all keys hash to the same bucket).
- **Space Complexity O(n):**
    - Creating a copy of an array or list of size `n`.
    - Recursive algorithms with a linear recursion depth (e.g., naive recursive factorial calculation uses O(n) stack space).

## Related Concepts
- [[Computational_Complexity]]
- [[Time_Complexity]], [[Space_Complexity]]
- Linear Search
- Array/List Traversal