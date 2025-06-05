---
tags:
  - testing
  - python
  - library
  - framework
  - unit_test
  - integration_test
aliases:
  - pytest framework
related:
  - "[[Python]]"
  - "[[Unit_Test]]"
  - "[[Integration_Test]]"
  - "[[Test_Framework]]"
  - "[[PyUnit]]"
  - "[[Doctest]]"
  - "[[Assertions]]"
  - "[[Test_Fixtures_Pytest]]" # Placeholder for pytest fixtures
  - "[[Test_Discovery]]"
worksheet: [WS24]
date_created: 2025-04-21
---
# Pytest

## Definition

**Pytest** is a popular, mature, and feature-rich third-party testing framework for [[Python]]. It allows writing tests ranging from simple [[Unit_Test|unit tests]] to complex functional and [[Integration_Test|integration tests]]. Pytest aims to make writing tests easier and more scalable compared to the built-in [[PyUnit|`unittest`]] module, using plain `assert` statements and powerful features like fixtures.

## Key Features & Advantages over `unittest`

- **Simple Assertions:** Uses the standard Python `assert` statement for checking conditions. Pytest provides detailed introspection on assertion failures, showing the values involved without requiring specific `assertX` methods (like `assertEqual`).
  ```python
  # Pytest style
  def test_addition():
      assert (1 + 1) == 2
  ```
- **Less Boilerplate:** Test functions don't need to be part of a class inheriting from `unittest.TestCase` (though class-based tests are still supported). Simple functions starting with `test_` are discovered and run.
- **Powerful [[Test_Fixtures_Pytest|Fixtures]]:** Provides a flexible and powerful fixture system using decorators (`@pytest.fixture`) for setup, teardown, and dependency injection into tests. Fixtures have explicit names, clear scope (function, class, module, session), and are easier to reuse and compose than `setUp/tearDown` methods.
- **[[Test_Discovery|Test Discovery]]:** Rich automatic discovery of test files ( `test_*.py` or `*_test.py`) and test functions/methods (`test_*`).
- **Rich Plugin Ecosystem:** Has a large number of plugins available for extending functionality (e.g., `pytest-cov` for coverage, `pytest-django` for Django integration, `pytest-xdist` for parallel execution).
- **Parameterization:** Easy to run the same test function with multiple different input/output combinations using `@pytest.mark.parametrize`.
- **Filtering:** Flexible options for selecting which tests to run based on markers, keywords, or file paths.
- **Readable Output:** Provides informative and configurable test reporting.

## Basic Structure Example

```python
# test_simple_math.py
import pytest # Usually needed for fixtures/markers, not basic asserts

def add(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise TypeError("Inputs must be numeric")
    return x + y

# Simple test function
def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2

# Test for expected exception
def test_add_type_error():
    with pytest.raises(TypeError):
        add("a", 3)

# Parameterized test
@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (0, 5, 5),
    (-1, 5, 4),
    (1.5, 2.5, 4.0)
])
def test_add_various(a, b, expected):
    assert add(a, b) == expected
```

## Running Tests

```bash
# Run all tests found in current directory and subdirectories
pytest

# Run tests in a specific file
pytest test_simple_math.py

# Run tests with a specific keyword expression
pytest -k "addition or error"

# Run tests with a specific marker
# (Add @pytest.mark.slow to a test function first)
# pytest -m slow

# Stop on first failure
pytest -x

# Verbose output
pytest -v
```

## Related Concepts
- [[Python]], [[Unit_Test]], [[Test_Framework]]
- [[PyUnit]] (Alternative standard library framework)
- [[Doctest]] (Another Python testing approach)
- [[Assertions]] (Pytest uses plain `assert`)
- [[Test_Fixtures_Pytest]] (Powerful setup/teardown mechanism)
- [[Test_Discovery]]
- Parameterization, Markers, Plugins

---
**Source:** Worksheet WS24, Pytest Documentation