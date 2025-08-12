---
tags:
  - python
  - dictionary
  - dict
  - method
  - popitem
  - remove
  - mutable
  - data_structures
  - function
  - LIFO
aliases:
  - dict.popitem()
related:
  - "[[Python_Dictionary]]"
  - "[[Python_Dictionary_Methods]]"
  - "[[Python_dict_pop]]"
worksheet:
  - WS17
date_created: 2025-06-11
---
# Python: `dict.popitem()`

The `popitem()` method is used to remove and return an arbitrary **(key, value) pair** from a [[Python_Dictionary|dictionary]]. This method modifies the original dictionary in-place.

## Syntax```python
dictionary_object.popitem()
```
This method takes no arguments.

## Behavior
-   Removes an arbitrary key-value pair from the dictionary.
-   **Order (Python 3.7+):** In Python versions 3.7 and later, `popitem()` is guaranteed to remove and return items in **LIFO (Last-In, First-Out)** order. This means it will remove the item that was most recently added to the dictionary.
-   **Order (Python < 3.7):** In older Python versions (before 3.7, and in 3.6 for CPython but not guaranteed for all implementations), `popitem()` removed a truly arbitrary item as dictionaries were unordered.
-   If the dictionary is empty, calling `popitem()` raises a `KeyError`.
-   The original dictionary is modified.

## Return Value
-   A **tuple** containing the removed `(key, value)` pair.
-   Raises `KeyError` if the dictionary is empty.

## Examples

**1. Basic usage (Python 3.7+ showing LIFO):**
```python
# E-commerce product features added sequentially
product_features = {}
product_features["color"] = "Red"
product_features["size"] = "M"
product_features["material"] = "Cotton" # Last item added
print(f"Initial features: {product_features}")

# Pop items (LIFO order)
last_added_item = product_features.popitem()
print(f"Popped item (LIFO): {last_added_item}") # Output: ('material', 'Cotton')
print(f"Features after first pop: {product_features}")

second_last_added_item = product_features.popitem()
print(f"Popped item (LIFO): {second_last_added_item}") # Output: ('size', 'M')
print(f"Features after second pop: {product_features}")
```
Output (Python 3.7+):
```
Initial features: {'color': 'Red', 'size': 'M', 'material': 'Cotton'}
Popped item (LIFO): ('material', 'Cotton')
Features after first pop: {'color': 'Red', 'size': 'M'}
Popped item (LIFO): ('size', 'M')
Features after second pop: {'color': 'Red'}
```

**2. Popping from an empty dictionary:**
```python
empty_cart_details = {}
try:
    empty_cart_details.popitem()
except KeyError as e:
    print(f"Error popping from empty dictionary: {e}") # Output: 'popitem(): dictionary is empty'
```

## Use Cases
-   **Iteratively processing and removing items from a dictionary:** Especially useful when you want to process items in a LIFO manner (for Python 3.7+) or when the specific order of removal doesn't matter and you just need to consume all items.
-   **Implementing algorithms that require LIFO processing of dictionary items.**
-   **Destructive iteration:** When you want to loop through a dictionary and remove items as you go, `popitem()` can be used in a `while` loop until the dictionary is empty.
    ```python
    # user_tasks = {"task1": "pending", "task2": "in-progress", "task3": "pending"}
    # print("\nProcessing tasks (LIFO):")
    # while user_tasks: # Loop while dictionary is not empty
    #     try:
    #         task_id, status = user_tasks.popitem()
    #         print(f"  Processing and removing: {task_id} ({status})")
    #     except KeyError: # Should not happen if while condition is correct
    #         break 
    # print(f"Tasks remaining: {user_tasks}")
    ```

## `popitem()` vs. `pop(key)`
-   **`popitem()`:** Removes an item without needing to specify a key (LIFO in Python 3.7+). Returns a `(key, value)` tuple.
-   **[[Python_dict_pop|`pop(key, default)`]]:** Removes an item by a *specific key*. Returns only the *value*. Allows specifying a default if the key might be missing.

If you need to remove items in a specific order (not LIFO) or by a known key, `pop(key)` or `del dict[key]` are more appropriate. If you need to consume items from a dictionary, and the LIFO order is suitable or order doesn't matter, `popitem()` is efficient.

---