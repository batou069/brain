---
tags:
  - python
  - list
  - method
  - clear
  - mutable
  - sequence
  - data_structures
  - function
aliases:
  - list.clear()
related:
  - "[[Python_List]]"
  - "[[Python_List_Methods]]"
  - "[[Python_list_pop]]"
  - "[[Python_list_remove]]"
worksheet:
  - WS17
date_created: 2025-06-11
---
# Python: `list.clear()`

The `clear()` method is used to remove **all items** from a [[Python_List|list]], making the list empty. This method modifies the original list in-place (it is a mutating operation) and does not return any value (it returns `None`).

## Syntax```python
list_object.clear()
```
This method takes no arguments.

## Behavior
-   All elements are removed from `list_object`.
-   After calling `clear()`, the list becomes empty (`[]`).
-   The list object itself still exists, but it contains no items. Its length becomes 0.
-   The original list is modified.

## Return Value
-   `None`. The method modifies the list in-place.

## Examples

**1. Clearing a list of product SKUs:**
```python
product_skus = ["WIDGET-001", "GADGET-002", "THINGY-003"]
print(f"Initial SKUs: {product_skus}, Length: {len(product_skus)}")

product_skus.clear()
print(f"SKUs after clear(): {product_skus}, Length: {len(product_skus)}")
```
Output:
```
Initial SKUs: ['WIDGET-001', 'GADGET-002', 'THINGY-003'], Length: 3
SKUs after clear(): [], Length: 0
```

**2. Effect on other references to the same list:**
Since `clear()` modifies the list in-place, other variables referencing the same list object will also see the change.
```python
shopping_cart = ["apple", "banana", "cherry"]
my_cart_alias = shopping_cart # Both names refer to the same list object

print(f"shopping_cart before clear: {shopping_cart}")
print(f"my_cart_alias before clear: {my_cart_alias}")

shopping_cart.clear()

print(f"shopping_cart after clear: {shopping_cart}")
print(f"my_cart_alias after clear (also empty): {my_cart_alias}")
```
Output:
```
shopping_cart before clear: ['apple', 'banana', 'cherry']
my_cart_alias before clear: ['apple', 'banana', 'cherry']
shopping_cart after clear: []
my_cart_alias after clear (also empty): []
```

## Alternatives to `clear()` (that create a new empty list)
If you want to reinitialize a list variable to an empty list *without* modifying the original list object (if other variables might still be referencing it), you would assign a new empty list:```python
original_list = [1, 2, 3]
ref_to_original = original_list

# Option 1: Reassigning the variable to a new empty list
original_list = [] 
print(f"original_list (reassigned): {original_list}") # Output: []
print(f"ref_to_original (still holds old data): {ref_to_original}") # Output: [1, 2, 3]

# Option 2: Clearing the original list object using clear()
original_list_for_clear = [4, 5, 6]
ref_to_original_for_clear = original_list_for_clear
original_list_for_clear.clear()
print(f"original_list_for_clear (cleared): {original_list_for_clear}") # Output: []
print(f"ref_to_original_for_clear (also empty): {ref_to_original_for_clear}") # Output: []
```
The choice depends on whether you want to affect all references to the list object or just reassign one variable.

`clear()` is a straightforward way to empty a list when you want to reuse the same list object but without its previous contents.

---