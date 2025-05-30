---
tags:
  - data_structures
  - concept
  - adt
  - linear
aliases:
  - Deque
  - Double Ended Queue
related:
  - Abstract_Data_Type
  - Data_Structure
  - Queue_ADT
  - Stack_ADT
  - Array_C
  - Doubly_Linked_List_DS
worksheet:
  - WS7
date_created: 2025-04-14
---
# Double-Ended Queue (Deque - ADT)

## Definition

A **Double-Ended Queue** (pronounced "deck"), or **Deque**, is a linear [[Abstract_Data_Type|Abstract Data Type (ADT)]] that generalizes a [[Queue_ADT|Queue]]. Unlike a standard queue where elements are added at one end (rear) and removed from the other (front), a deque allows elements to be added and removed efficiently from **both** ends (front and rear).

## Core Operations

-   **`addFront(item)`** (or `push_front`): Adds an item to the front end.
-   **`addRear(item)`** (or `push_back`, `enqueue`): Adds an item to the rear end.
-   **`removeFront()`** (or `pop_front`, `dequeue`): Removes and returns the item from the front end. Error if empty.
-   **`removeRear()`** (or `pop_back`): Removes and returns the item from the rear end. Error if empty.
-   **`peekFront()`** (or `front`): Returns the item at the front *without* removing it. Error if empty.
-   **`peekRear()`** (or `back`): Returns the item at the rear *without* removing it. Error if empty.
-   **`isEmpty()`:** Checks if the deque is empty.
-   **`size()`:** Returns the number of items.

## Key Aspects

- **Generalized Queue/Stack:** Can behave like a [[Queue_ADT]] (using `addRear` and `removeFront`) or a [[Stack_ADT]] (using `addRear`/`removeRear` or `addFront`/`removeFront`).
- **Bidirectional Access:** Allows efficient insertion and deletion at both ends.
- **Implementation:** Common implementations include:
    - **[[Doubly_Linked_List_DS]]:** Naturally supports O(1) insertion/deletion at both head (front) and tail (rear).
    - **Dynamic Array ([[Vector_DS]]) with Wrap-Around:** Similar to a [[Circular_Queue_DS]]/[[Circular_Buffer_DS]], using a dynamic array and indices that wrap around. Insertions/deletions at the front might require shifting or clever index management to maintain O(1) amortized performance. Some implementations use multiple blocks.

## Use Cases / Real-World Examples (WS7)

- **Job Scheduling Algorithms:** Some scheduling algorithms (like work-stealing) use deques.
- **Storing Undo/Redo History:** Can store a list of operations where additions/removals might happen at either end.
- **Palindrome Checking:** Can be used to efficiently compare characters from both ends of a string.
- **Implementing Sliding Window Algorithms:** Keeping track of elements within a moving window over a sequence.

## Related Concepts
- [[Abstract_Data_Type]], [[Data_Structure]]
- [[Queue_ADT]], [[Stack_ADT]] (Deque generalizes both)
- Implementation using [[Doubly_Linked_List_DS]], [[Vector_DS]] (often circular)

---
**Source:** Worksheet WS7