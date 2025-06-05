---
tags: [testing, concept, metric, quality]
aliases: [Bug Rate, Fault Rate]
related:
  - "[[Failures_Faults_Errors]]"
  - "[[Error_Density]]"
  - "[[Software_Testing]]"
  - "[[Quality_Assurance]]"
  - "[[Typical_Defect_Rates]]"
worksheet: [WS_Testing]
date_created: 2025-04-12
---
# Defect Rate

## Definition

**Defect Rate** (also Bug Rate or Fault Rate) is a metric used in software quality assurance to measure the frequency of defects ([[Failures_Faults_Errors|faults]]) found in a software component or system relative to a standard unit of measure, typically over a specific period or development phase.

## Key Aspects / Characteristics

- **Measurement:** Quantifies the number of defects found.
- **Normalization:** Usually normalized against:
    - **Size:** Defects per KLOC (Thousand Lines of Code) or Function Point. This is often called [[Error_Density]].
    - **Time:** Defects found per testing hour, per development week/month, or per release cycle.
    - **Number of Tests:** Defects found per number of test cases executed.
- **Purpose:**
    - Track the quality of the software over time.
    - Compare the quality of different modules or projects.
    - Evaluate the effectiveness of testing or development processes.
    - Help predict the number of remaining defects or estimate release readiness (with caution).
- **Interpretation:** A high defect rate might indicate poor code quality, inadequate development practices, or very effective testing. A low defect rate might indicate high quality, ineffective testing, or that defects are clustered elsewhere. Context is crucial.
- **Trends:** Monitoring the defect rate trend (e.g., decreasing over time as testing progresses) can be more informative than absolute numbers.

## Examples / Use Cases

- "Module A had a defect rate of 5 defects per KLOC during system testing."
- "The defect rate found during User Acceptance Testing was 0.5 defects per testing day."
- "Our automated regression suite found defects at a rate of 0.01 defects per test case run this week."

## Related Concepts
- [[Failures_Faults_Errors]] (What is being counted)
- [[Error_Density]] (A specific type of defect rate normalized by size)
- [[Software_Testing]], [[Quality_Assurance]] (Context where the metric is used)
- [[Typical_Defect_Rates]] (Industry benchmarks, vary widely)
- [[Metrics]] (*Implied*)

---
**Source:** Worksheet WS_Testing