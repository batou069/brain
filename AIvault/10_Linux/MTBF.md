---
tags:
  - linux
  - hardware
  - concept
  - reliability
  - testing
  - metric
aliases:
  - Mean Time Between Failures
related:
  - Reliability_Engineering
  - Failure
  - Availability
  - MTTF
  - MTTR
worksheet:
  - WS1
  - WS_Testing
date_created: 2025-04-14
---
# MTBF (Mean Time Between Failures)

## Definition

**Mean Time Between Failures (MTBF)** is a measure of the predicted elapsed time between inherent **failures** of a mechanical or electronic system during normal system operation. It represents the average time a system operates successfully before it fails *and needs repair*. MTBF is a key indicator of a system's **reliability**.

## Key Aspects / Characteristics

- **Reliability Metric:** Measures how reliable a *repairable* system is.
- **Calculation:** `MTBF = Total Operating Time / Number of Failures` over a given period.
- **Focus on Failures:** Measures time between operational failures.
- **Assumes Repair:** Implicitly assumes the system can be repaired after a failure and put back into service. For non-repairable items, Mean Time To Failure (MTTF) is often used.
- **Units:** Typically measured in hours.
- **Prediction vs. Observation:** Can be predicted based on component data or observed from operational data of deployed systems.
- **Usage:**
    - **Hardware:** Very common for hardware components (e.g., hard drives, power supplies) where manufacturers provide MTBF ratings.
    - **Software:** Can be applied to software systems, representing the average uptime between crashes or significant operational failures that require intervention (like a restart). However, software failures often stem from design faults ([[Failures_Faults_Errors]]) rather than wear-and-tear, making MTBF interpretation slightly different than for hardware. In testing, it might be tracked during long-running stability or stress tests.

## Related Concepts
- **Failure:** An event where the system stops performing its required function.
- **Reliability:** The probability that a system will perform its intended function for a specified period under stated conditions. MTBF is a measure of reliability.
- **Availability:** The probability that a system is operational and ready to perform its function when needed. Availability depends on both reliability (MTBF) and maintainability (MTTR).
- **MTTF (Mean Time To Failure):** Used for *non-repairable* systems or components. Average time until the first failure.
- **MTTR (Mean Time To Repair/Recover):** Average time taken to repair a failed system and return it to operational status.
- [[Software_Testing]] (Stability testing, stress testing can help estimate or verify MTBF).

## Calculation Example

If a fleet of 100 identical servers runs for 1000 hours each (total 100,000 operating hours) and experiences 5 failures during that time, the observed MTBF would be:
`MTBF = 100,000 hours / 5 failures = 20,000 hours`

## Notes
- A higher MTBF indicates a more reliable system (longer average time between failures).
- MTBF does *not* predict the lifespan of a component, only the average time between failures *while it is operational*.

---
**Source:** Worksheet WS1, WS_Testing