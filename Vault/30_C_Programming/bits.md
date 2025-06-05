---
tags: [c, concept, data_representation, hardware]
aliases: [bit]
related:
  - "[[bytes]]"
  - "[[Number_Systems]]"
  - "[[Data_Types_C]]"
  - "[[Bitwise_Operator_C]]"
date_created: 2025-04-12
---
# Bits

## Definition

A **bit** (short for **binary digit**) is the most basic unit of information in computing and digital communications. A bit can have only one of two values, commonly represented as **0** or **1**. These values typically correspond to electrical states (off/on), magnetic polarities, or other physical states in hardware.

## Key Aspects / Characteristics

- **Binary:** Represents two states (0 or 1).
- **Fundamental Unit:** All digital data (numbers, text, images, instructions) is ultimately stored and processed as sequences of bits.
- **Grouping:** Bits are commonly grouped into larger units, most notably [[bytes]] (typically 8 bits).
- **Representation:** Used to represent:
    - Logical values (0 for false, 1 for true).
    - Numbers using [[Number_Systems|binary representation]].
    - Characters via encoding schemes like [[ASCII]] or [[UTF-8]].
- **Manipulation:** [[Bitwise_Operator_C|Bitwise operators]] in C (`&`, `|`, `^`, `~`, `<<`, `>>`) allow direct manipulation of individual bits within integer types.

## Examples / Use Cases

- A single light switch: Off (0) or On (1).
- The binary number `1011` consists of 4 bits.
- An [[ASCII]] character like 'A' (decimal 65) is represented by the 7-bit sequence `1000001` (often stored in an 8-bit [[bytes|byte]] as `01000001`).

## Related Concepts
- [[bytes]] (A group of bits, usually 8)
- [[Number_Systems]] (Binary system uses bits)
- [[Data_Types_C]] (C data types like `int`, `char` occupy a specific number of bits/bytes)
- [[Bitwise_Operator_C]] (Operators that work directly on bits)

---
**Source:** Worksheet C_WS1