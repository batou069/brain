---
tags:
  - python
  - functions
  - recursion
  - algorithm
  - base_case
  - recursive_step
  - concept
  - example
aliases:
  - Recursive Functions Python
  - Python Recursive Call
related:
  - "[[100_Python/Python_Functions/_Python_Functions_MOC|_Python_Functions_MOC]]"
  - "[[Stack_Overflow_Error]]"
worksheet:
  - WS18
date_created: 2025-08-20
---
# Python: Recursion

**Recursion** is a programming technique where a function calls itself in order to solve a problem. A recursive function breaks a problem down into smaller, self-similar subproblems until it reaches a simple enough case that can be solved directly (the base case).

## Key Components of a Recursive Function
1.  **Base Case(s):**
    -   One or more conditions under which the function does not call itself again.
    -   This is crucial to prevent infinite recursion and a [[Stack_Overflow_Error|stack overflow error]].
    -   The base case provides a direct solution for the simplest instance of the problem.
2.  **Recursive Step (Recursive Call):**
    -   The part of the function where it calls itself, but with modified arguments that move it closer to a base case.
    -   The problem is broken down into a smaller or simpler version of the same problem.

## How Recursion Works
When a function calls itself, a new frame is added to the call stack to store the local variables and state of that particular call. When the recursive call returns, its frame is popped from the stack, and execution resumes in the calling frame. This continues until the base case is reached and the chain of calls unwinds.

## Example: Factorial Calculation
The factorial of a non-negative integer $n$, denoted by $n!$, is the product of all positive integers less than or equal to $n$.
-   $0! = 1$ (base case)
-   $n! = n \times (n-1)!$ for $n > 0$ (recursive step)

```python
def factorial_recursive(n: int) -> int:
    """Calculates factorial of n using recursion."""
    # Base case: factorial of 0 or 1 is 1
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0 or n == 1:
        return 1
    # Recursive step: n * (n-1)!
    else:
        return n * factorial_recursive(n - 1)

# Test the function
# print(f"Factorial of 5: {factorial_recursive(5)}")  # Output: 120 (5*4*3*2*1)
# print(f"Factorial of 0: {factorial_recursive(0)}")  # Output: 1
# print(f"Factorial of 1: {factorial_recursive(1)}")  # Output: 1
# try:
#     factorial_recursive(-2)
# except ValueError as e:
#     print(f"Error: {e}")
```

## Example: Sum of Elements in a List (Conceptual E-commerce Order Total)
Imagine an RDD-like structure or list of item prices from an order.
```python
def sum_list_recursive(data_list: list) -> float:
    """Calculates the sum of elements in a list using recursion."""
    # Base case: if the list is empty, sum is 0
    if not data_list: # or len(data_list) == 0
        return 0
    # Recursive step: first element + sum of the rest of the list
    else:
        return data_list[0] + sum_list_recursive(data_list[1:])

# Test the function
# item_prices = 
# total_order_value = sum_list_recursive(item_prices)
# print(f"Item prices: {item_prices}")
# print(f"Total order value: ${total_order_value:.2f}") # Output: $185.94

# empty_order = []
# print(f"Total for empty order: ${sum_list_recursive(empty_order):.2f}") # Output: $0.00
```

## Advantages of Recursion
-   **Elegance and Readability:** For problems that are naturally recursive (e.g., tree traversals, fractals, some mathematical functions like factorial or Fibonacci), recursive solutions can be very concise, elegant, and easier to understand than iterative solutions.
-   **Problem Decomposition:** Matches well with divide-and-conquer strategies.

## Disadvantages of Recursion
-   **Performance Overhead:** Each function call adds a new frame to the call stack, consuming memory and time. For deep recursion, this can be less efficient than an iterative solution.
-   **Stack Overflow Risk:** If the recursion is too deep (i.e., too many nested function calls without reaching a base case quickly enough), it can exhaust the call stack memory, leading to a [[Stack_Overflow_Error|stack overflow error]]. Python has a default recursion limit (often around 1000-3000 calls), which can be changed with `sys.setrecursionlimit()`, but this is generally not recommended as a primary solution.
-   **Debugging:** Tracing the flow of execution in recursive functions can sometimes be more challenging than in iterative ones.
-   **Not Always Intuitive:** For problems that are not inherently recursive, forcing a recursive solution can make the code harder to understand.

## Recursion vs. Iteration
Many problems that can be solved recursively can also be solved iteratively (using loops like `for` or `while`).
-   Iterative solutions often use less memory (no deep call stack) and can be faster due to less function call overhead.
-   Recursive solutions can be more intuitive for certain problems.

**Tail Recursion:**
Some programming languages perform **tail call optimization (TCO)**, where a recursive call that is the very last operation in a function (a tail call) can be optimized to not consume additional stack space, effectively behaving like an iteration. **Python does NOT perform tail call optimization.** Therefore, deep tail-recursive functions in Python can still lead to stack overflows.

When deciding whether to use recursion:
-   Consider if the problem has a natural recursive structure.
-   Be mindful of the potential depth of recursion and the risk of stack overflow.
-   If performance is critical for very deep call chains, an iterative solution might be preferable in Python.

Recursion is a powerful conceptual tool and a practical technique for solving certain types of problems elegantly.

---