---
tags: [c, concept, variable, memory, alias]
aliases: [C Data Segment Variables, Static/Global Variables C]
related:
  - "[[Data_Segment_C]]"
  - "[[BSS_Segment_C]]"
  - "[[Static_Variable_C]]"
  - "[[Global_Variable_C]]"
  - "[[Memory_Segments_C]]"
  - "[[Storage_Duration_C]]"
worksheet: [C_WS3]
date_created: 2025-04-11
---
# Data Variable (C)

## Definition

Similar to "Heap Variable", **Data Variable** isn't official C terminology but is often used informally to refer to variables with *static storage duration* that are stored in the program's **data segments**. This typically includes:

1.  [[Global_Variable_C|Global variables]] (defined outside any function).
2.  [[Static_Variable_C|Static global variables]] (defined outside any function with `static` keyword).
3.  [[Static_Variable_C|Static local variables]] (defined inside a function with `static` keyword).

These variables exist for the entire duration of the program's execution.

## Key Aspects / Characteristics

- **Informal Term:** Refers to variables stored in the data or BSS segments.
- **Static Storage Duration:** Exist throughout the program's lifetime. See [[Storage_Duration_C]].
- **Storage Location:**
    - **Initialized** global/static variables are stored in the **[[Data_Segment_C|Data Segment]]** (initialized data segment, sometimes called `.data`). Their initial values are part of the executable file.
    - **Uninitialized** (or zero-initialized) global/static variables are stored in the **[[BSS_Segment_C|BSS Segment]]** (Block Started by Symbol). The executable only needs to store the *size* of the BSS; the operating system loader initializes this segment to all zero bits when the program loads. This saves space in the executable file.
- **Scope:** Can be global/file scope (for globals) or local scope (for static locals).
- **Initialization:** Initialized once before program startup (or before first function entry for static locals). Zero-initialized if no explicit initializer is provided.

## Examples / Use Cases

```c
#include <stdio.h>

int global_initialized_data = 10; // Stored in .data segment
int global_uninitialized_data;    // Stored in .bss segment (zero-initialized)
static int file_static_data = 20; // Stored in .data segment (internal linkage)
static int file_static_bss;       // Stored in .bss segment (internal linkage)

void func() {
    static int local_static_data = 30; // Stored in .data segment
    static int local_static_bss;       // Stored in .bss segment
    // ...
}

int main() {
    // All the variables above are "data variables" in the informal sense
    printf("global_initialized_data = %d\n", global_initialized_data);
    printf("global_uninitialized_data = %d\n", global_uninitialized_data); // Will be 0
    printf("file_static_data = %d\n", file_static_data);
    printf("file_static_bss = %d\n", file_static_bss); // Will be 0

    func(); // Initializes local_static_data and local_static_bss if first call

    return 0;
}
```

## Related Concepts
- [[Data_Segment_C]], [[BSS_Segment_C]] (The memory segments used)
- [[Static_Variable_C]], [[Global_Variable_C]] (The types of variables stored here)
- [[Memory_Segments_C]] (Overall memory layout)
- [[Storage_Duration_C]] (Static lifetime)
- [[Stack_Variable_C]], [[Heap_Variable_C]] (Contrasted with data segment variables)

---
**Source:** Worksheet C_WS3