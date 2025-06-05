---
tags:
  - data_structures
  - concept
  - core
  - design
  - abstraction
aliases:
  - ADT
related:
  - "[[Data_Structure]]"
  - "[[Interface_C]]"
  - "[[Encapsulation_C]]"
  - "[[Abstraction_C]]"
  - "[[List_ADT]]"
  - "[[Stack_ADT]]"
  - "[[Queue_ADT]]"
  - "[[Set_ADT]]"
  - "[[Map_ADT]]"
worksheet:
  - WS7
date_created: 2025-04-12
---
# Abstract Data Type (ADT)

## Definition

An **Abstract Data Type (ADT)** is a mathematical model for data types defined by its **behavior** (semantics) from the point of view of a user. It specifies a set of possible values, a set of operations on those values, and the behavior of those operations, **without** specifying the concrete [[Data_Structure|data structure]] used to implement it or the algorithms used for the operations. An ADT defines the *what* (interface), not the *how* (implementation).

## Key Aspects / Characteristics

- **Abstraction:** Hides the internal implementation details from the user. Users interact with the data solely through the defined operations (the interface).
- **Encapsulation:** Bundles data (values) and operations together. The internal representation of the data is hidden.
- **Interface Definition:** Specifies:
    - The type of data being stored.
    - The set of operations that can be performed (e.g., `create`, `insert`, `delete`, `search`, `get_size`).
    - The parameters and return types for each operation.
    - The semantic meaning of each operation (what it does, preconditions, postconditions).
- **Implementation Independence:** An ADT can be implemented using various different concrete [[Data_Structure|data structures]]. The choice of implementation affects performance but not the logical behavior defined by the ADT.
- **Focus on Behavior:** Defines *what* operations are available and *what* they do, not *how* they are implemented.

## Examples

- **List ADT:**
    - *Values:* A sequence of items.
    - *Operations:* `add(item)`, `remove(index)`, `get(index)`, `set(index, item)`, `size()`, `isEmpty()`.
    - *Possible Implementations:* [[Array_C]] (static), [[Vector_DS]] (dynamic array), [[Singly_Linked_List_DS]], [[Doubly_Linked_List_DS]].
- **Stack ADT:**
    - *Values:* A collection of items with LIFO (Last-In, First-Out) access.
    - *Operations:* `push(item)`, `pop()`, `peek()` (or `top()`), `size()`, `isEmpty()`.
    - *Possible Implementations:* Array, Linked List.
- **Queue ADT:**
    - *Values:* A collection of items with FIFO (First-In, First-Out) access.
    - *Operations:* `enqueue(item)`, `dequeue()`, `front()`, `size()`, `isEmpty()`.
    - *Possible Implementations:* Array (often circular), Linked List.
- **Set ADT:**
    - *Values:* An unordered collection of unique items.
    - *Operations:* `add(item)`, `remove(item)`, `contains(item)`, `size()`, `union(otherSet)`, `intersection(otherSet)`.
    - *Possible Implementations:* Hash Table, Balanced Binary Search Tree.

## Related Concepts
- [[Data_Structure]] (The concrete implementation of an ADT)
- [[Interface_C]] (ADTs define interfaces)
- [[Abstraction_C]], [[Encapsulation_C]] (Key principles embodied by ADTs)
- Information Hiding

## Questions / Further Study
>[!question] What is the difference between a data structure and an ADT? (WS7)
> See [[Data_Structure]]. ADT is the logical/behavioral definition (the "what"), while Data Structure is the concrete implementation (the "how").

---
**Source:** Worksheet WS7, Wikipedia: Abstract data type