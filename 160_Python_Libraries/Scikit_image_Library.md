---
tags:
  - python
  - library
  - scikit_image
  - skimage
  - image_processing
  - computer_vision
  - concept
aliases:
  - Skimage
related:
  - "[[_Python_Libraries_MOC]]"
  - "[[_NumPy_MOC]]"
  - "[[_Matplotlib_MOC]]"
  - "[[SciPy_Library]]"
  - "[[Pillow_PIL]]"
worksheet:
  - WS_Python_Packages_1
date_created: 2025-06-01
---
# Scikit-image Library

## Overview
**Scikit-image** (often imported as `skimage`) is an open-source Python library dedicated to **image processing**. It provides a versatile collection of algorithms for tasks such as filtering, segmentation, feature detection, geometric transformations, and more. Scikit-image is built on [[_NumPy_MOC|NumPy]], meaning images are represented as NumPy arrays, making it highly efficient and well-integrated with the scientific Python ecosystem.

The library focuses on providing well-documented, high-quality implementations of established image processing algorithms.

## Key Modules and Functionality
Scikit-image is organized into several submodules, each focusing on a specific aspect of image processing:

[list2tab|#Skimage Modules]
- **`skimage.io` (Image Input/Output)**
    - Reading images from files (`io.imread()`) and saving images (`io.imsave()`).
    - Supports various image formats (often via plugins like Pillow, imageio).
    - Example:
      ```python
      from skimage import io
      # import matplotlib.pyplot as plt
      # try:
      #     image = io.imread('path/to/your/image.jpg') # Replace with actual path
      #     # plt.imshow(image); plt.title("Loaded Image"); plt.axis('off'); plt.show()
      # except FileNotFoundError:
      #     print("Image file not found. Please provide a valid path.")
      #     image = None # Placeholder
      ```
- **`skimage.color` (Color Space Manipulation)**
    - Converting images between different color spaces (e.g., RGB to grayscale, RGB to HSV, RGB to LAB).
    - Example:
      ```python
      from skimage import color, data
      # import matplotlib.pyplot as plt
      # astronaut_rgb = data.astronaut() # Sample RGB image
      # astronaut_gray = color.rgb2gray(astronaut_rgb)
      # astronaut_hsv = color.rgb2hsv(astronaut_rgb)
      # fig, axes = plt.subplots(1, 3, figsize=(12, 4))
      # ax = axes.ravel()
      # ax[0].imshow(astronaut_rgb); ax[0].set_title("RGB")
      # ax[1].imshow(astronaut_gray, cmap='gray'); ax[1].set_title("Grayscale")
      # ax[2].imshow(astronaut_hsv); ax[2].set_title("HSV (Hue channel shown as intensity)")
      # for a in ax: a.axis('off')
      # plt.tight_layout(); plt.show()
      ```
- **`skimage.filters` (Image Filtering)**
    - Applying various filters for smoothing, sharpening, edge detection, etc.
    - Examples: Gaussian filter (`filters.gaussian`), median filter (`filters.median`), Sobel filter for edge detection (`filters.sobel`), Gabor filters.
    - Example (Sobel edge detection):
      ```python
      from skimage import filters, data, color
      # import matplotlib.pyplot as plt
      # camera = data.camera() # Sample grayscale image
      # edges_sobel = filters.sobel(camera)
      # fig, axes = plt.subplots(1, 2, figsize=(8, 4))
      # ax = axes.ravel()
      # ax[0].imshow(camera, cmap='gray'); ax[0].set_title("Original")
      # ax[1].imshow(edges_sobel, cmap='gray'); ax[1].set_title("Sobel Edges")
      # for a in ax: a.axis('off')
      # plt.tight_layout(); plt.show()
      ```
- **`skimage.transform` (Geometric Transformations)**
    - Resizing (`transform.resize`), rotation (`transform.rotate`), warping, Radon transform, Hough transform.
    - Example (Resizing):
      ```python
      from skimage import transform, data
      # import matplotlib.pyplot as plt
      # astronaut = data.astronaut()
      # resized_astronaut = transform.resize(astronaut, (astronaut.shape[0] // 2, astronaut.shape[1] // 2),
      #                                      anti_aliasing=True) # anti_aliasing for better quality
      # fig, axes = plt.subplots(1, 2, figsize=(8, 4))
      # ax = axes.ravel()
      # ax[0].imshow(astronaut); ax[0].set_title(f"Original {astronaut.shape[:2]}")
      # ax[1].imshow(resized_astronaut); ax[1].set_title(f"Resized {resized_astronaut.shape[:2]}")
      # for a in ax: a.axis('off')
      # plt.tight_layout(); plt.show()
      ```
- **`skimage.segmentation` (Image Segmentation)**
    - Algorithms for partitioning an image into multiple segments or regions.
    - Examples: Thresholding methods (e.g., Otsu's), active contours (snakes), SLIC superpixels, watershed algorithm.
    - Example (Otsu's thresholding):
      ```python
      from skimage import filters, data, color
      # import matplotlib.pyplot as plt
      # coins = data.coins() # Sample grayscale image
      # thresh_otsu = filters.threshold_otsu(coins)
      # binary_coins = coins > thresh_otsu
      # fig, axes = plt.subplots(1, 2, figsize=(8, 4))
      # ax = axes.ravel()
      # ax[0].imshow(coins, cmap='gray'); ax[0].set_title("Original")
      # ax[1].imshow(binary_coins, cmap='gray'); ax[1].set_title(f"Otsu Thresholded (t={thresh_otsu})")
      # for a in ax: a.axis('off')
      # plt.tight_layout(); plt.show()
      ```
- **`skimage.feature` (Feature Detection and Extraction)**
    - Identifying interesting points or regions in an image.
    - Examples: Canny edge detector (`feature.canny`), blob detection (Difference of Gaussian, Laplacian of Gaussian), corner detection (Harris, Shi-Tomasi), HOG (Histogram of Oriented Gradients), ORB, BRIEF.
    - Example (Canny edge detection):
      ```python
      from skimage import feature, data
      # import matplotlib.pyplot as plt
      # camera = data.camera()
      # edges_canny = feature.canny(camera, sigma=1.5) # sigma for Gaussian smoothing
      # fig, axes = plt.subplots(1, 2, figsize=(8, 4))
      # ax = axes.ravel()
      # ax[0].imshow(camera, cmap='gray'); ax[0].set_title("Original")
      # ax[1].imshow(edges_canny, cmap='gray'); ax[1].set_title("Canny Edges")
      # for a in ax: a.axis('off')
      # plt.tight_layout(); plt.show()
      ```
- **`skimage.measure` (Measurement of Image Regions)**
    - Calculating properties of labeled image regions (e.g., area, perimeter, centroid, bounding box).
    - Finding contours (`measure.find_contours`), region properties (`measure.regionprops`).
    - Example (Region properties):
      ```python
      from skimage import measure, data, filters, morphology
      # import matplotlib.pyplot as plt
      # coins = data.coins()
      # thresh = filters.threshold_otsu(coins)
      # binary = coins > thresh
      # # Clean up binary image a bit
      # cleaned = morphology.remove_small_objects(morphology.remove_small_holes(binary, 64), 64)
      # labeled_coins = measure.label(cleaned) # Label connected regions
      # regions = measure.regionprops(labeled_coins)
      # fig, ax = plt.subplots()
      # ax.imshow(coins, cmap='gray')
      # for region in regions:
      #     # Draw bounding box for regions with area > 100
      #     if region.area > 100:
      #         minr, minc, maxr, maxc = region.bbox
      #         rect = plt.Rectangle((minc, minr), maxc - minc, maxr - minr,
      #                              fill=False, edgecolor='red', linewidth=1)
      #         ax.add_patch(rect)
      # ax.set_title(f"{len(regions)} regions found (some filtered by area)")
      # ax.axis('off'); plt.show()
      ```
- **`skimage.morphology` (Morphological Operations)**
    - Operations like erosion, dilation, opening, closing, watershed segmentation, skeletonization. Used for modifying image shapes, noise removal, segmentation.
    - Example (Dilation):
      ```python
      from skimage import morphology, data, util
      # import matplotlib.pyplot as plt
      # horse = util.img_as_bool(data.horse()) # Sample binary image
      # selem = morphology.disk(3) # Structuring element (disk of radius 3)
      # dilated_horse = morphology.dilation(horse, selem)
      # fig, axes = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)
      # ax = axes.ravel()
      # ax[0].imshow(horse, cmap='gray'); ax[0].set_title("Original Binary")
      # ax[1].imshow(dilated_horse, cmap='gray'); ax[1].set_title("Dilated")
      # for a in ax: a.axis('off')
      # plt.tight_layout(); plt.show()
      ```
- **`skimage.restoration` (Image Restoration)**
    - Algorithms for de-noising, deconvolution, inpainting.
- **`skimage.draw` (Drawing Primitives)**
    - Functions to draw lines, circles, polygons, text, etc., on NumPy arrays.
- **`skimage.data` (Sample Images)**
    - Provides a set of standard images for testing and demonstration (e.g., `data.camera()`, `data.coins()`, `data.astronaut()`).
- **`skimage.util` (Utility Functions)**
    - Conversion between data types (e.g., `img_as_float`, `img_as_ubyte`), padding, view_as_windows.

## Common Applications
- **Scientific Image Analysis:** Microscopy, medical imaging (though specialized libraries like `SimpleITK` or `NiBabel` are often used for medical formats), astronomy.
- **Computer Vision Preprocessing:** Preparing images for tasks like object detection, recognition, or tracking.
- **Automated Quality Control:** Inspecting manufactured parts.
- **Remote Sensing:** Analyzing satellite or aerial imagery.
- **Art and Graphics:** Image manipulation and effects.
- **Education and Research:** Provides a clean and Pythonic way to learn and experiment with image processing algorithms.

Scikit-image is valued for its clear API, good documentation, educational focus, and its seamless integration with the scientific Python stack, making it an excellent choice for a wide range of image processing tasks. It typically doesn't handle deep learning based image tasks itself (for which libraries like TensorFlow/Keras or PyTorch are used), but it's excellent for classical image processing algorithms and preprocessing.

---