---
tags:
  - mathematics
  - geometry
  - parabola
  - focus
  - directrix
  - conic_section
  - concept
aliases:
  - Parabola Focus
  - Parabola Directrix
related:
  - "[[Parabola]]"
  - "[[Conic_Sections]]"
  - "[[Eccentricity_Conic]]"
worksheet:
  - WS_Math_Foundations_1
date_created: 2025-05-30
---
# Focus and Directrix of a Parabola

## Definition
A **[[Parabola|parabola]]** is defined geometrically as the set (locus) of all points $P$ in a plane that are equidistant from a fixed point, called the **focus** ($F$), and a fixed line, called the **directrix** ($L$).

For any point $P$ on the parabola:
$$ d(P,F) = d(P,L) $$
where $d(P,F)$ is the distance from $P$ to the focus $F$, and $d(P,L)$ is the perpendicular distance from $P$ to the directrix $L$.

The [[Eccentricity_Conic|eccentricity]] $e$ of a parabola is $e = \frac{d(P,F)}{d(P,L)} = 1$.

## Key Components and Relationships

- **Focus ($F$):** The fixed point.
- **Directrix ($L$):** The fixed line. The directrix does not contain the focus.
- **Vertex ($V$):** The point on the parabola that is midway between the focus and the directrix. It is the point where the parabola makes its sharpest turn and lies on the axis of symmetry.
- **Axis of Symmetry (or simply Axis):** The line passing through the focus and the vertex, and perpendicular to the directrix. The parabola is symmetric about this axis.
- **Parameter $p$:** The distance from the vertex to the focus is equal to the distance from the vertex to the directrix. This distance is often denoted by $|p|$. The sign of $p$ can indicate the direction of opening.

## Standard Equations and Locations

1.  **Parabola with Vertex at Origin $(0,0)$ and Axis of Symmetry along the x-axis:**
    Equation: $y^2 = 4px$
    - **Focus $F$:** $(p,0)$
    - **Directrix $L$:** $x = -p$
    - **Vertex $V$:** $(0,0)$
    - If $p > 0$, the parabola opens to the right.
    - If $p < 0$, the parabola opens to the left.

    ```mermaid
    graph TD
    subgraph Parabola["y^2 = 4px, p > 0"]
        V[Vertex 0 0]
        F[Focus p 0]
        L[Directrix x = -p]
        P[Point x y]
        Curve[Parabola] --> P
        V --- F
        P ---|d P F| F
        P ---|d P L| ProjL[Point -p y on L]
        L --- ProjL
    end
    Note[Distance d P F = d P L] --> P

    style Curve fill:none,stroke:#00f,stroke-width:2px
    style V fill:#fff,stroke:#333,stroke-width:2px
    style F fill:#fff,stroke:#333,stroke-width:2px
    style L fill:none,stroke:#f00,stroke-width:1px,stroke-dasharray:5,5
    style P fill:#fff,stroke:#333,stroke-width:2px
    style ProjL fill:#fff,stroke:#333,stroke-width:2px
    style Note fill:#fff,stroke:#333,stroke-width:1px
    linkStyle 0 stroke:#00f,stroke-width:2px
    linkStyle 1 stroke:#000,stroke-width:1px
    linkStyle 2 stroke:#000,stroke-width:1px
    linkStyle 3 stroke:#f00,stroke-width:1px,stroke-dasharray:5,5
    linkStyle 4 stroke:#333,stroke-width:1px
    ```

2.  **Parabola with Vertex at Origin $(0,0)$ and Axis of Symmetry along the y-axis:**
    Equation: $x^2 = 4py$
    - **Focus $F$:** $(0,p)$
    - **Directrix $L$:** $y = -p$
    - **Vertex $V$:** $(0,0)$
    - If $p > 0$, the parabola opens upwards.
    - If $p < 0$, the parabola opens downwards.

    ```mermaid
    graph TD
    subgraph Parabola["x^2 = 4py, p > 0"]
        V[Vertex 0 0]
        F[Focus 0 p]
        L[Directrix y = -p]
        P[Point x y]
        Curve[Parabola] --> P
        F --- V
        P ---|d P F| F
        P ---|d P L| ProjL[Point x -p on L]
        L --- ProjL
    end
    Note[Distance d P F = d P L] --> P

    style Curve fill:none,stroke:#00f,stroke-width:2px
    style V fill:#fff,stroke:#333,stroke-width:2px
    style F fill:#fff,stroke:#333,stroke-width:2px
    style L fill:none,stroke:#f00,stroke-width:1px,stroke-dasharray:5,5
    style P fill:#fff,stroke:#333,stroke-width:2px
    style ProjL fill:#fff,stroke:#333,stroke-width:2px
    style Note fill:#fff,stroke:#333,stroke-width:1px
    linkStyle 0 stroke:#00f,stroke-width:2px
    linkStyle 1 stroke:#000,stroke-width:1px
    linkStyle 2 stroke:#000,stroke-width:1px
    linkStyle 3 stroke:#f00,stroke-width:1px,stroke-dasharray:5,5
    linkStyle 4 stroke:#333,stroke-width:1px
    ```

## Parabola with Vertex at $(h,k)$
- **Axis of Symmetry parallel to x-axis:** $(y-k)^2 = 4p(x-h)$
    - Focus: $(h+p, k)$
    - Directrix: $x = h-p$
- **Axis of Symmetry parallel to y-axis:** $(x-h)^2 = 4p(y-k)$
    - Focus: $(h, k+p)$
    - Directrix: $y = k-p$

## Reflective Property
One of the most important properties of a parabola related to its focus is its **reflective property**:
- Any ray of light (or sound, or other wave) that travels parallel to the axis of symmetry and strikes the concave side of the parabola will be reflected to pass through the focus.
- Conversely, any ray originating from the focus and striking the parabola will be reflected parallel to the axis of symmetry.

This property is the basis for many applications:
- **Parabolic Reflectors/Antennas:** Satellite dishes, radio telescopes, and reflecting telescopes use parabolic shapes to collect and focus incoming parallel waves (e.g., radio waves, light from distant stars) at the focus, where a receiver or detector is placed.
- **Headlights and Searchlights:** A light source placed at the focus of a parabolic mirror will produce a strong, parallel beam of light.
- **Solar Concentrators:** Parabolic troughs or dishes concentrate sunlight onto a focal line or point to heat a fluid or generate electricity.
- **Microphones:** Parabolic microphones collect sound from a specific direction and focus it onto a microphone element.

The focus and directrix are intrinsic to the definition of a parabola and dictate its unique geometric and reflective characteristics.

---