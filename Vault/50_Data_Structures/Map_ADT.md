---
tags:
  - data_structures
  - concept
  - adt
  - associative
  - collection
aliases:
  - Map ADT
  - Associative Array ADT
  - Dictionary ADT
  - Symbol Table ADT
related:
  - "[[Abstract_Data_Type]]"
  - "[[Data_Structure]]"
  - "[[Set_ADT]]"
  - "[[Hash_Table_DS]]"
  - "[[Balanced_Binary_Search_Tree_DS]]"
  - "[[Key_Value_Pair]]"
worksheet: [WS7] # Implied concept (Hash Table implements this)
date_created: 2025-04-21
---
# Map (ADT)

## Definition

A **Map** (also known as an **Associative Array**, **Dictionary**, or **Symbol Table**) is an [[Abstract_Data_Type|Abstract Data Type (ADT)]] representing a collection of **[[Key_Value_Pair|key-value pairs]]**, such that each possible **key** appears **at most once** in the collection. Keys are used to look up their corresponding values.

## Core Operations (Typical)

-   **`put(key, value)`** (or `insert`, `add`, `set`): Associates `value` with `key`. If `key` already exists, its associated value is typically updated to the new `value`.
-   **`get(key)`:** Retrieves the `value` associated with `key`. Returns a special value or signals an error if the key is not found.
-   **`remove(key)`:** Removes the key-value pair associated with `key` from the map if it exists.
-   **`containsKey(key)`:** Returns true if the map contains an entry for `key`, false otherwise.
-   **`size()`:** Returns the number of key-value pairs in the map.
-   **`isEmpty()`:** Returns true if the map is empty.
-   **`keys()`:** Returns a collection (often a [[Set_ADT]]) of all keys in the map.
-   **`values()`:** Returns a collection of all values in the map (may contain duplicates if different keys map to the same value).
-   **`items()`:** Returns a collection of all key-value pairs.

## Key Aspects

- **Key-Value Association:** Stores data as pairs, where each unique key maps to a specific value.
- **Unique Keys:** Keys within a map must be unique. The set of keys forms a [[Set_ADT]].
- **Lookup by Key:** The primary purpose is efficient retrieval of a value based on its associated key.
- **Unordered (Often):** Like sets, maps are often unordered by default (e.g., when implemented with hash tables), although ordered map implementations exist (e.g., using balanced trees).

## Common Implementations (Data Structures)

1.  **[[Hash_Table_DS]] (Hash Map / Dictionary):**
    -   *Pros:* Very fast `put`, `get`, `remove`, `containsKey` on average (O(1)). Most common implementation.
    -   *Cons:* Order is generally not preserved. Worst-case O(n). Requires a good [[Hash_Function]].
2.  **[[Balanced_Binary_Search_Tree_DS]] (Tree Map):** (e.g., Red-Black Tree, AVL Tree)
    -   *Pros:* Guaranteed O(log n) time for `put`, `get`, `remove`, `containsKey`. Keeps key-value pairs sorted by key, allowing ordered traversal and efficient range queries.
    -   *Cons:* Slower than hash tables on average. More complex implementation.
3.  **Association List (List of Pairs):**
    -   *Pros:* Very simple implementation (e.g., using a linked list of key-value structs).
    -   *Cons:* Very slow operations (O(n) for `put`, `get`, `remove`, `containsKey`) as it requires linear search. Only suitable for very small maps.
4.  **Direct Address Table (Array):**
    -   *Pros:* Extremely fast O(1) operations *if* keys are integers within a small, dense range suitable for direct array indexing.
    -   *Cons:* Only works for specific integer key types. Can waste huge amounts of space if the key range is large but sparse.

## Related Concepts
- [[Abstract_Data_Type]], [[Data_Structure]]
- [[Key_Value_Pair]] (The elements stored)
- [[Set_ADT]] (The collection of keys forms a set)
- [[Hash_Table_DS]], [[Balanced_Binary_Search_Tree_DS]] (Common implementations)
- Python `dict`, Java `HashMap`/`TreeMap`, C++ `std::unordered_map`/`std::map`

---
**Source:** Worksheet WS7 (Implied)