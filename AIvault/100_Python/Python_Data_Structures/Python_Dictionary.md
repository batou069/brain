---
tags:
  - python
  - data_structures
  - dictionary
  - dict
  - mapping
  - key_value
  - mutable
  - concept
  - example
aliases:
  - Python Dictionaries
  - dict object
  - Hash Map Python
  - Associative Array Python
related:
  - "[[100_Python/Python_Data_Structures/_Python_Data_Structures_MOC|_Python_Data_Structures_MOC]]"
  - "[[Python_Mutability_Immutability|Mutability and Immutability in Python]]"
  - "[[Python_Loops_Iteration|Looping and Iteration]]"
  - "[[Python_Dictionary_Methods]]"
  - "[[Python_Dictionary_Comprehensions|Dictionary Comprehensions]]"
worksheet:
  - WS17
date_created: 2025-06-11
---
# Python: Dictionaries (`dict`)

A **dictionary** in Python is an **unordered (in Python < 3.7, ordered in Python 3.7+) collection of key-value pairs**. It is a mutable mapping type.
-   **Key-Value Pairs:** Each item in a dictionary consists of a unique key and its associated value.
-   **Keys Must Be Unique and Immutable:**
    -   Keys within a dictionary must be unique. If you assign a value to an existing key, it overwrites the old value.
    -   Keys must be of an immutable type (e.g., strings, numbers, tuples containing only immutable elements). You cannot use lists or other dictionaries as keys.
-   **Values Can Be Anything:** Values in a dictionary can be of any data type and can be duplicated.
-   **Mutable:** You can add, remove, or modify key-value pairs after the dictionary is created.
-   **Ordering:**
    -   **Python 3.7+:** Dictionaries preserve insertion order.
    -   **Python < 3.7:** Dictionaries were unordered. Iterating over them might yield items in an arbitrary order. (For older Python, `collections.OrderedDict` could be used for ordered dictionaries).

Dictionaries are highly optimized for retrieving values when the key is known (average $O(1)$ time complexity) due to their underlying hash table implementation.

## Creating Dictionaries
-   Using curly braces `{}` with `key: value` pairs.
-   Using the `dict()` constructor.

```python
# Empty dictionary
empty_dict = {}
print(f"Empty dictionary: {empty_dict}, type: {type(empty_dict)}")

# Dictionary for product details
product_details = {
    "name": "SuperWidget X1000",
    "product_id": "SWX1000",
    "price": 49.99,
    "in_stock": True,
    "tags": ["electronics", "new", "gadget"]
}
print(f"Product details: {product_details}")

# Creating with dict() constructor
# From keyword arguments (keys must be valid identifiers)
customer_info = dict(id=123, name="Alice Wonderland", city="New York")
print(f"Customer info (from kwargs): {customer_info}")

# From a list of key-value tuples
item_specs_list = [('color', 'blue'), ('weight_g', 200)]
item_specs_dict = dict(item_specs_list)
print(f"Item specs (from list of tuples): {item_specs_dict}")
```

## Accessing Values
Values are accessed using their corresponding keys within square brackets `[]`. If the key is not found, a `KeyError` is raised.
The `.get()` method can be used to access values safely, allowing a default value if the key is not present.

```python
print(f"Product Name: {product_details['name']}")      # Output: SuperWidget X1000
print(f"Product Price: {product_details['price']}")    # Output: 49.99

# Using .get()
stock_status = product_details.get("in_stock")
print(f"Stock status (get): {stock_status}") # Output: True

manufacturer = product_details.get("manufacturer", "N/A") # Key doesn't exist, returns default
print(f"Manufacturer (get with default): {manufacturer}") # Output: N/A

# Accessing a non-existent key with [] raises KeyError
# print(product_details['color']) # This would raise KeyError
```

## Modifying Dictionaries (Mutable)
-   **Adding or Updating Key-Value Pairs:**
    ```python
    # product_details['color'] = 'Blue' # Adds a new key-value pair
    # product_details['price'] = 54.99  # Updates the value for existing key 'price'
    # print(f"Updated product details: {product_details}")
    ```
-   **Using `update()` method:** Merges another dictionary or an iterable of key-value pairs.
    ```python
    # new_info = {"warranty_years": 2, "origin_country": "USA"}
    # product_details.update(new_info)
    # product_details.update(color="Red", material="Titanium") # Can also use kwargs
    # print(f"After update(): {product_details}")
    ```
-   **Removing Key-Value Pairs:**
    -   `pop(key, default)`: Removes the item with the specified `key` and returns its value. Raises `KeyError` if key is not found and no default is provided.
    -   `popitem()`: Removes and returns an arbitrary (key, value) pair (LIFO order in Python 3.7+). Raises `KeyError` if dict is empty.
    -   `del dict[key]`: Deletes the item with the specified key. Raises `KeyError` if key is not found.
    -   `clear()`: Removes all items from the dictionary.
    ```python
    # removed_tags = product_details.pop("tags", None) # Remove 'tags', return None if not found
    # print(f"Removed tags: {removed_tags}")
    # print(f"Dict after pop('tags'): {product_details}")

    # if "in_stock" in product_details:
    #     del product_details["in_stock"]
    # print(f"Dict after del 'in_stock': {product_details}")

    # last_item_popped = product_details.popitem() # Removes and returns last inserted in 3.7+
    # print(f"Popped item: {last_item_popped}")
    # print(f"Dict after popitem: {product_details}")

    # product_details.clear()
    # print(f"Dict after clear: {product_details}")
    ```

## Iterating Over Dictionaries
See [[Python_Loops_Iteration]]. Common ways:
-   Iterating over keys: `for key in my_dict:`
-   Iterating over values: `for value in my_dict.values():`
-   Iterating over key-value pairs: `for key, value in my_dict.items():`

## Common Dictionary Methods
See [[Python_Dictionary_Methods]] for a detailed list including `keys()`, `values()`, `items()`, `get()`, `update()`, `pop()`, `popitem()`, `clear()`, `setdefault()`, `fromkeys()`.

## Use Cases
Dictionaries are extremely useful for:
-   Storing data that has a natural key-value relationship (e.g., configuration settings, JSON-like objects, representing database records).
-   Counting frequencies of items.
-   Fast lookups by key.
-   Building caches or memoization tables.
-   Representing sparse matrices or graphs (adjacency lists).

Dictionaries are one of Python's most powerful and frequently used data structures due to their flexibility and efficient key-based lookups.

---