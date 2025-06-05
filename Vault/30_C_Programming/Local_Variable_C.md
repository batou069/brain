---
tags: [c, concept, variable, scope, memory]
aliases: [C Local Variables]
related:
  - "[[Scope_C]]"
  - "[[Function_C]]"
  - "[[Stack_Memory_C]]"
  - "[[Automatic_Variable_C]]"
  - "[[Static_Variable_C]]"
  - "[[Block_Scope_C]]"
worksheet: [C_WS3]
date_created: 2025-04-11
---
# Local Variable (C)

## Definition

A **Local Variable** in C is a variable declared inside a function body or a block (code enclosed in `{}`). Its [[Scope_C|scope]] is limited to the function or block in which it is defined, meaning it can only be accessed from within that specific function or block.

## Key Aspects / Characteristics

- **Scope:** Limited to the defining function or block ([[Block_Scope_C]]). It is not visible or accessible outside.
- **Lifetime (Default: Automatic):** By default, local variables have *automatic storage duration* ([[Automatic_Variable_C]]). They come into existence when the function or block is entered and cease to exist (memory is typically deallocated from the [[Stack_Memory_C|stack]]) when the function or block is exited. Their values are not preserved between calls (unless declared `static`).
- **Storage:** Typically allocated on the [[Stack_Memory_C|call stack]].
- **Initialization:** Automatic local variables are **not** initialized by default; they contain indeterminate ("garbage") values unless explicitly initialized in their definition.
- **`static` Keyword:** If a local variable is declared with the `static` keyword ([[Static_Variable_C]]), it has *static storage duration*. It exists for the entire program execution, retains its value between function calls, and is initialized only once (to zero/NULL if not explicitly initialized). However, its *scope* remains local to the function/block.

## Examples / Use Cases

```c
#include <stdio.h>

void my_function() {
    int local_auto = 10; // Automatic local variable (on stack)
    static int local_static = 0; // Static local variable (in data/BSS segment)

    local_auto++;
    local_static++;

    printf("  Inside my_function: local_auto = %d, local_static = %d\n",
           local_auto, local_static);
}

int main() {
    int main_local = 100; // Local variable to main

    printf("Calling my_function first time:\n");
    my_function();

    printf("Calling my_function second time:\n");
    my_function();

    // printf("%d\n", local_auto); // ERROR: local_auto not visible here (out of scope)
    // printf("%d\n", local_static); // ERROR: local_static not visible here (out of scope)

    if (main_local > 50) {
        int block_local = 5; // Local variable with block scope
        printf("Inside if block: block_local = %d\n", block_local);
    }
    // printf("%d\n", block_local); // ERROR: block_local not visible here (out of scope)


    return 0;
}
```
**Output:**
```
Calling my_function first time:
  Inside my_function: local_auto = 11, local_static = 1
Calling my_function second time:
  Inside my_function: local_auto = 11, local_static = 2
Inside if block: block_local = 5
```

## Related Concepts
- [[Scope_C]], [[Block_Scope_C]] (Defines visibility)
- [[Function_C]] (Where local variables are typically defined)
- [[Stack_Memory_C]] (Default storage location)
- [[Automatic_Variable_C]] (Default lifetime/storage duration)
- [[Static_Variable_C]] (Local variable with static lifetime)
- [[Global_Variable_C]] (Variables defined outside functions - *to be created*)

---
**Source:** Worksheet C_WS3