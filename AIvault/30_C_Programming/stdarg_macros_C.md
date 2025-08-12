---
tags: [c, concept, macro, library, function, stdarg]
aliases: [va_list, va_start, va_arg, va_end, va_copy]
related:
  - "[[Variable_Length_Parameter_List_C]]"
  - "[[Function_C]]"
  - "[[Macro_C]]"
  - "[[Header_file_C]]"
worksheet: [C_WS3] # Implicitly related via Variable Length Parameter Lists
date_created: 2025-04-11
---
# `<stdarg.h>` Macros (C)

## Definition

The `<stdarg.h>` header file in the C Standard Library provides macros that allow functions to access their [[Variable_Length_Parameter_List_C|variable arguments]] (arguments passed via the ellipsis `...` notation). These macros provide a portable way to traverse the argument list passed on the [[Stack_Memory_C|stack]] or via registers during a function call.

## Key Macros

-   **`va_list`**:
    -   A type suitable for holding the information needed by `va_start`, `va_arg`, `va_end`, and `va_copy`. You declare a variable of this type within your variadic function.
    -   Example: `va_list my_args;`

-   **`va_start(va_list ap, last_named_param)`**:
    -   Initializes the `va_list` variable `ap` to point to the first variable argument.
    -   `last_named_param` **must** be the identifier of the *last named parameter* in the function's parameter list (the one immediately preceding the `...`).
    -   Must be called before any `va_arg` calls.
    -   Example: `va_start(my_args, count);` (where `count` is the last named parameter).

-   **`va_arg(va_list ap, type)`**:
    -   Retrieves the value of the *next* variable argument from the list pointed to by `ap`.
    -   `type` specifies the data type that the argument is expected to have *after default argument promotions* (`char`/`short` -> `int`, `float` -> `double`).
    -   It modifies `ap` to point to the subsequent argument.
    -   Using an incorrect `type` leads to [[Undefined_Behavior_C]]. The function must have some way (e.g., via a format string or count parameter) to know the expected type of the next argument.
    -   Example: `int next_int = va_arg(my_args, int);`, `double next_double = va_arg(my_args, double);`

-   **`va_end(va_list ap)`**:
    -   Performs necessary cleanup on the `va_list` variable `ap` after all arguments have been processed.
    -   **Must** be called before the function returns if `va_start` was called. Failure to call `va_end` can lead to undefined behavior or resource leaks on some systems.
    -   Example: `va_end(my_args);`

-   **`va_copy(va_list dest, va_list src)`** (C99+):
    -   Creates a copy (`dest`) of the current state of another `va_list` (`src`).
    -   Useful if you need to scan through the variable arguments multiple times.
    -   The `dest` `va_list` must also be cleaned up using `va_end`.
    -   Example: `va_copy(args_copy, my_args);`

## Usage Pattern

```c
#include <stdarg.h>

return_type function_name(named_param1, ..., last_named_param, ...) {
    // 1. Declare va_list variable
    va_list ap;

    // 2. Initialize va_list
    va_start(ap, last_named_param);

    // 3. Access arguments using va_arg
    while (/* condition to continue processing args */) {
        type current_arg = va_arg(ap, type);
        // ... process current_arg ...
    }

    // 4. Clean up va_list
    va_end(ap);

    // ... rest of function ...
    return value;
}

```

## Related Concepts
- [[Variable_Length_Parameter_List_C]] (The feature these macros enable)
- [[Macro_C]] (These are implemented as macros, not functions)
- [[Header_file_C]] (`<stdarg.h>` must be included)
- [[Stack_Memory_C]] (Where arguments are often passed, accessed indirectly via these macros)
- [[Undefined_Behavior_C]] (Risk if macros are used incorrectly, especially `va_arg` with wrong type)

---
**Source:** Worksheet C_WS3 (Implicit)