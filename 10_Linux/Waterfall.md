---
tags:
  - software_engineering
  - methodology
  - sdlc
  - concept
  - process
aliases:
  - Waterfall Model
related:
  - "[[Software_Development_Lifecycle]]"
  - "[[Agile_Development]]"
  - "[[Scrum]]"
  - "[[Requirements_Engineering]]"
  - "[[Software_Design]]"
  - "[[Software_Testing]]"
worksheet:
  - WS1
date_created: 2025-04-20
---
# Waterfall Model

## Definition

The **Waterfall Model** is a traditional, sequential (non-iterative) software development lifecycle (SDLC) model where progress flows steadily downwards (like a waterfall) through distinct phases: Requirements, Design, Implementation, Verification (Testing), and Maintenance. Each phase must be fully completed before the next phase begins.

## Phases (Typical)

1.  **Requirements Analysis & Definition:** Gather, analyze, and document all system requirements. Output: Requirements Specification document.
2.  **System and Software Design:** Define the overall architecture, modules, interfaces, and data structures based on the requirements. Output: Design documents.
3.  **Implementation and Unit Testing:** Write the code for individual modules/units based on the design, and perform [[Unit_Test|unit testing]] on each module. Output: Source code, unit-tested modules.
4.  **Integration and System Testing:** Integrate the individual modules and test the entire system as a whole ([[Integration_Test]], [[System_Test]]) to verify it meets the requirements defined in the first phase. Output: Tested system, test reports.
5.  **Operation and Maintenance:** Deploy the system to the user environment. Perform ongoing maintenance, including bug fixes, enhancements, and updates.

## Key Aspects / Characteristics

- **Sequential Flow:** Strict, linear progression from one phase to the next.
- **Phase Completion:** Each phase must be fully completed and signed off before the next can start.
- **Documentation-Heavy:** Relies heavily on comprehensive documentation being produced and approved at the end of each phase.
- **Limited Feedback Loop:** Difficult to go back to a previous phase once the current phase is underway. Changes to requirements late in the process are very costly and disruptive.
- **Predictive Approach:** Assumes requirements can be fully defined and frozen upfront.

## Advantages

- Simple to understand and manage.
- Clear milestones and deliverables for each phase.
- Well-suited for projects where requirements are very stable, well-understood, and unlikely to change (rare in practice).
- Discipline enforced through phase completion requirements.

## Disadvantages

- **Inflexible:** Very difficult and expensive to accommodate changes in requirements once a phase is complete.
- **Late Feedback:** Working software is not produced until late in the cycle, meaning users/clients don't see the product until near the end. Problems might be discovered too late.
- **Risk:** Assumes requirements are perfectly captured upfront, which is often unrealistic. If requirements are flawed, the entire project might deliver the wrong product.
- **Blocked Phases:** Delays in one phase directly impact the start of the next.
- **Not Suitable for Complex/Uncertain Projects:** Poor fit for projects with evolving requirements, high complexity, or significant technical uncertainty.

## Modern Relevance

While the pure Waterfall model is rarely used today for large or complex software projects due to its rigidity, its phased approach still influences some methodologies. It is generally considered unsuitable for most modern software development compared to iterative and incremental models like [[Agile_Development]].

## Related Concepts
- [[Software_Development_Lifecycle]] (SDLC)
- [[Agile_Development]], [[Scrum]] (Contrast: Iterative, flexible models)
- [[Requirements_Engineering]], [[Software_Design]], [[Software_Testing]] (Phases within the model)

---
**Source:** Worksheet WS1