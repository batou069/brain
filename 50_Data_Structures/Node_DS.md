---
tags:
  - data_structures
  - concept
  - building_block
  - linked_list
  - tree
  - graph
aliases:
  - Node (Data Structure)
related:
  - "[[Data_Structure]]"
  - "[[Linked_List_ADT]]"
  - "[[Tree_DS]]"
  - "[[Graph_DS]]"
  - "[[Pointer_C]]"
  - "[[struct_C]]"
  - "[[Dynamic_Allocation_C]]"
worksheet: [WS9] # Implied concept
date_created: 2025-04-21
---
# Node (Data Structure Component)

## Definition

In the context of various [[Data_Structure|data structures]] like [[Linked_List_ADT|linked lists]], [[Tree_DS|trees]], and [[Graph_DS|graphs]], a **Node** is the fundamental building block or element. A node typically contains two types of information:

1.  **Data:** The actual value or payload stored at that position in the structure.
2.  **Link(s):** One or more pointers or references connecting the node to other nodes within the data structure, defining its relationship to them (e.g., next, previous, child, parent).

## Key Aspects / Characteristics

- **Building Block:** Nodes are combined via their links to form the overall structure.
- **Data Storage:** Holds the information the data structure is intended to organize. The data part can be simple (like an integer) or complex (like a [[struct_C]]).
- **Links/Pointers:** Define the structure's topology by connecting nodes. The number and type of links depend on the specific data structure:
    - [[Singly_Linked_List_DS]]: One `next` pointer.
    - [[Doubly_Linked_List_DS]]: `next` and `prev` pointers.
    - Binary [[Tree_DS]]: `left_child` and `right_child` pointers (and sometimes `parent`).
    - [[Graph_DS]]: Nodes (vertices) might store a list of adjacent nodes/edges.
- **Dynamic Allocation:** Nodes for dynamic structures like linked lists and trees are typically allocated individually on the [[Heap_Memory_C]] using [[Dynamic_Allocation_C]] ([[malloc]]).
- **Implementation:** Often implemented in C using a `struct`. In Python, typically implemented using a `class`.

## Conceptual C Implementations

**Linked List Node:**
```c
typedef struct LinkedListNode {
    int data; // Example data type
    struct LinkedListNode *next;
} Node;
```

**Binary Tree Node:**
```c
typedef struct TreeNode {
    char *key; // Example data type
    struct TreeNode *left;
    struct TreeNode *right;
    // struct TreeNode *parent; // Optional parent pointer
} TreeNode;
```

## Conceptual Python Implementations

**Linked List Node:**
```python
class ListNode:
    def __init__(self, data: int, next_node=None) -> None:
        self.data = data  # Example data: integer
        self.next = next_node  # Reference to next node or None
```

**Binary Tree Node:**
```python
from typing import Optional

class TreeNode:
    def __init__(self, key: str, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None) -> None:
        self.key = key  # Example data: string
        self.left = left  # Left child or None
        self.right = right  # Right child or None
        # self.parent = None  # Optional parent reference
```

## Related Concepts
- [[Data_Structure]] (Nodes are components)
- [[Linked_List_ADT]], [[Tree_DS]], [[Graph_DS]] (Structures built from nodes)
- [[Pointer_C]] (Used for links)
- [[struct_C]] (Common way to implement nodes)
- [[Dynamic_Allocation_C]] (Used to create nodes)

---
**Source:** Worksheet WS9 (Implied)