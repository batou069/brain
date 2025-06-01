---
tags:
  - mathematics
  - functions
  - special_functions
  - gamma_function
  - factorial
  - combinatorics
  - statistics
  - concept
aliases:
  - Euler's Gamma Function
  - Γ(z)
related:
  - "[[_Functions_MOC]]"
  - "[[Factorial]]"
  - "[[Calculus_Integrals]]"
  - "[[Probability_Distribution]]"
worksheet:
  - WS_Math_Foundations_1
date_created: 2025-05-30
---
# Gamma Function ($\Gamma(z)$)

## Definition
The **Gamma function**, denoted by $\Gamma(z)$ (Greek capital letter Gamma), is an extension of the [[Factorial|factorial function]] to complex and real numbers (though typically introduced with real arguments $z > 0$). For a complex number $z$ with a positive real part, it is defined by a convergent improper integral:

$$ \Gamma(z) = \int_{0}^{\infty} t^{z-1} e^{-t} \,dt \quad \text{for } \text{Re}(z) > 0 $$

This definition can be extended to all complex numbers except non-positive integers ($0, -1, -2, \dots$) by analytic continuation.

## Relationship to Factorial
A key property of the Gamma function is its relationship with the factorial function:
For any positive integer $n$:
$$ \Gamma(n) = (n-1)! $$
This means:
- $\Gamma(1) = 0! = 1$
- $\Gamma(2) = 1! = 1$
- $\Gamma(3) = 2! = 2$
- $\Gamma(4) = 3! = 6$
And so on. This shows that the Gamma function interpolates the factorial function.

This can be derived using integration by parts, which also yields the fundamental recurrence relation:
$$ \Gamma(z+1) = z \Gamma(z) $$
If $z=n$ (a positive integer), then $\Gamma(n+1) = n \Gamma(n) = n (n-1)! = n!$.

## Properties
- **Recurrence Relation:** $\Gamma(z+1) = z \Gamma(z)$
- **Value at $\frac{1}{2}$:** A notable value is $\Gamma\left(\frac{1}{2}\right) = \sqrt{\pi}$.
  Using the recurrence relation:
  $\Gamma\left(\frac{3}{2}\right) = \frac{1}{2} \Gamma\left(\frac{1}{2}\right) = \frac{\sqrt{\pi}}{2}$
  $\Gamma\left(\frac{5}{2}\right) = \frac{3}{2} \Gamma\left(\frac{3}{2}\right) = \frac{3\sqrt{\pi}}{4}$
- **Poles:** The Gamma function has simple poles at $z = 0, -1, -2, \dots$ (non-positive integers), and is analytic everywhere else.
- **Reflection Formula (Euler's reflection formula):**
  $$ \Gamma(z) \Gamma(1-z) = \frac{\pi}{\sin(\pi z)} \quad \text{for non-integer } z $$
- **No Zeros:** $\Gamma(z)$ is never zero.
- **Log-convexity:** The Gamma function is logarithmically convex for positive real $z$.

## Graph for Real Positive Values

```mermaid
graph TD
    subgraph GammaGraph["Graph of Γ(x) for x > 0"]
        XAxis["x-axis (0 to 5)"] --- YAxis["y-axis (0 to 25)"]
        P0_plus((0, "+∞ (pole)"))
        P1((1,1))
        P2((2,1))
        P3((3,2))
        P4((4,6))
        P5((5,24))
        Minima((approx 1.46, approx 0.8856))

        P0_plus -.-> Minima --- P1 --- P2 --- P3 --- P4 --- P5 % Curve path
    end
    note right of P0_plus : Pole at x=0
    note right of P1 : Γ(1)=0!=1
    note right of P2 : Γ(2)=1!=1
    note right of P3 : Γ(3)=2!=2
    note right of P4 : Γ(4)=3!=6
    note right of P5 : Γ(5)=4!=24
    
    style P1 fill:#afa,stroke:#333,stroke-width:2px
    style P2 fill:#afa,stroke:#333,stroke-width:2px
    style P3 fill:#afa,stroke:#333,stroke-width:2px
    style P4 fill:#afa,stroke:#333,stroke-width:2px
    style P5 fill:#afa,stroke:#333,stroke-width:2px
    style Minima fill:#aaf,stroke:#333,stroke-width:2px
    linkStyle 6 stroke-width:2px,fill:none,stroke:blue;
```
The function decreases from $+\infty$ at $x=0^+$ to a minimum around $x \approx 1.4616$ (where $\Gamma(x) \approx 0.8856$) and then increases.

## Why is there more than one Gamma function?

>[!question] Why is there more than one Gamma function?
>This question might be slightly misleading. There is essentially **one standard Gamma function**, $\Gamma(z)$, as defined by Euler.
>
>However, related functions exist, or the term "gamma function" might appear in different contexts:
>1.  **Incomplete Gamma Functions:**
>    - **Lower Incomplete Gamma Function:** $\gamma(s, x) = \int_0^x t^{s-1} e^{-t} \,dt$
>    - **Upper Incomplete Gamma Function:** $\Gamma(s, x) = \int_x^\infty t^{s-1} e^{-t} \,dt$
>    Note that $\gamma(s,x) + \Gamma(s,x) = \Gamma(s)$. These are "incomplete" because the integration is not over the full range $(0, \infty)$. They appear in probability distributions (e.g., the CDF of the Gamma distribution uses the lower incomplete Gamma function).
>2.  **Multivariate Gamma Function:** Generalizes the Gamma function to multiple variables, used in multivariate statistics.
>3.  **Log-Gamma Function ($\ln \Gamma(z)$):** Often used for numerical stability when $\Gamma(z)$ values become very large.
>4.  **Digamma and Polygamma Functions:** These are derivatives of the log-gamma function:
>    - Digamma function: $\psi(z) = \frac{d}{dz} \ln \Gamma(z) = \frac{\Gamma'(z)}{\Gamma(z)}$
>    - Polygamma functions: $\psi^{(n)}(z)$ (higher derivatives).
>
>So, while there's one primary Gamma function, its name is lent to these related mathematical constructs. The prompt might be referring to these variations or possibly historical alternative definitions that are now less common.

## How are Gamma functions useful in combinatorics?

>[!question] How are Gamma functions useful in combinatorics?
>The primary link to combinatorics is through the Gamma function's generalization of the [[Factorial|factorial]]: $\Gamma(n+1) = n!$. Factorials are fundamental in combinatorics for counting permutations and combinations.
>
>1.  **Generalizing Combinatorial Formulas:** Many combinatorial formulas involve factorials. The Gamma function allows these formulas to be extended to non-integer arguments, which is particularly useful in probability and statistics where parameters might be continuous.
>    - **Binomial Coefficient:** $\binom{n}{k} = \frac{n!}{k!(n-k)!}$. This can be generalized using Gamma functions:
>      $$ \binom{x}{y} = \frac{\Gamma(x+1)}{\Gamma(y+1)\Gamma(x-y+1)} $$
>      This generalized binomial coefficient appears in various contexts, including the definition of the Beta function and Beta distribution.
>
>2.  **Connection to Beta Function:** The Beta function, $B(x,y)$, is also important in probability (e.g., Beta distribution, prior for binomial proportions) and is defined using Gamma functions:
>    $$ B(x,y) = \frac{\Gamma(x)\Gamma(y)}{\Gamma(x+y)} = \int_0^1 t^{x-1}(1-t)^{y-1} \,dt $$
>
>3.  **Volume of n-balls:** The volume of an n-dimensional ball of radius $R$ is given by:
>    $$ V_n(R) = \frac{\pi^{n/2}}{\Gamma(\frac{n}{2} + 1)} R^n $$
>    This formula, appearing in geometry and physics, uses the Gamma function to handle both even and odd dimensions smoothly.
>
>4.  **Analytic Combinatorics:** In more advanced combinatorics, generating functions are used to count objects. The analytic properties of these generating functions, which can involve Gamma functions (especially via Stirling's approximation for factorials/Gamma functions for large arguments), are used to derive asymptotic formulas for counts.
>    Stirling's Approximation: $\Gamma(z+1) \sim \sqrt{2\pi z} \left(\frac{z}{e}\right)^z$ for large $|z|$.

While direct combinatorial counting usually involves integers and thus factorials, the Gamma function provides the continuous mathematical framework that underpins and extends these discrete concepts, especially when bridging to continuous probability or analyzing asymptotic behavior.

## Applications
- **Probability and Statistics:**
    - **Gamma Distribution:** $f(x; k, \theta) = \frac{x^{k-1}e^{-x/\theta}}{\theta^k \Gamma(k)}$, used to model waiting times, rainfall, etc.
    - **Beta Distribution:** Used to model probabilities, defined using Beta functions (which in turn use Gamma functions).
    - **Chi-squared Distribution:** A special case of the Gamma distribution. Its PDF involves $\Gamma(k/2)$.
    - **Student's t-distribution and F-distribution:** Their PDFs also involve Gamma functions.
- **Analytic Number Theory:** Appears in connection with the Riemann zeta function and other L-functions.
- **Physics and Engineering:** String theory, quantum field theory, fluid dynamics (e.g., in solutions to certain differential equations).
- **Calculus:** Evaluating certain definite integrals.

## Example Calculation using Recurrence
Calculate $\Gamma(3.5)$:
$\Gamma(3.5) = \Gamma(2.5 + 1) = 2.5 \cdot \Gamma(2.5)$
$\Gamma(2.5) = \Gamma(1.5 + 1) = 1.5 \cdot \Gamma(1.5)$
$\Gamma(1.5) = \Gamma(0.5 + 1) = 0.5 \cdot \Gamma(0.5)$
We know $\Gamma(0.5) = \Gamma\left(\frac{1}{2}\right) = \sqrt{\pi}$.
So, $\Gamma(1.5) = 0.5 \sqrt{\pi} = \frac{\sqrt{\pi}}{2}$.
$\Gamma(2.5) = 1.5 \cdot \frac{\sqrt{\pi}}{2} = \frac{3\sqrt{\pi}}{4}$.
$\Gamma(3.5) = 2.5 \cdot \frac{3\sqrt{\pi}}{4} = \frac{5}{2} \cdot \frac{3\sqrt{\pi}}{4} = \frac{15\sqrt{\pi}}{8}$.
$\frac{15\sqrt{\pi}}{8} \approx \frac{15 \times 1.77245}{8} \approx \frac{26.58675}{8} \approx 3.3233$.

---