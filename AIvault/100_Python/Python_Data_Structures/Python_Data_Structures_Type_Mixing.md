---
tags:
  - python
  - data_structures
  - list
  - tuple
  - set
  - dictionary
  - data_types
  - heterogeneous
  - concept
aliases:
  - Mixed Types in Python Collections
  - Heterogeneous Data Structures Python
related:
  - "[[100_Python/Python_Data_Structures/_Python_Data_Structures_MOC|_Python_Data_Structures_MOC]]"
  - "[[Python_List]]"
  - "[[Python_Tuple]]"
  - "[[Python_Set_Frozenset|Python Set and Frozenset]]"
  - "[[Python_Dictionary]]"
  - "[[Python_Primitive_Types]]"
worksheet:
  - WS17
date_created: 2025-08-20
---
# Python: Mixing Element Types in Data Structures

A key feature of Python's built-in collection types like lists, tuples, sets, and dictionaries is their ability to hold elements of different data types. This makes them very flexible for representing diverse data.

>[!question] Can you mix all types of elements in all data structures?

**General Answer:** Yes, for the most part, Python's primary built-in data structures (`list`, `tuple`, `dict` values, `set` elements) allow you to store items of mixed data types. However, there are important caveats, especially concerning mutability for dictionary keys and set elements.

[list2tab|#Type Mixing by Data Structure]
- [[Python_List|Lists (`list`)]]
    -   **Can Mix Types?** Yes, absolutely.
    -   **Explanation:** Lists are ordered sequences and can store any combination of Python objects, regardless of their type.
    -   **Example (Product details with mixed types):**
        ```python
        product_A_details = [
            "SuperWidget X1000",  # str (name)
            "SWX1000",            # str (SKU)
            49.99,                # float (price)
            150,                  # int (stock_count)
            True,                 # bool (is_available)
            ["electronics", "gadget", "new"] # list (tags)
        ]
        print(f"Product A details list: {product_A_details}")
        for item in product_A_details:
            print(f"- Item: {item}, Type: {type(item)}")
        ```
- [[Python_Tuple|Tuples (`tuple`)]]
    -   **Can Mix Types?** Yes, absolutely.
    -   **Explanation:** Tuples are ordered, immutable sequences. Like lists, they can store elements of any data type.
    -   **Example (Customer record):**
        ```python
        customer_record = (
            1025,                     # int (customer_id)
            "Alice Wonderland",       # str (name)
            30,                       # int (age)
            "alice@example.com",      # str (email)
            ("123 Main St", "Anytown") # tuple (address components)
        )
        print(f"\nCustomer record tuple: {customer_record}")
        ```
- [[Python_Dictionary|Dictionaries (`dict`)]]
    -   **Keys:**
        -   **Can Mix Types?** Yes, keys can be of different immutable types within the same dictionary.
        -   **Constraint:** Dictionary keys **must be of an immutable (hashable) type**. This includes numbers, strings, tuples (if all their elements are immutable), and frozensets. You cannot use mutable types like lists or other dictionaries as keys.
    -   **Values:**
        -   **Can Mix Types?** Yes, absolutely. Values associated with keys can be of any data type, and different keys can have values of different types.
    -   **Example (E-commerce order information):**
        ```python
        order_info = {
            "order_id": "ORD789",           # str key, str value
            123: "Customer Account",      # int key, str value
            "total_amount": 127.50,         # str key, float value
            "items_ordered": ["P101", "P203"], # str key, list value
            "is_shipped": False,            # str key, bool value
            ("ship_to_country", "ship_to_zip"): ("USA", "90210") # tuple key, tuple value
        }
        print(f"\nOrder info dictionary: {order_info}")
        # print(f"Key 'order_id' type: {type('order_id')}, Value type: {type(order_info['order_id'])}")
        # print(f"Key 123 type: {type(123)}, Value type: {type(order_info)}")
        ```
- [[Python_Set_Frozenset|Sets (`set`)]]
    -   **Can Mix Types?** Yes, elements in a set can be of different immutable types.
    -   **Constraint:** Like dictionary keys, elements of a set **must be of an immutable (hashable) type**. You cannot add a list or another (mutable) set as an element to a set. You can add tuples (if all their elements are immutable) or frozensets.
    -   **Example (Collection of unique identifiers and properties):**
        ```python
        mixed_set = {
            101,                      # int
            "product_sku_abc",        # str
            3.14,                     # float
            True,                     # bool
            ("user_id", 1001),        # tuple
            frozenset({"tag1", "tag2"}) # frozenset
        }
        # mixed_set.add([]) # This would raise TypeError: unhashable type: 'list'
        print(f"\nMixed set: {mixed_set}")
        ```
- [[Python_Set_Frozenset|Frozen Sets (`frozenset`)]]
    -   **Can Mix Types?** Yes, same rules as `set`: elements can be of different immutable types.
    -   **Constraint:** Elements must be immutable. The `frozenset` itself is immutable after creation.
    -   **Example:**
        ```python
        mixed_frozenset = frozenset([1, "config_value", (True, None)])
        print(f"\nMixed frozenset: {mixed_frozenset}")
        ```

## Implications of Type Mixing
-   **Flexibility:** The ability to mix types makes Python's data structures very adaptable for representing real-world data which is often heterogeneous.
-   **Type Checking:** When iterating or accessing elements, you might need to check the type of an element using `isinstance()` if your processing logic depends on the type.
    ```python
    # mixed_data_list = [1, "hello",, {"a":5}, 3.14]
    # for item in mixed_data_list:
    #     if isinstance(item, int):
    #         print(f"Integer: {item * 2}")
    #     elif isinstance(item, str):
    #         print(f"String: {item.upper()}")
    #     else:
    #         print(f"Other type ({type(item)}): {item}")
    ```
-   **Operations:** Not all operations are valid for all types within a mixed collection. For example, you can't sum a list of mixed strings and numbers directly without conversion. Sorting a list of mixed, incomparable types will raise a `TypeError`.

While Python allows mixing types in its collections, it's often good practice to have collections with homogeneous types (all elements of the same type) if the subsequent processing expects uniformity, as this can simplify code and reduce the need for type checking. However, the flexibility to mix types is a powerful feature when needed.

---