---
tags:
  - python
  - list
  - method
  - reverse
  - mutable
  - sequence
  - data_structures
  - function
aliases:
  - list.reverse()
  - reversing a list
related:
  - "[[Python_List]]"
  - "[[Python_List_Methods]]"
  - "[[Python_Slicing]]"
  - "[[Built_In_Functions_Python#reversed()|reversed() built-in function]]"
worksheet:
  - WS17
date_created: 2025-06-11
---
# Python: `list.reverse()`

The `reverse()` method is used to reverse the order of elements in a [[Python_List|list]] **in-place**. This means the original list is modified, and the method does not return any value (it returns `None`).

## Syntax```python
list_object.reverse()
```
This method takes no arguments.

## Behavior
-   The elements of `list_object` are rearranged so that their order is reversed.
-   The first element becomes the last, the second becomes the second to last, and so on.
-   The original list is mutated directly.

## Return Value
-   `None`. The method modifies the list in-place.

## Examples

**1. Reversing a list of product processing steps:**
```python
processing_steps = ["Receive Order", "Pick Items", "Pack Items", "Ship Order", "Deliver"]
print(f"Original processing steps: {processing_steps}")

processing_steps.reverse()
print(f"Reversed processing steps: {processing_steps}")
```
Output:
```
Original processing steps: ['Receive Order', 'Pick Items', 'Pack Items', 'Ship Order', 'Deliver']
Reversed processing steps: ['Deliver', 'Ship Order', 'Pack Items', 'Pick Items', 'Receive Order']
```

**2. Reversing a list of numbers:**
```python
ratings =
print(f"Original ratings: {ratings}")

ratings.reverse()
print(f"Reversed ratings: {ratings}")
```
Output:
```
Original ratings:
Reversed ratings:
```

**3. Effect on other references:**
Since `reverse()` modifies the list in-place, other variables referencing the same list object will also see the change.
```python
my_list = ['a', 'b', 'c']
alias_list = my_list

my_list.reverse()

print(f"my_list after reverse: {my_list}")   # Output: ['c', 'b', 'a']
print(f"alias_list after reverse: {alias_list}") # Output: ['c', 'b', 'a']
```

## Alternatives for Reversing (that create a new list or iterator)

1.  **Slicing `[::-1]`:**
    -   This creates a **new, reversed shallow copy** of the list, leaving the original list unchanged.
    ```python
    original_items = ["apple", "banana", "cherry"]
    reversed_copy_items = original_items[::-1]

    print(f"Original items: {original_items}")         # Output: ['apple', 'banana', 'cherry']
    print(f"Reversed copy (slicing): {reversed_copy_items}") # Output: ['cherry', 'banana', 'apple']
    ```

2.  **`reversed()` built-in function:**
    -   This function returns a **reverse iterator**, not a list. To get a list, you need to convert the iterator (e.g., using `list()`).
    -   It does not modify the original list.
    ```python
    original_items = ["apple", "banana", "cherry"]
    reversed_iterator = reversed(original_items)
    
    print(f"Original items: {original_items}") # Output: ['apple', 'banana', 'cherry']
    print(f"Reversed iterator object: {reversed_iterator}") 
    
    reversed_list_from_iterator = list(reversed_iterator)
    print(f"Reversed list from iterator: {reversed_list_from_iterator}") # Output: ['cherry', 'banana', 'apple']
    ```

**Choosing between `list.reverse()`, slicing, and `reversed()`:**
-   Use `list.reverse()` when you want to modify the original list in-place and don't need to preserve the original order or create a new list object.
-   Use slicing `[::-1]` when you need a new list that is a reversed copy of the original, and the original list should remain unchanged.
-   Use the `reversed()` built-in function when you need an iterator to loop over the list in reverse order, especially for memory efficiency with large lists if you don't need the full reversed list in memory at once.

`list.reverse()` is a direct and efficient way to reverse the elements of a list when an in-place modification is desired.

---