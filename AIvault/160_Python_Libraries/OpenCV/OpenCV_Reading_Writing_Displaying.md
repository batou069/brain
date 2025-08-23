---
tags:
  - python
  - opencv
  - cv2
  - computer_vision
  - image_io
  - video_io
  - concept
  - example
aliases:
  - cv2.imread
  - cv2.imwrite
  - cv2.imshow
  - cv2.VideoCapture
related:
  - "[[160_Python_Libraries/OpenCV/_OpenCV_MOC|_OpenCV_MOC]]"
  - "[[_NumPy_MOC]]"
  - "[[_Matplotlib_MOC]]"
worksheet:
  - WS_ComputerVision_1
date_created: 2025-08-20
---
# OpenCV: Reading, Writing, and Displaying Images & Videos

The most basic operations in any computer vision workflow are getting image and video data into your program and displaying the results. OpenCV provides simple functions for these tasks.

## OpenCV and NumPy
A crucial point when using OpenCV with Python is that images are loaded as **[[_NumPy_MOC|NumPy arrays]]**.
-   A grayscale image is a 2D array of shape `(height, width)`.
-   A color image is a 3D array of shape `(height, width, channels)`.
-   **Important:** OpenCV loads color images in **BGR (Blue, Green, Red)** order by default, not the more common RGB order. This is a frequent source of confusion when displaying with other libraries like Matplotlib.

## Reading, Writing, and Displaying Images

[list2tab|#Image I/O]
- Reading an Image (`cv2.imread`)
    -   **Syntax:** `image = cv2.imread(filepath, flags)`
    -   `filepath`: Path to the image file.
    -   `flags`: Specifies the color type of the loaded image.
        -   `cv2.IMREAD_COLOR` (or `1`): Loads a color image. Any transparency is neglected. This is the default.
        -   `cv2.IMREAD_GRAYSCALE` (or `0`): Loads image in grayscale mode.
        -   `cv2.IMREAD_UNCHANGED` (or `-1`): Loads image as-is, including alpha (transparency) channel if present.
    -   **Returns:** A NumPy array, or `None` if the image cannot be read.
    -   **Example:**
        ```python
        import cv2
        # Load a color image
        img_bgr = cv2.imread('path/to/your/image.jpg', cv2.IMREAD_COLOR)
        if img_bgr is not None:
            print("Image loaded successfully.")
            print("Shape:", img_bgr.shape) # (height, width, 3)
            print("Data type:", img_bgr.dtype) # uint8
        else:
            print("Error: Could not read the image. Check the path.")
        ```
- Displaying an Image (`cv2.imshow`)
    -   **Syntax:** `cv2.imshow(window_name, image)`
    -   **Purpose:** Displays an image in a window. The window automatically fits to the image size. This function is part of OpenCV's HighGUI module and is intended for use in scripts, **not directly in Jupyter/Colab notebooks** (it can cause crashes). For notebooks, use Matplotlib.
    -   **Companion Functions:**
        -   `cv2.waitKey(delay)`: Waits for a key press for a specified number of milliseconds. If `0`, it waits indefinitely. **This is required to actually see the window created by `imshow`.**
        -   `cv2.destroyAllWindows()`: Closes all HighGUI windows.
    -   **Example (for a local Python script):**
        ```python
        import cv2
        img = cv2.imread('path/to/image.jpg')
        if img is not None:
            cv2.imshow('My Image Window', img)
            cv2.waitKey(0) # Wait for any key press
            cv2.destroyAllWindows()
        ```
- Displaying in Jupyter/Matplotlib
    -   Since `cv2.imshow` doesn't work well in notebooks, the standard practice is to use `matplotlib.pyplot.imshow`.
    -   **Remember to convert BGR to RGB!**
    -   **Example:**
        ```python
        import cv2
        import matplotlib.pyplot as plt

        img_bgr = cv2.imread('path/to/image.jpg')
        if img_bgr is not None:
            # Convert from BGR (OpenCV) to RGB (Matplotlib)
            img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
          
            plt.figure(figsize=(8, 6))
            plt.imshow(img_rgb)
            plt.title("Image Displayed with Matplotlib")
            plt.axis('off') # Hide axes
            plt.show()
        ```
- Writing an Image (`cv2.imwrite`)
    -   **Syntax:** `cv2.imwrite(filepath, image)`
    -   **Purpose:** Saves an image to a specified file. The image format is determined by the file extension (e.g., `.jpg`, `.png`).
    -   **Example:**
        ```python
        import cv2
        img = cv2.imread('path/to/image.jpg', cv2.IMREAD_GRAYSCALE)
        if img is not None:
            success = cv2.imwrite('output_grayscale_image.png', img)
            if success:
                print("Image saved successfully.")
            else:
                print("Failed to save image.")
        ```

## Reading and Processing Video
-   **`cv2.VideoCapture(source)`:**
    -   **Purpose:** Creates a video capture object to read from a video file or a camera.
    -   `source`: Can be the path to a video file or an integer for a camera index (e.g., `0` for the default camera).
-   **`cap.read()`:**
    -   **Purpose:** Reads the next frame from the video capture.
    -   **Returns:** A tuple `(ret, frame)`, where `ret` is a boolean (`True` if a frame was read successfully) and `frame` is the frame image (a NumPy array).
-   **`cap.release()`:**
    -   **Purpose:** Releases the video capture object and closes the file/camera.

**Example (Reading a video file frame by frame):**
```python
import cv2

cap = cv2.VideoCapture('path/to/your/video.mp4') # Or 0 for webcam

if not cap.isOpened():
    print("Error: Could not open video stream or file.")
else:
    frame_count = 0
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # if frame is read correctly, ret is True
        if not ret:
            print("Can't receive frame (end of stream?). Exiting ...")
            break
      
        frame_count += 1
        # Our operations on the frame come here
        # For example, convert to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame (in a script)
        cv2.imshow('Video Frame', gray_frame)
      
        # Press 'q' to exit the loop
        if cv2.waitKey(1) == ord('q'): # waitKey(1) gives a 1ms delay
            break
  
    print(f"Processed {frame_count} frames.")
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
```

These I/O functions are the entry and exit points for nearly all computer vision tasks performed with OpenCV.

---