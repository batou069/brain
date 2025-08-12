---
tags:
  - python
  - data_types
  - primitive_types
  - int
  - float
  - bool
  - str
  - concept
  - fundamental
  - type_casting
  - type_conversion
  - example
aliases:
  - Python Basic Data Types
  - Built-in Types Python
  - Python Type Conversion
  - Casting in Python
related:
  - "[[Python_Language_Overview]]"
  - "[[Python_Type_Casting]]"
  - "[[Python_Data_Structures_MOC|_Python_Data_Structures_MOC]]"
  - "[[Python_Primitive_Types]]"
  - "[[Dynamic_vs_Static_Typing]]"
worksheet:
  - WS16
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Python Primitive Data Types

Python has several built-in **primitive data types** that represent fundamental kinds of values. These are the basic building blocks for more complex data structures and objects. Python is [[Dynamic_vs_Static_Typing|dynamically typed]], so you don't need to declare the type of a variable explicitly.

The main primitive types are:

[list2tab|#Primitive Types]
- Integers (`int`)
    -   **Description:** Represent whole numbers (positive, negative, or zero) without a decimal point.
    -   Python integers have **arbitrary precision**, meaning they can grow to represent a number of any size, limited only by available memory.
    -   **Examples:**
        ```python
        age = 30
        count = -5
        year = 2024
        large_number = 12345678901234567890
        
        print(type(age))
        print(large_number)
        ```
        The output for `type(age)` would be `<class 'int'>`.
        The output for `large_number` would be `12345678901234567890`.
- Floating-Point Numbers (`float`)
    -   **Description:** Represent real numbers with a decimal point, or numbers in scientific notation (using `e` or `E`).
    -   They are typically implemented as **double-precision floating-point numbers** (64-bit) according to the IEEE 754 standard. This means they have a limited precision and can sometimes lead to small rounding errors in calculations.
    -   **Examples:**
        ```python
        price = 19.99
        temperature = -5.5
        pi_approx = 3.14159
        scientific_notation = 6.022e23 # Avogadro's number
        
        print(type(price))
        print(scientific_notation)
        ```
        The output for `type(price)` would be `<class 'float'>`.
        The output for `scientific_notation` would be `6.022e+23`.
- Booleans (`bool`)
    -   **Description:** Represent logical truth values: **True** or **False**. Note that these are capitalized in Python.
    -   Booleans are a subclass of integers, where `True` is internally represented as `1` and `False` as `0`.
    -   They are the result of comparison operations (e.g., `5 > 3` evaluates to `True`) and logical operations (`and`, `or`, `not`).
    -   **Examples:**
        ```python
        is_active = True
        has_permission = False
        result_comparison = (10 == 20) # False
        
        print(type(is_active))
        print(result_comparison)
        print(int(True))  # Output: 1
        print(int(False)) # Output: 0
        ```
        The output for `type(is_active)` would be `<class 'bool'>`.
        The output for `result_comparison` would be `False`.
- Strings (`str`)
    -   **Description:** Represent sequences of characters. Strings are **immutable**, meaning once a string is created, its content cannot be changed in place. Operations that appear to modify a string actually create a new string object.
    -   Can be created using single quotes (`'...'`), double quotes (`"..."`), or triple quotes (`'''...'''` or `"""..."""` for multi-line strings or strings containing quotes).
    -   Support various operations like concatenation (`+`), repetition (`*`), indexing, slicing, and many built-in methods (e.g., `.upper()`, `.lower()`, `.split()`, `.find()`).
    -   **Examples:**
        ```python
        product_name = "SuperWidget X1000"
        message = 'Welcome to our e-commerce store!'
        multiline_description = """This is a
        fantastic product with
        multiple features."""
        
        print(type(product_name))
        print(message)
        print(multiline_description)
        
        first_char = product_name # 'S'
        print(f"First character of product name: {first_char}")
        ```
        The output for `type(product_name)` would be `<class 'str'>`.
- NoneType (`None`)
    -   **Description:** A special data type that has only one value: `None`.
    -   It is often used to represent the absence of a value or a null value.
    -   Functions that don't explicitly return a value implicitly return `None`.
    -   **Example:**
        ```python
        customer_email = None # No email provided yet
        
        def my_void_function():
            # This function doesn't return anything explicitly
            pass 
            
        result = my_void_function()
        print(type(customer_email))
        print(result)
        ```
        The output for `type(customer_email)` would be `<class 'NoneType'>`.
        The output for `result` would be `None`.

These primitive types form the basis for all data manipulation in Python. More complex data can be organized using [[100_Python/Python_Data_Structures/_Python_Data_Structures_MOC|Python's built-in data structures]] like lists, tuples, dictionaries, and sets, which store collections of these primitive types (or other objects).

---

# Python: Type Casting (Type Conversion)

**Type casting** (or **type conversion**) in Python is the process of converting a variable or value from one data type to another. Python is a [[Dynamic_vs_Static_Typing|dynamically typed]] language, but it is also **strongly typed**, meaning it generally won't perform implicit conversions between incompatible types during operations (e.g., adding an integer to a string). Therefore, explicit type casting is often necessary.

Python provides several built-in functions for type casting:

## Common Type Casting Functions

[list2tab|#Casting Functions]
- `int(x, base=10)`
    -   **Purpose:** Converts `x` to an integer.
    -   **Behavior:**
        -   If `x` is a float, it truncates towards zero (e.g., `int(3.9)` is `3`, `int(-2.7)` is `-2`).
        -   If `x` is a boolean, `int(True)` is `1`, `int(False)` is `0`.
        -   If `x` is a string representing a whole number, it converts it (e.g., `int("123")` is `123`).
        -   The `base` argument can be used if the string represents a number in a different base (e.g., `int("101", base=2)` is `5`).
        -   Raises `ValueError` if the string cannot be converted (e.g., `int("hello")`, `int("12.3")`).
    -   **Example:**
        ```python
        float_num = 123.789
        int_from_float = int(float_num)
        print(f"int({float_num}) = {int_from_float}") # Output: 123

        str_num = "456"
        int_from_str = int(str_num)
        print(f"int('{str_num}') = {int_from_str}")   # Output: 456
        
        bool_true = True
        int_from_bool = int(bool_true)
        print(f"int({bool_true}) = {int_from_bool}")   # Output: 1
        ```
- `float(x)`
    -   **Purpose:** Converts `x` to a floating-point number.
    -   **Behavior:**
        -   If `x` is an integer, it adds a decimal point (e.g., `float(10)` is `10.0`).
        -   If `x` is a boolean, `float(True)` is `1.0`, `float(False)` is `0.0`.
        -   If `x` is a string representing a number (integer or float), it converts it (e.g., `float("123")` is `123.0`, `float("3.14")` is `3.14`).
        -   Can convert strings like `"inf"` or `"NaN"` (case-insensitive) to float infinity or NaN.
        -   Raises `ValueError` if the string cannot be converted (e.g., `float("hello")`).
    -   **Example:**
        ```python
        int_val = 789
        float_from_int = float(int_val)
        print(f"float({int_val}) = {float_from_int}") # Output: 789.0

        str_float = "273.15"
        float_from_str = float(str_float)
        print(f"float('{str_float}') = {float_from_str}") # Output: 273.15
        ```
- `str(object)`
    -   **Purpose:** Converts `object` to its string representation.
    -   **Behavior:**
        -   Works for most Python objects. For user-defined objects, it calls the `__str__()` dunder method if defined, otherwise `__repr__()`.
        -   Numbers are converted to their string form (e.g., `str(123)` is `'123'`, `str(3.14)` is `'3.14'`).
        -   Booleans are converted to `'True'` or `'False'`.
    -   **Example:**
        ```python
        number = 100
        str_from_num = str(number)
        print(f"str({number}) = '{str_from_num}' (type: {type(str_from_num)})")

        pi_val = 3.14159
        str_from_float = str(pi_val)
        print(f"str({pi_val}) = '{str_from_float}' (type: {type(str_from_float)})")

        is_valid = True
        str_from_bool = str(is_valid)
        print(f"str({is_valid}) = '{str_from_bool}' (type: {type(str_from_bool)})")
        ```
- `bool(x)`
    -   **Purpose:** Converts `x` to a boolean value (`True` or `False`).
    -   **Behavior (Truth Value Testing):**
        -   Most objects are considered `True`.
        -   The following are considered `False` by default:
            -   `None`
            -   `False` (the boolean value)
            -   Zero of any numeric type: `0`, `0.0`, `0j` (complex zero)
            -   Empty sequences: `''` (empty string), `[]` (empty list), `()` (empty tuple)
            -   Empty mappings: `{}` (empty dictionary)
            -   Empty sets: `set()`
            -   Instances of user-defined classes, if the class defines a `__bool__()` method that returns `False` or a `__len__()` method that returns zero.
    -   **Example:**
        ```python
        print(f"bool(0) = {bool(0)}")         # Output: False
        print(f"bool(10) = {bool(10)}")       # Output: True
        print(f"bool(0.0) = {bool(0.0)}")     # Output: False
        print(f"bool('') = {bool('')}")       # Output: False
        print(f"bool('Hi') = {bool('Hi')}")   # Output: True
        print(f"bool([]) = {bool([])}")       # Output: False
        print(f"bool([1,2]) = {bool([1,2])}") # Output: True
        print(f"bool(None) = {bool(None)}")   # Output: False
        ```
- Casting to Collection Types
    -   `list(iterable)`: Converts an iterable (e.g., tuple, string, set, dictionary keys/values/items) to a list.
    -   `tuple(iterable)`: Converts an iterable to a tuple.
    -   `set(iterable)`: Converts an iterable to a set (duplicates removed).
    -   `dict(iterable_of_pairs)` or `dict(**kwargs)`: Creates a dictionary.
    -   **Example:**
        ```python
        my_tuple = (1, 2, 2, 3)
        list_from_tuple = list(my_tuple)
        print(f"list({my_tuple}) = {list_from_tuple}") # Output: [1, 2, 2, 3]

        my_string = "hello"
        list_from_string = list(my_string)
        print(f"list('{my_string}') = {list_from_string}") # Output: ['h', 'e', 'l', 'l', 'o']
        
        set_from_list = set(list_from_tuple)
        print(f"set({list_from_tuple}) = {set_from_list}") # Output: {1, 2, 3}
        ```

## Implicit Type Conversion (Coercion)
In some limited cases, Python performs implicit type conversion, also known as coercion, particularly in numerical operations. For example, when an integer and a float are involved in an arithmetic operation, the integer is often implicitly converted to a float before the operation.
```python
result = 5 + 2.0 # 5 (int) is coerced to 5.0 (float)
print(f"5 + 2.0 = {result} (type: {type(result)})") # Output: 7.0 (type: <class 'float'>)
```
However, relying too much on implicit conversion can sometimes lead to less clear code or unexpected behavior if the coercion rules are not fully understood. Explicit casting is often preferred for clarity and safety, especially when dealing with types that are not automatically compatible (like strings and numbers).

Type casting is a fundamental operation for manipulating data and ensuring that variables have the correct type for the operations you intend to perform on them.

---