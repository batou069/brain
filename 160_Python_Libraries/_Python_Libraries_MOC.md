---
tags:
  - python
  - libraries
  - moc
  - data_science
  - scientific_computing
aliases:
  - Python Packages MOC
related:
  - "[[_Data_Science_AI_MOC]]"
  - "[[_NumPy_MOC]]"
  - "[[_Pandas_MOC]]"
  - "[[_Matplotlib_MOC]]"
worksheet:
  - WS_Python_Packages_1
date_created: 2025-06-01
---
# Python Libraries MOC 🐍

This section provides an overview of various Python libraries commonly used in scientific computing, data science, machine learning, and specialized domains. These libraries extend Python's capabilities, offering optimized functions and tools for complex tasks.

## Core Scientific Python Stack (Foundational)
Many libraries build upon or integrate with this core stack:


## Extended Scientific & Data Science Libraries
[list2tab]
- Core Scientific
	[list2card|addClass(ab-col2)|#Python Libraries Overview]
	-   🔢 **[[140_Data_Science_AI/NumPy/_NumPy_MOC|NumPy]]**
		- Fundamental package for numerical computation, n-dimensional arrays.
	-   🐼 **[[140_Data_Science_AI/Pandas/_Pandas_MOC|Pandas]]**
		- High-performance data structures (DataFrame) and data analysis tools.
	-   🎨 **[[140_Data_Science_AI/Matplotlib/_Matplotlib_MOC|Matplotlib]]**
		- Comprehensive library for static, animated, and interactive visualizations.
	-   🖼️ **[[140_Data_Science_AI/Pillow_PIL/_Pillow_PIL_MOC|Pillow (PIL Fork)]]**
		- Image processing library (opening, manipulating, saving image files).
- Extended Scientific
	[list2card|addClass(ab-col3)|#Python Libraries Overview]
	- **🧪 [[SciPy_Library|SciPy]]**
	  - **Focus:** Fundamental algorithms for scientific computing.
	  - **Keywords:** Optimization, integration, statistics, signal processing, linear algebra.
	- **📊 [[Statsmodels_Library|Statsmodels]]**
	  - **Focus:** Statistical modeling, tests, and econometrics.
	  - **Keywords:** Regression, time series, ANOVA, GLM.
	- **🤖 [[Scikit_learn_Library|Scikit-learn]]** (Often in ML sections)
	  - **Focus:** Machine learning algorithms and tools.
	  - **Keywords:** Classification, regression, clustering, model selection.
	- **📸 [[Scikit_image_Library|Scikit-image]]**
	  - **Focus:** Image processing algorithms.
	  - **Keywords:** Filtering, segmentation, feature detection, morphology.
	- **🌊 [[PyWavelets_Library|PyWavelets]]**
	  - **Focus:** Wavelet transforms.
	  - **Keywords:** DWT, CWT, signal denoising, image compression.
	- **🔬 [[Hyperspy_Library|HyperSpy]]**
	  - **Focus:** Analysis of multi-dimensional data arrays (e.g., microscopy, spectroscopy).
	  - **Keywords:** Hyperspectral data, EELS, EDX, decomposition.
	- **🕸️ [[Graph_tool_Library|Graph-tool]]**
	  - **Focus:** High-performance network/graph analysis and visualization.
	  - **Keywords:** Graph theory, centrality, community detection, SBM.
	- **🧠 [[PsychoPy_Library|PsychoPy]]** (To be created)
	  - **Focus:** Experiment creation for neuroscience and psychology.
	  - **Keywords:** Psychophysics, stimulus presentation, response collection.
	- **🌌 [[Astropy_Library|Astropy]]** (To be created)
	  - **Focus:** Tools for astronomy and astrophysics.
	  - **Keywords:** Coordinates, FITS files, cosmology, WCS.
	- **(Other libraries like TensorFlow, PyTorch, Keras, NLTK, SpaCy, etc., might be covered in more specialized AI/ML sections)**

## Notes in this Section
```dataview
LIST
FROM "160_Python_Libraries"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
```
---