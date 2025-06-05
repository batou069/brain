---
tags:
  - data_science
  - image_processing
  - numpy
  - pillow
  - matplotlib
  - workflow
  - concept
aliases:
  - Basic Image Workflow
  - NumPy Image Manipulation
  - Pillow Image Loading
related:
  - "[[NumPy]]"
  - "[[NumPy_ndarray]]"
  - "[[NumPy_Image_Representation]]"
  - "[[Pillow_PIL]]"
  - "[[NumPy_Pillow_Conversion]]"
  - "[[Matplotlib]]"
  - "[[Image_Display_Matplotlib]]"
  - "[[NumPy_Indexing_Slicing]]"
worksheet:
  - WS_DS_Workflow_Concepts_1
date_created: 2025-05-30
---
# Image Processing Workflow (NumPy, Pillow, Matplotlib)

This note outlines a basic workflow for image processing tasks using common Python libraries: [[Pillow_PIL|Pillow (PIL Fork)]] for image loading and basic manipulation, [[NumPy]] for numerical operations on image data (as images are represented as [[NumPy_ndarray|NumPy arrays]]), and [[Matplotlib]] for displaying images.

## Core Libraries
- **[[Pillow_PIL|Pillow (PIL Fork)]]:** Used for opening, manipulating, and saving many different image file formats. It provides an `Image` object.
- **[[NumPy]]:** Essential for numerical computing. Images are converted to NumPy arrays (see [[NumPy_Image_Representation]]) to perform mathematical operations, pixel manipulations, slicing, etc.
- **[[Matplotlib]]:** Used for displaying images (and other plots) within Python environments. (See [[Image_Display_Matplotlib]])

## Basic Image Processing Workflow

[list2card|addClass(ab-col1)|#Image Processing Steps]
- **1. Loading an Image**
    - **Action:** Read an image file from disk into memory.
    - **Tool:** `PIL.Image.open()`
    - **Output:** A Pillow `Image` object.
    ```python
    from PIL import Image
    import numpy as np
    import matplotlib.pyplot as plt

    # Assume 'sample_image.png' exists
    try:
        img_pil = Image.open('sample_image.png') # Replace with your image path
        print(f"Image loaded successfully. Format: {img_pil.format}, Size: {img_pil.size}, Mode: {img_pil.mode}")
    except FileNotFoundError:
        print("Error: sample_image.png not found. Please replace with a valid image path.")
        # Create a dummy image for workflow continuation if file not found
        img_pil = Image.new('RGB', (100, 100), color = 'red') 
    ```

- **2. Converting Image to NumPy Array**
    - **Action:** Transform the Pillow `Image` object into a NumPy array for numerical processing. (See [[NumPy_Pillow_Conversion]])
    - **Tool:** `np.array(image_object)`
    - **Output:** A NumPy `ndarray`. The shape of the array depends on the image:
        - Grayscale image: `(height, width)`
        - RGB image: `(height, width, 3)` (3 channels for Red, Green, Blue)
        - RGBA image: `(height, width, 4)` (4 channels for Red, Green, Blue, Alpha/transparency)
        - Data type is usually `uint8` (0-255).
    ```python
    img_np = np.array(img_pil)
    print(f"Image as NumPy array. Shape: {img_np.shape}, Data type: {img_np.dtype}")
    ```

- **3. Image Manipulation with NumPy**
    - **Action:** Perform various operations on the image data using NumPy's array manipulation capabilities.
    - **Tools:** [[NumPy_Indexing_Slicing|NumPy indexing and slicing]], arithmetic operations, universal functions (ufuncs).
    - **Common Manipulations:**
        - **Cropping:** Select a sub-region of the image.
          ```python
          # Example: Crop a 50x50 region from top-left, if image is large enough
          if img_np.shape[0] > 50 and img_np.shape[1] > 50:
              cropped_img_np = img_np[0:50, 0:50] 
              # plt.imshow(cropped_img_np)
              # plt.title("Cropped Image")
              # plt.show()
          else:
              cropped_img_np = img_np # No crop if too small
              print("Image too small to crop as specified, using original.")
          ```
        - **Color Channel Separation/Manipulation (for RGB/RGBA):**
          ```python
          if img_np.ndim == 3 and img_np.shape[2] >= 3: # Check if it's a color image
              red_channel = img_np[:, :, 0]
              green_channel = img_np[:, :, 1]
              blue_channel = img_np[:, :, 2]

              # Example: Create an image with only the red channel visible
              img_only_red = np.zeros_like(img_np)
              img_only_red[:, :, 0] = red_channel
              # plt.imshow(img_only_red)
              # plt.title("Red Channel Only")
              # plt.show()
          ```
        - **Changing Intensity/Brightness:** Add or multiply pixel values (clipping might be needed to keep values in range).
          ```python
          # Increase brightness (careful with dtype and clipping)
          # brighter_img_np = np.clip(img_np.astype(np.int16) + 50, 0, 255).astype(np.uint8)
          # plt.imshow(brighter_img_np)
          # plt.title("Brighter Image")
          # plt.show()
          ```
        - **Converting to Grayscale (simple average method, more sophisticated methods exist):**
          ```python
          if img_np.ndim == 3 and img_np.shape[2] >= 3:
              grayscale_img_np = img_np[:, :, :3].mean(axis=2).astype(np.uint8)
              # plt.imshow(grayscale_img_np, cmap='gray')
              # plt.title("Grayscale Image (Average)")
              # plt.show()
          elif img_np.ndim == 2: # Already grayscale
                grayscale_img_np = img_np
                print("Image is already grayscale.")
          ```
        - **Masking:** Applying an operation to a selected region based on a binary mask.
          ```python
          # # Create a circular mask (example)
          # if img_np.ndim >=2: # Ensure it's at least 2D
          #     center_x, center_y = img_np.shape[1] // 2, img_np.shape[0] // 2
          #     radius = min(center_x, center_y) // 2
          #     y, x = np.ogrid[:img_np.shape[0], :img_np.shape[1]]
          #     mask = (x - center_x)**2 + (y - center_y)**2 <= radius**2
          #
          #     masked_img_np = img_np.copy()
          #     if img_np.ndim == 3:
          #         masked_img_np[~mask] = 0 # Set pixels outside mask to black
          #     elif img_np.ndim == 2:
          #         masked_img_np[~mask] = 0
          #     # plt.imshow(masked_img_np)
          #     # plt.title("Masked Image")
          #     # plt.show()
          ```

- **4. Converting NumPy Array back to Pillow Image (Optional)**
    - **Action:** If you need to save the processed image or use Pillow-specific functions.
    - **Tool:** `Image.fromarray(numpy_array)`
    - **Input:** A NumPy array (ensure dtype is `uint8` and values are in range for standard image modes).
    ```python
    # Assuming 'processed_img_np' is the result of some NumPy manipulation
    processed_img_np = img_np # Placeholder if no specific processing shown above was run
    processed_img_pil = Image.fromarray(processed_img_np)
    print(f"Processed image converted back to PIL Image. Mode: {processed_img_pil.mode}")
    ```

- **5. Displaying Images**
    - **Action:** Show the original or processed image.
    - **Tool:** `matplotlib.pyplot.imshow()` (See [[Image_Display_Matplotlib]])
    ```python
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(img_pil) # Can display Pillow image directly
    plt.title("Original Image (via PIL)")
    plt.axis('off')

    plt.subplot(1, 2, 2)
    # Ensure processed_img_np is defined from a previous step or use img_np
    # For grayscale, specify cmap='gray'
    if processed_img_np.ndim == 2:
        plt.imshow(processed_img_np, cmap='gray')
    else:
        plt.imshow(processed_img_np)
    plt.title("Processed Image (via NumPy array)")
    plt.axis('off')

    plt.tight_layout()
    plt.show()
    ```

- **6. Saving Processed Image (Optional)**
    - **Action:** Write the modified image to a file.
    - **Tool:** `pil_image_object.save('output_path.png')`
    ```python
    # processed_img_pil.save('processed_sample_image.png')
    # print("Processed image saved as 'processed_sample_image.png'")
    ```

## Important Considerations
- **Data Types:** Ensure image data remains in `uint8` format with values for most standard operations and saving, unless you are intentionally working with float representations (e.g., for intermediate calculations or normalized images). Clipping (`np.clip`) might be necessary after arithmetic operations.
- **Color Modes:** Be aware of the image mode (RGB, RGBA, L for grayscale). Operations might differ based on the mode. Pillow's `img.convert('L')` or `img.convert('RGB')` can be used for mode conversions.
- **Image Coordinates:** Matplotlib's `imshow` origin is typically top-left, which matches NumPy array indexing.
- **Libraries for Advanced Tasks:** For more complex image processing tasks (e.g., filtering, feature detection, segmentation), libraries like OpenCV (`cv2`), Scikit-image (`skimage`), and Mahotas are widely used.

This basic workflow provides a foundation for more advanced image processing and computer vision tasks.

---