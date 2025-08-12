---
tags:
  - python
  - data_structures
  - list
  - methods
  - functions
  - concept
  - summary
aliases:
  - List Methods Python
  - Python List Functions
related:
  - "[[Python_List]]"
  - "[[100_Python/Python_Data_Structures/_Python_Data_Structures_MOC|_Python_Data_Structures_MOC]]"
  - "[[Python_list_append]]"
  - "[[Python_list_extend]]"
  - "[[Python_list_insert]]"
  - "[[Python_list_remove]]"
  - "[[Python_list_pop]]"
  - "[[Python_list_clear]]"
  - "[[Python_list_index]]"
  - "[[Python_list_count]]"
  - "[[Python_list_sort]]"
  - "[[Python_list_reverse]]"
  - "[[Python_list_copy]]"
  - "[[Built_In_Functions_Python#len()|len() for lists]]"
  - "[[Built_In_Functions_Python#max()|max() for lists]]"
  - "[[Built_In_Functions_Python#min()|min() for lists]]"
worksheet:
  - WS17
date_created: 2025-06-11
---
# Python: List Methods Summary

Python [[Python_List|lists]] are mutable sequences and come with a rich set of built-in methods to manipulate their content. This note summarizes the most common list methods. Many of these methods modify the list **in-place**.

## Modifying List Content (Adding/Removing Elements)
[list2mdtable|#List Modifying Methods]
- Method
    - Description
        - Mutates Original?
	        - Example
- `append(item)`
    -   Adds `item` to the **end** of the list.
	    -   Yes
	        -   `my_list.append(5)`
- `extend(iterable)`
    -   Appends all items from `iterable` (e.g., another list, tuple, string) to the end of the list.
	    -   Yes
	        -   `my_list.extend()`
- `insert(index, item)`
    -   Inserts `item` at the specified `index`, shifting subsequent elements.
	    -   Yes
	        -   `my_list.insert(1, 'new')`
- `remove(item)`
    -   Removes the **first** occurrence of `item` from the list. Raises `ValueError` if `item` is not found.
	    -   Yes
	        -   `my_list.remove('new')`
- `pop(index=-1)`
    -   Removes and **returns** the item at the given `index`. If `index` is not specified, it removes and returns the last item. Raises `IndexError` if list is empty or index is out of range.
	    -   Yes
	        -   `last_val = my_list.pop()`
	        -   `val_at_idx = my_list.pop(0)`
- `clear()`
    -   Removes all items from the list, making it empty.
	    -   Yes
	        -   `my_list.clear()`
- `del list[index]` / `del list[slice]`
    -   The `del` statement (not a method) removes an item by index or a slice of items.
	    -   Yes
	        -   `del my_list`
	        -   `del my_list[1:3]`

## Accessing and Searching
[list2mdtable|#List Access/Search Methods]
- Method
    - Description
        - Mutates Original?
	        - Example
- `index(item, start=0, end=len(list))`
    -   Returns the zero-based index of the first occurrence of `item`. Raises `ValueError` if `item` is not found. `start` and `end` can specify a sub-section to search.
	    -   No
	        -   `idx = my_list.index(5)`
- `count(item)`
    -   Returns the number of times `item` appears in the list.
	    -   No
	        -   `num_fives = my_list.count(5)`

## Ordering and Copying
[list2table|#List Ordering/Copying Methods]
- Method
    - Description
        - Mutates Original?
	        - Example
- `sort(key=None, reverse=False)`
    -   Sorts the items of the list **in-place**<br>-   `key`: A function to extract a comparison key from each list element.<br>-   `reverse`: If `True`, sorts in descending order.
	    -   Yes
	        -   `my_list.sort()`
	        -   `my_list.sort(reverse=True)`
	        -   `my_list.sort(key=len)`
- `reverse()`
    -   Reverses the elements of the list **in-place**.
	    -   Yes
	        -   `my_list.reverse()`
- `copy()`
    -   Returns a **shallow copy** of the list. The new list is a new object, but if the list contains mutable objects (like other lists), the copies of those nested objects are references to the original nested objects.
	    -   No
	        -   `new_list = my_list.copy()`
	        -   Also `new_list = my_list[:]` (slicing)

## Built-in Functions often used with Lists
These are not methods (called as `func(list)`) but are commonly used:
-   **[[Built_In_Functions_Python#len()|`len(list)`]]:** Returns the number of items in the list.
-   **[[Built_In_Functions_Python#max()|`max(list)`]]:** Returns the largest item in the list (items must be comparable).
-   **[[Built_In_Functions_Python#min()|`min(list)`]]:** Returns the smallest item in the list (items must be comparable).
-   **`sum(list, start=0)`:** Returns the sum of items in the list (items must be numeric).
-   **`sorted(iterable, key=None, reverse=False)`:** Returns a *new* sorted list from the items in an iterable (does not modify the original list).

**Example of Common Operations:**
```python
# Conceptual e-commerce order items list
order_items = ["Laptop", "Mouse", "Keyboard"]
print(f"Initial order: {order_items}")

# Add an item
order_items.append("Webcam")
print(f"Appended: {order_items}")

# Insert an item
order_items.insert(1, "External HDD")
print(f"Inserted: {order_items}")

# Remove an item
if "Mouse" in order_items:
    order_items.remove("Mouse")
print(f"Removed 'Mouse': {order_items}")

# Pop an item
popped_item = order_items.pop(0) # Remove "Laptop"
print(f"Popped '{popped_item}', list is now: {order_items}")

# Sort (in-place)
order_items.sort()
print(f"Sorted: {order_items}")

# Count
print(f"Number of items: {len(order_items)}")
```

Refer to individual notes for each method (e.g., [[Python_list_append]], [[Python_list_sort]]) for more detailed explanations and specific examples.

---