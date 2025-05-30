---
tags:
  - linux
  - hardware
  - concept
  - cpu
  - memory
aliases:
  - CPU Cache
  - Cache Memory
related:
  - "[[CPU]]"
  - "[[RAM]]"
  - "[[Memory_Hierarchy]]"
  - "[[Bus]]"
  - "[[Performance]]"
worksheet:
  - WS1
date_created: 2025-04-20
---
# CPU Cache

## Definition

**CPU Cache** is a small, extremely fast type of volatile computer memory ([[RAM]]) integrated directly into or located very close to the [[CPU]] core. It stores copies of frequently used data and instructions from the main [[RAM]] to reduce the average time the CPU has to wait for data, thereby improving overall system [[Performance]].

## Key Aspects / Characteristics

- **Speed:** Much faster access times compared to main RAM (orders of magnitude faster).
- **Size:** Significantly smaller capacity than main RAM due to cost and physical constraints.
- **Proximity:** Located physically close to the CPU core(s).
- **Memory Hierarchy:** Forms intermediate levels in the [[Memory_Hierarchy]] between CPU registers (fastest, smallest) and main RAM (slower, larger).
- **Levels (L1, L2, L3):** Modern CPUs typically have multiple levels of cache:
    - **L1 Cache:** Smallest, fastest, usually split into instruction cache (L1i) and data cache (L1d), private to each CPU core.
    - **L2 Cache:** Larger and slightly slower than L1, often private to each core.
    - **L3 Cache:** Largest and slowest cache level, typically shared among multiple CPU cores. Acts as a final cache before accessing main RAM.
- **Cache Hits & Misses:**
    - *Hit:* When the CPU requests data and finds it in the cache. (Fast)
    - *Miss:* When the requested data is not in the cache, requiring fetching it from a slower level (e.g., next cache level or main RAM). (Slow)
- **Cache Coherence:** In multi-core systems, mechanisms are needed to ensure that all cores have a consistent view of data shared across their private caches.
- **Transparency:** Cache operation is generally transparent to the programmer and operating system, managed automatically by hardware controllers.

## Visualization (Memory Hierarchy)

```mermaid
graph TD
    CPU_Reg[CPU Registers] --> L1[L1 Cache];
    L1 --> L2[L2 Cache];
    L2 --> L3[L3 Cache];
    L3 --> RAM[Main RAM];
    RAM --> Storage[Disk/SSD Storage];

    subgraph CPU Chip
        CPU_Reg; L1; L2; L3;
    end

    style CPU_Reg fill:#f9f
    style L1 fill:#ccf
    style L2 fill:#ccf
    style L3 fill:#ccf
    style RAM fill:#9cf
    style Storage fill:#ccc

    linkStyle 0 stroke-width:2px,stroke:red; linkStyle 4 stroke-width:1px,stroke:gray;
    linkStyle 1 stroke-width:2px,stroke:orange;
    linkStyle 2 stroke-width:2px,stroke:green;
    linkStyle 3 stroke-width:2px,stroke:blue;

    note right of L1 : Fastest, Smallest
    note right of RAM : Slower, Larger
```

## Related Concepts
- [[CPU]]
- [[RAM]]
- [[Memory_Hierarchy]]
- [[Bus]] (Connects CPU, Cache, RAM)
- [[Performance]] (Cache hits significantly improve performance)
- Cache Algorithms (LRU, LFU - *Implied*)
- Cache Coherence Protocols (MESI - *Implied*)

---
**Source:** Worksheet WS1