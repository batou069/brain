---
tags:
  - 10_linux
  - concept
aliases:
  - OS Kernel
related:
  - "[[Operating_System]]"
  - "[[System_call]]"
  - "[[Process]]"
  - "[[50_Data_Structures/Memory_Management]]"
  - "[[CPU]]"
  - "[[User_space]]"
  - "[[Kernel_space]]"
  - "[[Device_driver]]"
worksheet: []
date_created: 2025-04-10
---
# Kernel

## Definition

The **Kernel** is the central component of an [[Operating_System]] (OS). It is the first program loaded on startup (after the [[Boot_loader]]) and manages the system's resources, acting as the bridge between applications ([[User_space]]) and the actual data processing done at the hardware level.

## Key Aspects / Characteristics

- **Core Functionality:** Manages [[CPU]] scheduling ([[Process]] management), [[50_Data_Structures/Memory_Management]], and [[I/O device]] operations.
- **Privileged Mode:** Runs in a protected memory space ([[Kernel_space]]) with full access to hardware. User applications run in [[User_space]] and interact with the kernel via [[System_call|system calls]].
- **Monolithic vs. Microkernel:** Kernels can be designed differently. Linux uses a monolithic kernel (though modular), meaning most OS services run in kernel space. Microkernels have minimal code in kernel space, with services running as user-space processes.
- **System Calls:** Provides an interface ([[API]]) for user-space programs to request services from the kernel (e.g., file operations, process creation).
- **Device Drivers:** Contains or loads modules ([[Device_driver]]) to interact with specific hardware components.

## Examples / Use Cases

- The Linux kernel is the foundation for distributions like Ubuntu, Debian, Fedora, Android.
- The Windows NT kernel is used in modern Windows versions.
- XNU is the kernel used in macOS and iOS.

## Related Concepts
- [[Operating_System]] (The kernel is *part* of the OS)
- [[System_call]] (The interface to the kernel)
- [[Process]] & [[Thread]] (Managed by the kernel)
- [[50_Data_Structures/Memory_Management]] (Handled by the kernel)
- [[User_space]] & [[Kernel_space]] (Execution modes/privilege levels)
- [[Boot_loader]] (Loads the kernel)
- [[Interrupt]] (Hardware signals handled by the kernel)

## Diagrams (Optional)

```puml
@startuml
cloud "User Space" {
  [Application A]
  [Application B]
  [Shell]
}
rectangle "Kernel Space" {
  rectangle "System Call Interface" as SCI
  rectangle "Process Management" as PM
  rectangle "Memory Management" as MM
  rectangle "File System" as FS
  rectangle "Device Drivers" as DD
  rectangle "Network Stack" as Net
}
package "Hardware" {
  [CPU]
  [RAM]
  [Disk]
  [Network Card]
}

Application -down-> SCI : [[System_call|System Call]]
Shell -down-> SCI : [[System_call|System Call]]
SCI -down-> PM
SCI -down-> MM
SCI -down-> FS
SCI -down-> Net
PM <--> CPU
MM <--> RAM
FS <--> Disk
DD <--> Disk
DD <--> Network Card
Net <--> Network Card
@enduml
```
## Questions / Further Study

> [!question] What is the difference between User Space and Kernel Space? (WS13)  
> [[Kernel_space]] is a privileged memory area where the [[Kernel]] runs with direct access to hardware. [[User_space]] is a restricted area where user applications run. Applications must use [[System_call|system calls]] to request the kernel perform privileged operations on their behalf. This separation protects the OS and hardware from faulty or malicious applications.

---

**Source:** Worksheet WS1, WS13