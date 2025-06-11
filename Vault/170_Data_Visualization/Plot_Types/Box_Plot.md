---
tags:
  - data_visualization
  - plotting
  - box_plot
  - distribution
  - quartiles
  - outliers
  - concept
  - chart
aliases:
  - Boxplot
  - Box and Whisker Plot
related:
  - "[[Matplotlib_Basic_Plotting_Functions]]"
  - "[[Seaborn_Categorical_Plots]]"
  - "[[Choosing_the_Right_Plot]]"
  - "[[Violin_Plot]]"
  - "[[Interquartile_Range_IQR|Interquartile Range (IQR)]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-09
---
# Box Plot (Box and Whisker Plot)

## Definition
A **box plot**, also known as a **box and whisker plot**, is a standardized way of displaying the distribution of data based on a five-number summary: minimum, first quartile (Q1), median (Q2), third quartile (Q3), and maximum. It can also highlight outliers.

Box plots are particularly useful for comparing distributions between several groups or datasets.

## Key Components
-   **Box:**
    -   The central box spans from the **first quartile (Q1)** (25th percentile) to the **third quartile (Q3)** (75th percentile).
    -   The length of the box is thus the **[[Interquartile_Range_IQR|Interquartile Range (IQR)]]** = Q3 - Q1.
-   **Median (Q2):** A line inside the box marks the median (50th percentile) of the data.
-   **Whiskers:**
    -   Lines extending from the box to show the range of the data.
    -   Commonly, whiskers extend to 1.5 times the IQR from the Q1 and Q3.
        -   Upper whisker: $Q3 + 1.5 \times IQR$ (or the maximum data point within this limit).
        -   Lower whisker: $Q1 - 1.5 \times IQR$ (or the minimum data point within this limit).
    -   Other conventions for whisker length exist (e.g., min/max values, specific percentiles).
-   **Outliers (Fliers):** Data points that fall beyond the whiskers are often plotted individually as points, considered potential outliers.

## Purpose
-   **Summarize Data Distribution:** Provides a concise visual summary of key statistical measures (median, quartiles, range).
-   **Compare Distributions:** Excellent for comparing the distributions of a numerical variable across different categorical groups.
-   **Identify Skewness:** The position of the median within the box and the relative lengths of the whiskers can indicate skewness.
    -   Median closer to Q1 and longer upper whisker: Right (positive) skew.
    -   Median closer to Q3 and longer lower whisker: Left (negative) skew.
-   **Detect Outliers:** Clearly highlights potential outliers.

## When to Use
-   When you want to compare the distributions of a numerical variable across two or more groups.
-   To get a quick understanding of the central tendency, spread, and symmetry/skewness of a dataset.
-   To identify potential outliers.

## Matplotlib & Seaborn Implementation
-   **Matplotlib:** `plt.boxplot(data, labels=...)` or `ax.boxplot(...)`.
-   **Seaborn:** `sns.boxplot(x="category_col", y="value_col", data=df, ...)` or `sns.catplot(..., kind="box", ...)`. Seaborn makes it easy to group by `hue`.

## Example Scenario & Chart
>[!question]- For Box Plot: Come up with a scenario where it would be useful. Is this plot the best way to visualize this scenario?
>
>**Scenario:** Comparing the delivery times (in days) for products shipped by different carriers ('Carrier A', 'Carrier B', 'Carrier C') for an e-commerce company.
>
>**Usefulness:** A box plot is highly useful to:
>1.  Compare the median delivery time for each carrier.
>2.  Compare the variability (spread, IQR) of delivery times for each carrier.
>3.  Identify if any carrier has significantly more outliers (very long or very short delivery times).
>4.  Assess the skewness of delivery times for each carrier.
>
>**Is this the best way?**
>Yes, for comparing distributions of a numerical variable across several categories, a box plot is a **very effective and standard choice**.
>
>**Alternatives & Complements:**
>-   [[Violin_Plot|Violin plots]] (`sns.violinplot`) provide more detail about the shape of each distribution (like a KDE) in addition to summary statistics similar to a box plot. They can be better for identifying multimodality.
>-   Strip plots or swarm plots (`sns.stripplot`, `sns.swarmplot`) show all individual data points, which can be useful for smaller datasets or to see the raw data, but can get cluttered for larger datasets. They can be overlaid on box/violin plots.
>-   [[Bar_Chart|Bar charts]] could show the *mean* delivery time per carrier, but they wouldn't show the distribution, spread, or outliers.

**Obsidian Chart Plugin Example (Illustrative):**
> [!note] Obsidian Charts plugin has direct support for box plots. The `data` array for each dataset should be `[min, q1, median, q3, max]`. Outliers would typically be plotted as a separate scatter series if needed for full detail, but the basic box plot shows the main summary.

---
