---
tags: [c, concept, pointer, memory, error, undefined_behavior]
aliases: [C Dangling Pointers]
related:
  - "[[Pointer_C]]"
  - "[[free]]"
  - "[[Dynamic_Allocation_C]]"
  - "[[Scope_C]]"
  - "[[Stack_Memory_C]]"
  - "[[Undefined_Behavior_C]]"
worksheet: [C_WS3]
date_created: 2025-04-11
---
# Dangling Pointer (C)

## Definition

A **Dangling Pointer** is a [[Pointer_C]] that points to a memory location that has been deallocated (freed) or is otherwise invalid (e.g., points to a [[Local_Variable_C|local variable]] after its function has returned). Dereferencing (accessing the value via `*`) or writing through a dangling pointer leads to [[Undefined_Behavior_C]].

## Key Aspects / Characteristics

- **Points to Invalid Memory:** The pointer variable itself still holds an address, but that address no longer corresponds to valid, allocated memory that the program is allowed to access for that pointer's original purpose.
- **Causes:**
    - **Using Pointer After `free()`:** Accessing memory via a pointer after `free()` has been called on that pointer.
    - **Returning Pointer to Local Variable:** A function returns a pointer to one of its [[Automatic_Variable_C|automatic local variables]]. When the function returns, the local variable's memory (on the [[Stack_Memory_C|stack]]) is deallocated, leaving the returned pointer dangling.
    - **Pointer to Reallocated Memory:** If [[realloc_C]] moves a memory block to a new location and returns a new address, pointers still holding the *old* address become dangling.
- **Undefined Behavior:** Using a dangling pointer (reading or writing) can lead to unpredictable results:
    - Program crashes (segmentation fault).
    - Silent data corruption (overwriting unrelated data that now occupies the freed memory).
    - Seemingly correct behavior (if the memory hasn't been reused *yet*, but this is unreliable).
- **Detection Difficulty:** Dangling pointers can be hard to detect, as the error might only manifest much later or intermittently.

## Examples / Use Cases

**1. Use After `free()`**
```c
#include <stdlib.h>
#include <stdio.h>

int main() {
    int *ptr = (int*)malloc(sizeof(int));
    if (!ptr) return 1;
    *ptr = 10;
    printf("Value before free: %d\n", *ptr);

    free(ptr); // Memory is deallocated

    // ptr is now a dangling pointer
    // *ptr = 20; // UNDEFINED BEHAVIOR! Accessing freed memory.
    // printf("Value after free (BAD): %d\n", *ptr); // UNDEFINED BEHAVIOR!

    // Good practice:
    ptr = NULL; // Set pointer to NULL to prevent accidental use

    return 0;
}
```

**2. Returning Address of Local Variable**
```c
#include <stdio.h>

int* create_local_int() {
    int local_var = 5;
    printf("  Inside function, address of local_var: %p\n", (void*)&local_var);
    return &local_var; // Returning address of variable that will be destroyed
} // local_var ceases to exist here

int main() {
    int *dangling_ptr = create_local_int();
    printf("In main, received address: %p\n", (void*)dangling_ptr);

    // dangling_ptr points to memory that is no longer valid (part of a destroyed stack frame)
    // printf("Value via dangling pointer (BAD): %d\n", *dangling_ptr); // UNDEFINED BEHAVIOR!

    return 0;
}
```

## Prevention Strategies

- Set pointers to [[NULL_C]] immediately after calling [[free]] on them.
- Never return pointers to automatic local variables from a function. Return data by value, or allocate memory on the heap ([[malloc]]) and return a pointer to that (requiring the caller to `free` it later).
- Be careful when using [[realloc_C]]; update all relevant pointers if the memory block is moved.
- Use static analysis tools and memory debuggers (like Valgrind) to help detect dangling pointer usage.

## Related Concepts
- [[Pointer_C]] (The type of variable involved)
- [[free]], [[Dynamic_Allocation_C]] (Common source: use after free)
- [[Scope_C]], [[Local_Variable_C]], [[Stack_Memory_C]] (Common source: returning address of local)
- [[Undefined_Behavior_C]] (The consequence of using a dangling pointer)
- [[NULL_C]] (Assigning NULL after free helps prevent accidental use)

---
**Source:** Worksheet C_WS3