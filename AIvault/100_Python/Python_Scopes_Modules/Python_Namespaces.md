---
tags:
  - python
  - namespace
  - scope
  - identifier
  - mapping
  - concept
  - programming_fundamentals
aliases:
  - Python Namespace
  - Name Binding Python
related:
  - "[[Python_Scopes_Visibility]]"
  - "[[Python_LEGB_Rule]]"
  - "[[Python_Modules_Packages|Modules (each module has its own namespace)]]"
  - "[[Python_OOP_MOC|Classes and Objects (each instance has its own namespace)]]"
worksheet:
  - WS19
date_created: 2025-08-20
---
# Python: Namespaces

A **namespace** in Python is a system that ensures that all names (identifiers like variable names, function names, class names) in a program are unique and can be used without conflict. Think of it as a dictionary where keys are the names and values are the objects those names refer to.

Different namespaces can coexist at the same time, and names in one namespace do not clash with identical names in another namespace.

## Concept of Namespaces
-   **Mapping:** A namespace is essentially a mapping from names to objects.
-   **Context:** Each namespace provides a context for names. The same name can exist in different namespaces and refer to different objects. For example, a function might have a local variable `x`, and there might also be a global variable `x` in the module; these are distinct.
-   **Lifetime:** Namespaces are created at different moments and have different lifetimes:
    -   The **built-in namespace** (containing functions like `len()`, `print()`, and built-in exception names) is created when the Python interpreter starts and is never deleted.
    -   The **global namespace** for a module is created when the module definition is read in; normally, module namespaces also last until the interpreter quits.
    -   The **local namespace** for a function is created when the function is called, and deleted when the function returns or raises an unhandled exception.

## When are Namespaces Created?
-   When the Python interpreter starts (built-in namespace).
-   When a module is imported or run (global namespace for that module).
-   When a function is called (local namespace for that function call).
    -   [[Python_Nested_Functions_Closures|Nested functions]] create nested local namespaces.
-   When a class is defined (local namespace within the class definition, attributes become part of class/instance namespace).
-   When an object instance is created (instance attributes form a namespace for that object).

>[!question] What operations in Python create names in namespaces?
>Names are introduced into namespaces through various operations:
>
>1.  **Assignments:**
>    -   Direct assignment: `x = 10` (creates or rebinds `x` in the current local or global scope).
>    -   Augmented assignment: `x += 1` (if `x` doesn't exist, it might create it, depending on context, or raise `NameError`).
>2.  **Function Definitions (`def`):**
>    -   `def my_function(param1, param2): ...` creates the name `my_function` in the current scope (usually global or enclosing function local).
>    -   Function parameters (`param1`, `param2`) are bound to names in the function's local namespace when the function is called.
>3.  **Class Definitions (`class`):**
>    -   `class MyClass: ...` creates the name `MyClass` in the current scope.
>    -   Names assigned within the class body (but outside methods) become class attributes.
>    -   Names assigned to `self` within methods (e.g., `self.instance_var = value`) create instance attributes in the instance's namespace.
>4.  **`import` Statements:**
>    -   `import my_module`: Creates the name `my_module` in the current namespace, referring to the module object.
>    -   `from my_module import some_name`: Creates `some_name` directly in the current namespace, referring to the object `some_name` from `my_module`.
>    -   `from my_module import another_name as alias_name`: Creates `alias_name` in the current namespace.
>5.  **`for` Loop Variables:**
>    -   `for item in iterable: ...` assigns each element of `iterable` to the name `item` in the current scope (often local to a function, or global if the loop is at module level).
>6.  **`with ... as name:` (Context Managers):**
>    -   `with open('file.txt') as f: ...` binds the name `f` to the file object within the `with` block's scope.
>7.  **`except ... as name:` (Exception Handling):**
>    -   `try: ... except ValueError as e: ...` binds the name `e` to the exception instance within the `except` block.
>8.  **List/Set/Dictionary Comprehensions and Generator Expressions (Variables within them):**
>    -   In Python 3.x, variables used in comprehensions (e.g., `x` in `[x*x for x in range(5)]`) have their own scope and do not "leak" into the surrounding scope. In Python 2.x, they did leak.

These operations are how names get associated with objects within specific namespaces. The [[Python_Scopes_Visibility|scope]] then determines where these names are accessible.

## Relationship with Scopes
-   A **scope** is a textual region of a Python program where a namespace is directly accessible.
-   At any point in execution, there are at least three nested scopes whose namespaces are directly accessible:
    1.  The innermost scope, which is searched first, contains the local names.
    2.  The scopes of any enclosing functions, which are searched starting with the nearest enclosing scope.
    3.  The next-to-last scope contains the current module’s global names.
    4.  The outermost scope (searched last) is the namespace containing built-in names.
    (This is the [[Python_LEGB_Rule|LEGB rule]]).

**Example:**
```python
# Module's global namespace
global_var = "I am global in this module"

def outer_func():
    # Enclosing namespace for inner_func
    enclosing_var = "I am in outer_func's local (enclosing for inner) namespace"
    
    def inner_func():
        # Local namespace for inner_func
        local_var = "I am local to inner_func"
        print(local_var)         # Accesses inner_func's local namespace
        print(enclosing_var)     # Accesses outer_func's local namespace
        print(global_var)        # Accesses module's global namespace
        print(len("hello"))      # Accesses built-in namespace for 'len'
    
    inner_func()

# outer_func()
```
Each call to `outer_func` creates a new local namespace for it, and each call to `inner_func` (within `outer_func`) creates its own local namespace.

Namespaces are a fundamental concept for organizing code and preventing name conflicts in Python, allowing for modular and maintainable programs.

---
