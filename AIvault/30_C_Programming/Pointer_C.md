---
tags: [c, concept, memory, data_type, core]
aliases: [C Pointer, Pointers]
related: [Memory_Management, Address_Operator_C, Dereference_Operator_C, Array_C, String_in_C, Function_Pointer_C, Dynamic_Allocation_C, Pass_by_Address_C, NULL_C, Dangling_Pointer_C
worksheet: [C_WS3, C_WS4]
date_created: 2025-04-11
---
# Pointer (C)

## Definition

In C, a **Pointer** is a special type of variable that stores the memory address of another variable. Instead of holding a direct value (like an `int` or `char`), a pointer "points to" the location in memory where a value of a specific type resides.

## Key Aspects / Characteristics

- **Stores Addresses:** Holds a memory address (often represented internally as an unsigned integer, but treated as a distinct type by the compiler).
- **Typed:** Pointers are typed. A pointer declared as `int *` is expected to point to a memory location containing an `int`. This allows the compiler to know how many [[bytes]] to read/write when the pointer is dereferenced and enables pointer arithmetic.
- **Declaration:** Declared using the asterisk `*`. Example: `int *ptr;` declares `ptr` as a pointer to an integer.
- **Address-Of Operator (`&`):** The [[Address_Operator_C|address-of operator (`&`)]] is used to get the memory address of a variable, which can then be assigned to a pointer. Example: `ptr = &my_variable;`.
- **Dereference Operator (`*`):** The [[Dereference_Operator_C|dereference operator (`*`)]] (also called indirection operator) is used to access the value *at the address* stored in the pointer. Example: `value = *ptr;` reads the value pointed to by `ptr`. `*ptr = 10;` writes 10 to the location pointed to by `ptr`.
- **Pointer Arithmetic:** Arithmetic operations (addition, subtraction) on pointers are scaled by the size of the data type they point to. `ptr + 1` points to the memory location of the *next element* of the pointed-to type. Crucial for [[Array_C]] manipulation.
- **NULL Pointers:** A special value, [[NULL_C]], indicates that a pointer does not point to any valid memory location.
- **Uses:** Essential for [[Dynamic_Allocation_C]], efficient [[Array_C]] and [[String_in_C]] handling, [[Pass_by_Address_C|passing arguments by address]] to functions, implementing complex data structures (like linked lists), and interacting with hardware addresses.

## Examples / Use Cases

```c
#include <stdio.h>

int main() {
    int num = 42;
    int *ptr_to_num; // Declare a pointer to an integer

    ptr_to_num = &num; // Assign the address of 'num' to 'ptr_to_num'

    printf("Value of num: %d\n", num);
    printf("Address of num: %p\n", (void*)&num); // Use %p for addresses, cast to void*

    printf("Value stored in ptr_to_num (address): %p\n", (void*)ptr_to_num);
    printf("Value pointed to by ptr_to_num (*ptr_to_num): %d\n", *ptr_to_num);

    // Modify 'num' through the pointer
    *ptr_to_num = 100;
    printf("New value of num (after *ptr_to_num = 100): %d\n", num);

    // Pointer arithmetic (example with an array)
    int arr[3] = {10, 20, 30};
    int *ptr_to_arr = arr; // Array name decays to pointer to first element

    printf("First element (*ptr_to_arr): %d\n", *ptr_to_arr);
    printf("Second element (*(ptr_to_arr + 1)): %d\n", *(ptr_to_arr + 1));

    return 0;
}```

## Related Concepts
- [[Address_Operator_C]] (`&`)
- [[Dereference_Operator_C]] (`*`)
- [[Memory_Management]] & Memory Addresses
- [[Array_C]] (Closely related, array names often decay to pointers)
- [[String_in_C]] (Manipulated using `char*` pointers)
- [[Dynamic_Allocation_C]] (`malloc` returns a pointer)
- [[Pass_by_Address_C]] (Passing pointers to functions)
- [[NULL_C]] (Represents an invalid pointer)
- [[Dangling_Pointer_C]] (Pointer pointing to invalid memory)
- [[Function_Pointer_C]] (Pointers to functions - *to be created*)

---
**Source:** Worksheet C_WS3, C_WS4