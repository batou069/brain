---
tags:
  - testing
  - python
  - concept
  - verification
  - debugging
aliases:
  - Assert Statements
related:
  - "[[Software_Testing]]"
  - "[[Unit_Test]]"
  - "[[PyUnit]]"
  - "[[Pytest]]"
  - "[[Test_Case]]"
  - "[[assert_C]]" # C assert macro
worksheet: [WS24]
date_created: 2025-04-21
---
# Assertions (Python Testing Context)

## Definition

In the context of Python software testing, **Assertions** are statements used within test code to **verify** that a specific condition, assumed to be true, actually *is* true at that point during test execution. If the asserted condition is true, the test continues. If the condition is false, the assertion fails, which typically causes the test case to fail immediately and report an error.

## Purpose in Testing

- **Verification:** Check if the actual outcome of an operation matches the expected outcome defined in the [[Test_Case]].
- **Failure Indication:** Provide a clear signal that the code under test is not behaving as expected.
- **Self-Validation:** Make tests self-validating; the test itself determines pass/fail status without needing manual inspection of output.

## Implementation in Python Testing Frameworks

1.  **Plain `assert` Statement (used by [[Pytest]]):**
    -   Python's built-in `assert` statement is the primary mechanism in `pytest`.
    -   Syntax: `assert <boolean_expression> [, <optional_message>]`
    -   If `<boolean_expression>` evaluates to `False`, an `AssertionError` is raised (optionally including the `<optional_message>`).
    -   `pytest` enhances `assert` by providing detailed introspection upon failure, showing the values involved in the failed expression.
    ```python
    # Pytest example
    def test_addition():
        result = 2 + 2
        assert result == 4 # Pass
        assert result > 0  # Pass
        # assert result == 5 # Fail -> AssertionError with details
    ```

2.  **`unittest.TestCase` Assertion Methods (used by [[PyUnit]]):**
    -   The `unittest` framework requires tests to inherit from `unittest.TestCase`.
    -   This base class provides a rich set of specific assertion methods starting with `assert...`.
    -   These methods check specific conditions and provide more descriptive failure messages by default.
    -   **Common `unittest` Asserts (WS24):**
        -   `assertEqual(a, b)`: Checks `a == b`.
        -   `assertNotEqual(a, b)`: Checks `a != b`.
        -   `assertTrue(x)`: Checks `bool(x)` is `True`.
        -   `assertFalse(x)`: Checks `bool(x)` is `False`.
        -   `assertIs(a, b)`: Checks `a is b` (identity).
        -   `assertIsNot(a, b)`: Checks `a is not b`.
        -   `assertIsNone(x)`: Checks `x is None`.
        -   `assertIsNotNone(x)`: Checks `x is not None`.
        -   `assertIn(a, b)`: Checks `a in b`.
        -   `assertNotIn(a, b)`: Checks `a not in b`.
        -   `assertIsInstance(a, b)`: Checks `isinstance(a, b)`.
        -   `assertNotIsInstance(a, b)`: Checks `not isinstance(a, b)`.
        -   `assertRaises(exception, callable, *args, **kwds)`: Checks that calling `callable(*args, **kwds)` raises `exception`. Can also be used as a context manager (`with self.assertRaises(TypeError): ...`).
        -   `assertAlmostEqual(a, b)`: Checks if `a` and `b` are approximately equal (for floats).
        -   `assertNotAlmostEqual(a, b)`: Checks if `a` and `b` are not approximately equal.
        -   `assertGreater(a, b)`, `assertLess(a, b)`, etc.
    ```python
    # unittest example
    import unittest
    class MyTests(unittest.TestCase):
        def test_equality(self):
            self.assertEqual(2 + 2, 4)
            self.assertTrue(5 > 3)
            with self.assertRaises(ZeroDivisionError):
                x = 1 / 0
    ```

## Assertions vs. Error Handling

- Assertions check for conditions that **should logically never be false** if the code is correct (programmer errors/bugs). They are primarily for testing and debugging.
- Error handling (e.g., `try...except` blocks) deals with **expected runtime errors** or exceptional conditions (e.g., file not found, network timeout, invalid user input) that might occur even if the code logic is correct.

## Questions / Further Study
>[!question] What are assertions used For? When not to use assertions? (WS24)
> - **Used For:** Verifying expected outcomes and internal state consistency within automated tests. Checking preconditions, postconditions, and invariants during debugging (similar to C's `assert`). Making tests self-validating.
> - **Not Used For:** Handling expected runtime errors (use `try...except`), validating user input (use standard `if` checks and provide user feedback), checking for conditions that *might* legitimately be false during normal program operation outside of a testing/debugging context. Plain `assert` statements can be disabled globally in Python (using `-O` or `-OO` flags), so they should not be relied upon for essential runtime logic or error handling in production code.

>[!question] Can you customize the assertion's message to be raised if the code returns False? (WS24)
> - **Plain `assert`:** Yes, by providing an optional second argument: `assert condition, "This condition failed because..."`. If the assertion fails, this message will be part of the `AssertionError`.
> - **`unittest` methods:** Yes, most `unittest.TestCase` assertion methods accept an optional final `msg` argument: `self.assertEqual(a, b, msg="Values are not equal!")`. This custom message will be included in the failure report.

## Related Concepts
- [[Software_Testing]], [[Unit_Test]], [[Test_Case]]
- [[PyUnit]], [[Pytest]] (Frameworks providing assertion mechanisms)
- Verification, Validation
- [[assert_C]] (Similar concept in C, but often disabled in release builds)
- Preconditions, Postconditions, Invariants

---
**Source:** Worksheet WS24, Python Documentation