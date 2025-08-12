---
tags:
  - python
  - programming_paradigms
  - dynamic_typing
  - static_typing
  - type_checking
  - concept_comparison
aliases:
  - Dynamic Typing
  - Static Typing
  - Python Typing
related:
  - "[[Python_Language_Overview]]"
  - "[[Interpreted_vs_Compiled_Languages]]"
  - "[[Python_Type_Hinting]]"
worksheet:
  - WS16
date_created: 2025-06-11
---
# Dynamic Typing vs. Static Typing

**Typing** in programming languages refers to how data types are associated with variables and how type correctness is enforced. The two main approaches are static typing and dynamic typing.

## Static Typing
-   **Definition:** In statically-typed languages, the data type of a variable is known and checked at **compile-time**. Variables are typically declared with a specific type, and the compiler verifies that operations performed on these variables are compatible with their declared types.
-   **Type Checking:** Performed *before* program execution (during compilation).
-   **Characteristics:**
    -   **Early Error Detection:** Type errors (e.g., trying to add a string to an integer without explicit conversion) are caught by the compiler before the program runs. This can lead to more robust code.
    -   **Performance:** Knowing types at compile-time can allow for various optimizations by the compiler, potentially leading to faster execution.
    -   **Verbosity (Often):** Often requires explicit type declarations for variables (e.g., `int age = 30;` in C++ or Java).
    -   **Less Flexibility (Potentially):** Can sometimes feel more restrictive during rapid prototyping if types need to be changed frequently.
-   **Examples of Statically-Typed Languages:** C, C++, Java, C#, Go, Rust, Swift, Scala, Haskell.

**Example (Conceptual C++):**
```cpp
// int age = 30;       // 'age' is declared as an integer
// age = "hello";    // COMPILE-TIME ERROR: cannot assign string to int variable
// std::string name = "Alice";
// int result = age + name; // COMPILE-TIME ERROR: cannot add int and string
```

## Dynamic Typing
-   **Definition:** In dynamically-typed languages, the data type of a variable is associated with the **value** it holds at runtime, not with the variable name itself. Type checking is performed **during runtime** as the program executes.
-   **Type Checking:** Performed *during* program execution.
-   **Characteristics:**
    -   **Flexibility:** Variables can hold values of different types at different times during execution. No explicit type declarations are usually needed for variables.
    -   **Rapid Prototyping:** Often faster to write initial code due to less type boilerplate.
    -   **Later Error Detection:** Type errors are only caught when the problematic line of code is executed. This might mean errors surface later in the development cycle or even in production if not thoroughly tested.
    -   **Performance (Potentially Slower):** Runtime type checking can add overhead. Optimizations based on type information are harder for the interpreter/runtime to make ahead of time (though techniques like JIT compilation can mitigate this).
-   **Examples of Dynamically-Typed Languages:** Python, JavaScript, Ruby, PHP, Perl, Lisp.

**Example (Python):**
```python
age = 30          # 'age' now holds an integer value
print(type(age))  # Output: <class 'int'>

age = "thirty"    # 'age' now holds a string value. This is allowed.
print(type(age))  # Output: <class 'str'>

name = "Alice"
# result = age + 5  # RUNTIME TypeError: can only concatenate str (not "int") to str (if age is "thirty")
# result = name + 5 # RUNTIME TypeError: can only concatenate str (not "int") to str
```
In Python, the variable `age` is just a name pointing to an object. The object has a type. `age` can be reassigned to point to an object of a different type.

## Python's Typing System
-   Python is **dynamically typed**. You don't declare variable types.
-   Python is also **strongly typed**. This means that while a variable can change its type, operations between incompatible types are not implicitly allowed and will raise a `TypeError`. For example, you cannot directly add an integer and a string (`5 + "hello"`) without explicit conversion (`str(5) + "hello"` or `5 + int("10")`). This contrasts with weakly-typed languages (like some versions of JavaScript or PHP) which might try to automatically coerce types, sometimes leading to unexpected results.

## Type Hinting in Python (Optional Static Analysis)
Since Python 3.5+, **type hints** (see [[Python_Type_Hinting]]) have been introduced. These allow developers to optionally annotate variables, function arguments, and return values with their expected types.
-   Type hints **do not change Python's dynamic typing** at runtime by default. The standard Python interpreter (CPython) does not enforce them.
-   They are primarily used by **static analysis tools** (like MyPy, Pyright, Pytype) to catch type errors *before* runtime, bringing some of the benefits of static typing to Python development.
-   They also improve code readability and maintainability.

**Example with Type Hints:**
```python
def greet(name: str) -> str:
    return "Hello, " + name

# age: int = 30
# message: str = greet(age) # A static type checker like MyPy would flag this line as an error.
                          # Python itself would run it but might error later if 'age' isn't string-compatible.
```

## Comparison Summary

[list2mdtable|#Dynamic vs Static Typing]
- Feature
    - Static Typing
        - Dynamic Typing
- **Type Checking Time**
    - Compile-time (before execution)
        - Runtime (during execution)
- **Variable Declaration**
    - Usually requires explicit type declaration.
        - No explicit type declaration needed; type is associated with value.
- **Error Detection (Type Errors)**
    - Early (at compile-time).
        - Late (at runtime, when code is executed).
- **Flexibility**
    - Less flexible; variable type is fixed.
        - More flexible; variable can hold different types over time.
- **Performance**
    - Can allow for more compiler optimizations; potentially faster.
        - Runtime type checking can add overhead; potentially slower (though JITs help).
- **Readability/Verbosity**
    - Can be more verbose due to type declarations.
        - Can be less verbose. Type hints in Python improve readability.
- **Python's Approach**
    - (With Type Hints + Static Analyzer) Can achieve some benefits.
        - Primarily dynamically typed (but strongly typed).

The choice between static and dynamic typing involves trade-offs between development speed, flexibility, performance, and early error detection.

---