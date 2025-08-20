---
tags:
  - python
  - module
  - package
  - import
  - from_import
  - namespace
  - concept
  - syntax
aliases:
  - Python Import Statement
  - from ... import
  - Python Module Importing
related:
  - "[[Python_Modules_Packages]]"
  - "[[Python_Namespaces]]"
  - "[[Python_Script_vs_Module|Executing Modules as Scripts (`if __name__ == '__main__':`)]]"
  - "[[sys_module_python|sys.path]]"
worksheet:
  - WS19
date_created: 2025-08-20
---
# Python: The `import` System

Python's `import` system allows you to bring definitions (functions, classes, variables) from one module or package into another module or into the interactive interpreter's scope. This is the primary mechanism for code reuse and modularization.

## Basic `import module_name`
-   **Syntax:** `import module_name` or `import package_name.module_name`
-   **Behavior:**
    1.  Python searches for `module_name.py` (or the package directory) in a list of directories defined by `sys.path` (which includes the directory of the input script, `PYTHONPATH` environment variable, and installation-dependent default paths).
    2.  If found, the code in the module is executed (if it's the first time being imported in the session).
    3.  A **module object** is created.
    4.  The name `module_name` (or the last part of a dotted package path) is bound in the current [[Python_Namespaces|namespace]] to this module object.
    5.  To access definitions within the imported module, you must use the module name as a prefix (attribute access): `module_name.definition_name`.
-   **Example:**
    ```python
    # Assume ecommerce_utils.py exists with:
    # def calculate_shipping(weight): return weight * 0.5

    import math # Built-in module
    import ecommerce_utils # Custom module

    # print(math.sqrt(16)) # Access sqrt via math.
    # shipping_cost = ecommerce_utils.calculate_shipping(10)
    # print(f"Shipping cost: {shipping_cost}")
    ```

## `from module_name import name1, name2, ...`
-   **Syntax:** `from module_name import name1`, `from module_name import name1 as alias1, name2`
-   **Behavior:**
    1.  The module `module_name` is loaded and executed (if not already).
    2.  The specified names (`name1`, `name2`, etc.) are directly bound into the current [[Python_Namespaces|namespace]].
    3.  You can then use `name1` directly without prefixing it with `module_name.`.
    4.  The module object itself is *not* bound to `module_name` in the current namespace (unless you also do a separate `import module_name`).
-   **Example:**
    ```python
    # from math import sqrt, pi
    # from ecommerce_utils import calculate_tax, Product

    # print(sqrt(25)) # Use sqrt directly
    # print(f"Value of pi: {pi}")
    # tax = calculate_tax(100)
    # my_item = Product("Widget", 19.99)
    ```

>[!question] Explain the difference between `import module` and `from <module name> import *`. Why is it dangerous to use a second Form of importing?
>
>[list2tab|#import vs from import *]
>- `import module_name`
>    -   **What it does:** Imports the module `module_name`. You must use `module_name.attribute` to access its contents.
>    -   **Namespace:** Introduces only one name (`module_name`) into the current namespace.
>    -   **Clarity:** Very clear where names are coming from (e.g., `math.pi` clearly indicates `pi` is from the `math` module).
>    -   **Name Clashes:** Less prone to name clashes, as attributes are accessed via the module's namespace.
>    -   **Example:**
>        ```python
>        # import math
>        # print(math.pi)
>        # print(math.sqrt(4))
>        ```
>- `from module_name import *`
>    -   **What it does:** Imports **all public names** (those not starting with an underscore `_`, or all names if the module defines `__all__`) from `module_name` directly into the current namespace. You can use these names directly without the module prefix.
>    -   **Namespace:** Can introduce many names into the current namespace, potentially overwriting existing names.
>    -   **Clarity:** Can make it unclear where a specific name originated, especially if multiple modules are imported this way. This reduces code readability and maintainability.
>    -   **Name Clashes:** High risk of name clashes. If the imported module defines a name that already exists in your current scope, the existing name will be overwritten silently. This can lead to subtle bugs that are hard to trace.
>    -   **Example:**
>        ```python
>        # from math import * # Imports pi, sqrt, sin, cos, etc., directly
>        # print(pi)
>        # print(sqrt(4))
>        #
>        # def sqrt(x): # This would overwrite the imported math.sqrt if defined after the import!
>        #     print("My custom sqrt!")
>        #     return x**0.5 
>        ```>
>**Why is `from module_name import *` dangerous (and generally discouraged by PEP 8)?**
>1.  **Namespace Pollution:** It dumps all imported names into your current namespace, making it crowded and harder to manage.
>2.  **Name Clashes:** It can silently overwrite names that already exist in your namespace or that are imported from other modules, leading to unexpected behavior and bugs.
>3.  **Reduced Readability:** It becomes difficult to tell where a particular name (function, variable, class) came from without looking at all the `import *` statements. This makes code harder to understand and maintain, especially for others (or your future self).
>4.  **Tooling Issues:** Static analysis tools (linters, type checkers) may have a harder time analyzing code that uses `import *`.
>
>**When might it be (cautiously) acceptable?**
>-   In the interactive interpreter (`>>>`) for convenience during exploration.
>-   Sometimes within a module's `__init__.py` to re-export names from submodules to make the package API flatter (though explicit re-exporting `from .submodule import name` is often preferred).
>-   Very rarely, for specific modules designed to be used this way (e.g., some parts of `tkinter`).
>
>In general, prefer `import module_name` or `from module_name import specific_name1, specific_name2` for clarity and to avoid namespace issues.

## Absolute vs. Relative Imports

>[!question] What is the difference between *absolute* import and *relative* import? When will you use each?
>
>[list2tab|#Absolute vs Relative Imports]
>- Absolute Imports
>    -   **Definition:** Specify the full path to the module from the project's root directory (or a directory in `sys.path`). They are "absolute" because they don't depend on the location of the current file.
>    -   **Syntax:** `import package.subpackage.module` or `from package.subpackage import name`.
>    -   **When to Use:**
>        -   This is the **recommended default** for most imports, especially for modules outside the current package or for top-level scripts.
>        -   They are clear, unambiguous, and make it easy to understand where a module is coming from regardless of the current file's location.
>        -   More robust to refactoring if you move files around (as long as the top-level package structure relative to `sys.path` remains).
>    -   **Example:**
>        Assuming a project structure:
>        ```
>        my_project/
>            main.py
>            ecommerce/
>                __init__.py
>                utils.py
>                products/
>                    __init__.py
>                    catalog.py
>        ```
>        In `main.py` or `ecommerce/products/catalog.py`, to import `utils.py`:
>        ```python
>        # Absolute import
>        import ecommerce.utils
>        from ecommerce.utils import helper_function
>        ```
>- Relative Imports
>    -   **Definition:** Specify the module to be imported *relative* to the location of the current module. They use leading dots (`.` or `..`) to indicate current and parent directories.
>    -   **Syntax:**
>        -   `from . import sibling_module` (imports `sibling_module` from the same package as the current module)
>        -   `from .sibling_module import name`
>        -   `from .. import parent_package_module` (imports `parent_package_module` from the parent package)
>        -   `from ..parent_package_module import name`
>    -   **When to Use:**
>        -   Primarily used for imports **within the same package**. They make it easier to reorganize the internal structure of a package without having to update import statements that refer to modules within that package.
>        -   They help avoid hardcoding the top-level package name within the package itself, making the package more self-contained and easier to rename or move.
>    -   **Cannot be used in top-level scripts:** Relative imports are meant for modules within packages. Trying to use them in a script that is run directly (i.e., when `__name__ == "__main__"`) will result in an `ImportError` because the notion of "current package" is not well-defined for top-level scripts.
>    -   **Example (inside `ecommerce/products/catalog.py`):**
>        To import `inventory.py` (assuming it's in the same `products` sub-package):
>        ```python
>        # In ecommerce/products/catalog.py
>        from . import inventory # Relative import for a sibling module
>        from .inventory import check_stock
>        
>        # To import utils.py from the parent 'ecommerce' package:
>        from ..utils import format_price 
>        ```
>
>**PEP 8 Recommendation:** Absolute imports are generally recommended for clarity and explicitness. However, relative imports are acceptable and often preferred for intra-package imports to make packages more self-contained and easier to refactor. Avoid complex relative imports like `from ...some_other_branch import name`.

## The Module Search Path (`sys.path`)
When an `import` statement is encountered, Python searches for the module in a list of directories specified by `sys.path`. This list typically includes:
1.  The directory containing the input script (or the current directory if running interactively).
2.  Directories listed in the `PYTHONPATH` environment variable (if set).
3.  Installation-dependent default paths (e.g., where standard library modules and site-packages are installed).

You can inspect `sys.path` to see where Python is looking:
```python
import sys
# print(sys.path)
```

The import system is a powerful feature that allows Python programs to be structured logically and to leverage a vast ecosystem of libraries.

---