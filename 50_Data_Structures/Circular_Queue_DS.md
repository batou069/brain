---
tags:
  - data_structures
  - concept
  - implementation
  - queue
  - array
aliases:
  - Circular Buffer (Queue Context)
  - Ring Buffer
related:
  - Data_Structure
  - Queue_ADT
  - Array_C
  - Modulo_Arithmetic
  - Blocking_vs_Non-blocking
worksheet:
  - WS7
date_created: 2025-04-14
---
# Circular Queue

## Definition

A **Circular Queue** is a linear [[Data_Structure]] that implements the [[Queue_ADT]] (FIFO) using a fixed-size [[Array_C]] as if it were connected end-to-end, forming a circle or ring. It overcomes the inefficiency of linear array-based queues where dequeue operations would require shifting all subsequent elements.

## Key Aspects / Characteristics

- **Array-Based:** Uses a standard array for storage.
- **Fixed Size:** The maximum capacity is determined when the queue is created (size of the underlying array).
- **Wrap-Around Logic:** Uses indices (`front` and `rear`) to track the start and end of the queue within the array. When an index reaches the end of the array, it wraps around to the beginning (index 0). This wrap-around is typically achieved using the **modulo operator (`%`)**.
- **`front` and `rear` Indices:**
    - `front`: Index of the first element (or the slot *before* the first element, depending on implementation).
    - `rear`: Index of the last element (or the next available slot *after* the last element).
- **Empty/Full Conditions:** Determining if the queue is empty or full requires careful management of the `front` and `rear` indices. Common approaches:
    - Keep a separate `count` variable. Queue is full when `count == capacity`, empty when `count == 0`.
    - Leave one slot empty. Queue is full when `(rear + 1) % capacity == front`. Queue is empty when `rear == front`.
    - Use a flag to distinguish between empty and full when `rear == front`.
- **Efficiency:** Enqueue and Dequeue operations are typically **O(1)** because no element shifting is required.

## Visualization (Array of size 5)

**Initial:** `front=0`, `rear=0`, `count=0` (or `front=-1`, `rear=-1`)
`[ _, _, _, _, _ ]`

**Enqueue A, B, C:** `front=0`, `rear=3`, `count=3`
`[ A, B, C, _, _ ]`
   ^F        ^R

**Dequeue A:** `front=1`, `rear=3`, `count=2`
`[ _, B, C, _, _ ]`
      ^F     ^R

**Enqueue D, E:** `front=1`, `rear=0` (wraps around!), `count=4`
`[ E, B, C, D, _ ]`
   ^R ^F

**Enqueue F:** `front=1`, `rear=1`, `count=5` (Now Full if using count)
`[ E, F, C, D, _ ]`  <- WRONG if using count, should be:
`[ E, B, C, D, F ]`
   ^R ^F           <- Full if using one empty slot: `(rear+1)%5 == front` -> `(4+1)%5 = 0 != 1` (Not full yet)
   Let's use the "one empty slot" approach for clarity:
   Initial: `front=0`, `rear=0` -> Empty
   Enqueue A: `front=0`, `rear=1` -> `[A,_,_,_,_]`
   Enqueue B: `front=0`, `rear=2` -> `[A,B,_,_,_]`
   Enqueue C: `front=0`, `rear=3` -> `[A,B,C,_,_]`
   Enqueue D: `front=0`, `rear=4` -> `[A,B,C,D,_]` -> Full! `(4+1)%5 == 0`
   Dequeue A: `front=1`, `rear=4` -> `[_,B,C,D,_]`
   Enqueue E: `front=1`, `rear=0` -> `[E,B,C,D,_]` -> Full! `(0+1)%5 == 1`

```mermaid
graph TD
    subgraph Circular Queue (Capacity 5, One Slot Empty Strategy)
        Q0 --- Q1 --- Q2 --- Q3 --- Q4 --- Q0;
    end

    subgraph State 1 (Empty)
        Front1(front=0);
        Rear1(rear=0);
        Q0_1((Q0)); Q1_1((Q1)); Q2_1((Q2)); Q3_1((Q3)); Q4_1((Q4));
        style Front1 fill:#fff,stroke:#f00,stroke-width:2px;
        style Rear1 fill:#fff,stroke:#00f,stroke-width:2px;
    end
    subgraph State 2 (Enqueue A, B)
        Front2(front=0);
        Rear2(rear=2);
        Q0_2((Q0=A)); Q1_2((Q1=B)); Q2_2((Q2)); Q3_2((Q3)); Q4_2((Q4));
        style Front2 fill:#fff,stroke:#f00,stroke-width:2px;
        style Rear2 fill:#fff,stroke:#00f,stroke-width:2px;
    end
     subgraph State 3 (Dequeue A)
        Front3(front=1);
        Rear3(rear=2);
        Q0_3((Q0)); Q1_3((Q1=B)); Q2_3((Q2)); Q3_3((Q3)); Q4_3((Q4));
        style Front3 fill:#fff,stroke:#f00,stroke-width:2px;
        style Rear3 fill:#fff,stroke:#00f,stroke-width:2px;
    end
     subgraph State 4 (Enqueue C, D, E)
        Front4(front=1);
        Rear4(rear=0);
        Q0_4((Q0=E)); Q1_4((Q1=B)); Q2_4((Q2=C)); Q3_4((Q3=D)); Q4_4((Q4));
        style Front4 fill:#fff,stroke:#f00,stroke-width:2px;
        style Rear4 fill:#fff,stroke:#00f,stroke-width:2px;
        note right of Q0_4 : Queue is Full! (rear+1)%5 == front
    end
```

## Use Cases / Real-World Examples (WS7)

- **Keyboard Buffer:** Storing keystrokes temporarily.
- **I/O Buffering:** Buffering data for printers, disk drives, network cards.
- **CPU Scheduling:** Managing processes waiting for CPU time using algorithms like Round Robin.
- **Producer-Consumer Problem:** Often implemented using a circular buffer/queue to allow a producer thread to add data and a consumer thread to remove data concurrently (often requires synchronization). See [[Blocking_vs_Non-blocking]].

## Related Concepts
- [[Data_Structure]], [[Queue_ADT]] (Implements the Queue ADT)
- [[Array_C]] (Underlying storage)
- [[Circular_Buffer_DS]] (Very similar concept, often used interchangeably)
- Modulo Arithmetic (`%` operator for wrap-around)
- [[Blocking_vs_Non-blocking]] (Relevant for concurrent access)

---
**Source:** Worksheet WS7