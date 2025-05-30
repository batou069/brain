---
tags:
  - data_structures
  - concept
  - basic
  - composite
  - c
aliases:
  - Union (Data Structure Context)
  - union C
related:
  - "[[Data_Structure]]"
  - "[[struct_C]]"
  - "[[Record_DS]]"
  - "[[50_Data_Structures/Memory_Management]]"
  - "[[Type_Punning]]"
worksheet:
  - WS7
date_created: 2025-04-12
---
# Union (Data Structure)

## Definition

A **Union** is a composite [[Data_Structure]] (similar to a [[Record_DS|Record]] or [[struct_C|Struct]]) that allows storing different data types in the **same memory location**. Only one member of the union can hold a value at any given time. The size of the union is determined by the size of its largest member.

## Key Aspects / Characteristics

- **Shared Memory:** All members of a union share the same starting memory address.
- **One Active Member:** Only one member can be meaningfully stored in the union at a time. Writing to one member will overwrite the data previously stored via another member.
- **Size:** The total size allocated for a union is at least the size of its largest member (potentially larger due to alignment/padding).
- **Type Interpretation:** It is the programmer's responsibility to keep track of *which* member is currently active or valid. Accessing the value through a member different from the one last written to (known as *type punning*) has implementation-defined or potentially [[Undefined_Behavior_C|undefined behavior]] in standard C (though it's sometimes used intentionally for low-level programming).
- **Use Cases:**
    - Saving memory when only one of several possible data types needs to be stored at a time.
    - Implementing variant records or tagged unions (where an additional field indicates which union member is active).
    - Low-level programming involving reinterpreting the bit patterns of data (type punning - use with extreme caution).

## Implementation Examples (C)

```c
#include <stdio.h>

// Define a union named 'DataValue'
union DataValue {
    int i;
    float f;
    char str[20]; // Largest member determines size
};

int main() {
    union DataValue data;

    printf("Size of union DataValue: %zu bytes\n", sizeof(data)); // Size of char[20]

    // Store an integer
    data.i = 10;
    printf("Data as int: %d\n", data.i);
    // Accessing data.f or data.str now is problematic

    // Store a float (overwrites the integer)
    data.f = 220.5f;
    printf("Data as float: %f\n", data.f);
    // Accessing data.i now reads garbage (part of the float's bit pattern)
    printf("Data as int (after float): %d\n", data.i); // Undefined/Implementation-defined

    // Store a string (overwrites the float)
    strcpy(data.str, "Hello"); // Needs <string.h>
    printf("Data as string: %s\n", data.str);
    // Accessing data.i or data.f now is problematic

    return 0;
}```

## Visualization (Conceptual Memory)

```bash
Memory Address: 0x1000
+------------------------------------+
| Member 'i' (e.g., 4 bytes)         |
+------------------+-----------------+
| Member 'f' (e.g., 4 bytes)         |
+------------------------------------+
| Member 'str' (e.g., 20 bytes)      |
+------------------------------------+
<-- All members start at the same address -->
<-- Total size = size of largest member (str[20]) -->
```
*Writing to `i` uses the first 4 bytes. Writing to `f` uses the first 4 bytes (overwriting `i`). Writing to `str` uses up to 20 bytes (overwriting `i` and `f`).*

## Related Concepts
- [[Data_Structure]]
- [[struct_C]], [[Record_DS]] (Contrast: members have distinct memory locations)
- [[50_Data_Structures/Memory_Management]] (Unions save memory by overlapping storage)
- [[Type_Punning]] (Reinterpreting data using different union members)
- Tagged Union / Variant Record (Common pattern using a union with a type tag)

---
**Source:** Worksheet WS7