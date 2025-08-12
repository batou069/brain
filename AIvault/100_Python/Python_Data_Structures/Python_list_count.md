---
tags:
  - python
  - list
  - method
  - count
  - sequence
  - data_structures
  - function
aliases:
  - list.count()
related:
  - "[[Python_List]]"
  - "[[Python_List_Methods]]"
  - "[[Python_list_index_method|list.index()]]"
  - "[[Python_Operators#Membership Operators (in, not in)|Membership Operators (in, not in)]]"
worksheet:
  - WS17
date_created: 2025-06-11
---
# Python: `list.count(item)`

The `count()` method is used to determine the number of times a specified `item` appears in a [[Python_List|list]].

## Syntax```python
list_object.count(item)
```
-   `item`: The element whose occurrences are to be counted in the list.

## Behavior
-   The method iterates through the list and counts how many elements are equal to `item`.
-   Comparison is done using the equality operator (`==`).
-   If the `item` is not found in the list, `count()` returns 0.
-   This method does **not** modify the original list.

## Return Value
-   An integer representing the total number of occurrences of `item` in the list.

## Examples

**1. Counting occurrences of numbers in a list of product ratings:**
```python
product_ratings =
print(f"Product ratings: {product_ratings}")

count_of_5_stars = product_ratings.count(5)
print(f"Number of 5-star ratings: {count_of_5_stars}") # Output: 4

count_of_4_stars = product_ratings.count(4)
print(f"Number of 4-star ratings: {count_of_4_stars}") # Output: 3

count_of_1_star = product_ratings.count(1)
print(f"Number of 1-star ratings: {count_of_1_star}") # Output: 1

count_of_6_stars = product_ratings.count(6) # Item not in list
print(f"Number of 6-star ratings: {count_of_6_stars}") # Output: 0
```

**2. Counting occurrences of strings in a list of product categories:**
```python
order_categories = ["Electronics", "Books", "Apparel", "Electronics", "Home Goods", "Electronics"]
print(f"Order categories: {order_categories}")

count_electronics = order_categories.count("Electronics")
print(f"Count of 'Electronics': {count_electronics}") # Output: 3

count_toys = order_categories.count("Toys")
print(f"Count of 'Toys': {count_toys}") # Output: 0
```

**3. Counting occurrences with mixed data types (comparison rules apply):**
```python
mixed_items = [1, "1", True, 1.0, False, 0]
print(f"Mixed items: {mixed_items}")

# Note: True == 1 and False == 0 in Python for numeric comparisons
count_of_int_1 = mixed_items.count(1) 
print(f"Count of integer 1: {count_of_int_1}") # Output: 2 (1 and True)

count_of_str_1 = mixed_items.count("1")
print(f"Count of string '1': {count_of_str_1}") # Output: 1

count_of_bool_true = mixed_items.count(True)
print(f"Count of boolean True: {count_of_bool_true}") # Output: 2 (True and 1)

count_of_float_1_0 = mixed_items.count(1.0)
print(f"Count of float 1.0: {count_of_float_1_0}") # Output: 2 (1 and True, as 1 == 1.0 and True == 1.0)
```
This example highlights that `count()` uses equality comparison (`==`), so `1`, `1.0`, and `True` are considered equal for counting purposes.

## Performance
The time complexity of `list.count()` is $O(N)$, where $N$ is the number of elements in the list, because it generally needs to iterate through the entire list to count all occurrences.

`count()` is a straightforward method for determining the frequency of a specific element within a list. For counting frequencies of all unique elements, `collections.Counter` is often more efficient.

---