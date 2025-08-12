---
tags:
  - c
  - concept
  - hardware
  - architecture
  - data_representation
aliases:
  - Computer Word
  - Machine Word
related:
  - "[[CPU]]"
  - "[[Data_Types_C]]"
  - "[[bits]]"
  - "[[bytes]]"
  - "[[Register_C]]"
  - "[[50_Data_Structures/Memory_Management]]"
worksheet:
  - C_WS4
date_created: 2025-04-12
---
# Word (Computer Architecture)

## Definition

In computer architecture, a **Word** is the natural unit of data used by a particular processor design. It represents the amount of data (number of [[bits]] or [[bytes]]) that a [[CPU]] can process or transfer between memory and registers in a single operation. The size of a word is a fundamental characteristic of a computer's architecture (e.g., 16-bit, 32-bit, 64-bit architectures).

## Key Aspects / Characteristics

- **Natural Unit of Processing:** The size (in bits) that the CPU's internal registers, Arithmetic Logic Unit (ALU), and data buses are primarily designed to handle efficiently.
- **Architecture Dependent:** The word size varies between different CPU architectures. Common sizes include:
    - 8-bit (early microprocessors)
    - 16-bit (e.g., Intel 8086, 80286)
    - 32-bit (e.g., Intel 80386, 80486, Pentium, ARMv7)
    - 64-bit (e.g., x86-64/AMD64, ARMv8/AArch64, modern desktops/servers)
- **Impact on Data Types:** The size of fundamental C [[Data_Types_C]] like `int`, `long`, and pointers is often related to the machine's word size (though not strictly guaranteed by the C standard, e.g., `int` is often word-sized, pointers usually match the address bus width which is often word-sized).
- **Memory Addressing:** The word size often influences the range of memory addresses the CPU can naturally handle (e.g., a 32-bit architecture typically supports a 32-bit address space).
- **Performance:** Operations on data units matching the word size are generally faster than operations on smaller or larger units that might require multiple steps.

## Examples / Use Cases

- On a 32-bit CPU, a word is typically 32 bits (4 bytes). An `int` might also be 32 bits. The CPU can add two 32-bit numbers in a single instruction.
- On a 64-bit CPU, a word is typically 64 bits (8 bytes). `long int` and pointers are often 64 bits. The CPU can process 64 bits of data at once.

## Related Concepts
- [[CPU]] (The processor defines the word size)
- [[bits]], [[bytes]] (Word size is measured in bits/bytes)
- [[Data_Types_C]] (Sizes like `int`, `long`, pointers are often related to word size)
- [[Register_C]] (CPU registers are typically word-sized - *to be created*)
- [[Bus]] (Data bus width is often related to word size)
- [[50_Data_Structures/Memory_Management]] (Address space size is related to word/pointer size)

## Questions / Further Study
>[!question] What is a 'word'? What does it represent? (WS4)
> A 'word' is the natural unit of data handled by a specific CPU architecture. It represents the number of bits (e.g., 32 or 64) that the processor is optimized to process or transfer in a single operation. It influences the size of registers, the width of data buses, and often the default size of integer types and pointers.

---
**Source:** Worksheet C_WS4