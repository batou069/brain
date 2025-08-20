---
tags:
  - matplotlib
  - python
  - plotting
  - styles
  - themes
  - aesthetics
  - concept
  - example
aliases:
  - Matplotlib Stylesheets
  - Plot Styles
  - plt.style.use
related:
  - "[[Matplotlib_Overview]]"
  - "[[Matplotlib_Customization]]"
  - "[[Seaborn_Themes_Styles]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-08-20
---
# Matplotlib: Using Stylesheets (`plt.style`)

Matplotlib provides a way to customize the overall look and feel of your plots using **stylesheets**. A stylesheet contains a set of predefined parameters (rcParams) that control various aspects like colors, line widths, font sizes, grid appearance, etc. This allows you to easily switch between different visual themes for your plots without manually changing individual parameters for each plot.

The `plt.style` module is used to manage and apply these styles.

## Key `plt.style` Functionality

[list2tab|#Style Functions]
- `plt.style.available` (Attribute)
    -   A list of strings containing the names of all available built-in styles.
    -   **Example:**
        ```python
        import matplotlib.pyplot as plt
        # print(plt.style.available)
        # Output might include:
        # ['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid',
        #  'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot',
        #  'grayscale', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', ... many more]
        ```
- `plt.style.use(style_name)`
    -   **Purpose:** Applies a specified style globally to all subsequent plots created in the current Python session or script.
    -   `style_name`: Can be a string (name of a built-in style or path to a custom `.mplstyle` file), a list of style names (styles are applied sequentially, later ones overriding earlier ones), or a dictionary of rcParams.
    -   **Example:**
        ```python
        import matplotlib.pyplot as plt
        import numpy as np

        # Apply the 'ggplot' style (popular R plotting package style)
        # plt.style.use('ggplot')

        x = np.linspace(0, 10, 100)
        # fig, ax = plt.subplots()
        # ax.plot(x, np.sin(x), label='sin(x)')
        # ax.plot(x, np.cos(x), label='cos(x)')
        # ax.set_title("'ggplot' Style Example")
        # ax.legend()
        # plt.show()

        # Revert to default (or apply another style for subsequent plots)
        # plt.style.use('default') # 'default' reverts to Matplotlib's default rcParams
        ```
- `plt.style.context(style_name)` (Context Manager)
    -   **Purpose:** Applies a style temporarily within a `with` block. The style reverts to its previous state after exiting the block. This is useful for applying a specific style to a single plot or a group of plots without affecting global settings.
    -   **Example:**
        ```python
        import matplotlib.pyplot as plt
        import numpy as np
        x = np.linspace(0, 10, 100)

        # Plot 1: Default style
        # fig1, ax1 = plt.subplots()
        # ax1.plot(x, np.sin(x))
        # ax1.set_title("Plot with Default Style")
        # plt.show()

        # Plot 2: Temporarily use 'fivethirtyeight' style
        # with plt.style.context('fivethirtyeight'):
        #     fig2, ax2 = plt.subplots()
        #     ax2.plot(x, np.cos(x))
        #     ax2.set_title("Plot with 'fivethirtyeight' Style (Temporary)")
        #     # plt.show() # Show inside context if needed, or after if fig object is used

        # Plot 3: Back to default style
        # fig3, ax3 = plt.subplots()
        # ax3.plot(x, np.tan(x)) # tan might have discontinuities, be careful with ylim
        # ax3.set_ylim(-5, 5)
        # ax3.set_title("Plot with Default Style (Again)")
        # plt.show()
        ```
- Custom Stylesheets (`.mplstyle` files)
    -   You can create your own stylesheet files (with a `.mplstyle` extension) containing `rcParams` settings.
    -   Example `my_custom_style.mplstyle`:
        ```
        axes.titlesize : 20
        axes.labelsize : 16
        lines.linewidth : 3
        lines.markersize : 10
        xtick.labelsize : 12
        ytick.labelsize : 12
        figure.facecolor : lightgrey
        ```
    -   Then use it with `plt.style.use('./my_custom_style.mplstyle')` (provide path to the file).
    -   Stylesheets can also be placed in `matplotlib.get_configdir() + /stylelib/` to be accessible by name.

## Popular Built-in Styles
Some commonly used styles include:
-   **`'ggplot'`:** Mimics the aesthetics of plots from the popular R library `ggplot2`. Often features a gray background, white gridlines, and distinct colors.
-   **`'fivethirtyeight'`:** Emulates the style of the data journalism website FiveThirtyEight, often with thicker lines, specific fonts, and a characteristic look.
-   **`'seaborn-v0_8-*'` variants (e.g., `'seaborn-v0_8-whitegrid'`, `'seaborn-v0_8-darkgrid'`, `'seaborn-v0_8-colorblind'`):** Provide styles similar to those from the [[170_Data_Visualization/Seaborn/_Seaborn_MOC|Seaborn]] library. Using `sns.set_theme()` from Seaborn itself is now the more direct way to get Seaborn's full styling.
-   **`'dark_background'`:** Useful for plots on dark slides or UIs.
-   **`'grayscale'`:** For producing plots in grayscale.
-   **`'classic'`:** Reverts to the Matplotlib 1.x classic style.
-   **`'default'`:** Matplotlib's current default style.

## Combining Styles
You can apply multiple styles by passing a list of style names to `plt.style.use()`. Styles are applied from left to right, so later styles can override settings from earlier ones.
```python
# plt.style.use(['seaborn-v0_8-whitegrid', 'my_custom_settings'])
# This would first apply seaborn-whitegrid, then overlay 'my_custom_settings'.
```

Using stylesheets is a convenient way to achieve consistent and professional-looking plots with minimal effort, allowing you to focus more on the data and less on individual formatting commands for each plot.

---