---
tags:
  - testing
  - concept
  - metric
  - quality
aliases:
  - Defect Density
related:
  - Defect_Rate
  - Failures_Faults_Errors
  - Software_Testing
  - Quality_Assurance
  - KLOC
  - Function_Points
worksheet:
  - WS_Testing
date_created: 2025-04-14
---
# Error Density (Defect Density)

## Definition

**Error Density**, more commonly known as **Defect Density**, is a software quality metric that measures the number of confirmed defects ([[Failures_Faults_Errors|faults]]) detected in a software component or system, normalized by the **size** of that software. It provides a measure of defect concentration relative to size.

## Key Aspects / Characteristics

- **Normalization by Size:** Unlike a simple [[Defect_Rate]] (which might be time-based), defect density specifically relates defect counts to the size of the codebase or functionality.
- **Units of Size:** Size can be measured in various ways:
    - **KLOC/SLOC:** Thousands of Lines of Code / Source Lines of Code. (Most common but can be misleading due to language differences, coding style, comments, etc.)
    - **Function Points:** A measure based on the functional complexity and features delivered to the user (more language-independent but requires specific counting methodology).
    - Number of Classes, Modules, Requirements, etc.
- **Calculation:** `Defect Density = (Total Number of Defects Found) / (Size of Software)`
- **Purpose:**
    - Compare the relative quality or defect-proneness of different modules or components within a system.
    - Track quality improvements over time or across different versions.
    - Benchmark against industry standards ([[Typical_Defect_Rates]]).
    - Help identify high-risk components that might require more testing or refactoring.
- **Interpretation:** Higher density generally indicates lower quality or higher defect-proneness *for that size*. However, a high density could also result from very thorough testing finding more defects. Context is essential.

## Examples / Use Cases

- "Module X (5 KLOC) had 25 defects found, giving a defect density of 5 defects/KLOC."
- "Module Y (10 KLOC) had 30 defects found, giving a defect density of 3 defects/KLOC. Module Y appears to have relatively higher quality or was tested less thoroughly than Module X."
- "The overall project defect density at system test entry was 2.5 defects/Function Point."

## Related Concepts
- [[Defect_Rate]] (More general term, can be time-based)
- [[Failures_Faults_Errors]] (The defects being counted)
- [[Software_Testing]], [[Quality_Assurance]] (Context where metric is used)
- [[Typical_Defect_Rates]] (Industry comparison points)
- Lines of Code (LOC), Function Points (Units of size)

---
**Source:** Worksheet WS_Testing