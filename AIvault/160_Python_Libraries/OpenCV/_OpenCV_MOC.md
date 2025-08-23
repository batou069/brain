---
tags:
  - python
  - library
  - opencv
  - cv2
  - computer_vision
  - image_processing
  - video_processing
  - moc
  - concept
aliases:
  - OpenCV MOC
  - cv2 MOC
  - Open Computer Vision Library MOC
related:
  - "[[_Python_Libraries_MOC]]"
  - "[[_NumPy_MOC]]"
  - "[[_Matplotlib_MOC]]"
  - "[[Scikit_image_Library]]"
  - "[[Pillow_PIL_MOC|Pillow (PIL)]]"
worksheet:
  - WS_ComputerVision_1
date_created: 2025-08-20
---
# OpenCV MOC 📸👁️

**OpenCV (Open Source Computer Vision Library)** is a highly popular and comprehensive open-source library for computer vision, machine learning, and image processing. It has a vast number of optimized algorithms for real-time computer vision.

The Python binding for OpenCV is commonly imported as `cv2`.

## Core Philosophy & Features
-   **Performance:** Many of its algorithms are written in optimized C/C++, making it very fast for real-time applications.
-   **Comprehensive Functionality:** Provides a huge range of functions covering many areas of computer vision, from basic image processing to advanced techniques like object detection and feature recognition.
-   **Cross-Platform:** Runs on Windows, Linux, macOS, Android, and iOS.
-   **NumPy Integration:** In Python, OpenCV images are represented as [[_NumPy_MOC|NumPy arrays]], making it seamless to use NumPy for manipulation and to integrate with other scientific Python libraries like SciPy, Matplotlib, and Scikit-learn.
-   **Hardware Acceleration:** Can leverage GPU acceleration for some operations.
-   **Real-time Focus:** Many functions are optimized for processing video streams from cameras.

## Key Modules & Functionality Areas
-   [[OpenCV_Reading_Writing_Displaying|Reading, Writing, and Displaying Images & Videos]]
    -   `cv2.imread()`, `cv2.imwrite()`, `cv2.imshow()`, `cv2.VideoCapture()`.
-   [[OpenCV_Basic_Image_Processing|Basic Image Processing]]
    -   Color space conversions (e.g., BGR to Grayscale, BGR to HSV).
    -   Geometric transformations (scaling, rotation, translation, affine/perspective transforms).
    -   Thresholding (simple, adaptive, Otsu's).
    -   Image filtering and blurring (averaging, Gaussian, median, bilateral).
    -   Morphological transformations (erosion, dilation, opening, closing).
-   [[OpenCV_Image_Analysis|Image Analysis & Feature Detection]]
    -   Edge detection (Canny, Sobel, Laplacian).
    -   Contour detection and analysis.
    -   Histograms.
    -   Hough transforms (for detecting lines and circles).
    -   Feature detectors and descriptors (SIFT, SURF, ORB, FAST, BRIEF).
-   [[OpenCV_Video_Analysis|Video Analysis]]
    -   Reading from video files and camera streams.
    -   Background subtraction.
    -   Object tracking (e.g., MeanShift, CamShift, optical flow).
-   [[OpenCV_Object_Detection|Object Detection]]
    -   Haar cascades (for face and object detection).
    -   Integration with deep learning models (DNN module) for running pre-trained object detectors like YOLO, SSD, Faster R-CNN.
-   **Computational Photography**
    -   Image stitching, high dynamic range (HDR) imaging.
-   **Machine Learning (`cv2.ml`)**
    -   Includes implementations of some classic ML algorithms like K-Means, Support Vector Machines (SVM), Decision Trees, etc., though [[160_Python_Libraries/Scikit_learn/_Scikit_learn_MOC|Scikit-learn]] is often preferred for general ML tasks in Python.

## Notes in this OpenCV Section
```dataview
LIST
FROM "160_Python_Libraries/OpenCV"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
```

---