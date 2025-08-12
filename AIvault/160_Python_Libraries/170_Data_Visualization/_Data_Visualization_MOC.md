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
  - "[[160_Python_Libraries/170_Data_Visualization/Matplotlib/_Matplotlib_MOC|Matplotlib MOC]]"
  - "[[_Seaborn_MOC|Seaborn MOC]]"
  - "[[Plotly_and_Plotly_Express|Plotly and Plotly Express]]"
  - "[[Bokeh_Library|Bokeh Library]]"
  - "[[Altair_Library|Altair Library]]"
  - "[[Data_Visualization_Importance]]"
  - "[[Data_Visualization_Principles]]"
  - "[[Choosing_the_Right_Plot]]"
worksheet:
  - WS_DataViz_1
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
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

## Plot Types (General Categories - Specifics in Library MOCs)
-   **Comparison/Relationship:** [[Line_Plot|Line Plot]], [[Scatter_Plot|Scatter Plot]], [[Bar_Chart|Bar Chart]]
-   **Distribution:** [[Histogram|Histogram]], [[Box_Plot|Box Plot]], [[170_Data_Visualization/Plot_Types/Violin_Plot|Violin Plot]], Density Plot
-   **Composition:** [[Pie_Chart|Pie Chart]], Stacked Bar Chart
-   **Matrix/Grid:** [[170_Data_Visualization/Plot_Types/Heatmap|Heatmap]]

## Key Libraries
-   [[160_Python_Libraries/170_Data_Visualization/Matplotlib/_Matplotlib_MOC|Matplotlib]]
-   [[_Seaborn_MOC|Seaborn]]
-   [[Plotly_and_Plotly_Express|Plotly & Plotly Express]]
-   [[Bokeh_Library|Bokeh]]
-   [[Altair_Library|Altair]]
-   *ggplot2 (R) - (Mentioned for completeness, not detailed here)*

## Notes in this Section (General Visualization)
```dataview
LIST
FROM "170_Data_Visualization"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC") AND !contains(file.folder, "Matplotlib") AND !contains(file.folder, "Seaborn") AND !contains(file.folder, "Plot_Types")
SORT file.name ASC
```

## Library-Specific Sections
-   [[160_Python_Libraries/170_Data_Visualization/Matplotlib/_Matplotlib_MOC|Matplotlib]]
-   [[_Seaborn_MOC|Seaborn]]
-   [[Plotly_and_Plotly_Express|Plotly & Plotly Express]]
-   [[Bokeh_Library|Bokeh]]
-   [[Altair_Library|Altair]]

## Plot Type Specific Notes
```dataview
LIST
FROM "170_Data_Visualization/Plot_Types"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
```
---