---
tags:
  - testing
  - python
  - library
  - framework
  - unit_test
aliases:
  - unittest (Python module)
related:
  - "[[Python]]"
  - "[[Unit_Test]]"
  - "[[Test_Framework]]"
  - "[[Pytest]]"
  - "[[Doctest]]"
  - "[[Assertions]]"
  - "[[setUp_tearDown]]"
  - "[[Test_Case]]"
  - "[[Test_Suite]]"
  - "[[Test_Runner]]"
worksheet:
  - WS24
date_created: 2025-04-20
---
# PyUnit (`unittest` module)

## Definition

**PyUnit**, more commonly known as the **`unittest`** module, is the standard **unit testing framework** included in the Python standard library. It is inspired by JUnit (from the Java world) and provides a framework for organizing, executing, and reporting on [[Unit_Test|unit tests]] in an object-oriented way.

## Key Concepts & Components

1.  **Test Case (`unittest.TestCase`):**
    -   The fundamental building block. Tests are created by subclassing `unittest.TestCase`.
    -   Individual test methods within the class must start with the prefix `test_` (e.g., `def test_addition(self):`).
    -   Provides various assertion methods (`self.assertEqual()`, `self.assertTrue()`, `self.assertRaises()`, etc.) to check conditions and report failures. See [[Assertions]].

2.  **Test Fixture (`setUp` / `tearDown`):**
    -   Mechanisms for setting up preconditions before a test runs and cleaning up afterwards.
    -   `setUp(self)`: Method called immediately *before* each individual `test_` method runs. Used for creating resources needed by tests.
    -   `tearDown(self)`: Method called immediately *after* each individual `test_` method runs, regardless of whether the test passed or failed. Used for cleaning up resources.
    -   Class-level fixtures (`setUpClass()`, `tearDownClass()`) are also available for setup/teardown performed once per test class. See [[setUp_tearDown]].

3.  **Test Suite (`unittest.TestSuite`):**
    -   A collection of test cases, test suites, or both. Used to aggregate tests that should be executed together.

4.  **Test Runner:**
    -   A component responsible for executing tests and reporting results (e.g., text-based runner, graphical runners).
    -   The `unittest` module provides basic runner capabilities, often invoked from the command line.

5.  **Test Discovery:**
    -   `unittest` includes a test discovery mechanism (often run via `python -m unittest discover`) that can automatically find test modules and classes within a project structure.

## Basic Structure Example

```python
# test_calculator.py
import unittest
from my_calculator import Calculator # Assume this module exists

class TestCalculator(unittest.TestCase):

    def setUp(self):
        """Set up for test methods."""
        print("\nRunning setUp")
        self.calc = Calculator()

    def tearDown(self):
        """Tear down for test methods."""
        print("Running tearDown")
        del self.calc

    def test_addition(self):
        """Test add functionality"""
        print("Running test_addition")
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtraction(self):
        """Test subtract functionality"""
        print("Running test_subtraction")
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_error_on_non_numeric(self):
        """Test that add raises TypeError for non-numeric input"""
        print("Running test_error_on_non_numeric")
        # Use assertRaises as a context manager
        with self.assertRaises(TypeError):
            self.calc.add("a", 3)
        with self.assertRaises(TypeError):
            self.calc.add(2, "b")

# Allows running the tests directly using 'python test_calculator.py'
if __name__ == '__main__':
    unittest.main()

```

## Running Tests

```bash
# Run tests in a specific file
python -m unittest test_calculator.py

# Discover and run all tests in the current directory (and subdirectories)
# Looks for files named test*.py by default
python -m unittest discover
```

## Related Concepts
- [[Python]], [[Unit_Test]], [[Test_Framework]]
- [[Pytest]], [[Doctest]] (Alternative Python testing frameworks/tools)
- [[Assertions]] (Methods like `assertEqual`, `assertTrue`, `assertRaises`)
- [[setUp_tearDown]] (Test fixtures)
- [[Test_Case]], [[Test_Suite]], [[Test_Runner]], Test Discovery

---
**Source:** Worksheet WS24, Python `unittest` documentation