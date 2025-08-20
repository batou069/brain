---
tags:
  - python
  - scope
  - global_keyword
  - variable_scope
  - namespace
  - concept
  - example
aliases:
  - global statement python
related:
  - "[[Python_Scopes_Visibility]]"
  - "[[Python_LEGB_Rule]]"
  - "[[Python_Namespaces]]"
  - "[[Python_Nested_Functions_Closures|nonlocal Keyword]]"
worksheet:
  - WS19
date_created: 2025-08-20
---
# Python: `global` Keyword

The `global` keyword in Python is used to declare that a variable inside a function refers to a variable in the **global scope** (i.e., the module-level scope), rather than creating a new local variable with the same name.

## Purpose
Normally, if you assign a value to a variable inside a function, Python creates that variable in the function's local scope. If you want to *modify* a global variable from within a function, you must explicitly tell Python that you are referring to the global variable using the `global` keyword.

-   **Reading Globals:** You can *read* the value of a global variable from within a function without the `global` keyword, as Python will find it via the [[Python_LEGB_Rule|LEGB rule]] if it's not found locally or in enclosing scopes.
-   **Modifying Globals:** To *assign to* or *change* a global variable from within a function, you **must** use `global variable_name` before the assignment.

## Syntax
```python
global variable_name1, variable_name2, ...
```
This statement is typically placed at the beginning of the function body.

## Behavior
-   The `global` statement tells Python that any assignments to the specified variable names within that function should affect the global variable of that name, not create a new local one.
-   If the global variable does not exist when `global` is declared and then an assignment is made, a new global variable is created.

## Examples

**1. Reading a global variable (no `global` keyword needed):**
```python
# Global variable for an e-commerce site's default currency
default_currency = "USD"

def display_product_price(price):
    # Reads the global 'default_currency'
    print(f"Price: {price} {default_currency}")

# display_product_price(29.99) # Output: Price: 29.99 USD
```

**2. Modifying a global variable (requires `global` keyword):**
```python
# Global counter for total items processed
total_items_processed = 0

def process_order(items_in_order):
    global total_items_processed # Declare intent to modify the global variable
    
    print(f"Processing {items_in_order} items...")
    total_items_processed += items_in_order # Modifies the global variable
    print(f"Current total items processed: {total_items_processed}")

# print(f"Initial total items: {total_items_processed}")
# process_order(5)
# process_order(3)
# print(f"Final total items: {total_items_processed}")
```
Output:```
Initial total items: 0
Processing 5 items...
Current total items processed: 5
Processing 3 items...
Current total items processed: 8
Final total items: 8
```

**3. What happens without `global` when trying to modify:**
If you try to assign to a variable inside a function that has the same name as a global variable *without* using the `global` keyword, Python creates a new *local* variable. If you try to read it before this local assignment, you might get an `UnboundLocalError`.

```python
# Global variable for site status
site_status = "Online"

def attempt_to_update_status_locally(new_status):
    # This creates a NEW LOCAL variable 'site_status', shadowing the global one.
    # It does NOT modify the global 'site_status'.
    site_status = new_status 
    print(f"Inside function, local site_status: {site_status}")

def problematic_update_status():
    # This will cause UnboundLocalError if site_status is not yet assigned locally
    # because Python sees an assignment to site_status later in the function,
    # so it treats site_status as local throughout this function.
    # print(f"Trying to read site_status before local assignment: {site_status}") # This line would error
    site_status = "Maintenance" # This makes site_status local
    print(f"Inside problematic_update_status, local site_status: {site_status}")


# print(f"Initial global site_status: {site_status}")
# attempt_to_update_status_locally("Maintenance Mode")
# print(f"Global site_status after local attempt: {site_status}") # Still "Online"

# try:
#     problematic_update_status()
# except UnboundLocalError as e:
#     print(f"Error in problematic_update_status: {e}") 
# print(f"Global site_status after problematic attempt: {site_status}") # Still "Online"
```

>[!question] Why is using and modifying global names generally considered to be bad programming practice?
>Modifying global variables from within functions is generally discouraged for several reasons:
>1.  **Reduced Readability and Maintainability:** It makes it harder to understand the flow of data and the state of the program. When a function modifies global state, its effects are not self-contained, and you have to look outside the function to understand its full impact. This can lead to "spaghetti code" where changes in one part of the code unexpectedly affect other parts.
>2.  **Increased Complexity:** Global variables create hidden dependencies between functions and modules. Changes to a global variable can have far-reaching and often unintended consequences, making debugging difficult.
>3.  **Testing Difficulties:** Functions that rely on or modify global state are harder to test in isolation. You need to set up the global state correctly before each test and potentially clean it up afterwards. Pure functions (that don't rely on or modify external state) are much easier to test.
>4.  **Namespace Pollution:** Overuse of global variables can clutter the global namespace, increasing the risk of name collisions, especially in larger projects or when integrating multiple modules.
>5.  **Reduced Reusability:** Functions that depend on specific global variables are less reusable in different contexts or projects where those globals might not exist or have different meanings.
>
>**Alternatives to Modifying Globals:**
>-   **Pass variables as arguments:** If a function needs some data, pass it as an argument.
>-   **Return values from functions:** If a function computes a value that needs to be used elsewhere, return it.
>-   **Use Classes and Objects:** For managing state that needs to be shared and modified by multiple methods, encapsulate it within a class using instance attributes. This provides better organization and control.
>-   **Configuration Objects/Modules:** For application-wide settings, use dedicated configuration objects or modules that can be imported and accessed in a controlled manner.
>
>While there might be rare, specific cases where modifying a global variable is a pragmatic solution (e.g., simple scripts, some caching mechanisms), it should generally be avoided in favor of more explicit and encapsulated ways of managing state.

The `global` keyword is a necessary tool if you *must* modify a global variable from within a function, but its use should be carefully considered due to the potential downsides to code clarity and maintainability.

---