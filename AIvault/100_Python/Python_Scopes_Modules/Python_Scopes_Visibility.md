---
tags:
  - python
  - scope
  - visibility
  - namespace
  - legb
  - concept
  - programming_fundamentals
aliases:
  - Python Scope
  - Name Visibility Python
related:
  - "[[100_Python/Python_Scopes_Modules/_Python_Scopes_Modules_MOC|_Python_Scopes_Modules_MOC]]"
  - "[[Python_Namespaces]]"
  - "[[Python_LEGB_Rule]]"
  - "[[Python_global_Keyword]]"
  - "[[Python_Nested_Functions_Closures|nonlocal Keyword]]"
worksheet:
  - WS19
date_created: 2025-08-20
---
# Python: Scopes and Visibility

## What is a Scope?
In Python, a **scope** is a region of a program where a particular [[Python_Namespaces|namespace]] is directly accessible. A namespace is a mapping from names (identifiers like variable names, function names, class names) to objects. Scopes define the "visibility" or "accessibility" of these names.

When you refer to a name (e.g., use a variable `x`), Python searches through a sequence of scopes to find the object that name refers to. This search order is defined by the [[Python_LEGB_Rule|LEGB rule]].

## Types of Scopes in Python
Python has primarily four types of scopes:

1.  **Local (L):**
    -   The innermost scope, containing names defined **inside the current function**.
    -   When a function is called, a new local scope is created for that call.
    -   Parameters passed to the function are also in its local scope.
    -   Names assigned within the function (that are not declared `global` or `nonlocal`) belong to this local scope.
    -   This scope is destroyed when the function returns.

2.  **Enclosing function locals (E):**
    -   This scope exists for **[[Python_Nested_Functions_Closures|nested functions]]**.
    -   If a function is defined inside another function (the enclosing function), the nested function has access to the names in the local scope of its enclosing function(s).
    -   Python searches these enclosing scopes from the innermost enclosing scope outwards.

3.  **Global (G):**
    -   The scope of the **module** in which the code is currently running.
    -   Names defined at the top level of a module (outside any function or class) are in the global scope of that module.
    -   Each module has its own global scope.

4.  **Built-in (B):**
    -   The outermost scope, containing pre-defined names that are always available in Python without needing to be imported.
    -   Examples: `len()`, `print()`, `str()`, `list()`, `Exception` types like `ValueError`, `TypeError`.

## Visibility of Names

>[!question] How do you define the scope or visibility of a name?
>The scope or visibility of a name in Python is determined by **where that name is assigned or defined** within the code structure.
>
>1.  **Assignment within a function (`def` or `lambda`):** If a name is assigned a value inside a function (and not declared `global` or `nonlocal`), it becomes a **local** name to that function. Its visibility is limited to that function's body.
>    ```python
>    def my_func():
>        local_var = 10 # local_var is local to my_func
>        print(local_var)
>    # print(local_var) # This would cause a NameError
>    ```
>2.  **Parameters of a function:** Function parameters are also **local** to that function.
>    ```python
>    def another_func(param): # param is local to another_func
>        print(param)
>    ```
>3.  **Assignment within a nested function:** If a name is assigned within a nested function without `nonlocal` or `global`, it's local to that nested function. If `nonlocal` is used, it refers to a name in an enclosing function's scope. If `global` is used, it refers to a name in the module's global scope.
>4.  **Assignment at the top level of a module:** If a name is assigned outside of any function or class definition within a module file, it becomes a **global** name within that module. It's visible throughout that module and can be imported by other modules.
>    ```python
>    # my_module.py
>    global_module_var = 100 # global within my_module
>    def some_func():
>        print(global_module_var) # Accesses the module's global
>    ```
>5.  **Class definitions (`class`):** Names assigned inside a class definition (but outside methods) are class attributes. Names assigned inside methods (using `self.name = ...`) are instance attributes. These have their own scoping rules related to classes and instances.
>6.  **Import statements:** `import module_name` makes the `module_name` itself available in the current scope. `from module_name import name` brings `name` directly into the current scope.
>
>The [[Python_LEGB_Rule|LEGB rule]] then dictates how Python searches for these names when they are accessed (read).

## Scope Resolution (LEGB Rule)
When Python encounters a name, it tries to resolve it by searching the scopes in the following order:
1.  **L**ocal: The current function's local scope.
2.  **E**nclosing function locals: Scopes of any enclosing functions, from innermost to outermost.
3.  **G**lobal: The global scope of the current module.
4.  **B**uilt-in: The scope containing built-in functions and constants.

If the name is not found after searching all these scopes, a `NameError` exception is raised.

**Example Illustrating LEGB:**
```python
# Built-in scope
# print("This is from built-in scope:", len) 

# Global scope
x_global = "I am global"

def outer_function():
    # Enclosing function local scope for inner_function
    x_enclosing = "I am enclosing"
    
    def inner_function():
        # Local scope
        x_local = "I am local"
        print(x_local)       # Accesses L
        print(x_enclosing)   # Accesses E
        print(x_global)      # Accesses G
        print(len("test"))   # Accesses B (len is built-in)
    
    inner_function()
    # print(x_local) # NameError: x_local not defined in outer_function's scope

# outer_function()
# print(x_enclosing) # NameError: x_enclosing not defined in global scope
```

Understanding scopes is fundamental for writing correct Python code, avoiding `NameError` exceptions, and managing where variables are accessible and how they might be shadowed or modified.

---