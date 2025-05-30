---
tags: [c, concept, design, module, api]
aliases: [C Interface, API C]
related:
  - "[[Implementation_C]]"
  - "[[Header_file_C]]"
  - "[[Function_Declaration_C]]"
  - "[[struct_C]]"
  - "[[enum_C]]"
  - "[[typedef_C]]"
  - "[[Static_Function_C]]"
  - "[[Static_Variable_C]]"
  - "[[Abstraction_C]]"
worksheet: [C_WS3, C_WS6]
date_created: 2025-04-11
---
# Interface (C)

## Definition

In the context of C programming (which lacks built-in interface types like Java or C#), an **Interface** refers to the public "contract" of a software module or library. It defines *what* services (functions, data types, constants) the module provides and *how* they can be used by other parts of the program (the client code), without exposing the internal details of *how* those services are implemented. Interfaces in C are typically defined in [[Header_file_C|header files (`.h`)]].

## Key Aspects / Characteristics

- **Public Contract:** Defines the visible parts of a module.
- **Header Files:** Interfaces are almost always declared in `.h` files.
- **Contents:** Typically includes:
    - [[Function_Declaration_C|Function declarations (prototypes)]] for public functions.
    - Definitions for public data types ([[struct_C]], [[union_C]], [[enum_C]], [[typedef_C]]).
    - Macro definitions (`#define`) for public constants or function-like macros.
    - `extern` declarations for public global variables (though minimizing global variables is often good practice).
- **Abstraction:** Hides the [[Implementation_C|implementation details]] from the client code. Clients only need to know the interface to use the module.
- **Decoupling:** Separating interface from implementation allows the implementation to change without requiring changes to the client code, as long as the interface remains stable.
- **Compilation Model:** Header files containing the interface are `#include`d by both the implementation file (`.c`) and any client files (`.c`) that use the module.

## Examples / Use Cases

**Interface Definition (`counter.h`)**
```c
#ifndef COUNTER_H // Header guard
#define COUNTER_H

// Opaque pointer type (hides struct details)
typedef struct Counter Counter;

// Function declarations (the interface)
Counter* counter_create(int initial_value);
void counter_increment(Counter *c);
int counter_get_value(const Counter *c);
void counter_destroy(Counter *c);

#endif // COUNTER_H
```

**Client Code (`main.c`)**
```c
#include <stdio.h>
#include "counter.h" // Include the interface

int main() {
    Counter *my_counter = counter_create(10); // Use interface functions
    if (!my_counter) return 1;

    counter_increment(my_counter);
    counter_increment(my_counter);

    printf("Counter value: %d\n", counter_get_value(my_counter));

    counter_destroy(my_counter); // Use interface function

    return 0;
}
// Note: main.c does NOT know how 'Counter' is defined internally
// or how the functions are implemented. It only knows the interface.
```
*(The [[Implementation_C]] would be in `counter.c`)*

## Related Concepts
- [[Implementation_C]] (The hidden details providing the service)
- [[Header_file_C]] (Where interfaces are defined)
- [[Function_Declaration_C]] (Key part of a function interface)
- [[Abstraction_C]] (Hiding complexity via interfaces - *to be created*)
- [[Encapsulation_C]] (Bundling data and functions, often achieved via interfaces and opaque types - *to be created*)
- [[API]] (Application Programming Interface - often synonymous with interface in this context)
- [[Opaque_Pointer_C]] (Technique to hide data structure details in interfaces - *to be created*)

## Questions / Further Study
>[!question] What is the difference between interface and implementation? (WS6)
> - The **[[Interface_C|Interface]]** defines *what* a module does and *how* to use it (function signatures, data types, constants). It's the public contract, typically in a `.h` file. It focuses on the "what".
> - The **[[Implementation_C|Implementation]]** provides the actual code that *fulfills* the contract (function bodies, internal data structures, static helper functions). It's the private detail, typically in a `.c` file. It focuses on the "how".
> Separating them allows changing the implementation without breaking client code that relies only on the stable interface.

---
**Source:** Worksheet C_WS3, C_WS6