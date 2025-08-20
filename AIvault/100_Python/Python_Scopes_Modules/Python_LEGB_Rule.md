---
tags:
  - python
  - scope
  - namespace
  - legb
  - name_resolution
  - concept
  - programming_fundamentals
aliases:
  - LEGB Rule
  - Python Scope Resolution
  - Name Lookup Python
related:
  - "[[Python_Scopes_Visibility]]"
  - "[[Python_Namespaces]]"
  - "[[Python_global_Keyword]]"
  - "[[Python_Nested_Functions_Closures|nonlocal Keyword]]"
worksheet:
  - WS19
date_created: 2025-08-20
---
# Python: LEGB Rule (Scope Resolution)

When Python encounters a name (variable, function, class) in your code, it needs to determine what object that name refers to. The **LEGB rule** is the sequence of [[Python_Namespaces|namespaces]] Python searches to find this object. LEGB stands for:

1.  **L**ocal
2.  **E**nclosing function locals
3.  **G**lobal
4.  **B**uilt-in

Python searches these scopes in this specific order. The first place a name is found is the one that is used. If the name is not found in any of these scopes, a `NameError` exception is raised.

>[!question] What is the order of lookup For names?
>The order of lookup for names in Python follows the LEGB rule:
>1.  **Local (L):** This is the current scope. If inside a function, it's the function's local namespace (including its parameters). If in a class definition, it's the class's local namespace.
>2.  **Enclosing function locals (E):** If the current scope is a nested function, Python searches the local scopes of all enclosing functions, from the innermost enclosing function outwards. This is how [[Python_Nested_Functions_Closures|closures]] work. This scope is skipped if not in a nested function.
>3.  **Global (G):** This is the namespace of the module containing the current code. Names defined at the top level of a module are global to that module.
>4.  **Built-in (B):** This namespace contains all of Python's built-in functions (`len()`, `print()`, `str()`, etc.) and built-in exception names. It's always available and searched last.

## Detailed Explanation of LEGB Scopes

[list2tab|#LEGB Scopes]
- L: Local Scope
    -   The names assigned within the currently executing function (including its parameters).
    -   This is the first place Python looks.
    -   When a function call ends, its local scope is typically destroyed.
    -   **Example:**
        ```python
        # def my_function(product_price):
        #     discount = 0.1 # 'discount' is local to my_function
        #     final_price = product_price * (1 - discount)
        #     print(final_price) # Looks for product_price, discount, final_price locally first
        ```
- E: Enclosing Function Locals Scope
    -   If a function is nested inside another function, the inner function can access names from the outer (enclosing) function's local scope.
    -   Python searches these enclosing scopes from the nearest one outwards until it reaches the module's global scope.
    -   This is what enables closures.
    -   **Example:**
        ```python
        # def outer_checkout(customer_type):
        #     # customer_type is in the enclosing scope for apply_special_discount
        #     base_discount = 0.05 

        #     def apply_special_discount(price):
        #         # price is local to apply_special_discount
        #         if customer_type == "VIP":
        #             # Accesses customer_type and base_discount from enclosing scope
        #             return price * (1 - (base_discount + 0.10)) 
        #         return price * (1 - base_discount)
            
        #     return apply_special_discount # Returns the inner function

        # vip_discounter = outer_checkout("VIP")
        # print(vip_discounter(100)) # vip_discounter "remembers" customer_type and base_discount
        ```
- G: Global Scope
    -   The namespace of the module from which the code is currently executing.
    -   Names defined at the top level of a `.py` file (outside any function or class) are in this global scope.
    -   Each module has its own distinct global scope.
    -   To modify a global variable from within a function, you must use the [[Python_global_Keyword|`global` keyword]].
    -   **Example:**
        ```python
        # tax_rate = 0.07 # tax_rate is global to this module

        # def calculate_total_with_tax(subtotal):
        #     total = subtotal * (1 + tax_rate) # Accesses global tax_rate
        #     return total
        
        # print(calculate_total_with_tax(100))
        ```
- B: Built-in Scope
    -   The outermost scope, containing names that are always available in Python without needing any imports.
    -   Includes functions like `len()`, `print()`, `int()`, `str()`, `list()`, `dict()`, `range()`, `type()`, built-in exceptions like `ValueError`, `TypeError`, and constants like `True`, `False`, `None`.
    -   This is the last scope searched.
    -   It's possible (though generally bad practice) to shadow a built-in name by defining a global or local variable with the same name.
    -   **Example:**
        ```python
        # my_items = ["apple", "banana"]
        # print(len(my_items)) # 'len' is found in the built-in scope
        
        # Bad practice: shadowing a built-in
        # str = "This is now a variable, not the str() function"
        # print(str(123)) # Would raise TypeError: 'str' object is not callable
        ```

## How the LEGB Rule Works
When a name is encountered:
1.  Python checks the **Local** scope. If found, it's used.
2.  If not in Local, and if inside a nested function, it checks the **Enclosing function local** scopes, from innermost to outermost. If found, it's used.
3.  If not found in Local or Enclosing, it checks the **Global** (module) scope. If found, it's used.
4.  If not found in Global, it checks the **Built-in** scope. If found, it's used.
5.  If the name is not found in any of these scopes, a `NameError` is raised.

**Example Illustrating Full LEGB Search:**
```python
# B: Built-in (print, len)
# G: Global
global_api_key = "XYZ123_GLOBAL"

def configure_api(api_version="v2"):
    # E: Enclosing for process_data
    enclosing_service_url = f"http://api.example.com/{api_version}"
    
    def process_data(data_payload):
        # L: Local
        local_batch_id = "BATCH001"
        print(f"Processing batch: {local_batch_id}") # L
        print(f"Service URL: {enclosing_service_url}") # E
        print(f"Using API Key: {global_api_key}") # G
        print(f"Payload length: {len(data_payload)}") # B (len is built-in)
        return True

    return process_data

# processor_v2 = configure_api()
# sample_payload = {"item_id": "P789", "quantity": 5}
# processor_v2(sample_payload)

# processor_v3 = configure_api(api_version="v3") # Creates a new closure
# processor_v3(sample_payload)
```

The LEGB rule is a fundamental concept that governs how Python resolves names, ensuring that variables and functions are accessed from the correct context.

---