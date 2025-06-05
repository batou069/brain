---
tags:
  - testing
  - concept
  - technique
  - test_double
  - isolation
  - interaction
aliases:
  - Test Mock
  - Mock Objects
related:
  - Test_Double_C
  - Stubs
  - Dummies
  - Fakes
  - Spies
  - Unit_Test
  - Integration_Test
  - Behavior_Verification
  - TDD
  - BDD
worksheet:
  - WS_Testing
  - WS24
date_created: 2025-04-14
---
# Mocks (Test Doubles)

## Definition

In [[Software_Testing]], a **Mock** (or Mock Object) is a type of **Test Double** ([[Test_Double]]) used to replace a real component (a dependency) that the unit under test interacts with. Mocks are configured with **expectations** about how they will be called by the unit under test during the test execution. The test then verifies that these expected interactions actually occurred. Mocks are primarily used for **behavior verification**.

## Key Aspects / Characteristics

- **Purpose:** Verify the *interaction* between the unit under test and its dependencies. Ensure the unit calls the correct methods on its collaborators, with the right arguments, in the expected order.
- **Behavior:** Configured with expectations *before* the unit under test is executed. These expectations define the calls the mock anticipates receiving.
- **Interaction Verification:** After the unit under test runs, the test framework asks the mock object to verify that all expected calls were made (and potentially that no unexpected calls occurred). The test passes or fails based on this verification.
- **State vs. Behavior:** While [[Stubs]] focus on providing state (return values) to the unit under test, Mocks focus on verifying the *behavior* (the sequence and content of outgoing calls) of the unit under test towards its dependencies.
- **Frameworks:** Mocking is typically done using specialized mocking frameworks (e.g., `unittest.mock` in Python, Mockito/EasyMock for Java, Moq/NSubstitute for .NET, Google Mock for C++) which simplify the creation and verification of mock objects.

## Example Scenario

Imagine testing an `OrderProcessor` class that, when processing an order, needs to call a `Notifier` dependency to send a confirmation email.

- **Unit Under Test:** `OrderProcessor`
- **Dependency:** `Notifier` (with a method like `send_confirmation(email_address, order_details)`)
- **Mock:** A mock object replacing the real `Notifier`.
- **Test:**
    1.  Create a mock `Notifier` object.
    2.  **Set Expectation:** Configure the mock to expect *exactly one* call to `send_confirmation` with specific `email_address` and `order_details` arguments.
    3.  Create an `OrderProcessor` instance, injecting the mock `Notifier`.
    4.  Call the `process_order` method on the `OrderProcessor`.
    5.  **Verify:** Ask the mock `Notifier` to verify that the expected call(s) occurred. The test passes if the verification succeeds, fails otherwise.

This test verifies that `OrderProcessor` correctly interacts with the `Notifier`, without actually sending an email.

## Related Concepts
- [[Test_Double]] (Category that includes Mocks)
- [[Stubs]] (Test doubles focused on providing state/return values)
- [[Dummies]], [[Fakes]], [[Spies]]
- [[Unit_Test]], [[Integration_Test]] (Where mocks are used)
- Behavior Verification (The goal of using mocks)
- Mocking Frameworks (`unittest.mock`, Mockito, Google Mock, etc.)
- Dependency Injection

## Questions / Further Study
>[!question] Stub vs. Mock vs. Dummy vs. Fake? (WS_Testing)
> See [[Stubs]]. Mocks verify *interactions/behavior*, while Stubs provide *state/canned responses*.

>[!question] Give an example of when it's preferable to use a mock object in your test. (WS24)
> It's preferable to use a mock object when you need to verify that the unit under test correctly **interacts** with its dependency, rather than just testing the unit's state change based on the dependency's return value. Examples:
> - **Verifying Notifications:** Ensuring a notification service is called exactly once with the correct message when an event occurs.
> - **Verifying Logging:** Ensuring specific log messages are written via a logging dependency under certain conditions.
> - **Verifying Transactions:** Ensuring methods like `begin_transaction`, `commit`, or `rollback` are called correctly on a transaction manager dependency.
> - **Verifying API Calls:** Ensuring an external API (like payment gateway) is called with the correct parameters.
> In these cases, the *act of calling* the dependency (and the arguments used) is the crucial behavior being tested, making a mock the appropriate tool.

---
**Source:** Worksheet WS_Testing, WS24, Martin Fowler's "Mocks Aren't Stubs"