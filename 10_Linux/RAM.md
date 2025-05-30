---
tags:
  - 10_linux
  - concept
  - hardware
  - memory
aliases:
  - Random Access Memory
  - Main Memory
related:
  - "[[CPU]]"
  - "[[CPU_cache]]"
  - "[[Bus]]"
  - "[[50_Data_Structures/Memory_Management]]"
  - "[[Virtual_memory]]"
  - "[[Operating_System]]"
  - "[[Kernel]]"
  - "[[Process]]"
worksheet:
  - WS<% tp.file.cursor(1) %>
date_created: 2025-04-10
---
# RAM (Random Access Memory)

## Definition

**Random Access Memory (RAM)** is a form of computer memory that can be read and changed in any order, typically used to store working data and machine code currently in use. It is a volatile memory, meaning its contents are lost when the power is turned off. RAM allows the [[CPU]] to access data much faster than reading from persistent storage like a [[Hard_disk]] or [[SSD]].

## Key Aspects / Characteristics

- **Volatility:** Data is lost when power is removed.
- **Random Access:** Any memory location can be accessed directly and quickly (in contrast to sequential access devices).
- **Speed:** Significantly faster than secondary storage (HDDs, SSDs) but slower than [[CPU_cache]].
- **Working Area:** Used by the [[Operating_System]] and applications to store code and data that are actively being used or processed.
- **Physical Component:** Typically comes in modules (DIMMs) installed on the computer's motherboard.

## Examples / Use Cases

- Holding the [[Operating_System]] [[Kernel]] code after boot.
- Storing [[Program]] instructions loaded for execution by the [[CPU]].
- Holding data being actively manipulated by running [[Process|processes]].
- Caching data read from slower storage devices.

## Related Concepts
- [[CPU]] (Reads from and writes to RAM)
- [[CPU_cache]] (Faster memory closer to the CPU, often holding copies of RAM data)
- [[Bus]] (Connects the CPU to RAM)
- [[50_Data_Structures/Memory_Management]] (OS function to allocate and manage RAM for processes)
- [[Virtual_memory]] (Technique using disk space to extend available RAM)
- [[Hard_disk]] / [[SSD]] (Slower, persistent storage)
- [[ROM]] (Read-Only Memory, non-volatile)

## Questions / Further Study
>[!question] Why is RAM necessary if we have hard disks?
> [[Hard_disk|Hard disks]] and [[SSD|SSDs]] are too slow for the [[CPU]] to access directly for every instruction and piece of data it needs. [[RAM]] provides a much faster intermediate storage area for actively used information, preventing the CPU from constantly waiting for data from the slower persistent storage.

---
**Source:** Worksheet WS1
