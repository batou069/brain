---
tags:
  - python
  - scope
  - namespace
  - module
  - import
  - legb
  - concept
  - moc
aliases:
  - Python Scopes MOC
  - Python Modules MOC
  - Python Namespaces MOC
related:
  - "[[100_Python/_Python_Programming_MOC|_Python_Programming_MOC]]"
  - "[[Python_LEGB_Rule|LEGB Rule (Scope Resolution)]]"
  - "[[Python_Namespaces|Namespaces]]"
  - "[[Python_Modules_Packages|Modules and Packages]]"
  - "[[Python_Import_System|The `import` System (`import`, `from ... import`)]]"
  - "[[Python_global_Keyword|`global` Keyword]]"
  - "[[Python_nonlocal_Keyword|`nonlocal` Keyword (from Functions MOC)]]"
  - "[[Python_dunder_name|`__name__` Special Variable]]"
  - "[[Python_Script_vs_Module|Executing Modules as Scripts (`if __name__ == '__main__':`)]]"
  - "[[Python_Built_In_Modules_OS|OS Module]]"
  - "[[Python_Built_In_Modules_Sys|sys Module]]"
worksheet:
  - WS19
date_created: 2025-08-20
---
# Python Scopes and Modules MOC 📦🔍

This section delves into how Python manages names (variables, functions, classes) using **scopes** and **namespaces**, and how code is organized into reusable units called **modules** and packages. Understanding these concepts is crucial for writing well-structured, maintainable, and conflict-free Python programs.

## Core Concepts
-   [[Python_Scopes_Visibility|Scopes and Visibility]]
    -   What is a scope? How does it define the visibility of a name?
-   [[Python_Namespaces|Namespaces]]
    -   What are namespaces? How Python uses them to avoid name collisions.
    -   Operations in Python that create names in namespaces.
-   [[Python_LEGB_Rule|LEGB Rule (Scope Resolution)]]
    -   The order Python follows to look up names: Local, Enclosing function locals, Global, Built-in.
-   [[Python_global_Keyword|The `global` Keyword]]
    -   Accessing and modifying global variables from within a function.
    -   Why modifying globals is often discouraged.
-   [[Python_Nested_Functions_Closures#The nonlocal Keyword|The `nonlocal` Keyword]] (Covered in Functions)
    -   Modifying variables in an enclosing function's scope.
-   [[Python_Modules_Packages|Modules and Packages]]
    -   Organizing code into reusable files (modules) and directories (packages).
    -   Advantages of modularizing code.
-   [[Python_Import_System|The `import` System]]
    -   `import module_name`
    -   `from module_name import specific_name`
    -   `from module_name import *` (and its dangers)
    -   Absolute vs. Relative imports.
-   [[Python_dunder_name|The `__name__` Special Variable]]
-   [[Python_Script_vs_Module|Executing Modules as Scripts (`if __name__ == '__main__':`)]]
    -   How to make a module runnable as a script.
-   [[Python_reload_function|`importlib.reload()` (formerly `reload()`)]]

## Built-in Functions & Modules Related to Scope/Modules
-   [[Built_In_Functions_Python#globals()|`globals()`]]
-   [[Built_In_Functions_Python#locals()|`locals()`]]
-   [[Python_Built_In_Modules_OS|`os` Module]] (Overview)
-   [[Python_Built_In_Modules_Sys|`sys` Module]] (Overview, including `sys.argv`, `sys.path`)

## Notes in this Section
```dataview
LIST
FROM "100_Python/Python_Scopes_Modules"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
```

---