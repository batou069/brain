---
tags:
  - python
  - dictionary
  - dict
  - method
  - pop
  - remove
  - mutable
  - data_structures
  - function
aliases:
  - dict.pop()
related:
  - "[[Python_Dictionary]]"
  - "[[Python_Dictionary_Methods]]"
  - "[[Python_dict_popitem]]"
  - "[[Python_Data_Structures_MOC#Deleting Elements from Data Structures|Deleting Elements]]"
worksheet:
  - WS17
date_created: 2025-06-11
---
# Python: `dict.pop(key, default=RAISE_ERROR)`

The `pop()` method is used to remove a specified `key` and return its corresponding value from a [[Python_Dictionary|dictionary]]. If the key is not found, it either raises a `KeyError` or returns a `default` value if provided. This method modifies the original dictionary in-place.

## Syntax```python
dictionary_object.pop(key, default)
```
-   `key`: The key of the item to remove and return.
-   `default` (optional): The value to be returned if the `key` is not found in the dictionary. If this argument is not provided and the key is not found, a `KeyError` is raised.

## Behavior
-   If `key` is present in the dictionary, the key-value pair is removed from the dictionary, and the value associated with `key` is returned.
-   If `key` is not present:
    -   If `default` is specified, `default` is returned, and the dictionary remains unchanged.
    -   If `default` is not specified, a `KeyError` is raised.
-   The original dictionary is modified if the key is found and removed.

## Return Value
-   The value associated with the removed `key`.
-   The `default` value if the key is not found and `default` was specified.
-   Raises `KeyError` if the key is not found and no `default` was specified.

## Examples

**1. Popping an existing key:**
```python
product_settings = {
    "theme": "dark",
    "notifications_enabled": True,
    "language": "en-US",
    "items_per_page": 25
}
print(f"Initial settings: {product_settings}")

# Pop 'language' setting
language_setting = product_settings.pop("language")
print(f"Popped language: '{language_setting}'")
print(f"Settings after popping 'language': {product_settings}")
```
Output:
```
Initial settings: {'theme': 'dark', 'notifications_enabled': True, 'language': 'en-US', 'items_per_page': 25}
Popped language: 'en-US'
Settings after popping 'language': {'theme': 'dark', 'notifications_enabled': True, 'items_per_page': 25}
```

**2. Popping a non-existing key with a default value:**
```python
# Using product_settings from above
user_custom_css = product_settings.pop("custom_css_url", None) # Key doesn't exist, return default (None)
print(f"Custom CSS URL: {user_custom_css}") # Output: None
print(f"Settings remain unchanged: {product_settings}")
# Output: Settings remain unchanged: {'theme': 'dark', 'notifications_enabled': True, 'items_per_page': 25}

# Using a different default
font_preference = product_settings.pop("font_preference", "Arial")
print(f"Font preference: {font_preference}") # Output: Arial
```

**3. Popping a non-existing key without a default (raises KeyError):**
```python
# Using product_settings from above
try:
    admin_role = product_settings.pop("admin_role")
except KeyError as e:
    print(f"Error popping 'admin_role': {e}") # Output: Error popping 'admin_role': 'admin_role'
```

## Use Cases
-   Removing an item from a dictionary while also needing to use its value.
-   Safely removing optional configuration settings or data fields, providing a default if they don't exist.
-   Processing items from a dictionary one by one and removing them as they are processed (though iterating over `items()` and then deleting might be clearer for some patterns if the value isn't immediately needed from `pop`).

## `pop()` vs. `del dict[key]`
-   `dict.pop(key)`: Removes the item and **returns its value**. Can provide a default to avoid `KeyError`.
-   `del dict[key]`: Removes the item but **does not return its value**. Raises `KeyError` if the key is not found.

If you need the value of the item you are removing, `pop()` is the appropriate method. If you just want to delete it and don't need its value, `del` is slightly more direct.

---