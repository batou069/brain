---
tags:
  - data_structures
  - concept
  - linear
  - dynamic_array
aliases:
  - Dynamic Array
  - Growable Array
  - Resizable Array
  - Vector (Data Structure)
related:
  - "[[Data_Structure]]"
  - "[[Array_C]]"
  - "[[List_ADT]]"
  - "[[Amortized_Complexity]]"
  - "[[Direct_Access]]"
  - "[[Sequential_Access]]"
  - "[[malloc]]"
  - "[[realloc_C]]"
  - "[[free]]"
  - "[[Geometric_Expansion]]"
  - "[[Growth_Factor]]"
worksheet:
  - WS7
  - WS8
date_created: 2025-04-12
---
# Vector (Dynamic Array)

## Definition

A **Vector**, in the context of data structures (distinct from mathematical vectors), is a **dynamic array** or **growable array**. It's a linear [[Data_Structure]] that provides [[Direct_Access|direct (random) access]] to elements via an index, similar to a standard [[Array_C]], but with the ability to automatically resize itself (grow or shrink) as elements are added or removed.

## Key Aspects / Characteristics

- **Dynamic Sizing:** Can change size during runtime.
- **Contiguous Storage (Internally):** Typically implemented using an underlying static array allocated on the [[Heap_Memory_C]]. Elements are stored contiguously within this internal array.
- **Capacity vs. Size:** Maintains two concepts:
    - *Size (or Length):* The actual number of elements currently stored in the vector.
    - *Capacity:* The number of elements the underlying allocated array can currently hold. Capacity is always >= Size.
- **[[Direct_Access]]:** Accessing or modifying an element by index (`vector[i]`) is very fast, typically [[O_1]] on average, as long as the index is within the current *size*.
- **Appending (Amortized O(1)):** Adding an element to the end (`push_back`) is efficient on average. If `size < capacity`, it's [[O_1]]. If `size == capacity`, a resize is triggered:
    - A new, larger array is allocated (often using [[Geometric_Expansion]] - e.g., doubling capacity).
    - Elements are copied from the old array to the new one ([[O_n]] operation).
    - The old array is deallocated.
    - While resizing is O(n), it happens infrequently enough that the [[Amortized_Complexity|amortized cost]] per append operation remains **O(1)**.
- **Insertion/Deletion (Middle):** Inserting or deleting elements in the middle requires shifting subsequent elements, making these operations relatively slow ([[O_n]]).
- **Memory Management:** Handles its own memory allocation ([[malloc]], [[realloc_C]]) and deallocation ([[free]]) internally.

## Implementation (Conceptual C)

A vector in C would typically be implemented as a `struct` containing:
1.  A pointer to the dynamically allocated array on the heap (`element_type *data`).
2.  An integer storing the current number of elements (`size_t size`).
3.  An integer storing the current allocated capacity (`size_t capacity`).

Functions would be provided for operations like `create`, `destroy`, `push_back`, `pop_back`, `get_element`, `set_element`, `insert`, `remove`, `get_size`, `get_capacity`, `resize`, etc.

## Visualization

**Initial State:** `size=0`, `capacity=4` (example)
`data -> [ _, _, _, _ ]`

**After `push_back(A)`, `push_back(B)`:** `size=2`, `capacity=4`
`data -> [ A, B, _, _ ]`

**After `push_back(C)`, `push_back(D)`:** `size=4`, `capacity=4`
`data -> [ A, B, C, D ]`

**After `push_back(E)` (Triggers Resize):**
1. Allocate new array (e.g., capacity 8)
2. Copy A, B, C, D to new array
3. Add E
4. Free old array
**New State:** `size=5`, `capacity=8`
`data -> [ A, B, C, D, E, _, _, _ ]`

## Related Concepts
- [[Data_Structure]], [[List_ADT]] (Vector is a common implementation)
- [[Array_C]] (The underlying static structure often used)
- [[Dynamic_Allocation_C]] ([[malloc]], [[realloc_C]], [[free]])
- [[Amortized_Complexity]] (Key concept for append efficiency)
- [[Direct_Access]] (Fast access by index)
- [[Geometric_Expansion]], [[Growth_Factor]] (Strategy for resizing)
- C++ `std::vector`, Java `ArrayList`, Python `list` (Examples in other languages)

## Questions / Further Study
>[!question] When, where, and why do we need a dynamic vector? (WS8)
> We need a dynamic vector (vector/dynamic array) when:
> - We need array-like [[Direct_Access|direct access]] (O(1) lookup by index).
> - The number of elements is **not known at compile time** or can **change significantly** during runtime.
> - We frequently add elements to the **end** of the collection.
> **Why:** It provides the flexibility of variable size (like a linked list) while retaining the fast indexed access of an array. It avoids the fixed-size limitation of static arrays and the O(n) indexed access time of linked lists.

>[!question] Compare array vs. dynamic vector, including the relevant functions complexity. What are the differences / advantages between them? (WS8)
> | Feature             | Static Array (`int arr[N];`) | Dynamic Vector (`vector* v;`) |
> | :------------------ | :--------------------------- | :---------------------------- |
> | **Size**            | Fixed at compile time        | Dynamic, changes at runtime   |
> | **Allocation**      | Stack (if local) or Data/BSS (if global/static) | Heap (via `malloc`/`realloc`) |
> | **Memory Mgmt**     | Automatic (Stack) or None (Static) | Manual (via vector functions wrapping `free`) |
> | **Access by Index** | O(1)                         | O(1) (Amortized if index is valid) |
> | **Get Size**        | `sizeof(arr)/sizeof(arr[0])` (compile time) | `vector_size(v)` (O(1) runtime) |
> | **Add to End**      | N/A (fixed size)             | **O(1) Amortized**            |
> | **Insert/Delete Mid**| O(n) (manual shift needed if simulating) | O(n) (shifting elements)      |
> | **Memory Overhead** | Minimal                      | Stores size, capacity, pointer (small overhead) + potentially unused capacity |
> | **Flexibility**     | Low                          | High                          |
> **Advantages of Array:** Slightly faster element access (no indirection via pointer), less memory overhead (no size/capacity tracking), simpler if size is fixed and known.
> **Advantages of Vector:** Flexible size, handles unknown number of elements, efficient appending on average.

>[!question] What happens when the user sends an index bigger than size? (WS8)
> Accessing an index `i` where `i >= size` (the current number of elements) but potentially `i < capacity` accesses uninitialized or previously used (but now logically empty) parts of the underlying allocated array. This might return garbage data but doesn't necessarily crash immediately. Accessing an index `i` where `i >= capacity` accesses memory *outside* the allocated block, leading to **[[Undefined_Behavior_C]]** (likely a crash/segmentation fault). A robust vector implementation should include bounds checking in its access functions (e.g., `vector_get(v, i)`) to prevent this, potentially returning an error or terminating if the index is out of the valid range `[0, size-1]`. Direct access using `v->data[i]` bypasses such checks.

>[!question] What is the time complexity of push_back? (WS8)
> The **[[Amortized_Complexity|amortized time complexity]]** of `push_back` (appending to the end) on a dynamic vector that uses [[Geometric_Expansion]] (e.g., doubling capacity when full) is **O(1)**. While individual `push_back` operations that trigger a resize take O(n) time (where n is the current size), these expensive operations happen infrequently enough that their cost, when averaged over a long sequence of appends, contributes only a constant amount to the average cost per operation.

>[!question] When should the dynamic vector be resized, and what is the growth Factor? (WS8)
> - **When:** Resizing (increasing capacity) typically occurs during an insertion operation (like `push_back`) when the current `size` equals the current `capacity`. Some implementations might also offer explicit `resize` or `reserve` functions. Resizing (decreasing capacity) might occur during deletion operations if the size drops significantly below the capacity (e.g., size drops below capacity / 4) to save memory, though this is less common or done less aggressively than growing.
> - **[[Growth_Factor]]:** The factor by which the capacity is increased during a resize. Common growth factors include:
>     - **2 (Doubling):** Simple and ensures O(1) amortized append time. `new_capacity = old_capacity * 2`.
>     - **1.5 (Golden Ratio approx.):** Reduces memory waste compared to doubling, while still providing O(1) amortized append time. `new_capacity = old_capacity * 1.5`.
>     - Additive growth (`new_capacity = old_capacity + C`): **Leads to O(n) amortized append time** and should generally be avoided for growing vectors.

>[!question] Does realloc always succeed? Does realloc always malloc in place? What happens if it succeeds? What happens if it Fails? (WS8)
> See [[realloc_C]].
> - **Success:** `realloc` might resize the block in place (if space allows) or allocate a *new* block, copy the contents from the old block, free the old block, and return a pointer to the new block. If it succeeds, it returns a pointer to the (potentially new) start of the resized block. The original pointer passed to `realloc` should **not** be used afterwards unless `realloc` returned the same pointer.
> - **Failure:** If `realloc` cannot allocate the requested memory, it returns `NULL`. Crucially, if `realloc` fails, the **original memory block** (pointed to by the pointer passed to `realloc`) **remains allocated and unchanged**. You must still hold onto the original pointer to free it later or continue using the original block. **Never** assign the result of `realloc` directly back to the original pointer without checking for `NULL` first, or you risk losing the only pointer to the original block (a memory leak) if `realloc` fails.
>   ```c
>   // SAFE way to use realloc
>   int *temp = (int*)realloc(original_ptr, new_size_in_bytes);
>   if (temp == NULL && new_size_in_bytes > 0) {
>       // Realloc failed, original_ptr is still valid
>       perror("realloc failed");
>       // Handle error, maybe free(original_ptr) later
>   } else {
>       // Realloc succeeded (or new_size was 0)
>       // It's now safe to update the original pointer
>       original_ptr = temp;
>   }
>   ```

---
**Source:** Worksheet WS7, WS8