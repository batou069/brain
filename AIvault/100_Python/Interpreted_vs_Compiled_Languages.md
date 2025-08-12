---
tags:
  - python
  - programming_paradigms
  - interpreted_language
  - compiled_language
  - execution_model
  - concept_comparison
aliases:
  - Interpreted Languages
  - Compiled Languages
  - Python Execution
related:
  - "[[Python_Language_Overview]]"
  - "[[Python_Execution_Model_PVM_Bytecode|Python Execution Model (PVM, Bytecode)]]"
worksheet:
  - WS16
date_created: 2025-06-11
---
# Interpreted vs. Compiled Languages

Programming languages can be broadly categorized based on how their source code is translated into machine-executable instructions. The two primary approaches are **compilation** and **interpretation**.

## Compiled Languages
-   **Process:**
    1.  The entire source code is translated into machine code (or an intermediate assembly language, then to machine code) by a **compiler** *before* execution.
    2.  This machine code is specific to a particular processor architecture and operating system.
    3.  The resulting executable file can then be run directly by the computer's hardware.
-   **Characteristics:**
    -   **Performance:** Generally faster execution speed because the code is already translated into the machine's native language.
    -   **Error Detection:** Many errors (like syntax errors, type mismatches in statically-typed compiled languages) are caught during the compilation phase before the program runs.
    -   **Platform Dependence:** The compiled executable is typically platform-specific. To run on a different OS or CPU architecture, the code usually needs to be recompiled for that platform.
    -   **Development Cycle:** Involves a distinct compilation step, which can sometimes add time to the development cycle (compile -> link -> run).
-   **Examples:** C, C++, Java (compiles to bytecode for JVM, then JIT compiled to machine code), Go, Rust, Swift, Fortran.

## Interpreted Languages
-   **Process:**
    1.  The source code is read and executed line by line (or statement by statement) by an **interpreter** program *during runtime*.
    2.  The interpreter translates each statement into machine instructions and executes them immediately.
    3.  There is no separate, pre-compiled executable file in the same way as compiled languages (though some interpreted languages might involve an intermediate bytecode compilation step for optimization).
-   **Characteristics:**
    -   **Platform Independence (Portability):** The same source code can often run on any platform that has the appropriate interpreter installed, without needing to be recompiled for each platform.
    -   **Flexibility and Dynamic Features:** Often support dynamic typing, easier metaprogramming, and features like `eval()` (executing code from strings).
    -   **Development Cycle:** Typically faster development cycle (edit -> run) as there's no lengthy compilation step. Easier for scripting and rapid prototyping.
    -   **Performance:** Generally slower execution speed compared to compiled languages because the translation process happens at runtime for each statement.
    -   **Error Detection:** Many errors (especially runtime errors or type errors in dynamically-typed languages) are only discovered when the program is executed and the interpreter encounters the problematic line.
-   **Examples:** Python, JavaScript (though modern JS engines use JIT compilation), Ruby, PHP, Perl, Shell scripts.

## Python: A Hybrid Approach
Python is often described as an **interpreted language**, but its execution model has elements of compilation:
1.  **Compilation to Bytecode:** When a Python script (`.py` file) is run, the Python interpreter first compiles the source code into an intermediate form called **[[Python_Execution_Model_PVM_Bytecode|bytecode]]**. This bytecode is a lower-level, platform-independent representation of the source code.
2.  **Bytecode Storage:** This bytecode is often stored in `.pyc` files in a `__pycache__` directory. If the source code hasn't changed since the last run, Python can skip the compilation step and directly use the existing `.pyc` file.
3.  **Execution by Python Virtual Machine (PVM):** The bytecode is then executed by the **[[Python_Execution_Model_PVM_Bytecode|Python Virtual Machine (PVM)]]**, which is the runtime engine of Python. The PVM interprets the bytecode instructions and executes them.

**So, is Python compiled or interpreted?**
-   It's **interpreted** in the sense that there isn't a standalone executable file directly runnable by the OS without the Python interpreter. You need the Python interpreter to run Python programs.
-   It's **compiled** in the sense that the source code is first translated to bytecode, which is a form of compilation. This bytecode is then interpreted by the PVM.

This hybrid approach offers some of the portability and flexibility of interpreted languages along with some performance benefits from the bytecode compilation step.

## Comparison Summary

[list2mdtable|#Interpreted vs Compiled]
- Feature
    - Compiled Languages
        - Interpreted Languages
- **Translation**
    - Entire code translated to machine code *before* execution.
        - Code translated and executed line-by-line *during* runtime.
- **Execution Speed**
    - Generally faster.
        - Generally slower.
- **Platform Dependence**
    - Compiled executable is platform-specific.
        - Source code is often platform-independent (requires interpreter on target platform).
- **Error Detection**
    - Many errors caught at compile-time.
        - Many errors caught at runtime.
- **Development Cycle**
    - Longer (includes compilation step).
        - Shorter (edit and run).
- **Flexibility**
    - Often less flexible (e.g., static typing common).
        - Often more flexible (e.g., dynamic typing common).
- **Python's Position**
    - Not purely compiled in the traditional sense.
        - Often categorized as interpreted, but with an intermediate bytecode compilation step.

The lines can blur, as many modern "interpreted" languages (like JavaScript with V8, or Python with PyPy which uses JIT compilation) employ sophisticated Just-In-Time (JIT) compilation techniques to improve performance by compiling frequently executed code paths to native machine code at runtime.

---