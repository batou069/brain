---
tags:
  - matplotlib
  - python
  - plotting
  - data_visualization
  - customization
  - titles
  - labels
  - legends
  - colors
  - linestyles
  - markers
  - concept
  - example
aliases:
  - Customizing Matplotlib Plots
  - Matplotlib Plot Styling
related:
  - "[[160_Python_Libraries/170_Data_Visualization/Matplotlib/_Matplotlib_MOC|_Matplotlib_MOC]]"
  - "[[Matplotlib_Figure_Subplot_Axes]]"
  - "[[Matplotlib_Pyplot_API_vs_OO_API]]"
  - "[[Plot_Elements_Anatomy]]"
  - "[[Matplotlib_Colormaps]]"
  - "[[Matplotlib_Styles]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-11
---
# Matplotlib: Customizing Plots

Matplotlib offers extensive control over virtually every aspect of a plot, allowing for highly customized, publication-quality visualizations. Customizations can be applied to figures, axes, lines, markers, text, legends, and more. This is typically done using methods of the `Figure` and `Axes` objects in the [[Matplotlib_Pyplot_API_vs_OO_API|Object-Oriented API]], or corresponding functions in the `pyplot` API.

## Key Areas of Customization

[list2tab|#Matplotlib Customization]
- Titles and Labels
    -   **Purpose:** Provide context and describe the plot and its axes.
    -   **Object-Oriented API (`ax` is an `Axes` object, `fig` is a `Figure` object):**
        -   `ax.set_title("My Plot Title", fontsize=16, color='darkblue')`
        -   `ax.set_xlabel("X-axis Label (Units)", fontsize=12)`
        -   `ax.set_ylabel("Y-axis Label (Units)", fontsize=12)`
        -   `fig.suptitle("Overall Figure Title", fontsize=18, y=1.02)` (y for positioning)
    -   **Pyplot API:**
        -   `plt.title("My Plot Title")`
        -   `plt.xlabel("X-axis Label")`
        -   `plt.ylabel("Y-axis Label")`
    -   **Example (Customizing titles and labels for an e-commerce sales plot):**
        ```python
        import matplotlib.pyplot as plt
        import numpy as np

        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        sales = 
        
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(months, sales, marker='o')
        
        ax.set_title("Monthly Product Sales Trend", fontsize=16, fontweight='bold', color='navy')
        ax.set_xlabel("Month", fontsize=14, fontstyle='italic')
        ax.set_ylabel("Sales ($ Thousands)", fontsize=14)
        
        # fig.suptitle("E-commerce Performance Q1-Q2", fontsize=20, y=0.98) # If you want a figure-level title
        # plt.tight_layout(rect=[0, 0, 1, 0.95]) # Adjust for suptitle
        # plt.show()
        ```
- Lines and Markers (in `ax.plot()` or `ax.scatter()`)
    -   **Purpose:** Control the appearance of plotted lines and data points.
    -   **Common Parameters for `ax.plot()`:**
        -   `color` (or `c`): Color of the line/marker (e.g., 'red', '#FF0000', `(0.1, 0.2, 0.5)`).
        -   `linestyle` (or `ls`): Style of the line (e.g., `'-'`, `'--'`, `':'`, `'-.'`).
        -   `linewidth` (or `lw`): Width of the line.
        -   `marker`: Shape of the marker (e.g., `'o'`, `'s'`, `'^'`, `'D'`, `'+'`, `'x'`).
        -   `markersize` (or `ms`): Size of the marker.
        -   `markeredgecolor` (or `mec`): Color of marker edge.
        -   `markerfacecolor` (or `mfc`): Fill color of marker.
        -   `alpha`: Transparency (0.0 to 1.0).
    -   **Common Parameters for `ax.scatter()`:**
        -   `s`: Size of markers (can be a scalar or an array for variable sizes).
        -   `c`: Color of markers (can be a single color, an array of colors, or an array of values to be mapped by a colormap).
        -   `marker`: Marker style.
        -   `alpha`: Transparency.
        -   `cmap`: Colormap if `c` is an array of values.
        -   `edgecolors`: Color of marker edges.
    -   **Example (Customizing line and scatter plots for product A vs B sales):**
        ```python
        # (Continuing with months data)
        # sales_product_A = 
        # sales_product_B = 
        # customer_satisfaction = np.random.rand(len(months)) * 5 # 0-5 scale

        # fig, ax = plt.subplots(figsize=(10, 6))
        # ax.plot(months, sales_product_A, color='dodgerblue', linestyle='-', linewidth=2.5,
        #         marker='o', markersize=8, markerfacecolor='lightblue', markeredgecolor='blue',
        #         label='Product A Sales')
        # ax.plot(months, sales_product_B, color='orangered', linestyle='--', linewidth=2,
        #         marker='s', markersize=7, mfc='peachpuff', mec='darkred',
        #         label='Product B Sales')
        
        # Conceptual scatter plot overlaid (e.g., satisfaction vs. time)
        # ax2 = ax.twinx() # Create a second y-axis for a different scale
        # ax2.scatter(months, customer_satisfaction, color='green', marker='^', s=100, alpha=0.6,
        #             label='Avg Satisfaction (0-5)', edgecolors='darkgreen')
        # ax2.set_ylabel("Customer Satisfaction Score", color='green', fontsize=12)
        # ax2.tick_params(axis='y', labelcolor='green')

        # ax.set_title("Product Sales and Customer Satisfaction Over Time", fontsize=16)
        # ax.set_xlabel("Month", fontsize=12)
        # ax.set_ylabel("Monthly Sales ($ Thousands)", fontsize=12)
        # fig.legend(loc="upper center", bbox_to_anchor=(0.5, 0.95), ncol=3) # Unified legend
        # ax.grid(True, linestyle=':', alpha=0.7)
        # plt.tight_layout(rect=[0, 0, 1, 0.9])
        # plt.show()
        ```
- [[Plot_Elements_Anatomy#Ticks_and_Tick_Marks|Ticks, Tick Labels]], and [[Plot_Elements_Anatomy#Gridlines|Gridlines]]
    -   **Purpose:** Control the appearance and frequency of axis ticks, their labels, and grid lines.
    -   **Axes Methods:**
        -   `ax.set_xticks()` / `ax.set_yticks()`: Set the locations of major ticks.
        -   `ax.set_xticklabels()` / `ax.set_yticklabels()`: Set the labels for major ticks.
        -   `ax.tick_params(axis='both', which='major', labelsize=10, colors='gray', direction='inout', length=6, ...)`: Fine-grained control over tick appearance.
        -   `ax.minorticks_on()` / `ax.minorticks_off()`: Toggle minor ticks.
        -   `ax.grid(True/False, which='major'/'minor', axis='x'/'y'/'both', color='gray', linestyle=':', linewidth=0.5)`: Configure grid lines.
    -   **Example (Customizing ticks and grid for a financial chart):**
        ```python
        # dates = pd.to_datetime(['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01'])
        # stock_prices = 
        
        # fig, ax = plt.subplots(figsize=(10,5))
        # ax.plot(dates, stock_prices)
        
        # ax.set_title("Stock Price Trend (Custom Ticks/Grid)", fontsize=15)
        # ax.set_xlabel("Date", fontsize=12)
        # ax.set_ylabel("Price (USD)", fontsize=12)
        
        # X-axis tick customization (e.g., monthly ticks, formatted dates)
        # import matplotlib.dates as mdates
        # ax.xaxis.set_major_locator(mdates.MonthLocator())
        # ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y')) # E.g., Jan 2023
        # plt.xticks(rotation=45, ha='right')

        # Y-axis tick customization
        # ax.set_yticks(np.arange(min(stock_prices)//10*10, max(stock_prices)//10*10 + 10, 10)) # Ticks every $10
        # ax.tick_params(axis='y', which='major', labelsize=10, colors='darkgreen')

        # Grid customization
        # ax.grid(True, which='major', axis='y', linestyle='--', linewidth=0.7, color='lightgray')
        # ax.grid(True, which='major', axis='x', linestyle=':', linewidth=0.5, color='silver')
        
        # plt.tight_layout()
        # plt.show()
        ```
- [[Plot_Elements_Anatomy#Legend|Legends]]
    -   **Purpose:** Identify different plotted data series.
    -   **Axes Method:** `ax.legend()`
    -   **Key Parameters for `ax.legend()`:**
        -   `loc`: Location string (e.g., `'upper right'`, `'best'`, `'center left'`) or a 2-tuple `(x,y)`.
        -   `title`: Legend title.
        -   `fontsize`.
        -   `ncol`: Number of columns in the legend.
        -   `frameon`: Whether to draw a frame around the legend.
        -   `fancybox`, `shadow`.
    -   Requires `label` argument to be set in plotting commands (e.g., `ax.plot(..., label='Series A')`).
    -   **Example (from Line/Marker example above, or):**
        ```python
        # fig, ax = plt.subplots()
        # ax.plot(x, y1, label='Data A')
        # ax.plot(x, y2, label='Data B')
        # ax.legend(loc='lower center', ncol=2, fontsize='small', title='Datasets', frameon=False)
        # plt.show()
        ```
- Text and Annotations
    -   **Purpose:** Add textual information or highlight specific points on the plot.
    -   **Axes Methods:**
        -   `ax.text(x, y, "My Text", fontsize=10, color='red', ...)_`: Adds text at data coordinates `(x,y)`.
        -   `ax.annotate("Annotation Text", xy=(x_point, y_point), xytext=(x_text, y_text), arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5), ...)`: Adds text with an arrow pointing from `xytext` to `xy`.
    -   **Example (Annotating a peak in product sales):**
        ```python
        # (Using months, sales data from first example)
        # peak_sales_month_idx = np.argmax(sales)
        # peak_month = months[peak_sales_month_idx]
        # peak_value = sales[peak_sales_month_idx]

        # fig, ax = plt.subplots()
        # ax.plot(months, sales, marker='.')
        # ax.set_title("Monthly Sales with Peak Annotated")
        # ax.annotate(f"Peak Sale: ${peak_value:.0f}K",
        #             xy=(peak_month, peak_value), # Point to annotate
        #             xytext=(peak_month, peak_value + 10), # Position of text
        #             arrowprops=dict(facecolor='black', shrink=0.05, width=0.5, headwidth=4),
        #             fontsize=9, ha='center'
        #            )
        # ax.text(0.05, 0.95, "Data from Q1-Q2 2023", transform=ax.transAxes, ha='left', va='top', fontsize=8, style='italic')
        # plt.show()
        ```
- Colors and [[Matplotlib_Colormaps|Colormaps]]
    -   Colors can be specified by name, hex code, RGB(A) tuple.
    -   Colormaps (`cmap` argument in functions like `scatter`, `imshow`, `pcolormesh`) map numerical data to colors. See [[Matplotlib_Colormaps]].
- Figure Size and Layout
    -   `fig, ax = plt.subplots(figsize=(width_inches, height_inches))`
    -   `fig.set_dpi(dots_per_inch)`
    -   `plt.tight_layout()` or `fig.tight_layout()`: Adjusts subplot params for a tight layout.
    -   `plt.subplots_adjust(left=..., right=..., top=..., bottom=..., wspace=..., hspace=...)`: Fine-tune spacing.

Mastering these customization options allows you to tailor Matplotlib plots precisely to your needs, enhancing clarity and impact. Referencing the [[Plot_Elements_Anatomy]] note provides a good overview of what can be styled.

---