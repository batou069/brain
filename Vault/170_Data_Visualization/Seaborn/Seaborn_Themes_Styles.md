---
tags:
  - seaborn
  - python
  - plotting
  - data_visualization
  - themes
  - styles
  - aesthetics
  - concept
  - example
aliases:
  - Seaborn Plot Styling
  - sns.set_theme
  - sns.set_style
  - sns.set_palette
  - Seaborn Aesthetics
related:
  - "[[170_Data_Visualization/Seaborn/_Seaborn_MOC|_Seaborn_MOC]]"
  - "[[Matplotlib_Overview]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-09
---
# Seaborn: Themes and Styles

One of Seaborn's key strengths is its ability to create aesthetically pleasing plots with sensible defaults. It offers several built-in themes and styles that can be easily applied to change the overall look and feel of your visualizations. You can also customize color palettes.

## Managing Plot Aesthetics

[list2tab|#Aesthetic Controls]
- `sns.set_theme()` (Recommended way since Seaborn v0.11)
    - **Purpose:** A comprehensive function to set the theme, including style, palette, font, and font scale, all at once or individually. This is the modern way to manage aesthetics.
    - **Key Parameters:**
        -   `style`: Name of a Seaborn style (see `sns.set_style()`) or a dictionary of Matplotlib rcParams.
        -   `palette`: Name of a Seaborn color palette (see `sns.set_palette()`) or other palette specifications.
        -   `font`: Font family.
        -   `font_scale`: Separate scaling factor for font elements.
        -   `rc`: Dictionary of Matplotlib rcParams to override.
    - **Example:**
        ```python
        import seaborn as sns
        import matplotlib.pyplot as plt
        tips = sns.load_dataset("tips")

        # Apply a comprehensive theme
        # sns.set_theme(style="whitegrid", palette="pastel", font_scale=1.2)

        # sns.scatterplot(x="total_bill", y="tip", hue="day", data=tips)
        # plt.title("Plot with Custom Theme")
        # plt.show()

        # Reset to defaults for subsequent plots if needed
        # sns.set_theme() # Resets to Seaborn's defaults
        ```
- `sns.set_style(style=None, rc=None)` (Older, still functional)
    - **Purpose:** Sets the aesthetic style of the plots. Affects things like background color, gridlines, and spines.
    - **Predefined Styles:**
        -   `'darkgrid'` (default): Dark gray grid, white background. Good for plots with many lines/points.
        -   `'whitegrid'`: White background with a grid.
        -   `'dark'`: Dark gray background, no grid.
        -   `'white'`: White background, no grid.
        -   `'ticks'`: White background with ticks on axes (spines are visible).
    - **`rc` parameter:** Allows overriding specific Matplotlib rcParams.
    - **Example:**
        ```python
        # sns.set_style("darkgrid")
        # sns.histplot(tips["total_bill"])
        # plt.title("Darkgrid Style")
        # plt.show()

        # sns.set_style("white")
        # sns.kdeplot(tips["total_bill"], fill=True)
        # plt.title("White Style")
        # plt.show()
        ```
- `sns.set_palette(palette=None, n_colors=None, desat=None, color_codes=False)` (Older, still functional)
    - **Purpose:** Sets the default color palette for plots. Affects colors used for `hue` semantics, etc.
    - **Palettes:**
        -   Named Seaborn palettes (e.g., `'deep'`, `'muted'`, `'pastel'`, `'bright'`, `'dark'`, `'colorblind'`).
        -   Matplotlib colormap names (e.g., `'viridis'`, `'coolwarm'`).
        -   Specific color lists (e.g., `['red', 'blue', 'green']`).
        -   Specialized palette functions like `sns.color_palette("husl", 8)` or `sns.diverging_palette(220, 20, n=7)`.
    - **Example:**
        ```python
        # sns.set_style("whitegrid") # Set a style first

        # sns.set_palette("husl", 8) # Set HUSL palette with 8 colors
        # sns.boxplot(x="day", y="total_bill", data=tips)
        # plt.title("HUSL Palette")
        # plt.show()

        # sns.set_palette("Set2") # Another qualitative palette
        # sns.violinplot(x="day", y="total_bill", data=tips)
        # plt.title("Set2 Palette")
        # plt.show()
        ```
- `sns.set_context(context=None, font_scale=1, rc=None)`
    - **Purpose:** Sets the plotting context parameters. Affects the scale of plot elements like labels, lines, and points, making plots suitable for different contexts (e.g., notebook, paper, talk, poster).
    - **Predefined Contexts:**
        -   `'notebook'` (default)
        -   `'paper'`
        -   `'talk'`
        -   `'poster'`
    - **`font_scale`:** Scales font sizes independently.
    - **Example:**
        ```python
        # sns.set_style("ticks")
        # sns.set_context("talk", font_scale=1.1) # Larger elements for a talk
        # sns.scatterplot(x="total_bill", y="tip", data=tips)
        # plt.title("Plot in 'Talk' Context")
        # plt.show()

        # Reset to default context for other plots
        # sns.set_context("notebook")
        ```
- Removing Spines (`sns.despine()`)
    - **Purpose:** Removes the top and right spines from a plot, which can make plots look cleaner. Often used with `'white'` or `'ticks'` styles.
    - **Parameters:** `fig`, `ax`, `top`, `right`, `left`, `bottom`, `offset`, `trim`.
    - **Example:**
        ```python
        # sns.set_style("white")
        # ax = sns.lineplot(x=range(10), y=np.random.randn(10))
        # sns.despine(ax=ax, offset=10, trim=True) # Remove top/right, offset axes, trim spines
        # ax.set_title("Despined Plot")
        # plt.show()
        ```
- Using `with` statement for temporary styling (Context Manager)
    - **Purpose:** To apply a style or context temporarily for a specific block of code.
    - **Example:**
        ```python
        # with sns.axes_style("darkgrid"):
        #     plt.figure()
        #     sns.histplot(tips["total_bill"])
        #     plt.title("Temporary Darkgrid Style")
        #     # plt.show()

        # Style outside the 'with' block reverts to previous or default
        # plt.figure()
        # sns.kdeplot(tips["total_bill"])
        # plt.title("Default/Previous Style After 'with'")
        # plt.show()
        ```

## Color Palettes
Seaborn offers a rich set of tools for working with colors:
-   **Qualitative Palettes:** For distinguishing categorical data where order doesn't matter (e.g., `sns.color_palette("pastel")`, `sns.color_palette("Set2")`).
-   **Sequential Palettes:** For numerical or ordered categorical data where values range from low to high (e.g., `sns.color_palette("Blues")`, `sns.light_palette("green")`).
-   **Diverging Palettes:** For numerical data where there's a meaningful midpoint, and values diverge in two directions (e.g., `sns.color_palette("coolwarm")`, `sns.diverging_palette(220, 20, as_cmap=True)`).
-   You can set a palette for a specific plot using the `palette=` argument in most Seaborn functions.

By effectively using these styling functions, you can significantly enhance the readability and aesthetic appeal of your Seaborn visualizations, tailoring them to your specific needs and audience.

---