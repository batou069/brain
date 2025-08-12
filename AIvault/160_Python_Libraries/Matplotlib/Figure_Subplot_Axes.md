---
tags:
  - matplotlib
  - python
  - plotting
  - concept
  - structure
aliases:
  - Matplotlib Figure
  - Matplotlib Axes
  - Matplotlib Subplot
related:
  - "[[Matplotlib]]"
  - "[[Pyplot_API]]"
  - "[[Matplotlib_Object_Oriented_API]]"
worksheet: [WS_NumPy] # Implied
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Matplotlib Figure, Axes, and Subplots

## Anatomy of a Matplotlib Plot

Understanding the hierarchy of Matplotlib objects is key to creating and customizing visualizations effectively. The main components are the Figure and the Axes.

1.  **Figure (`matplotlib.figure.Figure`):**
    -   The **top-level container** for all plot elements. Think of it as the entire window or page on which everything is drawn.
    -   A Figure can contain one or more [[#Axes (`matplotlib.axes.Axes`)|Axes objects (subplots)]].
    -   Responsible for aspects like overall figure size, DPI, background color, and global title (suptitle).
    -   Created explicitly using `fig = plt.figure()` or implicitly when a plotting function like `plt.plot()` is called without an active figure/axes.

2.  **Axes (`matplotlib.axes.Axes`):**
    -   An **individual plot or chart** within a Figure. This is the region where data is actually plotted with x and y coordinates (or other coordinates for different plot types like polar or 3D).
    -   Each Axes object has its own:
        -   Coordinate system.
        -   X-axis (`xaxis`) and Y-axis (`yaxis`) objects, which control ticks, labels, limits.
        -   Title (`ax.set_title()`).
        -   X-label (`ax.set_xlabel()`) and Y-label (`ax.set_ylabel()`).
        -   Plotted data (lines, scatter points, bars, etc.).
        -   Legend (`ax.legend()`).
    -   A Figure can have multiple Axes objects, arranged in a grid (subplots) or positioned more freely.
    -   **This is the object you will interact with most when customizing a plot in the object-oriented API.**

3.  **Subplot:**
    -   A common way to refer to an **Axes** object when it's part of a regular grid of plots within a Figure.
    -   `plt.subplots()` is a convenient function to create a Figure and a grid of Axes (subplots) simultaneously.
    -   `fig.add_subplot(nrows, ncols, index)` or `plt.subplot(nrows, ncols, index)` are used to add individual subplots to a figure.

## Visualization with AnyBlock

[list2tab]
- Conceptual Diagram
	```mermaid
	graph TD
	    FIGURE["Figure (Top-Level Container)"] --> AXES1["Axes 1 (Subplot 1)"];
	    FIGURE --> AXES2["Axes 2 (Subplot 2)"];
	    FIGURE --> Suptitle["Figure Suptitle (Optional)"];

	    AXES1 --> XAxis1["X-Axis 1"];
	    AXES1 --> YAxis1["Y-Axis 1"];
	    AXES1 --> Title1["Axes Title 1"];
	    AXES1 --> Plot1["Plotted Data 1 (lines, points)"];
	    AXES1 --> Legend1["Legend 1"];

	    AXES2 --> XAxis2["X-Axis 2"];
	    AXES2 --> YAxis2["Y-Axis 2"];
	    AXES2 --> Title2["Axes Title 2"];
	    AXES2 --> Plot2["Plotted Data 2"];
	    AXES2 --> Legend2["Legend 2"];

	    style FIGURE fill:#lightgrey,stroke:#333,stroke-width:2px
	    style AXES1 fill:#lightblue,stroke:#333,stroke-width:2px
	    style AXES2 fill:#lightgreen,stroke:#333,stroke-width:2px
	```
- Code Example (Object-Oriented API)
	```python
	import matplotlib.pyplot as plt
	import numpy as np

	# Data
	x = np.linspace(0, 10, 100)
	y1 = np.sin(x)
	y2 = np.cos(x)

	# Create a Figure and a single Axes object
	fig, ax = plt.subplots(figsize=(7, 4)) # fig is the Figure, ax is the Axes

	# Plot on the Axes object
	ax.plot(x, y1, label='sin(x)')
	ax.set_title('Plot on a Single Axes')
	ax.set_xlabel('X data')
	ax.set_ylabel('Y data')
	ax.legend()
	ax.grid(True)

	# plt.show() # Display the plot

	# Create a Figure with two subplots (Axes)
	fig2, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(7, 6), sharex=True)
	# fig2 is the Figure
	# ax1 is the first Axes (top subplot)
	# ax2 is the second Axes (bottom subplot)

	fig2.suptitle('Figure with Two Subplots') # Overall title for the Figure

	ax1.plot(x, y1, color='r', label='sin(x)')
	ax1.set_ylabel('sin(x) values')
	ax1.legend()
	ax1.grid(True)

	ax2.plot(x, y2, color='g', label='cos(x)')
	ax2.set_ylabel('cos(x) values')
	ax2.set_xlabel('Shared X data')
	ax2.legend()
	ax2.grid(True)

	plt.tight_layout(rect=[0, 0, 1, 0.96]) # Adjust layout to prevent suptitle overlap
	plt.show()
	```

## Working with Figure and Axes

- **Pyplot API:** `plt.figure()`, `plt.subplot()`, `plt.title()`, `plt.plot()` often act on the "current" implicitly managed Figure and Axes.
- **Object-Oriented API:** You explicitly get Figure and Axes objects (e.g., `fig, ax = plt.subplots()`) and call methods on them (e.g., `ax.plot()`, `ax.set_title()`, `fig.savefig()`). This approach offers more control and is generally preferred for complex plots or when writing reusable plotting functions.

## Related Concepts
- [[Matplotlib]] (The library)
- [[Pyplot_API]] (State-based interface)
- [[Matplotlib_Object_Oriented_API]] (Object-based interface)
- Plot elements (lines, markers, text, titles, labels, legends)

---
**Source:** Matplotlib Documentation