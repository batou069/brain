---
tags:
  - data_structures
  - concept
  - adt
  - collection
aliases:
  - Set ADT
  - Abstract Set
related:
  - "[[Abstract_Data_Type]]"
  - "[[Data_Structure]]"
  - "[[List_ADT]]"
  - "[[Map_ADT]]"
  - "[[Hash_Table_DS]]"
  - "[[Balanced_Binary_Search_Tree_DS]]"
  - "[[Uniqueness]]"
  - "[[Mathematical_Set]]"
worksheet: [WS7] # Implied concept
date_created: 2025-04-21
---
# Set (ADT)

## Definition

A **Set** is an [[Abstract_Data_Type|Abstract Data Type (ADT)]] representing a collection of **unique** elements (items), where the order of elements typically does not matter. It models the mathematical concept of a finite set.

## Core Operations (Typical)

-   **`add(item)`:** Adds `item` to the set. If the item is already present, the set remains unchanged (due to uniqueness).
-   **`remove(item)`:** Removes `item` from the set if it exists.
-   **`contains(item)`** (or `isMember`, `search`): Returns true if `item` is present in the set, false otherwise.
-   **`size()`:** Returns the number of unique elements in the set.
-   **`isEmpty()`:** Returns true if the set is empty.
-   **Set-Theoretic Operations:**
    -   **`union(otherSet)`:** Returns a new set containing all elements from both sets.
    -   **`intersection(otherSet)`:** Returns a new set containing only elements present in *both* sets.
    -   **`difference(otherSet)`:** Returns a new set containing elements present in this set but *not* in `otherSet`.
    -   **`isSubset(otherSet)`:** Returns true if all elements of this set are also present in `otherSet`.

## Key Aspects

- **Uniqueness:** A set cannot contain duplicate elements. Adding an existing element has no effect.
- **Unordered (Usually):** The definition of a set doesn't imply a specific order, although some implementations might provide ordered traversal (e.g., if implemented with a balanced tree).
- **Membership Testing:** Efficiently checking if an element `contains` is a primary goal.

## Common Implementations (Data Structures)

1.  **[[Hash_Table_DS]] (Hash Set):**
    -   *Pros:* Very fast `add`, `remove`, `contains` on average (O(1)).
    -   *Cons:* Order is generally not preserved. Worst-case O(n). Requires a good [[Hash_Function]].
2.  **[[Balanced_Binary_Search_Tree_DS]] (Tree Set):** (e.g., Red-Black Tree, AVL Tree)
    -   *Pros:* Guaranteed O(log n) time for `add`, `remove`, `contains`. Keeps elements sorted, allowing ordered traversal and efficient min/max operations.
    -   *Cons:* Slower than hash tables on average. More complex implementation.
3.  **[[Bitmap_DS]] (Bitset):**
    -   *Pros:* Extremely space-efficient and fast (O(1)) operations *if* the elements are integers within a known, dense range.
    -   *Cons:* Only suitable for integer elements within a limited range. Can waste space if the range is large but sparsely populated.
4.  **Sorted Array/Vector:**
    -   *Pros:* Space efficient. `contains` is O(log n) using binary search.
    -   *Cons:* `add`/`remove` are slow (O(n)) due to shifting elements to maintain order.

## Related Concepts
- [[Abstract_Data_Type]], [[Data_Structure]]
- [[Mathematical_Set]] (The underlying concept)
- Uniqueness Constraint
- [[List_ADT]] (Contrast: ordered, allows duplicates)
- [[Map_ADT]] (Stores key-value pairs, keys form a set)
- [[Hash_Table_DS]], [[Balanced_Binary_Search_Tree_DS]], [[Bitmap_DS]] (Implementations)

---
**Source:** Worksheet WS7 (Implied)