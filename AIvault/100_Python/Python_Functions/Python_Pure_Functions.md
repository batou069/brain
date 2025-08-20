---
tags:
  - python
  - functions
  - pure_functions
  - functional_programming
  - side_effects
  - determinism
  - concept
  - example
aliases:
  - Pure Function Python
related:
  - "[[100_Python/Python_Functions/_Python_Functions_MOC|_Python_Functions_MOC]]"
  - "[[Python_Higher_Order_Functions]]"
  - "[[Python_Mutability_Immutability|Mutability and Immutability in Python]]"
worksheet:
  - WS18
date_created: 2025-08-20
---
# Python: Pure Functions

A **pure function** is a concept from functional programming that describes a function with two main properties:

1.  **Deterministic:** Given the same input arguments, the function will **always return the same output value**. It does not depend on any hidden state or external factors that might change between calls.
2.  **No Side Effects:** The function's execution does **not cause any observable changes outside its local scope**. This means it doesn't modify global variables, mutable arguments passed by reference, perform I/O operations (like printing to console, reading/writing files, network requests), or call other non-pure functions that have side effects.

## Characteristics of Pure Functions
-   **Predictable:** Their behavior is entirely determined by their input values.
-   **Testable:** Easy to test because you only need to check if the output is correct for a given input, without worrying about external state or side effects.
-   **Referential Transparency:** An expression involving a pure function call can be replaced by its return value without changing the program's behavior.
-   **Concurrency-Friendly:** Since they don't modify shared state, pure functions are inherently easier to parallelize and use in concurrent environments without race conditions.
-   **Cacheable/Memoizable:** The results of pure functions can be cached (memoized) because they always produce the same output for the same input.

>[!question] What is "Pure function" and "Higher-order Function"? Give 3 examples For each of them.

## Pure Functions
(Definition above)

**Examples of Pure Functions in Python:**
1.  **Simple Arithmetic Function:**
    ```python
    def add_numbers(x: float, y: float) -> float:
        """Returns the sum of x and y. Pure function."""
        return x + y
    
    print(add_numbers(2, 3))    # Always 5
    print(add_numbers(2, 3))    # Still 5, no side effects
    print(add_numbers(-1, 10))  # Always 9
    ```
    -   *Deterministic:* `add_numbers(2, 3)` will always return `5`.
    -   *No Side Effects:* It doesn't print anything, modify global variables, or change its input arguments (numbers are immutable).

2.  **String Manipulation Function:**
    ```python
    def create_greeting(name: str) -> str:
        """Returns a greeting string for the given name. Pure function."""
        return f"Hello, {name}!"
    
    print(create_greeting("Alice")) # Always "Hello, Alice!"
    print(create_greeting("Bob"))   # Always "Hello, Bob!"
    ```    -   *Deterministic:* Output depends only on the `name` argument.
    -   *No Side Effects:* Strings are immutable; a new string is created and returned.

3.  **List Transformation (returning a new list):**
    ```python
    def square_elements(numbers: list[int]) -> list[int]:
        """Returns a NEW list with each element squared. Pure function."""
        return [x**2 for x in numbers]

    original_list = 
    squared_list1 = square_elements(original_list)
    squared_list2 = square_elements(original_list) # original_list is unchanged
    
    print(f"Original: {original_list}")
    print(f"Squared 1: {squared_list1}") # [1, 4, 9, 16]
    print(f"Squared 2: {squared_list2}") # [1, 4, 9, 16] (same result)
    print(f"Original still unchanged: {original_list}")
    ```
    -   *Deterministic:* Given the same input list content, it always produces the same new list of squared numbers.
    -   *No Side Effects:* It does not modify the original `numbers` list. It creates and returns a *new* list. If it modified `numbers` in-place, it would not be pure.

## Impure Functions (Examples for Contrast)

1.  **Modifies Global State:**
    ```python
    # total_calls = 0
    # def count_function_calls():
    #     """Impure: Modifies a global variable."""
    #     global total_calls
    #     total_calls += 1
    #     return total_calls
    ```
2.  **Performs I/O (Printing):**
    ```python
    # def greet_with_print(name):
    #     """Impure: Has a side effect (printing to console)."""
    #     message = f"Hello, {name}!"
    #     print(message) # Side effect
    #     return message
    ```
3.  **Modifies Mutable Arguments In-Place:**
    ```python
    # def append_to_list_impure(item, target_list):
    #     """Impure: Modifies its mutable argument 'target_list'."""
    #     target_list.append(item)
    #     return target_list # Returning it doesn't make it pure if it was modified
    ```
4.  **Depends on External State (e.g., current time, random numbers):**
    ```python
    # import datetime
    # def get_current_time_string():
    #     """Impure: Output depends on external state (current time)."""
    #     return str(datetime.datetime.now())

    # import random
    # def get_random_number():
    #     """Impure: Output is not deterministic."""
    #     return random.randint(1, 100)
    ```

While not all functions can or should be pure (e.g., functions dealing with I/O inherently have side effects), striving to write pure functions for computational logic can lead to more robust, testable, and maintainable code. Pure functions are easier to reason about because their behavior is self-contained.

The concept of [[Python_Higher_Order_Functions|Higher-Order Functions]] is distinct but often benefits from using pure functions as arguments or return values.

---