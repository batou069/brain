---
tags:
  - python
  - memory_management
  - cpython
  - garbage_collection
  - reference_counting
  - memory_pools
  - concept
  - internal
aliases:
  - Python Memory Allocation
  - CPython Memory
  - Python GC
  - Reference Counting Python
related:
  - "[[Python_Execution_Model_PVM_Bytecode|Python Execution Model (PVM, Bytecode)]]"
  - "[[Python_References_Variables]]"
worksheet:
  - WS16
date_created: 2025-06-11
---
# Python Memory Management

Python manages memory automatically, meaning developers typically don't need to explicitly allocate or deallocate memory as they might in languages like C or C++. This is a key feature contributing to Python's ease of use. The specifics of memory management can vary slightly between Python implementations (CPython, Jython, PyPy), but this note will primarily focus on **CPython**, the reference implementation.

CPython uses a combination of techniques:
1.  **Object Allocation System (Blocks, Pools, Arenas):** For efficient allocation of small objects.
2.  **[[Python_Memory_Management#Reference Counting|Reference Counting]]:** The primary mechanism for reclaiming memory of objects that are no longer in use.
3.  **[[Python_Memory_Management#Generational Garbage Collector|Generational Garbage Collector]]:** A secondary mechanism to collect cyclic references that reference counting alone cannot handle.

## 1. CPython's Object Allocator (for small objects)
CPython has a specialized memory allocator for objects smaller than 512 bytes to optimize for speed and reduce memory fragmentation. This system works on top of the system's general-purpose allocator (`malloc`). It organizes memory into a hierarchy:

-   **Arenas:**
    -   The largest chunks of memory, typically 256 KiB, allocated from the system heap.
    -   Arenas are aligned on a page boundary (often 4 KiB).
-   **Pools:**
    -   Each arena is divided into multiple **pools** of a fixed size (typically the system page size, e.g., 4 KiB).
    -   A single pool can only store objects of the same size class (e.g., a pool for objects of 1-8 bytes, another for 9-16 bytes, etc.).
    -   Pools can be in one of three states:
        -   `used`: Partially filled with objects, has free space.
        -   `full`: All blocks are allocated.
        -   `empty`: No objects allocated, can be returned to the arena or reused for a different size class.
-   **Blocks:**
    -   Each pool is divided into fixed-size **blocks** of memory. The size of the block is determined by the size class of objects the pool is intended to store.
    -   A single Python object is stored within a block.
    -   When an object is deallocated, its block is marked as free and can be reused for a new object of the same size class within that pool.

**Benefits of this system:**
-   **Speed:** Allocating small objects from pre-allocated pools and blocks is much faster than calling the system `malloc` for every small object.
-   **Reduced Fragmentation:** By grouping objects of similar sizes into pools, it reduces external memory fragmentation.
-   **Memory Locality (Potentially):** Objects of the same type (and thus often size) might be allocated close together, which can be beneficial for CPU cache performance.

For objects larger than 512 bytes, CPython typically uses the system's `malloc` directly.

## 2. Reference Counting
This is the primary garbage collection mechanism in CPython.
-   **How it Works:**
    -   Every object in Python memory has a **reference count**, which is an integer indicating how many [[Python_References_Variables|names (variables) or other objects]] currently refer to it.
    -   When a name is assigned to an object, the object's reference count is incremented.
        ```python
        x = [] # List object created, ref count = 1 (due to x)
        y = x  # y now also refers to the same list, ref count = 2
        ```
    -   When a name goes out of scope, is reassigned to another object, or is deleted (using `del`), the reference count of the object it was pointing to is decremented.
        ```python
        del y  # ref count of the list becomes 1
        x = None # ref count of the list becomes 0
        ```
    -   When an object's reference count drops to **zero**, it means the object is no longer accessible from anywhere in the program. CPython immediately deallocates the memory occupied by this object, making it available for reuse.
-   **Advantages:**
    -   **Immediate Reclamation:** Memory is reclaimed as soon as an object becomes unreachable. This leads to relatively smooth memory usage without long pauses for garbage collection.
    -   **Deterministic:** The deallocation is predictable.
-   **Disadvantage:**
    -   **Cannot Handle Cyclic References:** If two or more objects refer to each other in a cycle, but are not referenced by anything else, their reference counts will never drop to zero, even though they are unreachable. This leads to memory leaks.
        ```python
        a = []
        b = []
        a.append(b) # a refers to b (b's ref count++)
        b.append(a) # b refers to a (a's ref count++)
        # Now a and b form a cycle.
        del a
        del b
        # Even after 'del a' and 'del b', the objects they pointed to still have
        # non-zero reference counts because they refer to each other.
        # These objects are now unreachable but not deallocated by reference counting alone.
        ```

## 3. Generational Garbage Collector (for Cyclic References)
To address the issue of cyclic references not handled by reference counting, CPython includes a supplementary **generational garbage collector**.
-   **How it Works (Simplified):**
    -   It divides objects into different **generations** (typically three: generation 0, 1, and 2).
    -   New objects start in generation 0.
    -   The garbage collector runs more frequently on younger generations (like generation 0) because new objects are more likely to become "dead" (unreachable) quickly.
    -   If an object survives a collection cycle in a younger generation, it gets promoted to an older generation.
    -   The collector periodically scans objects, looking specifically for **unreachable cyclic data structures**. It does this by:
        1.  Identifying "container" objects (objects that can hold references to other objects, like lists, dictionaries, instances of user-defined classes).
        2.  Temporarily breaking references to see if reference counts drop to zero through a more complex reachability analysis (often a mark-and-sweep like algorithm or variations).
        3.  If objects in a cycle are found to be unreachable from outside the cycle, they are collected.
-   **When it Runs:** The garbage collector runs periodically, or it can be triggered manually using the `gc` module (e.g., `gc.collect()`). The frequency is determined by thresholds based on the number of allocations and deallocations.
-   **Trade-offs:**
    -   Can cause slight pauses in program execution when it runs, but these are generally managed to be short for younger generations.
    -   Solves the cyclic reference problem that reference counting alone cannot.

## `gc` Module
Python's `gc` module provides an interface to the garbage collector:
-   `gc.enable()`: Enable automatic garbage collection.
-   `gc.disable()`: Disable automatic garbage collection.
-   `gc.collect(generation=2)`: Run a full collection (or for a specific generation).
-   `gc.get_threshold()`: Get current collection thresholds.
-   `gc.set_threshold(threshold0, threshold1, threshold2)`: Set collection thresholds.

## Summary
Python's memory management is designed to be automatic and largely transparent to the developer.
-   Small objects are efficiently managed by CPython's custom allocator using **blocks, pools, and arenas**.
-   The primary mechanism for reclaiming memory is **reference counting**, which deallocates objects immediately when they are no longer referenced.
-   A **generational garbage collector** complements reference counting by periodically detecting and collecting unreachable cyclic data structures.

This combination provides a balance between performance (fast allocation/deallocation for common cases) and robustness (handling complex object graphs).

---