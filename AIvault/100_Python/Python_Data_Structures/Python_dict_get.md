---
tags:
  - python
  - dictionary
  - dict
  - method
  - get
  - access
  - key_value
  - data_structures
  - function
aliases:
  - dict.get()
related:
  - "[[Python_Dictionary]]"
  - "[[Python_Dictionary_Methods]]"
  - "[[Python_dict_setdefault|dict.setdefault()]]"
worksheet:
  - WS17
date_created: 2025-06-11
---
# Python: `dict.get(key, default=None)`

The `get()` method is used to access the value associated with a specified `key` in a [[Python_Dictionary|dictionary]]. A key advantage of `get()` over standard square bracket indexing (`dict[key]`) is that it allows you to provide a **default value** to be returned if the key is not found, thus avoiding a `KeyError`.

## Syntax```python
dictionary_object.get(key, default)
```
-   `key`: The key whose associated value is to be retrieved.
-   `default` (optional): The value to be returned if the `key` is not found in the dictionary. If this argument is not provided and the key is not found, `get()` returns `None`.

## Behavior
-   If `key` is present in the dictionary, its corresponding value is returned.
-   If `key` is not present in the dictionary:
    -   If `default` is specified, the `default` value is returned.
    -   If `default` is not specified, `None` is returned.
-   This method does **not** modify the original dictionary.
-   It does **not** raise a `KeyError` if the key is missing (unlike `dictionary_object[key]`).

## Return Value
-   The value associated with `key` if the key is found.
-   The `default` value if the key is not found and `default` is specified.
-   `None` if the key is not found and `default` is not specified.

## Examples

**1. Accessing existing and non-existing keys:**
```python
product_config = {
    "name": "Wireless Mouse X5",
    "price": 24.99,
    "color": "Black",
    "stock_available": True
}

# Accessing an existing key
price = product_config.get("price")
print(f"Price: {price}") # Output: 24.99

# Accessing a non-existing key without a default
manufacturer = product_config.get("manufacturer")
print(f"Manufacturer (no default): {manufacturer}") # Output: None

# Accessing a non-existing key with a default value
warranty = product_config.get("warranty_period", "1 year standard")
print(f"Warranty Period: {warranty}") # Output: 1 year standard
```

**2. Using `get()` in conditional logic or to provide fallbacks:**
This is useful for safely accessing potentially missing configuration options or optional data fields.
```python
# Conceptual e-commerce item data
item_data = {"item_id": "A123", "discount_percentage": 0.10} # 'on_sale' key is missing

# Check if item is on sale, default to False if key not present
is_on_sale = item_data.get("on_sale", False) 
print(f"Item A123 on sale: {is_on_sale}") # Output: False

# Get discount, default to 0.0 if key not present
discount = item_data.get("discount_percentage", 0.0)
print(f"Item A123 discount: {discount}") # Output: 0.1
```

**3. Comparison with square bracket indexing `[]`:**
```python
product_config = {"name": "Keyboard K100", "price": 75.00}

# Using get() for a missing key
shipping_cost = product_config.get("shipping_cost")
print(f"Shipping cost (using get()): {shipping_cost}") # Output: None

# Using [] for a missing key - this would raise KeyError
try:
    shipping_cost_bracket = product_config["shipping_cost"]
except KeyError as e:
    print(f"Error with bracket access: {e}") # Output: Error with bracket access: 'shipping_cost'
```

## When to Use `get()`
-   When you are not sure if a key exists in a dictionary and want to avoid a `KeyError`.
-   When you want to provide a default value if a key is missing.
-   For writing more robust code that can handle missing optional keys gracefully.

If you are certain a key exists, or if its absence represents an error condition that should halt execution (or be caught by a broader `try-except KeyError`), then direct square bracket access (`dict[key]`) might be appropriate. Otherwise, `get()` is often a safer and more convenient choice.

---