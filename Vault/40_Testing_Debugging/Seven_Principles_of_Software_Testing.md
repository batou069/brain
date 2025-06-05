---
tags:
  - testing
  - concept
  - principle
  - technique
  - test_double
  - isolation
  - verification
aliases:
  - Testing Principles
  - Test Spy
related:
  - "[[Software_Testing]]"
  - "[[Exhaustive_Testing]]"
  - "[[Defect_Clustering]]"
  - "[[Pesticide_Paradox]]"
  - "[[Testing_Context_Dependence]]"
  - "[[Absence_of_Errors_Fallacy]]"
  - "[[Early_Testing]]"
  - "[[Test_Double_C]]"
  - "[[Stubs]]"
  - "[[Mocks]]"
  - "[[Dummies]]"
  - "[[Fakes]]"
  - "[[Unit_Test]]"
worksheet:
  - WS_Testing
date_created: 2025-04-21
---
\# Seven Principles of Software Testing

## Definition

These are seven fundamental principles derived from decades of software testing experience, providing guidance on the nature and best practices of [[Software_Testing]]. Understanding these principles helps testers work more effectively and manage expectations.

## The Principles

1.  **Testing shows presence of defects, not their absence:** [[Software_Testing]] can reveal that defects are present, but it cannot prove that there are no defects left. Even extensive testing doesn't guarantee bug-free software. Testing reduces the probability of undiscovered defects remaining.
2.  **Exhaustive testing is impossible:** Testing every possible combination of inputs, preconditions, and execution paths is infeasible for all but the simplest programs. Testers must use risk analysis, test techniques ([[Equivalence_Classes]], [[Boundary_Value_Analysis]]), and prioritization to focus efforts.
3.  **Early testing saves time and money:** Finding and fixing defects early in the Software Development Lifecycle (e.g., during requirements analysis or design) is significantly cheaper than fixing them later during system testing or after release.
4.  **Defect clustering:** Defects are often not evenly distributed throughout the software. A small number of modules or components usually contain most of the defects discovered during pre-release testing (Pareto principle). Testing effort should focus on these defect-prone areas.
5.  **The pesticide paradox:** If the same set of tests are run repeatedly, they eventually become ineffective at finding new defects, just like pesticides become ineffective against insects over time. Test cases need to be regularly reviewed, updated, and new tests added to find new bugs.
6.  **Testing is context-dependent:** The approach, techniques, rigor, and objectives of testing vary depending on the context of the software. Testing safety-critical software (e.g., medical device, avionics) is vastly different from testing a simple e-commerce website or a mobile game.
7.  **Absence-of-errors fallacy:** Finding and fixing many defects does not guarantee the software system is useful or meets user needs and expectations. If the system is built incorrectly according to flawed requirements, testing might show few defects but the system itself might be unusable or solve the wrong problem ([[Validation]] is also crucial).

## Related Concepts
- [[Software_Testing]]
- [[Verification]], [[Validation]]
- [[Risk_Based_Testing]] (*Implied by Principle 2*)
- [[Test_Case]] Design Techniques

---
**Source:** Worksheet WS_Testing, ISTQB Foundation Level Syllabus

# Spies (Test Doubles)

## Definition

A **Spy** is a type of [[Test_Double_C]] that acts like a [[Stubs|Stub]] (providing canned answers or performing default actions) but also **records information** about how it was interacted with by the unit under test. After the unit under test is exercised, the test can query the Spy to verify if certain methods were called, how many times, and potentially with what arguments.

## Purpose

- **Indirect Output Verification:** Verify actions taken by the unit under test that don't have an obvious return value or state change to assert on directly, but result in calls to a dependency (e.g., calling a logger, sending an email via a service).
- **State & Behavior:** Combines aspects of state verification (like stubs) with aspects of behavior verification (like mocks), but often less strictly than mocks.
- **Flexibility:** Unlike [[Mocks]], Spies typically don't have expectations set *before* the interaction. Verification happens *after* the interaction by inspecting the recorded information.

## Key Aspects

- **Acts Like Stub:** Can provide return values if needed.
- **Records Interactions:** Internally logs details about calls made to it (method name, arguments, number of calls).
- **Verification After Action:** Test code interacts with the unit under test first, then interrogates the Spy to assert on the recorded interactions.

## Example Scenario

Imagine testing a function `log_error(message, logger)` that should call the `logger.error(message)` method.

- **Unit Under Test:** `log_error` function
- **Dependency:** `logger` object
- **Spy:** A `SpyLogger` object that implements the `error` method. When `error` is called, it might do nothing (like a stub) but *also* record the message it received and increment a call counter.
- **Test:**
    1. Create a `SpyLogger`.
    2. Call `log_error("File not found", spy_logger)`.
    3. **Assert against the Spy:**
        - `assert(spy_logger.call_count == 1)`
        - `assert(strcmp(spy_logger.last_message_received, "File not found") == 0)`

## Related Concepts
- [[Test_Double_C]] (Spies are a type)
- [[Stubs]] (Spies often behave like stubs but add recording)
- [[Mocks]] (Contrast: Mocks have upfront expectations, Spies record for later verification)
- [[Dummies]], [[Fakes]]
- [[Unit_Test]]
- Behavior Verification

---
**Source:** Worksheet WS_Testing, Gerard Meszaros' "xUnit Test Patterns"