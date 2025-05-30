---
tags:
  - linux
  - concept
  - os
  - kernel
  - interface
  - api
  - process
aliases:
  - System Call
  - syscall
related:
  - "[[Operating_System]]"
  - "[[Kernel]]"
  - "[[User_space]]"
  - "[[Kernel_space]]"
  - "[[API_C]]"
  - "[[Process]]"
  - "[[Interrupt]]"
  - "[[glibc]]"
  - "[[POSIX]]"
  - "[[open_syscall_C]]"
  - "[[read_syscall_C]]"
  - "[[write_syscall_C]]"
  - "[[fork_syscall_C]]"
  - "[[exec_syscall_C]]"
worksheet:
  - WS1
  - WS13
  - WS14
date_created: 2025-04-20
---
# System Call

## Definition

A **System Call** (often abbreviated as **syscall**) is the programmatic way in which a computer program requests a service from the [[Kernel]] of the [[Operating_System]] it is executed on. It acts as the fundamental interface between a [[Process]] running in [[User_space]] and the protected [[Kernel_space]]. Operations that require privileged access to hardware or kernel data structures (like file I/O, process creation, network communication, memory allocation) must be performed via system calls.

## Purpose

- **Provide OS Services:** Allow user programs to access services managed by the kernel (file system, process management, networking, device access, etc.).
- **Protection:** Act as a controlled gateway between unprivileged user space and privileged kernel space, ensuring user programs cannot directly access hardware or interfere with the kernel or other processes improperly.
- **Abstraction:** Provide a standardized API (often defined by [[POSIX]]) that hides the complexities of the underlying hardware and kernel implementation details from the application programmer.

## How it Works (Conceptual)

1.  **User Program Request:** A user program needs a kernel service (e.g., read from a file). It typically calls a **wrapper function** provided by a standard library (like [[glibc]] on Linux, e.g., `read()`).
2.  **Library Wrapper:** The library function (`read()`) prepares the arguments for the system call and places a unique **system call number** (identifying the requested kernel service) into a specific [[CPU]] register (e.g., `eax` on x86).
3.  **Trap/Interrupt:** The library function executes a special CPU instruction (e.g., `syscall`, `sysenter`, `int 0x80` on older x86) that causes a software [[Interrupt]] or **trap**. This instruction switches the CPU from user mode to kernel mode and transfers control to a predefined kernel entry point (the system call handler).
4.  **Kernel Execution:** The kernel's system call handler uses the system call number to look up and execute the appropriate kernel function (e.g., the kernel's internal file reading routine). The kernel performs the requested operation, accessing hardware or kernel data structures as needed.
5.  **Return to User Space:** Once the kernel function completes, the kernel places the result (e.g., number of bytes read, error code) into a CPU register, switches the CPU back to user mode, and returns control to the library wrapper function immediately following the trap instruction.
6.  **Library Wrapper Return:** The library wrapper function takes the result from the CPU register, potentially sets `errno` if an error occurred, and returns the result to the original user program caller.

## Examples of Common System Calls (POSIX/Linux)

- File Management: `open`, `close`, `read`, `write`, `lseek`, `stat`, `unlink`, `mkdir`
- Process Management: `fork`, `execve` (and variants like `execl`, `execv`), `exit`, `wait`, `waitpid`, `kill`, `getpid`, `getppid`
- Memory Management: `brk`, `sbrk`, `mmap`, `munmap`
- Communication: `pipe`, `socket`, `bind`, `listen`, `accept`, `connect`, `send`, `recv`
- Device Management: `ioctl`

## Related Concepts
- [[Operating_System]], [[Kernel]] (Provides the services)
- [[User_space]], [[Kernel_space]] (Protection domains bridged by syscalls)
- [[API_C]], [[glibc]] (User-space libraries provide wrappers)
- [[Process]] (Entity making system calls)
- [[Interrupt]], Trap (Mechanism for switching to kernel mode)
- System Call Number (Identifies the requested service)
- [[POSIX]] (Standardizes many system call interfaces)

## Questions / Further Study
>[!question] What is a system call? (WS14)
> A system call is the mechanism used by a user-space program to request a service from the operating system kernel. It involves a special instruction that traps into the kernel, switching CPU privilege levels, allowing the kernel to perform protected operations (like I/O or process creation) on behalf of the user program.

>[!question] Can a process cause an interrupt? (WS14)
> Not directly in the hardware sense. Hardware interrupts are typically triggered by external devices (keyboard, timer, network card). However, a process *initiates* a **software interrupt** or **trap** when it executes a system call instruction (like `syscall` or `int 0x80`). This trap causes the CPU to switch to kernel mode and handle the request, similar to how it handles hardware interrupts. Processes can also cause *exceptions* (like division by zero, page fault) which are handled similarly by the kernel.

>[!question] Can a process handle an interrupt? (WS14)
> No, not directly. Hardware interrupts and system call traps cause the CPU to switch to **kernel mode**, and control is transferred to predefined handlers *within the OS kernel*. The kernel handles the interrupt (e.g., reads data from the device, services the system call) and then resumes the interrupted process (or switches to another process). User-space processes cannot directly intercept or handle these low-level hardware or software interrupts. They interact with the results via mechanisms like [[Signal|signals]] or the return values of system calls.

---
**Source:** Worksheet WS1, WS13, WS14