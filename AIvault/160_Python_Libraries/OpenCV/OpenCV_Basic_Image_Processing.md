---
tags:
  - python
  - opencv
  - cv2
  - computer_vision
  - image_processing
  - color_space
  - geometric_transformations
  - thresholding
  - concept
  - example
aliases:
  - OpenCV Image Processing Basics
  - cv2.cvtColor
  - cv2.resize
  - cv2.threshold
related:
  - "[[160_Python_Libraries/OpenCV/_OpenCV_MOC|_OpenCV_MOC]]"
  - "[[OpenCV_Reading_Writing_Displaying]]"
  - "[[_NumPy_MOC]]"
worksheet:
  - WS_ComputerVision_1
date_created: 2025-08-20
---

# OpenCV: Basic Image Processing

OpenCV provides a vast toolkit for performing basic image processing operations. These are fundamental steps in many computer vision pipelines. All operations are performed on [[_NumPy_MOC|NumPy arrays]].

## Color Space Conversions
OpenCV allows for easy conversion between color spaces (e.g., BGR, RGB, Grayscale, HSV). Remember, OpenCV's default is **BGR**.

**Example:**
```python
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Create a sample BGR color image (Blue, Green, Red squares)
bgr_image = np.zeros((100, 300, 3), dtype=np.uint8)
bgr_image[:, 0:100] =   # Blue
bgr_image[:, 100:200] = # Green
bgr_image[:, 200:300] = # Red

# Convert to Grayscale
gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)

# Convert to RGB for correct display in Matplotlib
rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)

# Convert to HSV (Hue, Saturation, Value)
hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)

# Display results
fig, axes = plt.subplots(1, 4, figsize=(16, 4))
axes.imshow(bgr_image); axes.set_title('Original BGR (Matplotlib shows as RGB)')
axes.imshow(gray_image, cmap='gray'); axes.set_title('Grayscale')
axes.imshow(rgb_image); axes.set_title('Converted to RGB')
axes.imshow(hsv_image); axes.set_title('Converted to HSV')
for ax in axes: ax.axis('off')
plt.tight_layout(); plt.show()
```

## Geometric Transformations
[list2tab|#Geometric Transformations]
- Scaling (Resizing)
    - **Example:**
        ```python
        # (using rgb_image from previous example)
        height, width = rgb_image.shape[:2]
        # Resize to half the original dimensions
        resized_half = cv2.resize(rgb_image, (width // 2, height // 2), interpolation=cv2.INTER_LINEAR)
        # Resize by a scale factor
        resized_double = cv2.resize(rgb_image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        print(f"Original shape: {rgb_image.shape}, Resized to half: {resized_half.shape}, Resized to double: {resized_double.shape}")
        ```
- Translation (Shifting)
    - **Example (Shift image 50 pixels right, 20 pixels down):**
        ```python
        # (using rgb_image)
        height, width = rgb_image.shape[:2]
        tx, ty = 50, 20
        translation_matrix = np.float32([,])
        translated_image = cv2.warpAffine(rgb_image, translation_matrix, (width, height))
        plt.imshow(translated_image); plt.title('Translated Image'); plt.show()
        ```
- Rotation
    - **Example (Rotate image 45 degrees around the center):**
        ```python
        # (using rgb_image)
        height, width = rgb_image.shape[:2]
        center = (width // 2, height // 2)
        angle = 45 # degrees
        scale = 1.0 # no scaling
        rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
        rotated_image = cv2.warpAffine(rgb_image, rotation_matrix, (width, height))
        plt.imshow(rotated_image); plt.title('Rotated Image'); plt.show()
        ```

## Image Thresholding
Thresholding is used to create a binary image.

**Example (Simple Binary & Otsu's Thresholding):**
```python
# (using gray_image from first example)
ret, binary_thresh_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
print(f"Threshold value used: {ret}")

# Example with Otsu's Thresholding
ret_otsu, otsu_thresh_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print(f"Otsu's optimal threshold value: {ret_otsu}")

fig, axes = plt.subplots(1, 3, figsize=(12, 4))
axes.imshow(gray_image, cmap='gray'); axes.set_title('Original Grayscale')
axes.imshow(binary_thresh_image, cmap='gray'); axes.set_title('Simple Threshold (127)')
axes.imshow(otsu_thresh_image, cmap='gray'); axes.set_title("Otsu's Threshold")
for ax in axes: ax.axis('off')
plt.show()
```

## Image Filtering and Blurring
Used for noise reduction and smoothing.

**Example (Gaussian Blurring):**
```python
# (using rgb_image)
# Apply a Gaussian blur with a 5x5 kernel
blurred_image = cv2.GaussianBlur(rgb_image, (5, 5), 0) # (ksize_x, ksize_y), sigmaX

fig, axes = plt.subplots(1, 2, figsize=(8, 4))
axes.imshow(rgb_image); axes.set_title('Original')
axes.imshow(blurred_image); axes.set_title('Gaussian Blurred')
for ax in axes: ax.axis('off')
plt.show()
```

---