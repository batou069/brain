---
tags: [testing, concept, quality_assurance]
aliases: []
related:
  - "[[Validation]]"
  - "[[Software_Testing]]"
  - "[[Requirements]]"
  - "[[Specification]]"
  - "[[Static_Analysis]]"
  - "[[Walkthrough]]"
  - "[[Inspection]]"
  - "[[Review]]"
worksheet: [WS_Testing]
date_created: 2025-04-12
---
# Verification

## Definition

**Verification** is the process of evaluating a software system or component during or at the end of a development phase to determine whether it satisfies the conditions imposed at the start of that phase. In essence, it answers the question: **"Are we building the product right?"** It focuses on ensuring the software conforms to its specification, standards, and design.

## Key Aspects / Characteristics

- **Focus:** Conformance to specification, design, standards, requirements. Checks if the product is built according to the defined rules and plans.
- **Timing:** Typically occurs throughout the development lifecycle, often involving static techniques.
- **Activities:** Includes activities like:
    - Reviews (design reviews, code reviews, requirements reviews)
    - Walkthroughs
    - Inspections
    - [[Static_Analysis]]
    - Checking adherence to coding standards
    - [[Unit_Test|Unit testing]] and [[Integration_Test|integration testing]] often have strong verification aspects (checking if code matches detailed design).
- **Goal:** To detect defects introduced during the development phase.

## Verification vs. Validation

- **Verification:** Are we building the product *right*? (Conformance to spec)
- **[[Validation]]:** Are we building the *right* product? (Fitness for purpose, meets user needs)

Both are essential parts of [[Software_Testing]] and quality assurance. A product can be verified (perfectly matches a flawed specification) but not validated (doesn't meet user needs). Conversely, a product might meet user needs (validated) but deviate from the original specification (failed verification).

## Related Concepts
- [[Validation]]
- [[Software_Testing]]
- [[Requirements_Engineering]] (*Implied*)
- [[Software_Design]] (*Implied*)
- [[Static_Analysis]], Code Reviews, Walkthroughs, Inspections

---

**Source:** Worksheet WS_Testing, IEEE Standard Glossary of Software Engineering Terminology