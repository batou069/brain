---
tags:
  - python
  - list
  - method
  - append
  - mutable
  - sequence
  - data_structures
  - function
aliases:
  - list.append()
related:
  - "[[Python_List]]"
  - "[[Python_List_Methods]]"
  - "[[Python_list_extend]]"
worksheet:
  - WS17
date_created: 2025-06-11
---
# Python: `list.append(item)`

The `append()` method is used to add a single **item** to the **end** of an existing [[Python_List|list]]. This method modifies the original list in-place (it is a mutating operation) and does not return any value (it returns `None`).

## Syntax```python
list_object.append(item)
```
-   `item`: The element to be added to the list. This can be of any data type (integer, string, float, another list, etc.).

## Behavior
-   The `item` is added as a single element at the end of the list.
-   If `item` itself is an iterable (like another list or a tuple), the entire iterable is added as one element, not its individual components. To add individual components from an iterable, use [[Python_list_extend|`extend()`]].
-   The list's length increases by one.

## Return Value
-   `None`. The method modifies the list in-place.

## Examples

**1. Appending basic data types:**
```python
product_categories = ["Electronics", "Books"]
print(f"Initial list: {product_categories}")

product_categories.append("Apparel")
print(f"After appending 'Apparel': {product_categories}")

product_categories.append("Home Goods")
print(f"After appending 'Home Goods': {product_categories}")

# Appending a number
item_counts = [10, 25]
item_counts.append(50)
print(f"Item counts: {item_counts}")
```
Output:
```
Initial list: ['Electronics', 'Books']
After appending 'Apparel': ['Electronics', 'Books', 'Apparel']
After appending 'Home Goods': ['Electronics', 'Books', 'Apparel', 'Home Goods']
Item counts: [10, 25, 50]
```

**2. Appending another list (as a single element):**
```python
main_categories = ["Clothing", "Shoes"]
sub_categories_list = ["Shirts", "Pants"]

main_categories.append(sub_categories_list) # Appends the list itself as one element
print(f"List with appended sub-list: {main_categories}")
print(f"Length of main_categories: {len(main_categories)}")
print(f"Last element type: {type(main_categories[-1])}")
```
Output:
```
List with appended sub-list: ['Clothing', 'Shoes', ['Shirts', 'Pants']]
Length of main_categories: 3
Last element type: <class 'list'>
```
Compare this with [[Python_list_extend|`extend()`]], which would add "Shirts" and "Pants" as individual elements.

**3. Building a list in a loop:**
`append()` is commonly used to build up a list dynamically.
```python
# Collect all even numbers from 0 to 9
even_numbers = []
for i in range(10):
    if i % 2 == 0:
        even_numbers.append(i)
print(f"Even numbers collected: {even_numbers}")
```
Output:
```
Even numbers collected: [0, 2, 4, 6, 8]
```
This is a common pattern, often more concisely written using [[Python_List_Comprehensions|list comprehensions]]: `even_numbers = [i for i in range(10) if i % 2 == 0]`.

## Common Mistakes
-   **Assigning the result of `append()`:**
    ```python
    my_list = [1, 2]
    # Incorrect: my_list = my_list.append(3) 
    # This makes my_list = None, because append() returns None
    my_list.append(3) # Correct
    print(my_list)
    ```
-   **Confusing `append()` with `extend()`:**
    -   `append()` adds its argument as a single element.
    -   `extend()` iterates over its argument and adds each element.

`append()` is one of the most fundamental list operations for growing a list by adding elements one at a time to its end.

---