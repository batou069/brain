---
tags:
  - c
  - concept
  - technique
  - data_structures
  - linked_list
aliases:
  - Sentinel Node
  - Header Node (Linked List)
related:
  - Linked_List_ADT
  - Singly_Linked_List_DS
  - Doubly_Linked_List_DS
  - Circular_Linked_List_DS
  - Edge_Cases
worksheet:
  - WS9
date_created: 2025-04-14
---
# Dummy Node (Linked List)

## Definition

A **Dummy Node** (also known as a **Sentinel Node** or sometimes a **Header Node**) is a special, non-data-carrying node added to the beginning (and sometimes the end) of a [[Linked_List_ADT|linked list]]. Its purpose is to simplify the logic for insertion and deletion operations by eliminating the need for special case handling for operations at the very beginning (or end) of the list.

## Key Aspects / Characteristics

- **Simplifies Edge Cases:** Operations like inserting before the first element or deleting the first element often require special handling of the `head` pointer in a standard linked list implementation. A dummy head node ensures that *every* actual data node always has a node preceding it, making insertion/deletion logic uniform.
- **Always Present:** The dummy node exists even when the list is logically empty. An empty list consists *only* of the dummy node(s).
- **No Data:** The dummy node's data field is typically ignored or unused.
- **Implementation:**
    - **Dummy Head:** A dummy node is placed before the first actual data node. The list's `head` pointer always points to this dummy node. The first *data* node is `head->next`. An empty list is indicated by `head->next == NULL`.
    - **Dummy Head and Tail (Doubly Linked):** Sometimes used in [[Doubly_Linked_List_DS|doubly linked lists]], where dummy head and tail nodes point to each other when the list is empty, further simplifying insertion/deletion at both ends.
- **Trade-off:** Adds a small, constant memory overhead (one or two extra nodes) but can significantly simplify the implementation code for list operations, reducing potential bugs in edge case handling.

## Visualization (Singly Linked List with Dummy Head)

**Empty List:**
```mermaid
graph LR
    Head --> Dummy[Dummy, next];
    Dummy -- ptr --> Null[NULL];

    style Head fill:#fff,stroke:#f00,stroke-width:2px
```

**List with Nodes A, B:**
```mermaid
graph LR
    Head --> Dummy[Dummy, next];
    Dummy -- ptr --> NodeA[Data: A, next];
    NodeA -- ptr --> NodeB[Data: B, next];
    NodeB -- ptr --> Null[NULL];

    style Head fill:#fff,stroke:#f00,stroke-width:2px
```

**Insertion at Beginning (Node X):**
1. Find node *before* insertion point (always the Dummy node).
2. `newNode->next = dummy->next;`
3. `dummy->next = newNode;`
*(No special check needed if list was empty or not)*

**Deletion of First Element (Node A):**
1. Find node *before* deletion point (always the Dummy node).
2. `nodeToDelete = dummy->next;`
3. `dummy->next = nodeToDelete->next;` (or `dummy->next = dummy->next->next;`)
4. `free(nodeToDelete);`
*(No special check needed to update the main list head pointer)*

## Related Concepts
- [[Linked_List_ADT]], [[Singly_Linked_List_DS]], [[Doubly_Linked_List_DS]], [[Circular_Linked_List_DS]]
- [[Node_DS]]
- Edge Cases (Dummy nodes help eliminate these)
- Implementation Complexity

---
**Source:** Worksheet WS9