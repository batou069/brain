---
tags: [c, concept, data_type, keyword, syntax]
aliases: [C Enum, Enumeration C]
related:
  - "[[Data_Types_C]]"
  - "[[int_C]]"
  - "[[Symbolic_Constants_C]]"
  - "[[struct_C]]"
  - "[[typedef_C]]"
worksheet: [C_WS5]
date_created: 2025-04-12
---
# `enum` (Enumeration) (C)

## Definition

An **`enum` (enumeration)** in C is a user-defined data type consisting of a set of named integer constants, called **enumerators**. It provides a way to create symbolic names for related constant values, improving code readability and maintainability compared to using raw integers or `#define` macros for such constants.

## Key Aspects / Characteristics

- **User-Defined Type:** Creates a new type, although its underlying representation is compatible with `int`.
- **Named Integer Constants:** Defines symbolic names (enumerators) that represent integer values.
- **Automatic Value Assignment:** By default, the first enumerator is assigned the value 0, the second 1, and so on.
- **Explicit Value Assignment:** You can explicitly assign integer values to enumerators. Subsequent enumerators without explicit values will continue incrementing from the last assigned value.
- **Readability:** Using meaningful names (e.g., `COLOR_RED`, `STATE_RUNNING`) makes code easier to understand than using magic numbers (e.g., `0`, `1`).
- **Type Compatibility:** Variables of an enum type are compatible with `int`. You can assign enum values to `int` variables and vice-versa (though assigning arbitrary ints to enum variables might be questionable style).
- **Scope:** Enum types and enumerators follow standard C scoping rules (block, file, etc.).

## Syntax

```c
// Define an enum type named 'TypeName'
enum TypeName {
    ENUMERATOR_1,          // Value 0 by default
    ENUMERATOR_2,          // Value 1
    ENUMERATOR_3 = 10,     // Explicitly assigned value 10
    ENUMERATOR_4,          // Value 11 (increments from previous)
    ENUMERATOR_5 = 10      // Values can be duplicated
};

// Declare a variable of the enum type
enum TypeName my_variable;

// Can also define and declare in one step
enum Color { RED, GREEN, BLUE } current_color;

// Using typedef for convenience
typedef enum {
    STATUS_OK,
    STATUS_ERROR,
    STATUS_PENDING
} StatusCode;

StatusCode current_status;
```

## Examples / Use Cases

```c
#include <stdio.h>

// Enum for representing days of the week
typedef enum {
    MON = 1, TUE, WED, THU, FRI, SAT, SUN // Start explicitly from 1
} DayOfWeek;

// Enum for representing states
typedef enum {
    STATE_IDLE,
    STATE_CONNECTING,
    STATE_ACTIVE,
    STATE_ERROR = -1 // Can use negative values
} MachineState;

void print_day(DayOfWeek day) {
    switch (day) {
        case MON: printf("Monday"); break;
        case TUE: printf("Tuesday"); break;
        // ... other days ...
        case SUN: printf("Sunday"); break;
        default: printf("Invalid Day"); break;
    }
    printf(" (Value: %d)\n", day);
}

int main() {
    DayOfWeek today = WED;
    MachineState current_state = STATE_CONNECTING;

    print_day(today); // Output: Wednesday (Value: 3)

    printf("Current state value: %d\n", current_state); // Output: 1

    // Assigning enum to int
    int state_val = current_state;
    printf("State value as int: %d\n", state_val); // Output: 1

    // Using enumerators directly
    if (current_state == STATE_CONNECTING) {
        printf("Still connecting...\n");
    }

    return 0;
}
```

## Related Concepts
- [[Data_Types_C]] (Enum creates a distinct integer-compatible type)
- [[int_C]] (The underlying compatible type)
- [[Symbolic_Constants_C]] (Enums provide named constants - *to be created*)
- [[#define]] (Alternative way to define constants, but less type-safe)
- [[struct_C]], [[typedef_C]] (Other ways to define custom types)
- `switch` statement (Often used with enum types)

---
**Source:** Worksheet C_WS5