---
tags:
  - python
  - data_structures
  - dictionary
  - dict
  - methods
  - functions
  - concept
  - summary
aliases:
  - Dictionary Methods Python
  - Python Dict Functions
related:
  - "[[Python_Dictionary]]"
  - "[[100_Python/Python_Data_Structures/_Python_Data_Structures_MOC|_Python_Data_Structures_MOC]]"
  - "[[Python_dict_get]]"
  - "[[Python_dict_keys]]"
  - "[[Python_dict_values]]"
  - "[[Python_dict_items]]"
  - "[[Python_dict_update]]"
  - "[[Python_dict_pop]]"
  - "[[Python_dict_popitem]]"
  - "[[Python_dict_clear]]"
  - "[[Python_dict_setdefault]]"
  - "[[Python_dict_fromkeys]]"
  - "[[Built_In_Functions_Python#len()|len() for dicts]]"
worksheet:
  - WS17
date_created: 2025-06-11
---
# Python: Dictionary Methods Summary

Python [[Python_Dictionary|dictionaries (`dict`)]] are mutable mappings of key-value pairs. They offer a variety of methods for accessing, modifying, and iterating over their contents.

## Accessing Data
[list2tab|#Dict Access Methods]
- Method
    - Description
        - Example
- `get(key, default=None)`
    -   Returns the value for `key` if `key` is in the dictionary, else `default`. If `default` is not given, it defaults to `None`, so this method never raises a `KeyError`.
    -   `price = product.get('price', 0.0)`
- `keys()`
    -   Returns a new **view object** that displays a list of all the keys in the dictionary. The view object is dynamic; changes to the dictionary are reflected in the view.
    -   `all_keys = product.keys()`
    -   `for k in product.keys(): print(k)`
- `values()`
    -   Returns a new **view object** that displays a list of all the values in the dictionary.
    -   `all_values = product.values()`
    -   `for v in product.values(): print(v)`
- `items()`
    -   Returns a new **view object** that displays a list of a dictionary's key-value tuple pairs.
    -   `all_items = product.items()`
    -   `for k, v in product.items(): print(f"{k}: {v}")`

## Modifying Dictionary Content
[list2tab|#Dict Modifying Methods]
- Method
    - Description
        - Mutates Original?
        - Example
- `update(other_dict)` or `update(iterable_of_pairs)` or `update(**kwargs)`
    -   Updates the dictionary with the key-value pairs from `other_dict` or an iterable, overwriting existing keys. Can also take keyword arguments.
    -   Yes
        -   `product.update({'stock': 10, 'color': 'blue'})`
        -   `product.update(price=59.99, on_sale=True)`
- `pop(key, default=RAISE_ERROR)`
    -   Removes the specified `key` and returns its corresponding value. If `key` is not found, `default` is returned if given, otherwise a `KeyError` is raised.
    -   Yes
        -   `color = product.pop('color', 'N/A')`
- `popitem()`
    -   Removes and returns an arbitrary (key, value) pair from the dictionary. In Python 3.7+, items are popped in LIFO (Last-In, First-Out) order. Raises `KeyError` if the dictionary is empty.
    -   Yes
        -   `key, value = product.popitem()`
- `clear()`
    -   Removes all items from the dictionary, making it empty.
    -   Yes
        -   `product.clear()`
- `setdefault(key, default=None)`
    -   If `key` is in the dictionary, return its value. If not, insert `key` with a value of `default` and return `default`. `default` defaults to `None`.
    -   Yes (if key is not present)
        -   `category = product.setdefault('category', 'General')`

## Other Useful Methods and Operations
-   **`fromkeys(seq, value=None)` (Class Method):**
    -   Creates a new dictionary with keys from `seq` and all values set to `value`.
    -   `new_dict = dict.fromkeys(['name', 'email'], 'unknown')`
-   **`copy()`:**
    -   Returns a **shallow copy** of the dictionary.
    -   `copied_dict = product.copy()`
-   **`len(dict)` (Built-in Function):**
    -   Returns the number of key-value pairs in the dictionary.
-   **`key in dict` (Membership Testing):**
    -   Checks if `key` exists in the dictionary. Returns `True` or `False`.
    -   `if 'price' in product: ...`
-   **`del dict[key]` (Statement):**
    -   Deletes the key-value pair with the given `key`. Raises `KeyError` if key is not found. Mutates original.
    -   `del product['old_feature']`

**Example of Common Operations:**
```python
# Conceptual e-commerce product data
product = {
    "name": "Smart Thermostat",
    "brand": "EcoHome",
    "price": 199.99,
    "features": ["WiFi", "Learning", "App Control"]
}
print(f"Initial product: {product}")

# Get a value safely
print(f"Price: {product.get('price', 0.0)}")
print(f"Warranty: {product.get('warranty', 'Not specified')}")

# Get all keys and values
print(f"Keys: {list(product.keys())}") # Convert view to list for printing
print(f"Values: {list(product.values())}")
print(f"Items: {list(product.items())}")

# Update dictionary
product.update({"color": "White", "price": 189.99}) # Update price, add color
print(f"Updated product: {product}")

# Pop an item
removed_feature_list = product.pop("features")
print(f"Removed features: {removed_feature_list}, Product now: {product}")

# Set default if key missing
product.setdefault("rating", 4.5) # Adds 'rating': 4.5 because it wasn't there
product.setdefault("brand", "Generic") # Does nothing, 'brand' already exists
print(f"Product with defaults: {product}")

print(f"Number of entries: {len(product)}")
```

Refer to individual notes for each method (e.g., [[Python_dict_get]], [[Python_dict_keys]]) for more detailed explanations and specific examples.

---