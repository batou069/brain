---
tags:
  - python
  - module
  - script
  - dunder_name
  - __name__
  - __main__
  - execution_context
  - concept
aliases:
  - __name__ variable
  - Python __name__
  - if __name__ == "__main__"
related:
  - "[[Python_Modules_Packages]]"
  - "[[Python_Import_System]]"
  - "[[Python_Script_vs_Module|Executing Modules as Scripts]]"
worksheet:
  - WS19
date_created: 2025-08-20
---
# Python: The `__name__` Special Variable

`__name__` (pronounced "dunder name," for double underscore name) is a special built-in variable in Python that is automatically set in every module. Its value depends on how the module is being used.

## Value of `__name__`

1.  **When a Module is Run Directly (as a Script):**
    -   If you execute a Python file directly (e.g., `python my_script.py`), the `__name__` variable within that script is set to the string `__main__`.
    -   This indicates that the script is the main program being run.

2.  **When a Module is Imported:**
    -   If a Python file is imported as a module into another script (e.g., `import my_module`), the `__name__` variable within `my_module.py` is set to the **name of the module itself** (as a string, e.g., `'my_module'`).

## The `if __name__ == "__main__":` Idiom

This common Python idiom leverages the behavior of the `__name__` variable to control code execution.

```python
# my_module.py

def helper_function():
    print("Helper function from my_module is called.")

def main_logic():
    print("Main logic of my_module is executing.")
    helper_function()

print(f"In my_module.py, __name__ is set to: {__name__}")

if __name__ == "__main__":
    # This block of code will ONLY execute if this script is run directly.
    # It will NOT execute if this module is imported by another script.
    print("my_module.py is being run directly.")
    main_logic()
else:
    # This block executes if the module is being imported.
    print("my_module.py is being imported into another module.")
```

**Scenario 1: Running `my_module.py` directly**
```bash
$ python my_module.py
```
Output:
```
In my_module.py, __name__ is set to: __main__
my_module.py is being run directly.
Main logic of my_module is executing.
Helper function from my_module is called.
```
Here, `__name__` inside `my_module.py` is `__main__`, so the code inside the `if` block executes.

**Scenario 2: Importing `my_module.py` into another script**
Let's say we have `another_script.py`:
```python
# another_script.py
import my_module # This will execute the top-level code in my_module.py

print("\nIn another_script.py, now using my_module:")
my_module.helper_function()
# my_module.main_logic() # We can still call it if we want
```
Output when running `python another_script.py`:
```
In my_module.py, __name__ is set to: my_module  <-- Note this!
my_module.py is being imported into another module.

In another_script.py, now using my_module:
Helper function from my_module is called.
```
Here, when `my_module` is imported, `__name__` inside `my_module.py` is `'my_module'`, so the `else` block executes, and the code inside `if __name__ == "__main__":` in `my_module.py` does *not* execute automatically upon import.

## Purpose and Advantages of `if __name__ == "__main__":`
1.  **Reusability:** Allows a Python file to serve a dual purpose:
    -   It can be **imported as a module** by other scripts, providing its functions and classes for reuse without automatically running example code or a main script logic.
    -   It can also be **executed as a standalone script**, typically to run tests, demonstrations, or a main application flow defined within the `if` block.
2.  **Preventing Unintended Execution:** Code that is intended only for when the file is the main program (like test calls, example usage, or application startup logic) is placed inside this block. This prevents it from running automatically every time the module is imported elsewhere.
3.  **Clarity and Convention:** It's a standard Python idiom that clearly signals the entry point for script execution.

>[!question] Can we execute a module as a script?
>Yes, any Python file (`.py`) can be executed as a script by passing its name to the Python interpreter (e.g., `python my_module.py`). When executed this way, its `__name__` variable is set to `__main__`. The `if __name__ == "__main__":` block allows you to define specific behavior for when the module is run as the main script.

The `__name__` variable and the `if __name__ == "__main__":` construct are fundamental for creating reusable Python modules that can also be run independently for testing or as top-level programs.

---