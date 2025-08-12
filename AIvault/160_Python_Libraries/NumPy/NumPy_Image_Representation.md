---
tags:
  - numpy
  - python
  - image_processing
  - data_representation
  - concept
aliases:
  - NumPy Image Array
  - Digital Image Representation NumPy
related:
  - "[[NumPy_ndarray]]"
  - "[[Pillow_PIL_MOC|Pillow (PIL)]]"
  - "[[Matplotlib_MOC|Matplotlib]]"
  - "[[Color_Spaces]]"
  - "[[Pixel]]" # Placeholder
worksheet: [WS_NumPy]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Digital Image Representation in NumPy

## Definition

Digital images can be naturally represented using [[NumPy_ndarray|NumPy `ndarray`s]]. The structure of the array depends on the type of image:

1.  **Black & White (Binary) Image:**
    -   Typically represented as a **2D `ndarray`** with a boolean `dtype` (`np.bool_`) or an integer `dtype` (e.g., `np.uint8`) where values are restricted to 0 (black) and 1 (white) (or 0 and 255).
    -   Shape: `(height, width)`

2.  **Grayscale Image:**
    -   Represented as a **2D `ndarray`**.
    -   Each element represents the intensity (brightness) of a pixel.
    -   `dtype` is typically `np.uint8` (values 0-255, where 0 is black, 255 is white) or `np.float32`/`np.float64` (values often normalized to 0.0-1.0).
    -   Shape: `(height, width)`

3.  **Color Image:**
    -   Typically represented as a **3D `ndarray`**.
    -   The dimensions usually correspond to: `(height, width, channels)`.
    -   **Channels:** Represent the color components. Common channel orders:
        -   **RGB:** 3 channels (Red, Green, Blue). Shape: `(height, width, 3)`.
        -   **RGBA:** 4 channels (Red, Green, Blue, Alpha - for transparency). Shape: `(height, width, 4)`.
        -   Other [[Color_Spaces]] like HSV, CMYK are also possible but might be stored differently or require conversion.
    -   `dtype` is usually `np.uint8` (values 0-255 per channel) or `np.float32`/`np.float64` (values 0.0-1.0 per channel).

## AnyBlock Visualization: Image Array Structures

[list2tab]
- Grayscale Image
	A `(H, W)` 2D NumPy array. Each element is a pixel intensity.
	```python
	import numpy as np
	# Example: 2x3 grayscale image
	grayscale_img = np.array([
	    ,  # Row 0
	    ], # Row 1
	    dtype=np.uint8
	)
	# grayscale_img.shape -> (2, 3)
	```
	```d2
	# Grayscale Image (H=2, W=3)
	img: {
	  shape: "2x3 Matrix"
	  "Pixel (0,0) intensity"
	  "Pixel (0,1) intensity"
	  "Pixel (0,2) intensity"
	  "Pixel (1,0) intensity"
	  "Pixel (1,1) intensity"
	  "Pixel (1,2) intensity"
	  # Arrange in grid
	  { direction: right; 0: {direction: down; "Pixel (0,0) intensity"; "Pixel (1,0) intensity"}}
	  { direction: right; 1: {direction: down; "Pixel (0,1) intensity"; "Pixel (1,1) intensity"}}
	  { direction: right; 2: {direction: down; "Pixel (0,2) intensity"; "Pixel (1,2) intensity"}}
	}
	```
- Color (RGB) Image
	A `(H, W, 3)` 3D NumPy array. Each `(i, j)` location holds 3 values [R, G, B].
	```python
	import numpy as np
	# Example: 1x2 RGB image (1 row, 2 pixels, 3 channels)
	rgb_img = np.array([
	    [ ,  ]  # Pixel (0,0) & Pixel (0,1)
	], dtype=np.uint8)
	# rgb_img.shape -> (1, 2, 3)
	```
	```d2
	# RGB Image (H=1, W=2, C=3)
	pixel_0_0: "R00 G00 B00"
	pixel_0_1: "R01 G01 B01"

	layer: {
	  direction: right
	  p00: pixel_0_0
	  p01: pixel_0_1
	}

	label: "Pixel (row, col) = [R, G, B]"
	```
	Conceptual Access:
	- `rgb_img[y, x]` gives the `[R, G, B]` triplet for pixel at (y,x).
	- `rgb_img[y, x, 0]` gives the Red value for pixel at (y,x).
	- `rgb_img[:, :, 0]` gives the entire Red channel as a 2D array.
- Color (RGBA) Image
	A `(H, W, 4)` 3D NumPy array. Each `(i, j)` location holds 4 values [R, G, B, A].
	```python
	import numpy as np
	# Example: 1x1 RGBA image
	rgba_img = np.array([
	    [ ] # Pixel (0,0)
	], dtype=np.uint8)
	# rgba_img.shape -> (1, 1, 4)
	```
	Similar structure to RGB, but with an added Alpha channel for transparency.

## Libraries for Image I/O and Manipulation

- **[[Pillow_PIL_MOC|Pillow (PIL Fork)]]:** Commonly used for opening, manipulating, and saving images in various formats. Images opened with Pillow can be easily converted to/from NumPy arrays.
  ```python
  from PIL import Image
  import numpy as np

  # Load image with Pillow and convert to NumPy array
  pil_img = Image.open("my_image.png")
  numpy_image = np.array(pil_img)

  # Convert NumPy array back to Pillow Image
  pil_img_from_numpy = Image.fromarray(numpy_image)
  ```
- **[[Matplotlib_MOC|Matplotlib]]:** Used for displaying images represented as NumPy arrays (`plt.imshow(numpy_image)`).
- **OpenCV (`cv2`):** Powerful library for computer vision; uses NumPy arrays extensively for image representation (often in BGR order by default).
- **Scikit-image:** Another library for image processing, also heavily based on NumPy arrays.

## Related Concepts
- [[NumPy_ndarray]], [[NumPy_Dimension_Shape_Axis]]
- [[Pillow_PIL_MOC|Pillow (PIL)]], [[Matplotlib_MOC|Matplotlib]], OpenCV (Libraries for image handling)
- [[Pixel]] (Individual element of an image)
- [[Color_Spaces]] (RGB, RGBA, Grayscale, HSV, etc.)
- Image File Formats (JPEG, PNG, GIF, TIFF, BMP)

## Questions / Further Study
>[!question] What is the difference between a black & white picture and a color picture (in terms of NumPy representation)? (WS_NumPy)
> - **Black & White (Binary):** Typically a 2D NumPy array, `shape=(height, width)`. Each element is a single value representing black (0) or white (1 or 255). `dtype` is often `bool` or `uint8`.
> - **Grayscale:** Also a 2D NumPy array, `shape=(height, width)`. Each element is an intensity value (e.g., 0-255 for `uint8`).
> - **Color (e.g., RGB):** Typically a 3D NumPy array, `shape=(height, width, 3)`. The third dimension (axis 2) represents the color channels (Red, Green, Blue). Each `(row, col)` location contains a triplet of values like `[R, G, B]`. For RGBA, it would be `shape=(height, width, 4)`.

>[!question] Exercise: "Write a function that returns the central part of a matrix (excluding the first and last quarter of the rows and columns). Then load a color image into a `np.ndarray` and zoom into the central part of the picture."
> This exercise directly applies array slicing.
> ```python
> import numpy as np
> from PIL import Image # Assuming Pillow is used for loading
>
> def get_central_part(matrix):
>     rows, cols = matrix.shape[:2] # Get H, W (works for 2D or 3D)
>     row_quarter = rows // 4
>     col_quarter = cols // 4
>
>     # Slicing: start_row:end_row, start_col:end_col
>     # Excludes first quarter and last quarter
>     central_matrix = matrix[row_quarter : rows - row_quarter,
>                             col_quarter : cols - col_quarter]
>     return central_matrix
>
> # Example usage with an image
> try:
>     img = Image.open("your_image.jpg") # Load image using Pillow
>     img_array = np.array(img)       # Convert to NumPy array
>
>     print(f"Original image shape: {img_array.shape}")
>
>     central_image_part = get_central_part(img_array)
>     print(f"Central part shape: {central_image_part.shape}")
>
>     # To display (using Matplotlib):
>     # import matplotlib.pyplot as plt
>     # fig, axes = plt.subplots(1, 2)
>     # axes[0].imshow(img_array)
>     # axes[0].set_title("Original")
>     # axes[1].imshow(central_image_part)
>     # axes[1].set_title("Central Part (Zoomed)")
>     # plt.show()
>
>     # To save the central part (using Pillow):
>     # central_pil_img = Image.fromarray(central_image_part)
>     # central_pil_img.save("central_part.jpg")
>
> except FileNotFoundError:
>     print("Error: Image file not found. Replace 'your_image.jpg' with an actual image path.")
> except Exception as e:
>     print(f"An error occurred: {e}")
> ```
> **Explanation:**
> - The function calculates one-quarter of the rows and columns.
> - It then uses NumPy's powerful slicing `[start:end]` for both row and column axes. For rows, it takes from `row_quarter` up to (but not including) `rows - row_quarter`. Similar logic applies to columns.
> - If `matrix` is a 3D color image array (H, W, C), the slicing `matrix[r_start:r_end, c_start:c_end]` automatically includes all color channels for the selected pixel region.

---
**Source:** Worksheet WS_NumPy, NumPy & Pillow Documentation