---
tags:
  - data_structures
  - concept
  - implementation
  - buffer
  - array
aliases:
  - Ring Buffer
  - Circular Queue (Buffer Context)
related:
  - Data_Structure
  - Circular_Queue_DS
  - Array_C
  - Modulo_Arithmetic
  - Producer_Consumer_Problem
  - IO_Buffering
worksheet:
  - WS7
date_created: 2025-04-14
---
# Circular Buffer

## Definition

A **Circular Buffer** (also known as a **Ring Buffer**) is a fixed-size buffer [[Data_Structure]] managed as if the memory were connected end-to-end in a circle. When the buffer is full and new data is written, it typically overwrites the oldest data in the buffer. Read and write pointers (or indices) track the positions for the next read and write operations, wrapping around the end of the buffer as needed.

## Key Aspects / Characteristics

- **Fixed Size:** Has a predetermined maximum capacity.
- **Array-Based:** Usually implemented using a contiguous array.
- **Wrap-Around:** Write and read indices wrap around from the end of the array to the beginning, typically using the modulo operator (`%`).
- **Overwrite on Full (Often):** A common behavior is that when the buffer is full, writing a new element overwrites the oldest element currently in the buffer. This makes it suitable for storing recent data streams (like logs or sensor readings). *Alternatively*, writes can be blocked or return an error when full, making it behave identically to a [[Circular_Queue_DS]].
- **Read/Write Pointers:** Uses separate indices/pointers to track the next position to write to and the next position to read from.
- **Use Cases:** Primarily used for buffering data streams between producers and consumers, especially when the producer and consumer operate at different or variable rates.

## Circular Buffer vs. Circular Queue

The terms are often used interchangeably, but a subtle distinction sometimes exists:
- **[[Circular_Queue_DS]]:** Primarily implements the [[Queue_ADT]] (FIFO). When full, `enqueue` operations typically fail or block, rather than overwriting data. The focus is on preserving the FIFO order of elements currently in the queue.
- **Circular Buffer:** Often implies that when full, new writes **overwrite** the oldest data. The focus is often on maintaining a buffer of the *most recent* data or acting as a fixed-size communication channel.

*However, in many contexts, a circular buffer is simply used as an efficient fixed-size implementation of a queue where overwriting is disallowed.*

## Visualization (Capacity 5, Overwriting Behavior)

**Initial:** `read=0`, `write=0`, `count=0`
`[ _, _, _, _, _ ]`
   ^R ^W

**Write A, B, C:** `read=0`, `write=3`, `count=3`
`[ A, B, C, _, _ ]`
   ^R     ^W

**Read A:** `read=1`, `write=3`, `count=2`
`[ _, B, C, _, _ ]`
      ^R  ^W

**Write D, E:** `read=1`, `write=0` (wraps!), `count=4`
`[ E, B, C, D, _ ]`
   ^W ^R

**Write F:** `read=1`, `write=1`, `count=5` (Full)
`[ E, F, C, D, _ ]`
      ^W
      ^R

**Write G (Overwrite):** `read=2` (read ptr advances!), `write=2`, `count=5` (Still Full)
`[ E, F, G, D, _ ]`
         ^W
         ^R  *(Overwrote B)*

## Use Cases / Real-World Examples (WS7)

- **I/O Buffering:** Buffering data for audio/video streaming, serial communication, keyboard input.
- **Data Streaming:** Storing the latest `N` samples from a sensor or data feed.
- **Logging:** Keeping a buffer of the most recent log messages.
- **Producer-Consumer Problem:** Efficient fixed-size buffer between threads or processes.

## Related Concepts
- [[Data_Structure]], [[Array_C]]
- [[Circular_Queue_DS]] (Similar implementation, often different full behavior)
- Modulo Arithmetic
- [[Producer_Consumer_Problem]] (*Implied*)
- Buffering

---
**Source:** Worksheet WS7