---
tags:
  - c
  - os
  - concept
  - core
  - memory
  - python
  - mem
aliases:
  - Memory Management
related:
  - "[[Operating_System]]"
  - "[[Kernel]]"
  - "[[Process]]"
  - "[[Virtual_memory]]"
  - "[[Memory_Segments_C]]"
  - "[[Stack_Memory_C]]"
  - "[[Heap_Memory_C]]"
  - "[[Dynamic_Allocation_C]]"
  - "[[malloc]]"
  - "[[free]]"
  - "[[Paging]]"
  - "[[MMU]]"
  - "[[Garbage_Collection]]"
  - "[[Memory_Leak_C]]"
  - "[[Dangling_Pointer_C]]"
worksheet:
  - WS13
date_created: 2025-04-21
---
# Memory Management

## Definition

**Memory Management** is the process by which a computer system (primarily the [[Operating_System]] in coordination with hardware like the [[MMU]]) manages primary memory ([[RAM]]). It involves allocating portions of memory to programs (processes) when they need it and freeing it for reuse when they no longer do, while ensuring processes do not interfere with each other's allocated memory or the OS itself.

## Key Responsibilities & Techniques

1.  **Allocation/Deallocation:**
    -   Assigning memory blocks to processes for their code, data, stack, and heap.
    -   Reclaiming memory when processes terminate or explicitly release it ([[free]]).
    -   Tracking which parts of memory are currently in use and which are free.

2.  **Address Space Management ([[Virtual_memory]]):**
    -   Providing each [[Process]] with its own private virtual address space.
    -   Translating virtual addresses used by processes into physical addresses in [[RAM]] using [[Paging]] and [[Page_Table|Page Tables]], often assisted by the [[MMU]].

3.  **Memory Protection:**
    -   Ensuring a process cannot access memory outside its allocated virtual address space, protecting the OS kernel and other processes from corruption. Usually enforced by the [[MMU]].

4.  **Swapping/Paging:**
    -   Using secondary storage ([[Swap_Space]]) as an extension of RAM when physical memory is full. Inactive memory pages are moved (swapped out) to disk and loaded back (swapped in) when needed ([[Paging|Demand Paging]]). See [[Virtual_memory]].

5.  **Sharing:**
    -   Allowing multiple processes to share the same physical memory pages (e.g., for shared libraries or inter-process communication) by mapping them into the virtual address spaces of relevant processes.

## C Language Context

- **Manual Memory Management (Heap):** C requires programmers to explicitly manage memory allocated on the [[Heap_Memory_C]] using [[Dynamic_Allocation_C]] functions ([[malloc]], [[calloc_C]], [[realloc_C]]) and [[free]]. Failure to `free` leads to [[Memory_Leak_C|memory leaks]]; using memory after `free` leads to [[Dangling_Pointer_C|dangling pointers]].
- **Automatic Memory Management (Stack):** Memory for [[Automatic_Variable_C|automatic local variables]] is managed automatically on the [[Stack_Memory_C]] as functions are called and return.
- **Static Memory Management (Data/BSS):** Memory for global and static variables ([[Static_Variable_C]]) is allocated in the [[Data_Segment_C]] or [[BSS_Segment_C]] when the program loads and persists for the program's lifetime.

## Python Language Context

- **Automatic Memory Management (Garbage Collection):** Python uses [[Garbage_Collection]] to automatically manage memory. The Python runtime (CPython) primarily uses **reference counting** to track objects, freeing them when their reference count drops to zero. Cyclic references are handled by a **cyclic garbage collector** (in the `gc` module).
- **Stack and Heap:** Like C, Python uses the [[Stack_Memory_C]] for function call frames and local variables, but all objects (e.g., integers, lists) are allocated on the [[Heap_Memory_C]]. Python abstracts manual allocation/deallocation (no `malloc` or `free` equivalent).
- **Memory Management Tools:** Python provides tools to inspect and manage memory:
  - `sys.getsizeof()`: Returns the size of an object in bytes.
  - `gc` module: Allows manual control over the cyclic garbage collector (e.g., `gc.collect()` to force collection).
- **Potential Issues:** While Python avoids [[Memory_Leak_C|memory leaks]] from manual allocation, leaks can still occur due to lingering references (e.g., global variables or cyclic references not collected). No direct [[Dangling_Pointer_C|dangling pointer]] issues due to automatic management, but improper use of objects can lead to unexpected behavior.

## Contrast with Garbage Collection

- Languages like Java, Python, C# use **[[Garbage_Collection|Automatic Garbage Collection]]**. The runtime environment automatically detects and reclaims memory that is no longer reachable by the program, relieving the programmer from manual `free` calls but introducing potential overhead and non-deterministic pauses. C does **not** have built-in garbage collection.

## Related Concepts
- [[Operating_System]], [[Kernel]], [[MMU]]
- [[Process]], [[Virtual_memory]], [[Memory_Segments_C]]
- [[RAM]], [[Swap_Space]]
- [[Stack_Memory_C]], [[Heap_Memory_C]], [[Data_Segment_C]], [[BSS_Segment_C]]
- [[Paging]], [[Page_Table]], [[Page_Fault]]
- [[Dynamic_Allocation_C]], [[malloc]], [[free]]
- [[Memory_Leak_C]], [[Dangling_Pointer_C]], [[Segmentation_Fault]]
- [[Garbage_Collection]]

## Questions / Further Study
>[!question] Explain the need in memory management? (WS13)
> Memory management is essential to:
> 1.  **Allocate/Deallocate:** Provide memory to processes and reclaim it for reuse.
> 2.  **Sharing:** Enable safe sharing of resources like code libraries.
> 3.  **Protection:** Isolate processes from each other and protect the OS kernel.
> 4.  **Abstraction:** Give processes a simple, consistent view of memory (virtual address space).
> 5.  **Efficiency:** Utilize limited physical RAM effectively, allowing more programs to run than would physically fit (via [[Virtual_memory]]).

---
**Source:** Worksheet WS13 (Implied), General OS/CS knowledge