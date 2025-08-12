---
tags:
  - python
  - dictionary
  - dict
  - method
  - values
  - view_object
  - iterable
  - data_structures
  - function
aliases:
  - dict.values()
  - dictionary values
related:
  - "[[Python_Dictionary]]"
  - "[[Python_Dictionary_Methods]]"
  - "[[Python_dict_keys]]"
  - "[[Python_dict_items]]"
  - "[[Python_Loops_Iteration|Looping over Dictionaries]]"
worksheet:
  - WS17
date_created: 2025-06-11
---
# Python: `dict.values()`

The `values()` method of a [[Python_Dictionary|dictionary]] returns a **view object** that displays a list of all the values in the dictionary. This view object provides a dynamic view on the dictionary’s values, meaning that when the dictionary changes, the view reflects these changes.

## Syntax```python
dictionary_object.values()
```
This method takes no arguments.

## Behavior
-   Returns a **dictionary view object** (of type `dict_values`).
-   This view object is iterable, so you can loop over it.
-   It provides a dynamic view; changes to the dictionary's values (or adding/removing items) will be reflected in the `dict_values` object.
-   The order of values in the view object corresponds to the insertion order of their keys in the dictionary (for Python 3.7+). In older Python versions (before 3.6), the order was arbitrary.
-   The view object can contain duplicate values if multiple keys map to the same value.

## Return Value
-   A `dict_values` object containing the values of the dictionary.

## Examples

**1. Getting and iterating over values:**
```python
product_inventory = {
    "LaptopX": 50,
    "MouseY": 120,
    "KeyboardZ": 75,
    "MonitorA": 50 # Duplicate value
}

# Get the values view object
values_view = product_inventory.values()
print(f"Values view object: {values_view}")
# Output (Python 3.7+): dict_values([50, 120, 75, 50])

print("\nIterating over values:")
for stock_count in product_inventory.values():
    print(f"- Stock: {stock_count}")
```
Output for iteration:
```
Iterating over values:
- Stock: 50
- Stock: 120
- Stock: 75
- Stock: 50
```

**2. Converting values view to a list:**
If you need a static list of values at a particular moment, you can convert the view object to a `list`.
```python
stock_levels_list = list(product_inventory.values())
print(f"\nList of stock levels: {stock_levels_list}")
# Output: [50, 120, 75, 50]
```
This list will contain duplicates if they exist in the dictionary's values.

**3. Dynamic nature of the view:**
```python
user_preferences = {"theme": "dark", "notifications": True}
prefs_values_view = user_preferences.values()

print(f"\nInitial preferences values view: {prefs_values_view}")
# Output: dict_values(['dark', True])

# Modify the dictionary
user_preferences["notifications"] = False
user_preferences["font_size"] = 12

print(f"Updated preferences values view: {prefs_values_view}")
# Output: dict_values(['dark', False, 12])
# The view reflects the changes in the dictionary's values.
```

**4. Checking for value existence (though less direct than iterating):**
To check if a specific value exists in the dictionary, you typically iterate or use the `in` operator on the view.
```python
if 120 in product_inventory.values():
    print("\nA stock level of 120 exists.") # Output: A stock level of 120 exists.

if 1000 in product_inventory.values():
    print("A stock level of 1000 exists.")
else:
    print("A stock level of 1000 does NOT exist.") # Output: A stock level of 1000 does NOT exist.
```

Unlike `dict_keys` objects, `dict_values` objects do not directly support set-like operations (like intersection or union) because values can be duplicates and may not all be hashable.

The `values()` method is essential for accessing or iterating over all the values stored in a dictionary, especially when you don't need the corresponding keys.

---