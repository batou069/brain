---
tags:
  - data_structures
  - concept
  - adt
aliases:
  - Priority Queue
related:
  - Abstract_Data_Type
  - Data_Structure
  - Queue_ADT
  - Heap_DS
  - Sorting_Algorithms
  - Scheduling_Algorithms
worksheet:
  - WS7
date_created: 2025-04-14
---
# Priority Queue (ADT)

## Definition

A **Priority Queue** is an [[Abstract_Data_Type|Abstract Data Type (ADT)]] similar to a regular [[Queue_ADT|Queue]] or [[Stack_ADT|Stack]], but where each element has an associated **priority**. Elements are added to the queue at any time, but when an element is removed (dequeued), it is always the element with the **highest priority** currently in the queue. If multiple elements have the same highest priority, their relative order might be based on FIFO or be undefined.

## Core Operations

-   **`insert(item, priority)`** (or `enqueue(item, priority)`): Adds an `item` with its associated `priority` to the queue.
-   **`extractMax()`** (or `deleteMax()`, `dequeueMax()`): Removes and returns the item with the highest priority from the queue. (Alternatively `extractMin` if lower values indicate higher priority).
-   **`peekMax()`** (or `findMax()`, `getMax()`): Returns the item with the highest priority *without* removing it. (Or `peekMin`).
-   **`increaseKey(item, new_priority)`** (Optional): Increases the priority of a specific item already in the queue. (Or `decreaseKey`).
-   **`isEmpty()`:** Returns true if the queue is empty.
-   **`size()`:** Returns the number of items.

## Key Aspects

- **Priority-Based Removal:** Unlike FIFO (Queue) or LIFO (Stack), removal is determined by priority.
- **Priority Definition:** "Highest" priority can mean the largest numeric value or the smallest numeric value, depending on the implementation (Max-Priority Queue vs. Min-Priority Queue).
- **Implementation:** Can be implemented using various [[Data_Structure|data structures]], with different performance trade-offs:
    - **Unsorted Array/List:** `insert` is O(1), `extractMax` is O(n) (requires searching).
    - **Sorted Array/List:** `insert` is O(n) (requires shifting/finding spot), `extractMax` is O(1) (if sorted by priority).
    - **[[Heap_DS|Heap]] (Binary Heap):** Most common and efficient implementation. `insert` is O(log n), `extractMax` is O(log n), `peekMax` is O(1). See [[Heap_Sort]].
    - **Balanced [[Binary_Search_Tree_DS]]:** `insert`, `extractMax`, `peekMax` are typically O(log n).

## Use Cases / Real-World Examples (WS7)

- **Event-Driven Simulations:** Managing events ordered by time.
- **Operating System Scheduling:** Scheduling processes based on priority.
- **Bandwidth Management:** Prioritizing network traffic.
- **Graph Algorithms:**
    - Dijkstra's algorithm (shortest path) uses a min-priority queue.
    - Prim's algorithm (minimum spanning tree) uses a priority queue.
- **Huffman Coding:** Used in the compression algorithm.
- **A* Search Algorithm:** Uses a priority queue to explore promising paths first.

## Related Concepts
- [[Abstract_Data_Type]], [[Data_Structure]]
- [[Queue_ADT]], [[Stack_ADT]] (Contrast in removal order)
- [[Heap_DS]] (Common efficient implementation)
- [[Sorting_Algorithms]] (Heapsort uses a heap, which is a priority queue implementation)
- Scheduling Algorithms

---
**Source:** Worksheet WS7