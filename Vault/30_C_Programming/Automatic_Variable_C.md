---
tags: [c, concept, variable, scope, memory, lifetime]
aliases: [C Auto Variables, Stack Variables C]
related:
  - "[[Local_Variable_C]]"
  - "[[Scope_C]]"
  - "[[Stack_Memory_C]]"
  - "[[Static_Variable_C]]"
  - "[[Storage_Duration_C]]"
  - "[[auto_keyword_C]]"
worksheet: [C_WS3]
date_created: 2025-04-11
---
# Automatic Variable (C)

## Definition

An **Automatic Variable** in C is a [[Local_Variable_C|local variable]] that has *automatic storage duration*. This is the default behavior for variables declared inside functions or blocks without the `static` or `extern` storage class specifiers. Automatic variables are created when their defining block or function is entered and destroyed when it is exited.

## Key Aspects / Characteristics

- **Storage Duration:** Automatic (temporary). Exists only during the execution of the block/function where it's defined.
- **Storage Location:** Typically allocated on the [[Stack_Memory_C|call stack]] within the function's activation record (stack frame).
- **Scope:** [[Local_Variable_C|Local scope]] (block or function scope).
- **Initialization:** **Not** initialized by default. Contains indeterminate ("garbage") values unless explicitly initialized in the definition. Each time the function/block is entered, a new instance is created, and if not initialized, its value is unpredictable.
- **`auto` Keyword:** The `auto` keyword can be used explicitly (`auto int x;`), but it's redundant as it's the default for local variables. It's rarely used in modern C.
- **Recursion:** Each recursive call to a function gets its own separate set of automatic variables on the stack.

## Examples / Use Cases

```c
#include <stdio.h>

void counter() {
    int auto_count = 0; // Automatic variable, initialized to 0 *each time*
    auto_count++;
    printf("auto_count = %d\n", auto_count);
}

int factorial(int n) {
    if (n <= 1) {
        int base_case_var = 1; // Automatic variable for this call
        return base_case_var;
    } else {
        int recursive_result; // Automatic variable for this call
        recursive_result = n * factorial(n - 1); // Each call gets own 'n' and 'recursive_result'
        return recursive_result;
    }
}

int main() {
    printf("Calling counter:\n");
    counter(); // auto_count becomes 1
    counter(); // auto_count becomes 1 again (new instance)
    counter(); // auto_count becomes 1 again (new instance)

    printf("\nCalculating factorial(4):\n");
    int fact4 = factorial(4); // Demonstrates separate auto vars in recursion
    printf("Factorial of 4 is %d\n", fact4);

    return 0;
}
```
**Output:**
```
Calling counter:
auto_count = 1
auto_count = 1
auto_count = 1

Calculating factorial(4):
Factorial of 4 is 24
```

## Related Concepts
- [[Local_Variable_C]] (Automatic is the default storage duration for locals)
- [[Scope_C]] (Local scope)
- [[Stack_Memory_C]] (Typical storage location)
- [[Storage_Duration_C]] (Automatic vs. Static vs. Allocated)
- [[Static_Variable_C]] (Local variables with static duration, preserving value between calls)
- [[Initialization_C]] (Crucial for automatic variables to avoid garbage values)
- [[auto_keyword_C]] (Explicit but redundant keyword)

---
**Source:** Worksheet C_WS3