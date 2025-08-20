---
tags:
  - python
  - data_structures
  - list
  - tuple
  - set
  - dictionary
  - order
  - sequence
  - concept_comparison
aliases:
  - Ordered Data Structures Python
  - Unordered Data Structures Python
  - Python Collection Order
related:
  - "[[100_Python/Python_Data_Structures/_Python_Data_Structures_MOC|_Python_Data_Structures_MOC]]"
  - "[[Python_List]]"
  - "[[Python_Tuple]]"
  - "[[Python_Set_Frozenset|Python Set and Frozenset]]"
  - "[[Python_Dictionary]]"
worksheet:
  - WS17
date_created: 2025-08-20
---
# Python: Ordered vs. Unordered Data Structures

Python's built-in data structures can be categorized based on whether they maintain the order of their elements.

>[!question] List the ordered and the unordered data structures.

## Ordered Data Structures
**Ordered data structures** preserve the order in which items were inserted. When you iterate over them or access elements by index (if applicable), you get them back in that same defined sequence.

1.  **[[Python_List|Lists (`list`)]]**
    -   **Definition:** `my_list = `
    -   **Order:** Inherently ordered. Elements are stored in a sequence, and this sequence is maintained. You can access elements by their numerical index (e.g., `my_list`, `my_list`).
    -   **Example:**
        ```python
        product_order = ["Laptop", "Mouse", "Keyboard"]
        # Iterating will always give "Laptop", then "Mouse", then "Keyboard"
        # for item in product_order:
        #     print(item)
        # print(product_order[0]) # Always "Laptop"
        ```

2.  **[[Python_Tuple|Tuples (`tuple`)]]**
    -   **Definition:** `my_tuple = ("alpha", "beta", "gamma")`
    -   **Order:** Inherently ordered, just like lists. Elements are stored in a sequence and accessed by index.
    -   **Example:**
        ```python
        coordinates = (10.5, 20.3, 5.0) # x, y, z
        # print(coordinates[1]) # Always 20.3
        ```

3.  **[[Python_Primitive_Types|Strings (`str`)]]**
    -   **Definition:** `my_string = "hello"`
    -   **Order:** Strings are sequences of characters, and their order is fundamental.
    -   **Example:**
        ```python
        # print(my_string[0]) # Always 'h'
        ```

4.  **[[Python_Dictionary|Dictionaries (`dict`)]] (Python 3.7+ and CPython 3.6+)**
    -   **Definition:** `my_dict = {"name": "Alice", "age": 30}`
    -   **Order:**
        -   **Python 3.7+:** Dictionaries are guaranteed to preserve insertion order. When you iterate over a dictionary (e.g., its keys, values, or items), they will appear in the order they were added.
        -   **CPython 3.6:** This version also implemented insertion order preservation as an implementation detail, which became official in 3.7.
        -   **Python < 3.6:** Dictionaries were unordered. The order of items could be arbitrary and might change during operations. For ordered dictionaries in older Python, `collections.OrderedDict` was used.
    -   **Example (Python 3.7+):**
        ```python
        # product_config = {"color": "blue", "size": "M", "material": "cotton"}
        # product_config["in_stock"] = True # Added last

        # print("Keys in insertion order (Python 3.7+):")
        # for key in product_config:
        #     print(key)
        # Output:
        # color
        # size
        # material
        # in_stock
        ```

## Unordered Data Structures
**Unordered data structures** do not maintain any specific order for their elements. The concept of a "first" or "second" element is not well-defined, and iterating over them might yield elements in a different sequence each time or in an order based on internal hashing mechanisms rather than insertion.

1.  **[[Python_Set_Frozenset|Sets (`set`)]]**
    -   **Definition:** `my_set = {1, "apple", 3.14}` or `my_set = set()`
    -   **Order:** Inherently unordered. Sets are implemented using hash tables, and the internal storage order is optimized for efficient membership testing and uniqueness, not for preserving insertion sequence.
    -   You cannot access elements by index.
    -   **Example:**
        ```python
        # customer_tags = {"vip", "new_customer", "newsletter_subscriber"}
        # print(f"Customer tags set: {customer_tags}")
        # The output order might be different each time or across Python versions/runs, e.g.:
        # {'newsletter_subscriber', 'vip', 'new_customer'} or
        # {'vip', 'new_customer', 'newsletter_subscriber'}

        # print("\nIterating over the set (order not guaranteed):")
        # for tag in customer_tags:
        #     print(tag)
        ```

2.  **[[Python_Set_Frozenset|Frozen Sets (`frozenset`)]]**
    -   **Definition:** `my_fset = frozenset([1, "apple", 3.14])`
    -   **Order:** Inherently unordered, just like regular sets.

3.  **[[Python_Dictionary|Dictionaries (`dict`)]] (Python < 3.6, or non-CPython 3.6 implementations)**
    -   As mentioned above, dictionaries were unordered before Python 3.7 (officially). If working with older Python versions, you should assume dictionaries are unordered.

## Summary Table

[list2mdtable|#Order in Python Data Structures]
- Data Structure
    - Ordered?
        - Notes
- `list`
    - Yes
        - Order of insertion is preserved. Indexable.
- `tuple`
    - Yes
        - Order of insertion is preserved. Indexable.
- `str`
    - Yes
        - Sequence of characters. Indexable.
- `dict`
    - Yes (Python 3.7+)
        - Preserves insertion order.
    - No (Python < 3.6 generally)
        - Use `collections.OrderedDict` for guaranteed order in older Python.
- `set`
    - No
        - Elements are unique; order is not guaranteed and not indexable.
- `frozenset`
    - No
        - Immutable version of set; order is not guaranteed and not indexable.

Understanding whether a data structure is ordered or unordered is important for predicting its behavior during iteration, indexing (if applicable), and for operations where sequence matters.

---