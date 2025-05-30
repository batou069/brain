---
tags:
  - testing
  - concept
  - technique
  - verification
  - tool
aliases:
  - Static Code Analysis
related:
  - Software_Testing
  - Verification
  - White-box_Test
  - Linting
  - Compiler_Warnings
  - Code_Review
  - Dynamic_Analysis
worksheet:
  - WS_Testing
date_created: 2025-04-14
---
# Static Analysis

## Definition

**Static Analysis** (or Static Code Analysis) is the analysis of computer software performed **without actually executing** the program. It involves examining the source code, byte code, or object code using automated tools (static analyzers) or manual processes (like code reviews) to find potential defects, vulnerabilities, or deviations from coding standards.

## Key Aspects / Characteristics

- **No Execution:** The code is analyzed in its static state, not while running. This contrasts with Dynamic Analysis (which involves observing the program during execution).
- **Automated Tools:** Often performed using specialized static analysis tools (e.g., SonarQube, Checkstyle, PMD, FindBugs for Java; Pylint, Flake8, MyPy for Python; Cppcheck, Clang Static Analyzer for C/C++; ESLint for JavaScript).
- **Manual Processes:** [[Code_Review|Code reviews]], walkthroughs, and inspections are also forms of static analysis.
- **Types of Issues Found:** Can detect various issues, including:
    - Potential bugs (e.g., null pointer dereferences, resource leaks, buffer overflows, race conditions).
    - Security vulnerabilities (e.g., SQL injection flaws, cross-site scripting).
    - Violations of coding standards or style guides.
    - Unreachable code ("dead code").
    - Complex code that might be hard to maintain (high cyclomatic complexity).
    - Potential performance bottlenecks.
    - Type errors (especially with type hinting tools like MyPy).
- **Early Detection:** Can find defects early in the development cycle, often before the code is even run or tested dynamically.
- **False Positives:** Static analysis tools can sometimes report issues that are not actual defects (false positives), requiring human review.
- **Limitations:** Cannot detect runtime errors that depend on specific inputs, timing, or environmental factors. Cannot fully verify functional correctness.

## Examples / Use Cases

- Running a [[Linting|linter]] like Pylint on Python code to check for style violations and potential errors.
- Using a security-focused static analyzer (SAST tool) to scan code for common vulnerabilities.
- Compiling C code with high warning levels (`gcc -Wall -Wextra`) enables the compiler's built-in static analysis checks.
- Performing a peer code review to manually inspect code for logic errors and maintainability issues.

## Related Concepts
- [[Software_Testing]], [[Verification]] (Static analysis is a verification technique)
- [[White-box_Test]] (Analyzes internal structure)
- [[Linting]] (A specific type of static analysis focused on style and simple errors)
- [[Compiler_Warnings]] (A form of static analysis performed by the compiler)
- [[Code_Review]] (Manual static analysis)
- Dynamic Analysis (Contrasting technique involving execution)

---
**Source:** Worksheet WS_Testing