---
tags: [c, function, stdlib, memory, pointer, dynamic_allocation]
aliases: []
related:
  - "[[Dynamic_Allocation_C]]"
  - "[[malloc]]"
  - "[[calloc_C]]"
  - "[[realloc_C]]"
  - "[[Heap_Memory_C]]"
  - "[[Pointer_C]]"
  - "[[NULL_C]]"
  - "[[Dangling_Pointer_C]]"
  - "[[Memory_Leak_C]]"
  - "[[Undefined_Behavior_C]]"
worksheet: [C_WS3]
header_file: <stdlib.h>
date_created: 2025-04-11
---
# ` free() `

## Purpose

The `free()` function deallocates a block of memory previously allocated using [[malloc]], [[calloc_C]], or [[realloc_C]], returning it to the [[Heap_Memory_C|heap]] manager so it can be reused for future allocations.

## Signature

```c
#include <stdlib.h>
void free(void *ptr);
```

## Parameters

-   `ptr`: A `void*` pointer to the beginning of a memory block that was previously returned by `malloc`, `calloc`, or `realloc`.

## Return Value

-   `free()` returns no value (`void`).

## Key Aspects

-   **Deallocation:** Marks the memory block pointed to by `ptr` as available for reuse.
-   **Pointer Invalidation:** After `free(ptr)` is called, the pointer `ptr` itself still holds the same address value, but it now points to deallocated memory. Accessing memory through this pointer ([[Dangling_Pointer_C]]) leads to [[Undefined_Behavior_C]]. It's good practice to set the pointer to [[NULL_C]] immediately after freeing it (`ptr = NULL;`).
-   **Matching Allocation:** `free()` must be called exactly once for each successful call to `malloc`, `calloc`, or `realloc` that allocated the block.
-   **`NULL` Pointer Safe:** If `ptr` is `NULL`, `free(ptr)` does nothing and is guaranteed to be safe.
-   **Errors:**
    -   *Double Free:* Calling `free()` twice on the same non-NULL pointer leads to [[Undefined_Behavior_C]] (often memory corruption or crash).
    -   *Invalid Pointer:* Calling `free()` on a pointer that was not obtained from `malloc`/`calloc`/`realloc` (e.g., a pointer to a stack variable or static variable) leads to [[Undefined_Behavior_C]].

## Example Usage

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *numbers = NULL;
    size_t count = 10;

    // Allocate memory
    numbers = (int*)malloc(count * sizeof(int));
    if (numbers == NULL) {
        perror("malloc failed");
        return 1;
    }
    printf("Memory allocated at address: %p\n", (void*)numbers);

    // Use the memory (example)
    for (size_t i = 0; i < count; ++i) {
        numbers[i] = i;
    }

    // Deallocate the memory
    printf("Freeing memory...\n");
    free(numbers);

    // Good practice: Set pointer to NULL after freeing
    numbers = NULL;

    // Attempting to use 'numbers' now would be undefined behavior
    // if (numbers != NULL) { // This check prevents crash if numbers is NULL
    //    printf("Value after free (BAD): %d\n", numbers[0]);
    // }

    // Freeing NULL is safe
    free(NULL);
    printf("Freeing NULL pointer did not crash.\n");

    return 0;
}
```

## Related Functions/Concepts
- [[Dynamic_Allocation_C]] (The overall concept)
- [[malloc]], [[calloc_C]], [[realloc_C]] (Functions that allocate memory needing `free`)
- [[Heap_Memory_C]] (Where memory is returned to)
- [[Pointer_C]] (The argument type)
- [[Dangling_Pointer_C]] (The state of the pointer after `free` if not set to NULL)
- [[Memory_Leak_C]] (Result of *not* calling `free`)
- [[Undefined_Behavior_C]] (Result of double free or freeing invalid pointers)
- [[NULL_C]] (Safe value to pass to `free`)

---
**Source:** Worksheet C_WS3