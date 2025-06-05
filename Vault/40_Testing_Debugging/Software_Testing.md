---
tags: [testing, concept, quality_assurance, core]
aliases: [Testing]
related:
  - "[[Verification]]"
  - "[[Validation]]"
  - "[[Debugging]]"
  - "[[Quality Assurance]]"
  - "[[Software Development Lifecycle]]"
worksheet: [WS_Testing] 
---
# Software Testing

## Definition

**Software Testing** is the process of evaluating and verifying that a software product or application does what it is supposed to do. It involves executing software components or systems using manual or automated tools to evaluate one or more properties of interest, primarily aimed at finding defects ([[Failures_Faults_Errors]]) and ensuring the software meets specified requirements and quality standards.

## Key Aspects / Characteristics

- **Objective:** To find defects, reduce risk, improve quality, verify requirements are met, and build confidence in the software.
- **Process:** Involves planning tests, designing [[Test_Case|test cases]], executing tests, and evaluating results.
- **Scope:** Can range from testing small individual units of code ([[Unit_Test]]) to testing integrated components ([[Integration_Test]]) and the entire system ([[System_Test]]).
- **[[Verification]] vs [[Validation]]:** Testing encompasses both verifying that the software is built correctly according to specifications and validating that it meets the user's actual needs.
- **Destructive Intent (Constructive Outcome):** While the goal is quality software, the *process* of testing often involves trying to break the software or find scenarios where it fails.
- **Not Exhaustive:** Testing can show the presence of defects, but generally cannot prove their absence (except in very simple cases). Testing aims to reduce the probability of undiscovered defects remaining. See [[Seven_Principles_of_Software_Testing]].

## Examples / Use Cases

- Running [[Unit_Test|unit tests]] to verify individual functions work as expected.
- Performing [[Integration_Test|integration tests]] to ensure different modules interact correctly.
- Executing [[Regression_Test|regression tests]] after code changes to ensure existing functionality hasn't broken.
- Conducting user acceptance testing (UAT) to validate if the software meets user needs before release.
- Using automated test scripts in a [[CI/CD]] pipeline.

## Related Concepts
- [[Seven_Principles_of_Software_Testing]]
- [[Verification]], [[Validation]]
- [[Testing_vs_Debugging]]
- [[Unit_Test]], [[Integration_Test]], [[System_Test]], [[Acceptance_Test]], [[Regression_Test]], [[Smoke_Test]]
- [[Black-box_Test]], [[White-box_Test]]
- [[Test_Case]], [[Test_Plan]], [[Test_Coverage]]
- [[Failures_Faults_Errors]]

## Questions / Further Study
>[!question] Why is testing important?
> Testing is crucial because software defects can lead to financial loss, reputational damage, security vulnerabilities, incorrect results, user frustration, and even physical harm in safety-critical systems. Testing helps mitigate these risks by identifying and enabling the correction of defects before software reaches end-users. It improves product quality, reliability, and user satisfaction.

---
**Source:** Worksheet WS_Testing, Wikipedia: Software testing