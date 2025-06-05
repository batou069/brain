---
tags:
  - data_structures
  - concept
  - technique
  - hash_table
aliases:
  - Hash Collision Resolution
related:
  - "[[Hash_Table_DS]]"
  - "[[Hash_Function]]"
  - "[[Separate_Chaining]]"
  - "[[Open_Addressing]]"
  - "[[Linear_Probing]]"
  - "[[Quadratic_Probing]]"
  - "[[Double_Hashing]]"
  - "[[Load_Factor]]"
worksheet: [WS7] # Implied by Hash Table
date_created: 2025-04-21
---
# Collision Resolution (Hash Tables)

## Definition

In a [[Hash_Table_DS]], a **collision** occurs when the [[Hash_Function]] produces the same index (bucket address) for two or more different keys. Since only one key-value pair can typically be stored directly at a single array index, **Collision Resolution Techniques** are strategies used to handle these collisions and allow all colliding keys to be stored and retrieved correctly.

## Purpose

- Ensure all keys can be stored, even if they hash to the same index.
- Maintain reasonable performance for insertion, deletion, and search operations despite collisions.

## Common Techniques

1.  **[[Separate_Chaining|Separate Chaining (Closed Addressing)]]:**
    -   **Idea:** Each bucket (slot) in the hash table array does not store the element directly, but instead points to a secondary data structure (typically a [[Linked_List_ADT|linked list]]) that holds all the key-value pairs whose keys hash to that index.
    -   **Operations:**
        -   *Insert:* Hash the key to find the bucket index. Insert the key-value pair into the linked list at that index (e.g., add to head). O(1) if list is short.
        -   *Search/Delete:* Hash the key to find the bucket index. Search the linked list at that index for the key. Average time depends on list length (related to [[Load_Factor]]).
    -   **Pros:** Simple to implement. Performance degrades gracefully with increasing load factor. Deletion is straightforward.
    -   **Cons:** Requires extra memory for pointers in the linked lists. Can have O(n) worst-case performance if all keys hash to the same bucket (long list). Cache performance might be worse due to scattered list nodes.

2.  **[[Open_Addressing|Open Addressing (Closed Hashing)]]:**
    -   **Idea:** All key-value pairs are stored directly within the hash table array itself. When a collision occurs (the target bucket `h(key)` is already occupied by a *different* key), systematically probe for alternative empty slots in the array until one is found.
    -   **Probing Sequences:** Different strategies exist for finding the next slot:
        -   **[[Linear_Probing]]:** Try `h(key)+1`, `h(key)+2`, `h(key)+3`, ... (wrapping around). Suffers from *primary clustering* (long runs of occupied slots).
        -   **[[Quadratic_Probing]]:** Try `h(key)+1^2`, `h(key)+2^2`, `h(key)+3^2`, ... (wrapping). Reduces primary clustering but can suffer from *secondary clustering* (keys hashing to same initial slot follow same probe sequence).
        -   **[[Double_Hashing]]:** Use a second hash function to determine the step size for probing: `h1(key) + i * h2(key)`. Generally provides the best distribution and avoids clustering issues but requires a good second hash function.
    -   **Operations:**
        -   *Insert:* Hash key, probe until an empty slot is found, insert.
        -   *Search:* Hash key, probe along the same sequence until the key is found or an *empty* slot is encountered (indicating key is not present).
        -   *Delete:* Deletion is complex. Simply emptying the slot can break probe sequences for later searches. Usually requires marking the slot as "deleted" (tombstone) rather than "empty", which complicates insertion and search slightly.
    -   **Pros:** No pointer overhead, potentially better cache performance (data stored together in array).
    -   **Cons:** Performance degrades sharply as load factor gets high (approaching 1). Deletion is complex. Requires careful implementation of probing to avoid clustering. Load factor must be kept below 1 (ideally below 0.7 or 0.5 depending on technique).

## Related Concepts
- [[Hash_Table_DS]] (Where collisions occur)
- [[Hash_Function]] (A good function minimizes collisions)
- [[Separate_Chaining]], [[Open_Addressing]] (Main categories of techniques)
- [[Linear_Probing]], [[Quadratic_Probing]], [[Double_Hashing]] (Specific open addressing methods)
- [[Load_Factor]] (Ratio affecting collision probability)
- [[Rehashing]] (Often triggered when load factor gets too high)

---
**Source:** Worksheet WS7 (Implied)