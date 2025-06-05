---
tags:
  - data_structures
  - concept
  - adt
  - linear
aliases:
  - List ADT
  - Abstract List
related:
  - "[[Abstract_Data_Type]]"
  - "[[Data_Structure]]"
  - "[[Array_C]]"
  - "[[Vector_DS]]"
  - "[[Linked_List_ADT]]"
  - "[[Singly_Linked_List_DS]]"
  - "[[Doubly_Linked_List_DS]]"
  - "[[Sequence_Container]]" # General category
worksheet: [WS7] # Implied concept
date_created: 2025-04-21
---
# List (ADT)

## Definition

A **List** is a fundamental [[Abstract_Data_Type|Abstract Data Type (ADT)]] representing a finite, **ordered sequence** of elements (items), where the same element may occur more than once. It defines operations for accessing elements by their position (index), adding elements, removing elements, and querying the list's size.

## Core Operations (Typical)

-   **`add(index, item)`:** Inserts `item` at the specified `index`, shifting subsequent elements.
-   **`remove(index)`:** Removes the item at the specified `index`, shifting subsequent elements.
-   **`get(index)`:** Returns the item at the specified `index`.
-   **`set(index, item)`:** Replaces the item at the specified `index` with `item`.
-   **`append(item)`:** Adds `item` to the end of the list (equivalent to `add(size(), item)`).
-   **`prepend(item)`:** Adds `item` to the beginning of the list (equivalent to `add(0, item)`).
-   **`search(item)`:** Finds the index of the first occurrence of `item` (returns special value like -1 if not found).
-   **`size()`:** Returns the number of items in the list.
-   **`isEmpty()`:** Returns true if the list is empty.
-   **`create()`:** Creates an empty list.

## Key Aspects

- **Ordered Sequence:** Elements have a defined position (index), starting from 0.
- **Allows Duplicates:** The same value can appear multiple times in the list.
- **Abstract:** Defines *what* operations can be done, not *how* the list is stored or how operations are implemented.

## Common Implementations (Data Structures)

The List ADT can be implemented using various concrete [[Data_Structure|data structures]], leading to different performance characteristics:

1.  **[[Array_C]] (Static Array):**
    -   *Pros:* Fast `get`/`set` by index (O(1)). Space efficient if size is known and fixed.
    -   *Cons:* Fixed size. Slow `add`/`remove` in the middle (O(n) due to shifting).
2.  **[[Vector_DS]] (Dynamic Array):**
    -   *Pros:* Fast `get`/`set` by index (O(1) average). Fast `append` (O(1) amortized). Flexible size.
    -   *Cons:* Slow `add`/`remove` at beginning/middle (O(n) due to shifting). Resizing incurs occasional overhead. Wasted space due to capacity > size.
3.  **[[Singly_Linked_List_DS]]:**
    -   *Pros:* Fast `add`/`remove` at the beginning (O(1)). Flexible size. Memory allocated per element.
    -   *Cons:* Slow `get`/`set`/`search` by index (O(n) traversal). Slow `append`/`remove` at the end (O(n)) unless tail pointer maintained. Higher memory overhead per element (for pointer).
4.  **[[Doubly_Linked_List_DS]]:**
    -   *Pros:* Fast `add`/`remove` at both beginning and end (O(1)) if head/tail pointers maintained. Fast `add`/`remove` at a known node position (O(1)). Flexible size.
    -   *Cons:* Slow `get`/`set`/`search` by index (O(n) traversal, but can start from closest end). Even higher memory overhead per element (two pointers).

## Related Concepts
- [[Abstract_Data_Type]], [[Data_Structure]]
- [[Array_C]], [[Vector_DS]], [[Linked_List_ADT]] (Implementations)
- [[Stack_ADT]], [[Queue_ADT]] (More restricted linear ADTs)
- [[Sequence_Container]] (General term for ordered collections)

---
**Source:** Worksheet WS7 (Implied)