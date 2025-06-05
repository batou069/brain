---
tags:
  - c
  - concept
  - error
  - data_structures
  - iterator
  - pointer
aliases:
  - Iterator Invalidation Problem
related:
  - Iterator_C
  - Pointer_C
  - Vector_DS
  - Linked_List_ADT
  - Undefined_Behavior_C
  - Memory_Management
worksheet:
  - WS9
date_created: 2025-04-14
---
# Iterator Invalidation

## Definition

**Iterator Invalidation** refers to the situation where an [[Iterator_C|iterator]] (or a [[Pointer_C]] acting as an iterator) pointing to an element within a container [[Data_Structure]] becomes **invalid** because the underlying container has been modified in a way that changes its structure or element locations after the iterator was created. Using an invalidated iterator leads to [[Undefined_Behavior_C]].

## Causes of Invalidation

The specific operations that invalidate iterators depend heavily on the underlying data structure:

1.  **[[Vector_DS|Vectors / Dynamic Arrays]]:**
    -   **Insertion/Deletion (Middle):** Inserting or deleting elements generally invalidates all iterators/pointers pointing to elements *at or after* the modification point (due to element shifting).
    -   **Resizing (Append/Insert causing reallocation):** If adding an element causes the vector's underlying array to be reallocated (moved to a new memory location), **all** existing iterators and pointers to elements in the *old* array become invalid (they become dangling pointers).

2.  **[[Linked_List_ADT|Linked Lists]]:**
    -   **Deletion:** Deleting the node that an iterator points to invalidates that specific iterator. Iterators pointing to *other* nodes generally remain valid (unless it's the only node, affecting head/tail).
    -   **Insertion:** Inserting a node generally does *not* invalidate iterators pointing to *existing* nodes (as existing nodes don't move). However, care must be taken when iterating and inserting simultaneously.

3.  **[[Hash_Table_DS|Hash Tables]]:**
    -   **Rehashing:** Any operation that causes the hash table to resize and rehash its elements (typically insertions) usually invalidates **all** existing iterators.
    -   **Deletion:** Deleting the element an iterator points to invalidates that iterator. Depending on the implementation (e.g., open addressing), deleting might sometimes affect other iterators.

## Consequences of Using Invalidated Iterators

- Dereferencing an invalidated iterator/pointer.
- Incrementing/decrementing an invalidated iterator.
- Comparing an invalidated iterator.
... all lead to **[[Undefined_Behavior_C]]**, potentially causing:
- Program crashes (segmentation faults).
- Reading/writing incorrect memory locations (data corruption).
- Infinite loops or incorrect loop termination.
- Seemingly random errors that are hard to debug.

## Prevention Strategies

- **Understand Container Guarantees:** Know which operations invalidate iterators for the specific data structure you are using (consult documentation, e.g., C++ STL iterator invalidation rules).
- **Re-acquire Iterators:** After performing an operation known to potentially invalidate iterators, re-acquire the iterator if needed (e.g., get a new iterator to the desired position).
- **Careful Iteration and Modification:** When modifying a container while iterating over it:
    - Use container-specific methods if available (e.g., Java's `Iterator.remove()`).
    - If deleting the current element, make sure to obtain the *next* iterator/pointer *before* deleting the current one (common pattern in linked lists).
    - Be aware that insertions might invalidate iterators depending on the structure.
- **Use Indices (Carefully):** For array-based structures, using integer indices *might* be safer than iterators/pointers across some modifications (like appending without reallocation), but indices become invalid if elements are inserted/deleted *before* the indexed position. Indices are also invalidated by reallocation.

## Related Concepts
- [[Iterator_C]], [[Pointer_C]] (The entities that get invalidated)
- [[Data_Structure]] ([[Vector_DS]], [[Linked_List_ADT]], [[Hash_Table_DS]], etc. - have different invalidation rules)
- [[Undefined_Behavior_C]] (The result of using invalidated iterators)
- [[50_Data_Structures/Memory_Management]], [[Dynamic_Allocation_C]], [[realloc_C]] (Reallocation is a common cause)

---
**Source:** Worksheet WS9