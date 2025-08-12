---
tags: [c, concept, variable, memory, alias]
aliases: [C Heap Variables]
related:
  - "[[Heap_Memory_C]]"
  - "[[Dynamic_Allocation_C]]"
  - "[[Pointer_C]]"
  - "[[malloc]]"
  - "[[free]]"
worksheet: [C_WS3]
date_created: 2025-04-11
---
# Heap "Variable" (C)

## Definition

While C doesn't have a distinct keyword for a "heap variable" in the same way it has [[Automatic_Variable_C|automatic]] or [[Static_Variable_C|static]] variables, the term **Heap Variable** is often used informally to refer to a block of memory allocated on the [[Heap_Memory_C|heap]] using [[Dynamic_Allocation_C|dynamic memory allocation]] functions like [[malloc]]. This memory is not associated with a named variable identifier directly but is instead accessed solely through a [[Pointer_C]].

## Key Aspects / Characteristics

- **Informal Term:** Not official C terminology, but commonly understood.
- **Dynamic Allocation:** Refers to memory obtained via [[malloc]], [[calloc_C]], or [[realloc_C]].
- **Heap Storage:** Resides in the [[Heap_Memory_C]] region.
- **Pointer Access:** Can *only* be accessed via a [[Pointer_C]] variable that stores the starting address returned by the allocation function. The pointer variable itself might be automatic (stack) or static/global.
- **Manual Lifetime Management:** The programmer is responsible for explicitly deallocating the memory using [[free]] when it's no longer needed. The lifetime is not tied to function scope.
- **No Name:** The allocated memory block itself doesn't have a variable name like stack or static variables do.

## Examples / Use Cases

```c
#include <stdlib.h>

int main() {
    int *heap_ptr; // 'heap_ptr' is an automatic (stack) variable

    // Allocate memory on the heap. The memory block itself is the "heap variable".
    heap_ptr = (int*)malloc(sizeof(int));
    if (!heap_ptr) return 1;

    // Access the "heap variable" through the pointer
    *heap_ptr = 100;

    // ... use *heap_ptr ...

    // Deallocate the "heap variable"
    free(heap_ptr);
    heap_ptr = NULL;

    return 0;
}
```
In this example, `heap_ptr` is a stack variable holding an address. The memory block at that address (allocated by `malloc`) is what we informally call the "heap variable".

## Related Concepts
- [[Heap_Memory_C]] (The location)
- [[Dynamic_Allocation_C]] (The process)
- [[Pointer_C]] (The access mechanism)
- [[malloc]], [[free]] (The management functions)
- [[Stack_Variable_C]], [[Data_Variable_C]] (Contrasted with heap allocation)

---
**Source:** Worksheet C_WS3