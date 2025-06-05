---
tags:
  - matplotlib
  - python
  - plotting
  - image_processing
  - numpy
aliases:
  - plt.imshow
  - Displaying Images with Matplotlib
related:
  - "[[Matplotlib]]"
  - "[[Pyplot_API]]"
  - "[[Figure_Subplot_Axes]]"
  - "[[NumPy_ndarray]]"
  - "[[NumPy_Image_Representation]]"
  - "[[Pillow_PIL_MOC|Pillow (PIL)]]"
  - "[[Colormaps_Matplotlib]]"
worksheet: [WS_NumPy] # Implied by exercise "load a color image into a np.ndarray and zoom"
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Image Display with Matplotlib (`imshow`)

## Definition

Matplotlib provides the `imshow()` function (available in `matplotlib.pyplot` and as a method of `Axes` objects) to display image data. It can handle 2D [[NumPy_ndarray|NumPy arrays]] (for grayscale or pseudocolor images) and 3D NumPy arrays (for RGB/RGBA color images).

## `plt.imshow()` / `ax.imshow()`

**Syntax (Simplified):**
```python
matplotlib.pyplot.imshow(X, cmap=None, norm=None, aspect=None, interpolation=None, alpha=None, vmin=None, vmax=None, origin=None, extent=None, ...)
```
```python
Axes.imshow(X, cmap=None, ...) # Similar parameters
```

- **`X`**: The image data. A [[NumPy_ndarray]] or array-like.
    - **2D array `(M, N)`:** Interpreted as scalar data to be mapped to colors using a colormap (`cmap`). Grayscale by default if no `cmap` specified.
    - **3D array `(M, N, 3)`:** Interpreted as an RGB image (values typically 0-1 for float, 0-255 for uint8).
    - **3D array `(M, N, 4)`:** Interpreted as an RGBA image (values typically 0-1 for float, 0-255 for uint8).
- **`cmap` (Colormap):** Optional. The colormap instance or registered colormap name used to map scalar data to colors. Only used for 2D arrays. Common examples: `'gray'`, `'viridis'`, `'jet'`, `'hot'`. See [[Colormaps_Matplotlib]].
- **`aspect`:** Controls the aspect ratio of the axes. `'auto'` adjusts axes to fill figure. `'equal'` ensures pixels are square.
- **`interpolation`:** Specifies the interpolation method used when displaying an image that is not at its native resolution (e.g., 'nearest', 'bilinear', 'bicubic').
- **`origin`:** Place the `[0,0]` index of the array in the upper-left or lower-left corner of the axes. Default is usually `'upper'` for images.
- **`vmin`, `vmax`:** Used with 2D data to scale the colormap (normalize data range).

## AnyBlock Tabs: `imshow` Examples

[list2tab]
- Grayscale Image (2D Array)
	```python
	import matplotlib.pyplot as plt
	import numpy as np

	# Create a sample 2D NumPy array (e.g., a gradient)
	gradient = np.linspace(0, 255, 256, dtype=np.uint8)
	grayscale_image = np.tile(gradient, (256, 1)) # Repeat row to make 256x256

	plt.figure(figsize=(5, 5))
	plt.imshow(grayscale_image, cmap='gray', vmin=0, vmax=255)
	plt.title("Grayscale Image from NumPy Array")
	plt.colorbar(label="Pixel Intensity")
	plt.show()
	```
	![[imshow_grayscale.png]] %% Placeholder for generated image %%
	>*This would display a vertical gradient from black to white.*
- Color RGB Image (3D Array)
	```python
	import matplotlib.pyplot as plt
	import numpy as np

	# Create a sample 3D NumPy array (Height, Width, Channels)
	# Example: 100x100 image with random RGB values
	rgb_image = np.random.randint(0, 256, size=(100, 100, 3), dtype=np.uint8)

	plt.figure(figsize=(5, 5))
	plt.imshow(rgb_image) # Matplotlib infers RGB from (M,N,3) shape
	plt.title("Random Color RGB Image")
	plt.axis('off') # Turn off axis numbers and ticks for images
	plt.show()
	```
	![[imshow_rgb.png]] %% Placeholder for generated image %%
	>*This would display a 100x100 image of random colored pixels.*
- Loading and Displaying with Pillow & NumPy
	This is relevant to the NumPy worksheet exercise to "load a color image into a `np.ndarray` and zoom".
	```python
	import matplotlib.pyplot as plt
	import numpy as np
	from PIL import Image # Requires Pillow: pip install Pillow

	try:
	    # 1. Load image using Pillow
	    pil_img = Image.open("your_image.jpg") # Replace with an actual image path

	    # 2. Convert Pillow Image to NumPy array
	    img_array = np.array(pil_img)
	    print(f"Image shape: {img_array.shape}, dtype: {img_array.dtype}")

	    # 3. (Optional) Process/Slice the NumPy array (e.g., zoom)
	    height, width = img_array.shape[:2]
	    h_q, w_q = height // 4, width // 4
	    zoomed_part = img_array[h_q : height-h_q, w_q : width-w_q]

	    # 4. Display using Matplotlib
	    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

	    axes[0].imshow(img_array)
	    axes[0].set_title("Original Image")
	    axes[0].axis('off')

	    axes[1].imshow(zoomed_part)
	    axes[1].set_title("Central Part (Zoomed)")
	    axes[1].axis('off')

	    plt.tight_layout()
	    plt.show()

	except FileNotFoundError:
	    print("Error: 'your_image.jpg' not found. Please provide a valid image path.")
	except Exception as e:
	    print(f"An error occurred: {e}")
	```
	>*This code loads an image, converts it to a NumPy array, extracts a central part, and then displays both using `imshow`.*

## Related Concepts
- [[Matplotlib]], [[Pyplot_API]], [[Figure_Subplot_Axes]]
- [[NumPy_ndarray]], [[NumPy_Image_Representation]] (How images are stored in arrays)
- [[Pillow_PIL_MOC|Pillow (PIL)]] (Common library for image I/O)
- [[Colormaps_Matplotlib]] (For displaying 2D scalar data as images)
- Image Processing

---
**Source:** NumPy Worksheet Exercises (Implied), Matplotlib Documentation