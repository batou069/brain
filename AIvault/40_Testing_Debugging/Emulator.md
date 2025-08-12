---
tags:
  - testing
  - concept
  - tool
  - environment
  - hardware
aliases: []
related:
  - Simulator
  - Software_Testing
  - Hardware_Dependency
  - Mobile_Testing
  - Embedded_Systems
worksheet:
  - WS_Testing
date_created: 2025-04-14
---
# Emulator

## Definition

An **Emulator** is hardware or software that enables one computer system (the *host*) to behave like another computer system (the *guest*). It duplicates the functions and, crucially, mimics the **internal hardware behavior** of the guest system, allowing software or peripherals designed for the guest system to run on the host system.

## Key Aspects / Characteristics

- **Mimics Hardware:** Replicates the low-level hardware behavior, instruction set, memory management, and I/O of the target system.
- **Runs Guest Software:** Allows running the guest system's operating system and applications unmodified on the host system.
- **Accuracy vs. Speed:** Often prioritizes accuracy in replicating the hardware, which can sometimes make emulation slower than the original hardware or simulation.
- **Purpose in Testing:**
    - Testing software designed for specific hardware (e.g., mobile devices, game consoles, embedded systems) when the physical hardware is unavailable, expensive, or impractical to use for large-scale testing.
    - Debugging interactions between software and specific hardware behaviors.
    - Testing different hardware configurations virtually.

## Examples / Use Cases

- **Android Emulator:** Allows developers to run and test Android applications on a desktop computer (Windows, macOS, Linux) by emulating the ARM architecture and Android OS environment.
- **Game Console Emulators:** (e.g., MAME, Dolphin) Emulate the hardware of older arcade machines or consoles to allow playing their games on modern PCs.
- **Hardware Emulators:** Used in embedded systems development to test firmware before the actual hardware is ready.

## Emulator vs. Simulator

- **[[Emulator]]:** Mimics the *internal hardware behavior* of the target system. Aims to be a substitute for the hardware. Runs the actual guest software.
- **[[Simulator]]:** Models the *external behavior or interface* of the target system or component, without necessarily replicating its internal workings accurately. Often used for high-level modeling or testing interactions with an abstracted version of a system. May not run the actual guest software.

## Related Concepts
- [[Simulator]] (Contrasting concept)
- [[Software_Testing]] (Emulators provide test environments)
- [[Hardware_Dependency]]
- [[Virtualization]] (Related concept, but virtualization typically runs guest OS on host hardware directly when compatible, while emulation translates/mimics potentially different hardware).

---
**Source:** Worksheet WS_Testing