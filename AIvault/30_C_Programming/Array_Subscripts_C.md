---
tags: [c, concept, syntax, operator, array, pointer]
aliases: [C Array Indexing, "[] Operator C"]
related:
  - "[[Array_C]]"
  - "[[Pointer_C]]"
  - "[[Operator_C]]"
  - "[[Address_Operator_C]]"
  - "[[Dereference_Operator_C]]"
worksheet: [C_WS3]
date_created: 2025-04-11
---
# Array Subscripts `[]` (C)

## Definition

The **Array Subscript Operator (`[]`)** in C is used to access individual elements within an [[Array_C]]. It takes two operands: an expression that evaluates to an [[Pointer_C|array or pointer type]] (usually the array name or a pointer to an element), and an integer expression (the index or subscript) enclosed in square brackets.

## Key Aspects / Characteristics

- **Element Access:** Provides a convenient way to read or write specific elements of an array.
- **Zero-Based Indexing:** Array indices in C always start at 0. For an array `arr` of size `N`, the valid indices are `0` to `N-1`.
- **Pointer Arithmetic Equivalence:** The expression `array[index]` is defined by the C standard to be exactly equivalent to `*(array + index)`. This highlights the close relationship between arrays and pointers in C.
    - `array` (when used in this expression) decays into a pointer to its first element.
    - `array + index` performs pointer arithmetic to calculate the address of the element at the given index.
    - `*` dereferences that calculated address to access the element's value.
- **Commutativity (Surprising!):** Because `a[i]` is equivalent to `*(a + i)`, and pointer addition is commutative (`*(a + i)` is the same as `*(i + a)`), the expression `index[array]` is also technically valid C code and equivalent to `array[index]`. However, `index[array]` is extremely unconventional and should **never** be used in practice as it severely harms readability.
- **Bounds Checking:** C does **not** perform automatic bounds checking on array access. Accessing an element outside the valid index range (e.g., `arr[-1]` or `arr[N]` for an array of size N) results in [[Undefined_Behavior_C]], often leading to corrupted data or program crashes.

## Examples / Use Cases

```c
#include <stdio.h>

int main() {
    int numbers[5] = {10, 20, 30, 40, 50};
    int third_element;
    int *ptr = numbers; // Array name decays to pointer to first element

    // Read using array subscript
    third_element = numbers[2]; // Access the element at index 2 (value 30)
    printf("Using numbers[2]: %d\n", third_element);

    // Write using array subscript
    numbers[0] = 11; // Change the first element
    printf("Using numbers[0] after change: %d\n", numbers[0]);

    // Access using pointer arithmetic equivalent
    printf("Using *(numbers + 2): %d\n", *(numbers + 2)); // Equivalent to numbers[2]
    printf("Using *(ptr + 0): %d\n", *(ptr + 0));       // Equivalent to ptr[0] or numbers[0]

    // Access using pointer and subscript operator
    printf("Using ptr[2]: %d\n", ptr[2]); // Equivalent to numbers[2]

    // Unconventional but valid syntax (DO NOT USE)
    printf("Using 2[numbers]: %d\n", 2[numbers]); // Equivalent to numbers[2]
    printf("Using 2[ptr]: %d\n", 2[ptr]);       // Equivalent to ptr[2]

    // Out-of-bounds access (UNDEFINED BEHAVIOR!)
    // printf("Accessing numbers[5]: %d\n", numbers[5]); // Likely crash or garbage data
    // numbers[-1] = 0; // Likely crash or memory corruption

    return 0;
}
```

## Related Concepts
- [[Array_C]] (The data structure accessed)
- [[Pointer_C]] (Array subscripting is defined in terms of pointer arithmetic)
- [[Operator_C]] (`[]` is an operator)
- [[Pointer_Arithmetic_C]] (The underlying mechanism - *to be created*)
- [[Undefined_Behavior_C]] (Result of out-of-bounds access)
- [[Zero_Based_Indexing_C]] (The indexing convention - *to be created*)

---
**Source:** Worksheet C_WS3