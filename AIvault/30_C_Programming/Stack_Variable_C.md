---
tags: [c, concept, variable, scope, memory, lifetime, keyword]
aliases: [C Static Variables]
related:
  - "[[Local_Variable_C]]"
  - "[[Global_Variable_C]]"
  - "[[Scope_C]]"
  - "[[Data_Segment_C]]"
  - "[[BSS_Segment_C]]"
  - "[[Automatic_Variable_C]]"
  - "[[Storage_Duration_C]]"
  - "[[Static_Function_C]]"
  - "[[static_keyword_C]]"
worksheet: [C_WS3, C_WS6]
date_created: 2025-04-11
---
# Stack Variable (C)

## Definition

A **Stack Variable** in C is simply another term for an [[Automatic_Variable_C]]. These are [[Local_Variable_C|local variables]] declared inside a function or block without the `static` specifier. They are called "stack variables" because they are typically allocated on the program's [[Stack_Memory_C|call stack]] when their defining function or block is entered.

## Key Aspects / Characteristics

- **Synonym for Automatic Variable:** Functionally identical to [[Automatic_Variable_C]].
- **Storage Location:** Allocated on the [[Stack_Memory_C]]. Space is automatically reserved when the function/block starts and automatically released when it ends.
- **Fast Allocation/Deallocation:** Allocation and deallocation on the stack is extremely fast, usually just involving adjusting the stack pointer register.
- **Lifetime:** Limited to the execution duration of the function or block where they are defined. Values are not preserved between calls.
- **Scope:** Local to the defining function or block.
- **Initialization:** Not automatically initialized; contain garbage values unless explicitly initialized.
- **Size Limitation:** The total size of the stack is usually limited, so declaring very large arrays or deeply nested recursive calls can lead to a [[30_C_Programming/Stack_Overflow_C|stack overflow]].

## Examples / Use Cases

```c
#include <stdio.h>

void process(int x) {
    int temp_result = x * x; // temp_result is a stack variable
    char buffer[100];       // buffer is a stack variable (array on stack)

    printf("  Inside process: temp_result = %d\n", temp_result);
    // ... use buffer ...
} // temp_result and buffer are destroyed here

int main() {
    int main_var = 5; // main_var is a stack variable

    process(main_var);

    return 0;
}
```

## Related Concepts
- [[Stack_Memory_C]] (The memory region used)
- [[Automatic_Variable_C]] (The official C terminology for storage duration)
- [[Local_Variable_C]] (Stack variables are always local)
- [[Function_Call_C]] (Stack frames are created/destroyed during calls/returns)
- [[Scope_C]] (Local scope)
- [[Heap_Memory_C]], [[Dynamic_Allocation_C]] (Contrasted with stack allocation)
- [[30_C_Programming/Stack_Overflow_C]] (Potential error condition - *to be created*)

---
**Source:** Worksheet C_WS3