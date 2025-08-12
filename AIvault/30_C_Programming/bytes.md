---
tags:
  - c
  - concept
  - data_representation
  - hardware
  - memory
aliases:
  - byte
related:
  - "[[bits]]"
  - "[[Data_Types_C]]"
  - "[[50_Data_Structures/Memory_Management]]"
  - "[[sizeof_operator_C]]"
  - "[[Number_Systems]]"
  - "[[ASCII]]"
  - "[[UTF-8]]"
worksheet:
  - C_WS1
date_created: 2025-04-12
---
# Bytes

## Definition

A **byte** is a unit of digital information that most commonly consists of 8 [[bits]]. Historically, the size of a byte has been hardware-dependent, but the 8-bit byte is now nearly universal and codified in standards like C's `CHAR_BIT` macro (usually defined as 8). Bytes are the smallest addressable unit of memory in many computer architectures.

## Key Aspects / Characteristics

- **Group of Bits:** Typically 8 bits.
- **Addressable Unit:** Memory is often organized and accessed in byte-sized chunks. The address of a variable usually refers to the address of its first byte.
- **Data Representation:** Used to store:
    - Single characters in encodings like [[ASCII]] or the basic multilingual plane of [[UTF-8]].
    - Parts of larger data types (e.g., an `int` might be 4 bytes).
    - Binary data (e.g., image pixels, machine code instructions).
- **Range:** An 8-bit byte can represent 2<sup>8</sup> = 256 different values (e.g., 0 to 255 for unsigned, or -128 to 127 for signed two's complement).
- **`sizeof` Operator:** The [[sizeof_operator_C]] in C returns the size of a data type or variable in *bytes*.

## Examples / Use Cases

- The C `char` data type is typically one byte in size (`sizeof(char)` is guaranteed to be 1).
- A 32-bit integer (`int` on many systems) occupies 4 bytes.
- Memory addresses often increment byte by byte.
- File sizes are measured in bytes (or kilobytes, megabytes, gigabytes, etc.).

## Related Concepts
- [[bits]] (A byte is composed of bits)
- [[Data_Types_C]] (Sizes are measured in bytes)
- [[50_Data_Structures/Memory_Management]], Memory Addresses (Memory is often byte-addressable)
- [[sizeof_operator_C]] (Measures size in bytes)
- [[Number_Systems]] (Bytes can represent numbers in binary/hex)
- [[ASCII]], [[UTF-8]] (Character encodings using bytes)
- [[Word_C]] (A larger unit, often multiple bytes, natural processing size for CPU)

---
**Source:** Worksheet C_WS1