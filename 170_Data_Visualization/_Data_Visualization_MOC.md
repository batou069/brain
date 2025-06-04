---
tags:
  - data_visualization
  - plotting
  - charts
  - graphs
  - moc
  - concept
aliases:
  - Visualization MOC
  - Data Viz MOC
related:
  - "[[_Data_Science_AI_MOC]]"
  - "[[170_Data_Visualization/Matplotlib/_Matplotlib_MOC|Matplotlib MOC]]"
  - "[[170_Data_Visualization/Seaborn/_Seaborn_MOC|Seaborn MOC]]"
  - "[[Data_Visualization_Importance]]"
  - "[[Data_Visualization_Principles]]"
  - "[[Choosing_the_Right_Plot]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-03
---
# Data Visualization MOC 📊

Data visualization is the graphical representation of information and data. By using visual elements like charts, graphs, and maps, data visualization tools provide an accessible way to see and understand trends, outliers, and patterns in data. It's a critical component of [[Exploratory_Data_Analysis_Workflow|Exploratory Data Analysis (EDA)]], data reporting, and communicating insights.

## Core Concepts
-   [[Data_Visualization_Importance|Why is Visualization Important (and its Limitations)?]]
-   [[Data_Visualization_Principles|Principles of Effective Data Visualization]]
-   [[Choosing_the_Right_Plot|Choosing the Right Plot Type]]
-   [[Categorical_vs_Numerical_Data_Visualization|Visualizing Categorical vs. Numerical Data]]
-   [[Visualizing_Multidimensional_Data|Visualizing Multidimensional Data]]
-   [[Plot_Elements_Anatomy|Anatomy of a Plot]] (Axes, Ticks, Gridlines, Legend, Title)

## Plot Types
A comprehensive list of plot types will be detailed under specific library MOCs or dedicated notes. Common categories include:
-   **Comparison/Relationship:** [[Line_Plot|Line Plot]], [[Scatter_Plot|Scatter Plot]], [[Bar_Chart|Bar Chart]] (for comparing categories)
-   **Distribution:** [[Histogram|Histogram]], [[Box_Plot|Box Plot]], [[Violin_Plot|Violin Plot]], Density Plot
-   **Composition:** [[Pie_Chart|Pie Chart]], Stacked Bar Chart, Treemap
-   **Geospatial:** Choropleth Maps, Scatter Maps
-   **Matrix/Grid:** [[Heatmap|Heatmap]]

## Key Libraries
-   **[[170_Data_Visualization/Matplotlib/_Matplotlib_MOC|Matplotlib]]**: Foundational plotting library in Python.
-   **[[170_Data_Visualization/Seaborn/_Seaborn_MOC|Seaborn]]**: High-level interface for statistical graphics, built on Matplotlib.
-   **Plotly / Dash**: Interactive visualizations and web applications.
-   **Bokeh**: Interactive visualizations for modern web browsers.
-   **ggplot2 (R)**: Powerful grammar of graphics implementation in R.

## Notes in this Section (General Visualization)
```dataview
LIST
FROM "170_Data_Visualization"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC") AND !contains(file.folder, "Matplotlib") AND !contains(file.folder, "Seaborn")
SORT file.name ASC
```

## Library-Specific Sections
-   [[170_Data_Visualization/Matplotlib/_Matplotlib_MOC|Matplotlib]]
-   [[170_Data_Visualization/Seaborn/_Seaborn_MOC|Seaborn]] (Placeholder)

---