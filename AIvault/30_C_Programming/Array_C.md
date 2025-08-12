---
tags:
  - c
  - concept
  - data_structure
  - memory
  - core
aliases:
  - C Array
related:
  - "[[Array_Subscripts_C]]"
  - "[[Pointer_C]]"
  - "[[String_in_C]]"
  - "[[50_Data_Structures/Memory_Management]]"
  - "[[sizeof_operator_C]]"
  - "[[Array_Decay_C]]"
  - "[[Multidimensional_Array_C]]"
worksheet:
  - C_WS3
  - C_WS4
date_created: 2025-04-11
---
# Array (C)

## Definition

An **Array** in C is a derived data type that represents a collection of a fixed number of elements of the **same data type**, stored in a **contiguous block of memory**. Elements are accessed using an index (subscript) starting from 0.

## Key Aspects / Characteristics

- **Fixed Size:** The size of a standard C array must be a constant expression known at compile time (except for Variable Length Arrays - VLAs, introduced in C99, which have some limitations). Once declared, the size cannot be changed.
- **Homogeneous Elements:** All elements in an array must be of the same data type (e.g., an array of `int`, an array of `double`, an array of `struct Point`).
- **Contiguous Memory:** Array elements are stored one after another in memory without gaps. This allows for efficient access using pointer arithmetic.
- **Zero-Based Indexing:** The first element is at index 0, the second at index 1, ..., and the last element of an array `arr` of size `N` is at index `N-1`. See [[Array_Subscripts_C]].
- **Decay to Pointer:** In many contexts (e.g., when passed to functions, used in expressions except as operand of `sizeof` or `&`), an array name automatically "decays" into a [[Pointer_C]] to its first element. See [[Array_Decay_C]].
- **No Bounds Checking:** C does not perform runtime checks to ensure array indices are within the valid range. Accessing elements outside the array bounds leads to [[Undefined_Behavior_C]].
- **Initialization:** Can be initialized at definition using curly braces `{}`. If partially initialized, remaining elements are zero-initialized (for static/global arrays) or left indeterminate (for automatic arrays).

## Examples / Use Cases

```c
#include <stdio.h>

#define ARRAY_SIZE 5

int main() {
    // Definition and initialization
    int scores[ARRAY_SIZE] = {85, 92, 78, 99, 88}; // Size 5
    double temps[] = {12.5, 13.0, 11.8}; // Size inferred as 3
    char name[] = "Alice"; // Size inferred as 6 (includes '\0')

    // Accessing elements
    printf("First score: %d\n", scores[0]); // Output: 85
    printf("Third temp: %.1f\n", temps[2]); // Output: 11.8
    printf("Second char of name: %c\n", name[1]); // Output: l

    // Modifying elements
    scores[1] = 95;

    // Iterating through an array
    printf("Scores: ");
    for (int i = 0; i < ARRAY_SIZE; ++i) {
        printf("%d ", scores[i]);
    }
    printf("\n");

    // Sizeof array vs. element
    printf("Size of scores array: %zu bytes\n", sizeof(scores)); // Output: 5 * sizeof(int)
    printf("Size of one score: %zu bytes\n", sizeof(scores[0])); // Output: sizeof(int)
    printf("Number of elements: %zu\n", sizeof(scores) / sizeof(scores[0])); // Common idiom

    // Array decay
    int *ptr = scores; // 'scores' decays to 'int*' pointing to scores[0]
    printf("Value via pointer: %d\n", *ptr); // Output: 85

    return 0;
}
```

## Related Concepts
- [[Array_Subscripts_C]] (`[]` operator for access)
- [[Pointer_C]] (Close relationship, array decay)
- [[Array_Decay_C]] (Implicit conversion to pointer)
- [[String_in_C]] (Arrays of characters)
- [[50_Data_Structures/Memory_Management]], Contiguous Memory
- [[sizeof_operator_C]] (Used to get array size in bytes)
- [[Multidimensional_Array_C]] (Arrays of arrays - *to be created*)
- [[Dynamic_Allocation_C]] (Used to create arrays whose size is determined at runtime, often called dynamic arrays or vectors, though C doesn't have a built-in dynamic array type)
- [[Undefined_Behavior_C]] (Out-of-bounds access)

---
**Source:** Worksheet C_WS3, C_WS4