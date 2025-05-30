---
tags:
  - testing
  - concept
  - technique
aliases:
  - Black-box Testing
  - Specification-based Testing
  - Behavioral Testing
related:
  - White-box_Test
  - Gray-box_Testing
  - Software_Testing
  - Requirements
  - Specification
  - Equivalence_Classes
  - Boundary_Value_Analysis
  - Decision_Table_Testing
  - State_Transition_Testing
worksheet:
  - WS_Testing
date_created: 2025-04-14
---
# Black-box Testing

## Definition

**Black-box Testing** is a software testing technique where the tester evaluates the functionality of the software **without** looking at or knowing the internal code structure, implementation details, or internal paths. Tests are based solely on analyzing the software's requirements and specifications (inputs, outputs, expected behavior). The software is treated as an opaque "black box."

## Key Aspects / Characteristics

- **Focus:** External behavior, inputs, and outputs. Validates software against requirements.
- **Perspective:** Tests from an end-user perspective.
- **Basis:** Requirements documents, specifications, use cases, user documentation.
- **No Code Knowledge:** Tester does not need programming skills or access to the source code.
- **Applicability:** Applicable at all levels of testing (unit, integration, system, acceptance), but particularly common at system and acceptance levels.
- **Techniques:** Common black-box test design techniques include:
    - [[Equivalence_Classes|Equivalence Partitioning]]
    - [[Boundary_Value_Analysis]]
    - Decision Table Testing
    - State Transition Testing
    - Use Case Testing

## Advantages

- Tests are independent of implementation; they remain valid even if the code changes (as long as requirements don't).
- Tester doesn't need programming expertise.
- Tests are done from a user's point of view, helping find usability issues and requirement discrepancies.
- Test case development can happen early, based on specifications.

## Disadvantages

- Can be inefficient, potentially leading to many redundant test cases if not designed well.
- Limited coverage; certain code paths or internal conditions might never be tested without seeing the code.
- Can miss internal logic errors or "extra" features not specified in requirements.
- Test results might be harder to trace back to specific code faults without internal knowledge.

## Related Concepts
- [[White-box_Test]] (Tests based on internal structure)
- [[Gray-box_Testing]] (Combines aspects of black-box and white-box)
- [[Software_Testing]]
- [[Requirements]], Specifications
- Test Design Techniques: [[Equivalence_Classes]], [[Boundary_Value_Analysis]], Decision Tables, State Transitions, Use Cases

---
**Source:** Worksheet WS_Testing