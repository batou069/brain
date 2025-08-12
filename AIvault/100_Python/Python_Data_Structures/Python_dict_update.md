---
tags:
  - python
  - dictionary
  - dict
  - method
  - update
  - merge
  - mutable
  - data_structures
  - function
aliases:
  - dict.update()
related:
  - "[[Python_Dictionary]]"
  - "[[Python_Dictionary_Methods]]"
worksheet:
  - WS17
date_created: 2025-06-11
---
# Python: `dict.update(other)`

The `update()` method is used to update a [[Python_Dictionary|dictionary]] with key-value pairs from another dictionary or from an iterable of key-value pairs (like tuples). It can also take keyword arguments to add or update key-value pairs.

This method modifies the original dictionary in-place and returns `None`.

## Syntax
There are several ways to call `update()`:

1.  **With another dictionary:**
    ```python
    dictionary_object.update(other_dictionary)
    ```
2.  **With an iterable of key-value pairs:**
    ```python
    dictionary_object.update(iterable_of_key_value_pairs) 
    # e.g., list_of_tuples = [('key1', 'value1'), ('key2', 'value2')]
    ```
3.  **With keyword arguments:**
    ```python
    dictionary_object.update(key1=value1, key2=value2, ...)
    ```
You can also combine these.

## Behavior
-   If a key from the `other` dictionary (or iterable/keyword arguments) already exists in `dictionary_object`, its value in `dictionary_object` is **updated** with the new value.
-   If a key from `other` does not exist in `dictionary_object`, the key-value pair is **added** to `dictionary_object`.
-   The original `dictionary_object` is modified in-place.

## Return Value
-   `None`. The method modifies the dictionary in-place.

## Examples

**1. Updating with another dictionary:**
```python
# E-commerce product details
product_info = {
    "product_id": "XYZ123",
    "name": "Wireless Mouse",
    "price": 25.99
}
print(f"Initial product_info: {product_info}")

additional_details = {
    "color": "Black",
    "brand": "TechGear",
    "price": 24.99 # This will update the existing price
}
product_info.update(additional_details)
print(f"After update with another dict: {product_info}")
```
Output:
```
Initial product_info: {'product_id': 'XYZ123', 'name': 'Wireless Mouse', 'price': 25.99}
After update with another dict: {'product_id': 'XYZ123', 'name': 'Wireless Mouse', 'price': 24.99, 'color': 'Black', 'brand': 'TechGear'}
```

**2. Updating with an iterable of key-value pairs (e.g., list of tuples):**
```python
customer_profile = {"id": "C001", "status": "Active"}
contact_info = [("email", "customer@example.com"), ("phone", "555-1234")]

customer_profile.update(contact_info)
print(f"Customer profile after update with list of tuples: {customer_profile}")
```
Output:
```
Customer profile after update with list of tuples: {'id': 'C001', 'status': 'Active', 'email': 'customer@example.com', 'phone': '555-1234'}
```

**3. Updating with keyword arguments:**
```python
# Using product_info from example 1
product_info.update(in_stock=True, rating=4.5, price=23.99) # 'price' will be updated again
print(f"After update with kwargs: {product_info}")
```
Output (assuming `product_info` was updated in example 1):
```
After update with kwargs: {'product_id': 'XYZ123', 'name': 'Wireless Mouse', 'price': 23.99, 'color': 'Black', 'brand': 'TechGear', 'in_stock': True, 'rating': 4.5}
```

**4. Combining methods (order of precedence if keys overlap):**
Keyword arguments will override keys from dictionaries or iterables if there's a conflict during the same `update()` call. If multiple dictionaries are merged, the rightmost one takes precedence for overlapping keys.
```python
# Using | or ** for merging (Python 3.9+) - These create NEW dictionaries
dict_a = {'a': 1, 'b': 20}
dict_b = {'b': 2, 'c': 3}

# merged_pipe = dict_a | dict_b # {'a': 1, 'b': 2, 'c': 3} - dict_b's 'b' wins
# print(f"Merged with |: {merged_pipe}")

# merged_unpack = {**dict_a, **dict_b} # {'a': 1, 'b': 2, 'c': 3} - dict_b's 'b' wins
# print(f"Merged with **: {merged_unpack}")

# If using update, the effect is similar but in-place for the first dict
dict_a_copy = dict_a.copy()
dict_a_copy.update(dict_b) # dict_a_copy is now {'a': 1, 'b': 2, 'c': 3}
print(f"dict_a_copy after update: {dict_a_copy}")```

## Use Cases
-   Merging two dictionaries.
-   Adding multiple key-value pairs to an existing dictionary efficiently.
-   Updating existing values in a dictionary based on new information from another source.
-   Setting default configuration values and then overriding them with user-specific settings.

`update()` is a versatile method for modifying a dictionary by incorporating data from another dictionary, an iterable of key-value pairs, or keyword arguments.

---