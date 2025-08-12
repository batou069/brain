---
tags:
  - 10_linux
  - concept
  - linux
  - core
aliases:
  - OS
related:
  - "[[Kernel]]"
  - "[[Process]]"
  - "[[50_Data_Structures/Memory_Management]]"
  - "[[File_System]]"
  - "[[User_space]]"
  - "[[Kernel_space]]"
worksheet:
  - WS1
date_created: 2025-04-10
---
# Operating System

## Definition

An **Operating System (OS)** is system software that manages computer hardware, software resources, and provides common services for computer programs. It acts as an intermediary between the user and the computer hardware.

## Key Aspects / Characteristics

- **Resource Management:** Manages [[CPU]] time, [[RAM]], [[Hard_disk]] space, and [[I/O device|I/O devices]].
- **Process Management:** Handles the creation, scheduling, and termination of [[Process|processes]].
- **Memory Management:** Allocates and deallocates memory space for programs ([[Virtual_memory]], [[Memory_paging]]).
- **File System Management:** Organizes files and directories on storage devices ([[File_System]], [[inode]]).
- **Security:** Provides mechanisms for user authentication and access control.
- **User Interface:** Offers a way for users to interact with the system (e.g., [[Shell]], Graphical User Interface).
- **Device Drivers:** Manages communication with hardware devices.

## Examples / Use Cases

- **Desktop OS:** Windows, macOS, [[Linux]] distributions (like Ubuntu, Fedora).
- **Server OS:** Linux distributions (like CentOS, Debian), Windows Server.
- **Mobile OS:** Android, iOS.
- **Embedded OS:** Real-time operating systems (RTOS) used in specific devices.

## Related Concepts
- [[Kernel]] (The core component of most OSes)
- [[Von_Neumann_architecture]]
- [[History_of_Unix]]
- [[Linux]] (A specific family of OS kernels/systems)

## Diagrams (Optional)

```d2
direction: right
User -> Application -> OS -> Hardware: Interacts
OS <-> Hardware: Manages
OS <-> Application: Provides Services
```

## Questions / Further Study

> [!question] What is the difference between the OS and the Kernel?  
> The [[Kernel]] is the central part of the OS that manages the most critical operations (CPU, memory, devices). The OS includes the kernel plus other system software like shells, utilities, and libraries.

---

**Source:** Worksheet WS1