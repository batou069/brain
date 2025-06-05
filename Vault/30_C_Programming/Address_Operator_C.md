---
tags:
  - c
  - concept
  - operator
  - pointer
  - memory
aliases:
  - Address-of Operator
  - Operator C
related:
  - "[[Pointer_C]]"
  - "[[Dereference_Operator_C]]"
  - "[[50_Data_Structures/Memory_Management]]"
  - "[[Variable_Definition_C]]"
  - "[[scanf]]"
worksheet:
  - C_WS3
date_created: 2025-04-11
---
# Address-Of Operator `&` (C)

## Definition

The **Address-Of Operator (`&`)** is a unary [[Operator_C]] in C that yields the memory address of its operand. The operand must be an lvalue (something that designates an object, like a variable or an array element, that resides in memory). The result is a [[Pointer_C]] to the operand's type.

## Key Aspects / Characteristics

- **Unary Operator:** Takes one operand (e.g., `&my_variable`).
- **Operand Must Be Lvalue:** Cannot take the address of constants (`&5`), register variables (`&register_var`), or expressions that don't represent a stored object (`&(a + b)`).
- **Returns a Pointer:** The result's type is "pointer to operand's type". If `x` is an `int`, `&x` has the type `int *`.
- **Assigning to Pointers:** Used to initialize or assign values to pointer variables.
- **Passing by Address:** Used to pass the address of a variable to a function (like [[scanf]] or custom functions using [[Pass_by_Address_C]]), allowing the function to modify the original variable.

## Examples / Use Cases

```c
#include <stdio.h>

void modify_value(int *ptr) {
    *ptr = *ptr * 2; // Modify the original variable via its address
}

int main() {
    int value = 10;
    int *pointer_to_value;
    int arr[5];

    // Assign address to a pointer
    pointer_to_value = &value;
    printf("Address of 'value': %p\n", (void*)&value);
    printf("Value stored in 'pointer_to_value': %p\n", (void*)pointer_to_value);

    // Pass address to scanf
    printf("Enter a new value: ");
    scanf("%d", &value); // Pass the address so scanf can store input in 'value'
    printf("You entered: %d\n", value);

    // Pass address to a custom function
    modify_value(&value);
    printf("Value after modify_value: %d\n", value);

    // Address of an array element
    int *ptr_to_element = &arr[2];
    printf("Address of arr[2]: %p\n", (void*)ptr_to_element);

    // Address of the array itself (same as address of first element)
    printf("Address of arr: %p\n", (void*)&arr);
    printf("Address of arr[0]: %p\n", (void*)&arr[0]);


    // Error examples:
    // int *p1 = &10; // ERROR: Cannot take address of a constant literal
    // int *p2 = &(value + 5); // ERROR: Cannot take address of temporary result

    return 0;
}
```

## Related Concepts
- [[Pointer_C]] (The result of the `&` operator is a pointer)
- [[Dereference_Operator_C]] (`*`) (The inverse operation - gets value from address)
- [[50_Data_Structures/Memory_Management]] (Deals with memory addresses)
- [[Variable_Definition_C]] (Operands are typically defined variables)
- [[Pass_by_Address_C]] (Mechanism enabled by the `&` operator)
- [[scanf]] (Common standard library function requiring addresses)

---
**Source:** Worksheet C_WS3