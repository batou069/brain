---
tags:
  - python
  - execution_model
  - pvm
  - bytecode
  - interpreter
  - compiler
  - concept
aliases:
  - Python Virtual Machine
  - Python Bytecode
  - .pyc files
  - CPython Execution
related:
  - "[[Python_Language_Overview]]"
  - "[[Interpreted_vs_Compiled_Languages]]"
  - "[[Python_Memory_Management]]"
worksheet:
  - WS16
date_created: 2025-06-11
---
# Python Execution Model (PVM, Bytecode)

While Python is often described as an [[Interpreted_vs_Compiled_Languages|interpreted language]], its execution process involves an intermediate compilation step to **bytecode**, which is then executed by the **Python Virtual Machine (PVM)**.

## The Execution Process

[d2]
```d2
direction: down
shape: sequence_diagram

SourceCode: "Python Source Code (.py file)" {
  shape: document
  style.fill: "#E3F2FD" # Light Blue
}

Compiler: "Python Compiler (Part of Interpreter)" {
  shape: process
  style.fill: "#FFF9C4" # Light Yellow
}

Bytecode: "Bytecode (.pyc file - cached)" {
  shape: document
  style.fill: "#FFE0B2" # Light Orange
}

PVM: "Python Virtual Machine (PVM)" {
  shape: process
  style.fill: "#C8E6C9" # Light Green
  InterpreterLoop: "Bytecode Interpreter Loop"
}

OS_Hardware: "Operating System / Hardware" {
  shape: cylinder # Represents lower level
  style.fill: "#D1C4E9" # Light Purple
}

SourceCode -> Compiler: "1. Read & Parse"
Compiler -> Bytecode: "2. Compile to Bytecode"
Bytecode -> PVM.InterpreterLoop: "3. Load & Execute"
PVM.InterpreterLoop -> OS_Hardware: "4. Interacts with OS/Hardware via C calls (for CPython)"
OS_Hardware -> PVM.InterpreterLoop: "Results/System Calls"

style SourceCode { icon: "📄" }
style Compiler { icon: "⚙️" }
style Bytecode { icon: "📜" }
style PVM { icon: "🚀" }
style OS_Hardware { icon: "💻" }
```

1.  **Parsing and Compilation to Bytecode:**
    -   When you run a Python script (e.g., `python my_script.py`), the Python interpreter first reads your source code.
    -   The source code is parsed into an Abstract Syntax Tree (AST).
    -   This AST is then **compiled** into a lower-level, platform-independent intermediate representation called **bytecode**.
    -   This bytecode is a set of instructions specifically designed for the Python Virtual Machine.

2.  **Bytecode Caching (`.pyc` files and `__pycache__`):**
    -   To speed up subsequent executions, Python automatically caches the compiled bytecode in files with a `.pyc` extension (e.g., `my_script.cpython-39.pyc`).
    -   These `.pyc` files are typically stored in a subdirectory named `__pycache__` within the same directory as the `.py` source file.
    -   When you run a script again, Python checks if a valid `.pyc` file exists (i.e., if its timestamp matches or is newer than the `.py` file). If so, it skips the compilation step and directly loads the bytecode from the `.pyc` file. This makes subsequent startups faster.
    -   You don't typically interact with `.pyc` files directly; Python manages them automatically.

3.  **Execution by the Python Virtual Machine (PVM):**
    -   The **Python Virtual Machine (PVM)** is the runtime engine of Python. It's the component that actually executes the Python program.
    -   The PVM takes the compiled bytecode and interprets it instruction by instruction.
    -   It manages memory ([[Python_Memory_Management]]), handles object creation and destruction, manages the call stack for function calls, and interacts with the underlying operating system and hardware.
    -   The PVM is what makes Python portable: as long as a PVM is implemented for a specific platform, Python bytecode can run on it.

## Bytecode
-   **Nature:** Bytecode consists of a sequence of operation codes (opcodes) and their arguments. Each opcode performs a specific action, such as loading a variable, performing an arithmetic operation, calling a function, or jumping to another instruction.
-   **Platform Independence:** Bytecode itself is platform-independent. The same `.pyc` file can (in principle) be run on any system with a compatible Python PVM.
-   **Not Machine Code:** Bytecode is not native machine code that can be directly executed by the computer's CPU. It requires the PVM to interpret it.
-   **Inspection:** You can inspect the bytecode for a function or module using the `dis` module (disassembler) in Python.
    ```python
    import dis

    def example_function(a, b):
        c = a + b
        return c * 2

    # dis.dis(example_function)
    ```
    Executing `dis.dis(example_function)` would output a human-readable representation of the bytecode instructions for that function.

## Python Virtual Machine (PVM)
-   **Core Component:** The PVM is the heart of a Python interpreter (like CPython, Jython, IronPython, PyPy).
-   **Stack-Based Architecture (Commonly):** CPython's PVM, for example, is a stack-based virtual machine. It uses a stack to hold operands and intermediate results for computations.
-   **Main Loop:** The PVM executes a main loop that fetches a bytecode instruction, evaluates its arguments, performs the operation, and moves to the next instruction.
-   **[[Python_Memory_Management|Memory Management]]:** The PVM is responsible for allocating memory for objects and reclaiming it when objects are no longer in use (via reference counting and garbage collection in CPython).
-   **Interaction with OS:** For operations like file I/O or network communication, the PVM makes calls to the underlying operating system.

## Implementations of Python
It's important to note that "Python" is a language specification, and there are multiple implementations of this language. Each implementation has its own PVM (or an alternative execution strategy):
-   **CPython:** The reference implementation, written in C. This is the most widely used version of Python, and its PVM is what's typically referred to when discussing "the PVM."
-   **Jython:** Python implemented in Java, compiles Python code to Java bytecode, which then runs on the Java Virtual Machine (JVM).
-   **IronPython:** Python implemented for the .NET framework, compiles to Common Language Intermediate Language (CIL) bytecode.
-   **PyPy:** An alternative Python interpreter that includes a Just-In-Time (JIT) compiler. PyPy compiles Python bytecode (or parts of it) to native machine code at runtime for frequently executed sections, often resulting in significant performance improvements over CPython for certain workloads.

**In summary:**
Python code undergoes a compilation step to **bytecode**. This bytecode is then executed by the **Python Virtual Machine (PVM)**. This hybrid approach provides a balance of platform independence, ease of development, and reasonable performance (which can be further enhanced by implementations like PyPy).

---