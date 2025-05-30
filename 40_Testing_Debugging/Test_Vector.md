---
tags:
  - testing
  - concept
  - data
  - input
  - hardware
aliases:
  - Test Vectors
related:
  - Test_Case
  - Test_Data
  - Hardware_Testing
  - Simulation
  - Emulation
worksheet:
  - WS_Testing
date_created: 2025-04-14
---
# Test Vector

## Definition

A **Test Vector** is a set of inputs applied during the testing of a system, particularly common in hardware testing, simulation, and testing of components with well-defined input/output interfaces (like digital logic circuits or some software components). It represents a single instance or scenario used to stimulate the system under test.

## Key Aspects / Characteristics

- **Set of Inputs:** Represents a specific combination of input values applied simultaneously or in a specific sequence to the inputs of the system under test.
- **Hardware Context:** The term originated and is heavily used in hardware verification and testing (e.g., testing integrated circuits). A vector corresponds to the state of all input pins at a given clock cycle.
- **Software Context:** Can also be used more broadly in software testing to refer to a specific set of input data used for a [[Test_Case]], especially when dealing with multiple related inputs or testing state machines.
- **Stimulus:** Provides the stimulus to drive the system into a particular state or through a specific execution path.
- **Paired with Expected Output:** Test vectors are usually paired with the expected output(s) or state changes that the system should produce in response to that specific input vector.
- **Generation:** Can be generated manually, algorithmically (e.g., for fault models in hardware), or captured from real-world scenarios.

## Examples / Use Cases

- **Hardware (Testing an AND gate):**
    - Vector 1: Input A=0, Input B=0 -> Expected Output=0
    - Vector 2: Input A=0, Input B=1 -> Expected Output=0
    - Vector 3: Input A=1, Input B=0 -> Expected Output=0
    - Vector 4: Input A=1, Input B=1 -> Expected Output=1
- **Software (Testing a function `calculate(op, val1, val2)`):**
    - Vector 1: op='+', val1=5, val2=3 -> Expected Result=8
    - Vector 2: op='-', val1=10, val2=4 -> Expected Result=6
    - Vector 3: op='/', val1=8, val2=0 -> Expected Result=Error/Exception

## Related Concepts
- [[Test_Case]] (A test case might use one or more test vectors)
- [[Test_Data]] (Test vectors are a form of test data)
- Hardware Testing, Logic Simulation
- [[Input_Vector]] (Synonym in some contexts)

---
**Source:** Worksheet WS_Testing