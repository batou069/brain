---
tags:
  - 10_linux
  - concept
  - hardware
aliases:
  - System Bus
  - Address Bus
  - Data Bus
  - Control Bus
related:
  - "[[CPU]]"
  - "[[RAM]]"
  - "[[I/O device]]"
  - "[[Motherboard]]"
  - "[[Von_Neumann_architecture]]"
worksheet:
  - WS<% tp.file.cursor(1) %>
date_created: 2025-04-10
---
# Bus (Computer)

## Definition

In computer architecture, a **Bus** is a communication system that transfers data between components inside a computer, or between computers. It consists of a set of physical connections (wires, optical fibers, etc.) which can be shared by multiple hardware components to communicate with one another.

## Key Aspects / Characteristics

Buses are often categorized by their function:

-   **Data Bus:** Transfers the actual data between components (e.g., between [[CPU]] and [[RAM]]). The width of the data bus (number of wires) determines how much data can be transferred simultaneously (e.g., 32-bit, 64-bit).
-   **Address Bus:** Specifies the source or destination location for the data being transferred (e.g., a specific memory address in [[RAM]] or an [[I/O device]] port). The width of the address bus determines the maximum amount of memory the system can address.
-   **Control Bus:** Carries control signals and commands from the [[CPU]] to manage and coordinate the activities of other components. Signals include things like read/write commands, interrupt requests, clock signals, and bus requests/grants.

- **System Bus:** Often refers collectively to the data, address, and control buses connecting the main components like CPU, RAM, and I/O controllers on the motherboard.
- **Speed/Bandwidth:** Measured in terms of clock speed (MHz/GHz) and data transfer rate (MB/s or GB/s).

## Examples / Use Cases

- Connecting the [[CPU]] to [[RAM]].
- Connecting the CPU to peripheral controllers (like [[USB]], [[SATA]]).
- Expansion slots (like PCIe) connect peripheral cards to the system bus.

## Related Concepts
- [[CPU]] (Uses the bus to fetch instructions/data)
- [[RAM]] (Connected to the CPU via the bus)
- [[I/O device]] (Communicate via buses)
- [[Motherboard]] (Contains the physical buses)
- [[Von_Neumann_architecture]] (Relies on buses for communication between CPU and memory)

## Diagrams (Optional)

```puml
@startuml
rectangle CPU
rectangle RAM
rectangle "I/O Controller" as IO

CPU <-down-> Bus : Address/Data/Control
RAM <-up-> Bus : Address/Data/Control
IO <-up-> Bus : Address/Data/Control

rectangle Bus [
  .. Address Bus ..
  .. Data Bus ..
  .. Control Bus ..
]

note right of Bus : System Bus connecting components
@enduml
```
---
**Source:** Worksheet WS1