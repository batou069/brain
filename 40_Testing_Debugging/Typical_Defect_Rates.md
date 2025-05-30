---
tags:
  - testing
  - concept
  - metric
  - quality
  - benchmark
aliases:
  - Industry Defect Rates
related:
  - Defect_Rate
  - Error_Density
  - Software_Testing
  - Quality_Assurance
worksheet:
  - WS_Testing
date_created: 2025-04-14
---
# Typical Defect Rates

## Definition

**Typical Defect Rates** refer to industry benchmarks or commonly observed ranges for [[Defect_Rate|defect rates]] or [[Error_Density|defect densities]] found in software during different phases of development or after release. These figures provide a rough point of comparison but vary significantly based on numerous factors.

## Factors Influencing Defect Rates

Defect rates are **highly variable** and depend heavily on:

- **Industry/Domain:** Safety-critical systems (avionics, medical) aim for extremely low rates compared to consumer web applications.
- **Development Process Maturity:** Organizations with mature processes (e.g., strong code reviews, automated testing, experienced teams) tend to have lower rates.
- **Testing Rigor & Phase:** More defects are typically found during intensive testing phases (System Test, Integration Test) than during early development or after release. Post-release defect rates are usually much lower (but defects found are often more critical or expensive).
- **Complexity of Software:** More complex software naturally tends to have more potential for defects.
- **Team Experience & Skills:** Developer and tester experience impacts quality.
- **Technology Stack:** Language, frameworks, and tools used can influence defect introduction.
- **Definition of "Defect":** How defects are classified (e.g., severity, type) affects reported rates.
- **Measurement Unit:** Rates per KLOC vs. Function Point vs. time yield different numbers.

## General (Highly Approximate) Benchmarks

>[!warning] Use with Extreme Caution
> These are very rough, generalized figures often cited, but real-world results vary enormously. Do not treat these as absolute targets.

- **Industry Average (Pre-Release):** Often cited in the range of **1 to 25 defects per KLOC** found during development and testing phases. Lower end for high-maturity organizations, higher end for less mature ones or complex systems. Some sources cite averages around 10-15 defects/KLOC.
- **Microsoft Applications (Historically):** Often cited around 10-20 defects/KLOC during internal testing.
- **NASA / Space Shuttle Software:** Aimed for extremely low rates, perhaps less than 0.1 defects/KLOC after rigorous verification and validation.
- **Post-Release:** Defect rates found by users after release are typically much lower, often measured in defects per user, per month, or per year, and ideally should be very low (e.g., < 1 defect/KLOC remaining).

## Purpose

- **Benchmarking:** Provides a rough comparison point for an organization's own quality levels.
- **Goal Setting (with caution):** Can inform realistic quality goals, but should be adapted to the specific project context.
- **Process Improvement:** Significant deviation from expected ranges might indicate areas for process improvement (either in development or testing).

## Related Concepts
- [[Defect_Rate]], [[Error_Density]] (The metrics being discussed)
- [[Software_Testing]], [[Quality_Assurance]]
- [[KLOC]], [[Function_Points]] (Units of measurement)

---
**Source:** Worksheet WS_Testing, Various industry studies and software engineering literature (e.g., Capers Jones, Steve McConnell) - specific numbers vary widely.