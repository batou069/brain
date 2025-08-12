---
tags: [c_programming, concept]
aliases: []
related: []
worksheet: [WS]
date_created: 2025-04-11
---
# Static Variable (C)

## Definition

In C, the `static` keyword used with a variable declaration modifies its **storage duration** and/or **linkage**, depending on whether the variable is declared inside or outside a function.

1.  **Inside a function (Local Static Variable):** A variable declared with `static` inside a function block has *static storage duration* but retains its *local scope*.
2.  **Outside a function (Global Static Variable):** A variable declared with `static` at file scope (outside any function) has *static storage duration* and *internal linkage*.

## Key Aspects / Characteristics

**1. Local Static Variables (Inside Function):**
    - **Storage Duration:** Static. The variable exists and retains its value for the entire lifetime of the program, not just during the function's execution.
    - **Initialization:** Initialized only *once*, before program startup (or technically, before the first time the function is called). If not explicitly initialized, it's automatically zero-initialized.
    - **Scope:** Remains local to the function/block where it's defined. It cannot be accessed directly from outside the function.
    - **Use Case:** Maintaining state between function calls (e.g., call counters, memoization).

**2. Global Static Variables (Outside Function):**
    - **Storage Duration:** Static. Exists for the entire program lifetime.
    - **Initialization:** Initialized once before program startup (zero-initialized if not explicit).
    - **Linkage:** Internal Linkage. The variable is accessible only within the source file (`.c` file) where it is defined. It is not visible to the [[Linker_C]] from other source files, preventing naming conflicts.
    - **Scope:** File scope. Accessible from the point of declaration to the end of the file.
    - **Use Case:** Creating file-private global variables, hiding implementation details within a module.

## Examples / Use Cases

```c
#include <stdio.h>

// Global static variable (internal linkage)
static int file_scope_counter = 0;

void count_calls() {
    // Local static variable
    static int call_count = 0; // Initialized only ONCE

    call_count++;
    file_scope_counter++; // Accessing global static variable

    printf("  count_calls() called %d times.\n", call_count);
    printf("  file_scope_counter is now %d.\n", file_scope_counter);
}

// Another function in the same file can access file_scope_counter
void report_file_counter() {
     printf("Report: file_scope_counter = %d\n", file_scope_counter);
}

/*
// In another file (e.g., other.c):
extern int file_scope_counter; // LINKER ERROR! file_scope_counter has internal linkage
void some_other_function() {
    // file_scope_counter = 100; // Cannot access
}
*/

int main() {
    printf("Calling count_calls first time:\n");
    count_calls();
    report_file_counter();

    printf("\nCalling count_calls second time:\n");
    count_calls();
    report_file_counter();

    return 0;
}
```
**Output:**
```
Calling count_calls first time:
  count_calls() called 1 times.
  file_scope_counter is now 1.
Report: file_scope_counter = 1

Calling count_calls second time:
  count_calls() called 2 times.
  file_scope_counter is now 2.
Report: file_scope_counter = 2
```

## Related Concepts
- [[static_keyword_C]] (The keyword itself)
- [[Storage_Duration_C]] (Static vs. Automatic)
- [[Linkage_C]] (Internal vs. External - *to be created*)
- [[Scope_C]] (Local vs. File scope)
- [[Local_Variable_C]], [[Global_Variable_C]]
- [[Data_Segment_C]], [[BSS_Segment_C]] (Where static variables are stored)
- [[Static_Function_C]] (Functions declared `static` also have internal linkage)

## Questions / Further Study
>[!question] What are static variables? (WS6)
> Static variables, declared using the `static` keyword, have *static storage duration*, meaning they exist for the entire program's lifetime.
> - If declared *locally* within a function, they retain their value between calls but are only accessible within that function. They are initialized only once.
> - If declared *globally* (at file scope), they are accessible only within that specific source file (internal linkage), preventing naming conflicts with global variables in other files.

---
**Source:** Worksheet C_WS3, C_WS6