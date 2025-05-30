---
tags:
  - linux
  - hardware
  - concept
  - os
aliases:
  - Input/Output Device
  - Peripheral Device
related:
  - "[[Operating_System]]"
  - "[[Kernel]]"
  - "[[Device_driver]]"
  - "[[Bus]]"
  - "[[Interrupt]]"
  - "[[DMA]]"
  - "[[Block_device]]"
  - "[[Character_device]]"
  - "[[CPU]]"
  - "[[RAM]]"
worksheet:
  - WS1
date_created: 2025-04-20
---
# I/O Device (Input/Output Device)

## Definition

An **I/O (Input/Output) Device**, also known as a peripheral device, is any piece of computer hardware equipment used to provide data and control signals *to* an information processing system (such as a computer) or to receive results *from* it. Input devices bring data *in*, while output devices send data *out*. Some devices perform both input and output.

## Key Aspects / Characteristics

- **Communication Bridge:** Connects the computer's core ([[CPU]], [[RAM]]) to the external world or other subsystems.
- **Input vs. Output:**
    - **Input Devices:** Keyboard, mouse, scanner, microphone, webcam, sensors.
    - **Output Devices:** Monitor, printer, speakers, projector, actuators.
    - **Input/Output Devices:** [[Hard_disk|Hard disk drive (HDD)]], [[SSD|Solid-state drive (SSD)]], Network interface card (NIC), Touchscreen, USB drives, Modems.
- **Interaction with OS/CPU:**
    - Managed by the [[Operating_System]]'s [[Kernel]] through [[Device_driver|device drivers]].
    - Communicate with the CPU and memory via the system [[Bus]].
    - Often use [[Interrupt|interrupts]] to signal the CPU when they need attention (e.g., data ready, operation complete).
    - May use [[DMA|Direct Memory Access (DMA)]] to transfer data directly to/from [[RAM]] without continuous CPU involvement.
- **Device Drivers:** Specialized software that understands how to communicate with a specific hardware device and provides a standardized interface for the OS kernel.
- **Device Files (Linux):** In Linux/Unix, I/O devices are often represented as special files in the `/dev` directory, categorized as:
    - [[Block_device|Block Devices]]: Transfer data in fixed-size blocks (e.g., disks `/dev/sda`). Buffered.
    - [[Character_device|Character Devices]]: Transfer data character-by-character (or byte-by-byte) (e.g., terminals `/dev/tty1`, serial ports `/dev/ttyS0`). Often unbuffered.

## Related Concepts
- [[Operating_System]], [[Kernel]] (Manages devices)
- [[Device_driver]] (Software interface)
- [[Bus]] (Communication pathway)
- [[Interrupt]], [[DMA]] (Communication mechanisms)
- [[Block_device]], [[Character_device]] (Linux device types)
- [[CPU]], [[RAM]] (Core components interacting with I/O)
- Peripherals

---
**Source:** Worksheet WS1