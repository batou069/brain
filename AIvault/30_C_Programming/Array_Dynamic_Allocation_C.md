---
tags: [c, concept, array, memory, dynamic_allocation, pointer]
aliases: [C Dynamic Arrays]
related:
  - "[[Array_C]]"
  - "[[Dynamic_Allocation_C]]"
  - "[[malloc]]"
  - "[[calloc_C]]"
  - "[[realloc_C]]"
  - "[[free]]"
  - "[[Pointer_C]]"
  - "[[sizeof_operator_C]]"
  - "[[Heap_Memory_C]]"
worksheet: [C_WS3]
date_created: 2025-04-11
---
# Array Dynamic Allocation (C)

## Definition

Since standard C [[Array_C|arrays]] must have their size fixed at compile time (with the limited exception of VLAs), **Array Dynamic Allocation** refers to the technique of allocating memory for an array on the [[Heap_Memory_C|heap]] at runtime using [[Dynamic_Allocation_C]] functions like [[malloc]], [[calloc_C]], or [[realloc_C]]. This allows creating arrays whose size is determined during program execution (e.g., based on user input or file content).

## Key Aspects / Characteristics

- **Runtime Sizing:** The number of elements can be decided while the program is running.
- **Heap Allocation:** Memory is allocated from the [[Heap_Memory_C]].
- **Pointer Access:** The allocation functions return a [[Pointer_C]] to the first element of the allocated block. This pointer is used to access the array elements, often using the same [[Array_Subscripts_C|array subscript notation (`[]`)]] as with static arrays (due to pointer/array equivalence in expressions).
- **Manual Deallocation:** The allocated memory **must** be explicitly deallocated using [[free]] when no longer needed to prevent [[Memory_Leak_C|memory leaks]].
- **Contiguous Memory:** The allocated block is guaranteed to be contiguous in memory, just like a standard array.
- **`sizeof` Limitation:** Applying `sizeof` to the pointer variable holding the address of the dynamically allocated array will only give the size of the pointer itself, *not* the size of the allocated block. The size must be tracked separately by the programmer.

## Examples / Use Cases

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *dynamic_array = NULL;
    int size;

    // Get array size at runtime
    printf("Enter the desired size of the array: ");
    scanf("%d", &size);

    if (size <= 0) {
        printf("Invalid size.\n");
        return 1;
    }

    // Allocate memory dynamically using malloc
    // dynamic_array = (int*)malloc(size * sizeof(int));

    // Or using calloc (allocates and zero-initializes)
    dynamic_array = (int*)calloc(size, sizeof(int));

    // Check if allocation was successful
    if (dynamic_array == NULL) {
        perror("Failed to allocate memory for the array");
        return 1;
    }

    printf("Successfully allocated memory for %d integers at %p.\n", size, (void*)dynamic_array);

    // Use the dynamically allocated array like a normal array
    for (int i = 0; i < size; ++i) {
        dynamic_array[i] = i * i; // Access using []
    }

    printf("Array contents: ");
    for (int i = 0; i < size; ++i) {
        printf("%d ", *(dynamic_array + i)); // Access using pointer arithmetic
    }
    printf("\n");

    // IMPORTANT: Deallocate the memory when done
    free(dynamic_array);
    dynamic_array = NULL; // Good practice

    // sizeof(dynamic_array) here would just give sizeof(int*), not the allocated size.

    return 0;
}```

## Related Concepts
- [[Array_C]] (The data structure being allocated dynamically)
- [[Dynamic_Allocation_C]] (The underlying mechanism)
- [[malloc]], [[calloc_C]], [[realloc_C]], [[free]] (The functions used)
- [[Pointer_C]] (Used to store the address and access the array)
- [[Heap_Memory_C]] (Where the memory resides)
- [[sizeof_operator_C]] (Used to calculate element size for allocation, but doesn't work on the pointer to get allocated size)
- [[Memory_Leak_C]] (Risk if `free` is forgotten)
- [[Vector_C]] (Higher-level dynamic array structures often built using this technique - *to be created*)

---
**Source:** Worksheet C_WS3