---
tags:
  - python
  - list
  - method
  - insert
  - mutable
  - sequence
  - data_structures
  - function
aliases:
  - list.insert()
related:
  - "[[Python_List]]"
  - "[[Python_List_Methods]]"
  - "[[Python_list_append]]"
  - "[[Python_list_extend]]"
worksheet:
  - WS17
date_created: 2025-06-11
---
# Python: `list.insert(index, item)`

The `insert()` method is used to add a single **item** to a [[Python_List|list]] at a specified **index**. This method modifies the original list in-place (it is a mutating operation) and does not return any value (it returns `None`).

## Syntax```python
list_object.insert(index, item)
```
-   `index`: The index at which the `item` should be inserted. Elements at and after this index are shifted to the right.
    -   If `index` is 0, the item is inserted at the beginning of the list.
    -   If `index` is greater than or equal to the length of the list, the item is appended to the end (similar to `append()`).
    -   Negative indexing can be used (e.g., `-1` inserts before the last element, effectively becoming the second to last).
-   `item`: The element to be inserted into the list.

## Behavior
-   The `item` is inserted into the list at the position specified by `index`.
-   All elements originally at or after the `index` are shifted one position to the right to make space for the new item.
-   The list's length increases by one.
-   The original list is modified.

## Return Value
-   `None`. The method modifies the list in-place.

## Examples

**1. Inserting at a specific index:**
```python
product_wishlist = ["Smartwatch", "Headphones", "Tablet"]
print(f"Initial wishlist: {product_wishlist}")

# Insert "E-reader" at index 1 (second position)
product_wishlist.insert(1, "E-reader")
print(f"After inserting 'E-reader' at index 1: {product_wishlist}")
```
Output:
```
Initial wishlist: ['Smartwatch', 'Headphones', 'Tablet']
After inserting 'E-reader' at index 1: ['Smartwatch', 'E-reader', 'Headphones', 'Tablet']
```

**2. Inserting at the beginning of the list:**
```python
tasks = ["Write report", "Send email"]
print(f"Initial tasks: {tasks}")

tasks.insert(0, "Attend meeting") # Insert at the beginning
print(f"After inserting at index 0: {tasks}")
```
Output:
```
Initial tasks: ['Write report', 'Send email']
After inserting at index 0: ['Attend meeting', 'Write report', 'Send email']
```

**3. Inserting at an index beyond the current length (appends):**
```python
numbers =
print(f"Initial numbers: {numbers}")

numbers.insert(10, 40) # Index 10 is out of bounds, so it appends
print(f"After inserting at index 10: {numbers}") # Same as numbers.append(40)
```
Output:
```
Initial numbers:
After inserting at index 10:
```

**4. Inserting using negative indexing:**
```python
items = ['a', 'b', 'c', 'd']
print(f"Initial items: {items}")

items.insert(-1, 'X') # Inserts 'X' before the last element 'd'
print(f"After inserting 'X' at index -1: {items}")
```
Output:
```
Initial items: ['a', 'b', 'c', 'd']
After inserting 'X' at index -1: ['a', 'b', 'c', 'X', 'd']
```

## Performance Considerations
Inserting elements into a list (especially near the beginning or in the middle) can be relatively slow for large lists. This is because all subsequent elements need to be shifted to make space. The time complexity for `insert()` is generally $O(N)$, where $N$ is the number of elements in the list. Appending to the end (`append()`) is typically faster, with an amortized $O(1)$ complexity.

If you need to perform many insertions and deletions from both ends of a sequence, `collections.deque` might be a more efficient data structure.

`insert()` is useful when you need to add an element at a specific position within a list, maintaining the order of other elements.

---