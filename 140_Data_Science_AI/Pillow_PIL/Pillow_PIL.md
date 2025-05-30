---
tags:
  - pillow
  - pil
  - python
  - library
  - image_processing
aliases:
  - Pillow Library
  - Python Imaging Library (Fork)
related:
  - "[[Python]]"
  - "[[NumPy]]"
  - "[[Matplotlib_MOC|Matplotlib]]"
  - "[[Image_Object_Pillow]]"
  - "[[Image_File_Formats_Pillow]]"
  - "[[NumPy_Pillow_Conversion]]"
worksheet: [WS_NumPy] # Implied by exercises requiring image loading
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Pillow (PIL Fork)

## Definition

**Pillow** is the "friendly fork" of **PIL (Python Imaging Library)**. PIL itself is no longer maintained (last release in 2009), and Pillow is the active, maintained library that provides extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities. It is the de facto standard image manipulation library for Python.

## Key Features

- **Wide File Format Support:** Supports a large variety of image file formats for reading and writing, including PNG, JPEG, GIF, TIFF, BMP, WebP, and many more. See [[Image_File_Formats_Pillow]].
- **[[Image_Object_Pillow|`Image` Module/Class]]:** The core of the library is the `Image` module, which provides the `Image` class to represent an image.
- **Pixel-Level Access:** Allows direct manipulation of pixel data.
- **Image Manipulation:** Provides a range of functions for common image manipulations:
    - Resizing, cropping, rotating, flipping.
    - Color space conversions (e.g., RGB to Grayscale - [[Image_Modes_Pillow]]).
    - Applying filters (blur, sharpen, edge detection, etc. via `ImageFilter`).
    - Adjusting brightness, contrast, color, sharpness (via `ImageEnhance`).
    - Drawing basic shapes and text on images (via `ImageDraw`).
- **[[NumPy_Pillow_Conversion|Integration with NumPy]]:** Easy conversion between Pillow `Image` objects and [[NumPy_ndarray|NumPy arrays]], making it suitable for use in scientific computing and machine learning pipelines where images are often processed as arrays.
- **Animation Support:** Can work with animated formats like GIF.

## Installation

```bash
pip install Pillow
```

## Basic Usage Example

```python
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import numpy as np
import os # For file checks

# --- 1. Opening an Image ---
try:
    img = Image.open("example.jpg") # Replace with your image path
    print(f"Image format: {img.format}, Size: {img.size}, Mode: {img.mode}")

    # --- 2. Basic Manipulations ---
    # Resize
    resized_img = img.resize((img.width // 2, img.height // 2))

    # Convert to grayscale
    grayscale_img = img.convert("L") # "L" mode is for grayscale

    # Rotate
    rotated_img = img.rotate(45) # Rotates 45 degrees counter-clockwise

    # Apply a filter
    blurred_img = img.filter(ImageFilter.GaussianBlur(radius=2))

    # --- 3. Saving an Image ---
    resized_img.save("example_resized.png") # Can change format on save
    grayscale_img.save("example_grayscale.jpg")

    # --- 4. Converting to/from NumPy array ---
    img_array = np.array(img) # Pillow Image to NumPy array
    print(f"NumPy array shape: {img_array.shape}, dtype: {img_array.dtype}")

    img_from_array = Image.fromarray(img_array) # NumPy array back to Pillow Image

    # --- 5. Drawing on an Image (Example) ---
    # Create a new blank image or use an existing one
    # For this example, let's draw on a copy of the original
    img_to_draw_on = img.copy()
    draw = ImageDraw.Draw(img_to_draw_on)
    try:
        # Attempt to load a system font; fallback if not found
        font = ImageFont.truetype("arial.ttf", 40)
    except IOError:
        font = ImageFont.load_default()
    draw.text((10, 10), "Hello Pillow!", fill="red", font=font)
    img_to_draw_on.save("example_with_text.png")


    # --- 6. Displaying (often done with Matplotlib for inline viewing) ---
    img.show() # Opens in default image viewer
    # To display with matplotlib:
    import matplotlib.pyplot as plt
    plt.imshow(img_array)
    plt.title("Image via Matplotlib")
    plt.axis('off')
    plt.show()

except FileNotFoundError:
    print("Error: 'example.jpg' not found. Please create or use a valid image path.")
except Exception as e:
    print(f"An error occurred: {e}")

# Clean up example files if created
if os.path.exists("example_resized.png"): os.remove("example_resized.png")
if os.path.exists("example_grayscale.jpg"): os.remove("example_grayscale.jpg")
if os.path.exists("example_with_text.png"): os.remove("example_with_text.png")
```

## Related Concepts
- [[Python]], [[Image_Processing]]
- [[Image_Object_Pillow]], [[Image_File_Formats_Pillow]], [[Image_Modes_Pillow]]
- [[NumPy_ndarray]], [[NumPy_Pillow_Conversion]] (For numerical processing)
- [[Matplotlib_MOC|Matplotlib]] (Often used for displaying images from Pillow/NumPy)
- OpenCV (`cv2`), Scikit-image (Alternative/complementary image processing libraries)

---
**Source:** NumPy Worksheet Exercises (Implied), Pillow Documentation