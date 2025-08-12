---
tags:
  - pillow
  - pil
  - numpy
  - python
  - image_processing
  - data_conversion
  - interop
aliases:
  - Pillow to NumPy
  - NumPy to Pillow
  - Image to Array
  - Array to Image
related:
  - "[[Pillow_PIL]]"
  - "[[NumPy_ndarray]]"
  - "[[Image_Object_Pillow]]"
  - "[[NumPy_Image_Representation]]"
worksheet: [WS_NumPy] # Implied by exercises
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Pillow Image <=> NumPy Array Conversion

## Definition

Seamless conversion between Pillow `Image` objects and [[NumPy_ndarray|NumPy arrays]] is a crucial feature for image processing pipelines in Python. Pillow is excellent for image I/O and many basic manipulations, while NumPy provides powerful numerical operations ideal for more complex image processing algorithms, machine learning model inputs, etc.

## Pillow `Image` to NumPy `ndarray`

This is achieved using `numpy.array()` or `numpy.asarray()`.

- **`np.array(pil_image)`:**
    - Creates a NumPy array from a Pillow `Image` object.
    - This usually creates a **copy** of the image data.
    - The resulting `ndarray`'s shape and `dtype` depend on the image's mode:
        - **'L' (Grayscale):** 2D array, `dtype=uint8`. Shape `(height, width)`.
        - **'RGB':** 3D array, `dtype=uint8`. Shape `(height, width, 3)`.
        - **'RGBA':** 3D array, `dtype=uint8`. Shape `(height, width, 4)`.
        - Other modes might result in different structures or require conversion first.

- **`np.asarray(pil_image)`:**
    - Similar to `np.array()`, but if the Pillow image object already supports the array interface in a compatible way (which is generally true for modern Pillow), it *might* avoid a copy if possible, creating a view. However, for safety and typical usage with Pillow `Image` objects, assume it behaves much like `np.array()` and often makes a copy when converting from the Pillow internal representation.

```python
from PIL import Image
import numpy as np

try:
    # Load image using Pillow
    pil_img = Image.open("your_image.png") # Example: an RGBA PNG
    print(f"Pillow Image Mode: {pil_img.mode}, Size: {pil_img.size}")

    # Convert to NumPy array
    img_array = np.array(pil_img)
    print(f"NumPy Array Shape: {img_array.shape}") # e.g., (height, width, 4) for RGBA
    print(f"NumPy Array Dtype: {img_array.dtype}")   # e.g., uint8

    # Example: Modify the NumPy array (changes will NOT affect pil_img directly here)
    # img_array[0, 0] = [255, 0, 0, 255] # Change top-left pixel to red

except FileNotFoundError:
    print("Image file not found.")
except Exception as e:
    print(f"An error occurred: {e}")
```

## NumPy `ndarray` to Pillow `Image`

This is achieved using `Image.fromarray(numpy_array, mode=None)`.

- **`Image.fromarray(obj, mode=None)`:**
    - Creates a Pillow `Image` object from an object exporting the array interface (like a NumPy array).
    - **Shares memory if possible (view-like behavior):** If the NumPy array has a compatible `dtype` (e.g., `uint8`, `int32`, `float32`) and memory layout, `Image.fromarray` tries to create an image that shares the memory buffer with the NumPy array. Changes to the NumPy array's data *after* creating the Pillow image *may* reflect in the image object, and vice-versa (depending on internal Pillow copying for certain operations).
    - **`mode` parameter:**
        - If `None` (default), Pillow attempts to infer the mode from the array's `dtype` and `shape`:
            - `(H, W)` with `uint8` -> 'L' (Grayscale)
            - `(H, W)` with `bool` -> '1' (Binary)
            - `(H, W, 3)` with `uint8` -> 'RGB'
            - `(H, W, 4)` with `uint8` -> 'RGBA'
            - Float arrays are typically scaled to 0-255 and converted to 'L' or 'F' mode.
        - You can explicitly specify the mode (e.g., `mode='L'`, `mode='RGB'`) if the inference is not correct or to force a conversion.

```python
from PIL import Image
import numpy as np

# Create a sample NumPy array (e.g., representing an RGB image)
# Shape (height, width, channels), dtype=uint8
image_data = np.random.randint(0, 256, size=(100, 150, 3), dtype=np.uint8)

# Convert NumPy array to Pillow Image
pil_image_from_array = Image.fromarray(image_data) # Mode 'RGB' inferred
print(f"Pillow Image Mode from array: {pil_image_from_array.mode}")
print(f"Pillow Image Size from array: {pil_image_from_array.size}")

# pil_image_from_array.show()
# pil_image_from_array.save("from_numpy.png")

# Example with grayscale
gray_data = np.array([, ], dtype=np.uint8)
pil_gray = Image.fromarray(gray_data, mode='L') # Can specify mode 'L'
# pil_gray.show()
```

## Key Considerations

- **Data Types:** `uint8` is most common for standard image display and saving in formats like JPEG/PNG. Float arrays (often 0.0-1.0 range) are common in processing pipelines and need appropriate scaling/conversion before saving to typical 8-bit image formats or display.
- **Channel Order:** For color images, ensure the NumPy array has the channels in the expected order (usually H, W, C with C being RGB or RGBA for Pillow). Libraries like OpenCV might use BGR by default, requiring conversion.
- **Views vs. Copies:**
    - `np.array(pil_image)` usually creates a copy.
    - `Image.fromarray(numpy_array)` often tries to share memory (view-like), but Pillow might make internal copies during subsequent operations. If you need to ensure the Pillow image is independent after creation, use `Image.fromarray(numpy_array.copy())`.

## Related Concepts
- [[Pillow_PIL]], [[Image_Object_Pillow]], [[Image_Modes_Pillow]]
- [[NumPy_ndarray]], [[NumPy_Image_Representation]], [[NumPy_Data_Types]]
- [[Data_Conversion]], Image I/O

---
**Source:** NumPy Worksheet Exercises (Implied), Pillow & NumPy Documentation