---
tags:
  - python
  - library
  - pywavelets
  - wavelet_transform
  - signal_processing
  - image_processing
  - concept
aliases:
  - PyWavelets
  - Wavelet Analysis Python
related:
  - "[[_Python_Libraries_MOC]]"
  - "[[_NumPy_MOC]]"
  - "[[SciPy_Library]]"
  - "[[Fourier_Series_Transforms]]"
worksheet:
  - WS_Python_Packages_1
date_created: 2025-06-01
---
# PyWavelets Library

## Overview
**PyWavelets** is an open-source Python library for **wavelet transforms**. Wavelets are mathematical functions that cut up data into different frequency components, and then study each component with a resolution matched to its scale. They are particularly useful for analyzing signals or images where features occur at different scales or are localized in time or space, a capability that the traditional [[Fourier_Series_Transforms|Fourier Transform]] lacks (as FFT provides frequency information but loses time localization).

PyWavelets provides easy-to-use implementations of various wavelet families and transform types.

## Key Features and Functionality
[list2tab|#PyWavelets Features]
- **Wavelet Families:**
    - Supports a wide range of wavelet families, including:
        - Haar (`haar`)
        - Daubechies (`db1` to `db38`)
        - Symlets (`sym2` to `sym20`)
        - Coiflets (`coif1` to `coif17`)
        - Biorthogonal (`bior1.1` to `bior6.8`)
        - Reverse Biorthogonal (`rbio1.1` to `rbio6.8`)
        - Meyer (`dmey`)
        - Gaussian (`gaus1` to `gaus8`)
        - Mexican Hat (`mexh`)
        - Morlet (`morl`)
        - Complex Gaussian (`cgau1` to `cgau8`)
        - Shannon (`shan`)
        - Frequency B-Spline (`fbsp`)
        - Complex Morlet (`cmor`)
    - You can list available wavelets: `pywt.wavelist(kind='discrete')` or `pywt.wavelist(kind='continuous')`.
- **Transform Types:**
    - **Discrete Wavelet Transform (DWT):** `pywt.dwt()` (single level), `pywt.wavedec()` (multilevel decomposition).
        - Decomposes a signal into approximation (low-frequency) and detail (high-frequency) coefficients.
    - **Inverse Discrete Wavelet Transform (IDWT):** `pywt.idwt()` (single level), `pywt.waverec()` (multilevel reconstruction).
        - Reconstructs the signal from its DWT coefficients.
    - **Stationary Wavelet Transform (SWT) / Undecimated DWT:** `pywt.swt()`.
        - Translation-invariant, produces coefficients of the same length as the input at each level.
    - **Continuous Wavelet Transform (CWT):** `pywt.cwt()`.
        - Provides a time-frequency representation of a signal. More computationally intensive.
    - **2D DWT and IDWT:** `pywt.dwt2()`, `pywt.idwt2()`, `pywt.wavedec2()`, `pywt.waverec2()`.
        - For image processing. Decomposes an image into LL (approximation), LH (horizontal detail), HL (vertical detail), and HH (diagonal detail) subbands.
- **Coefficient Manipulation:**
    - Thresholding functions for denoising (e.g., `pywt.threshold()`).
    - Accessing and modifying approximation and detail coefficients.
- **Other Utilities:**
    - Wavelet packet transforms (`pywt.WaveletPacket`, `pywt.WaveletPacket2D`).
    - Calculating energy of coefficients.
    - Visualizing wavelets and scaling functions.

## Example Usage

### 1D Discrete Wavelet Transform (DWT) and Reconstruction
```python
import pywt
import numpy as np
# import matplotlib.pyplot as plt

# Sample 1D signal
signal = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
wavelet_name = 'db4' # Daubechies 4 wavelet

# Single level DWT
coeffs = pywt.dwt(signal, wavelet=wavelet_name)
cA, cD = coeffs # Approximation and Detail coefficients
# print(f"Wavelet: {wavelet_name}")
# print("Original signal length:", len(signal))
# print("Approximation coeffs (cA) length:", len(cA))
# print("Detail coeffs (cD) length:", len(cD))
# print("cA:", cA)
# print("cD:", cD)

# Single level IDWT (reconstruction)
reconstructed_signal = pywt.idwt(cA, cD, wavelet=wavelet_name)
# print("Reconstructed signal:", reconstructed_signal)
# print("Reconstruction close to original:", np.allclose(signal, reconstructed_signal[:len(signal)])) # May need slicing due to padding

# Multilevel DWT (e.g., 3 levels)
coeffs_multilevel = pywt.wavedec(signal, wavelet=wavelet_name, level=3)
cA3, cD3, cD2, cD1 = coeffs_multilevel # cA3 is the approx at level 3, cD3, cD2, cD1 are details
# print("\nMultilevel Decomposition (3 levels):")
# print("cA3 length:", len(cA3))
# print("cD3 length:", len(cD3))
# print("cD2 length:", len(cD2))
# print("cD1 length:", len(cD1))

# Multilevel IDWT
reconstructed_multilevel = pywt.waverec(coeffs_multilevel, wavelet=wavelet_name)
# print("\nReconstructed from multilevel:", reconstructed_multilevel)
# print("Multilevel reconstruction close:", np.allclose(signal, reconstructed_multilevel[:len(signal)]))
```

### 2D Discrete Wavelet Transform (DWT) for Images
```python
import pywt
import numpy as np
# import matplotlib.pyplot as plt
# from skimage import data, color # Using scikit-image for sample image

# try:
#     image_rgb = data.astronaut()
#     image_gray = color.rgb2gray(image_rgb)
# except ImportError:
#     # Create a dummy grayscale image if skimage is not available
#     image_gray = np.random.rand(128, 128)
# except AttributeError: # If data.astronaut() is not found
#     image_gray = np.random.rand(128, 128)


# wavelet_name_2d = 'haar' # Haar wavelet is simple for visualization

# Single level 2D DWT
# coeffs2d = pywt.dwt2(image_gray, wavelet=wavelet_name_2d)
# cA_2d, (cH_2d, cV_2d, cD_2d) = coeffs2d
# LL (Approximation), LH (Horizontal), HL (Vertical), HH (Diagonal)

# Visualize the decomposition (requires matplotlib)
# fig, axes = plt.subplots(2, 2, figsize=(8, 8))
# axes[0, 0].imshow(cA_2d, cmap='gray'); axes[0, 0].set_title('Approximation (LL)')
# axes[0, 1].imshow(cH_2d, cmap='gray'); axes[0, 1].set_title('Horizontal Detail (LH)')
# axes[1, 0].imshow(cV_2d, cmap='gray'); axes[1, 0].set_title('Vertical Detail (HL)')
# axes[1, 1].imshow(cD_2d, cmap='gray'); axes[1, 1].set_title('Diagonal Detail (HH)')
# for ax_row in axes:
#     for ax in ax_row:
#         ax.axis('off')
# plt.suptitle(f"2D DWT with '{wavelet_name_2d}' wavelet", fontsize=14)
# plt.tight_layout(rect=[0, 0, 1, 0.96]); plt.show()
```

### Denoising Example (Conceptual)
```python
import pywt
import numpy as np
# import matplotlib.pyplot as plt

# Create a noisy signal
# t = np.linspace(0, 1, 256, endpoint=False)
# clean_signal = np.sin(2 * np.pi * 7 * t) + np.sin(2 * np.pi * 15 * t)
# noise = 0.5 * np.random.randn(len(clean_signal))
# noisy_signal = clean_signal + noise

# Decompose
# wavelet = 'sym8'
# level = 4
# coeffs = pywt.wavedec(noisy_signal, wavelet, level=level)

# Threshold detail coefficients
# sigma = np.median(np.abs(coeffs[-1])) / 0.6745 # Estimate noise std from finest detail
# threshold_value = sigma * np.sqrt(2 * np.log(len(noisy_signal))) # Universal threshold

# thresholded_coeffs = [coeffs[0]] # Keep approximation coeffs
# for i in range(1, len(coeffs)):
#     thresholded_coeffs.append(pywt.threshold(coeffs[i], value=threshold_value, mode='soft'))

# Reconstruct
# denoised_signal = pywt.waverec(thresholded_coeffs, wavelet)

# Plotting (requires matplotlib)
# plt.figure(figsize=(12, 6))
# plt.plot(t, noisy_signal, label='Noisy Signal', alpha=0.7)
# plt.plot(t, denoised_signal, label='Denoised Signal (Wavelet)', linewidth=1.5)
# plt.plot(t, clean_signal, label='Original Clean Signal', linestyle='--', color='gray')
# plt.legend(); plt.title("Wavelet Denoising Example"); plt.show()
```

## Common Applications
- **Signal Denoising:** One of the most common applications. By transforming the signal into the wavelet domain, noise (often high-frequency) can be separated from the signal and removed or reduced by thresholding detail coefficients.
- **Image Compression (e.g., JPEG 2000):** Wavelet transforms are used in image compression standards because they can efficiently represent image features at different scales.
- **Feature Extraction:** Wavelet coefficients can serve as features for classification or regression tasks in machine learning, especially for signals and images.
- **Time-Frequency Analysis:** Analyzing signals whose frequency content changes over time (non-stationary signals), e.g., biomedical signals (ECG, EEG), audio signals, financial time series. CWT is particularly good for this.
- **Image Fusion:** Combining information from multiple images.
- **Edge Detection in Images:** Detail coefficients highlight edges and textures.
- **Numerical Analysis:** Solving partial differential equations.

PyWavelets is a powerful tool for anyone working with signals or images who needs to analyze or process data in the time-frequency or time-scale domain.

---