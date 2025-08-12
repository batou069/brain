---
tags: [c, macro, library, debugging, testing, error_handling]
aliases: [assert macro]
related:
  - "[[Debugging_Techniques_C]]"
  - "[[Error_Handling_C]]"
  - "[[Preprocessor_C]]"
  - "[[Macro_C]]"
  - "[[NDEBUG]]"
worksheet: [C_WS3]
header_file: <assert.h>
date_created: 2025-04-11
---
# ` assert() `

## Purpose

`assert()` is a macro defined in `<assert.h>` used for [[Debugging_Techniques_C|debugging]]. It tests an **assertion** (an expression assumed to be true) at a specific point in the program. If the expression evaluates to false (0), `assert()` prints an error message to `stderr` (standard error) indicating the failed assertion, the source file name, the line number, and the enclosing function name, and then terminates the program by calling `abort()`.

## Signature

```c
#include <assert.h>
void assert(scalar expression);
```
*(Note: `assert` is implemented as a macro, not a true function, but this shows its usage.)*

## Parameters

-   `expression`: Any scalar expression (arithmetic or pointer type). If this expression evaluates to logical false (zero), the assertion fails.

## Return Value

-   `assert` returns no value (`void`). Its effect is either nothing (if the assertion is true) or program termination (if the assertion is false).

## Key Aspects

-   **Debugging Aid:** Used to check for conditions that *should* always be true if the program logic is correct (e.g., preconditions, postconditions, invariants). Helps catch logical errors early during development.
-   **Failure Action:** If `expression == 0`, prints a diagnostic message to `stderr` (e.g., `Assertion failed: expression, file filename, line N, function funcname`) and calls `abort()` to terminate the program immediately.
-   **Conditional Compilation:** Assertions can be disabled at compile time by defining the macro `NDEBUG` (No Debug). If `NDEBUG` is defined *before* `<assert.h>` is included, the `assert(expression)` macro expands to nothing `((void)0)`, effectively removing the check and the associated overhead from the production code. This is commonly done for release builds.
    ```bash
    # Example compilation command to disable asserts
    gcc main.c -o main -DNDEBUG
    ```
-   **Not for Error Handling:** `assert` should **not** be used for handling expected runtime errors (like invalid user input or file-not-found errors). It's meant for detecting internal programming errors (bugs). Runtime errors should be handled gracefully (e.g., using `if` checks and returning error codes or printing user-friendly messages).

## Example Usage

```c
#include <stdio.h>
#include <stdlib.h>
#include <assert.h> // Required for assert()

// Function with a precondition check using assert
double calculate_ratio(int numerator, int denominator) {
    // Precondition: denominator must not be zero
    assert(denominator != 0); // Program terminates here if denominator is 0 (in debug builds)

    // If assert passes, proceed with calculation
    return (double)numerator / denominator;
}

int main(int argc, char *argv[]) {
    int x = 10;
    int y = 5;
    double ratio;

    printf("Calculating ratio for %d / %d\n", x, y);
    ratio = calculate_ratio(x, y);
    printf("Ratio: %f\n", ratio);

    // Example with a pointer check
    int *ptr = (int*)malloc(sizeof(int));
    assert(ptr != NULL); // Check if malloc succeeded
    *ptr = 100;
    printf("Pointer value: %d\n", *ptr);
    free(ptr);
    ptr = NULL;

    // Example that will likely fail (if run without -DNDEBUG)
    y = 0;
    printf("\nCalculating ratio for %d / %d\n", x, y);
    ratio = calculate_ratio(x, y); // Assertion failure expected here
    printf("Ratio: %f\n", ratio); // This line likely won't be reached

    return 0;
}
```
**Output (when run normally):**
```
Calculating ratio for 10 / 5
Ratio: 2.000000
Pointer value: 100

Calculating ratio for 10 / 0
Assertion failed: denominator != 0, file main.c, line 10, function calculate_ratio
Aborted (core dumped)
```
**Output (when compiled with `-DNDEBUG`):**
```
Calculating ratio for 10 / 5
Ratio: 2.000000
Pointer value: 100

Calculating ratio for 10 / 0
Floating point exception (core dumped) // Crash due to division by zero, assert was disabled
```

## Related Functions/Concepts
- [[Debugging_Techniques_C]] (Asserts are a key technique)
- [[Error_Handling_C]] (Asserts are *not* for runtime error handling)
- [[Preprocessor_C]], [[Macro_C]] (`assert` is a macro)
- [[NDEBUG]] (Macro used to disable asserts)
- `abort()` (Function called by `assert` on failure)
- `stderr` ([[stdout_stdout_stderr_C|Standard error stream]] where the message is printed)

---
**Source:** Worksheet C_WS3