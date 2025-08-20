---
tags:
  - data_visualization
  - plotting
  - advanced_plots
  - area_chart
  - bubble_chart
  - treemap
  - concept
aliases:
  - More Plot Types
  - Other Visualizations
related:
  - "[[_Data_Visualization_MOC]]"
  - "[[Choosing_the_Right_Plot]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-08-20
---
# Additional Plot Types and Scenarios

Beyond the most common plots, many other visualization types serve specific purposes. Here are three examples not previously detailed, along with scenarios and considerations.

>[!question] Come up with 3 types of plots not mentioned above, and answer the same questions (scenario, usefulness, best way?).

[list2tab|#Additional Plots]
- 1. Area Chart (Stacked Area Chart)
    -   **Definition:** An area chart is like a [[170_Data_Visualization/Plot_Types/Line_Plot|line chart]] but with the area below the line(s) filled with color or shading. A **stacked area chart** displays the contribution of different parts to a whole over time or another continuous variable. Each constituent part is stacked on top of the previous one.
    -   **Scenario:** Visualizing the change in an e-commerce company's revenue sources (e.g., 'Online Sales', 'In-Store Sales', 'Subscription Services') over several quarters. We want to see both the trend of each source and the trend of the total revenue.
    -   **Usefulness:**
        -   Shows the trend of a total and the changing contribution of its parts over a continuous axis (usually time).
        -   Good for illustrating how a whole is divided into parts that change over time.
    -   **Best Way?:**
        -   **Yes, for showing part-to-whole relationships changing over a continuous axis, a stacked area chart is often a very good choice.** It clearly shows the total and the magnitude of each component.
        -   **Considerations:**
            -   Can become cluttered if there are too many categories (parts).
            -   It can be difficult to accurately compare the trends of individual components that are not at the baseline, as their baseline changes.
            -   A 100% stacked area chart (where the y-axis goes up to 100%) is good for showing changing proportions over time, rather than absolute magnitudes.
        -   **Alternatives:** Grouped [[170_Data_Visualization/Plot_Types/Bar_Chart|bar charts]] can show components per time period but might not emphasize the continuous trend or total as well. Multiple line charts can show individual trends but not the part-to-whole composition.
    -   **Obsidian Chart Plugin Example (Illustrative Stacked Area):**
        > [!note] Chart.js (used by Obsidian Charts) supports stacked area charts by setting `fill: true` and `stacked: true` on line chart datasets.
        ```chart
        type: line
        labels: ['Q1 2022', 'Q2 2022', 'Q3 2022', 'Q4 2022', 'Q1 2023']
        datasets:
          - label: 'Online Sales'
            data: # Conceptual data
            backgroundColor: 'rgba(54, 162, 235, 0.5)' # Blue
            borderColor: 'rgba(54, 162, 235, 1)'
            fill: true
            tension: 0.1
          - label: 'In-Store Sales'
            data: 
            backgroundColor: 'rgba(255, 99, 132, 0.5)' # Red
            borderColor: 'rgba(255, 99, 132, 1)'
            fill: true
            tension: 0.1
          - label: 'Subscription Services'
            data: 
            backgroundColor: 'rgba(75, 192, 192, 0.5)' # Teal
            borderColor: 'rgba(75, 192, 192, 1)'
            fill: true
            tension: 0.1
        options:
          responsive: true
          plugins:
            title: { display: true, text: 'Revenue Sources Over Time (Stacked Area)' }
            tooltip: { mode: 'index', intersect: false }
          scales:
            x: { title: { display: true, text: 'Quarter' } }
            y: { stacked: true, title: { display: true, text: 'Revenue ($)' }, min: 0 }
        ```
- 2. Bubble Chart
    -   **Definition:** A bubble chart is a variation of a [[170_Data_Visualization/Plot_Types/Scatter_Plot|scatter plot]] where data points are replaced with bubbles, and an additional dimension of the data is represented by the **size** of the bubbles. It can display three dimensions of data (x-position, y-position, size). A fourth dimension can be added with color.
    -   **Scenario:** Analyzing marketing campaigns for different e-commerce products. We want to visualize `cost_per_campaign` (x-axis), `conversion_rate` (y-axis), and `total_reach` (bubble size) for each campaign. We could also color bubbles by `product_category`.
    -   **Usefulness:**
        -   Allows visualization of three or four dimensions simultaneously on a 2D plot.
        -   Good for comparing entities based on multiple attributes, especially when one attribute represents magnitude or importance (mapped to size).
    -   **Best Way?:**
        -   **Yes, for comparing three numerical variables where one clearly represents a "size" or "weight" aspect, a bubble chart is a very effective choice.** If a fourth categorical dimension needs to be shown, color is a good addition.
        -   **Considerations:**
            -   Too many bubbles or too much overlap can make it hard to read.
            -   Accurate perception of bubble area/size can be tricky for humans; ensure clear scaling and legend for size.
            -   Avoid using bubble size for variables that don't have a clear magnitude interpretation.
        -   **Alternatives:** A [[170_Data_Visualization/Plot_Types/Scatter_Plot_Matrix|scatter plot matrix]] could show all pairwise 2D relationships but wouldn't combine three variables into one view as directly. 3D scatter plots are an option but have their own interpretation challenges.
    -   **Obsidian Chart Plugin Example (Illustrative Bubble Chart):**
        > [!note] Chart.js scatter plots can represent bubble charts by varying `pointRadius` or `pointStyle` properties based on data.
        ```chart
        type: bubble // Or scatter with varying pointRadius
        datasets:
          - label: 'Campaign A (Electronics)'
            data: [ {x: 500, y: 0.05, r: 20} ] # x=cost, y=conversion, r=reach (mapped to radius)
            backgroundColor: 'rgba(255, 99, 132, 0.7)'
          - label: 'Campaign B (Books)'
            data: [ {x: 200, y: 0.08, r: 10} ]
            backgroundColor: 'rgba(54, 162, 235, 0.7)'
          - label: 'Campaign C (Electronics)'
            data: [ {x: 1000, y: 0.03, r: 30} ]
            backgroundColor: 'rgba(255, 99, 132, 0.5)' # Same color as A for same category
          - label: 'Campaign D (Home Goods)'
            data: [ {x: 300, y: 0.06, r: 15} ]
            backgroundColor: 'rgba(75, 192, 192, 0.7)'
        options:
          responsive: true
          plugins:
            title: { display: true, text: 'Marketing Campaign Performance (Bubble Chart)' }
            tooltip: { callbacks: { label: function(c) { return `${c.dataset.label}: Cost $${c.raw.x}, Conv ${c.raw.y*100}%, Reach ${c.raw.r*1000}`; } } }
          scales:
            x: { title: { display: true, text: 'Campaign Cost ($)' } }
            y: { title: { display: true, text: 'Conversion Rate' } }
          elements: { point: { radius: function(ctx) { const size = ctx.raw.r; return size; } } } // Dynamically set radius
        ```
- 3. Treemap
    -   **Definition:** A treemap displays hierarchical (tree-structured) data as a set of nested rectangles. Each branch of the tree is given a rectangle, which is then tiled with smaller rectangles representing sub-branches. The area of each rectangle is typically proportional to a specified dimension of the data.
    -   **Scenario:** Visualizing the sales breakdown of an e-commerce store, starting from overall sales, then by product category (e.g., 'Electronics', 'Clothing'), then by sub-category (e.g., 'Laptops', 'Shirts'), and finally by individual product. The area of each rectangle represents its proportion of sales.
    -   **Usefulness:**
        -   Excellent for showing hierarchical data and part-to-whole relationships at multiple levels simultaneously.
        -   Can effectively display a large number of categories and their relative sizes.
        -   Color can be used to encode another dimension (e.g., sales growth rate).
    -   **Best Way?:**
        -   **Yes, for visualizing hierarchical data where you want to show the proportion of parts within a whole at multiple levels, a treemap is a very strong and often the best choice.**
        -   **Considerations:**
            -   Not good for showing precise comparisons between non-adjacent rectangles, especially if areas are similar.
            -   Can become cluttered if the hierarchy is too deep or there are too many very small items.
            -   Not ideal for showing trends over time.
        -   **Alternatives:** Sunburst charts are similar for hierarchical data but use a radial layout. Nested [[170_Data_Visualization/Plot_Types/Pie_Chart|pie charts]] (donuts) can show a couple of levels but quickly become hard to read. Stacked [[170_Data_Visualization/Plot_Types/Bar_Chart|bar charts]] can show one level of hierarchy well.
    -   **Obsidian Chart Plugin Example (Illustrative Treemap):**
        > [!note] Treemaps are a specialized chart type not directly supported by basic Chart.js (and thus likely not by the standard Obsidian Charts plugin). Libraries like Plotly, Highcharts, or D3.js are typically used. This is a conceptual description.

        ```
        Conceptual Data for Treemap (Sales Hierarchy):

        - Total Sales (Root Rectangle)
            - Electronics (Sub-Rectangle, area proportional to electronics sales)
                - Laptops (Sub-sub-rectangle within Electronics)
                - Smartphones
                - Accessories
            - Clothing (Sub-Rectangle)
                - Shirts
                - Pants
            - Books (Sub-Rectangle)

        (Imagine nested rectangles where the size of each rectangle represents its sales contribution.
        Colors could represent product categories or sales growth.)
        ```
        *Actual treemap requires specialized plotting libraries.*

These additional plot types expand the toolkit for visualizing different kinds of data structures and relationships.

---