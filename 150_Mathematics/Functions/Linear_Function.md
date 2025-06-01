---
tags:
  - mathematics
  - functions
  - algebra
  - linear_function
  - polynomial
  - concept
aliases:
  - Linear Equation
  - Straight Line Function
related:
  - "[[_Functions_MOC]]"
  - "[[Polynomials]]"
  - "[[Calculus_Derivatives]]"
  - "[[Slope_Intercept_Form]]"
  - "[[Point_Slope_Form]]"
worksheet:
  - WS_Math_Foundations_1
date_created: 2025-05-30
---
# Linear Function

## Definition
A **linear function** is a [[Polynomials|polynomial function]] of degree one or zero. Its graph in the Cartesian coordinate system is a straight line.

A linear function in one variable $x$ can be written in the **[[Slope_Intercept_Form|slope-intercept form]]**:
$$ f(x) = mx + b $$
or equivalently $y = mx + b$, where:
- $m$ is the **slope** of the line. It represents the rate of change of $y$ with respect to $x$. For every one unit increase in $x$, $y$ increases by $m$ units (if $m>0$) or decreases by $|m|$ units (if $m<0$).
- $b$ is the **y-intercept**. It is the value of $y$ when $x=0$, i.e., the point $(0,b)$ where the line crosses the y-axis.

If $m=0$, the function becomes $f(x) = b$, which is a **constant function** (a polynomial of degree zero). Its graph is a horizontal line.

## Other Forms of Linear Equations

1.  **[[Point_Slope_Form|Point-Slope Form]]:**
    Given a point $(x_1, y_1)$ on the line and the slope $m$:
    $$ y - y_1 = m(x - x_1) $$

2.  **Standard Form:**
    $$ Ax + By = C $$
    where $A, B, C$ are constants. If $B \neq 0$, this can be rewritten in slope-intercept form as $y = -\frac{A}{B}x + \frac{C}{B}$.
    - If $B=0$ (and $A \neq 0$), the equation becomes $Ax=C$ or $x = C/A$, which represents a **vertical line**. A vertical line is *not* a function of $x$ because one x-value maps to infinitely many y-values (it fails the vertical line test). However, it is a linear equation.
    - If $A=0$ (and $B \neq 0$), the equation becomes $By=C$ or $y = C/B$, a horizontal line (constant function).

## Properties
- **Graph:** A straight line.
- **Domain:** $(-\infty, \infty)$ (all real numbers).
- **Range:**
    - $(-\infty, \infty)$ if $m \neq 0$.
    - $\{b\}$ (a single value) if $m = 0$ (constant function).
- **[[Calculus_Derivatives|Derivative]]:** The derivative of $f(x) = mx+b$ is $f'(x) = m$. This means the slope (rate of change) is constant everywhere.
- **[[Calculus_Integrals|Integral]]:** $\int (mx+b) \,dx = \frac{1}{2}mx^2 + bx + C$.

## Slope ($m$)
The slope $m$ can be calculated from any two distinct points $(x_1, y_1)$ and $(x_2, y_2)$ on the line:
$$ m = \frac{\text{change in } y}{\text{change in } x} = \frac{y_2 - y_1}{x_2 - x_1} $$
- If $m > 0$: The line slopes upwards from left to right (increasing function).
- If $m < 0$: The line slopes downwards from left to right (decreasing function).
- If $m = 0$: The line is horizontal (constant function).
- If the line is vertical: The slope is undefined (division by zero as $x_2 - x_1 = 0$).

## Visualization ($y = 2x + 1$)

```mermaid
graph TD
    subgraph LinearGraph["Graph of y = 2x + 1"]
        XAxis["x-axis (-2 to 2)"] --- YAxis["y-axis (-3 to 5)"]
        
        P0((0,1)) % y-intercept
        P1((1,3))
        Pneg1((-1,-1))
        
        Pneg1 --- P0 --- P1 % Line path
        
        note right of P0 : y-intercept b=1
        note right of P1 : Slope m = (3-1)/(1-0) = 2
    end

    style P0 fill:#afa,stroke:#000,stroke-width:2px
    style P1 fill:#aaf,stroke:#000,stroke-width:1px
    style Pneg1 fill:#aaf,stroke:#000,stroke-width:1px
    linkStyle 2 stroke:blue,stroke-width:2px;
```

## Applications
Linear functions are fundamental and widely used due to their simplicity and ability to model or approximate many real-world phenomena:
- **Direct Proportionality:** If $b=0$, then $y=mx$, meaning $y$ is directly proportional to $x$.
- **Physics:**
    - Distance-time relationship for constant velocity: $d = vt + d_0$.
    - Ohm's Law: $V = IR$ (Voltage = Current $\times$ Resistance, if R is constant).
    - Hooke's Law for springs: $F = kx$ (Force = spring constant $\times$ displacement).
- **Economics and Finance:**
    - Simple interest calculations.
    - Cost functions (e.g., Total Cost = Fixed Cost + Variable Cost $\times$ Quantity).
    - Supply and demand curves (often modeled as linear in introductory economics).
- **Data Analysis and Statistics:**
    - **Linear Regression:** Finding the best-fitting straight line to describe the relationship between two variables. This is a cornerstone of statistical modeling.
    - Linear interpolation and extrapolation.
- **Computer Science:**
    - Linear time complexity $O(n)$ for algorithms.
- **Everyday Life:**
    - Conversion formulas (e.g., Celsius to Fahrenheit: $F = \frac{9}{5}C + 32$).
    - Calculating costs based on per-unit