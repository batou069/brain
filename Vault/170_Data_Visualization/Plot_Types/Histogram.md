---
tags:
  - data_visualization
  - plotting
  - histogram
  - distribution
  - frequency
  - numerical_data
  - concept
  - chart
aliases:
  - Frequency Distribution Plot
related:
  - "[[Matplotlib_Basic_Plotting_Functions]]"
  - "[[Seaborn_Distribution_Plots]]"
  - "[[Choosing_the_Right_Plot]]"
  - "[[Kernel_Density_Estimate_KDE|Kernel Density Estimate (KDE)]]"
  - "[[Bar_Chart]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-09
---
# Histogram

## Definition
A **histogram** is a graphical representation of the distribution of numerical data. It is an estimate of the probability distribution of a continuous variable (quantitative variable). To construct a histogram, the first step is to "bin" the range of values—that is, divide the entire range of values into a series of intervals—and then count how many values fall into each interval.

The bins are usually specified as consecutive, non-overlapping intervals of a variable. The bins (intervals) must be adjacent and are often (but not necessarily) of equal size.

## Key Characteristics
-   **Bars:** The height of each bar represents the frequency (count of data points) or relative frequency (proportion) of data falling within that bin.
-   **Bins:** The intervals that divide the data range. The choice of the number of bins or bin width can significantly affect the appearance and interpretation of the histogram.
-   **Continuous Data:** Used for numerical data (continuous or discrete with many values).
-   **No Gaps Between Bars (Typically):** Unlike a [[Bar_Chart|bar chart]] for categorical data, there are typically no gaps between the bars of a histogram, indicating the continuous nature of the underlying variable (though some styling might introduce small gaps for visual clarity).

## Purpose
-   **Visualize Data Distribution:** To understand the underlying frequency distribution of a set of continuous or discrete numerical data.
-   **Identify Shape of Distribution:**
    -   Symmetric (e.g., bell-shaped like a [[Normal_Distribution|normal distribution]])
    -   Skewed (left/negative skew or right/positive skew)
    -   Modality (unimodal, bimodal, multimodal)
-   **Estimate Central Tendency and Spread:** Get a visual sense of where data clusters and how spread out it is.
-   **Detect Outliers:** Extreme values might appear as isolated bars.

## When to Use
-   When you have a single numerical variable and want to understand its distribution.
-   To check for normality or other distributional assumptions.
-   To compare distributions (though overlaid density plots or side-by-side boxplots might be better for comparison).

## Matplotlib & Seaborn Implementation
-   **Matplotlib:** `plt.hist(data, bins=..., ...)` or `ax.hist(...)`.
-   **Seaborn:** `sns.histplot(data=df, x="col_name", bins=..., kde=True, ...)` or `sns.displot(data=df, x="col_name", kind="hist", ...)`. Seaborn's `histplot` can easily add a [[Kernel_Density_Estimate_KDE|KDE]] overlay.

## Example Scenario & Chart
>[!question]- For Histogram: Come up with a scenario where it would be useful. Is this plot the best way to visualize this scenario?
>
>**Scenario:** Analyzing the distribution of customer ages for an e-commerce website to understand the primary age demographics.
>
>**Usefulness:** A histogram is highly useful to:
>1.  See which age groups are most common among customers.
>2.  Identify if the age distribution is symmetric, skewed (e.g., more younger or older customers), or has multiple peaks (bimodal).
>3.  Understand the range and spread of customer ages.
>
>**Is this the best way?**
>Yes, for visualizing the frequency distribution of a single numerical variable like age, a histogram is the **standard and most effective method**.
>
>**Alternatives & Complements:**
>-   A [[Kernel_Density_Estimate_KDE|Kernel Density Estimate (KDE) plot]] (`sns.kdeplot`) can provide a smoother representation of the distribution, which can be overlaid on the histogram or plotted separately.
>-   A [[Box_Plot|box plot]] can summarize the distribution (median, quartiles, outliers) but won't show the detailed shape like modality or specific peaks as well as a histogram.
>-   An [[Cumulative_Distribution_Function_CDF|Empirical Cumulative Distribution Function (ECDF) plot]] (`sns.ecdfplot`) shows the cumulative proportion and is good for understanding percentiles.

**Obsidian Chart Plugin Example (Illustrative):**
```chart
type: bar
labels: [18-25, 26-35, 36-45, 46-55, 56-65, 65+]
series:
  - title: Customer Age Distribution
    data: [150, 300, 250, 200, 100, 50]
    backgroundColor: rgba(75, 192, 192, 0.7)
    borderColor: rgba(75, 192, 192, 1)
    borderWidth: 1
options:
  title: Histogram of Customer Ages
  xTitle: Age Group
  yTitle: Number of Customers (Frequency)
  beginAtZero: true
  legend: true
  categoryPercentage: 1.0
  barPercentage: 1.0
```
> **Note on Chart.js for Histograms:** True histograms in Chart.js are often implemented using the bar chart type where the `labels` are the bin edges (or bin centers) and `data` is the frequency. The appearance of continuous bins (bars touching) can be controlled with `barPercentage` and `categoryPercentage` in `options.scales.x`. The example above uses categorical labels for simplicity in Obsidian Charts.

---