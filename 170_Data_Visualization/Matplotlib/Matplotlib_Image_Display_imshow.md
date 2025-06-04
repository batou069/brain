---
tags:
  - matplotlib
  - python
  - plotting
  - image_processing
  - numpy
  - imshow
  - concept
aliases:
  - plt.imshow
  - Displaying Images Matplotlib
  - ax.imshow
related:
  - "[[Matplotlib_Overview]]"
  - "[[Matplotlib_Pyplot_API_vs_OO_API]]"
  - "[[Matplotlib_Figure_Subplot_Axes]]"
  - "[[_NumPy_MOC|NumPy ndarray]]"
  - "[[NumPy_Image_Representation]]"
  - "[[140_Data_Science_AI/Pillow_PIL/_Pillow_PIL_MOC|Pillow (PIL)]]"
  - "[[Matplotlib_Colormaps]]"
worksheet:
  - WS_DataViz_1
  - WS_NumPy
date_created: 2025-06-03
---
# Matplotlib: Image Display with `imshow`

## Definition
Matplotlib provides the `imshow()` function (available in `matplotlib.pyplot` as `plt.imshow()` and as a method of `Axes` objects, `ax.imshow()`) to display image data. It is highly versatile and can handle 2D [[_NumPy_MOC|NumPy arrays]] (for grayscale or pseudocolor images) and 3D NumPy arrays (for RGB/RGBA color images).

See [[NumPy_Image_Representation]] for how images are typically stored in arrays.

## `imshow()` Function
**Syntax (Simplified):**
```python
matplotlib.pyplot.imshow(X, cmap=None, norm=None, aspect=None, interpolation=None, alpha=None, vmin=None, vmax=None, origin=None, extent=None, ...)
# Axes.imshow(X, cmap=None, ...) has similar parameters
```

-   **`X`**: The image data, typically a [[_NumPy_MOC|NumPy ndarray]].
    -   **2D array `(M, N)`:** Interpreted as scalar data. Mapped to colors using a colormap (`cmap`). If `cmap` is not specified, a default colormap (often 'viridis') is used. For grayscale, explicitly use `cmap='gray'`.
    -   **3D array `(M, N, 3)`:** Interpreted as an RGB image. Values are typically expected to be floats in $[0, 1]$ or integers in $[0, 255]$.
    -   **3D array `(M, N, 4)`:** Interpreted as an RGBA image (includes an alpha/transparency channel). Values typically floats in $[0, 1]$ or integers in $[0, 255]$.
-   **`cmap` (Colormap):** Optional string or Colormap instance. Used to map scalar data (2D arrays) to colors. Ignored for RGB/RGBA images. Common examples: `'gray'`, `'viridis'`, `'jet'`, `'hot'`. See [[Matplotlib_Colormaps|Colormaps]].
-   **`aspect`:** Controls the aspect ratio of the Axes.
    -   `'auto'`: Adjusts axes to fill the figure. Pixels may not be square.
    -   `'equal'`: Ensures pixels are square by adjusting the Axes box.
-   **`interpolation`:** String specifying the interpolation method used if the image display size is different from the image data size. Examples: `'nearest'`, `'bilinear'`, `'bicubic'`, `'lanczos'`. `'nearest'` gives a blocky look, others are smoother.
-   **`origin`:** `{'upper', 'lower'}`. Places the `[0,0]` index of the array in the upper-left or lower-left corner of the axes. Default for `imshow` is typically `'upper'`, which is standard for images.
-   **`vmin`, `vmax`:** Scalars, optional. Used with 2D scalar data to set the data range that the colormap covers. Values outside `[vmin, vmax]` will be clipped.

## Examples

[list2tab|#imshow Examples]
- Grayscale (2D Array)
    -
        ```python
        import matplotlib.pyplot as plt
        import numpy as np

        # Create a sample 2D NumPy array (e.g., a gradient)
        gradient = np.linspace(0, 255, 256, dtype=np.uint8)
        grayscale_image = np.tile(gradient, (256, 1)) # Repeat row to make 256x256

        fig, ax = plt.subplots()
        im = ax.imshow(grayscale_image, cmap='gray', vmin=0, vmax=255)
        ax.set_title("Grayscale Image (2D Array)")
        fig.colorbar(im, ax=ax, label="Pixel Intensity") # Add a colorbar
        # plt.show()
        ```
    -   This displays a vertical gradient from black to white. `cmap='gray'` ensures it's grayscale. `vmin` and `vmax` define the intensity mapping.
- Color RGB (3D Array)
    -
        ```python
        import matplotlib.pyplot as plt
        import numpy as np

        # Create a sample 3D NumPy array (Height, Width, Channels)
        # Example: 64x64 image with random RGB values (0-255 integers)
        rgb_image = np.random.randint(0, 256, size=(64, 64, 3), dtype=np.uint8)

        fig, ax = plt.subplots()
        ax.imshow(rgb_image) # Matplotlib infers RGB from (M,N,3) shape
        ax.set_title("Random Color RGB Image")
        ax.axis('off') # Often desirable for images
        # plt.show()
        ```
    -   `imshow` automatically detects the 3-channel array as an RGB image. `axis('off')` removes the axis ticks and labels.
- Loading & Displaying
    -
        ```python
        import matplotlib.pyplot as plt
        import numpy as np
        from skimage import data # Using scikit-image for a sample image
        # Alternatively, use Pillow: from PIL import Image

        try:
            # Load a sample color image (e.g., from scikit-image.data)
            # This is already a NumPy array
            img_array = data.astronaut() # This is an RGB image (uint8)

            # Display using Matplotlib
            fig, ax = plt.subplots(figsize=(6, 6))
            ax.imshow(img_array)
            ax.set_title(f"Astronaut Image ({img_array.shape}x{img_array.shape})")
            ax.axis('off')
            # plt.show()

        except Exception as e:
            print(f"Could not load/display sample image: {e}")
            # Fallback: create a dummy array if data loading fails
            img_array = np.zeros((50,50,3), dtype=np.uint8)
            img_array[:,:,0] = 255 # Make it red
            fig, ax = plt.subplots()
            ax.imshow(img_array)
            ax.set_title("Dummy Red Image")
            ax.axis('off')
            # plt.show()
        ```
    -   This example shows loading an image (here, a sample from `skimage.data`) which is already a NumPy array, and then displaying it. If using Pillow, you'd convert the PIL Image object to a NumPy array first (`np.array(pil_image_object)`).

## Important Considerations
-   **Data Type and Range:**
    -   For RGB/RGBA images, `imshow` expects float data in the range $[0, 1]$ or integer data in the range $[0, 255]$. Data outside these ranges might be clipped or result in unexpected colors.
    -   Use `skimage.util.img_as_float` or `skimage.util.img_as_ubyte` for conversions if needed.
-   **Pixel-Perfect Display:** To ensure pixels are displayed without interpolation and with the correct aspect ratio, use `interpolation='nearest'` and `aspect='equal'`.
-   **Colormaps for Grayscale:** When displaying a 2D array that represents a grayscale image, always specify `cmap='gray'`. Otherwise, Matplotlib might use a default colormap (like 'viridis') which will add false color.

`imshow` is the primary tool for visualizing matrix-like data in Matplotlib, whether it's a true photograph, a heatmap of data values, or any other 2D array.

---