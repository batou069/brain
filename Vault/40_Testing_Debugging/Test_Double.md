---
tags: [testing, concept, technique, isolation, c, python]
aliases: [Test Doubles]
related: 
  - "[[Stubs]]"
  - "[[Mocks]]"
  - "[[Dummies]]"
  - "[[Fakes]]"
  - "[[Spies]]"
  - "[[Unit_Test]]"
  - "[[Integration_Test]]"
  - "[[Dependency_Injection]]"
worksheet: [WS_Testing] # Implicitly covers "Stub vs. mock vs. dummy vs. fake"
date_created: 2025-04-14
---
# Test Double (General / C and Python Contexts)

## Definition

A **Test Double** is a generic term (coined by Gerard Meszaros) for any object or component created specifically for testing purposes to replace a real production dependency (a "real" object) that the system or unit under test interacts with. Test doubles are used to isolate the unit under test, make tests faster and more reliable, control dependencies' behavior, and enable verification of interactions.

## Purpose

- **Isolation:** Allow the unit under test (UUT) to be tested independently of its real dependencies. This ensures test failures are due to issues in the UUT, not its collaborators.
- **Control:** Provide control over the behavior of dependencies during a test (e.g., force error conditions, return specific values).
- **Speed & Reliability:** Replace slow or unreliable dependencies (e.g., network services, databases) with fast, predictable doubles.
- **Verification:** Enable verification of how the UUT interacts with its dependencies (especially with [[Mocks]] and [[Spies]]).
- **Availability:** Allow testing even when real dependencies are unavailable or not yet implemented.

## Types of Test Doubles

Common types include (definitions vary slightly between sources):

1.  **[[Dummies|Dummy]]:** Objects passed around but never actually used. Their methods might not even be implemented (e.g., just throw exceptions or do nothing). Used solely to satisfy parameter lists.
2.  **[[Fakes|Fake]]:** Objects with working implementations, but simplified for testing, not suitable for production. They often substitute complex dependencies with simpler versions (e.g., an in-memory database instead of a real SQL server, providing the same API but without persistence or complex features).
3.  **[[Stubs|Stub]]:** Provide predefined ("canned") answers to calls made during the test. They don't respond dynamically to interactions. Used primarily to provide necessary state or return values to the UUT.
4.  **[[Spies|Spy]]:** Stubs that also record some information about how they were called (e.g., number of calls, arguments passed). This information can be checked by the test after the UUT is exercised. Spies offer a middle ground between stubs and mocks.
5.  **[[Mocks|Mock]]:** Objects pre-programmed with expectations about the calls they should receive during the test. The test verifies *against the mock* whether these expected interactions occurred correctly. Focuses on behavior verification.

## Implementation in C

Since C lacks built-in object orientation and dynamic dispatch features common in higher-level languages, implementing test doubles often involves techniques like:

- **[[Function_Pointer_C|Function Pointers]]:** Replacing direct function calls with calls through function pointers, allowing the pointers to be redirected to stub/mock functions during tests.
- **Linker Seams / Weak Symbols:** Using [[Weak_Symbol_C|weak symbols]] or linker tricks to substitute test implementations for real ones at link time.
- **Conditional Compilation (`#ifdef`):** Compiling different versions of a dependency function based on whether a test build is being performed (can become complex to manage).
- **Manual Implementation:** Writing specific stub/fake functions manually for each test scenario.
- **C Mocking Frameworks:** Libraries like CMocka, Google Mock (for C++ but can sometimes interface with C), or Unity/CMock provide tools to automate the creation of mocks and stubs for C code.

## Implementation in Python

Python’s dynamic nature and rich ecosystem make implementing test doubles more straightforward compared to C. Common techniques and tools include:

- **Manual Implementation:** Creating simple classes or functions that mimic the behavior of the dependency. For example, a `FakeDatabase` class with simplified logic can replace a real database connection.
- **Monkey Patching:** Dynamically replacing a function or method at runtime using Python’s dynamic capabilities (e.g., `module.function = fake_function`).
- **Dependency Injection:** Passing test doubles explicitly to the unit under test, often via constructor or function arguments, facilitated by Python’s flexible argument passing.
- **Python Mocking Libraries:**
  - **`unittest.mock`:** Python’s standard library provides the `unittest.mock` module, which includes `Mock` and `MagicMock` classes for creating mocks, stubs, and spies. You can patch dependencies, set return values, and verify calls.
    - Example: `from unittest.mock import Mock; db = Mock(); db.query.return_value = [1, 2, 3]` creates a mock database that returns `[1, 2, 3]` when `query()` is called.
  - **`pytest-mock`:** A pytest plugin that integrates `unittest.mock` with pytest, providing a `mocker` fixture for easier mocking.
  - **`responses`:** A library for mocking HTTP requests, useful for faking network-dependent code.
- **Example with `unittest.mock`:**
  ```python
  from unittest.mock import Mock

  # Real dependency
  class RealDatabase:
      def query(self, sql):
          return [1, 2, 3]  # Simulate a real DB query

  # Unit under test
  class DataProcessor:
      def __init__(self, db):
          self.db = db
      def process(self):
          data = self.db.query("SELECT * FROM table")
          return [x * 2 for x in data]

  # Test with a mock
  mock_db = Mock()
  mock_db.query.return_value = [4, 5, 6]  # Predefined response
  processor = DataProcessor(mock_db)
  result = processor.process()
  assert result == [8, 10, 12]  # Verify behavior
  mock_db.query.assert_called_once_with("SELECT * FROM table")  # Verify interaction