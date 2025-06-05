---
tags:
  - testing
  - concept
  - technique
  - test_double
  - isolation
aliases:
  - Test Dummy
related:
  - "[[Test_Double_C]]"
  - "[[Stubs]]"
  - "[[Mocks]]"
  - "[[Fakes]]"
  - "[[Spies]]"
  - "[[Unit_Test]]"
worksheet:
  - WS_Testing
date_created: 2025-04-20
---
# Dummies (Test Doubles)

## Definition

A **Dummy** object is the simplest type of [[Test_Double_C]]. It is an object that is passed around to satisfy parameter lists or dependencies but is **never actually used** or relied upon during the specific test case. Its methods are often not implemented or might just throw exceptions if called unexpectedly.

## Purpose

- **Fill Parameter Lists:** Satisfy the type requirements for method or constructor arguments when the argument itself is irrelevant to the behavior being tested in that specific scenario.
- **Placeholder:** Act as a minimal placeholder for a required dependency when no interaction or return value from that dependency is needed for the test.

## Example Scenario

Imagine testing a function `process_user(user_object, logger_object)` where the test specifically verifies logic related to the `user_object` and doesn't care about logging in this particular test case.

- **Unit Under Test:** `process_user`
- **Dependency:** `logger_object`
- **Dummy:** A dummy `logger_object` could be passed in. It might have the required logging methods (e.g., `log_info`, `log_error`), but these methods would do nothing or throw an error if called, as this test doesn't expect them to be invoked.

```c
// Conceptual C Dummy Logger
typedef struct { /* No state needed */ } DummyLogger;

void dummy_log_info(DummyLogger* logger, const char* msg) { /* Do nothing */ }
void dummy_log_error(DummyLogger* logger, const char* msg) { /* Do nothing */ }

// In Test:
// DummyLogger dummy_log;
// User user_to_test;
// process_user(&user_to_test, &dummy_log); // Pass dummy, its methods aren't called/verified```

## Related Concepts
- [[Test_Double_C]] (Dummies are the simplest type)
- [[Stubs]], [[Mocks]], [[Fakes]], [[Spies]] (Other test doubles with more active roles)
- [[Unit_Test]]

---
**Source:** Worksheet WS_Testing, Gerard Meszaros' "xUnit Test Patterns"