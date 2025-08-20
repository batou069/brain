---
tags: [python, functions, arguments, parameters, args, kwargs, variable_arguments, unpacking, concept, example]
aliases: [*args, **kwargs, Arbitrary Arguments Python, Keyword Arguments Python]
related:
  - "[[100_Python/Python_Functions/_Python_Functions_MOC|_Python_Functions_MOC]]"
  - "[[Python_Function_Definition_Syntax]]"
worksheet: [WS18]
date_created: 2025-08-20
---
# Python: `*args` and `**kwargs` (Variable Arguments)

Python functions can be defined to accept a variable number of arguments using special syntax: `*args` for positional arguments and `**kwargs` for keyword arguments.

>[!question] What is the definition of "args" and the definition of "kwargs"? Are we required to use these specific names?
>
>-   **`*args` (Arbitrary Positional Arguments):**
>    -   **Definition:** When used in a function definition, `*args` allows the function to accept an **arbitrary number of positional arguments**. These arguments are collected into a **tuple** named `args` (or whatever name follows the `*`).
>    -   **Required Name?** No, `args` is just a convention. You could use `*my_numbers` or `*params`, but `*args` is widely understood. The single asterisk `*` is the important part of the syntax.
>
>-   **`**kwargs` (Arbitrary Keyword Arguments):**
>    -   **Definition:** When used in a function definition, `**kwargs` allows the function to accept an **arbitrary number of keyword arguments** (arguments passed in the form `key=value`). These arguments are collected into a **dictionary** named `kwargs` (or whatever name follows the `**`).
>    -   **Required Name?** No, `kwargs` is just a convention. You could use `**options` or `**attributes`, but `**kwargs` is standard. The double asterisk `**` is the important part.

## Using `*args`
To accept a variable number of positional arguments.

```python
def calculate_product_sum(*numbers): # 'numbers' will be a tuple
    """Calculates the sum of all numbers passed as arguments."""
    print(f"Received numbers as a tuple: {numbers}")
    total = 0
    for num in numbers:
        total += num
    return total

# print(calculate_product_sum(10, 20))          # Output: Received numbers... (10, 20) -> 30
# print(calculate_product_sum(5, 15, 25, 5))    # Output: Received numbers... (5, 15, 25, 5) -> 50
# print(calculate_product_sum())                # Output: Received numbers... () -> 0
```
Inside `calculate_product_sum`, `numbers` is a tuple containing all the positional arguments passed.

## Using `**kwargs`
To accept a variable number of keyword arguments.

```python
def display_product_info(**details): # 'details' will be a dictionary
    """Displays product information passed as keyword arguments."""
    print("Product Details:")
    if not details:
        print("  No details provided.")
        return
    for key, value in details.items():
        print(f"  {key.replace('_', ' ').title()}: {value}")

# display_product_info(name="Super Laptop", price=1299.99, category="Electronics")
# display_product_info(item_id="XYZ001", in_stock=True, color="Silver", warranty_years=2)
# display_product_info()
```
Inside `display_product_info`, `details` is a dictionary containing all the keyword arguments passed.

## Combining `*args`, `**kwargs` with Standard Arguments

>[!question] If you want to use standard arguments along with `*args` and `**kwargs`, what is the correct order?
>The correct order for parameters in a function definition is:
>1.  **Standard positional arguments.**
>2.  `*args` (for arbitrary positional arguments).
>3.  **Keyword-only arguments** (arguments that can *only* be passed by keyword, appear after `*args` or a bare `*`).
>4.  `**kwargs` (for arbitrary keyword arguments).
>
>```python
>def example_function(pos_arg1, pos_arg2, default_arg="default", *args, kw_only_arg1, kw_only_arg2="val2", **kwargs):
>    print(f"pos_arg1: {pos_arg1}")
>    print(f"pos_arg2: {pos_arg2}")
>    print(f"default_arg: {default_arg}")
>    print(f"args: {args}")
>    print(f"kw_only_arg1: {kw_only_arg1}")
>    print(f"kw_only_arg2: {kw_only_arg2}")
>    print(f"kwargs: {kwargs}")

# Calling it:
# example_function(1, 2, "custom_default", 10, 20, 30, 
#                  kw_only_arg1="hello", option1="A", option2="B")
# Output:
# pos_arg1: 1
# pos_arg2: 2
# default_arg: custom_default
# args: (10, 20, 30)
# kw_only_arg1: hello
# kw_only_arg2: val2
# kwargs: {'option1': 'A', 'option2': 'B'}

# example_function(1, 2, kw_only_arg1="world") # Also valid
```

## Unpacking Arguments (`*` and `**` in function calls)

>[!question] What is an "unpacking operator"? Why do we use a single asterisk in "args" and double in "kwargs"?
>The `*` and `**` symbols when used in *function calls* (not definitions) are **unpacking operators**.
>
>-   **`*iterable` (Unpacking Positional Arguments):**
>    -   When calling a function, `*` unpacks an iterable (like a list or tuple) into individual positional arguments.
>    -   **Why single asterisk for `*args` in definition?** In the function definition, `*args` *collects* multiple positional arguments into a single tuple named `args`. The single asterisk signifies "collect all remaining positional arguments."
>
>-   **`**dictionary` (Unpacking Keyword Arguments):**
>    -   When calling a function, `**` unpacks a dictionary into individual keyword arguments, where dictionary keys become argument names and dictionary values become argument values.
>    -   **Why double asterisk for `**kwargs` in definition?** In the function definition, `**kwargs` *collects* multiple keyword arguments into a single dictionary named `kwargs`. The double asterisk signifies "collect all remaining keyword arguments."

**Example of Unpacking in Function Calls:**
```python
def describe_item(item_id, name, price=0.0, category="General"):
    print(f"ID: {item_id}, Name: {name}, Price: ${price:.2f}, Category: {category}")

# Using * to unpack a list/tuple for positional arguments
product_data_list = ["P456", "Deluxe Coffee Grinder"]
# describe_item(*product_data_list, price=89.99, category="Appliances")
# Equivalent to: describe_item("P456", "Deluxe Coffee Grinder", price=89.99, category="Appliances")

# Using ** to unpack a dictionary for keyword arguments
product_details_dict = {
    "name": "Ergonomic Keyboard",
    "price": 75.50,
    "category": "Accessories"
}
# describe_item("K789", **product_details_dict)
# Equivalent to: describe_item("K789", name="Ergonomic Keyboard", price=75.50, category="Accessories")

# Combining them
# required_args = ("S001", "Premium Subscription")
# optional_attrs = {"price": 19.99, "category": "Service"}
# describe_item(*required_args, **optional_attrs)
```

`*args` and `**kwargs` provide great flexibility in designing functions that can handle a varying number of inputs or pass arguments through to other functions.

---