---
tags:
  - data_structures
  - concept
  - implementation
  - associative
  - map
aliases:
  - Hash Map
  - Dictionary (Implementation Context)
  - Associative Array
related:
  - Data_Structure
  - Map_ADT
  - Set_ADT
  - Hash_Function
  - Collision_Resolution
  - Array_C
  - Linked_List_ADT
  - Amortized_Complexity
  - O_1
worksheet:
  - WS7
date_created: 2025-04-14
---
# Hash Table

## Definition

A **Hash Table** (also known as a Hash Map) is a [[Data_Structure]] that implements an associative array abstract data type ([[Map_ADT]]), which maps **keys** to **values**. It uses a [[Hash_Function]] to compute an index (a "hash code," often mapped to a "bucket" index) into an underlying [[Array_C]] (the "hash table"), from which the desired value can be found.

## Key Aspects / Characteristics

- **Key-Value Mapping:** Stores pairs of (key, value).
- **Hash Function:** Uses a [[Hash_Function]] to convert a key into an index into the array. A good hash function distributes keys uniformly across the array indices.
- **Array Storage:** Uses an array (often called the bucket array) as the primary storage mechanism.
- **Fast Lookups (Average Case):** The main advantage is very fast average time complexity for insertion, deletion, and search (lookup) operations - typically **[[O_1]] on average**.
- **Collisions:** Occur when the hash function generates the same index for two or more different keys. [[Collision_Resolution|Collision resolution techniques]] are essential for a functional hash table.
- **Collision Resolution Techniques:**
    - **Separate Chaining:** Each array slot (bucket) points to a [[Linked_List_ADT|linked list]] (or other data structure) containing all key-value pairs that hash to that index.
    - **Open Addressing:** If a collision occurs, probe for the next available slot in the array itself according to a defined sequence (e.g., linear probing, quadratic probing, double hashing).
- **Load Factor:** The ratio of the number of stored elements to the number of buckets in the array (`Load Factor = n / capacity`). Performance degrades as the load factor increases (more collisions).
- **Resizing (Rehashing):** When the load factor exceeds a certain threshold, the hash table is typically resized (a larger array is allocated), and all existing elements must be **rehashed** (their indices recalculated based on the new array size) and inserted into the new table. This is an O(n) operation but leads to O(1) [[Amortized_Complexity|amortized]] insertion time if done correctly (e.g., doubling size).
- **Worst-Case Complexity:** In the worst case (e.g., all keys hash to the same bucket), performance degrades to [[O_n]] for search, insertion, and deletion (equivalent to searching a linked list).

## Visualization (Separate Chaining)

**Hash Function:** `hash(key) -> index`
**Bucket Array:** (Size 7)
```
Index 0: -> NULL
Index 1: -> [KeyA, ValA] -> [KeyH, ValH] -> NULL
Index 2: -> [KeyB, ValB] -> NULL
Index 3: -> NULL
Index 4: -> [KeyD, ValD] -> NULL
Index 5: -> [KeyE, ValE] -> [KeyL, ValL] -> NULL
Index 6: -> NULL
```
*Keys A and H hash to index 1. Keys E and L hash to index 5.*

## Use Cases / Real-World Examples (WS7)

- **Implementing Dictionaries/Maps:** Used internally by Python `dict`, Java `HashMap`/`HashSet`, C++ `std::unordered_map`/`std::unordered_set`.
- **Database Indexing:** Hashing is used to quickly locate data records based on keys.
- **Caches:** Used for fast lookups of cached data (e.g., web caches, memory caches).
- **Symbol Tables:** Compilers use hash tables to store information about identifiers (variables, functions).
- **Checking for Duplicates:** Efficiently track seen items by inserting them into a hash set (a hash table storing only keys).

## Related Concepts
- [[Data_Structure]], [[Map_ADT]], [[Set_ADT]]
- [[Hash_Function]] (Core component)
- [[Collision_Resolution]] (Separate Chaining, Open Addressing)
- [[Array_C]], [[Linked_List_ADT]] (Used in implementations)
- [[Amortized_Complexity]], [[O_1]] (Average time complexity)
- Load Factor, Rehashing

---
**Source:** Worksheet WS7