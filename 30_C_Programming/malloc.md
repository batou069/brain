---
tags: [c, function, stdlib, memory, pointer, dynamic_allocation]
aliases: []
related:
  - "[[Dynamic_Allocation_C]]"
  - "[[free]]"
  - "[[calloc_C]]"
  - "[[realloc_C]]"
  - "[[Heap_Memory_C]]"
  - "[[Pointer_C]]"
  - "[[void_pointer_C]]"
  - "[[sizeof_operator_C]]"
  - "[[NULL_C]]"
  - "[[Memory_Leak_C]]"
worksheet: [C_WS3]
header_file: <stdlib.h>
date_created: 2025-04-11
---
# ` malloc() `

## Purpose

The `malloc()` (memory allocation) function allocates a block of memory of a specified size (in bytes) from the [[Heap_Memory_C|heap]]. The content of the allocated block is uninitialized (contains garbage values).

## Signature

```c
#include <stdlib.h>
void *malloc(size_t size);
```

## Parameters

-   `size`: A `size_t` (unsigned integer type) value specifying the number of bytes of memory to allocate.

## Return Value

-   On **success**, returns a `void*` ([[void_pointer_C]]) pointer to the beginning of the allocated memory block. This `void*` pointer can (and usually must) be cast to the appropriate pointer type (e.g., `int*`, `char*`, `struct MyStruct*`) before being used.
-   On **failure** (e.g., if insufficient memory is available on the heap), returns a [[NULL_C|NULL pointer]].

## Example Usage

```c
#include <stdio.h>
#include <stdlib.h> // Required for malloc, free

typedef struct {
    int id;
    double value;
} Record;

int main() {
    int *int_ptr = NULL;
    Record *record_ptr = NULL;
    size_t num_records = 5;

    // Allocate memory for a single integer
    int_ptr = (int*)malloc(sizeof(int)); // Request size of one int
    if (int_ptr == NULL) {
        perror("malloc failed for int");
        return 1;
    }
    *int_ptr = 101;
    printf("Allocated int value: %d\n", *int_ptr);
    free(int_ptr); // Don't forget to free!
    int_ptr = NULL;

    // Allocate memory for an array of 5 Record structs
    record_ptr = (Record*)malloc(num_records * sizeof(Record)); // Request size for 5 Records
    if (record_ptr == NULL) {
        perror("malloc failed for Record array");
        return 1;
    }

    // Initialize and use the allocated memory (content is initially garbage)
    for (size_t i = 0; i < num_records; ++i) {
        record_ptr[i].id = i + 1;
        record_ptr[i].value = (i + 1) * 1.1;
        printf("Record %zu: ID=%d, Value=%.2f\n", i, record_ptr[i].id, record_ptr[i].value);
    }

    free(record_ptr); // Free the entire block
    record_ptr = NULL;

    return 0;
}
```

## Related Functions/Concepts
- [[Dynamic_Allocation_C]] (The overall concept)
- [[free]] (Used to deallocate memory allocated by `malloc`)
- [[calloc_C]] (Allocates and zero-initializes memory)
- [[realloc_C]] (Resizes previously allocated memory)
- [[Heap_Memory_C]] (Where the memory comes from)
- [[Pointer_C]], [[void_pointer_C]] (Return type)
- [[sizeof_operator_C]] (Crucial for calculating the `size` argument)
- [[NULL_C]] (Return value on failure, always check for it!)
- [[Memory_Leak_C]] (Occurs if `free` is not called)
- [[Type_Cast_C]] (Usually needed for the returned `void*`)

## Notes
>[!warning] Initialization
> `malloc()` does **not** initialize the allocated memory. It will contain indeterminate ("garbage") values. If you need zero-initialized memory, use [[calloc_C]] or initialize the memory manually after `malloc`.

>[!warning] Error Checking
> **Always** check the return value of `malloc()` against [[NULL_C]]. If allocation fails and you attempt to use the `NULL` pointer, your program will likely crash ([[Undefined_Behavior_C]]).

---
**Source:** Worksheet C_WS3