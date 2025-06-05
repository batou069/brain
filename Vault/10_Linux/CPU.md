---
tags: [linux, hardware, concept]
aliases: [Central Processing Unit, Processor]
related:
  - "[[[CPU_cache]]]]"
  - "[[[[RAM]]]]"
  - "[[[[Bus]]]]"
  - "[[[[Von_Neumann_architecture]]]]"
  - "[[[[Kernel]]]]"
  - "[[[[Process]]]]"
  - "[[[[Context_switch]]]"
worksheet: [WS1, WS13]
date_created: 2025-04-21
---
# CPU

## Definition

The **Central Processing Unit (CPU)**, also called a processor, is the primary component of a computer that executes instructions comprising a computer program. It performs most of the basic arithmetic, logic, controlling, and input/output (I/O) operations specified by the instructions.

## Key Aspects / Characteristics

- **Execution Core:** Contains the Arithmetic Logic Unit (ALU) for calculations and the Control Unit (CU) for managing instruction execution.
- **Clock Speed:** Measured in Hertz (Hz), indicates how many cycles the CPU can perform per second.
- **Cores:** Modern CPUs often have multiple cores, allowing for [[Parallelism]].
- **Cache:** Small, fast memory located on or near the CPU chip ([[CPU_cache]]) to speed up access to frequently used data.
- **Instruction Set Architecture (ISA):** Defines the set of instructions the CPU can understand and execute (e.g., x86, ARM).
- **Interaction with Memory:** Fetches instructions and data from [[RAM]] via the system [[Bus]].

## Examples / Use Cases

- Executing operating system tasks ([[Kernel]], [[System_call]]).
- Running user applications ([[Program]], [[Process]]).
- Performing calculations in spreadsheets, simulations, etc.
- Rendering graphics (though often assisted by a GPU).

## Related Concepts
- [[CPU_cache]]
- [[RAM]]
- [[Bus]]
- [[Von_Neumann_architecture]]
- [[MMU]] (Memory Management Unit, often part of the CPU)
- [[Round-Robin]] (CPU scheduling algorithm)
- [[Hyper_Threading]]
- [[SIMD]]

## Diagrams (Optional)

```puml
@startuml
rectangle CPU {
  rectangle "Control Unit (CU)" as CU
  rectangle "Arithmetic Logic Unit (ALU)" as ALU
  rectangle "Registers" as Regs
  rectangle "[[CPU_cache|Cache]]" as Cache
}

CPU <--> [[Bus]] : Data/Address/Control
[[Bus]] <--> [[RAM]]
CU -> ALU : Directs Operations
CU -> Regs : Manages Data Flow
CU -> Cache : Manages Cache Access
ALU <--> Regs : Performs Operations
Cache <--> Regs : Speeds up Access
@enduml
```
## Questions / Further Study

> [!question] How does the CPU interact with the OS?  
> The [[Operating_System]]'s [[Kernel]] schedules [[Process|processes]] to run on the CPU, manages [[Context_switch|context switches]], and handles [[Interrupt|interrupts]] and [[System_call|system calls]] that require CPU execution in [[Kernel_space|kernel mode]].

---

**Source:** Worksheet WS1, WS13