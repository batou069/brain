---
tags: [testing, concept, defect, bug]
aliases: [Error Fault Failure, Defect, Bug]
related:
  - "[[Software_Testing]]"
  - "[[Debugging]]"
  - "[[Defect_Rate]]"
  - "[[Root_Cause_Analysis]]"
worksheet: [WS_Testing]
date_created: 2025-04-12
---
# Failures, Faults, and Errors (Defects)

## Definition

These terms describe different aspects of software defects, often used interchangeably but having distinct meanings in software testing theory (e.g., according to IEEE standards or ISTQB):

1.  **Error (or Mistake):** A human action that produces an incorrect result. This is the source of the problem, typically made by developers, designers, analysts, etc. (e.g., a typo in code, a misunderstanding of requirements, a logical flaw in design).
2.  **Fault (Defect or Bug):** A manifestation of an error in the software artifact (e.g., specification, design document, source code). It's an anomaly or flaw in a component or system that could cause it to fail to perform its required function. This is what testers often refer to as a "bug" found in the code.
3.  **Failure:** The observable incorrect behavior or deviation of the software from its expected result during execution. A failure occurs when a fault is executed under specific conditions. This is what the end-user typically observes as the system "not working correctly".

## Relationship

**Error** (Human Mistake) -> leads to -> **Fault** (Defect/Bug in code/docs) -> which, when executed under certain conditions, may cause a -> **Failure** (Observable incorrect behavior).

## Key Aspects / Characteristics

- **Not all faults cause failures:** A fault might exist in code that is rarely or never executed, or its execution might not lead to observable incorrect behavior under tested conditions.
- **Failures can have multiple causes:** A single failure might be triggered by the interaction of multiple faults, or environmental conditions.
- **Root Cause:** [[Debugging]] often involves tracing a failure back to the underlying fault(s) and potentially further back to the originating error (mistake) to prevent recurrence (Root Cause Analysis).
- **Terminology:** While the distinction is precise, in common practice, "bug" or "defect" are often used to refer to both faults and failures. [[Software_Testing]] aims to trigger failures to reveal underlying faults caused by errors.

## Examples

- **Error:** A programmer misunderstands an algorithm and writes `x < 0` instead of `x <= 0`.
- **Fault (Bug):** The incorrect line of code `if (x < 0)` exists in the software.
- **Failure:** When the program runs with `x = 0`, it takes the wrong execution path because the fault `(x < 0)` evaluates to false when it should have been true (`x <= 0`), leading to incorrect output or behavior. If the program only ever runs with `x = 5` or `x = -5`, this specific fault might never cause an observable failure.

## Related Concepts
- [[Software_Testing]] (Aims to find failures/faults)
- [[Debugging]] (Process of finding and fixing faults causing failures)
- [[Defect_Rate]] (Metric related to faults)
- [[Root_Cause_Analysis]] (*Implied*)

---
**Source:** Worksheet WS_Testing, ISTQB Glossary