---
tags:
  - linux
  - concept
  - software
  - license
  - project
aliases:
  - GNU's Not Unix
related:
  - "[[Linux]]"
  - "[[Operating_System]]"
  - "[[POSIX]]"
  - "[[Free_Software]]"
  - "[[Open_Source]]"
  - "[[Bash]]"
  - "[[GCC]]"
  - "[[glibc]]"
worksheet:
  - WS1
date_created: 2025-04-11
---
# GNU (GNU's Not Unix)

## Definition

**GNU** is an extensive collection of free software, which can be used as an [[Operating_System]] or can be used in parts with other operating systems. The development of GNU, started by Richard Stallman in 1983 under the auspices of the Free Software Foundation (FSF), aimed to create a complete Unix-like operating system composed entirely of [[Free_Software]]. The name "GNU" is a recursive acronym for "GNU's Not Unix!".

## Key Aspects / Characteristics

- **Free Software Focus:** Emphasizes user freedom – the freedom to run, copy, distribute, study, change, and improve the software. This is legally defined by licenses like the GNU General Public License (GPL).
- **Unix-like:** Designed to be compatible with [[Unix]] and [[POSIX]] standards.
- **Components:** Includes a vast array of software:
    - Core utilities (fileutils, textutils, shellutils - providing commands like `ls`, `cp`, `mv`, `grep`, etc.)
    - [[Bash]] (The GNU Bourne-Again SHell)
    - [[GCC]] (The GNU Compiler Collection)
    - [[glibc]] (The GNU C Library)
    - Emacs (Text editor)
    - GNOME (Desktop environment, though now largely independent)
    - Many other applications and libraries.
- **GNU/Linux:** The [[Linux]] [[Kernel]] (developed separately by Linus Torvalds) filled the last major gap in the GNU system. The combination, commonly called "Linux", is more accurately referred to as "GNU/Linux" by the FSF to acknowledge the significant contribution of the GNU project's components.

## Examples / Use Cases

- Most "Linux distributions" heavily rely on GNU software for the user-space environment (shell, core utilities, compiler, C library).
- Using GCC to compile C/C++ programs.
- Using Bash as the command-line shell.
- Using GNU Emacs for text editing and development.

## Related Concepts
- [[Linux]] (The kernel often used with the GNU system)
- [[Operating_System]] (GNU provides the components for a complete OS)
- [[POSIX]] (GNU tools aim for POSIX compatibility)
- [[Free_Software]] (The philosophy behind GNU)
- [[Open_Source]] (Related but distinct concept focusing more on development methodology)
- [[Bash]], [[GCC]], [[glibc]] (Key GNU software components)

## Questions / Further Study
>[!question] What is the difference between GNU and Linux?
> [[GNU]] is a large collection of [[Free_Software]] components (like the [[Shell]], [[Compiler]], core utilities, libraries) that form most of a Unix-like [[Operating_System]]. [[Linux]] is specifically the [[Kernel]], the core part of the OS that manages hardware and processes. Most systems people refer to as "Linux" are actually a combination of the Linux kernel and the GNU system software (hence [[GNU]]/Linux).

---
**Source:** Worksheet WS1

    