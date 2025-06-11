---
tags:
  - altair
  - python
  - data_visualization
  - declarative_plotting
  - vega_lite
  - grammar_of_graphics
  - moc
  - concept
aliases:
  - Altair MOC
  - Altair Library
  - Declarative Visualization Python
related:
  - "[[_Data_Visualization_MOC]]"
  - "[[_Pandas_MOC|Pandas DataFrame]]"
  - "[[Vega_Lite_Grammar]]"
  - "[[Grammar_of_Graphics]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-11
---
# Altair MOC 📊✨

**Altair** is a declarative statistical visualization library for Python, based on the **Vega-Lite** visualization grammar. "Declarative" means that instead of writing code to draw shapes and lines, you describe the *links* between data columns and visual properties (encodings like x-position, y-position, color, size, shape). Altair then determines the most effective way to render that specification.

This approach, inspired by the [[Grammar_of_Graphics|Grammar of Graphics]], allows for concise and intuitive creation of a wide range of statistical visualizations.

## Core Philosophy & Features
-   **Declarative Syntax:** Define *what* you want to visualize (data, marks, encodings) rather than *how* to draw it step-by-step.
-   **Based on Vega-Lite:** Altair specifications are compiled into JSON objects that conform to the Vega-Lite grammar. Vega-Lite is a high-level grammar for interactive graphics.
-   **Pandas DataFrame Integration:** Designed to work primarily and seamlessly with [[_Pandas_MOC|Pandas DataFrames]]. Data is typically passed as a DataFrame.
-   **Statistical Focus:** Well-suited for creating common statistical charts and exploring data relationships.
-   **Interactive by Default (with limitations/renderers):** Can produce interactive charts (hover, selection, zoom/pan) when rendered appropriately (e.g., in JupyterLab/Notebook with a Vega-Lite renderer, or when exported to HTML).
-   **Concise Code:** Often requires less code to produce complex visualizations compared to imperative libraries like Matplotlib.
-   **Automatic Inferences:** Altair can often infer appropriate scales, axes, and legends from the data and encodings.

## Key Concepts & Components
-   [[Altair_Overview_Declarative_Viz|Altair Overview & Declarative Visualization]]
    -   The Grammar of Graphics principles.
    -   Altair's relationship with Vega-Lite.
-   [[Altair_Chart_Object_Data|The Chart Object and Data]]
    -   Creating a `alt.Chart(data_frame)`.
    -   Data formats (Pandas DataFrame, URL to JSON/CSV).
-   [[Altair_Marks_Encodings|Marks and Encodings]]
    -   **Marks:** Geometric objects representing data (e.g., `mark_point()`, `mark_line()`, `mark_bar()`, `mark_area()`, `mark_rect()`).
    -   **Encodings (`encode()`):** Mapping data columns (fields) to visual properties (channels).
        -   Positional: `x`, `y`.
        -   Appearance: `color`, `size`, `shape`, `opacity`.
        -   Text: `text`, `tooltip`.
        -   Ordering: `order`.
        -   Faceting: `row`, `column`, `facet`.
-   [[Altair_Data_Types_Scales|Data Types and Scales]]
    -   Specifying data types for fields (`Q` for quantitative, `N` for nominal, `O` for ordinal, `T` for temporal).
    -   Customizing scales (linear, log, pow, time), bins, domains, ranges.
-   [[Altair_Compound_Charts_Interactivity|Compound Charts & Interactivity]]
    -   **Layering (`+`):** Overlaying multiple charts.
    -   **Concatenation (`|`, `&`):** Placing charts side-by-side (horizontal `|`) or one above another (vertical `&`).
    -   **Faceting (`facet()`):** Creating small multiples.
    -   **Repeating (`repeat()`):** Creating grids of similar plots with different fields.
    -   **Selections (`alt.selection_interval()`, `alt.selection_point()`):** Enabling interactive selections that can drive conditional properties or filter other charts.
-   [[Altair_Customization_Saving|Customization and Saving Charts]]
    -   Configuring properties (`configure_axis()`, `configure_legend()`, `configure_title()`, `properties()`).
    -   Saving charts (HTML, JSON, PNG/SVG via external tools like `altair_viewer` or `vl-convert`).

## Notes in this Altair Section
```dataview
LIST
FROM "170_Data_Visualization/Altair"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
```

---