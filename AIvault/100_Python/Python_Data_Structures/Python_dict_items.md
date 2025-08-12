---
tags:
  - python
  - dictionary
  - dict
  - method
  - items
  - view_object
  - iterable
  - key_value_pair
  - data_structures
  - function
aliases:
  - dict.items()
  - dictionary items
  - key-value pairs python
related:
  - "[[Python_Dictionary]]"
  - "[[Python_Dictionary_Methods]]"
  - "[[Python_dict_keys]]"
  - "[[Python_dict_values]]"
  - "[[Python_Loops_Iteration|Looping over Dictionaries]]"
worksheet:
  - WS17
date_created: 2025-06-11
---
# Python: `dict.items()`

The `items()` method of a [[Python_Dictionary|dictionary]] returns a **view object** that displays a list of a dictionary's key-value tuple pairs. This view object provides a dynamic view on the dictionary’s items, meaning that when the dictionary changes, the view reflects these changes.

## Syntax```python
dictionary_object.items()
```This method takes no arguments.

## Behavior
-   Returns a **dictionary view object** (of type `dict_items`).
-   Each element in this view is a **tuple** of the form `(key, value)`.
-   The view object is iterable, making it very common for looping through both keys and values of a dictionary simultaneously.
-   It provides a dynamic view; changes to the original dictionary (e.g., adding, removing, or updating items) will be reflected in the `dict_items` object.
-   The order of items in the view object corresponds to the insertion order in the dictionary (for Python 3.7+). In older Python versions (before 3.6), the order was arbitrary.

## Return Value
-   A `dict_items` object containing the key-value tuple pairs of the dictionary.

## Examples

**1. Getting and iterating over items (key-value pairs):**
```python
product_attributes = {
    "product_id": "XYZ123",
    "name": "Premium Coffee Beans",
    "origin": "Colombia",
    "weight_grams": 500,
    "in_stock": True
}

# Get the items view object
items_view = product_attributes.items()
print(f"Items view object: {items_view}")
# Output (Python 3.7+): 
# dict_items([('product_id', 'XYZ123'), ('name', 'Premium Coffee Beans'), ('origin', 'Colombia'), 
# ('weight_grams', 500), ('in_stock', True)])

print("\nIterating over key-value pairs:")
for key, value in product_attributes.items(): # Common unpacking pattern
    print(f"- Key: '{key}', Value: {value}")
```
Output for iteration:
```
Iterating over key-value pairs:
- Key: 'product_id', Value: XYZ123
- Key: 'name', Value: Premium Coffee Beans
- Key: 'origin', Value: Colombia
- Key: 'weight_grams', Value: 500
- Key: 'in_stock', Value: True
```

**2. Converting items view to a list of tuples:**
If you need a static list of key-value pairs at a particular moment, you can convert the view object to a `list`.
```python
items_list = list(product_attributes.items())
print(f"\nList of (key, value) tuples: {items_list}")
# Output: [('product_id', 'XYZ123'), ('name', 'Premium Coffee Beans'), ...]
```

**3. Dynamic nature of the view:**
```python
user_settings = {"theme": "light", "language": "en"}
settings_items_view = user_settings.items()

print(f"\nInitial settings items view: {settings_items_view}")
# Output: dict_items([('theme', 'light'), ('language', 'en')])

# Modify the dictionary
user_settings["language"] = "fr"
user_settings["notifications"] = "on"
del user_settings["theme"]

print(f"Updated settings items view: {settings_items_view}")
# Output: dict_items([('language', 'fr'), ('notifications', 'on')])
# The view reflects the changes in the dictionary.
```

## Use Cases
-   **Iterating through Keys and Values:** This is the most common use case. The `for key, value in my_dict.items():` pattern is idiomatic Python for processing dictionary content.
-   **Creating Dictionaries from other Dictionaries (with modifications):**
    ```python
    # Example: Create a new dictionary with prices increased by 10%
    # product_prices = {"laptop": 1200, "mouse": 25, "keyboard": 75}
    # increased_prices = {name: price * 1.10 for name, price in product_prices.items()}
    # print(f"\nIncreased prices: {increased_prices}")
    ```
-   **Filtering Dictionaries into New Dictionaries:**
    ```python
    # Example: Create a dictionary of only expensive products
    # expensive_products = {name: price for name, price in product_prices.items() if price > 100}
    # print(f"Expensive products: {expensive_products}")
    ```
-   **Set-like Operations on Items Views (Python 3):**
    Dictionary item views (`dict_items`) support some set-like operations if their items (key-value tuples) are hashable.
    ```python
    # dict1 = {"a": 1, "b": 2}
    # dict2 = {"b": 2, "c": 3} # Note: ("b", 2) is common
    # dict3 = {"b": 20, "c": 3} # ("b", 20) is different from ("b",2)

    # items1 = dict1.items()
    # items2 = dict2.items()
    # items3 = dict3.items()

    # common_items_1_2 = items1 & items2 # Intersection
    # print(f"\nCommon items between dict1 and dict2: {common_items_1_2}") # {('b', 2)}

    # common_items_1_3 = items1 & items3
    # print(f"Common items between dict1 and dict3: {common_items_1_3}") # set() (empty)
    ```

The `items()` method provides a convenient and efficient way to work with both the keys and values of a dictionary simultaneously.

---