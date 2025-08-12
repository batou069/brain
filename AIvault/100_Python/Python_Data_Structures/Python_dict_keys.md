---
tags:
  - python
  - dictionary
  - dict
  - method
  - keys
  - view_object
  - iterable
  - data_structures
  - function
aliases:
  - dict.keys()
  - dictionary keys
related:
  - "[[Python_Dictionary]]"
  - "[[Python_Dictionary_Methods]]"
  - "[[Python_dict_values]]"
  - "[[Python_dict_items]]"
  - "[[Python_Loops_Iteration|Looping over Dictionaries]]"
worksheet:
  - WS17
date_created: 2025-06-11
---
# Python: `dict.keys()`

The `keys()` method of a [[Python_Dictionary|dictionary]] returns a **view object** that displays a list of all the keys in the dictionary. This view object provides a dynamic view on the dictionary’s keys, meaning that when the dictionary changes, the view reflects these changes.

## Syntax```python
dictionary_object.keys()
```
This method takes no arguments.

## Behavior
-   Returns a **dictionary view object** (of type `dict_keys`).
-   This view object is iterable, so you can loop over it.
-   It provides a dynamic view, so changes to the original dictionary (e.g., adding or removing keys) will be reflected in the `dict_keys` object.
-   The order of keys in the view object is the insertion order of keys in the dictionary (for Python 3.7+). In older Python versions (before 3.6), the order was arbitrary.

## Return Value
-   A `dict_keys` object containing the keys of the dictionary.

## Examples

**1. Getting and iterating over keys:**
```python
product_specs = {
    "name": "Wireless Earbuds Pro",
    "brand": "AudioPhile",
    "color": "Midnight Blue",
    "bluetooth_version": 5.2,
    "battery_life_hours": 8
}

# Get the keys view object
keys_view = product_specs.keys()
print(f"Keys view object: {keys_view}")
# Output (Python 3.7+): dict_keys(['name', 'brand', 'color', 'bluetooth_version', 'battery_life_hours'])

print("\nIterating over keys:")
for key in product_specs.keys(): # Or simply: for key in product_specs:
    print(f"- {key}")
```
Output for iteration:
```
Iterating over keys:
- name
- brand
- color
- bluetooth_version
- battery_life_hours
```

**2. Converting keys view to a list:**
If you need a static list of keys at a particular moment (e.g., to modify it without affecting the dictionary or the view), you can convert the view object to a `list`.
```python
keys_list = list(product_specs.keys())
print(f"\nList of keys: {keys_list}")
# Output: ['name', 'brand', 'color', 'bluetooth_version', 'battery_life_hours']
```

**3. Dynamic nature of the view:**
```python
customer_profile = {"id": "CUST001", "email": "customer@example.com"}
profile_keys_view = customer_profile.keys()

print(f"\nInitial profile keys view: {profile_keys_view}")
# Output: dict_keys(['id', 'email'])

# Modify the dictionary
customer_profile["loyalty_status"] = "Gold"
del customer_profile["email"]

print(f"Updated profile keys view: {profile_keys_view}")
# Output: dict_keys(['id', 'loyalty_status'])
# The view reflects the changes in the dictionary.
```

**4. Checking for key existence (though `in` operator is more direct):**
```python
# While you can do this, using the 'in' operator is more Pythonic and efficient.
if "price" in product_specs.keys(): # Same as: if "price" in product_specs:
    print("\n'price' is a key in product_specs.")
else:
    print("\n'price' is NOT a key in product_specs.")
```

## Set-like Operations on Keys Views (Python 3)
Dictionary key views (`dict_keys`) support some set-like operations directly if the keys are hashable (which they always are):
-   `&` (intersection)
-   `|` (union)
-   `-` (difference)
-   `^` (symmetric difference)

```python
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 20, "c": 30, "d": 40}

keys1 = dict1.keys()
keys2 = dict2.keys()

common_keys = keys1 & keys2 # Intersection
print(f"\nCommon keys: {common_keys}") # Output: {'c', 'b'} (order might vary for set)

all_unique_keys = keys1 | keys2 # Union
print(f"All unique keys: {all_unique_keys}") # Output: {'d', 'c', 'a', 'b'}
```

The `keys()` method is fundamental for accessing or iterating over the keys of a dictionary, providing a dynamic and efficient way to work with the dictionary's structure.

---