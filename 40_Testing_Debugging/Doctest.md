---
tags:
  - testing
  - python
  - library
  - documentation
  - unit_test
aliases:
  - doctest module
related:
  - "[[Python]]"
  - "[[Unit_Test]]"
  - "[[PyUnit]]"
  - "[[Pytest]]"
  - "[[Documentation]]"
  - "[[REPL]]"
worksheet: [WS24]
date_created: 2025-04-21
---
# Doctest

## Definition

**Doctest** is a module included in the Python standard library that allows tests to be embedded directly within docstrings. It works by searching for pieces of text that look like interactive Python sessions ([[REPL]]) within the docstrings, executing those sessions, and verifying that the output matches the expected output shown in the docstring.

## Purpose

- **Combine Documentation and Testing:** Ensures that documentation examples remain correct and up-to-date as the code evolves. If the code changes and breaks an example, the doctest will fail.
- **Simple Usage Examples as Tests:** Provides a very simple way to test basic functionality using the kind of examples often included in documentation anyway.
- **Living Documentation:** Makes documentation more reliable and useful.

## How it Works

- **Scanning:** The `doctest` module scans module docstrings, function docstrings, class docstrings, and method docstrings (and optionally external text files).
- **REPL Syntax:** It looks for lines starting with the Python interactive prompt `>>> ` followed by code, and subsequent lines showing the expected output exactly as it would appear in the REPL. Blank lines are used to terminate expected output.
  ```python
  >>> function_call(argument)
  Expected Output
  ```
- **Execution:** Doctest executes the code found after `>>> ` prompts.
- **Comparison:** It compares the actual output produced by executing the code with the expected output listed immediately below it in the docstring. Whitespace differences can matter unless options are used.
- **Reporting:** Reports any discrepancies as test failures.

## Example

```python
# my_module.py

def add(a, b):
    """
    Adds two numbers together.

    Examples:
        >>> add(2, 3)
        5
        >>> add(-1, 1)
        0
        >>> add(10, -5)
        5

    Handles non-numeric types by raising TypeError:
        >>> add("a", 3)
        Traceback (most recent call last):
            ...
        TypeError: Inputs must be numeric
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Inputs must be numeric")
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod() 
    # Discover and run doctests in this module
```

## Running Doctests

- **From within the module:** Add `import doctest; doctest.testmod()` inside an `if __name__ == "__main__":` block, then run the module directly (`python my_module.py`). Add `-v` for verbose output (`python my_module.py -v`).
- **From the command line:** `python -m doctest my_module.py` (or `-v` for verbose).
- **Integration with other frameworks:** [[Pytest]] can discover and run doctests automatically (often enabled via command-line flag like `pytest --doctest-modules`).

## Advantages

- Keeps documentation examples accurate.
- Simple way to write basic tests for simple functions.
- Encourages writing clear, example-based documentation.

## Disadvantages

- Not suitable for complex test logic, setup/teardown (fixtures), or testing non-deterministic behavior.
- Sensitive to exact output formatting (including whitespace).
- Can clutter docstrings if overused for complex testing.
- Best used as a supplement to, not a replacement for, more robust frameworks like [[PyUnit]] or [[Pytest]].

## Related Concepts
- [[Python]], [[Documentation]], Docstrings
- [[Unit_Test]] (Doctests serve as simple unit tests)
- [[PyUnit]], [[Pytest]] (More comprehensive testing frameworks)
- [[REPL]] (Syntax mimics the interactive prompt)

## Questions / Further Study
>[!question] Explain how Doctest works. (WS24)
> Doctest works by scanning Python docstrings (or text files) for text formatted like an interactive Python session (`>>> code` followed by expected output). It executes the `code` part and compares the actual output generated with the `expected output` written in the docstring. If they match exactly, the test passes; otherwise, it fails.

---
**Source:** Worksheet WS24, Python `doctest` documentation