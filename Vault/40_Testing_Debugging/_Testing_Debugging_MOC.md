---
tags:
  - MOC
  - testing
  - debugging
date_created: 2025-04-12
---
      
---
tags: [MOC, testing, debugging]
date_created: 2025-04-12
---
# Testing & Debugging MOC (Map of Content)

This note serves as a central hub for all topics related to **Software Testing and Debugging**.

## Core Concepts & Principles
- [[Software_Testing]]
- [[Seven_Principles_of_Software_Testing]]
- [[Verification]] vs [[Validation]]
- [[Failures_Faults_Errors]] (Defects)
- [[Defect_Rate]]
- [[Testing_vs_Debugging]]

## Testing Levels & Types
- [[Unit_Test]]
- [[Integration_Test]]
- [[System_Test]] (*Implied, add if covered later*)
- [[Acceptance_Test]] (*Implied, add if covered later*)
- [[Regression_Test]]
- [[Progression_Tests]] (Often synonymous with new feature testing)
- [[Smoke_Test]] (Build Verification Test)

## Testing Techniques & Approaches
- [[Black-box_Test]]
- [[White-box_Test]]
- [[Equivalence_Classes]]
- [[Boundary_Value_Analysis]]
- [[Static_Analysis]]
- [[Linting]]
- [[Test-Driven_Development]] (TDD)

## Test Artifacts & Infrastructure
- [[Test_Case]]
- [[Test_Plan]]
- [[Test_Vector]]
- [[Test_Coverage]]
- [[Test_Data_Files]]
- [[Stubs]], [[Mocks]], [[Dummies]], [[Test_Double]]
- [[Emulator]] vs [[Simulator]]
- [[Service_Virtualization]]

## Metrics & Requirements
- [[Error_Density]]
- [[Typical_Defect_Rates]]
- [[MTBF]] (Mean Time Between Failures)
- [[Functional_Requirement]]
- [[Non-functional_Requirement]]

## Integration Strategies
- [[Top-down_Integration]]
- [[Bottom-up_Integration]]

## Debugging
- [[Debugging_Techniques_C]] (*Placeholder, link to specific techniques*)
- [[GDB]] (*Placeholder, add if covered*)
- [[Valgrind]] (*Placeholder, add if covered*)

## Notes in this Section

```dataview
LIST
FROM "40_Testing_Debugging"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
```