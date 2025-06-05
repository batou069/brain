---
tags: [c, concept, operator, struct, union, pointer]
aliases: [Dot Operator C, Arrow Operator C, Structure Member Access C]
related:
  - "[[struct_C]]"
  - "[[Union_C]]"
  - "[[Pointer_C]]"
  - "[[Operator_C]]"
worksheet: [C_WS5] # Implicitly related via struct
date_created: 2025-04-12
---
# Member Access Operators (`.` and `->`) (C)

## Definition

C provides two [[Operator_C|operators]] specifically for accessing members (fields) of [[struct_C|structures]] and [[Union_C|unions]]:

1.  **Dot Operator (`.`):** Used to access a member directly from a structure or union *variable*.
2.  **Arrow Operator (`->`):** Used to access a member via a *pointer* to a structure or union.

## Key Aspects / Characteristics

-   **Dot Operator (`.`):**
    -   Syntax: `structure_variable.member_name` or `union_variable.member_name`
    -   Left operand must be a variable of `struct` or `union` type.
    -   Right operand must be the name of a member within that `struct` or `union`.

-   **Arrow Operator (`->`):**
    -   Syntax: `pointer_to_struct->member_name` or `pointer_to_union->member_name`
    -   Left operand must be a pointer to a `struct` or `union`.
    -   Right operand must be the name of a member within the pointed-to `struct` or `union`.
    -   Shorthand: `pointer->member` is exactly equivalent to `(*pointer).member`. The arrow operator provides more convenient syntax when working with pointers to structures/unions.

-   **Precedence:** Both `.` and `->` have very high precedence, typically evaluated before most other operators except postfix `++`/`--`. See [[Operator_Precedence_C]].

## Examples / Use Cases

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int id;
    double value;
} Item;

int main() {
    Item item1;         // Structure variable
    Item *item_ptr;     // Pointer to a structure

    // --- Using Dot Operator (.) ---
    item1.id = 101;
    item1.value = 99.5;
    printf("Using dot (.): ID=%d, Value=%.1f\n", item1.id, item1.value);

    // --- Using Arrow Operator (->) ---
    // Allocate memory for an Item and get a pointer
    item_ptr = (Item*)malloc(sizeof(Item));
    if (item_ptr == NULL) return 1;

    // Access members using arrow operator
    item_ptr->id = 202;
    item_ptr->value = 123.4;
    printf("Using arrow (->): ID=%d, Value=%.1f\n", item_ptr->id, item_ptr->value);

    // Equivalent access using dereference (*) and dot (.)
    printf("Using (*ptr).: ID=%d, Value=%.1f\n", (*item_ptr).id, (*item_ptr).value);

    // Using arrow with pointer to existing struct variable
    Item *ptr_to_item1 = &item1;
    printf("Arrow on ptr to item1: ID=%d\n", ptr_to_item1->id); // Accesses item1.id

    free(item_ptr); // Clean up allocated memory
    item_ptr = NULL;

    return 0;
}
```

## Related Concepts
- [[struct_C]], [[Union_C]] (The types whose members are accessed)
- [[Pointer_C]] (The arrow operator requires a pointer)
- [[Operator_C]] (`.` and `->` are operators)
- [[Dereference_Operator_C]] (`*`) (Used in the `(*ptr).member` equivalent)

---
**Source:** Worksheet C_WS5 (Implicit)