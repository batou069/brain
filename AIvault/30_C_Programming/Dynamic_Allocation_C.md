---
tags: [c_programming, concept]
aliases: []
related: []
worksheet: [WS]
date_created: 2025-04-11
---
# Dynamic Memory Allocation (C)

## Definition

**Dynamic Memory Allocation** in C refers to the process of allocating memory for variables or data structures at **runtime** (while the program is running), rather than at compile time. This memory is allocated from a region called the [[Heap_Memory_C|heap]]. Dynamically allocated memory persists until it is explicitly deallocated by the programmer.

## Key Aspects / Characteristics

- **Runtime Allocation:** Memory size and allocation timing can be determined while the program executes, allowing for flexible memory usage based on input or changing conditions.
- **Heap Storage:** Memory is allocated from the [[Heap_Memory_C|heap]], a large pool of memory managed by the C runtime library, separate from the [[Stack_Memory_C|stack]] (used for automatic variables) and static/global data segments.
- **Explicit Deallocation:** Memory allocated dynamically **must** be explicitly released back to the system using [[free]] when it's no longer needed. Failure to do so results in a [[Memory_Leak_C]].
- **Pointer-Based:** Dynamic allocation functions ([[malloc]], [[calloc_C]], [[realloc_C]]) return a [[Pointer_C]] to the beginning of the allocated memory block (or [[NULL_C]] if allocation fails). This pointer is the only way to access the allocated memory.
- **`sizeof` Usage:** The [[sizeof_operator_C]] is crucial for calculating the correct number of bytes to request (e.g., `malloc(10 * sizeof(int))` to allocate space for 10 integers).
- **Flexibility:** Allows creating data structures whose size is unknown at compile time (e.g., arrays based on user input, linked lists, trees).
- **Responsibility:** Puts the burden of memory management (allocation and deallocation) entirely on the programmer.

## Core Functions (`<stdlib.h>`)

-   **[[malloc]](`size_t size`):** Allocates `size` bytes of uninitialized memory. Returns `void*` pointer to the block, or `NULL` on failure.
-   **[[calloc_C]](`size_t num, size_t size`):** Allocates memory for an array of `num` elements, each of `size` bytes. Initializes the allocated memory to all zero bits. Returns `void*` or `NULL`.
-   **[[realloc_C]](`void *ptr, size_t new_size`):** Attempts to resize a previously allocated memory block (pointed to by `ptr`) to `new_size`. May move the block to a new location. Returns `void*` to the (potentially new) block, or `NULL` on failure (original block remains allocated). If `ptr` is `NULL`, it behaves like `malloc`. If `new_size` is 0, it may free the block or return `NULL` (implementation-defined).
-   **[[free]](`void *ptr`):** Deallocates the memory block previously allocated by `malloc`, `calloc`, or `realloc` and pointed to by `ptr`. Passing `NULL` to `free` is safe and does nothing. Freeing memory not allocated dynamically or freeing the same block twice leads to [[Undefined_Behavior_C]].

## Examples / Use Cases

```c
#include <stdio.h>
#include <stdlib.h> // For malloc, free

int main() {
    int *dynamic_int_ptr = NULL;
    int *dynamic_array = NULL;
    int num_elements;

    // Allocate memory for a single integer
    dynamic_int_ptr = (int*)malloc(sizeof(int));
    if (dynamic_int_ptr == NULL) {
        fprintf(stderr, "Memory allocation failed!\n");
        return 1; // Exit indicating error
    }
    *dynamic_int_ptr = 123; // Use the allocated memory
    printf("Dynamically allocated int: %d\n", *dynamic_int_ptr);

    // Deallocate the memory for the single integer
    free(dynamic_int_ptr);
    dynamic_int_ptr = NULL; // Good practice to NULL pointer after free

    // Allocate memory for an array based on user input
    printf("Enter number of elements for array: ");
    scanf("%d", &num_elements);

    if (num_elements <= 0) {
         printf("Invalid number of elements.\n");
         return 1;
    }

    dynamic_array = (int*)malloc(num_elements * sizeof(int));
    if (dynamic_array == NULL) {
        fprintf(stderr, "Array memory allocation failed!\n");
        return 1;
    }

    // Use the dynamically allocated array
    printf("Allocated space for %d integers.\n", num_elements);
    for (int i = 0; i < num_elements; ++i) {
        dynamic_array[i] = i * 10;
        printf("dynamic_array[%d] = %d\n", i, dynamic_array[i]);
    }

    // Deallocate the array memory
    free(dynamic_array);
    dynamic_array = NULL;

    return 0;
}
```

## Related Concepts
- [[50_Data_Structures/Memory_Management]] (Dynamic allocation is one aspect)
- [[Heap_Memory_C]] (Where the memory comes from)
- [[Stack_Memory_C]] (Contrasted with heap allocation)
- [[Pointer_C]] (Essential for accessing allocated memory)
- [[malloc]], [[free]], [[calloc_C]], [[realloc_C]] (The library functions)
- [[sizeof_operator_C]] (Used to calculate allocation size)
- [[NULL_C]] (Return value on allocation failure)
- [[Dangling_Pointer_C]] (Pointer after `free` if not set to NULL)
- [[Memory_Leak_C]] (Forgetting to `free` allocated memory)
- [[Undefined_Behavior_C]] (Using freed memory, double free, etc.)

---
**Source:** Worksheet C_WS3