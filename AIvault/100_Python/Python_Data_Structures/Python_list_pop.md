---
tags:
  - python
  - list
  - method
  - pop
  - remove
  - mutable
  - sequence
  - data_structures
  - function
aliases:
  - list.pop()
related:
  - "[[Python_List]]"
  - "[[Python_List_Methods]]"
  - "[[Python_list_remove]]"
  - "[[Python_list_clear]]"
  - "[[Python_Data_Structures_MOC#Stacks (using lists)|Stacks (using lists)]]"
worksheet:
  - WS17
date_created: 2025-06-11
---
# Python: `list.pop(index=-1)`

The `pop()` method is used to remove and **return** an item from a [[Python_List|list]] at a specified `index`. If no index is specified, `pop()` removes and returns the **last item** in the list. This method modifies the original list in-place (it is a mutating operation).

## Syntax```python
list_object.pop(index)
```
-   `index` (optional): The zero-based index of the item to remove and return.
    -   If `index` is not provided or is `-1`, the last item is removed and returned (Last-In, First-Out behavior, useful for implementing stacks).
    -   If the specified `index` is out of range (e.g., greater than or equal to the list length, or too small for negative indexing), an `IndexError` is raised.
    -   If the list is empty and `pop()` is called (with or without an index), an `IndexError` is raised.

## Behavior
-   The item at the specified `index` is removed from the list.
-   Elements after the popped item (if any) are shifted to the left.
-   The list's length decreases by one.
-   The original list is modified.

## Return Value
-   The item that was removed from the list.

## Examples

**1. Popping the last item (default behavior):**
```python
pending_tasks = ["Process Orders", "Update Inventory", "Send Newsletter"]
print(f"Initial tasks: {pending_tasks}")

last_task = pending_tasks.pop()
print(f"Popped task: '{last_task}'") # Output: 'Send Newsletter'
print(f"Remaining tasks: {pending_tasks}") # Output: ['Process Orders', 'Update Inventory']

next_to_last_task = pending_tasks.pop()
print(f"Popped task: '{next_to_last_task}'") # Output: 'Update Inventory'
print(f"Remaining tasks: {pending_tasks}") # Output: ['Process Orders']
```

**2. Popping an item at a specific index:**```python
product_queue = ["P101", "P203", "P305", "P407"] # Product IDs in a processing queue
print(f"Initial product queue: {product_queue}")

# Process the item at the front of the queue (index 0)
processed_product = product_queue.pop(0)
print(f"Processed product: '{processed_product}'") # Output: 'P101'
print(f"Remaining queue: {product_queue}") # Output: ['P203', 'P305', 'P407']

# Process item at index 1 (which is now "P305")
another_processed = product_queue.pop(1)
print(f"Processed product: '{another_processed}'") # Output: 'P305'
print(f"Remaining queue: {product_queue}") # Output: ['P203', 'P407']
```

**3. Using negative indexing:**
`pop(-1)` is equivalent to `pop()`. `pop(-2)` removes the second to last item.
```python
items = ['a', 'b', 'c', 'd', 'e']
second_last = items.pop(-2) # Removes 'd'
print(f"Removed second last: '{second_last}'") # Output: 'd'
print(f"List after pop(-2): {items}") # Output: ['a', 'b', 'c', 'e']
```

**4. Handling `IndexError`:**
```python
empty_list = []
try:
    empty_list.pop()
except IndexError as e:
    print(f"Error popping from empty list: {e}")

non_empty_list = ['item1']
try:
    non_empty_list.pop(5) # Index out of range
except IndexError as e:
    print(f"Error popping with out-of-range index: {e}")
```
Output:
```
Error popping from empty list: pop from empty list
Error popping with out-of-range index: pop index out of range
```

## Performance
-   `pop()` (from the end): Amortized $O(1)$ time complexity.
-   `pop(0)` (from the beginning) or `pop(i)` (from the middle): $O(N)$ time complexity, where $N$ is the number of elements, because subsequent elements need to be shifted.

If you need efficient appends and pops from both ends, consider using `collections.deque`.

## Use Cases
-   **Implementing Stacks (LIFO):** Use `append()` to push onto the stack and `pop()` to pop from the stack.
-   **Processing Queues (FIFO, less efficient with list `pop(0)`):** Use `append()` to enqueue and `pop(0)` to dequeue. (Again, `collections.deque` is better for queues).
-   Iteratively processing and removing items from a list.

`pop()` is a versatile method for removing items from a list by their position while also retrieving the removed item.

---