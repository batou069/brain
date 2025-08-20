
Filename: 170_Data_Visualization/Plot_Types/Box_Plot.md
````markdown
[[Box_Plot]]
````

`````markdown

Filename: 170_Data_Visualization/Plot_Types/Pie_Chart.md

````markdown
[[Pie_Chart]]
````

`````markdown

Filename: 170_Data_Visualization/Plot_Types/Heatmap.md
````markdown
[[Heatmaps]]
````

`````markdown

Filename: 170_Data_Visualization/Plot_Types/Violin_Plot.md
````markdown
[[Violin_Plots]]
````

`````markdown

Filename: 170_Data_Visualization/Plot_Types/Trend_Line.md
````markdown
[[Trend_Line]]
````

`````markdown

Filename: 170_Data_Visualization/Plot_Types/Scatter_Plot_Matrix.md
````markdown
[[Scatter_Plot_Matrix]]
`````

This covers the basic plot types. Next, I'll create the Matplotlib-specific concept notes that were identified (`Matplotlib_Object_Oriented_API.md`, `Matplotlib_Customization.md`, `Matplotlib_Saving_Plots.md`, `Matplotlib_Styles.md`, `Matplotlib_3D_Plotting.md`, `Matplotlib_Interactive_Plots.md`) and then update the `_Matplotlib_MOC.md` to ensure all links are valid.

---


Okay, let's create the Matplotlib-specific concept notes.

---
**Creating Matplotlib Concept Notes:**

`````markdown

Filename: 170_Data_Visualization/Matplotlib/Matplotlib_Object_Oriented_API.md
````markdown
[[Matplotlib_Object_Oriented_API]]
````

`````markdown

Filename: 170_Data_Visualization/Matplotlib/Matplotlib_Customization.md
````markdown

```

---
````

`````markdown

Filename: 170_Data_Visualization/Matplotlib/Matplotlib_Saving_Plots.md
````markdown
---
tags: [matplotlib, python, plotting, saving_figures, export, file_formats, concept, example]
aliases: [Saving Matplotlib Figures, plt.savefig, fig.savefig]
related:
  - "[[Matplotlib_Overview]]"
  - "[[Matplotlib_Figure_Subplot_Axes]]" # Figure object has the savefig method
worksheet: [WS_DataViz_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Matplotlib: Saving Plots to Files

Matplotlib allows you to save your generated plots to a wide variety of file formats, suitable for inclusion in documents, presentations, web pages, or for archival purposes. The primary function for this is `savefig()`.

## `savefig()` Method
This method can be called on a [[Matplotlib_Figure_Subplot_Axes|`Figure` object]] (`fig.savefig()`) in the object-oriented API, or as a `pyplot` function (`plt.savefig()`) which acts on the current figure.

**Syntax (Simplified):**
```python
fig.savefig(fname, dpi=None, format=None, bbox_inches=None, pad_inches=0.1, transparent=False, ...)
plt.savefig(fname, ...) # Similar parameters
```

[list2tab|#savefig Parameters]
- `fname` (Filename or File-like object)
    -   A string representing the path and filename (e.g., `'my_plot.png'`, `'../figures/report_figure.pdf'`).
    -   The file format is often inferred from the extension of `fname`.
    -   Can also be a Python file-like object (e.g., `io.BytesIO`).
- `dpi` (Dots Per Inch)
    -   Integer, controls the resolution of rasterized output formats (like PNG, JPG). Higher DPI means higher resolution and larger file size.
    -   Common values: 100 (screen), 300 (print), 600 (high-quality print).
    -   If `None`, uses the figure's DPI or a default.
- `format`
    -   String, explicitly specifies the output format (e.g., `'png'`, `'pdf'`, `'svg'`, `'jpg'`, `'eps'`, `'tiff'`).
    -   If not provided, Matplotlib tries to infer it from the `fname` extension.
- `bbox_inches`
    -   `'tight'`: Adjusts the bounding box of the saved figure to include all artists, removing excess whitespace. Very useful.
    -   Can also be a `Bbox` object to specify a custom bounding box.
- `pad_inches`
    -   Amount of padding around the figure when `bbox_inches='tight'`.
- `transparent`
    -   Boolean. If `True`, the figure and axes backgrounds will be transparent (if the output format supports transparency, like PNG or SVG).
- `facecolor`, `edgecolor`
    -   The color of the figure background and edge. `fig.patch.set_facecolor('w')` can be used before saving for a white background if the default is different.
- `orientation`
    -   `{'landscape', 'portrait'}` (for formats like PDF that support it).
- `metadata`
    -   Dictionary of metadata to embed in supported formats (e.g., PDF, SVG).

## Supported File Formats
Matplotlib supports numerous output formats. Common ones include:
-   **Raster Formats (Pixel-based):**
    -   `png`: Portable Network Graphics (good for web, lossless compression, supports transparency).
    -   `jpg` or `jpeg`: Joint Photographic Experts Group (good for photographs, lossy compression).
    -   `tiff`: Tagged Image File Format (often used for high-quality print, can be lossless or lossy).
    -   `bmp`: Bitmap.
-   **Vector Formats (Scalable):**
    -   `pdf`: Portable Document Format (excellent for documents, scalable, widely supported).
    -   `svg`: Scalable Vector Graphics (good for web, XML-based, scalable, editable in vector graphics software).
    -   `eps`: Encapsulated PostScript (older vector format, common in academic publishing with LaTeX).
    -   `ps`: PostScript.

Vector formats are generally preferred for line art, text, and plots that need to be scaled without loss of quality. Raster formats are suitable for images with complex color gradients or when file size for web display is a concern (e.g., JPG for photos).

## Example Usage

```python
import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plot (OO API example)
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(x, y, label='sin(x)')
ax.set_title('Sine Wave Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.legend()
ax.grid(True)

# --- Saving the plot ---

# 1. Save as PNG (common raster format)
# fig.savefig('sine_wave.png', dpi=300) # Save with 300 DPI
# print("Plot saved as sine_wave.png")

# 2. Save as PDF (common vector format for documents)
# fig.savefig('sine_wave.pdf', bbox_inches='tight') # 'tight' removes extra whitespace
# print("Plot saved as sine_wave.pdf")

# 3. Save as SVG (scalable vector format for web/editing)
# fig.savefig('sine_wave.svg', transparent=True) # Save with transparent background
# print("Plot saved as sine_wave.svg")

# 4. Using pyplot interface (acts on the current figure)
# plt.plot(x, np.cos(x)) # Add another plot to the current figure/axes
# plt.title("Another Plot on Current Figure")
# plt.savefig('current_figure_plot.jpg', format='jpeg', quality=90) # Specify format and JPG quality
# print("Plot saved as current_figure_plot.jpg")

# Important: plt.show() often clears the figure in some environments.
# It's generally good practice to save BEFORE calling plt.show() if you are in a script.
# In Jupyter notebooks, figures often persist after show().
# plt.show()
```

## Tips for Saving Figures
-   **Save Before `plt.show()`:** In scripts, `plt.show()` can sometimes clear the figure, so save it before calling `show()`. In interactive environments like Jupyter, this is less of an issue.
-   **`bbox_inches='tight'`:** This is very useful for creating well-cropped figures without excessive whitespace, especially for inclusion in documents.
-   **Choose Appropriate DPI:** For raster formats, select a DPI suitable for the intended use (e.g., 72-100 DPI for web/screen, 300+ DPI for print).
-   **Vector vs. Raster:** Use vector formats (PDF, SVG, EPS) when scalability and crisp lines/text are important (e.g., publications). Use raster formats (PNG, JPG) for web display where file size might be a concern or for images with complex color gradients.
-   **Transparency:** Use `transparent=True` with PNG or SVG if you need the plot background to be transparent (e.g., for overlaying on other content).
-   **Consistent Figure Size:** Set `figsize` when creating the figure (`plt.figure(figsize=(w,h))` or `plt.subplots(figsize=(w,h))`) to control the aspect ratio and initial size, which affects how text and elements are scaled when saved.

Saving plots effectively is crucial for sharing and documenting your data visualizations.

---
````

`````markdown

Filename: 170_Data_Visualization/Matplotlib/Matplotlib_Styles.md
````markdown
[[Matplotlib_Styles]]
````

`````markdown

Filename: 170_Data_Visualization/Matplotlib/Matplotlib_3D_Plotting.md
````markdown
[[Matplotlib_3D_Plotting]]
````

`````markdown

Filename: 170_Data_Visualization/Matplotlib/Matplotlib_Interactive_Plots.md
````markdown
---
tags: [matplotlib, python, plotting, interactive_plots, jupyter, ipympl, widgets, concept]
aliases: [Interactive Matplotlib, Matplotlib Widgets]
related:
  - "[[Matplotlib_Overview]]"
  - "[[Matplotlib_Figure_Subplot_Axes]]"
  - "[[Jupyter_Notebook_Lab]]" # Common environment for interactive plotting
worksheet: [WS_DataViz_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Matplotlib: Interactive Plots

While Matplotlib is primarily known for generating static plots, it also supports varying degrees of interactivity, especially when used within certain environments or with specific backends. True web-native interactivity like that found in [[Plotly_and_Plotly_Express|Plotly]] or [[Bokeh_Library|Bokeh]] is not its core strength, but useful interactive features are available.

## Interactivity in Different Environments

1.  **Standard Matplotlib Window (GUI Backends):**
    -   When Matplotlib uses a GUI backend (like Qt5Agg, TkAgg, WXAgg, MacOSX), the plot window that appears typically has built-in interactive tools:
        -   **Pan/Zoom:** Buttons to pan (move the plot around) and zoom into specific regions.
        -   **Save:** Button to save the figure.
        -   **Configure Subplots:** Tool to adjust subplot layout parameters.
        -   **Home/Back/Forward:** Navigate view history.
    -   This is the default behavior when running a Matplotlib script outside of environments like Jupyter.

2.  **Jupyter Notebook / JupyterLab:**
    -   **`%matplotlib inline` (Default):**
        -   Renders static PNG images embedded directly in the notebook. No interactivity beyond the generated image.
    -   **`%matplotlib notebook` (Older, classic Jupyter Notebook):**
        -   Renders interactive plots within the notebook output cell. Provides zoom, pan, and other tools similar to GUI backends.
        -   Can be a bit clunky and is less favored now.
    -   **`%matplotlib widget` (Recommended for JupyterLab, also works in Notebook):**
        -   Uses the `ipympl` backend to provide fully interactive figures directly in the notebook or JupyterLab.
        -   Offers smoother panning, zooming, and the ability to connect Python widgets (from `ipywidgets`) to control plot elements dynamically.
        -   Requires `ipympl` to be installed: `pip install ipympl jupyterlab_widgets`.
        -   **Example (`%matplotlib widget`):**
            ```python
            # In a Jupyter Notebook/Lab cell, run this first:
            # %matplotlib widget 
            
            import matplotlib.pyplot as plt
            import numpy as np

            fig, ax = plt.subplots()
            x = np.linspace(0, 10, 100)
            line, = ax.plot(x, np.sin(x)) # Get the line object

            # Example of updating plot (more complex interactivity involves widgets)
            # def update(change): # Conceptual, would be tied to a widget
            #    line.set_ydata(np.sin(x * change.new))
            #    fig.canvas.draw_idle()
            
            # Simple plot that will be interactive with this backend
            ax.set_title("Interactive Plot with %matplotlib widget")
            ax.grid(True)
            # plt.show() # Often not needed with %matplotlib widget, plot appears directly
            ```

## Event Handling
Matplotlib has an event handling system that allows you to connect to events like mouse clicks, key presses, or pick events (clicking on an artist). This enables building custom interactive behaviors.

-   `fig.canvas.mpl_connect('event_name', callback_function)`
-   **Common Event Names:** `'button_press_event'`, `'button_release_event'`, `'motion_notify_event'`, `'key_press_event'`, `'pick_event'`.
-   **Callback Function:** A Python function that takes an `event` object as an argument and performs actions based on the event (e.g., update plot, print coordinates).

**Conceptual Example (Event Handling):**
```python
import matplotlib.pyplot as plt
import numpy as np

# fig, ax = plt.subplots()
# points, = ax.plot(np.random.rand(10), np.random.rand(10), 'o', picker=5) # picker=5 means pick event within 5 points

# def on_pick(event):
#     artist = event.artist
#     xmouse, ymouse = event.mouseevent.xdata, event.mouseevent.ydata
#     ind = event.ind
#     print(f"Picked point(s) at index: {ind}")
#     print(f"Data coordinates: X={artist.get_xdata()[ind]}, Y={artist.get_ydata()[ind]}")
#     print(f"Mouse coordinates: x={xmouse:.2f}, y={ymouse:.2f}\n")

# fig.canvas.mpl_connect('pick_event', on_pick)

# ax.set_title("Click on points to trigger pick event")
# plt.show()
```

## Matplotlib Widgets
Matplotlib also provides a basic set of GUI-neutral widgets (in `matplotlib.widgets`) like `Slider`, `Button`, `RadioButtons`, `CheckButtons`, `TextBox`. These can be used to control plot parameters interactively, but they are more involved to set up compared to using `ipywidgets` with `%matplotlib widget`.

**Example (Conceptual Slider):**
```python
# from matplotlib.widgets import Slider
# ... (setup plot) ...
# ax_slider = plt.axes([0.25, 0.02, 0.50, 0.03]) # Position for slider
# freq_slider = Slider(
#     ax=ax_slider,
#     label='Frequency',
#     valmin=0.1,
#     valmax=10.0,
#     valinit=1.0
# )
# def update_freq(val):
#     line.set_ydata(np.sin(val * x)) # Assuming 'line' and 'x' are defined
#     fig.canvas.draw_idle()
# freq_slider.on_changed(update_freq)
# plt.show()
```

## Limitations Compared to Web-Native Libraries
-   **Web Embedding:** While plots can be saved as images (PNG, SVG) for web use, creating truly interactive web applications with Matplotlib typically requires integration with frameworks like Flask/Django and potentially custom JavaScript, or using the `ipympl` backend which renders to an HTML5 canvas. Libraries like [[Plotly_and_Plotly_Express|Plotly]], [[Bokeh_Library|Bokeh]], and [[Altair_Library|Altair]] are designed from the ground up for web-native interactivity and are generally easier for this purpose.
-   **Complexity of Advanced Interactivity:** Building complex interactive dashboards with many linked components and custom behaviors can be more involved in Matplotlib than with libraries specifically designed for such applications (e.g., Dash, Bokeh Server, Streamlit).

**Summary:**
Matplotlib offers good basic interactivity through its GUI backends and especially with the `ipympl` backend in Jupyter environments. For highly sophisticated, web-native interactive dashboards or applications, dedicated libraries like Plotly, Bokeh, or Altair are often more suitable. However, for scientific plotting where the primary output might be static figures but some level of exploration is needed, Matplotlib's interactive features are very useful.

---
````

Now I will update the `170_Data_Visualization/Matplotlib/_Matplotlib_MOC.md` to ensure all links are correct and point to the newly created or existing notes.

---
**Revised `170_Data_Visualization/Matplotlib/_Matplotlib_MOC.md`**

`````markdown

Filename: 170_Data_Visualization/Matplotlib/_Matplotlib_MOC.md
````markdown
---
tags: [matplotlib, python, plotting, data_visualization, library, moc, concept]
aliases: [Matplotlib Library MOC]
related:
  - "[[_Data_Visualization_MOC]]"
  - "[[_NumPy_MOC]]"
  - "[[_Pandas_MOC]]"
  - "[[Matplotlib_Overview]]"
  - "[[Matplotlib_Pyplot_API_vs_OO_API]]"
  - "[[Matplotlib_Figure_Subplot_Axes]]"
  - "[[Matplotlib_Basic_Plotting_Functions]]"
  - "[[Matplotlib_Customization]]"
  - "[[Matplotlib_Image_Display_imshow]]"
  - "[[Matplotlib_Colormaps]]"
  - "[[Matplotlib_3D_Plotting]]"
  - "[[Matplotlib_Interactive_Plots]]"
  - "[[Matplotlib_Saving_Plots]]"
  - "[[Matplotlib_Styles]]"
worksheet: [WS_DataViz_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Matplotlib MOC 🎨

**[[Matplotlib_Overview|Matplotlib]]** is a comprehensive library for creating static, animated, and interactive visualizations in Python. It is the foundational plotting library in the Python scientific computing stack.

## Core Concepts & Usage
-   [[Matplotlib_Overview|Overview of Matplotlib]]
-   [[Matplotlib_Pyplot_API_vs_OO_API|Pyplot API vs. Object-Oriented API]]
    -   [[Matplotlib_Pyplot_API|Pyplot API (State-Based)]]
    -   [[Matplotlib_Object_Oriented_API|Object-Oriented API]]
-   [[Matplotlib_Figure_Subplot_Axes|Figure, Axes, and Subplots]]
    -   The fundamental building blocks of a Matplotlib plot.
-   [[Plot_Elements_Anatomy|Anatomy of a Plot]] (General, but heavily applicable here)

## Basic Plotting
-   [[Matplotlib_Basic_Plotting_Functions|Basic Plotting Functions Overview]]
    -   [[170_Data_Visualization/Plot_Types/Line_Plot|Line Plot]] (`plt.plot()` / `ax.plot()`)
    -   [[170_Data_Visualization/Plot_Types/Scatter_Plot|Scatter Plot]] (`plt.scatter()` / `ax.scatter()`)
    -   [[170_Data_Visualization/Plot_Types/Bar_Chart|Bar Chart]] (`plt.bar()` / `ax.bar()`, `plt.barh()` / `ax.barh()`)
    -   [[170_Data_Visualization/Plot_Types/Histogram|Histogram]] (`plt.hist()` / `ax.hist()`)
    -   [[170_Data_Visualization/Plot_Types/Box_Plot|Box Plot]] (`plt.boxplot()` / `ax.boxplot()`)
    -   [[170_Data_Visualization/Plot_Types/Pie_Chart|Pie Chart]] (`plt.pie()` / `ax.pie()`)
-   [[Matplotlib_Image_Display_imshow|Image Display with `imshow`]]

## Customization & Advanced Features
-   [[Matplotlib_Customization|Customizing Plots]]
    -   Titles, Labels, Legends
    -   Colors, Linestyles, Markers
    -   Ticks, Tick Labels, and Gridlines
    -   Text and Annotations
-   [[Matplotlib_Colormaps|Working with Colormaps (`cmap`)]]
-   [[Matplotlib_Saving_Plots|Saving Plots (`savefig`)]]
-   [[Matplotlib_Styles|Using Stylesheets (`plt.style`)]]
-   [[Matplotlib_3D_Plotting|3D Plotting with `mpl_toolkits.mplot3d`]]
-   [[Matplotlib_Interactive_Plots|Interactive Plotting]]

## Notes in this Section
```dataview
LIST
FROM "170_Data_Visualization/Matplotlib"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
```

---
`````

This completes the creation of the Matplotlib-specific concept notes and the revision of the Matplotlib MOC with correct links. All linked notes should now exist.

Next, I will move on to the remaining questions from your "Data Visualization" chapter prompt. I'll create new notes for these or integrate answers into existing ones as appropriate.

---

Okay, let's address the remaining questions from your "Data Visualization" chapter prompt by creating new notes or integrating answers into existing ones.

---
**Addressing Remaining Data Visualization Questions:**

First, I'll create a note for `Tufte_Principles.md` as it was linked in `Data_Visualization_Principles.md`.

`````markdown

Filename: 170_Data_Visualization/Tufte_Principles.md
````markdown
[[Tufte_Principles]]
````

Now, addressing the specific questions. Some will go into new notes, others might be integrated if a suitable note already exists or is planned.

**New Notes for Specific Questions:**

`````markdown

Filename: 170_Data_Visualization/Anscombes_Quartet.md
````markdown
[[Anscombes_Quartet]]
````

`````markdown

Filename: 170_Data_Visualization/Additional_Plot_Types.md
````markdown
[[Additional_Plot_Types]]
`````

I've created notes for "Anscombe's Quartet" and "Additional Plot Types" (Area Chart, Bubble Chart, Treemap), including scenarios, usefulness, and whether they are the best choice, along with illustrative chart examples or descriptions for the Obsidian Charts plugin.

I will now review the remaining questions from your list and integrate answers or create specific notes as needed. Key remaining questions seem to be about Matplotlib API differences (which is partially covered in `Matplotlib_Pyplot_API_vs_OO_API.md` but can be expanded), and general visualization importance/limitations (covered in `Data_Visualization_Importance.md`).

Let me know if you want me to specifically address any other of the original questions in more detail or create dedicated notes for them. Otherwise, I'll assume the current set of notes covers the essence of the "Data Visualization" chapter request.

---

[[python packages and spark]]