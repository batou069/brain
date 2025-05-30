---
tags:
  - data_structures
  - algorithms
  - complexity
  - analysis
  - average
aliases:
  - Amortized Analysis
related:
  - "[[Computational_Complexity]]"
  - "[[Time_Complexity]]"
  - "[[Vector_DS]]"
  - "[[Hash_Table_DS]]"
  - "[[Big_O_Notation]]"
worksheet:
  - WS7
  - WS8
date_created: 2025-04-12
---
# Amortized Complexity

## Definition

**Amortized Complexity** (or Amortized Analysis) is a method for analyzing the [[Time_Complexity]] of a sequence of operations performed on a [[Data_Structure]]. Instead of focusing on the worst-case cost of a single operation, it calculates the **average cost per operation** over the entire sequence. This is particularly useful when occasional operations are very expensive, but most operations are cheap, and the expensive operations ensure that subsequent operations remain cheap for a while.

## Key Aspects

- **Average Over Sequence:** Calculates the average time per operation across a sequence of operations.
- **Smoothes Out Peaks:** Averages out the cost of infrequent but expensive operations over the more frequent cheap operations.
- **Guarantee Over Sequence:** Provides a guarantee on the average performance per operation in the long run, even if individual operations might occasionally exceed this average cost.
- **Not Average-Case:** Distinct from average-case analysis (which averages over random inputs for a single operation). Amortized analysis considers a specific sequence of operations and averages the cost, even in the worst-case sequence.
- **Common Techniques:** Aggregate analysis, accounting method, potential method.

## Examples / Use Cases

- **[[Vector_DS|Dynamic Array (Vector)]] Appending:**
    - Most `append` operations take [[O_1]] time (just add element if space available).
    - Occasionally, when the array is full, it needs to be resized (allocate a new, larger array, copy elements, deallocate old array). This resize operation takes [[O_n]] time, where `n` is the current number of elements.
    - However, if the array size is consistently doubled during resizing ([[Geometric_Expansion]]), the expensive O(n) resizes happen infrequently enough that the *amortized* cost of each `append` operation over a long sequence averages out to **O(1)**. The cost of resizing is "paid for" by the cheap appends that preceded it.
- **[[Hash_Table_DS|Hash Table]] with Resizing:** Similar to dynamic arrays, inserting into a hash table is typically O(1) on average, but occasionally requires resizing the table (rehashing), which takes O(n) time. The amortized cost per insertion remains O(1) on average if resizing is done appropriately.
- **Multipop Stack:** A stack supporting a `multipop(k)` operation that pops `k` elements. While `multipop(k)` can take O(k) time, any sequence of `n` `push`, `pop`, and `multipop` operations takes at most O(n) total time, meaning the amortized cost per operation is O(1).

## Related Concepts
- [[Computational_Complexity]], [[Time_Complexity]]
- [[Big_O_Notation]] (Used to express amortized bounds)
- [[Vector_DS]] (Classic example where amortized analysis is used for append)
- [[Hash_Table_DS]] (Another common example for insertion)
- Average-Case Analysis (Different concept)

---
**Source:** Worksheet WS7, WS8