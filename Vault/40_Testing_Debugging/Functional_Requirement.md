---
tags:
  - testing
  - concept
  - requirements
  - specification
  - quality
aliases:
  - Functional Requirements
  - Non-functional Requirements
  - NFRs
  - Quality Attributes
  - -ilities
related:
  - Non-functional_Requirement
  - Requirements_Engineering
  - Software_Testing
  - Black-box_Test
  - Acceptance_Test
  - Use_Case
  - Functional_Requirement
  - Performance_Testing
  - Security_Testing
  - Usability_Testing
worksheet:
  - WS_Testing
date_created: 2025-04-21
---
# Functional Requirement

## Definition

A **Functional Requirement** defines **what** a software system or component must *do*. It specifies a function, behavior, or task that the system must be capable of performing, often described in terms of inputs, processing, and outputs. Functional requirements describe the core functionality delivered to the user or interacting systems.

## Key Aspects / Characteristics

- **Defines Functionality:** Specifies *what* the system does.
- **Behavioral:** Describes interactions, calculations, data manipulation, business logic, etc.
- **Testable:** Should be specific, measurable, and testable. [[Black-box_Test|Black-box testing]] techniques are often used to verify functional requirements.
- **Examples:**
    - "The system *shall* allow users to log in using a username and password."
    - "The system *shall* calculate the total cost of items in the shopping cart, including tax."
    - "The system *shall* generate a monthly sales report in PDF format."
    - "The user *must* be able to search for customers by name or ID."
- **Source:** Derived from use cases, user stories, business rules, and stakeholder needs.

## Functional vs. Non-functional Requirements

- **Functional:** *What* the system does (features, tasks).
- **[[Non-functional_Requirement|Non-functional]]:** *How* the system does it, or constraints on its operation (quality attributes like performance, security, usability, reliability).

## Related Concepts
- [[Non-functional_Requirement]] (Describes quality attributes)
- [[Requirements_Engineering]] (Process of eliciting, documenting, managing requirements)
- [[Software_Testing]], [[Black-box_Test]], [[Acceptance_Test]] (Verify functional requirements)
- [[Use_Case]], User Story (Common ways to capture functional requirements)
- Specification Document

---
**Source:** Worksheet WS_Testing

# Non-functional Requirement (NFR)

## Definition

A **Non-functional Requirement (NFR)** defines **how** a software system or component should perform a function or specifies a constraint on its operation. NFRs describe the **quality attributes** or characteristics of the system, rather than its specific behaviors ([[Functional_Requirement|functional requirements]]). They often describe the "-ilities" of a system.

## Key Aspects / Characteristics

- **Defines Quality/Constraints:** Specifies *how well* the system performs or constraints under which it must operate.
- **Non-Behavioral (Mostly):** Describes attributes of the system, not specific actions it takes (though performance requirements often relate to function execution time).
- **Testable:** Should ideally be specific, measurable, achievable, relevant, and time-bound (SMART) to be testable. Testing NFRs often requires specialized techniques (e.g., performance testing tools, security scanning).
- **Categories/Examples:**
    - **Performance:** Response time, throughput, resource utilization (e.g., "Login *shall* complete within 2 seconds under peak load," "System *shall* handle 1000 concurrent users").
    - **Security:** Authentication, authorization, data encryption, vulnerability resistance (e.g., "Passwords *must* be stored hashed," "System *shall* resist common SQL injection attacks").
    - **Reliability:** [[MTBF]], availability, fault tolerance (e.g., "System uptime *shall* be 99.9%," "System *shall* recover from database connection failure within 5 minutes").
    - **Usability:** Ease of use, learnability, accessibility (e.g., "A new user *shall* be able to complete task X within 3 minutes without training," "System *shall* comply with WCAG 2.1 AA accessibility standards").
    - **Maintainability:** Ease of modification, testability, modularity (e.g., "Code *shall* adhere to specified coding standards," "[[Unit_Test|Unit test]] [[Test_Coverage|coverage]] *shall* be at least 80%").
    - **Portability:** Ability to run on different environments (e.g., "Application *shall* run on Windows 10 and macOS Monterey").
    - **Scalability:** Ability to handle increased load (e.g., "System *shall* be able to scale horizontally to handle a 50% increase in user traffic").
- **Source:** Derived from stakeholder expectations, business goals, technical constraints, industry standards.

## Functional vs. Non-functional Requirements

- **[[Functional_Requirement|Functional]]:** *What* the system does (features, tasks).
- **Non-functional:** *How* the system does it, or constraints on its operation (quality attributes).

## Related Concepts
- [[Functional_Requirement]] (Describes features)
- [[Requirements_Engineering]] (Process of eliciting, documenting, managing requirements)
- [[Software_Testing]] (Specialized testing types verify NFRs)
- Performance Testing, Security Testing, Usability Testing, Reliability Testing
- Quality Attributes, "-ilities"

---
**Source:** Worksheet WS_Testing