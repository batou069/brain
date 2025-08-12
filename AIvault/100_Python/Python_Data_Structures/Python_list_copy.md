---
tags:
  - python
  - list
  - method
  - copy
  - mutable
  - sequence
  - data_structures
  - shallow_copy
  - deep_copy
  - concept
  - function
aliases:
  - list.copy()
  - copying lists
  - shallow copy list
related:
  - "[[Python_List]]"
  - "[[Python_List_Methods]]"
  - "[[Python_Mutability_Immutability|Mutability and Immutability in Python]]"
  - "[[Python_References_Variables]]"
  - "[[Python_Slicing]]"
  - "[[Python_copy_module|copy module (deepcopy)]]"
worksheet:
  - WS17
date_created: 2025-06-11
---
# Python: `list.copy()`

The `list.copy()` method returns a **shallow copy** of the [[Python_List|list]]. This means it creates a new list object, but the elements inside the new list are references to the same objects found in the original list.

## Syntax

```python
new_list = list_object.copy()
```
This method takes no arguments.

## Behavior
-   A new list object is created.
-   The elements of the original list are copied into the new list.
    -   If the elements are immutable (e.g., numbers, strings, tuples of immutables), the new list effectively has independent copies of these values.
    -   If the elements are mutable (e.g., other lists, dictionaries), the new list will contain **references** to these same mutable objects. Changes to these nested mutable objects will be reflected in both the original and the copied list. This is the characteristic of a **shallow copy**.
-   The original list is not modified.

## Return Value
-   A new list object that is a shallow copy of the original list.

## Examples

**1. Copying a list of immutable items (e.g., product SKUs):**
```python
original_skus = ["SKU001", "SKU002", "SKU003"]
copied_skus = original_skus.copy()

print(f"Original SKUs: {original_skus}, id: {id(original_skus)}")
print(f"Copied SKUs:   {copied_skus}, id: {id(copied_skus)}")

# Modify the copied list
copied_skus.append("SKU004")
print(f"Modified copied SKUs: {copied_skus}")
print(f"Original SKUs (unchanged): {original_skus}")

# Modify an element in the original list (strings are immutable, so this rebinds)
# This doesn't illustrate shallow vs deep well with immutables, but shows list independence
original_skus = "SKU_NEW"
print(f"Modified original SKUs: {original_skus}")
print(f"Copied SKUs (unchanged by original's element reassignment): {copied_skus}")
```
Output:
```
Original SKUs: ['SKU001', 'SKU002', 'SKU003'], id: <some_id_1>
Copied SKUs:   ['SKU001', 'SKU002', 'SKU003'], id: <some_id_2>  (Note: different list object IDs)
Modified copied SKUs: ['SKU001', 'SKU002', 'SKU003', 'SKU004']
Original SKUs (unchanged): ['SKU001', 'SKU002', 'SKU003']
Modified original SKUs: ['SKU_NEW', 'SKU002', 'SKU003']
Copied SKUs (unchanged by original's element reassignment): ['SKU001', 'SKU002', 'SKU003', 'SKU004']
```
The IDs of `original_skus` and `copied_skus` are different, indicating they are distinct list objects.

**2. Shallow copy with nested mutable objects (e.g., list of product orders, where each order is a list):**
```python
order1_details = ["Laptop", 1200.00]
order2_details = ["Mouse", 25.00]
all_orders_original = [order1_details, order2_details]

all_orders_copy = all_orders_original.copy()

print(f"Original orders ID: {id(all_orders_original)}, Content: {all_orders_original}")
print(f"Copied orders ID:   {id(all_orders_copy)}, Content: {all_orders_copy}")
print(f"ID of first order in original: {id(all_orders_original)}")
print(f"ID of first order in copy:   {id(all_orders_copy)}") # Will be the SAME as above

# Modify a nested list through the copy
all_orders_copy.append("Warranty") # Add "Warranty" to the first order in the copied list
all_orders_copy.append(["Keyboard", 75.00]) # Add a new order to the copied list

print(f"\nAfter modifying nested list in copy AND appending to copy:")
print(f"Original orders: {all_orders_original}")
# Output: Original orders: [['Laptop', 1200.0, 'Warranty'], ['Mouse', 25.0]]
# Note: The nested list (order1_details) in original_orders is also changed.
print(f"Copied orders:   {all_orders_copy}")
# Output: Copied orders:   [['Laptop', 1200.0, 'Warranty'], ['Mouse', 25.0], ['Keyboard', 75.0]]
```
In this case, `all_orders_original[0]` and `all_orders_copy[0]` refer to the *same* inner list object `['Laptop', 1200.00]`. So, modifying this inner list through `all_orders_copy` also affects `all_orders_original`. However, appending a *new* list `["Keyboard", 75.00]` to `all_orders_copy` only affects `all_orders_copy` because it modifies the outer list structure.

## Alternatives for Shallow Copying
-   **Slicing `[:]`:** `new_list = old_list[:]` also creates a shallow copy. This is a very common and idiomatic way to do it.
    ```python
    list_a = [1,]
    list_b_slice_copy = list_a[:]
    print(f"ID of list_a: {id(list_a)}, ID of list_b_slice_copy: {id(list_b_slice_copy)}") # Different IDs
    print(f"ID of list_a: {id(list_a)}, ID of list_b_slice_copy: {id(list_b_slice_copy)}") # Same IDs for nested list
    ```
-   **`list(old_list)` constructor:** `new_list = list(old_list)` also creates a shallow copy.

## Deep Copy
If you need a completely independent copy of a list and all its nested mutable objects, you must use a **deep copy**. This is done using the `copy` module.
```python
import copy

original_nested_list = [1,, {"key": "value"}]
deep_copied_list = copy.deepcopy(original_nested_list)

# Modify a nested mutable element in the deep copy
deep_copied_list.append(30)
deep_copied_list["new_key"] = "new_value"

print(f"Original nested list: {original_nested_list}")
# Output: Original nested list: [1,, {'key': 'value'}] (UNCHANGED by deep copy modifications)
print(f"Deep copied list:     {deep_copied_list}")
# Output: Deep copied list:     [1,, {'key': 'value', 'new_key': 'new_value'}]
```
With `deepcopy`, `original_nested_list[1]` and `deep_copied_list[1]` are now different list objects.

`list.copy()` provides a convenient way to create a shallow copy, which is often sufficient when the list contains immutable elements or when shared references to nested mutable objects are acceptable or desired. For full independence with nested structures, `copy.deepcopy()` is necessary.

---