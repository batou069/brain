---
tags:
  - python
  - library
  - hyperspy
  - microscopy
  - spectroscopy
  - multidimensional_data
  - data_analysis
  - concept
aliases:
  - HyperSpy
related:
  - "[[_Python_Libraries_MOC]]"
  - "[[_NumPy_MOC]]"
  - "[[_Matplotlib_MOC]]"
  - "[[SciPy_Library]]"
  - "[[_Pandas_MOC]]"
worksheet:
  - WS_Python_Packages_1
date_created: 2025-06-01
---
# HyperSpy Library

## Overview
**HyperSpy** is an open-source Python library for **interactive data analysis of multi-dimensional arrays**, with a particular focus on signals originating from electron microscopy and other similar experimental techniques (e.g., X-ray spectroscopy, scanning probe microscopy). It aims to provide a comprehensive platform for analyzing "hyperspectral" data, where each point in a 1D, 2D, or 3D spatial map has an associated spectrum or image.

HyperSpy provides specialized `Signal` classes that extend [[_NumPy_MOC|NumPy]] arrays with rich metadata (axis information, units, experimental parameters) and a suite of domain-specific analysis tools.

## Key Features and Functionality
[list2tab|#HyperSpy Features]
- **Signal Model:**
    - `Signal1D`: For spectral data (e.g., EELS, EDX spectra) where each point in a navigation space (0D, 1D, or 2D) has an associated 1D spectrum.
    - `Signal2D`: For image data (e.g., image stacks, diffraction patterns) where each point in a navigation space has an associated 2D image.
    - Rich metadata handling for axes (name, units, scale, offset), signal type, experimental conditions.
- **Data Input/Output:**
    - Supports reading a wide variety of common microscopy and spectroscopy file formats (e.g., DM3/DM4, GSF, Bruker, EDAX, HDF5, TIFF stacks).
    - `hs.load()` function for loading data.
- **Data Visualization:**
    - Interactive plotting capabilities built on [[_Matplotlib_MOC|Matplotlib]].
    - Easy visualization of spectra, images, and map data.
    - Navigators for exploring multi-dimensional datasets.
    - Example: `signal.plot()` for spectra/images, `signal_map.plot()` for map data.
- **Signal Processing:**
    - Common operations: cropping, rebinning, filtering (Gaussian, median), alignment, background subtraction.
    - `signal.align1D()`, `signal.remove_background()`.
- **Decomposition and Blind Source Separation (BSS):**
    - Powerful tools for decomposing hyperspectral datasets into constituent components and their corresponding abundance maps.
    - Principal Component Analysis (PCA): `signal.decomposition()`
    - Non-negative Matrix Factorization (NMF): `signal.decomposition(algorithm='nmf')`
    - Independent Component Analysis (ICA), Vertex Component Analysis (VCA).
- **Model Fitting and Curve Fitting:**
    - Fitting various theoretical models (Gaussians, Lorentzians, power laws, etc.) to spectral features.
    - `signal.fit_gaussian()`, `signal.fit_lorentzian()`.
    - General model creation and fitting framework: `hs.model.components`, `m.fit()`.
- **Quantitative Analysis:**
    - Tools for elemental quantification in EELS and EDX spectroscopy.
    - Peak finding, integration.
- **Machine Learning Integration:**
    - Can be used for preprocessing data for machine learning or applying ML techniques to extracted features.
- **Lazy Evaluation and Big Data:**
    - Can operate in "lazy" mode, where computations are only performed when results are needed, allowing analysis of datasets larger than available RAM. This is often facilitated by Dask integration.
- **Extensibility:**
    - Designed to be extensible with custom plugins and functions.

## Example Usage (Conceptual - actual data files needed)

### Loading and Basic Plotting (Conceptual)
```python
import hyperspy.api as hs
import numpy as np # For creating dummy data if needed

# Load a hyperspectral dataset (e.g., a spectrum image)
# This requires a real data file in a supported format.
# For demonstration, we might create a dummy Signal object.
# try:
#     s = hs.load("path/to/your/hyperspectral_data.dm3") # Example for a DM3 file
# except (FileNotFoundError, IOError):
#     print("Data file not found or dummy data used.")
#     # Create a dummy 2D Signal with 1D navigation (a line scan of spectra)
#     data_dummy = np.random.rand(50, 1024) # 50 spectra, each 1024 channels long
#     s_dummy = hs.signals.Signal1D(data_dummy)
#     s_dummy.axes_manager[0].name = 'Position'
#     s_dummy.axes_manager[0].scale = 0.1
#     s_dummy.axes_manager[0].units = 'nm'
#     s_dummy.axes_manager[1].name = 'Energy'
#     s_dummy.axes_manager[1].scale = 0.5
#     s_dummy.axes_manager[1].offset = 100
#     s_dummy.axes_manager[1].units = 'eV'
#     s = s_dummy

# Basic plotting
# if s is not None:
#     s.plot() # Interactive plot depending on signal type
    # For a Signal1D that is a map of spectra:
    # s.plot() might show an image of the map, and clicking a pixel shows the spectrum.
    # Or, if it's a single spectrum:
    # hs.signals.Signal1D(np.random.rand(100)).plot()

# Accessing data as NumPy array
# numpy_data = s.data
# print("Shape of data:", numpy_data.shape)
```

### Decomposition (e.g., PCA)
```python
# Assuming 's' is a loaded hyperspectral Signal (e.g., spectrum image)
# if s is not None and hasattr(s, 'decomposition'):
#     try:
#         s.decomposition(algorithm="pca", n_components=5, centre='mean') # Perform PCA
        # This adds 'PCA_loadings' and 'PCA_scores' to s.learning_results
        # loadings = s.get_decomposition_loadings()
        # scores = s.get_decomposition_factors() # Note: factors are often called scores in PCA context
        # loadings.plot() # Plot PCA loadings (eigenvectors/eigenspectra)
        # scores.plot()   # Plot PCA scores (component maps)
#     except Exception as e:
#         print(f"Decomposition example error (likely needs real data): {e}")
```

### Model Fitting (e.g., Gaussian to a peak)
```python
# Assuming 'spec' is a 1D Signal (a single spectrum) with a peak
# For example, take a spectrum from the hyperspectral data 's'
# if s is not None and s.axes_manager.navigation_dimension == 2: # If it's a map
#    spec = s.inav[s.axes_manager.navigation_shape[0]//2, s.axes_manager.navigation_shape[1]//2]
# elif s is not None and s.axes_manager.navigation_dimension == 0 and s.axes_manager.signal_dimension == 1:
#    spec = s # If s is already a single spectrum
# else:
#    spec = None

# if spec is not None:
#     try:
#         # Create a Gaussian component model
#         g = hs.model.components.Gaussian()
#         # Add it to the spectrum's model
#         spec.model.append(g)
        # Initial guess for parameters (center, sigma, amplitude) might be needed
        # g.centre.value = 500 # Example center
        # g.sigma.value = 10  # Example sigma
        # g.A.value = np.max(spec.data) # Example amplitude
        # Fit the model
        # spec.model.fit()
        # spec.plot() # Plot spectrum with the fitted model
        # print(g) # Print fitted parameters
#     except Exception as e:
#         print(f"Model fitting example error (likely needs real data/peak): {e}")
```

## Common Applications
- **Electron Microscopy:**
    - **EELS (Electron Energy Loss Spectroscopy):** Analyzing core-loss edges for elemental mapping, fine structure for chemical bonding information.
    - **EDX/EDS (Energy-Dispersive X-ray Spectroscopy):** Elemental composition mapping.
    - **STEM (Scanning Transmission Electron Microscopy) Imaging:** Analyzing image series, diffraction patterns.
- **X-ray Spectroscopy:** Analyzing XRF (X-ray Fluorescence) maps, XPS (X-ray Photoelectron Spectroscopy) data.
- **Scanning Probe Microscopy (SPM):** Analyzing force curves, tunneling spectra from AFM/STM.
- **Any field generating multi-dimensional datasets where each spatial point has an associated spectrum or image series.** This includes some forms of medical imaging, astronomical data, and materials science characterization.

HyperSpy provides a powerful, unified environment for these types of complex data analyses, combining data handling, processing, visualization, and modeling within a single Python framework. Its strength lies in handling the associated metadata correctly and providing domain-specific tools.

---