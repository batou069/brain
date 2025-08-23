---
tags:
  - python
  - opencv
  - cv2
  - computer_vision
  - image_analysis
  - feature_detection
  - edge_detection
  - contours
  - histograms
  - concept
  - example
aliases:
  - OpenCV Feature Detection
  - Canny Edge Detection
  - OpenCV Contours
  - Image Histograms
related:
  - "[[160_Python_Libraries/OpenCV/_OpenCV_MOC|_OpenCV_MOC]]"
  - "[[OpenCV_Basic_Image_Processing]]"
worksheet:
  - WS_ComputerVision_1
date_created: 2025-08-20
---
# OpenCV: Image Analysis and Feature Detection

OpenCV provides a rich set of tools for analyzing images to extract meaningful features and information. This includes detecting edges, finding contours of objects, and analyzing pixel intensity distributions.

## Edge Detection
Edge detection is a fundamental technique for identifying points in a digital image at which the image brightness changes sharply.

**Example (Canny Edge Detection):**
```python
import cv2
import matplotlib.pyplot as plt
from skimage import data # Using scikit-image for a sample image
import numpy as np

# Load a sample image and convert to grayscale
try:
    image = data.camera()
except Exception:
    # Fallback if skimage.data is not available
    image = np.random.randint(0, 256, (256, 256), dtype=np.uint8)

if image is not None:
    # Apply Canny edge detection
    edges = cv2.Canny(image, threshold1=100, threshold2=200)

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes.imshow(image, cmap='gray'); axes.set_title('Original Image')
    axes.imshow(edges, cmap='gray'); axes.set_title('Canny Edges')
    for ax in axes: ax.axis('off')
    plt.show()
```

## Contours
Contours are curves joining all continuous points along a boundary that have the same color or intensity. They are useful for shape analysis and object detection.

**Example (Finding and drawing contours of coins):**
```python
import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage import data

# Load coins image and create a binary version
try:
    coins_image = data.coins()
except Exception:
    # Fallback if skimage.data is not available
    coins_image = np.zeros((256,256), dtype=np.uint8)
    cv2.circle(coins_image, (64,64), 30, 200, -1)
    cv2.circle(coins_image, (180,128), 50, 150, -1)

ret, thresh = cv2.threshold(coins_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Find contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create a color image to draw contours on
output_image = cv2.cvtColor(coins_image, cv2.COLOR_GRAY2BGR)

# Draw all found contours
# -1 in the contourIdx parameter means draw all contours
cv2.drawContours(output_image, contours, -1, (0, 255, 0), 2) # Draw in green with thickness 2

print(f"Found {len(contours)} contours.")

fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes.imshow(thresh, cmap='gray'); axes.set_title('Binary Image')
axes.imshow(cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB)); axes.set_title('Contours Drawn')
for ax in axes: ax.axis('off')
plt.show()
```

## Histograms
An image histogram is a graphical representation of the intensity distribution in an image.

**Example (Calculating and plotting a grayscale histogram):**
```python
import cv2
import matplotlib.pyplot as plt
from skimage import data
import numpy as np

try:
    image = data.camera()
except Exception:
    image = np.random.randint(0, 256, (256, 256), dtype=np.uint8)

# Calculate histogram using OpenCV
# The image must be in a list: [image]
hist = cv2.calcHist([image],, None,,)

# Plot histogram using Matplotlib
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.plot(hist)
plt.title('Grayscale Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Number of Pixels')
plt.xlim()
plt.grid(True)
plt.tight_layout()
plt.show()
```

---