---
tags:
  - data_structures
  - concept
  - adt
  - linear
aliases:
  - Linked List
related:
  - Abstract_Data_Type
  - Data_Structure
  - List_ADT
  - Singly_Linked_List_DS
  - Doubly_Linked_List_DS
  - Circular_Linked_List_DS
  - Node_DS
  - Pointer_C
  - Sequential_Access
  - Dynamic_Allocation_C
worksheet:
  - WS7
  - WS9
date_created: 2025-04-14
---
# Linked List (ADT)

## Definition

A **Linked List** is a linear [[Abstract_Data_Type|Abstract Data Type (ADT)]] where elements (often called **nodes**) are not necessarily stored in contiguous memory locations. Instead, each element contains the data itself and one or more **pointers** (links) that reference the next (and possibly previous) element in the sequence.

## Core Operations (Typical for a List ADT)

-   `insert(item, position)`: Adds an item at a specific position.
-   `delete(position)`: Removes the item at a specific position.
-   `append(item)`: Adds an item to the end.
-   `prepend(item)`: Adds an item to the beginning.
-   `get(position)`: Retrieves the item at a specific position.
-   `search(item)`: Finds the position of a given item.
-   `isEmpty()`: Checks if the list is empty.
-   `size()`: Returns the number of items.

## Key Aspects

- **Nodes:** Consists of nodes, where each node typically contains:
    - Data field(s).
    - Pointer(s) to other node(s).
- **Dynamic Size:** Size can grow and shrink easily at runtime by allocating/deallocating nodes using [[Dynamic_Allocation_C]].
- **Non-Contiguous Memory:** Nodes can be scattered throughout memory ([[Heap_Memory_C]]).
- **[[Sequential_Access]]:** Accessing an element at a specific position usually requires traversing the list from the beginning (or end, for doubly linked lists), making access by index an [[O_n]] operation. This contrasts with the [[O_1]] indexed access of arrays/vectors.
- **Efficient Insertion/Deletion:** Inserting or deleting an element at a known position (once the node is found or if inserting/deleting at the head/tail) is typically efficient ([[O_1]]), as it only involves updating pointers, unlike arrays where elements might need shifting. Finding the position first might still take O(n).
- **Pointer Overhead:** Each node requires extra memory space for the pointer(s).

## Common Implementations (Data Structures)

- **[[Singly_Linked_List_DS]]:** Each node points only to the *next* node in the sequence. Traversal is only possible in one direction.
- **[[Doubly_Linked_List_DS]]:** Each node points to *both* the *next* and the *previous* nodes. Allows traversal in both directions.
- **[[Circular_Linked_List_DS]]:** The last node points back to the first node (and optionally the first points to the last in a doubly circular list), forming a ring.

## Visualization (Conceptual Singly Linked List)

```mermaid
graph LR
    Head --> NodeA[Data: A, Next]
    NodeA --o NodeB[Data: B, Next]
    NodeB --o NodeC[Data: C, Next]
    NodeC --o Null[NULL]

    style Head fill:#fff,stroke:#f00,stroke-width:2px
```

## Use Cases / Real-World Examples (WS7)

- **Implementing other ADTs:** Used as the underlying structure for [[Stack_ADT|Stacks]] and [[Queue_ADT|Queues]].
- **Dynamic Memory Management:** Used internally by memory allocators.
- **File Systems:** Maintaining lists of free blocks or directory entries.
- **Undo Functionality:** Storing a sequence of operations.
- **Situations with Frequent Insertions/Deletions:** More efficient than arrays when insertions/deletions in the middle are common and random access is not the priority.

## Related Concepts
- [[Abstract_Data_Type]], [[Data_Structure]], [[List_ADT]]
- [[Singly_Linked_List_DS]], [[Doubly_Linked_List_DS]], [[Circular_Linked_List_DS]], [[Skip_List_DS]] (Implementations)
- [[Node_DS]] (Building block - *to be created*)
- [[Pointer_C]] (Essential for linking nodes)
- [[Sequential_Access]] (Primary access method)
- [[Direct_Access]] (Contrast with arrays)
- [[Dynamic_Allocation_C]] (Used for node creation/deletion)

---
**Source:** Worksheet WS7, WS9