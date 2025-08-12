---
tags:
  - c
  - concept
  - memory
  - dynamic_allocation
aliases:
  - C Heap
  - Free Store C
related:
  - "[[50_Data_Structures/Memory_Management]]"
  - "[[Dynamic_Allocation_C]]"
  - "[[malloc]]"
  - "[[free]]"
  - "[[calloc_C]]"
  - "[[realloc_C]]"
  - "[[Stack_Memory_C]]"
  - "[[Memory_Segments_C]]"
  - "[[Pointer_C]]"
  - "[[Memory_Leak_C]]"
worksheet:
  - C_WS3
  - C_WS6
date_created: 2025-04-11
---
# Heap Memory (C)

## Definition

The **Heap** in C refers to a region of a process's memory used for [[Dynamic_Allocation_C|dynamic memory allocation]]. Unlike the [[Stack_Memory_C|stack]] (used for function calls and local variables) or static/global data segments, memory on the heap is explicitly requested by the programmer at runtime (using functions like [[malloc]], [[calloc_C]], [[realloc_C]]) and persists until explicitly deallocated (using [[free]]).

## Key Aspects / Characteristics

- **Dynamic Allocation:** Used for memory whose size or lifetime is not known at compile time.
- **Runtime Management:** Managed by the C runtime library's memory allocator.
- **Explicit Control:** Programmer is responsible for requesting allocation ([[malloc]], etc.) and ensuring deallocation ([[free]]).
- **No Automatic Cleanup:** Memory allocated on the heap remains allocated until `free` is called, even after the function that allocated it returns. Failure to `free` leads to [[Memory_Leak_C|memory leaks]].
- **Flexibility:** Allows creating data structures that can grow or shrink during program execution.
- **Slower Allocation:** Allocation/deallocation on the heap is generally slower than stack allocation due to the need for the memory manager to find suitable blocks and manage fragmentation.
- **Fragmentation:** Over time, repeated allocation and deallocation can lead to heap fragmentation (where available memory is broken into small, non-contiguous blocks), potentially making it difficult to allocate large contiguous chunks later.
- **Access via Pointers:** Memory allocated on the heap is accessed exclusively through [[Pointer_C|pointers]] returned by the allocation functions.

## Examples / Use Cases

- Allocating an array whose size is determined by user input.
- Implementing dynamic data structures like linked lists, trees, hash tables.
- Reading a file into memory when the file size isn't known beforehand.
- Creating objects or data buffers that need to outlive the function that creates them.

```c
// See examples in [[Dynamic_Allocation_C]], [[malloc]], [[free]]
```

## Related Concepts
- [[50_Data_Structures/Memory_Management]] (Heap is a key part)
- [[Dynamic_Allocation_C]] (Takes place on the heap)
- [[malloc]], [[free]], [[calloc_C]], [[realloc_C]] (Functions operating on the heap)
- [[Stack_Memory_C]] (Contrasted with heap: automatic, faster, limited size, LIFO)
- [[Memory_Segments_C]] (Heap is one segment)
- [[Pointer_C]] (Used to access heap memory)
- [[Memory_Leak_C]] (Problem caused by not freeing heap memory)
- Heap Fragmentation (Potential performance issue)

---
**Source:** Worksheet C_WS3, C_WS6