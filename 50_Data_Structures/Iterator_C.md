---
tags:
  - c
  - concept
  - design_pattern
  - data_structures
  - list
  - iteration
aliases:
  - C Iterator
related:
  - Data_Structure
  - Linked_List_ADT
  - Singly_Linked_List_DS
  - Doubly_Linked_List_DS
  - Vector_DS
  - Iterator_Invalidation
  - Sequential_Access
worksheet:
  - WS9
date_created: 2025-04-14
---
# Iterator (C Context)

## Definition

In C programming (which lacks built-in iterator support like C++ or Java), an **Iterator** is a design pattern or convention used to traverse the elements of a container [[Data_Structure]] (like a [[Linked_List_ADT|linked list]], [[Vector_DS|vector]], etc.) sequentially without exposing the underlying representation of the container. It typically involves an object or `struct` that keeps track of the current position within the container and provides operations to get the current element and advance to the next one.

## Key Aspects / Characteristics (Conceptual C Implementation)

- **Abstraction:** Hides the internal structure of the container (array indices, node pointers).
- **Sequential Access:** Provides a standard way to step through elements one by one.
- **State:** The iterator object maintains the current state (e.g., a pointer to the current node in a linked list, an index in an array).
- **Common Operations:**
    - `iterator_create(container)`: Creates an iterator for a given container, usually positioned before the first element.
    - `iterator_has_next(iterator)`: Checks if there are more elements to visit.
    - `iterator_next(iterator)`: Advances the iterator to the next element and often returns the element it *was* pointing to, or the *new* current element.
    - `iterator_get_data(iterator)`: Returns the data element at the current iterator position.
    - `iterator_destroy(iterator)`: Frees resources associated with the iterator (if any).
- **Implementation:** The iterator structure and functions depend heavily on the underlying container:
    - *Linked List:* Iterator struct might hold a `Node *current_node`. `next()` advances the pointer.
    - *Vector/Array:* Iterator struct might hold an index `int current_index`. `next()` increments the index.

## Conceptual C Example (for Singly Linked List)

```c
#include <stdbool.h> // For bool type

// Assume Node and LinkedList structs are defined as in Singly_Linked_List_DS.md

// Iterator structure for a LinkedList
typedef struct {
    Node *current; // Points to the node *whose data will be returned by next()*
                   // Or points to the node *before* the next one to return
                   // Design choice! Let's say it points to the current node.
} ListIterator;

// Create iterator (points to head)
ListIterator list_iterator_create(LinkedList *list) {
    ListIterator it;
    it.current = (list != NULL) ? list->head : NULL;
    return it;
}

// Check if there's a current element (iterator is not NULL)
bool list_iterator_is_valid(ListIterator *it) {
    return (it != NULL && it->current != NULL);
}

// Get data from the current node
DataType list_iterator_get_data(ListIterator *it) {
    // Add error handling for invalid iterator (it == NULL or it->current == NULL)
    return it->current->data;
}

// Advance iterator to the next node
void list_iterator_next(ListIterator *it) {
    if (list_iterator_is_valid(it)) {
        it->current = it->current->next;
    }
}

// --- Usage ---
/*
LinkedList my_list;
// ... populate list ...

ListIterator iter = list_iterator_create(&my_list);
while (list_iterator_is_valid(&iter)) {
    DataType data = list_iterator_get_data(&iter);
    // ... process data ...
    list_iterator_next(&iter);
}
*/
```

## Related Concepts
- [[Data_Structure]], [[Linked_List_ADT]], [[Vector_DS]] (Containers being iterated over)
- [[Sequential_Access]] (The access pattern provided)
- [[Iterator_Invalidation]] (A common problem with iterators)
- Design Patterns
- C++ Iterators, Java Iterator interface (More formalized language features)

---
**Source:** Worksheet WS9