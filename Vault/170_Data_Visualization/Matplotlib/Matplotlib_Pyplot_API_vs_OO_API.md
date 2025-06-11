---
tags:
  - matplotlib
  - python
  - api
  - plotting
  - pyplot
  - object_oriented
  - concept
  - comparison
  - state_based
aliases:
  - Matplotlib APIs
  - Pyplot vs OO API
  - Matplotlib Plotting Approaches
  - pyplot
  - plt (Matplotlib)
related:
  - "[[Matplotlib_Overview]]"
  - "[[Matplotlib_Figure_Subplot_Axes]]"
  - "[[Matplotlib_Pyplot_API]]"
  - "[[Matplotlib_Object_Oriented_API]]"
  - "[[Matplotlib_Pyplot_API_vs_OO_API]]"
worksheet:
  - WS_DataViz_1
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Matplotlib: Pyplot API vs. Object-Oriented (OO) API

Matplotlib offers two primary approaches or Application Programming Interfaces (APIs) for creating visualizations: the `pyplot` API and the Object-Oriented (OO) API.

>[!question] What are the 2 main approaches to use matplotlib?
>The two main approaches are:
>1.  The **`pyplot` API** (state-based).
>2.  The **Object-Oriented (OO) API** (explicit figure and axes management).

[list2tab|#API Comparison]
- `pyplot` API (State-Based)
    - **Concept:** `matplotlib.pyplot` is a collection of functions that make Matplotlib work like MATLAB. It's a state-based interface where plotting commands implicitly refer to and modify a "current" [[Matplotlib_Figure_Subplot_Axes|Figure]] and [[Matplotlib_Figure_Subplot_Axes|Axes]].
    - **Import:** Typically `import matplotlib.pyplot as plt`.
    - **Usage:** Functions like `plt.plot()`, `plt.title()`, `plt.xlabel()` are called directly.
    - **Pros:**
        -   Concise and convenient for simple, quick plots.
        -   Familiar to MATLAB users.
        -   Lower barrier to entry for beginners.
    - **Cons:**
        -   Can become less clear and harder to manage for complex plots with multiple figures or subplots, as it relies on an internal state.
        -   Less explicit control over individual plot elements.
    - **Example:**
        ```python
        import matplotlib.pyplot as plt
        import numpy as np
        x = np.linspace(0, 5, 100)
        y = x**2

        plt.figure() # Implicitly creates and sets current figure
        plt.plot(x, y)
        plt.title("Simple Plot (pyplot)")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.show()
        ```
- Object-Oriented (OO) API
    - **Concept:** This approach involves explicitly creating and keeping track of [[Matplotlib_Figure_Subplot_Axes|Figure]] and [[Matplotlib_Figure_Subplot_Axes|Axes]] objects. Plotting functions are then methods of these objects.
    - **Usage:**
        1.  Create a `Figure` instance (e.g., `fig = plt.figure()` or often `fig, ax = plt.subplots()`).
        2.  Add `Axes` to the `Figure` (e.g., `ax = fig.add_subplot(1,1,1)` or `fig, axes_array = plt.subplots(nrows, ncols)`).
        3.  Call methods directly on the `Axes` object(s) (e.g., `ax.plot()`, `ax.set_title()`, `ax.set_xlabel()`).
    - **Pros:**
        -   More explicit, offering finer-grained control over all plot elements.
        -   Better for complex plots, multiple subplots, or when embedding plots in applications (e.g., GUIs).
        -   Generally considered more "Pythonic" and robust for larger projects or reusable functions.
        -   Easier to manage multiple figures and axes simultaneously.
    - **Cons:**
        -   Can be slightly more verbose for very simple plots.
    - **Example:**
        ```python
        import matplotlib.pyplot as plt
        import numpy as np
        x = np.linspace(0, 5, 100)
        y = x**2

        fig, ax = plt.subplots() # Creates a Figure (fig) and an Axes (ax)
        ax.plot(x, y)
        ax.set_title("Simple Plot (OO API)")
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        plt.show()
        ```

>[!question] List all the things you can do using one of the approach and not the other
>Essentially, **anything that can be done with the `pyplot` API can also be done with the Object-Oriented API**. The OO API provides the underlying structure that `pyplot` manipulates.
>
>However, the **OO API offers more explicit control and flexibility that might be cumbersome or less direct to achieve purely through `pyplot`'s stateful nature, especially in complex scenarios:**
>
>**Advantages / Capabilities more pronounced with OO API:**
>1.  **Managing Multiple Figures and Axes:** Explicitly holding references to `Figure` and `Axes` objects makes it straightforward to work with several plots simultaneously or to modify a specific subplot in a complex layout without relying on `pyplot`'s notion of the "current" axes.
>2.  **Fine-grained Control over Layout:** Tools like `GridSpec` for complex subplot arrangements, or `fig.add_axes([left, bottom, width, height])` for arbitrarily placed axes, are inherently object-oriented.
>3.  **Embedding in Applications:** When integrating Matplotlib plots into GUI toolkits (Tkinter, Qt, WxPython, etc.) or web applications, the OO API is essential as you need to pass `Figure` objects to the embedding canvas.
>4.  **Creating Reusable Plotting Functions/Classes:** Writing functions or classes that create and customize plots is much cleaner and more robust with the OO API, as you can pass `Axes` objects as arguments and operate on them directly, avoiding global state issues.
>5.  **Access to More Artist Properties:** While `pyplot` provides functions for common customizations, the OO API gives direct access to all properties of the various `Artist` objects (lines, text, patches, etc.) that make up a plot, allowing for more advanced modifications.
>6.  **Clarity in Complex Scripts:** For longer scripts or applications involving many plots, the explicit nature of the OO API makes the code easier to read, understand, and maintain because it's always clear which plot object is being modified.
>
>**Things `pyplot` does for convenience (which OO users often still use `pyplot` for initially):**
>7.  **Implicit Figure/Axes Creation:** `plt.plot()` will automatically create a figure and axes if none exist. In OO, you usually start with `fig, ax = plt.subplots()`.
>8.  **Global Figure Management:** `plt.figure(num)` allows switching between or creating figures by number.
>9.  **`plt.show()`:** This `pyplot` function is almost always used at the end, even in OO-style plotting, to actually display the figures.
>
>In practice, many users employ a hybrid approach: using `pyplot` for convenience functions like `plt.figure()`, `plt.subplots()`, and `plt.show()`, but then primarily using the methods of the returned `Figure` and `Axes` objects for the actual plotting and customization.

## Recommendation
-   For quick, simple, or interactive plotting (e.g., in a Jupyter notebook for EDA), the `pyplot` API is often sufficient and faster to type.
-   For more complex visualizations, reusable functions, scripts, or applications, the **Object-Oriented API is generally preferred** for its explicitness, control, and maintainability.

Most Matplotlib documentation and examples showcase both styles or lean towards the OO API for demonstrating full capabilities.

---

# Matplotlib: `pyplot` API

## Definition
`matplotlib.pyplot` is a collection of functions in [[Matplotlib_Overview|Matplotlib]] that provide a **state-based interface** for creating figures and plots. It's designed to make Matplotlib work in a way that is similar to MATLAB's plotting environment. Each `pyplot` function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc.

It is conventionally imported under the alias `plt`:
```python
import matplotlib.pyplot as plt
```

## Key Characteristics
-   **Procedural / State-Based:** `pyplot` maintains an internal state, keeping track of the "current" [[Matplotlib_Figure_Subplot_Axes|Figure]] and "current" [[Matplotlib_Figure_Subplot_Axes|Axes]]. Plotting commands implicitly apply to this current context. This simplifies creating plots quickly.
-   **MATLAB-like:** The API is intentionally similar to MATLAB's plotting commands, making it familiar for users transitioning from MATLAB.
-   **Convenience Layer:** It serves as a convenient layer on top of Matplotlib's more fundamental object-oriented structure. Many `pyplot` functions are wrappers that create or manipulate the underlying `Figure` and `Axes` objects.
-   **Typical Workflow:**
    1.  (Optional) Create a figure: `plt.figure()`
    2.  (Optional) Define subplots: `plt.subplot()` or rely on plotting functions like `plt.plot()` to create default axes.
    3.  Use plotting functions: `plt.plot()`, `plt.scatter()`, `plt.bar()`, `plt.hist()`, `plt.imshow()`, etc.
    4.  Add labels, titles, legends: `plt.xlabel()`, `plt.ylabel()`, `plt.title()`, `plt.legend()`.
    5.  Customize aspects: `plt.grid()`, `plt.xlim()`, `plt.ylim()`, `plt.xticks()`.
    6.  Display or save the figure: `plt.show()`, `plt.savefig()`.

## Example
```python
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = np.linspace(0, 2 * np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Using pyplot functions directly
plt.figure(figsize=(7, 5)) # Create a new figure and set its size

plt.plot(x, y_sin, label='sin(x)', color='blue') # Plot sin(x)
plt.plot(x, y_cos, label='cos(x)', color='red', linestyle='--') # Plot cos(x)

plt.title('Plot created with pyplot API')
plt.xlabel('Angle (radians)')
plt.ylabel('Function Value')
plt.legend() # Display legend
plt.grid(True) # Add grid

# plt.savefig('pyplot_example.png')
plt.show() # Display the plot
```
![[lineplot.png]]
## Relationship to Object-Oriented API
While `pyplot` is convenient, Matplotlib also offers a more explicit and powerful **[[Matplotlib_Pyplot_API_vs_OO_API|Object-Oriented (OO) API]]**. The OO API involves directly creating and manipulating `Figure` and `Axes` objects.

-   `pyplot` is excellent for simple, quick, or interactive plots.
-   The OO API is generally recommended for more complex plots, functions that create plots, or when embedding Matplotlib in applications, as it offers greater control and clarity.

Many users employ a hybrid approach, using `pyplot` for figure creation (`plt.figure()`, `plt.subplots()`) and display (`plt.show()`), but then using the methods of the returned `Figure` and `Axes` objects for detailed plotting and customization.

---