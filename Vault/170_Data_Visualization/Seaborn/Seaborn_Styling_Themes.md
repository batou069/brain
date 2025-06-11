---
tags:
  - seaborn
  - python
  - plotting
  - data_visualization
  - styling
  - themes
  - color_palettes
  - concept
  - example
aliases:
  - Seaborn Themes
  - Seaborn Color Palettes
  - Seaborn Plot Styling
  - sns.set_theme
related:
  - "[[170_Data_Visualization/Seaborn/_Seaborn_MOC|_Seaborn_MOC]]"
  - "[[Matplotlib_Overview]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-11
---
# Seaborn: Styling and Themes

One of Seaborn's key strengths is its ability to create aesthetically pleasing plots with sensible defaults. It also provides easy ways to customize the appearance of plots using themes, styles, and color palettes. These settings often affect global Matplotlib parameters.

## Setting Themes and Styles
Seaborn offers several pre-defined themes and styles that control the overall look of the plots (e.g., background color, gridlines, font).

-   **`sns.set_theme(**kwargs)` (Recommended for modern Seaborn):**
    -   This is the primary function for setting the theme. It updates Matplotlib's RC parameters.
    -   Key Parameters:
        -   `context`: `{'paper', 'notebook', 'talk', 'poster'}`. Scales plot elements (font sizes, line widths) for different contexts. Default is 'notebook'.
        -   `style`: `{'darkgrid', 'whitegrid', 'dark', 'white', 'ticks'}`. Affects background, grid, and axes spines.
        -   `palette`: Name of a Seaborn color palette or a list of colors. See below.
        -   `font`, `font_scale`: Font family and scaling factor.
    -   Example:
        ```python
        import seaborn as sns
        import matplotlib.pyplot as plt
        import numpy as np

        # sns.set_theme(style="whitegrid", palette="pastel", font_scale=1.2)
        
        # Example plot that will use the theme
        # x = np.linspace(0, 10, 100)
        # y = np.sin(x)
        # plt.figure(figsize=(6,4))
        # plt.plot(x, y)
        # plt.title("Plot with Seaborn Theme ('whitegrid', 'pastel')")
        # plt.show()

        # Reset to Matplotlib defaults (if needed for other plots)
        # sns.reset_defaults() 
        ```

-   **`sns.set_style(style=None, rc=None)` (Older, still works):**
    -   Sets the aesthetic style of the plots.
    -   `style`: `{'darkgrid', 'whitegrid', 'dark', 'white', 'ticks'}`.
    -   `rc`: Dictionary of Matplotlib RC parameters to override.
-   **`sns.set_context(context=None, font_scale=1, rc=None)` (Older, still works):**
    -   Sets the plotting context parameters.
    -   `context`: `{'paper', 'notebook', 'talk', 'poster'}`.

**Available Styles:**
-   `darkgrid`: Dark gray background with white gridlines (default in older Seaborn).
-   `whitegrid`: White background with gray gridlines.
-   `dark`: Dark gray background, no gridlines.
-   `white`: White background, no gridlines.
-   `ticks`: White background with ticks on axes (spines might be offset).

## Color Palettes
Seaborn provides powerful tools for working with colors, making it easy to create plots that are both attractive and effectively convey information.

-   **`sns.color_palette(palette=None, n_colors=None, desat=None)`:**
    -   Returns a list of RGB tuples representing a color palette.
    -   `palette`: Can be:
        -   Name of a Seaborn palette (e.g., 'deep', 'muted', 'pastel', 'bright', 'dark', 'colorblind').
        -   Name of a Matplotlib colormap (e.g., 'viridis', 'coolwarm', 'Blues').
        -   "HUSL" or "HSL" system colors.
        -   "Color Brewer" palettes (e.g., 'Set1', 'Paired', 'YlGnBu').
        -   A list of colors (e.g., `['red', '#00FF00', (0,0,1)]`).
    -   `n_colors`: Number of colors in the palette.
    -   `desat`: Proportion to desaturate each color.
-   **`sns.set_palette(palette, n_colors=None, desat=None, color_codes=False)`:**
    -   Sets the default color palette for all plots.
-   **Types of Palettes:**
    -   **Qualitative:** For representing categorical data where categories have no inherent order (e.g., `sns.color_palette("pastel")`, `sns.color_palette("Set2")`).
    -   **Sequential:** For representing numerical data that progresses from low to high (e.g., `sns.color_palette("Blues")`, `sns.light_palette("green")`).
    -   **Diverging:** For representing numerical data where values diverge from a central point (e.g., correlations ranging from negative to positive, `sns.color_palette("coolwarm")`, `sns.diverging_palette(220, 20, n=7)`).

**Example using color palettes:**
```python
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# sns.set_theme() # Apply default theme for consistency

# Example with a qualitative palette
# current_palette = sns.color_palette("Set2", 5) # Get 5 colors from Set2
# sns.palplot(current_palette) # Plot the palette itself
# plt.title("Seaborn 'Set2' Qualitative Palette (5 colors)")
# plt.show()

# Example with a sequential palette
# sequential_palette = sns.color_palette("YlGnBu", 7)
# sns.palplot(sequential_palette)
# plt.title("Seaborn 'YlGnBu' Sequential Palette (7 colors)")
# plt.show()

# Example with a diverging palette
# diverging_palette = sns.diverging_palette(250, 15, s=75, l=40, n=9, center="light") # hue1, hue2, saturation, lightness, num_colors
# sns.palplot(diverging_palette)
# plt.title("Custom Diverging Palette")
# plt.show()

# Using a palette in a plot
# data = pd.DataFrame(np.random.rand(10, 3), columns=['A', 'B', 'C'])
# data['category'] = np.random.choice(['X', 'Y', 'Z'], 10)
# sns.scatterplot(data=data, x='A', y='B', hue='category', palette='bright')
# plt.title("Scatter Plot with 'bright' Palette")
# plt.show()
```

## Temporarily Setting Styles (`with sns.axes_style()`)
You can temporarily change the style for a specific plot or block of code using a context manager:
```python
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# x = np.arange(10)
# y = x * 2

# Default style (or previously set theme)
# plt.figure(figsize=(5,3))
# plt.plot(x, y)
# plt.title("Plot with Default/Current Style")
# plt.show()

# with sns.axes_style("darkgrid"):
#     # This plot will have the 'darkgrid' style
#     plt.figure(figsize=(5,3))
#     plt.plot(x, y + 5)
#     plt.title("Plot with 'darkgrid' Style (Temporary)")
#     plt.show()

# Plot after the 'with' block reverts to the previous style
# plt.figure(figsize=(5,3))
# plt.plot(x, y + 10)
# plt.title("Plot with Default/Current Style Again")
# plt.show()
```
Similarly, `sns.plotting_context()` can be used as a context manager.

## Despining (`sns.despine()`)
This function can remove the top and right axes spines, which can often make plots look cleaner.
```python
# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.set_style("ticks") # A style where despining is common
# plt.figure(figsize=(5,3))
# plt.plot(range(5), range(5))
# sns.despine(offset=10, trim=True) # Remove top/right spines, offset them slightly
# plt.title("Plot with Despined Axes")
# plt.show()
```

By combining themes, styles, and color palettes, Seaborn allows for the creation of publication-quality statistical graphics with relative ease, while still allowing for fine-grained Matplotlib customization when needed.

---