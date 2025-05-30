---
tags:
  - testing
  - concept
  - technique
  - test_double
  - isolation
aliases:
  - Test Fake
related:
  - "[[Test_Double_C]]"
  - "[[Stubs]]"
  - "[[Mocks]]"
  - "[[Dummies]]"
  - "[[Spies]]"
  - "[[Unit_Test]]"
  - "[[Integration_Test]]"
  - "[[In_Memory_Database]]"
worksheet:
  - WS_Testing
date_created: 2025-04-21
---
# Fakes (Test Doubles)

## Definition

A **Fake** is a type of [[Test_Double_C]] that provides a **working implementation** of the dependency it replaces, but takes some shortcut or simplification that makes it unsuitable for production use. Fakes often substitute complex, slow, or external dependencies with simpler, faster, in-memory versions that share the same interface.

## Purpose

- **Simulate Complex Dependencies:** Provide a functional replacement for dependencies like databases, network services, or complex subsystems.
- **Enable Testing:** Allow [[Unit_Test|unit]] or [[Integration_Test|integration tests]] to run without relying on the actual heavy-weight dependency.
- **Speed & Reliability:** Fakes are typically much faster and more reliable/deterministic than the real dependencies they replace.
- **Control State:** Allow tests to easily set up and verify the state of the simulated dependency.

## Key Aspects

- **Working Implementation:** Unlike Stubs or Mocks, Fakes actually implement the required behavior, just in a simplified way.
- **Not Production Ready:** The simplification makes them unsuitable for production (e.g., an in-memory database doesn't provide persistence).
- **Stateful:** Fakes often maintain state across calls within a single test, allowing tests for more complex interactions than simple stubs might support.

## Example Scenario

Imagine testing a data repository layer (`UserRepository`) that normally interacts with a real SQL database.

- **Unit Under Test:** `UserService` (which uses `UserRepository`)
- **Dependency:** `UserRepository` (real implementation talks to SQL DB)
- **Fake:** A `FakeUserRepository` could be implemented using an in-memory [[Data_Structure]] (like a [[Hash_Table_DS]] or [[Vector_DS]]) to store user data. It would implement the same methods (`find_user`, `save_user`, `delete_user`) as the real repository, but operate entirely in memory.
- **Test:** Tests for `UserService` would be configured (e.g., via dependency injection) to use the `FakeUserRepository`. This allows testing the `UserService` logic quickly without needing a database connection.

## Related Concepts
- [[Test_Double_C]] (Fakes are a type)
- [[Stubs]], [[Mocks]], [[Dummies]], [[Spies]] (Other test doubles)
- [[Unit_Test]], [[Integration_Test]]
- [[In_Memory_Database]] (A common example of a Fake)
- Dependency Injection

---
**Source:** Worksheet WS_Testing, Gerard Meszaros' "xUnit Test Patterns"