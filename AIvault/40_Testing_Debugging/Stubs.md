---
tags:
  - testing
  - concept
  - technique
  - test_double
  - isolation
aliases:
  - Test Stub
related:
  - Test_Double_C
  - Mocks
  - Dummies
  - Fakes
  - Spies
  - Unit_Test
  - Integration_Test
  - Top-down_Integration
worksheet:
  - WS_Testing
date_created: 2025-04-14
---
# Stubs (Test Doubles)

## Definition

In [[Software_Testing]], a **Stub** is a type of **Test Double** ([[Test_Double]]) used to replace a real component (a dependency) that the unit under test calls. Stubs provide predefined, canned answers to calls made during the test, ensuring the test runs predictably and focuses on the unit under test rather than its collaborators. They typically don't respond differently based on interactions; they just return configured values.

## Key Aspects / Characteristics

- **Purpose:** Provide indirect input to the unit under test by responding to its calls to dependencies. Enable testing in isolation.
- **Behavior:** Returns predefined values (e.g., hardcoded responses, configured values) when called. Does not usually contain complex logic itself.
- **State Verification:** Stubs are generally *not* used for verifying *how* the unit under test interacted with the dependency (that's more the role of [[Mocks]]). They primarily provide necessary return values or states.
- **Use Cases:**
    - Replacing a dependency that is slow (e.g., database, network service).
    - Replacing a dependency that is unavailable in the test environment.
    - Forcing specific execution paths in the unit under test by controlling the return values from dependencies.
    - Simulating error conditions from dependencies.
    - Used in [[Top-down_Integration]] testing to simulate lower-level modules that haven't been integrated yet.

## Example Scenario

Imagine testing a `calculate_order_total(order_id)` function that needs to call a `get_product_price(product_id)` function (which might involve a slow database lookup).

- **Unit Under Test:** `calculate_order_total`
- **Dependency:** `get_product_price`
- **Stub:** A test-specific implementation of `get_product_price` could be created:
  ```c
  // Conceptual Stub in C
  double stub_get_product_price(int product_id) {
      if (product_id == 101) {
          return 19.99; // Canned response for product 101
      } else if (product_id == 202) {
          return 5.00;  // Canned response for product 202
      } else {
          return 0.0;   // Default canned response
      }
  }
```


Test: The unit test for calculate_order_total would be configured to call stub_get_product_price instead of the real one. This allows testing the calculation logic within calculate_order_total quickly and reliably, regardless of the actual database state.

Related Concepts

[[Test_Double_C]] (Category that includes Stubs)

[[Mocks]] (Test doubles focused on verifying interactions)

[[Dummies]] (Passed around but never used)

[[Fakes]] (Working implementations, but simplified for testing, e.g., in-memory database)

[[Spies]] (Stubs that also record information about how they were called)

[[Unit_Test]], [[Integration_Test]] (Where stubs are used)

Dependency Injection (Technique often used to replace real dependencies with stubs/mocks)

Questions / Further Study

[!question] Stub vs. Mock vs. Dummy vs. Fake? (WS_Testing)
These are all types of [[Test_Double_C]]:

[[Dummies|Dummy]]: Objects passed around but never actually used. Usually just fill parameter lists.

[[Fakes|Fake]]: Objects with working implementations, but simplified for testing (not production-ready). E.g., an in-memory database instead of a real one.

[[Stubs|Stub]]: Provide canned answers to calls made during the test. Used for state verification (ensuring the unit under test behaves correctly given the stub's responses).

[[Mocks|Mock]]: Objects pre-programmed with expectations about which methods will be called, with what arguments, and in what order. Used for behavior verification (ensuring the unit under test interacts correctly with its dependencies). Tests typically assert against the mock object itself after the unit under test is exercised.

Spy: A stub that also records some information about how it was called (e.g., how many times, with what arguments). Allows for state verification while also providing some interaction information without demanding strict expectations upfront like a mock.

Source: Worksheet WS_Testing, Martin Fowler's "Mocks Aren't Stubs"