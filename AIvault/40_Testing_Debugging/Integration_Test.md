---
tags:
  - testing
  - concept
  - level
aliases:
  - Integration Testing
related:
  - Software_Testing
  - Unit_Test
  - System_Test
  - Stubs
  - Mocks
  - Top-down_Integration
  - Bottom-up_Integration
  - Big_Bang_Integration
  - Interface_Testing
worksheet:
  - WS_Testing
date_created: 2025-04-14
---
# Integration Test

## Definition

**Integration Testing** is a level of [[Software_Testing]] where individual software modules or units (that have typically already passed [[Unit_Test|unit testing]]) are combined and tested as a group. The primary purpose is to verify the interaction and communication between these integrated components, exposing defects in their interfaces and interactions.

## Key Aspects / Characteristics

- **Focus:** Interfaces between components, data flow between modules, interaction logic.
- **Scope:** Tests combinations of units working together. Can range from integrating two units to integrating entire subsystems.
- **Goal:** Verify that integrated components work together as expected, find defects related to interfacing (e.g., incorrect data passing, timing issues, invalid assumptions about collaborators).
- **Timing:** Occurs after [[Unit_Test]] and before [[System_Test]].
- **Test Basis:** Software design documents, interface specifications, architecture diagrams, use cases involving multiple components.
- **Stubs and Drivers:** May require the use of test doubles ([[Stubs]], drivers) to simulate components that are not yet integrated or available.
- **Approaches:** Different strategies exist for the order of integration:
    - [[Top-down_Integration]]: Test high-level modules first, using stubs for lower-level ones.
    - [[Bottom-up_Integration]]: Test low-level modules first, using drivers to simulate higher-level ones.
    - Big Bang Integration: Integrate all (or most) modules at once (generally discouraged due to difficulty in isolating faults).
    - Sandwich/Hybrid Integration: Combines top-down and bottom-up.

## Advantages

- Detects defects related to interfaces and interactions early.
- Verifies that independently developed units work together correctly.
- Can be more effective at finding issues related to data flow or control flow between modules than unit testing alone.

## Disadvantages

- Can be complex to set up, especially managing dependencies and test doubles.
- Isolating the root cause of a failure can be harder than in unit testing, as the failure might stem from any of the integrated components or their interface.
- Requires integrating code, which might happen later in the cycle than unit testing.

## Related Concepts
- [[Software_Testing]] Levels ([[Unit_Test]], [[System_Test]])
- Interfaces, Modules, Components
- Test Doubles ([[Stubs]], [[Mocks]], Drivers)
- Integration Strategies ([[Top-down_Integration]], [[Bottom-up_Integration]], Big Bang)

---
**Source:** Worksheet WS_Testing