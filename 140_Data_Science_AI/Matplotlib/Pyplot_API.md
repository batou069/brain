---
tags:
  - matplotlib
  - python
  - api
  - plotting
  - concept
aliases:
  - pyplot
  - plt (Matplotlib)
related:
  - "[[Matplotlib]]"
  - "[[Figure_Subplot_Axes]]"
  - "[[Matplotlib_Object_Oriented_API]]" # Placeholder for contrast
worksheet: [WS_NumPy] # Implied
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# `pyplot` API (Matplotlib)

## Definition

`matplotlib.pyplot` is a collection of functions in [[Matplotlib]] that provide a **state-based interface** for creating figures and plots, making Matplotlib work like MATLAB. Each `pyplot` function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc.

It is commonly imported under the alias `plt`:
```python
import matplotlib.pyplot as plt
```

## Key Characteristics

- **Procedural / State-Based:** `pyplot` keeps track of the "current" figure and axes, and plotting commands apply to this current context implicitly. This makes it convenient for quickly generating plots.
- **MATLAB-like:** Designed to feel familiar to users of MATLAB's plotting capabilities.
- **Convenience Layer:** Provides a simpler way to create common plots without needing to explicitly manage [[Figure_Subplot_Axes|Figure and Axes objects]] directly in many simple cases.
- **Foundation:** While often used for quick plots, `pyplot` functions often create and manipulate the underlying Figure and Axes objects. One can still access these objects for finer control if needed.
- **Typical Workflow:**
    1. (Optional) Create a figure: `plt.figure()`
    2. (Optional) Create axes/subplots: `plt.subplot()` or rely on `plt.plot()` to create them.
    3. Use plotting functions: `plt.plot()`, `plt.scatter()`, `plt.bar()`, `plt.hist()`, `plt.imshow()`, etc.
    4. Add labels, titles, legends: `plt.xlabel()`, `plt.ylabel()`, `plt.title()`, `plt.legend()`.
    5. Customize: `plt.grid()`, `plt.xlim()`, `plt.ylim()`.
    6. Display or save: `plt.show()`, `plt.savefig()`.

## Example

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Using pyplot functions directly
plt.figure(figsize=(6,4)) # Create a figure
plt.plot(x, y, label='sin(x)') # Plot on the "current" axes (created if needed)
plt.title('Simple Sine Plot using pyplot')
plt.xlabel('Angle (radians)')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()
```

## Relation to Object-Oriented API

Matplotlib also has a more explicit and flexible **Object-Oriented (OO) API**. In the OO API, you explicitly create and work with `Figure` and `Axes` objects:

```python
fig, ax = plt.subplots() # Creates a Figure and a single Axes
ax.plot(x, y, label='sin(x)')
ax.set_title('Sine Plot (OO Style)')
ax.set_xlabel('Angle (radians)')
ax.set_ylabel('Value')
ax.legend()
ax.grid(True)
plt.show()
```
While `pyplot` is convenient for simple plots, the OO API is generally recommended for more complex plots, when you need to manage multiple subplots, or when embedding plots in GUI applications. Many `pyplot` functions are essentially wrappers around methods of `Figure` and `Axes` objects.

## Related Concepts
- [[Matplotlib]]
- [[Figure_Subplot_Axes]] (The objects `pyplot` implicitly manages)
- [[Matplotlib_Object_Oriented_API]] (The more explicit alternative)
- Plotting functions (`plot`, `scatter`, `bar`, `hist`, `imshow`)

---
**Source:** Matplotlib Documentation