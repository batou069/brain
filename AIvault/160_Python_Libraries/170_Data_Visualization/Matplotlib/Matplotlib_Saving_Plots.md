---
tags:
  - matplotlib
  - python
  - plotting
  - data_visualization
  - saving_figures
  - export_plots
  - png
  - pdf
  - svg
  - concept
  - example
aliases:
  - Saving Matplotlib Figures
  - Exporting Matplotlib Plots
  - plt.savefig
  - fig.savefig
related:
  - "[[160_Python_Libraries/170_Data_Visualization/Matplotlib/_Matplotlib_MOC|_Matplotlib_MOC]]"
  - "[[Matplotlib_Figure_Subplot_Axes]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-11
---
# Matplotlib: Saving Plots to Files

Once you have created a plot with Matplotlib, you'll often want to save it to a file for inclusion in reports, presentations, publications, or websites. Matplotlib supports saving figures in various formats.

## `savefig()` Method
The primary way to save a figure is using the `savefig()` method, which is available on `Figure` objects (`fig.savefig()`) or via the `pyplot` interface (`plt.savefig()`).

**Syntax:**
```python
fig.savefig(fname, dpi=None, facecolor='w', edgecolor='w',
            orientation='portrait', format=None, transparent=False,
            bbox_inches=None, pad_inches=0.1, metadata=None, ...)

plt.savefig(fname, ...) # Similar arguments
```

**Key Parameters:**
-   `fname`: A string (filename or path) or a Python file-like object. The file format is inferred from the extension (e.g., `.png`, `.pdf`, `.svg`, `.jpg`).
-   `dpi` (Dots Per Inch): The resolution of the figure. Higher DPI results in higher resolution images. Common values: 100, 150, 300 (for print), 600. If `None`, uses the figure's DPI or a default.
-   `format`: Explicitly specify the file format (e.g., 'png', 'pdf', 'svg'). If `None`, inferred from `fname` extension.
-   `transparent`: If `True`, the figure background will be transparent (if supported by the format, e.g., PNG).
-   `bbox_inches`: Bounding box in inches to save.
    -   `'tight'`: Adjusts the figure size to include all artists, removing extra whitespace. Very useful.
    -   A `Bbox` object.
-   `pad_inches`: Amount of padding around the figure when `bbox_inches='tight'`.
-   `facecolor`, `edgecolor`: Color of the figure background and edge (can override figure's settings at save time).

## Common File Formats
Matplotlib supports many raster and vector formats:
-   **Raster Formats (Pixel-based):**
    -   **PNG (Portable Network Graphics):** Good for plots with sharp lines, text, and transparency. Lossless compression. Excellent for web and documents.
    -   **JPG/JPEG (Joint Photographic Experts Group):** Good for photographic images, uses lossy compression. Generally not ideal for line art or plots with text due to compression artifacts, but can result in smaller file sizes.
    -   **TIFF (Tagged Image File Format):** High-quality raster format, can be lossless or lossy.
    -   **BMP (Bitmap):** Uncompressed raster format, usually large files.
-   **Vector Formats (Scalable):**
    -   **SVG (Scalable Vector Graphics):** XML-based vector image format. Excellent for web, scales perfectly without loss of quality. Can be edited in vector graphics software.
    -   **PDF (Portable Document Format):** Good for documents and publications. Vector content remains scalable.
    -   **PS/EPS (PostScript/Encapsulated PostScript):** Older vector formats, still used in some academic publishing workflows.

**Choosing a Format:**
-   For web display or general use where scalability isn't critical: **PNG** is often a good choice.
-   For publications, or when you need to scale the image without loss of quality, or edit it in vector software: **SVG** or **PDF** are preferred.

## Examples

**1. Saving a Simple Plot (Pyplot API):**
```python
import matplotlib.pyplot as plt
import numpy as np

# x = np.linspace(0, 2 * np.pi, 100)
# y = np.sin(x)

# plt.figure(figsize=(6,4))
# plt.plot(x, y)
# plt.title("Sine Wave for Saving")
# plt.xlabel("Radians")
# plt.ylabel("sin(x)")
# plt.grid(True)

# Save as PNG
# plt.savefig("sine_wave_pyplot.png", dpi=150)
# print("Saved sine_wave_pyplot.png")

# Save as PDF with tight bounding box
# plt.savefig("sine_wave_pyplot.pdf", bbox_inches='tight')
# print("Saved sine_wave_pyplot.pdf")

# plt.show() # Optional, if you also want to display it
# plt.close() # Close the figure to free memory if creating many plots in a loop
```

**2. Saving a Plot (Object-Oriented API):**
```python
import matplotlib.pyplot as plt
import numpy as np

# Conceptual e-commerce sales data
# months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
# sales_product_A = 
# sales_product_B = 

# fig, ax = plt.subplots(figsize=(8, 5))
# ax.plot(months, sales_product_A, label="Product A", marker='o')
# ax.plot(months, sales_product_B, label="Product B", marker='x')
# ax.set_title("Monthly Sales Comparison")
# ax.set_xlabel("Month")
# ax.set_ylabel("Sales Units")
# ax.legend()
# ax.grid(axis='y', linestyle=':')

# Save as SVG (vector format)
# fig.savefig("product_sales_oo.svg", transparent=False, bbox_inches='tight')
# print("Saved product_sales_oo.svg")

# Save as high-resolution PNG for a report
# fig.savefig("product_sales_oo_high_res.png", dpi=300, facecolor='lightyellow', bbox_inches='tight')
# print("Saved product_sales_oo_high_res.png")

# plt.show() # Optional
# plt.close(fig) # Close the specific figure
```

## Important Considerations
-   **Call `savefig()` *before* `plt.show()`:** If you call `plt.show()`, Matplotlib might reset some internal states or clear the figure in some backends, potentially leading to a blank saved image if `savefig()` is called afterwards. It's best practice to save before showing.
-   **`bbox_inches='tight'`:** This is a very useful option to automatically crop the saved figure to include all artists, removing unnecessary white space around the plot.
-   **Resolution (`dpi`):** For print or high-quality displays, use a higher DPI (e.g., 300 or 600). For web, 72-100 DPI might be sufficient, but higher DPI PNGs often look crisper even on screens.
-   **Vector vs. Raster:** Understand the difference. Vector formats (SVG, PDF) are ideal for scalability and print, while raster formats (PNG, JPG) are pixel-based.
-   **File Paths:** Ensure the directory path where you are saving the file exists, or `savefig()` will raise an error.
-   **Closing Figures (`plt.close()`):** If you are generating many plots in a script (e.g., in a loop), it's important to close figures using `plt.close(fig)` or `plt.close('all')` after saving them to free up memory. Otherwise, all figures remain in memory and can lead to performance issues or crashes.

`savefig()` provides comprehensive control over how your Matplotlib visualizations are exported for various purposes.

---