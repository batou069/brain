---
tags:
  - c
  - concept
  - error
  - runtime_error
  - memory
  - recursion
  - stack
aliases:
  - C Stack Overflow
related:
  - Stack_Memory_C
  - Stack_Segment_C
  - Recursion_C
  - Function_Call_C
  - Automatic_Variable_C
  - Segmentation_Fault
  - Operating_System
worksheet:
  - WS10
  - WS13
date_created: 2025-04-14
---
# Stack Overflow (C)

## Definition

A **Stack Overflow** is a runtime error that occurs when a program attempts to use more memory space on the [[Stack_Segment_C|call stack]] than has been allocated for it. The stack has a limited size, and when this limit is exceeded (the stack pointer goes beyond the allocated boundary), a stack overflow happens, typically causing the program to crash, often with a [[Segmentation_Fault]].

## Causes

1.  **Deep [[Recursion_C|Recursion]]:** The most common cause. Each recursive [[Function_Call_C]] pushes a new [[Stack_Frame_C]] onto the stack. If the recursion depth is too large (due to large input, slow convergence to the [[Stop_Condition_C|base case]], or infinite recursion caused by a missing/incorrect base case), the stack space is exhausted.
2.  **Very Large [[Automatic_Variable_C|Automatic (Local) Variables]]:** Declaring extremely large arrays or structures as local variables inside a function allocates them on the stack frame for that function. If a single frame (or the cumulative size of frames) exceeds the stack limit, an overflow occurs.
    ```c
    void problematic_function() {
        char large_buffer[2 * 1024 * 1024]; // Request 2MB on the stack - likely overflow!
        // ... use buffer ...
    }
    ```
3.  **Incorrect Stack Pointer Manipulation:** (Rare in standard C, more likely in assembly or with compiler bugs) Directly manipulating the stack pointer register incorrectly.

## Consequences

- **Program Crash:** Usually results in abnormal program termination.
- **[[Segmentation_Fault]] (Segfault):** On Unix-like systems, attempting to access memory outside the allocated stack segment often triggers a segmentation fault signal (`SIGSEGV`).
- **Stack Smashing / Corruption:** In some cases, overflowing the stack might overwrite crucial data in adjacent stack frames (like return addresses or saved registers), potentially leading to unpredictable behavior or security vulnerabilities (stack buffer overflows).

## Prevention / Mitigation

- **Avoid Deep/Infinite Recursion:** Ensure recursive functions have correct, reachable base cases. Consider iterative solutions if recursion depth might be very large. Use [[Tail_Recursion_C|tail recursion]] optimization if supported and applicable (though not guaranteed in C).
- **Avoid Very Large Stack Allocations:** Allocate large arrays or structures dynamically on the [[Heap_Memory_C]] using [[malloc]] instead of declaring them as local variables.
- **Increase Stack Size (If Possible):** Some operating systems or compiler/linker settings allow increasing the default stack size allocated per thread or process, but this is often a workaround rather than a fix for the underlying problem.

## Related Concepts
- [[Stack_Memory_C]], [[Stack_Segment_C]] (The memory region that overflows)
- [[Recursion_C]] (Common cause)
- [[Function_Call_C]], [[Stack_Frame_C]] (Stack usage mechanism)
- [[Automatic_Variable_C]] (Large ones can cause overflow)
- [[Segmentation_Fault]] (Common symptom)
- [[Heap_Memory_C]], [[Dynamic_Allocation_C]] (Alternative for large data)
- [[Operating_System]] (Manages process memory, including stack limits)

## Questions / Further Study
>[!question] What is a stack overflow error? What causes it? (WS13)
> A stack overflow error is a runtime error occurring when a program tries to use more memory on the call [[Stack_Segment_C|stack]] than is available. It's primarily caused by:
> 1.  **Deep or Infinite [[Recursion_C]]:** Too many nested function calls consume all available stack space for their [[Stack_Frame_C|stack frames]].
> 2.  **Large [[Automatic_Variable_C|Local Variables]]:** Declaring excessively large arrays or structs as local variables within functions can exceed the stack limit.

---
**Source:** Worksheet WS10, WS13