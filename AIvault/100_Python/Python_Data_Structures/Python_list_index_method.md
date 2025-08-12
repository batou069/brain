---
tags:
  - python
  - list
  - method
  - index
  - search
  - sequence
  - data_structures
  - function
aliases:
  - list.index()
  - find index in list
related:
  - "[[Python_List]]"
  - "[[Python_List_Methods]]"
  - "[[Python_list_count]]"
  - "[[Python_Operators#Membership Operators (in, not in)|Membership Operators (in, not in)]]"
worksheet:
  - WS17
date_created: 2025-06-11
---
# Python: `list.index(item, start=0, end=len(list))`

The `index()` method is used to find the **zero-based index** in a [[Python_List|list]] of the **first occurrence** of a specified `item`.

If the `item` is not found in the list, this method raises a `ValueError`.

## Syntax```python
list_object.index(item, start, end)
```
-   `item`: The element whose index is to be found.
-   `start` (optional): The starting index from where the search begins. Defaults to 0 (the beginning of the list).
-   `end` (optional): The ending index where the search stops (exclusive). Defaults to the length of the list.

## Behavior
-   Searches for the `item` within the specified slice of the list (from `start` to `end-1`).
-   Returns the index of the *first* match found.
-   If the `item` appears multiple times, only the index of its first appearance (within the search range) is returned.
-   If the `item` is not found, a `ValueError` exception is raised.

## Return Value
-   An integer representing the index of the first occurrence of `item`.

## Examples

**1. Basic usage:**
```python
product_tags = ["new", "sale", "electronics", "featured", "sale"]
print(f"Tags: {product_tags}")

index_of_sale = product_tags.index("sale")
print(f"Index of first 'sale': {index_of_sale}") # Output: 1

index_of_electronics = product_tags.index("electronics")
print(f"Index of 'electronics': {index_of_electronics}") # Output: 2
```

**2. Using `start` and `end` parameters:**
```python
# Find the index of "sale" starting after the first occurrence
index_of_second_sale = product_tags.index("sale", index_of_sale + 1)
print(f"Index of second 'sale' (searching from index {index_of_sale + 1}): {index_of_second_sale}") # Output: 4

# Search within a specific slice
numbers = [10, 20, 30, 40, 30, 50, 30]
# Search for 30 between index 3 (inclusive) and 5 (exclusive)
index_of_30_in_slice = numbers.index(30, 3, 5) # Searches in numbers[3:5] which is [40, 30]
print(f"Index of 30 in numbers[3:5]: {index_of_30_in_slice}") # Output: 4 (index in the original list)
```

**3. Handling `ValueError` if item is not found:**
It's often good practice to check for an item's existence using the `in` operator before calling `index()` to avoid `ValueError`, or to use a `try-except` block.

```python
inventory_ids = ["A101", "B202", "C303"]

item_to_find = "D404"
if item_to_find in inventory_ids:
    idx = inventory_ids.index(item_to_find)
    print(f"'{item_to_find}' found at index: {idx}")
else:
    print(f"'{item_to_find}' not found in the list.")

# Using try-except
item_to_find_alt = "A101"
try:
    idx_alt = inventory_ids.index(item_to_find_alt)
    print(f"'{item_to_find_alt}' found at index: {idx_alt} (using try-except)")
except ValueError:
    print(f"'{item_to_find_alt}' not found (using try-except).")
```
Output:
```
'D404' not found in the list.
'A101' found at index: 0 (using try-except)
```

## Performance
The time complexity of `list.index()` is $O(N)$ in the worst case, where $N$ is the number of elements in the list (or the slice being searched), because it may have to scan through all elements to find the item or determine it's not present.

If you need to perform many lookups, and the order doesn't matter or duplicates are not allowed, converting the list to a `set` can provide much faster average $O(1)$ membership testing (though sets don't store indices). If you need to find all indices of an item, you would typically loop or use a list comprehension with `enumerate`.

`index()` is useful when you need to find the position of the first occurrence of a specific element in a list.

---