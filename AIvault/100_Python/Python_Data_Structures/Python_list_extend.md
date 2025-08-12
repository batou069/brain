---
tags:
  - python
  - list
  - method
  - extend
  - mutable
  - sequence
  - iterable
  - data_structures
  - function
aliases:
  - list.extend()
related:
  - "[[Python_List]]"
  - "[[Python_List_Methods]]"
  - "[[Python_list_append]]"
  - "[[Python_Operators#List Concatenation (+)|List Concatenation (+)]]"
worksheet:
  - WS17
date_created: 2025-06-11
---
# Python: `list.extend(iterable)`

The `extend()` method is used to add all items from an **iterable** (e.g., another list, a tuple, a string, a set) to the **end** of an existing [[Python_List|list]]. This method modifies the original list in-place (it is a mutating operation) and does not return any value (it returns `None`).

## Syntax```python
list_object.extend(iterable)
```
-   `iterable`: An iterable object whose elements will be added to the list.

## Behavior
-   Each element from the `iterable` is added individually to the end of `list_object`.
-   The original list is modified.
-   If the `iterable` is a string, each character of the string is added as a separate element.

## Return Value
-   `None`. The method modifies the list in-place.

## Examples

**1. Extending a list with another list:**
```python
main_product_list = ["Laptop", "Mouse"]
accessories = ["Keyboard", "Webcam", "Monitor"]

print(f"Initial main list: {main_product_list}")
main_product_list.extend(accessories)
print(f"After extending with accessories: {main_product_list}")
```
Output:
```
Initial main list: ['Laptop', 'Mouse']
After extending with accessories: ['Laptop', 'Mouse', 'Keyboard', 'Webcam', 'Monitor']
```

**2. Extending a list with a tuple:**
```python
numbers_list = [1, 2, 3]
more_numbers_tuple = (4, 5, 6)

numbers_list.extend(more_numbers_tuple)
print(f"After extending with tuple: {numbers_list}")
```
Output:
```
After extending with tuple: [1, 2, 3, 4, 5, 6]
```

**3. Extending a list with a string (adds individual characters):**
```python
letters = ['a', 'b']
word = "cat"

letters.extend(word)
print(f"After extending with string 'cat': {letters}")
```
Output:
```
After extending with string 'cat': ['a', 'b', 'c', 'a', 't']
```

**4. Comparison with `append()`:**
It's crucial to understand the difference between `extend()` and [[Python_list_append|`append()`]] when the argument is an iterable:
```python
list_a = [1, 2]
list_b = [3, 4]
list_a.append(list_b) # Appends list_b as a single element (a nested list)
print(f"Using append with a list: {list_a}") # Output: [1, 2, [3, 4]]

list_c = [1, 2]
list_d = [3, 4]
list_c.extend(list_d) # Appends elements of list_d individually
print(f"Using extend with a list: {list_c}") # Output: [1, 2, 3, 4]
```

## `extend()` vs. `+` (Concatenation)
-   `extend()` modifies the original list in-place.
-   The `+` operator for lists creates a *new* list containing elements from both operands, leaving the original lists unchanged.

```python
list1 = [1, 2]
list2 = [3, 4]

# Using extend (modifies list1)
list1_copy_for_extend = list1.copy()
list1_copy_for_extend.extend(list2)
print(f"list1_copy_for_extend after extend: {list1_copy_for_extend}")
print(f"Original list1 (unchanged by copy): {list1}")

# Using + operator (creates a new list)
list3 = list1 + list2
print(f"list3 (new list from +): {list3}")
print(f"Original list1 after +: {list1}") # Unchanged
print(f"Original list2 after +: {list2}") # Unchanged
```
Generally, `extend()` can be more memory-efficient than `+` followed by assignment (e.g., `list1 = list1 + list2`) for adding multiple items, especially to large lists, as `+` involves creating a new list object.

`extend()` is the appropriate method when you want to add all elements from an iterable to an existing list, modifying that list directly.

---