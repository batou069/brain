---
tags:
  - data_structures
  - concept
  - composite
aliases:
  - Variant Record
  - Tagged Union
  - Discriminated Union
  - Sum Type
related:
  - "[[Data_Structure]]"
  - "[[Union_DS]]"
  - "[[enum_C]]"
  - "[[struct_C]]"
  - "[[Type_Safety]]"
worksheet:
  - WS7
date_created: 2025-04-12
---
# Variant (Data Structure)

## Definition

A **Variant** (also known as a **Variant Record**, **Tagged Union**, **Discriminated Union**, or **Sum Type**) is a [[Data_Structure]] designed to hold a value that could be one of several different, specified types. It typically consists of two parts:

1.  A [[Union_DS|Union]] to hold the actual data value (capable of storing any of the possible types).
2.  A **tag** or **discriminant** field (often an [[enum_C|enumeration]]) indicating *which* type is currently stored in the union part, i.e., which union member is active and valid.

## Key Aspects / Characteristics

- **Holds One of Several Types:** Can store a value of type A, OR type B, OR type C, etc., at any given time.
- **Type Safety:** The tag field allows code to safely determine the current type stored in the union before accessing it, avoiding the potential [[Undefined_Behavior_C|undefined behavior]] associated with accessing the wrong member of a plain [[Union_DS]].
- **Implementation:** Commonly implemented using a `struct` that contains both the `union` and the `tag` field.
- **Memory Efficiency:** Still benefits from the memory-saving aspect of unions, as storage is only needed for the largest possible type plus the tag.
- **Use Cases:**
    - Representing data that can take on different forms (e.g., a JSON value could be a string, number, boolean, array, or object).
    - Implementing nodes in a parse tree or abstract syntax tree where nodes can represent different language constructs.
    - Handling messages of different types in a communication system.
    - Representing states in a state machine where data associated with each state differs.

## Implementation Example (C)

```c
#include <stdio.h>
#include <string.h>

// 1. Define the possible types using an enum (the tag)
typedef enum {
    TYPE_INT,
    TYPE_FLOAT,
    TYPE_STRING
} VariantType;

// 2. Define the union to hold the data
typedef union {
    int i;
    float f;
    char s[50]; // Assume max string length 49 + null
} ValueUnion;

// 3. Define the Variant struct containing the tag and the union
typedef struct {
    VariantType type; // The tag
    ValueUnion value; // The union holding the data
} Variant;

// Function to print the variant value safely
void print_variant(const Variant *v) {
    if (v == NULL) return;

    switch (v->type) {
        case TYPE_INT:
            printf("Variant (Int): %d\n", v->value.i);
            break;
        case TYPE_FLOAT:
            printf("Variant (Float): %f\n", v->value.f);
            break;
        case TYPE_STRING:
            printf("Variant (String): \"%s\"\n", v->value.s);
            break;
        default:
            printf("Variant (Unknown Type)\n");
            break;
    }
}

int main() {
    Variant var1, var2, var3;

    // Store an integer
    var1.type = TYPE_INT;
    var1.value.i = 123;

    // Store a float
    var2.type = TYPE_FLOAT;
    var2.value.f = 45.67f;

    // Store a string
    var3.type = TYPE_STRING;
    strcpy(var3.value.s, "Test String");

    // Print using the safe function
    print_variant(&var1);
    print_variant(&var2);
    print_variant(&var3);

    return 0;
}
```

## Related Concepts
- [[Data_Structure]]
- [[Union_DS]] (Core component holding the value)
- [[enum_C]] (Often used for the tag/discriminant)
- [[struct_C]] (Used to combine the tag and the union)
- Type Safety (Variants improve safety over raw unions)
- Pattern Matching (Languages with built-in variant/sum types often support pattern matching for safe access)

---
**Source:** Worksheet WS7