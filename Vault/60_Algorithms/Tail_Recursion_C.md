---
tags:
  - algorithms
  - concept
  - recursion
  - optimization
  - compiler
aliases:
  - Tail Call Optimization
  - TCO
  - Tail Recursion Optimization
related:
  - "[[Recursion_C]]"
  - "[[Function_Call_C]]"
  - "[[Stack_Memory_C]]"
  - "[[Stack_Overflow]]"
  - "[[Compiler_Optimization]]"
  - "[[Functional_Programming]]"
worksheet:
  - WS10
date_created: 2025-04-12
---
# Tail Recursion

## Definition

**Tail Recursion** occurs when a [[Recursion_C|recursive call]] is the **very last operation** performed in a function. This means there is no pending computation or operation to be done with the result of the recursive call after it returns; the result of the recursive call is directly returned by the calling function.

```c
// Example of Tail Recursion
int factorial_tail_recursive(int n, int accumulator) {
    if (n == 0) {
        return accumulator; // Base case returns accumulator
    } else {
        // Recursive call is the LAST thing done before returning
        return factorial_tail_recursive(n - 1, n * accumulator);
    }
}
// Initial call: factorial_tail_recursive(num, 1);

// Example of NON-Tail Recursion (standard factorial)
int factorial_standard(int n) {
    if (n == 0) {
        return 1;
    } else {
        // Multiplication happens *after* recursive call returns
        return n * factorial_standard(n - 1);
    }
}
```

## Tail Call Optimization (TCO)

The significance of tail recursion lies in an optimization technique called **Tail Call Optimization (TCO)** or Tail Recursion Optimization. Compilers that support TCO can recognize tail-recursive calls and optimize them by **reusing the current function's stack frame** instead of creating a new one for the recursive call.

- **How TCO Works:** Instead of pushing a new stack frame, the compiler can essentially replace the current frame's parameters with the arguments for the recursive call and perform a simple `goto` or jump back to the beginning of the function.
- **Effect:** Transforms the recursion into an iteration (a loop) at the machine code level.
- **Benefit:** Prevents [[Stack_Overflow|stack overflow]] errors for deep tail recursions, as the stack doesn't grow with each call. It also eliminates the overhead associated with function call setup and teardown for the recursive calls, making it as efficient as an iterative loop.

## C Compiler Support for TCO

- **Not Guaranteed:** The C standard does **not** require compilers to perform Tail Call Optimization.
- **Commonly Implemented (with Optimization):** Many modern C compilers (like [[GCC]], [[Clang_C]]) *can* perform TCO, but usually only when **optimization flags** are enabled (e.g., `-O1`, `-O2`, `-O3`). Without optimization, TCO is often disabled, and tail recursion will still consume stack space.
- **Verification:** It's often necessary to inspect the generated assembly code (`gcc -S -O2 ...`) to confirm if TCO has actually been applied for a specific function and compiler settings.

## Related Concepts
- [[Recursion_C]] (Tail recursion is a specific form)
- [[Function_Call_C]], [[Stack_Memory_C]], [[Stack_Overflow]] (TCO avoids stack growth)
- [[Compiler_Optimization]] (TCO is an optimization technique)
- Iteration (TCO effectively converts tail recursion to iteration)
- [[Functional_Programming]] (Tail recursion is heavily used and often guaranteed to be optimized in functional languages)

---
**Source:** Worksheet WS10