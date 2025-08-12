---
tags: [c, concept, function, parameter, memory, pointer]
aliases: [C Pass by Reference (Simulated), C Pass by Pointer]
related:
  - "[[Function_C]]"
  - "[[Function_Parameters_C]]"
  - "[[Function_Call_C]]"
  - "[[Pass_by_Value_C]]"
  - "[[Pointer_C]]"
  - "[[Address_Operator_C]]"
  - "[[Dereference_Operator_C]]"
  - "[[scanf]]"
worksheet: [C_WS3]
date_created: 2025-04-11
---
# Pass by Address (C)

## Definition

**Pass by Address** (often loosely called "pass by reference" in the context of C, though technically C only has pass-by-value) is a technique used to allow a called [[Function_C]] to modify variables in its caller's scope. This is achieved by passing a [[Pointer_C]] (which holds the memory address of the caller's variable) as an argument to the function. The function parameter receives a copy of this address ([[Pass_by_Value_C|pass-by-value] applied to the pointer), but this copied address still points to the original variable's memory location.

## Key Aspects / Characteristics

- **Passing Pointers:** Instead of passing the variable's value, the argument passed is the variable's memory address, obtained using the [[Address_Operator_C|`&` operator]].
- **Pointer Parameters:** The corresponding [[Function_Parameters_C|function parameter]] must be declared as a pointer type (e.g., `int *`, `char *`, `struct Data *`).
- **Dereferencing:** Inside the function, the [[Dereference_Operator_C|`*` operator]] is used on the pointer parameter to access or modify the value *at the original address* (i.e., the caller's variable).
- **Simulates Pass-by-Reference:** Allows functions to have "output parameters" or modify input arguments directly, simulating the behavior of pass-by-reference found in other languages.
- **Efficiency for Large Data:** Passing a pointer (typically 4 or 8 bytes) can be more efficient than passing a large `struct` by value (which would involve copying the entire structure).

## Examples / Use Cases

**Example: Swapping two integers**
```c
#include <stdio.h>

// Function takes pointers to integers as parameters
void swap(int *ptr_a, int *ptr_b) {
    if (ptr_a == NULL || ptr_b == NULL) return; // Safety check

    printf("  Inside swap: Before: *ptr_a=%d, *ptr_b=%d\n", *ptr_a, *ptr_b);
    int temp = *ptr_a;  // Read value at address ptr_a points to
    *ptr_a = *ptr_b;    // Write value from ptr_b's location to ptr_a's location
    *ptr_b = temp;      // Write temp value to ptr_b's location
    printf("  Inside swap: After: *ptr_a=%d, *ptr_b=%d\n", *ptr_a, *ptr_b);
}

int main() {
    int x = 10, y = 20;

    printf("In main: Before swap: x=%d, y=%d\n", x, y);

    // Call swap, passing the ADDRESSES of x and y
    swap(&x, &y);

    printf("In main: After swap: x=%d, y=%d\n", x, y); // x and y are now swapped

    return 0;
}
```
**Output:**
```
In main: Before swap: x=10, y=20
  Inside swap: Before: *ptr_a=10, *ptr_b=20
  Inside swap: After: *ptr_a=20, *ptr_b=10
In main: After swap: x=20, y=10
```

**Common Use Case: `scanf`**
```c
int age;
printf("Enter your age: ");
scanf("%d", &age); // Pass the address of 'age' so scanf can store the input there
```

## Related Concepts
- [[Function_C]], [[Function_Parameters_C]], [[Function_Call_C]]
- [[Pass_by_Value_C]] (The underlying mechanism - the pointer address is passed by value)
- [[Pointer_C]] (The core tool for pass-by-address)
- [[Address_Operator_C]] (`&`) (Used to get the address to pass)
- [[Dereference_Operator_C]] (`*`) (Used inside the function to access the original variable)
- [[scanf]] (Standard library function requiring pass-by-address)

---
**Source:** Worksheet C_WS3