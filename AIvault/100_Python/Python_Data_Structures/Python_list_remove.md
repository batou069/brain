---
tags:
  - python
  - list
  - method
  - remove
  - mutable
  - sequence
  - data_structures
  - function
aliases:
  - list.remove()
related:
  - "[[Python_List]]"
  - "[[Python_List_Methods]]"
  - "[[Python_list_pop]]"
  - "[[Python_Data_Structures_MOC#Deleting Elements from Data Structures|Deleting Elements]]"
worksheet:
  - WS17
date_created: 2025-06-11
---
# Python: `list.remove(item)`

The `remove()` method is used to remove the **first occurrence** of a specified `item` from a [[Python_List|list]]. This method modifies the original list in-place (it is a mutating operation) and does not return any value (it returns `None`).

## Syntax```python
list_object.remove(item)
```
-   `item`: The element to be removed from the list.

## Behavior
-   Searches for the `item` in the list from the beginning.
-   If `item` is found, its first occurrence is removed from the list.
-   Elements that were after the removed item are shifted to the left to fill the gap.
-   The list's length decreases by one if the item is found and removed.
-   If the `item` is not found in the list, a `ValueError` exception is raised.
-   The original list is modified.

## Return Value
-   `None`. The method modifies the list in-place.

## Examples

**1. Removing an item from a list of product categories:**
```python
available_categories = ["Electronics", "Books", "Apparel", "Home Goods", "Electronics"]
print(f"Initial categories: {available_categories}")

# Remove the first occurrence of "Electronics"
available_categories.remove("Electronics")
print(f"After removing 'Electronics': {available_categories}")
# Output: ['Books', 'Apparel', 'Home Goods', 'Electronics']

# Remove "Apparel"
available_categories.remove("Apparel")
print(f"After removing 'Apparel': {available_categories}")
# Output: ['Books', 'Home Goods', 'Electronics']
```

**2. Attempting to remove an item not in the list:**
```python
inventory = ["Laptop", "Mouse", "Keyboard"]
print(f"Initial inventory: {inventory}")

try:
    inventory.remove("Monitor") # "Monitor" is not in the list
except ValueError as e:
    print(f"Error removing 'Monitor': {e}")

print(f"Inventory after attempting to remove 'Monitor': {inventory}")```
Output:
```
Initial inventory: ['Laptop', 'Mouse', 'Keyboard']
Error removing 'Monitor': list.remove(x): x not in list
Inventory after attempting to remove 'Monitor': ['Laptop', 'Mouse', 'Keyboard']
```

**3. Removing items in a loop (requires caution):**
If you try to remove items from a list while iterating over it using a standard `for` loop, you can run into issues because the list size and indices change. It's often safer to iterate over a copy or build a new list.

```python
# Example of a potentially problematic way (modifying list during iteration)
# For demonstration only, usually better to use list comprehension or filter
data_points =
value_to_remove = 5
print(f"Original data points: {data_points}")

# This approach might miss some occurrences if not careful
# It's better to use a while loop or list comprehension for this pattern
# for item in data_points[:]: # Iterating over a shallow copy
#     if item == value_to_remove:
#         data_points.remove(item) 
# This loop structure is safer if you must use remove in a loop.

# A more robust way to remove all occurrences:
# Using a while loop
while value_to_remove in data_points:
    data_points.remove(value_to_remove)
print(f"Data points after removing all {value_to_remove} (using while): {data_points}")

# Using list comprehension (creates a new list)
data_points_lc =
filtered_data = [x for x in data_points_lc if x != value_to_remove]
print(f"Filtered data (using list comprehension): {filtered_data}")
```
Output for the `while` loop part:
```
Original data points:
Data points after removing all 5 (using while):
Filtered data (using list comprehension):
```

## `remove()` vs. `pop()` vs. `del`
-   **`remove(item)`:** Removes the first occurrence of a specific *value*.
-   **[[Python_list_pop|`pop(index)`]]:** Removes an item at a specific *index* and returns it.
-   **`del list_object[index]` or `del list_object[slice]`:** Removes an item or slice by *index/slice*.

`remove()` is useful when you know the value of the item you want to delete but not necessarily its position. If the item might not exist, it's good practice to check for its presence first using `in` or handle the `ValueError`.

---