---
tags:
  - python
  - data_structures
  - set
  - frozenset
  - collection
  - unordered
  - unique
  - mutable
  - immutable
  - concept
  - example
aliases:
  - Python Sets
  - Python Frozensets
  - set object
  - frozenset object
related:
  - "[[100_Python/Python_Data_Structures/_Python_Data_Structures_MOC|_Python_Data_Structures_MOC]]"
  - "[[Python_Mutability_Immutability|Mutability and Immutability in Python]]"
  - "[[Python_Loops_Iteration|Looping and Iteration]]"
  - "[[Python_Set_Methods]]"
worksheet:
  - WS17
date_created: 2025-06-11
---
# Python: Sets (`set`) and Frozen Sets (`frozenset`)

## `set` (Mutable Set)
A **set** in Python is an **unordered collection of unique, immutable items**.
-   **Unordered:** The items in a set do not have a defined order. You cannot access items by index. When you iterate over a set or print it, the order of items might vary.
-   **Unique Elements:** Sets automatically enforce uniqueness; duplicate items are not stored.
-   **Mutable:** You can add or remove items from a set after it's created.
-   **Elements Must Be Immutable:** Items within a set must be of an immutable type (e.g., numbers, strings, tuples containing only immutable elements). You cannot have a list or another set as an element of a set directly (because lists/sets are mutable).

**Creating Sets:**
-   Using curly braces `{}` with comma-separated items.
-   Using the `set()` constructor with an iterable.
-   **Important:** To create an empty set, you **must** use `set()`. Using `{}` creates an empty dictionary.

```python
# Creating sets
unique_product_tags = {"electronics", "sale", "new", "gadget", "sale"} # Duplicates ignored
print(f"Unique product tags: {unique_product_tags}")
# Output might be {'new', 'gadget', 'electronics', 'sale'} - order is not guaranteed

numbers_set = set([1, 2, 2, 3, 4, 4, 4, 5])
print(f"Set from list: {numbers_set}") # Output: {1, 2, 3, 4, 5}

empty_set_correct = set()
print(f"Empty set: {empty_set_correct}, type: {type(empty_set_correct)}")

# This creates an empty dictionary, NOT a set:
# empty_dict_wrong = {} 
# print(f"Empty dict: {empty_dict_wrong}, type: {type(empty_dict_wrong)}")
```

**Common Set Operations and Methods:**
See [[Python_Set_Methods]] for a detailed list and examples of methods like `add()`, `remove()`, `discard()`, `pop()`, `clear()`, `union()`, `intersection()`, `difference()`, `issubset()`, `issuperset()`, etc.

**Use Cases for `set`:**
-   **Removing Duplicates:** Quickly get unique items from a list or other iterable: `unique_items = list(set(my_list))`.
-   **Membership Testing:** Checking if an item exists in a collection is very fast with sets (average $O(1)$ time complexity) due to their hash-table based implementation.
    ```python
    # available_features = {"bluetooth", "wifi", "gps", "nfc"}
    # print(f"Is 'wifi' available? {'wifi' in available_features}") # True
    # print(f"Is '5g' available? {'5g' in available_features}")   # False
    ```
-   **Mathematical Set Operations:** Performing union, intersection, difference, symmetric difference between collections.
    ```python
    # features_product_A = {"bluetooth", "wifi", "camera"}
    # features_product_B = {"wifi", "gps", "nfc", "camera"}

    # common_features = features_product_A.intersection(features_product_B)
    # print(f"Common features: {common_features}") # {'wifi', 'camera'}

    # all_unique_features = features_product_A.union(features_product_B)
    # print(f"All unique features: {all_unique_features}")
    ```

## `frozenset` (Immutable Set)
A **frozenset** is an **immutable version of a set**. Once created, its contents cannot be changed (no adding or removing elements).
-   **Creation:** Using the `frozenset()` constructor with an iterable.
-   **Properties:**
    -   Unordered, unique elements.
    -   Immutable.
    -   Because they are immutable and hashable, `frozenset` objects **can be used as elements in other sets or as keys in dictionaries**. Regular `set` objects cannot, as they are mutable.

```python
# Creating frozensets
frozen_categories = frozenset(["electronics", "books", "apparel"])
print(f"Frozen categories: {frozen_categories}")

# Attempting to modify a frozenset will raise an AttributeError
# frozen_categories.add("home") # This would cause an AttributeError

# Using frozenset as a dictionary key (e.g., for product feature combinations)
# feature_set_stats = {
#     frozenset({"wifi", "bluetooth"}): {"count": 150, "avg_price": 299.99},
#     frozenset({"gps", "nfc"}): {"count": 80, "avg_price": 450.50}
# }
# key_to_lookup = frozenset({"bluetooth", "wifi"}) # Order doesn't matter for the key itself
# print(f"Stats for wifi & bluetooth: {feature_set_stats.get(key_to_lookup)}")
```

>[!question] What is a "Frozen Set"?
>A **frozenset** is an immutable, hashable, unordered collection of unique elements. It has the same properties as a regular `set` (uniqueness of elements, support for set operations like union, intersection, etc.) except that its contents cannot be modified after creation.
>
>The primary reason for `frozenset`'s existence is its **immutability**, which makes it **hashable**. This allows `frozenset` objects to be used in contexts where mutable `set` objects cannot, such as:
>1.  **Elements of another `set`:**
>    ```python
>    set_of_frozensets = {frozenset({1,2}), frozenset({2,3})}
>    # set_of_sets = {{1,2}, {2,3}} # This would raise a TypeError: unhashable type: 'set'
>    ```
>2.  **Keys in a `dict`:**
>    ```python
>    # config_options = {
>    #     frozenset({'optionA', 'optionB'}): "Setting1",
>    #     frozenset({'optionC'}): "Setting2"
>    # }
>    # print(config_options[frozenset({'optionB', 'optionA'})]) # Access using equivalent frozenset
>    ```
>
>Essentially, if you need a set-like collection (unique, unordered items) but also need it to be immutable (e.g., to use it as a dictionary key or in another set), you use `frozenset`.

**When to use `set` vs. `frozenset`:**
-   Use `set` when you need a collection of unique items and you anticipate needing to add or remove items after creation.
-   Use `frozenset` when you need an immutable set, typically because you need to use it as a dictionary key, an element in another set, or to ensure its contents remain constant.

Both `set` and `frozenset` are highly efficient for membership testing and removing duplicates.

---