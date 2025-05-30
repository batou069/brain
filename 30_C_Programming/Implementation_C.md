---
tags: [c, concept, design, module]
aliases: [C Implementation]
related:
  - "[[Interface_C]]"
  - "[[Source_File_C]]"
  - "[[Function_Definition_C]]"
  - "[[Static_Function_C]]"
  - "[[Static_Variable_C]]"
  - "[[Abstraction_C]]"
  - "[[Encapsulation_C]]"
worksheet: [C_WS6]
date_created: 2025-04-11
---
# Implementation (C)

## Definition

In C programming, the **Implementation** refers to the actual code that provides the functionality declared in a module's [[Interface_C]]. It contains the definitions of functions, the definitions of internal data structures, and any private helper functions or variables needed to make the module work. The implementation details are typically hidden from client code and reside in source files (`.c` files).

## Key Aspects / Characteristics

- **Provides Functionality:** Contains the function bodies ([[Function_Definition_C]]) that execute the tasks declared in the interface.
- **Source Files:** Implementation code is written in `.c` files (sometimes called implementation files or source files).
- **Hides Details:** Keeps the internal workings of a module private. Client code interacts only through the public [[Interface_C]] defined in the header file.
- **Includes Own Header:** An implementation file (`.c`) should typically `#include` its own corresponding header file (`.h`). This allows the compiler to check that the definitions in the `.c` file match the declarations in the `.h` file.
- **Internal Linkage:** Helper functions or global variables intended only for use within the implementation file should be declared `static` ([[Static_Function_C]], [[Static_Variable_C]]) to give them internal linkage, preventing them from being accessed or conflicting with names in other modules.
- **Data Structures:** Defines the concrete layout of data structures (like `struct`s) that might only be forward-declared or represented by opaque pointers in the interface header.

## Examples / Use Cases

**Implementation File (`counter.c`)**
```c
#include <stdlib.h> // For malloc, free
#include "counter.h" // Include the interface header

// Define the actual structure (hidden from clients)
struct Counter {
    int value;
};

// Helper function only used within this file (internal linkage)
static void log_error(const char *msg) {
    fprintf(stderr, "Counter Error: %s\n", msg); // fprintf needs <stdio.h>
}

// --- Implementation of Interface Functions ---

Counter* counter_create(int initial_value) {
    Counter *c = (Counter*)malloc(sizeof(Counter));
    if (c == NULL) {
        log_error("Allocation failed in counter_create");
        return NULL;
    }
    c->value = initial_value;
    return c;
}

void counter_increment(Counter *c) {
    if (c != NULL) {
        c->value++;
    } else {
        log_error("NULL pointer passed to counter_increment");
    }
}

int counter_get_value(const Counter *c) {
    if (c != NULL) {
        return c->value;
    } else {
        log_error("NULL pointer passed to counter_get_value");
        return -1; // Or some other error indication
    }
}

void counter_destroy(Counter *c) {
    // It's safe to pass NULL to free
    free(c);
}

```
*(This corresponds to the [[Interface_C]] defined in `counter.h`)*

## Related Concepts
- [[Interface_C]] (The public contract implemented here)
- [[Header_file_C]] (Declares the interface, included by the implementation)
- [[Source_File_C]] (Where implementation code resides - *to be created*)
- [[Function_Definition_C]] (The core of the implementation)
- [[Static_Function_C]], [[Static_Variable_C]] (Used for hiding internal details)
- [[Abstraction_C]], [[Encapsulation_C]] (Design principles supported by separating interface and implementation)

---
**Source:** Worksheet C_WS6