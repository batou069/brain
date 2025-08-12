---
tags:
  - testing
  - concept
  - artifact
  - data
aliases:
  - Test Data
related:
  - Test_Case
  - Automation_Testing
  - Data_Driven_Testing
worksheet:
  - WS_Testing
date_created: 2025-04-14
---
# Test Data Files

## Definition

**Test Data Files** are external files containing input data used to drive [[Test_Case|test cases]], particularly in automated testing scenarios. Separating test data from the test logic (scripts or code) allows for easier maintenance, scalability, and the ability to run the same test logic with multiple data sets.

## Key Aspects / Characteristics

- **External Storage:** Data (inputs and sometimes expected outputs) is stored outside the test script/code itself.
- **Formats:** Can be stored in various formats, such as:
    - CSV (Comma Separated Values)
    - JSON
    - YAML
    - XML
    - Plain text files
    - Spreadsheets (Excel)
    - Database tables
- **Data-Driven Testing:** Enables Data-Driven Testing, where a single test script executes multiple times, each time using a different row or record of data from the external file as input.
- **Maintainability:** Easier to add, remove, or modify test data without changing the test execution code.
- **Scalability:** Allows testing with large volumes of data or numerous combinations.
- **Reusability:** Data sets can potentially be reused across different test cases or test suites.
- **Readability:** Can make test scenarios clearer by separating complex data setup from the test steps.

## Examples / Use Cases

- **Login Testing:** A CSV file containing rows of username/password combinations (valid, invalid, boundary cases) and expected outcomes (success, specific error message). An automated test script reads each row and attempts login.
- **API Testing:** A JSON file defining different request payloads and expected response codes/bodies for an API endpoint.
- **Calculation Engine:** An Excel file with columns for inputs and a column for the expected calculated result.
- **Boundary Value Testing:** A file listing minimum, maximum, just inside/outside boundary values for a specific input field.

## Related Concepts
- [[Test_Case]] (Test data provides inputs/expected outputs for test cases)
- [[Automation_Testing]] (Test data files are heavily used in automation)
- [[Data_Driven_Testing]] (The approach enabled by external test data)
- [[Test_Data_Generation]] (Process of creating appropriate test data - *Implied*)

---
**Source:** Worksheet WS_Testing