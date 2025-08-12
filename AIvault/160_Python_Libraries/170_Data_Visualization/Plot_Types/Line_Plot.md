---
tags:
  - data_visualization
  - plotting
  - line_plot
  - trends
  - time_series
  - concept
aliases:
  - Line Chart
  - Line Graph
related:
  - "[[Matplotlib_Basic_Plotting_Functions]]"
  - "[[Choosing_the_Right_Plot]]"
  - "[[Trend_Line]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-03
---
# Line Plot

## Definition
A **line plot** or **line chart** is a type of chart which displays information as a series of data points called 'markers' connected by straight line segments. It is one of the most basic types of chart common in many fields.

Line plots are primarily used to visualize the trend of a numerical variable over a continuous interval or an ordered sequence, most commonly time.

## Key Characteristics
-   **Data Points:** Represents individual data values as markers (though markers can be omitted).
-   **Connecting Lines:** Straight lines connect consecutive data points, implying a continuous progression or relationship between them.
-   **Axes:** Typically, the horizontal axis (x-axis) represents an ordered variable (e.g., time, sequence steps, ordered categories), and the vertical axis (y-axis) represents a numerical quantity.

## When to Use a Line Plot
-   **Showing Trends Over Time:** This is the most common use case (e.g., stock prices, temperature changes, website traffic over months).
-   **Visualizing Sequential Data:** When the x-axis variable has a natural order and you want to see how the y-variable changes along this sequence.
-   **Comparing Multiple Series:** Multiple lines can be plotted on the same axes to compare trends of different groups or variables over the same interval. A [[Plot_Elements_Anatomy#Legend|legend]] is crucial here.
-   **Displaying Frequency Polygons:** A variation where midpoints of histogram bins are connected.

## Advantages
-   **Clear Trend Visualization:** Excellent at showing increases, decreases, volatility, and overall patterns over an interval.
-   **Simplicity:** Easy to create and generally easy to understand.
-   **Comparison:** Effective for comparing trends of multiple series.

## Disadvantages/Considerations
-   **Not for Categorical Data (Unordered):** Less suitable if the x-axis represents unordered categories (a [[Bar_Chart|bar chart]] is usually better).
-   **Can Be Misleading with Too Many Lines:** Plotting too many lines on a single chart can make it cluttered and hard to read (the "spaghetti plot" problem). Consider faceting or highlighting specific lines.
-   **Implied Continuity:** The connecting lines imply a continuous change between data points. If the data is sparse or the underlying process is not continuous, this implication might be misleading.
-   **Scale Effects:** The perception of the trend can be significantly affected by the scale of the y-axis.

## Matplotlib Implementation
-   `plt.plot(x, y, ...)` or `ax.plot(x, y, ...)`
-   Key parameters: `color`, `linestyle` (e.g., '-', '--', ':', '-.'), `linewidth`, `marker` (e.g., 'o', 's', '^'), `markersize`, `label`.

## Example Scenario
>[!question]- For Line Plot: Come up with a scenario where it would be useful. Is this plot the best way to visualize this scenario?
>
>**Scenario:** Visualizing the average monthly temperature for a city over a period of 12 months to observe seasonal patterns.
>
>**Usefulness:** A line plot is highly useful here because:
>1.  **Time is Ordered:** Months have a natural sequence.
>2.  **Trend is Key:** We want to see how temperature changes month-to-month, identifying peaks (summer) and troughs (winter).
>3.  **Continuity Implied:** While temperature is measured at discrete points (average for the month), the underlying phenomenon of temperature change is continuous, making line connections appropriate.
>
>**Is this the best way?**
>Yes, for showing this type of seasonal trend over a continuous (or discretely sampled continuous) variable like time, a line plot is generally the **best and most standard choice**.
>
>**Alternatives & Complements:**
>-   A [[Bar_Chart|bar chart]] could also show monthly averages, but it would emphasize individual monthly values rather than the continuous trend between them.
>-   If comparing multiple years, multiple lines (one per year) could be used, or a [[Heatmap|heatmap]] (month vs. year, color for temperature) could be an alternative.
>-   [[Box_Plot|Box plots]] per month could show the distribution of daily temperatures within each month if that level of detail is available and desired.

```chart
type: line
labels: [T1, T2, T3, T4, T5, T6, T7, T8, T9, T10]
series:
  - title: Bill vs. Tip
    data: [1.01, 1.66, 3.50, 3.31, 3.61, 4.71, 2.00, 3.12, 1.96, 3.23]
    backgroundColor: rgba(0, 123, 255, 0.6)
    pointRadius: 5
    fill: false
options:
  xTitle: Total Bill ($)
  yTitle: Tip Amount ($)
  xMin: 0
  yMin: 0
  title: Scatter Plot Total Bill vs. Tip Amount
```
---