---
tags:
  - python
  - data_structures
  - list
  - dictionary
  - set
  - delete
  - remove
  - pop
  - mutable
  - concept
aliases:
  - Deleting from Python Data Structures
  - Removing Elements Python
related:
  - "[[100_Python/Python_Data_Structures/_Python_Data_Structures_MOC|_Python_Data_Structures_MOC]]"
  - "[[Python_List_Methods]]"
  - "[[Python_Dictionary_Methods]]"
  - "[[Python_Set_Methods]]"
  - "[[Python_Mutability_Immutability|Mutability and Immutability in Python]]"
worksheet:
  - WS17
date_created: 2025-08-20
---
# Python: Deleting Elements from Data Structures

Python's built-in [[Python_Mutability_Immutability|mutable data structures]] (lists, dictionaries, sets) provide various ways to remove or delete elements. Immutable data structures (tuples, frozensets, strings, numbers) cannot have elements removed from them in-place; any operation that "removes" an element from an immutable structure actually creates a new object without that element.

>[!question] Can you delete an element inside a data structure?
>Yes, you can delete elements from **mutable** data structures like lists, dictionaries, and sets. You cannot directly delete elements from immutable data structures like tuples or strings in-place; instead, you would create a new object excluding the desired element(s).

## Deleting from Lists (`list`)
Lists offer several ways to remove elements:

[list2tab|#List Deletion Methods]
- `list.remove(value)`
    -   **How:** Removes the **first occurrence** of the specified `value`.
    -   **Raises:** `ValueError` if the value is not found.
    -   **Example:**
        ```python
        product_cart = ["apple", "banana", "cherry", "banana"]
        product_cart.remove("banana") # Removes the first "banana"
        print(product_cart) # Output: ['apple', 'cherry', 'banana']
        ```
    -   See [[Python_list_remove]].
- `list.pop(index=-1)`
    -   **How:** Removes and returns the element at the specified `index`. If no index is given, it removes and returns the last element (LIFO behavior).
    -   **Raises:** `IndexError` if the list is empty or the index is out of range.
    -   **Example:**
        ```python
        product_cart = ["apple", "banana", "cherry"]
        removed_item = product_cart.pop(0) # Removes "apple"
        print(f"Removed: {removed_item}, Cart: {product_cart}") # Output: Removed: apple, Cart: ['banana', 'cherry']
        last_item = product_cart.pop() # Removes "cherry"
        print(f"Removed: {last_item}, Cart: {product_cart}") # Output: Removed: cherry, Cart: ['banana']
        ```
    -   See [[Python_list_pop]].
- `del list[index]`
    -   **How:** The `del` statement removes the element at the specified `index`.
    -   **Raises:** `IndexError` if the index is out of range.
    -   **Example:**
        ```python
        product_cart = ["apple", "banana", "cherry"]
        del product_cart[1] # Removes "banana"
        print(product_cart) # Output: ['apple', 'cherry']
        ```
- `del list[start:stop:step]` (Slice Deletion)
    -   **How:** The `del` statement can remove a slice of elements.
    -   **Example:**
        ```python
        numbers = [10, 20, 30, 40, 50, 60]
        del numbers[1:4] # Removes elements at index 1, 2, 3 (i.e., 20, 30, 40)
        print(numbers) # Output: [10, 50, 60]
        ```
- `list.clear()`
    -   **How:** Removes all elements from the list, making it empty.
    -   **Example:**
        ```python
        product_cart = ["apple", "banana"]
        product_cart.clear()
        print(product_cart) # Output: []
        ```
    -   See [[Python_list_clear]].

## Deleting from Dictionaries (`dict`)
Dictionaries store key-value pairs. Deletion is typically done by key.

[list2tab|#Dictionary Deletion Methods]
- `dict.pop(key, default=RAISE_ERROR)`
    -   **How:** Removes the item with the specified `key` and returns its value.
    -   **Raises/Returns:** If `key` is not found, it returns `default` if provided, otherwise raises `KeyError`.
    -   **Example:**
        ```python
        product_info = {"name": "Laptop", "price": 1200, "stock": 50}
        price_value = product_info.pop("price")
        print(f"Removed price: {price_value}, Info: {product_info}") 
        # Output: Removed price: 1200, Info: {'name': 'Laptop', 'stock': 50}
        
        color = product_info.pop("color", "Not Available") # Key "color" doesn't exist
        print(f"Removed color: {color}, Info: {product_info}")
        # Output: Removed color: Not Available, Info: {'name': 'Laptop', 'stock': 50}
        ```
    -   See [[Python_dict_pop]].
- `dict.popitem()`
    -   **How:** Removes and returns an arbitrary (key, value) pair. In Python 3.7+, this is LIFO (Last-In, First-Out).
    -   **Raises:** `KeyError` if the dictionary is empty.
    -   **Example:**
        ```python
        product_info = {"name": "Laptop", "price": 1200, "stock": 50}
        key, value = product_info.popitem() # Removes ('stock', 50) in Python 3.7+
        print(f"Popped item: ({key}, {value}), Info: {product_info}")
        ```
    -   See [[Python_dict_popitem]].
- `del dict[key]`
    -   **How:** The `del` statement removes the item with the specified `key`.
    -   **Raises:** `KeyError` if the key is not found.
    -   **Example:**
        ```python
        product_info = {"name": "Laptop", "price": 1200, "stock": 50}
        if "stock" in product_info:
            del product_info["stock"]
        print(f"Info after del 'stock': {product_info}") # Output: {'name': 'Laptop', 'price': 1200}
        ```
- `dict.clear()`
    -   **How:** Removes all items from the dictionary, making it empty.
    -   **Example:**
        ```python
        product_info = {"name": "Laptop", "price": 1200}
        product_info.clear()
        print(f"Info after clear: {product_info}") # Output: {}
        ```

## Deleting from Sets (`set`)
Sets store unique, unordered elements.

[list2tab|#Set Deletion Methods]
- `set.remove(element)`
    -   **How:** Removes the specified `element` from the set.
    -   **Raises:** `KeyError` if the element is not found.
    -   **Example:**
        ```python
        product_tags = {"electronics", "sale", "new", "gadget"}
        product_tags.remove("sale")
        print(product_tags) # Output example: {'new', 'gadget', 'electronics'}
        ```
- `set.discard(element)`
    -   **How:** Removes the specified `element` from the set if it is present.
    -   **Raises:** Does **not** raise an error if the element is not found.
    -   **Example:**
        ```python
        product_tags = {"electronics", "new", "gadget"}
        product_tags.discard("new")
        print(product_tags) # Output example: {'gadget', 'electronics'}
        product_tags.discard("obsolete") # "obsolete" is not in the set, no error
        print(product_tags) # Output example: {'gadget', 'electronics'}
        ```
- `set.pop()`
    -   **How:** Removes and returns an **arbitrary** element from the set. Since sets are unordered, you cannot predict which element will be removed.
    -   **Raises:** `KeyError` if the set is empty.
    -   **Example:**
        ```python
        product_tags = {"electronics", "new", "gadget"}
        removed_tag = product_tags.pop()
        print(f"Removed tag: {removed_tag}, Remaining tags: {product_tags}")
        ```
- `set.clear()`
    -   **How:** Removes all elements from the set, making it empty.
    -   **Example:**
        ```python
        product_tags = {"electronics", "new"}
        product_tags.clear()
        print(product_tags) # Output: set()
        ```

## Immutable Structures (Tuples, Strings, Frozensets)
You cannot directly delete elements from immutable structures in-place. To achieve a similar effect, you typically create a new object by slicing or filtering out the unwanted elements.

**Example (Tuple):**
```python
my_tuple = (10, 20, 30, 40, 50)
# To "remove" 30, create a new tuple without it:
new_tuple = my_tuple[:2] + my_tuple[3:] # Concatenate slices
print(f"New tuple after 'removing' 30: {new_tuple}") # Output: (10, 20, 40, 50)
```

Understanding how to delete elements is crucial for managing the state of mutable data structures in Python.

---