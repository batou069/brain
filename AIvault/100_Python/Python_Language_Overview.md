---
tags:
  - python
  - programming_language
  - high_level
  - interpreted
  - dynamic_typing
  - general_purpose
  - concept
  - overview
aliases:
  - What is Python
related:
  - "[[100_Python/Python_Intro/_Python_Intro_MOC|_Python_Intro_MOC]]"
  - "[[Interpreted_vs_Compiled_Languages]]"
  - "[[Dynamic_vs_Static_Typing]]"
worksheet:
  - WS16
date_created: 2025-06-11
---
# Python Language Overview

**Python** is a high-level, general-purpose programming language known for its emphasis on code readability and simplicity. Created by Guido van Rossum and first released in 1991, Python's design philosophy highlights developer productivity and code maintainability.

## Key Characteristics
[list2tab|#Python Features]
- High-Level
    -   Python abstracts many low-level details of the computer's hardware (like memory management, CPU operations). This allows developers to focus on solving problems rather than on intricate system details.
    -   Syntax is designed to be human-readable, often resembling pseudocode.
- Interpreted
    -   Python code is typically executed line by line by an interpreter, rather than being compiled into machine code beforehand. This makes development faster and more interactive. (See [[Interpreted_vs_Compiled_Languages]])
    -   However, Python code is first compiled into an intermediate form called [[Python_Execution_Model_PVM_Bytecode|bytecode]], which is then executed by the [[Python_Execution_Model_PVM_Bytecode|Python Virtual Machine (PVM)]].
- Dynamically Typed
    -   The data type of a variable is checked during runtime, not at compile time. You don't need to declare a variable's type explicitly. (See [[Dynamic_vs_Static_Typing]])
    -   Example: `x = 5` (x is an int), then `x = "hello"` (x is now a string).
- Strongly Typed
    -   While dynamically typed, Python is also strongly typed. This means that operations are generally not allowed between incompatible types without explicit conversion.
    -   Example: `5 + "hello"` will raise a `TypeError`. You need `str(5) + "hello"`.
- General-Purpose
    -   Python can be used for a wide variety of applications, including:
        -   Web development (e.g., Django, Flask)
        -   Data science, machine learning, AI (e.g., NumPy, Pandas, Scikit-learn, TensorFlow, PyTorch)
        -   Scientific and numeric computing
        -   Automation and scripting
        -   Software development
        -   Game development (e.g., Pygame)
        -   Desktop GUIs (e.g., Tkinter, PyQt, Kivy)
- Object-Oriented (OOP) and Multi-Paradigm
    -   Python supports multiple programming paradigms, including object-oriented, imperative, and functional programming styles.
    -   Everything in Python is an object.
- Extensive Standard Library
    -   Python comes with a large standard library that provides tools for many common tasks (e.g., working with strings, files, networking, regular expressions, dates/times). This is often referred to as "batteries included."
- Large Ecosystem of Third-Party Packages
    -   The Python Package Index (PyPI) hosts hundreds of thousands of third-party packages that extend Python's capabilities for virtually any task.
- Readability and Simplicity
    -   Python's syntax is designed to be clean and readable, using indentation to define code blocks rather than braces or keywords.
    -   This focus on readability makes it easier to learn and maintain code.
- Cross-Platform
    -   Python interpreters are available for many operating systems (Windows, macOS, Linux/Unix), making Python code generally portable.
- Open Source
    -   Python is free to use and distribute, even for commercial purposes. Its development is managed by the Python Software Foundation (PSF).

## Python Versions
-   Python 2.x (Legacy): Reached end-of-life in 2020. Not recommended for new projects.
-   Python 3.x: The current and future version of Python. Offers many improvements and new features over Python 2.

Python's combination of ease of use, versatility, and a strong ecosystem has made it one of the most popular programming languages in the world.

---