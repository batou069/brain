---
tags:
  - data_visualization
  - plotting
  - pie_chart
  - composition
  - proportions
  - concept
  - chart
aliases:
  - Pie Graph
related:
  - "[[Matplotlib_Basic_Plotting_Functions]]"
  - "[[Choosing_the_Right_Plot]]"
  - "[[Bar_Chart]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-09
---
nvim# Pie Chart

## Definition
A **pie chart** (or a circle chart) is a circular statistical graphic, which is divided into slices to illustrate numerical proportion. In a pie chart, the arc length of each slice (and consequently its central angle and area) is proportional to the quantity it represents.

Pie charts are used to show the composition of a whole, where each slice represents a part or percentage of that whole.

## Key Characteristics
-   **Circular Shape:** The entire chart represents 100% or the total sum of categories.
-   **Slices (Wedges):** Each category is represented by a slice.
-   **Proportionality:** The size (angle/area) of each slice is proportional to its value relative to the total.
-   **Labels:** Slices are typically labeled with the category name and often its percentage or value.

## When to Use
-   To show **parts of a whole** or percentage composition.
-   When you have a **small number of categories** (ideally 2-5). With too many slices, the chart becomes cluttered and difficult to interpret.
-   When the sum of the parts is meaningful and equals 100% or a clear total.
-   When emphasizing the relative size of one or two categories compared to the total.

## Advantages
-   **Simplicity:** Easy to understand for showing simple part-to-whole relationships.
-   **Visual Appeal (for some):** Can be visually engaging for simple compositions.

## Disadvantages/Considerations
-   **Difficulty in Comparing Slices:** Humans are not good at accurately comparing angles or areas, especially if slices are similar in size or if there are many slices. This makes precise comparisons between categories difficult.
-   **Not Suitable for Many Categories:** Becomes cluttered and unreadable with more than 5-7 categories.
-   **Can Be Misleading:** 3D pie charts or "exploded" slices can distort perception of proportions.
-   **Poor for Showing Trends or Changes Over Time:** Not designed for this purpose.
-   **[[Bar_Chart|Bar charts]] are often a better alternative:** Bar charts (especially sorted ones) make it easier to compare the magnitudes of different categories accurately. Stacked bar charts can also show parts of a whole effectively.

## Matplotlib & Seaborn Implementation
-   **Matplotlib:** `plt.pie(sizes, labels=..., autopct='%1.1f%%', ...)` or `ax.pie(...)`.
-   **Seaborn:** Does not have a dedicated high-level pie chart function. You would typically use Matplotlib's `plt.pie()` if needed, or reconsider if a pie chart is the best choice (Seaborn focuses more on statistical graphics where pie charts are less favored for rigorous analysis).

## Example Scenario & Chart
>[!question]- For Pie Chart: Come up with a scenario where it would be useful. Is this plot the best way to visualize this scenario?
>
>**Scenario:** Showing the distribution of an e-commerce company's marketing budget across different channels: 'Social Media', 'Search Engine Ads', 'Email Marketing', 'Affiliate Marketing'.
>
>**Usefulness:** A pie chart can be useful here if the goal is to quickly show the proportion of the total budget allocated to each of these few channels.
>
>**Is this the best way?**
>It can be acceptable for a very small number of categories (like 3-4) where the proportions are distinctly different. However, even in this case, a **[[Bar_Chart|bar chart]] (e.g., a horizontal bar chart sorted by budget amount) would likely be better for accurately comparing the budget allocations** between channels. If the goal is precise comparison, a bar chart is superior. If the goal is a quick visual of "parts of a whole" and the categories are few and distinct, a pie chart *can* be used, but with caution.
>
>**Alternatives & Complements:**
>-   A **sorted bar chart** would allow for easier comparison of channel budgets.
>-   A **100% stacked bar chart** could show the composition if this budget allocation changes over time or across different campaigns.
>-   A **treemap** could be used if there's a hierarchical structure to the budget.

**Obsidian Chart Plugin Example (Illustrative):**

```chart
type: pie
labels: [Social Media, Search Engine Ads, Email Marketing, Affiliate Marketing, Content Creation]
series:
  - title: Marketing Budget Allocation
    data: [30, 25, 20, 15, 10]
    backgroundColor:
      - rgba(255, 99, 132, 0.8)
      - rgba(54, 162, 235, 0.8)
      - rgba(255, 206, 86, 0.8)
      - rgba(75, 192, 192, 0.8)
      - rgba(153, 102, 255, 0.8)
    borderColor: #fff
    borderWidth: 1
options:
  title: Marketing Budget Allocation by Channel
  legend: top
  width: 40%
  labelColors: true
```

> The `tooltip.callbacks.label` function in `options` is a Chart.js way to customize tooltips, e.g., to show percentages.

---