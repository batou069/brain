---
tags:
  - bokeh
  - python
  - data_visualization
  - interactive_plotting
  - embedding
  - bokeh_server
  - web_applications
  - concept
  - example
aliases:
  - Embedding Bokeh Plots
  - Bokeh Server Applications
  - Interactive Bokeh Apps
related:
  - "[[170_Data_Visualization/Bokeh/_Bokeh_MOC|_Bokeh_MOC]]"
  - "[[Bokeh_Layouts_Interactivity]]"
  - "[[Bokeh_Widgets]]"
  - "[[Dash_Framework]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-11
---
# Bokeh: Embedding Plots and Bokeh Server Applications

Bokeh visualizations are designed for web browsers. There are several ways to share or deploy them: as standalone HTML files, embedded components in web pages, or as part of full-fledged interactive web applications powered by the Bokeh server.

## 1. Standalone HTML Files
This is the simplest way to save and share a Bokeh plot. The output is a single HTML file that contains all the necessary data, BokehJS library (or a link to it), and plot definitions.

-   **Functions:** `bokeh.io.output_file("filename.html")` followed by `bokeh.io.show(plot_object_or_layout)`.
-   **Interactivity:** Most client-side interactivity (tools like zoom, pan, hover, tap, CustomJS callbacks) is preserved.
-   **Python Callbacks:** Python-backed interactivity (requiring a Bokeh server) will **not** work in standalone HTML files.

**Example:**
```python
from bokeh.plotting import figure, show
from bokeh.io import output_file
import numpy as np

# output_file("standalone_plot.html", title="My Bokeh Plot HTML") # Specify output file

# x = np.linspace(0, 10, 100)
# y = np.sin(x)

# p = figure(title="Simple Sine Wave (Standalone HTML)")
# p.line(x, y, line_width=2)

# show(p) # This will generate and open (or just save) standalone_plot.html
```

## 2. Embedding Bokeh Content
Bokeh provides functions to generate components that can be embedded into existing HTML documents or web templates (e.g., in Flask or Django applications).

-   **`bokeh.embed.components(plot_object_or_layout)`:**
    -   Returns a `script` tag and one or more `<div>` tags.
    -   The `script` contains the data and plot definitions.
    -   The `<div>` tags are placeholders where the plots will be rendered.
    -   This method requires BokehJS to be loaded separately on the host HTML page.
-   **`bokeh.embed.file_html(plot_object_or_layout, resources, title)`:**
    -   Creates a full HTML page string, similar to `output_file` but returns the string instead of writing to a file. `resources` (e.g., `CDN`, `INLINE`) controls how BokehJS is included.
-   **`bokeh.embed.json_item(plot_object, target_id)`:**
    -   Serializes a Bokeh plot to a JSON representation that can be embedded and rendered by BokehJS. Useful for dynamic loading or integration with other JavaScript applications.

**Example (Conceptual `components` usage for a Flask app):**
```python
# --- In your Flask app (app.py) ---
# from flask import Flask, render_template
# from bokeh.plotting import figure
# from bokeh.embed import components
# import numpy as np

# app = Flask(__name__)

# @app.route('/')
# def index():
#     x = np.linspace(0, 10, 50)
#     y = np.cos(x)
#     p = figure(title="Embedded Cosine Wave")
#     p.line(x, y, line_width=2, color="green")
    
#     script, div = components(p)
#     return render_template("index.html", script=script, div=div, page_title="Bokeh Embedded Plot")

# --- In your Flask template (templates/index.html) ---
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>{{ page_title }}</title>
#     <!-- Link to BokehJS (e.g., from CDN) -->
#     <script src="https://cdn.bokeh.org/bokeh/release/bokeh-x.y.z.min.js"></script> 
#     <!-- Replace x.y.z with Bokeh version -->
#     {{ script|safe }} {# This is where the script from components() goes #}
# </head>
# <body>
#     <h1>My Web Page with a Bokeh Plot</h1>
#     {{ div|safe }} {# This is where the plot div from components() goes #}
# </body>
# </html>

# if __name__ == '__main__':
#     app.run(debug=True)
```

## 3. Bokeh Server Applications
For fully interactive applications where user interactions (e.g., moving a slider, clicking a button, selecting data) need to trigger Python code execution and update plots dynamically, you use the **Bokeh server**.

-   **How it Works:**
    1.  You write a Python script or a directory of Python modules that define a Bokeh `Document`.
    2.  This script includes Python callback functions that modify Bokeh models (figures, data sources, widgets) in response to events.
    3.  You run this script using the command `bokeh serve myapp.py` (or `bokeh serve myapp_directory/`).
    4.  The Bokeh server process keeps your Python code running.
    5.  When a user connects via a web browser, BokehJS establishes a connection with the server.
    6.  User interactions in the browser trigger events. These events are sent to the Bokeh server, which executes the corresponding Python callbacks.
    7.  The Python callbacks modify the Bokeh `Document` (e.g., update a `ColumnDataSource`, change a plot title).
    8.  The Bokeh server automatically synchronizes these changes back to the browser, and BokehJS re-renders the affected parts of the visualization.
-   **Key for Python-backed Interactivity:** This allows for complex interactions involving data queries, model fitting, simulations, or any Python computation.

**Example (Simple Bokeh Server App with a Slider):**
Save as `bokeh_server_app.py`:
```python
from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource, Slider
from bokeh.layouts import column
import numpy as np

# Prepare data source
x = np.linspace(0, 10, 100)
y = np.sin(x)
source = ColumnDataSource(data=dict(x=x, y=y))

# Create plot
plot = figure(title="Sine Wave with Frequency Control",
              x_range=(0, 10), y_range=(-1.5, 1.5),
              width=500, height=400)
line_renderer = plot.line(x='x', y='y', source=source, line_width=2)

# Create a slider widget
freq_slider = Slider(start=0.1, end=5.0, value=1.0, step=0.1, title="Frequency")

# Define a Python callback function
def update_data(attrname, old, new):
    # Get the current slider value
    k = freq_slider.value
    # Generate new y values
    new_y = np.sin(k * source.data['x']) # Use original x from source
    # Update the 'y' column in the ColumnDataSource
    source.data = dict(x=source.data['x'], y=new_y)

# Attach the callback to the slider's 'value' property
freq_slider.on_change('value', update_data)

# Arrange plot and widget in a layout
layout = column(freq_slider, plot)

# Add the layout to the current document (for Bokeh server)
curdoc().add_root(layout)
curdoc().title = "Bokeh Server Sine App"
```
**To run this application:**
1.  Save the code above as `bokeh_server_app.py`.
2.  Open your terminal/command prompt in the same directory.
3.  Run: `bokeh serve --show bokeh_server_app.py`
4.  This will start the Bokeh server and open the application in your web browser. Moving the slider will execute the `update_data` Python function and dynamically change the sine wave's frequency.

Bokeh server applications enable the creation of powerful, interactive data dashboards and tools directly in Python.

---