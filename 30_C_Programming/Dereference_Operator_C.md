---
tags: [c, concept, operator, pointer, memory]
aliases: [Indirection Operator, * Operator C (Pointer)]
related:
  - "[[Pointer_C]]"
  - "[[Address_Operator_C]]"
  - "[[Memory_Management]]"
  - "[[Variable_Definition_C]]"
worksheet: [C_WS3]
date_created: 2025-04-11
---
# Dereference Operator `*` (C)

## Definition

The **Dereference Operator (`*`)**, also known as the **Indirection Operator**, is a unary [[Operator_C]] in C used with a [[Pointer_C]] operand. It accesses the object or value located *at the memory address* stored in the pointer. It essentially means "get the value pointed to by".

## Key Aspects / Characteristics

- **Unary Operator:** Takes one operand, which must be a pointer (e.g., `*ptr`).
- **Accesses Value:** Reads or writes the value at the memory location the pointer points to.
- **Requires Valid Pointer:** Dereferencing a [[NULL_C|NULL pointer]] or a [[Dangling_Pointer_C|dangling pointer]] (one pointing to invalid or deallocated memory) results in [[Undefined_Behavior_C]], often a program crash (segmentation fault).
- **Lvalue Result:** When used on the left side of an assignment (`*ptr = value;`), the dereferenced pointer acts as an lvalue, allowing modification of the pointed-to memory. When used elsewhere (`value = *ptr;`), it yields the value stored at the address.
- **Distinction from Declaration:** The asterisk `*` is also used in pointer declarations (`int *ptr;`), but in that context, it signifies the type, whereas when used as an operator in an expression (`*ptr`), it performs dereferencing.

## Examples / Use Cases

```c
#include <stdio.h>
#include <stdlib.h> // For NULL

int main() {
    int num = 99;
    int *ptr = &num;
    int value_read;

    // Read the value pointed to by ptr
    value_read = *ptr;
    printf("Value read via *ptr: %d\n", value_read); // Output: 99

    // Modify the value pointed to by ptr
    *ptr = 55;
    printf("Value of num after *ptr = 55: %d\n", num); // Output: 55

    // Using dereference in expressions
    *ptr = *ptr + 10; // Increment the value pointed to by 10
    printf("Value of num after *ptr = *ptr + 10: %d\n", num); // Output: 65

    // Dereferencing NULL (BAD!)
    int *null_ptr = NULL;
    // *null_ptr = 10; // CRASH! (Undefined Behavior) - Uncommenting will likely cause a segfault

    return 0;
}
```

## Related Concepts
- [[Pointer_C]] (The operand for the `*` operator)
- [[Address_Operator_C]] (`&`) (Used to get the address to store in a pointer)
- [[50_Data_Structures/Memory_Management]] (Dereferencing accesses memory)
- [[NULL_C]], [[Dangling_Pointer_C]], [[Undefined_Behavior_C]] (Risks of dereferencing invalid pointers)

---
**Source:** Worksheet C_WS3