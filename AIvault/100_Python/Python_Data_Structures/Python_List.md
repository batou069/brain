---
tags:
  - python
  - data_structures
  - list
  - sequence
  - mutable
  - ordered
  - concept
  - example
aliases:
  - Python Lists
  - list object
related:
  - "[[100_Python/Python_Data_Structures/_Python_Data_Structures_MOC|_Python_Data_Structures_MOC]]"
  - "[[Python_Mutability_Immutability|Mutability and Immutability in Python]]"
  - "[[Python_Tuple]]"
  - "[[Python_Slicing]]"
  - "[[Python_Loops_Iteration|Looping and Iteration]]"
  - "[[Python_List_Comprehensions|List Comprehensions]]"
worksheet:
  - WS17
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Python: Lists (`list`)

A **list** in Python is one of the most versatile and commonly used built-in data structures. It is an **ordered, mutable sequence** of items. This means:
-   **Ordered:** The items in a list are stored in a specific sequence, and this order is preserved.
-   **Mutable:** You can change the contents of a list after it's created (add, remove, or modify items).
-   **Sequence:** Supports indexing, slicing, and iteration.
-   Lists can contain items of **mixed data types** (integers, floats, strings, other lists, etc.).

## Creating Lists
Lists are created using square brackets `[]`, with items separated by commas.

```python
# Empty list
empty_list = []
print(f"Empty list: {empty_list}")

# List of integers (e.g., product quantities)
quantities = [10, 25, 5, 150, 30]
print(f"Quantities: {quantities}")

# List of strings (e.g., product categories)
categories = ["Electronics", "Books", "Apparel", "Home Goods"]
print(f"Categories: {categories}")

# List with mixed data types
mixed_list = [1, "Product A", 29.99, True]
print(f"Mixed list: {mixed_list}")

# List created using the list() constructor (e.g., from a tuple or string)
list_from_tuple = list((1, 2, 3))
print(f"List from tuple: {list_from_tuple}")
list_from_string = list("hello")
print(f"List from string: {list_from_string}") # Output: ['h', 'e', 'l', 'l', 'o']
```

## Accessing Elements (Indexing)
List elements are accessed using zero-based indexing.
-   `my_list` is the first element.
-   `my_list[-1]` is the last element.

```python
product_categories = ["Electronics", "Books", "Apparel", "Home Goods"]
first_category = product_categories[0]
last_category = product_categories[-1]

print(f"First category: {first_category}")  # Output: Electronics
print(f"Last category: {last_category}")    # Output: Home Goods

# Modifying an element (since lists are mutable)
product_categories[1] = "Digital Books"
print(f"Modified categories: {product_categories}") # Output: ['Electronics', 'Digital Books', 'Apparel', 'Home Goods']
```

## Slicing Lists
[[Python_Slicing|Slicing]] allows you to get a sub-list.
`my_list[start:stop:step]`

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sub_list = numbers[2:5]    # Elements from index 2 up to (but not including) index 5
print(f"numbers[2:5] = {sub_list}") # Output: [2, 3, 4]

first_three = numbers[:3]  # Elements from the beginning up to index 3
print(f"numbers[:3] = {first_three}") # Output: [0, 1, 2]

from_index_5 = numbers[5:] # Elements from index 5 to the end
print(f"numbers[5:] = {from_index_5}") # Output: [5, 6, 7, 8, 9]

every_other = numbers[::2] # Every other element, starting from the first
print(f"numbers[::2] = {every_other}") # Output: [0, 2, 4, 6, 8]

reversed_list_slice = numbers[::-1] # A common way to get a reversed copy
print(f"numbers[::-1] = {reversed_list_slice}")
```

## Common List Methods (Mutating and Non-Mutating)
Since lists are mutable, many methods modify the list in-place.

[list2tab|#List Methods]
- Adding Elements
    -   **`append(item)`:** Adds `item` to the end of the list. (Mutates list)
        ```python
        # product_list = ["Laptop", "Mouse"]
        # product_list.append("Keyboard")
        # print(f"After append: {product_list}") # ['Laptop', 'Mouse', 'Keyboard']
        ```
    -   **`extend(iterable)`:** Appends all items from `iterable` to the end of the list. (Mutates list)
        ```python
        # accessories = ["Webcam", "Monitor"]
        # product_list.extend(accessories)
        # print(f"After extend: {product_list}") # ['Laptop', 'Mouse', 'Keyboard', 'Webcam', 'Monitor']
        ```
    -   **`insert(index, item)`:** Inserts `item` at the specified `index`. (Mutates list)
        ```python
        # product_list.insert(1, "Tablet") # Insert "Tablet" at index 1
        # print(f"After insert: {product_list}") # ['Laptop', 'Tablet', 'Mouse', ...]
        ```
    -   **Concatenation (`+`):** Creates a *new* list.
        ```python
        # list1 = [1, 2]
        # list2 = [3, 4]
        # combined_list = list1 + list2
        # print(f"Concatenated list: {combined_list}") # [1, 2, 3, 4]
        # print(f"Original list1: {list1}") # Unchanged
        ```
- Removing Elements
    -   **`remove(item)`:** Removes the *first* occurrence of `item` from the list. Raises `ValueError` if `item` is not found. (Mutates list)
        ```python
        # product_list = ["Laptop", "Mouse", "Keyboard", "Mouse"]
        # product_list.remove("Mouse")
        # print(f"After remove('Mouse'): {product_list}") # ['Laptop', 'Keyboard', 'Mouse']
        ```
    -   **`pop(index=-1)`:** Removes and returns the item at the given `index`. If `index` is not specified, it removes and returns the last item. Raises `IndexError` if the list is empty or index is out of range. (Mutates list)
        ```python
        # product_list = ["Laptop", "Tablet", "Keyboard"]
        # removed_item = product_list.pop(1) # Removes "Tablet"
        # print(f"Removed item by pop(1): {removed_item}") # Tablet
        # print(f"List after pop: {product_list}") # ['Laptop', 'Keyboard']
        # last_item = product_list.pop()
        # print(f"Removed last item: {last_item}") # Keyboard
        ```
    -   **`clear()`:** Removes all items from the list. (Mutates list)
        ```python
        # temp_list = [1, 2, 3]
        # temp_list.clear()
        # print(f"After clear: {temp_list}") # []
        ```
    -   **`del` statement:** Can remove items by index or slice. (Mutates list)
        ```python
        # numbers_del = [10, 20, 30, 40, 50]
        # del numbers_del[1] # Delete item at index 1 (20)
        # print(f"After del numbers_del[1]: {numbers_del}") # [10, 30, 40, 50]
        # del numbers_del[1:3] # Delete slice from index 1 to 2 (30, 40)
        # print(f"After del numbers_del[1:3]: {numbers_del}") # [10, 50]
        ```
- Searching and Counting
    -   **`index(item, start=0, end=len(list))`:** Returns the zero-based index in the list of the first item whose value is equal to `item`. Raises `ValueError` if `item` is not found.
        ```python
        # product_list = ["Laptop", "Mouse", "Keyboard", "Mouse"]
        # first_mouse_index = product_list.index("Mouse")
        # print(f"Index of first 'Mouse': {first_mouse_index}") # 1
        ```
    -   **`count(item)`:** Returns the number of times `item` appears in the list.
        ```python
        # mouse_count = product_list.count("Mouse")
        # print(f"Count of 'Mouse': {mouse_count}") # 2
        ```
    -   **`in` operator:** Checks if an item exists in the list.
        ```python
        # has_laptop = "Laptop" in product_list
        # print(f"Is 'Laptop' in product_list? {has_laptop}") # True
        ```
- Sorting and Reversing
    -   **`sort(key=None, reverse=False)`:** Sorts the items of the list in-place. (Mutates list)
        -   `key`: A function to be called on each list element prior to making comparisons.
        -   `reverse`: If `True`, sorts in descending order.
        ```python
        # unsorted_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
        # unsorted_numbers.sort()
        # print(f"Sorted numbers (ascending): {unsorted_numbers}")
        # unsorted_numbers.sort(reverse=True)
        # print(f"Sorted numbers (descending): {unsorted_numbers}")

        # Sort products by length of name
        # product_names = ["Monitor", "Keyboard", "Mouse", "Webcam Adapter"]
        # product_names.sort(key=len)
        # print(f"Products sorted by name length: {product_names}")
        ```
    -   **`sorted(iterable, key=None, reverse=False)`:** A built-in function that returns a *new* sorted list from the items in an iterable (does not mutate original).
        ```python
        # original_list = [5, 2, 8, 1]
        # new_sorted_list = sorted(original_list)
        # print(f"Original list: {original_list}") # [5, 2, 8, 1]
        # print(f"New sorted list: {new_sorted_list}") # [1, 2, 5, 8]
        ```
    -   **`reverse()`:** Reverses the elements of the list in-place. (Mutates list)
        ```python
        # my_items = ['a', 'b', 'c', 'd']
        # my_items.reverse()
        # print(f"Reversed items: {my_items}") # ['d', 'c', 'b', 'a']
        ```
- Copying
    -   **`copy()`:** Returns a shallow copy of the list.
        ```python
        # original = [1, [2, 3], 4]
        # shallow_copy = original.copy()
        # shallow_copy[0] = 100
        # shallow_copy[1].append(99) # Modifies nested list in both original and copy

        # print(f"Original after shallow copy mod: {original}") # [1, [2, 3, 99], 4]
        # print(f"Shallow copy: {shallow_copy}") # [100, [2, 3, 99], 4]
        ```
        For a completely independent copy of nested mutable structures, use `copy.deepcopy()`.
    -   Slicing `[:]` also creates a shallow copy: `new_list = old_list[:]`.
- Other Useful Functions
    -   **`len(list)`:** Returns the number of items in the list.
    -   **`min(list)` / `max(list)`:** Returns the minimum/maximum item (if items are comparable).

## Use Cases
Lists are used extensively in Python for:
-   Storing collections of related items where order matters.
-   Implementing stacks (using `append()` and `pop()`).
-   Implementing queues (using `append()` and `pop(0)`, though `collections.deque` is more efficient for queues).
-   Accumulating results during iteration.
-   Representing rows of data before loading into more structured formats like Pandas DataFrames.

Due to their mutability and ordered nature, lists are a flexible and fundamental data structure in Python.

---

# Python: Lists (`list`)

A **list** in Python is one of the most versatile and commonly used built-in data structures. It is an **ordered, mutable sequence** of items. This means:
-   **Ordered:** The items in a list are stored in a specific sequence, and this order is preserved.
-   **Mutable:** You can change the contents of a list after it's created (add, remove, or modify items).
-   **Sequence:** Supports indexing, slicing, and iteration.
-   Lists can contain items of **mixed data types** (integers, floats, strings, other lists, etc.).

## Creating Lists
Lists are created using square brackets `[]`, with items separated by commas.

```python
# Empty list
empty_list = []
print(f"Empty list: {empty_list}")

# List of integers (e.g., product quantities)
quantities = [10, 25, 5, 150, 30]
print(f"Quantities: {quantities}")

# List of strings (e.g., product categories)
categories = ["Electronics", "Books", "Apparel", "Home Goods"]
print(f"Categories: {categories}")

# List with mixed data types
mixed_list = [1, "Product A", 29.99, True]
print(f"Mixed list: {mixed_list}")

# List created using the list() constructor (e.g., from a tuple or string)
list_from_tuple = list((1, 2, 3))
print(f"List from tuple: {list_from_tuple}")
list_from_string = list("hello")
print(f"List from string: {list_from_string}") # Output: ['h', 'e', 'l', 'l', 'o']
```

## Accessing Elements (Indexing)
List elements are accessed using zero-based indexing.
-   `my_list` is the first element.
-   `my_list[-1]` is the last element.

```python
product_categories = ["Electronics", "Books", "Apparel", "Home Goods"]
first_category = product_categories[0]
last_category = product_categories[-1]

print(f"First category: {first_category}")  # Output: Electronics
print(f"Last category: {last_category}")    # Output: Home Goods

# Modifying an element (since lists are mutable)
product_categories[1] = "Digital Books"
print(f"Modified categories: {product_categories}") # Output: ['Electronics', 'Digital Books', 'Apparel', 'Home Goods']
```

## Slicing Lists
[[Python_Slicing|Slicing]] allows you to get a sub-list.
`my_list[start:stop:step]`

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sub_list = numbers[2:5]    # Elements from index 2 up to (but not including) index 5
print(f"numbers[2:5] = {sub_list}") # Output: [2, 3, 4]

first_three = numbers[:3]  # Elements from the beginning up to index 3
print(f"numbers[:3] = {first_three}") # Output: [0, 1, 2]

from_index_5 = numbers[5:] # Elements from index 5 to the end
print(f"numbers[5:] = {from_index_5}") # Output: [5, 6, 7, 8, 9]

every_other = numbers[::2] # Every other element, starting from the first
print(f"numbers[::2] = {every_other}") # Output: [0, 2, 4, 6, 8]

reversed_list_slice = numbers[::-1] # A common way to get a reversed copy
print(f"numbers[::-1] = {reversed_list_slice}")
```

## Common List Methods (Mutating and Non-Mutating)
Since lists are mutable, many methods modify the list in-place.

[list2tab|#List Methods]
- Adding Elements
    -   **`append(item)`:** Adds `item` to the end of the list. (Mutates list)
        ```python
        # product_list = ["Laptop", "Mouse"]
        # product_list.append("Keyboard")
        # print(f"After append: {product_list}") # ['Laptop', 'Mouse', 'Keyboard']
        ```
    -   **`extend(iterable)`:** Appends all items from `iterable` to the end of the list. (Mutates list)
        ```python
        # accessories = ["Webcam", "Monitor"]
        # product_list.extend(accessories)
        # print(f"After extend: {product_list}") # ['Laptop', 'Mouse', 'Keyboard', 'Webcam', 'Monitor']
        ```
    -   **`insert(index, item)`:** Inserts `item` at the specified `index`. (Mutates list)
        ```python
        # product_list.insert(1, "Tablet") # Insert "Tablet" at index 1
        # print(f"After insert: {product_list}") # ['Laptop', 'Tablet', 'Mouse', ...]
        ```
    -   **Concatenation (`+`):** Creates a *new* list.
        ```python
        # list1 = [1, 2]
        # list2 = [3, 4]
        # combined_list = list1 + list2
        # print(f"Concatenated list: {combined_list}") # [1, 2, 3, 4]
        # print(f"Original list1: {list1}") # Unchanged
        ```
- Removing Elements
    -   **`remove(item)`:** Removes the *first* occurrence of `item` from the list. Raises `ValueError` if `item` is not found. (Mutates list)
        ```python
        # product_list = ["Laptop", "Mouse", "Keyboard", "Mouse"]
        # product_list.remove("Mouse")
        # print(f"After remove('Mouse'): {product_list}") # ['Laptop', 'Keyboard', 'Mouse']
        ```
    -   **`pop(index=-1)`:** Removes and returns the item at the given `index`. If `index` is not specified, it removes and returns the last item. Raises `IndexError` if the list is empty or index is out of range. (Mutates list)
        ```python
        # product_list = ["Laptop", "Tablet", "Keyboard"]
        # removed_item = product_list.pop(1) # Removes "Tablet"
        # print(f"Removed item by pop(1): {removed_item}") # Tablet
        # print(f"List after pop: {product_list}") # ['Laptop', 'Keyboard']
        # last_item = product_list.pop()
        # print(f"Removed last item: {last_item}") # Keyboard
        ```
    -   **`clear()`:** Removes all items from the list. (Mutates list)
        ```python
        # temp_list = [1, 2, 3]
        # temp_list.clear()
        # print(f"After clear: {temp_list}") # []
        ```
    -   **`del` statement:** Can remove items by index or slice. (Mutates list)
        ```python
        # numbers_del = [10, 20, 30, 40, 50]
        # del numbers_del[1] # Delete item at index 1 (20)
        # print(f"After del numbers_del[1]: {numbers_del}") # [10, 30, 40, 50]
        # del numbers_del[1:3] # Delete slice from index 1 to 2 (30, 40)
        # print(f"After del numbers_del[1:3]: {numbers_del}") # [10, 50]
        ```
- Searching and Counting
    -   **`index(item, start=0, end=len(list))`:** Returns the zero-based index in the list of the first item whose value is equal to `item`. Raises `ValueError` if `item` is not found.
        ```python
        # product_list = ["Laptop", "Mouse", "Keyboard", "Mouse"]
        # first_mouse_index = product_list.index("Mouse")
        # print(f"Index of first 'Mouse': {first_mouse_index}") # 1
        ```
    -   **`count(item)`:** Returns the number of times `item` appears in the list.
        ```python
        # mouse_count = product_list.count("Mouse")
        # print(f"Count of 'Mouse': {mouse_count}") # 2
        ```
    -   **`in` operator:** Checks if an item exists in the list.
        ```python
        # has_laptop = "Laptop" in product_list
        # print(f"Is 'Laptop' in product_list? {has_laptop}") # True
        ```
- Sorting and Reversing
    -   **`sort(key=None, reverse=False)`:** Sorts the items of the list in-place. (Mutates list)
        -   `key`: A function to be called on each list element prior to making comparisons.
        -   `reverse`: If `True`, sorts in descending order.
        ```python
        # unsorted_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
        # unsorted_numbers.sort()
        # print(f"Sorted numbers (ascending): {unsorted_numbers}")
        # unsorted_numbers.sort(reverse=True)
        # print(f"Sorted numbers (descending): {unsorted_numbers}")

        # Sort products by length of name
        # product_names = ["Monitor", "Keyboard", "Mouse", "Webcam Adapter"]
        # product_names.sort(key=len)
        # print(f"Products sorted by name length: {product_names}")
        ```
    -   **`sorted(iterable, key=None, reverse=False)`:** A built-in function that returns a *new* sorted list from the items in an iterable (does not mutate original).
        ```python
        # original_list = [5, 2, 8, 1]
        # new_sorted_list = sorted(original_list)
        # print(f"Original list: {original_list}") # [5, 2, 8, 1]
        # print(f"New sorted list: {new_sorted_list}") # [1, 2, 5, 8]
        ```
    -   **`reverse()`:** Reverses the elements of the list in-place. (Mutates list)
        ```python
        # my_items = ['a', 'b', 'c', 'd']
        # my_items.reverse()
        # print(f"Reversed items: {my_items}") # ['d', 'c', 'b', 'a']
        ```
- Copying
    -   **`copy()`:** Returns a shallow copy of the list.
        ```python
        # original = [1, [2, 3], 4]
        # shallow_copy = original.copy()
        # shallow_copy[0] = 100
        # shallow_copy[1].append(99) # Modifies nested list in both original and copy

        # print(f"Original after shallow copy mod: {original}") # [1, [2, 3, 99], 4]
        # print(f"Shallow copy: {shallow_copy}") # [100, [2, 3, 99], 4]
        ```
        For a completely independent copy of nested mutable structures, use `copy.deepcopy()`.
    -   Slicing `[:]` also creates a shallow copy: `new_list = old_list[:]`.
- Other Useful Functions
    -   **`len(list)`:** Returns the number of items in the list.
    -   **`min(list)` / `max(list)`:** Returns the minimum/maximum item (if items are comparable).

## Use Cases
Lists are used extensively in Python for:
-   Storing collections of related items where order matters.
-   Implementing stacks (using `append()` and `pop()`).
-   Implementing queues (using `append()` and `pop(0)`, though `collections.deque` is more efficient for queues).
-   Accumulating results during iteration.
-   Representing rows of data before loading into more structured formats like Pandas DataFrames.

Due to their mutability and ordered nature, lists are a flexible and fundamental data structure in Python.

---