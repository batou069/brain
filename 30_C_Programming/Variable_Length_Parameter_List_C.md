---
tags: [c, concept, syntax, function, stdarg]
aliases: [Variadic Functions C, Ellipsis Parameter C, ...]
related:
  - "[[Function_C]]"
  - "[[Function_Parameters_C]]"
  - "[[Function_Call_C]]"
  - "[[printf]]"
  - "[[scanf]]"
  - "[[stdarg_macros_C]]"
worksheet: [C_WS3]
date_created: 2025-04-11
---
# Variable Length Parameter List (C)

## Definition

C allows defining functions that can accept a variable number of arguments. These are often called **variadic functions**. This is achieved by using an ellipsis (`...`) as the last item in the [[Function_Parameters_C|parameter list]] in the function's declaration and definition. Special macros defined in the `<stdarg.h>` header are required to access these variable arguments within the function body.

## Key Aspects / Characteristics

- **Ellipsis (`...`):** Signals that zero or more additional arguments may be passed after the named parameters.
- **At Least One Named Parameter:** A variadic function *must* have at least one named parameter before the ellipsis. This named parameter (or information passed within it) is often used to determine the number and types of the variable arguments.
- **`<stdarg.h>` Macros:** Accessing the variable arguments requires using macros from `<stdarg.h>`:
    - `va_list`: A type to hold information about the variable arguments.
    - `va_start(ap, last_named_param)`: Initializes the `va_list` (`ap`). `last_named_param` is the name of the *last named parameter* before the ellipsis.
    - `va_arg(ap, type)`: Retrieves the next argument from the list, assuming it has the specified `type`. The caller *must* know the type.
    - `va_end(ap)`: Cleans up the `va_list`. Must be called before the function returns.
    - `va_copy(dest, src)`: (C99+) Creates a copy of the `va_list` state.
- **Type Safety Issues:** Variadic functions bypass standard function prototype type checking for the variable arguments. The function relies entirely on the caller passing arguments of the expected types and number, often based on information in the named parameters (like a format string in [[printf]]). Passing incorrect types leads to [[Undefined_Behavior_C]].
- **Default Argument Promotions:** Certain types passed as variable arguments undergo default promotions (e.g., `char`, `short` are promoted to `int`; `float` is promoted to `double`). `va_arg` must be used with the *promoted* type.

## Examples / Use Cases

**Example: Simple Sum Function**
```c
#include <stdio.h>
#include <stdarg.h>

// Function takes at least one integer (count), followed by 'count' integers to sum.
int sum_variadic(int count, ...) {
    va_list args; // Declare va_list variable
    int total = 0;
    int i;

    // Initialize args to point to the first variable argument
    va_start(args, count);

    // Loop 'count' times, retrieving each integer argument
    for (i = 0; i < count; ++i) {
        int num = va_arg(args, int); // Get next argument as an int
        total += num;
    }

    // Clean up the va_list
    va_end(args);

    return total;
}

int main() {
    int s1 = sum_variadic(3, 10, 20, 30);       // Pass 3 variable args
    int s2 = sum_variadic(5, 1, 2, 3, 4, 5); // Pass 5 variable args

    printf("Sum 1: %d\n", s1); // Output: 60
    printf("Sum 2: %d\n", s2); // Output: 15

    return 0;
}
```

**Common Standard Library Examples:**
- [[printf]], [[fprintf]], [[sprintf]], etc. (Format string determines types/number of args)
- [[scanf]], [[fscanf]], [[sscanf]], etc. (Format string determines types/number of pointer args)

## Related Concepts
- [[Function_C]], [[Function_Parameters_C]], [[Function_Call_C]]
- [[stdarg_macros_C]] (`va_list`, `va_start`, `va_arg`, `va_end`)
- [[printf]], [[scanf]] (Prominent users of this feature)
- [[Type_Cast_C]] (May be needed if types don't match exactly after promotion)
- [[Undefined_Behavior_C]] (Risk due to lack of type safety)

---
**Source:** Worksheet C_WS3