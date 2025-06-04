---
tags:
  - matplotlib
  - python
  - plotting
  - line_plot
  - scatter_plot
  - bar_chart
  - histogram
  - box_plot
  - pie_chart
  - concept
aliases:
  - Matplotlib Basic Plots
  - Common Matplotlib Plots
related:
  - "[[170_Data_Visualization/Matplotlib/_Matplotlib_MOC|_Matplotlib_MOC]]"
  - "[[Matplotlib_Pyplot_API_vs_OO_API]]"
  - "[[Matplotlib_Figure_Subplot_Axes]]"
  - "[[Line_Plot]]"
  - "[[Scatter_Plot]]"
  - "[[Bar_Chart]]"
  - "[[Histogram]]"
  - "[[Box_Plot]]"
  - "[[Pie_Chart]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-03
---
# Matplotlib: Basic Plotting Functions

Matplotlib provides a wide array of functions for creating common plot types. These can be accessed via the `matplotlib.pyplot` interface (e.g., `plt.plot()`) or as methods of an `Axes` object (e.g., `ax.plot()`) in the object-oriented approach.

This note covers some of the most frequently used basic plotting functions.

[list2tab|#Basic Plot Types]
- Line Plot
	[[Line_Plot|Line Plot (`plot`)]]
    - **Function:** `plt.plot()` or `ax.plot()`
    - **Purpose:** Displays data points connected by straight line segments. Ideal for showing trends over a continuous interval or sequence (e.g., time series, mathematical functions).
    - **Key Parameters:** `x`, `y`, `color`, `linestyle`, `linewidth`, `marker`, `label`.
    - **Example:**
        ```python
        import matplotlib.pyplot as plt
        import numpy as np
        x = np.linspace(0, 10, 50)
        y = np.sin(x)
        fig, ax = plt.subplots()
        ax.plot(x, y, color='green', marker='o', linestyle='--', label='sin(x)')
        ax.set_title('Line Plot Example')
        ax.set_xlabel('X Value')
        ax.set_ylabel('Y Value (sin(x))')
        ax.legend()
        ax.grid(True)
        # plt.show()
        ```
    -   **Use Case Scenario:** Visualizing stock price changes over a month, plotting temperature readings over a day.
    -   **Best Way?:** Excellent for showing trends in continuous data over an ordered sequence. For comparing many categories or showing exact values, a bar chart might be better.
- Scatter Plot
	[[Scatter_Plot|Scatter Plot (`scatter`)]]
    - **Function:** `plt.scatter()` or `ax.scatter()`
    - **Purpose:** Displays individual data points as markers. Used to show the relationship or correlation between two numerical variables and to identify clusters or outliers.
    - **Key Parameters:** `x`, `y`, `s` (size of markers), `c` (color of markers), `marker`, `alpha` (transparency), `label`, `cmap` (colormap if `c` is an array of values).
    - **Example:**
        ```python
        import matplotlib.pyplot as plt
        import numpy as np
        x_rand = np.random.rand(50) * 10
        y_rand = x_rand + np.random.randn(50) * 2 # y related to x with some noise
        sizes = np.random.rand(50) * 100
        colors = np.random.rand(50)

        fig, ax = plt.subplots()
        scatter = ax.scatter(x_rand, y_rand, s=sizes, c=colors, alpha=0.7, cmap='viridis', label='Random Data')
        ax.set_title('Scatter Plot Example')
        ax.set_xlabel('X Variable')
        ax.set_ylabel('Y Variable')
        fig.colorbar(scatter, label='Color Value') # Add colorbar if 'c' maps to values
        ax.legend()
        # plt.show()
        ```
    -   **Use Case Scenario:** Examining the relationship between students' study hours and exam scores, visualizing height vs. weight.
    -   **Best Way?:** Ideal for showing relationships between two numerical variables and identifying patterns like correlation or clusters. Not suitable for time series trends directly (line plot is better).
- Bar Chart
	[[Bar_Chart|Bar Chart (`bar`, `barh`)]]
    - **Function:** `plt.bar()` (vertical), `plt.barh()` (horizontal) or `ax.bar()`, `ax.barh()`.
    - **Purpose:** Represents categorical data with rectangular bars. Heights (or lengths for `barh`) of bars are proportional to the values they represent. Used for comparing quantities across different categories.
    - **Key Parameters:** `x` (categories/positions), `height` (values), `width`, `color`, `label`.
    - **Example (Vertical):**
        ```python
        import matplotlib.pyplot as plt
        categories = ['A', 'B', 'C', 'D']
        values =

        fig, ax = plt.subplots()
        ax.bar(categories, values, color=['skyblue', 'lightgreen', 'salmon', 'gold'], label='Values')
        ax.set_title('Bar Chart Example')
        ax.set_xlabel('Category')
        ax.set_ylabel('Count / Value')
        ax.legend()
        # plt.show()
        ```
    -   **Use Case Scenario:** Comparing sales figures for different products, showing the number of students in different university departments.
    -   **Best Way?:** Excellent for comparing discrete categories. For many categories, horizontal bar charts (`barh`) can be more readable. Not for showing trends over continuous time.
- Histogram
	[[Histogram|Histogram (`hist`)]]
    - **Function:** `plt.hist()` or `ax.hist()`
    - **Purpose:** Represents the distribution of a single numerical variable by dividing the data range into a series of intervals (bins) and showing the frequency (or density) of observations falling into each bin.
    - **Key Parameters:** `x` (data), `bins` (number of bins or bin edges), `color`, `edgecolor`, `density` (normalize to form a probability density), `label`.
    - **Example:**
        ```python
        import matplotlib.pyplot as plt
        import numpy as np
        data = np.random.randn(1000) # Sample from standard normal distribution

        fig, ax = plt.subplots()
        ax.hist(data, bins=30, color='purple', edgecolor='black', alpha=0.7, label='Data Distribution')
        ax.set_title('Histogram Example')
        ax.set_xlabel('Value')
        ax.set_ylabel('Frequency')
        ax.legend()
        # plt.show()
        ```
    -   **Use Case Scenario:** Visualizing the distribution of exam scores for a class, showing the frequency of different age groups in a population.
    -   **Best Way?:** The standard and best way to visualize the distribution of a single numerical variable. Choice of `bins` is important. For comparing distributions, density plots or overlaid histograms can be used.
- Box Plot
	[[Box_Plot|Box Plot (`boxplot`)]]
    - **Function:** `plt.boxplot()` or `ax.boxplot()`
    - **Purpose:** Displays the distribution of numerical data through quartiles. Shows the median (Q2), interquartile range (IQR = Q3 - Q1), whiskers (typically 1.5 * IQR from Q1 and Q3), and outliers. Useful for comparing distributions across categories.
    - **Key Parameters:** `x` (data, can be a list of arrays/vectors for multiple boxplots), `labels`, `vert` (vertical or horizontal), `patch_artist` (fill boxes with color), `showfliers` (show outliers).
    - **Example:**
        ```python
        import matplotlib.pyplot as plt
        import numpy as np
        data1 = np.random.normal(0, 1, 100)
        data2 = np.random.normal(1, 1.5, 100)
        data_to_plot = [data1, data2]

        fig, ax = plt.subplots()
        bp = ax.boxplot(data_to_plot, labels=['Group A', 'Group B'], patch_artist=True, showfliers=True)
        # Color the boxes
        colors = ['lightblue', 'lightgreen']
        for patch, color in zip(bp['boxes'], colors):
            patch.set_facecolor(color)
        ax.set_title('Box Plot Example')
        ax.set_ylabel('Value')
        # plt.show()
        ```
    -   **Use Case Scenario:** Comparing salary distributions across different departments, visualizing the range of test scores for different teaching methods.
    -   **Best Way?:** Excellent for summarizing and comparing distributions, especially for identifying median, spread, and outliers. [[Violin_Plot|Violin plots]] can provide more detail about the shape of the distribution.
- Pie Chart
	[[Pie_Chart|Pie Chart (`pie`)]]
    - **Function:** `plt.pie()` or `ax.pie()`
    - **Purpose:** Represents proportions or percentages of categories within a whole. Each slice's angle is proportional to the quantity it represents.
    - **Key Parameters:** `x` (data values/sizes), `labels`, `colors`, `autopct` (format for percentages), `explode` (offset slices), `startangle`.
    - **Example:**
        ```python
        import matplotlib.pyplot as plt
        sizes = # Proportions
        labels = ['Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5']
        explode = (0.1, 0, 0, 0, 0)  # Explode the 1st slice

        fig, ax = plt.subplots()
        ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
               shadow=True, startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        ax.set_title('Pie Chart Example')
        # plt.show()
        ```
    -   **Use Case Scenario:** Showing market share of different companies, representing the composition of a budget by expense categories.
    -   **Best Way?:** Generally discouraged for more than a few categories as it becomes hard to compare slice sizes accurately. Bar charts are often a better alternative for comparing proportions, especially if precise comparison is needed or there are many categories. Best for showing parts of a whole when there are few distinct parts.

---