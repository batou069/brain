---
tags:
  - python
  - data_structures
  - tuple
  - sequence
  - immutable
  - ordered
  - concept
  - example
aliases:
  - Python Tuples
  - tuple object
related:
  - "[[100_Python/Python_Data_Structures/_Python_Data_Structures_MOC|_Python_Data_Structures_MOC]]"
  - "[[Python_Mutability_Immutability|Mutability and Immutability in Python]]"
  - "[[Python_List]]"
  - "[[Python_Slicing]]"
  - "[[Python_Loops_Iteration|Looping and Iteration]]"
worksheet:
  - WS17
date_created: 2025-06-11
---
# Python: Tuples (`tuple`)

A **tuple** in Python is an **ordered, immutable sequence** of items. This means:
-   **Ordered:** The items in a tuple are stored in a specific sequence, and this order is preserved.
-   **Immutable:** Once a tuple is created, its contents **cannot be changed**. You cannot add, remove, or modify items in place.
-   **Sequence:** Supports indexing, slicing, and iteration.
-   Tuples can contain items of **mixed data types**.

## Creating Tuples
Tuples are created using parentheses `()`, with items separated by commas. A tuple with a single element requires a trailing comma.

```python
# Empty tuple
empty_tuple = ()
print(f"Empty tuple: {empty_tuple}, type: {type(empty_tuple)}")

# Tuple of integers (e.g., RGB color values)
rgb_color = (255, 128, 0) # Orange
print(f"RGB color tuple: {rgb_color}")

# Tuple of strings (e.g., product coordinates)
product_location = ("Warehouse A", "Shelf 3", "Bin 7")
print(f"Product location: {product_location}")

# Tuple with mixed data types
product_info_tuple = ("WidgetX", 1001, 49.99, True) # Name, ID, Price, InStock
print(f"Mixed info tuple: {product_info_tuple}")

# Single element tuple (requires a trailing comma)
single_item_tuple = ("Electronics",) 
print(f"Single item tuple: {single_item_tuple}, type: {type(single_item_tuple)}")
# Without the comma, ('Electronics') would be just a string in parentheses.

# Tuple created using the tuple() constructor (e.g., from a list or string)
tuple_from_list = tuple([1, "apple", 3.0])
print(f"Tuple from list: {tuple_from_list}")
tuple_from_string = tuple("hello")
print(f"Tuple from string: {tuple_from_string}") # Output: ('h', 'e', 'l', 'l', 'o')
```

## Accessing Elements (Indexing)
Tuple elements are accessed using zero-based indexing, just like lists.
-   `my_tuple[0]` is the first element.
-   `my_tuple[-1]` is the last element.

```python
point_3d = (10, 20, 30) # x, y, z coordinates
x_coord = point_3d
z_coord = point_3d

print(f"X-coordinate: {x_coord}") # Output: 10
print(f"Z-coordinate: {z_coord}") # Output: 30

# Attempting to modify an element will raise a TypeError because tuples are immutable
# point_3d = 15 # This would cause: TypeError: 'tuple' object does not support item assignment
```

## Slicing Tuples
[[Python_Slicing|Slicing]] works the same way for tuples as it does for lists, returning a *new* tuple.
`my_tuple[start:stop:step]`

```python
numbers_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
sub_tuple = numbers_tuple[2:5]
print(f"numbers_tuple[2:5] = {sub_tuple}") # Output: (2, 3, 4)

first_three_tuple = numbers_tuple[:3]
print(f"numbers_tuple[:3] = {first_three_tuple}") # Output: (0, 1, 2)
```

## Tuple Packing and Unpacking
-   **Packing:** Creating a tuple by assigning a sequence of values to a single variable.
    ```python
    product_details = "Laptop Pro", "Electronics", 1299.99 # Tuple packing
    print(f"Packed tuple: {product_details}")
    ```
-   **Unpacking:** Assigning the elements of a tuple to multiple variables. The number of variables must match the number of elements in the tuple.
    ```python
    name, category, price = product_details # Tuple unpacking
    print(f"Name: {name}, Category: {category}, Price: {price}")
    ```
    This is very useful for returning multiple values from a function.

>[!question] How do you switch two variables, in one line of code? Can you do it for more than two variables? How does it work?
>Yes, Python allows for elegant swapping of variables in one line using tuple packing and unpacking.
>
>```python
>a = 10
>b = 20
>print(f"Before swap: a = {a}, b = {b}")
>
>a, b = b, a # One-line swap
>
>print(f"After swap: a = {a}, b = {b}") # Output: a = 20, b = 10
>```
>   **Can you do it for more than two variables?**
>   Yes, you can extend this to more variables:
>```python
>x, y, z = 1, 2, 3
>print(f"Before: x={x}, y={y}, z={z}")
>x, y, z = z, x, y # Cyclic shift
>print(f"After: x={x}, y={y}, z={z}") # Output: x=3, y=1, z=2
>```
>   **How does it work?**
>   1.  On the right-hand side (`b, a` or `z, x, y`), Python first evaluates all expressions and creates a **temporary tuple** containing these values. For `a, b = b, a`, it creates `(value_of_b, value_of_a)`.
>   2.  Then, this temporary tuple is **unpacked**, and its elements are assigned to the variables on the left-hand side in order. So, `a` gets the first element of the temporary tuple (which was `value_of_b`), and `b` gets the second element (which was `value_of_a`).
>   This all happens effectively simultaneously from the programmer's perspective, avoiding the need for a temporary variable like in some other languages (`temp = a; a = b; b = temp;`).

## Common Tuple Methods
Tuples have fewer built-in methods than lists because they are immutable.
-   **`count(item)`:** Returns the number of times `item` appears in the tuple.
-   **`index(item, start=0, end=len(tuple))`:** Returns the zero-based index of the first occurrence of `item`. Raises `ValueError` if not found.

```python
my_tuple_methods = (1, 'a', 'b', 'a', 3, 'a')
count_a = my_tuple_methods.count('a')
print(f"Count of 'a': {count_a}") # Output: 3

index_b = my_tuple_methods.index('b')
print(f"Index of 'b': {index_b}") # Output: 2
```

## Use Cases for Tuples
-   **Representing Fixed Collections:** When you have a collection of items that should not change (e.g., coordinates `(x,y,z)`, RGB color values `(r,g,b)`, records from a database).
-   **Dictionary Keys:** Since tuples are immutable and hashable (if all their elements are immutable), they can be used as keys in dictionaries. Lists cannot be dictionary keys because they are mutable.
    ```python
    # location_inventory = {
    #     ("Warehouse A", "Shelf 3"): 100, # Tuple as key
    #     ("Warehouse B", "Shelf 1"): 50
    # }
    # print(location_inventory[("Warehouse A", "Shelf 3")])
    ```
-   **Elements in Sets:** Similar to dictionary keys, tuples can be elements of a set if all their elements are immutable.
-   **Returning Multiple Values from Functions:** Functions often return multiple values packed as a tuple.
    ```python
    # def get_product_stats(product_id):
    #     # ... fetch data ...
    #     price = 49.99
    #     stock = 150
    #     return price, stock # Returns a tuple (49.99, 150)

    # product_price, product_stock = get_product_stats("P123")
    ```
-   **String Formatting:** Older style string formatting using the `%` operator often uses tuples.
    ```python
    # name = "Alice"
    # age = 30
    # print("Name: %s, Age: %d" % (name, age))
    ```
-   **Performance:** Tuples can be slightly more memory-efficient and faster to iterate over than lists for fixed collections, though this difference is often negligible for small collections.

While lists are used for dynamic, modifiable sequences, tuples provide a way to create ordered, unchangeable collections, which is useful for data integrity, performance in certain contexts, and as hashable items.

---