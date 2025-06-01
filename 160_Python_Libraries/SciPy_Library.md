---
tags:
  - python
  - library
  - scipy
  - scientific_computing
  - optimization
  - statistics
  - signal_processing
  - concept
aliases:
  - SciPy
related:
  - "[[_Python_Libraries_MOC]]"
  - "[[_NumPy_MOC]]"
  - "[[Calculus_Optimization]]"
  - "[[Linear_Algebra]]"
  - "[[Fourier_Series_Transforms]]"
  - "[[Probability_Distribution]]"
worksheet:
  - WS_Python_Packages_1
date_created: 2025-06-01
---
# SciPy Library

## Overview
**SciPy** (Scientific Python) is an open-source Python library used for scientific and technical computing. It builds on the [[_NumPy_MOC|NumPy]] library (providing efficient array operations) and provides a large number of higher-level functions and algorithms for various scientific domains.

SciPy is organized into sub-packages covering different scientific computing domains. It aims to provide functionality comparable to commercial packages like MATLAB, GNU Octave, or Scilab.

## Key Sub-packages and Functionality
[list2tab|#SciPy Modules]
- **`scipy.cluster` (Clustering algorithms)**
    - Vector quantization / K-means (`scipy.cluster.vq`)
    - Hierarchical clustering (`scipy.cluster.hierarchy`)
    - Example:
      ```python
      from scipy.cluster.vq import kmeans, vq
      import numpy as np
      # Sample data points
      data = np.array([[1.9, 2.3], [1.5, 2.5], [0.8, 0.6],
                       [0.4, 1.8], [0.1, 0.1], [0.2, 1.8],
                       [1.0, 1.0], [2.5, 2.8], [2.1, 2.0]])
      # Compute K-Means with K=2 (2 clusters)
      centroids, _ = kmeans(data, 2)
      # Assign each observation to a centroid
      idx, _ = vq(data, centroids)
      # print("Data points:\n", data)
      # print("Centroids:\n", centroids)
      # print("Cluster assignments:", idx)
      ```
- **`scipy.constants` (Physical and mathematical constants)**
    - Provides values like pi, speed of light, Planck constant, etc.
    - Example:
      ```python
      from scipy import constants
      # print(f"Pi: {constants.pi}")
      # print(f"Speed of light (m/s): {constants.c}")
      # print(f"Golden ratio: {constants.golden_ratio}")
      ```
- **`scipy.fft` or `scipy.fftpack` (Fourier Transforms)**
    - Fast Fourier Transforms (FFT), inverse FFT, etc. Used for signal processing and analyzing frequency components.
    - Example:
      ```python
      from scipy.fft import fft, ifft
      import numpy as np
      # Create a sample signal
      x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])
      y = fft(x)
      # print("Original signal:", x)
      # print("FFT of signal:", y)
      # y_inv = ifft(y)
      # print("Inverse FFT:", y_inv.real) # Should be close to original x
      ```
- **`scipy.integrate` (Integration routines)**
    - Numerical integration (quadrature), solving ordinary differential equations (ODEs).
    - Example (numerical integration):
      ```python
      from scipy.integrate import quad
      # Define a function to integrate, e.g., f(x) = x^2
      def integrand(x):
          return x**2
      # Integrate f(x) from 0 to 1
      result, error = quad(integrand, 0, 1)
      # print(f"Integral of x^2 from 0 to 1: {result} (Error: {error:.2e})") # Expected: 1/3
      ```
    - Example (solving ODE $y' = -2y$ with $y(0)=1$):
      ```python
      from scipy.integrate import solve_ivp
      import numpy as np
      # Define the ODE dy/dt = -2*y
      def ode_func(t, y):
          return -2 * y
      # Initial condition
      y0 = [1.0]
      # Time span for solution
      t_span = [0, 5]
      t_eval = np.linspace(t_span[0], t_span[1], 100) # Points to evaluate solution
      sol = solve_ivp(ode_func, t_span, y0, t_eval=t_eval)
      # print("Time points:", sol.t[:5])
      # print("Solution y(t):", sol.y[0][:5]) # y(t) = exp(-2t)
      ```
- **`scipy.interpolate` (Interpolation)**
    - Tools for interpolating data (e.g., linear, cubic spline interpolation).
    - Example:
      ```python
      from scipy.interpolate import interp1d
      import numpy as np
      x_known = np.array([0, 1, 2, 3, 4, 5])
      y_known = np.array([0, 0.8, 0.9, 0.1, -0.8, -1.0])
      # Create an interpolation function (linear by default)
      f_linear = interp1d(x_known, y_known)
      # Create a cubic spline interpolation function
      f_cubic = interp1d(x_known, y_known, kind='cubic')
      x_new = np.linspace(0, 5, 50)
      # y_linear_interp = f_linear(x_new)
      # y_cubic_interp = f_cubic(x_new)
      # import matplotlib.pyplot as plt
      # plt.plot(x_known, y_known, 'o', label='Data')
      # plt.plot(x_new, y_linear_interp, '-', label='Linear Interp')
      # plt.plot(x_new, y_cubic_interp, '--', label='Cubic Interp')
      # plt.legend(); plt.show()
      ```- **`scipy.io` (Data input and output)**
    - Reading and writing various file formats like MATLAB files (`.mat`), NetCDF, etc.
    - Example (MATLAB files):
      ```python
      from scipy.io import savemat, loadmat
      import numpy as np
      # a = np.arange(20)
      # savemat('matlab_array.mat', {'my_array': a})
      # data_loaded = loadmat('matlab_array.mat')
      # loaded_array = data_loaded['my_array']
      # print(loaded_array)
      ```
- **`scipy.linalg` (Linear algebra routines)**
    - Extends `numpy.linalg` with more advanced functions like matrix decompositions (Cholesky, LU, QR, SVD), solvers for linear systems, matrix functions (exponential, logarithm, square root).
    - Example (Solving linear system $Ax=b$):
      ```python
      from scipy.linalg import solve
      import numpy as np
      A = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]])
      b = np.array([2, 4, -1])
      x_solution = solve(A, b)
      # print("Solution x:", x_solution)
      # print("Check A @ x_solution:", A @ x_solution) # Should be close to b
      ```
- **`scipy.ndimage` (N-dimensional image processing)**
    - Functions for multi-dimensional image filtering, morphological operations, interpolation, measurements.
    - Example (Gaussian filter on an image):
      ```python
      from scipy import ndimage
      import numpy as np
      # import matplotlib.pyplot as plt
      # try:
      #     from skimage import data # Using scikit-image for sample image
      #     face = data.camera() # Example image
      # except ImportError:
      #     face = np.random.rand(100,100) * 255 # Dummy image if skimage not available
      # blurred_face = ndimage.gaussian_filter(face, sigma=3)
      # plt.figure(figsize=(8,4))
      # plt.subplot(121); plt.imshow(face, cmap='gray'); plt.title('Original')
      # plt.subplot(122); plt.imshow(blurred_face, cmap='gray'); plt.title('Gaussian Filtered')
      # plt.show()
      ```
- **`scipy.optimize` (Optimization algorithms)**
    - Function minimization (scalar or multivariate), curve fitting, root finding.
    - Example (Minimizing a scalar function):
      ```python
      from scipy.optimize import minimize
      # Define a function to minimize, e.g., Rosenbrock function
      def rosen(x):
          return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)
      x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2]) # Initial guess
      res = minimize(rosen, x0, method='nelder-mead', options={'xatol': 1e-8, 'disp': False})
      # print("Minimization result:\n", res)
      # print("Found minimum at x =", res.x)
      ```
- **`scipy.signal` (Signal processing tools)**
    - Filtering, convolution, spectral analysis, waveform generation, B-splines.
    - Example (Applying a median filter to a noisy signal):
      ```python
      from scipy import signal
      import numpy as np
      # import matplotlib.pyplot as plt
      # # Generate a noisy signal
      # t = np.linspace(0, 1.0, 2001)
      # x_low = np.sin(2 * np.pi * 5 * t)
      # x_high = np.sin(2 * np.pi * 250 * t)
      # x = x_low + x_high * 0.2 + np.random.randn(len(t)) * 0.1
      # # Apply a median filter
      # x_filtered = signal.medfilt(x, kernel_size=21)
      # plt.figure(figsize=(10,4))
      # plt.plot(t, x, label='Noisy signal')
      # plt.plot(t, x_filtered, label='Filtered signal (median)', linewidth=2)
      # plt.legend(); plt.ylim([-2,2]); plt.show()
      ```
- **`scipy.sparse` (Sparse matrices and associated routines)**
    - Efficient storage and computation for matrices with many zero elements. Includes sparse linear algebra routines in `scipy.sparse.linalg`.
    - Example:
      ```python
      from scipy.sparse import csr_matrix
      import numpy as np
      # Create a dense array with many zeros
      dense_array = np.array([[0, 0, 1, 0, 2],
                              [0, 0, 0, 3, 0],
                              [4, 0, 0, 0, 0]])
      # Convert to Compressed Sparse Row (CSR) format
      sparse_csr = csr_matrix(dense_array)
      # print("Dense array:\n", dense_array)
      # print("\nCSR sparse matrix:\n", sparse_csr)
      # print("\nData:", sparse_csr.data)
      # print("Indices:", sparse_csr.indices)
      # print("Indptr:", sparse_csr.indptr)
      ```
- **`scipy.spatial` (Spatial data structures and algorithms)**
    - KD-trees, Delaunay triangulation, Voronoi diagrams, convex hulls, distance computations.
    - Example (Finding nearest neighbors using KDTree):
      ```python
      from scipy.spatial import KDTree
      import numpy as np
      points = np.array([[0,0], [0,1], [1,0], [1,1], [0.6, 0.6]])
      tree = KDTree(points)
      # Query for the 2 nearest neighbors of point [0.5, 0.5]
      distances, indices = tree.query([0.5, 0.5], k=2)
      # print("Points:\n", points)
      # print("Query point: [0.5, 0.5]")
      # print("Distances to nearest neighbors:", distances)
      # print("Indices of nearest neighbors:", indices)
      # print("Nearest points:\n", points[indices])
      ```
- **`scipy.stats` (Statistical functions)**
    - A very large module with probability distributions (continuous and discrete), statistical tests, descriptive statistics, correlation functions.
    - Example (Working with a normal distribution):
      ```python
      from scipy.stats import norm
      # Generate random numbers from a normal distribution with mean=0, std=1
      random_samples = norm.rvs(loc=0, scale=1, size=5)
      # print("Random samples from N(0,1):", random_samples)
      # Calculate PDF (Probability Density Function) at x=0
      pdf_at_0 = norm.pdf(0, loc=0, scale=1)
      # print("PDF at x=0 for N(0,1):", pdf_at_0)
      # Calculate CDF (Cumulative Distribution Function) at x=0
      cdf_at_0 = norm.cdf(0, loc=0, scale=1)
      # print("CDF at x=0 for N(0,1):", cdf_at_0) # Should be 0.5
      # Perform a t-test (example)
      # from scipy.stats import ttest_ind
      # group1 = norm.rvs(loc=0, scale=1, size=30)
      # group2 = norm.rvs(loc=0.5, scale=1, size=30) # Slightly different mean
      # t_stat, p_value = ttest_ind(group1, group2)
      # print(f"T-test: t-statistic={t_stat:.2f}, p-value={p_value:.3f}")
      ```

## Common Applications
- Numerical analysis and algorithm development.
- Data analysis and statistical modeling.
- Signal and image processing.
- [[Calculus_Optimization|Optimization]] of complex functions.
- Solving differential equations that model physical systems.
- Scientific research across various disciplines (physics, engineering, biology, finance, etc.).

SciPy provides the building blocks for many higher-level scientific applications and is a cornerstone of the scientific Python ecosystem.

---