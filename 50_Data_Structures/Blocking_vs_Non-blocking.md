---
tags:
  - data_structures
  - algorithms
  - concurrency
  - concept
  - io
  - synchronization
aliases:
  - Blocking Operations
  - Non-blocking Operations
  - Synchronous vs Asynchronous (Related Context)
related:
  - "[[Concurrency]]"
  - "[[Multithreading]]"
  - "[[Synchronization]]"
  - "[[Queue_ADT]]"
  - "[[Circular_Queue_DS]]"
  - "[[IO_Operations]]" # Placeholder
  - "[[Sockets]]"
  - "[[Producer_Consumer_Problem]]"
worksheet: [WS7]
date_created: 2025-04-21
---
# Blocking vs. Non-blocking Operations

## Definition

**Blocking** and **Non-blocking** refer to how an operation (like reading/writing data, acquiring a lock, or accessing a shared resource) behaves when it cannot be completed immediately.

1.  **Blocking Operation:** If the operation cannot be completed immediately (e.g., data is not available to read, a buffer is full for writing, a lock is held by another thread), a blocking call will **suspend the execution** of the calling thread or process until the operation *can* be completed. The thread yields control and waits.

2.  **Non-blocking Operation:** If the operation cannot be completed immediately, a non-blocking call will **return immediately** without waiting, typically indicating (e.g., via a return code, exception, or special value like 0 bytes read) that the operation could not be completed at that moment. The calling thread can then choose to do other work, retry the operation later, or use a mechanism like polling or event notification (`select`, `poll`, `epoll`, async/await) to wait efficiently.

## Contexts

This distinction is crucial in several areas:

- **I/O Operations:**
    - *Blocking I/O (Default):* `read()` might block until data arrives, `write()` might block until data is accepted by the OS buffer, `accept()` might block until a connection arrives. Simple to program but can limit concurrency.
    - *Non-blocking I/O:* Calls return immediately (e.g., with `EAGAIN` or `EWOULDBLOCK` error code if data isn't ready). Requires more complex application logic (event loops, polling) but allows a single thread to handle multiple I/O channels concurrently (I/O multiplexing).
- **[[Synchronization]] Primitives:**
    - *Blocking Mutex/Semaphore:* `lock()` or `wait()` will block the thread until the lock is acquired or the semaphore is signaled.
    - *Non-blocking/Try:* `try_lock()` or `try_wait()` attempts to acquire the resource but returns immediately (e.g., with `false`) if it cannot, allowing the thread to do something else.
- **[[Data_Structure|Data Structure]] Operations (e.g., Queues):**
    - *Blocking Queue:* If `dequeue` is called on an empty queue, the thread blocks until an item is available. If `enqueue` is called on a full queue, the thread blocks until space is available. Used commonly in [[Producer_Consumer_Problem|producer-consumer scenarios]].
    - *Non-blocking Queue:* `dequeue` returns a special value (e.g., `NULL`, `false`) if empty. `enqueue` returns a special value if full. The caller must handle these conditions.

## Trade-offs

| Feature        | Blocking                                  | Non-blocking                              |
| :------------- | :---------------------------------------- | :---------------------------------------- |
| **Simplicity** | Easier to program (looks sequential)      | More complex application logic required   |
| **Efficiency** | Can waste resources if blocked often      | Potentially more efficient use of threads |
| **Concurrency**| Limited concurrency per thread            | Enables high concurrency (I/O multiplexing)|
| **Responsiveness**| Can lead to unresponsive systems if blocked | Generally leads to more responsive systems|
| **Resource Use**| Each blocked thread consumes resources   | Fewer threads can handle more work        |

## Related Concepts
- [[Concurrency]], [[Multithreading]]
- [[Synchronization]] (Mutexes, Semaphores)
- [[IO_Operations]], [[Sockets]]
- [[Queue_ADT]], [[Circular_Queue_DS]] (Blocking/Non-blocking variants)
- Event Loops, Polling, `select`, `epoll`, Asynchronous Programming

---
**Source:** Worksheet WS7