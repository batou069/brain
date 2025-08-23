---
tags: [statistics, descriptive_statistics, summary_statistics, mean, median, mode, variance, standard_deviation, concept, scipy]
aliases: [Essential Statistics Features, Summary Statistics]
related:
  - "[[Descriptive_vs_Inferential_Statistics]]"
  - "[[Correlation_vs_Covariance]]"
  - "[[160_Python_Libraries/SciPy_Stats_Module|scipy.stats]]"
  - "[[_NumPy_MOC]]"
  - "[[_Pandas_MOC]]"
worksheet: [WS_StatsProb_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Essential Descriptive Statistics Features

Descriptive statistics are summary statistics that quantitatively describe or summarize features of a collection of information. They provide a simple way to understand the main characteristics of a dataset.

>[!question]- List essential statistics features you can get from a dataset that can help you better understand it. Are these numbers always helpful?
>
>Essential descriptive statistics can be grouped into measures of central tendency, variability, position, and shape.
>
>**Are these numbers always helpful?**
>Generally, yes, they are very helpful for an initial understanding. However, they can be misleading on their own, especially if the underlying distribution is not what you assume.
>-   The **mean** can be heavily skewed by outliers.
>-   A **standard deviation** of 0 indicates no spread, but a large standard deviation doesn't tell you *how* the data is spread (e.g., bimodal, skewed).
>-   Summary statistics can be nearly identical for vastly different distributions, as famously shown by **[[Anscombes_Quartet]]**.
>
>Therefore, descriptive statistics are most powerful when used in conjunction with **data visualization** (e.g., [[Histogram|histograms]], [[Box_Plot|box plots]]) to get a complete picture of the data.

## Key Descriptive Statistics

[list2tab|#Descriptive Measures]
- Measures of Central Tendency
    -   Describe the center or typical value of a dataset.
    -   **Mean (Average):** The sum of all values divided by the number of values. Sensitive to outliers.
    -   **Median:** The middle value of a dataset when it is sorted. If there's an even number of values, it's the average of the two middle values. Robust to outliers.
    -   **Mode:** The value that appears most frequently in a dataset. Can be used for categorical data. A dataset can have one mode (unimodal), two modes (bimodal), or more (multimodal).
- Measures of Variability (Dispersion or Spread)
    -   Describe how spread out the data points are.
    -   **Range:** The difference between the maximum and minimum values. Very sensitive to outliers.
    -   **Interquartile Range (IQR):** The range between the first quartile (25th percentile) and the third quartile (75th percentile): $IQR = Q3 - Q1$. It represents the spread of the middle 50% of the data and is robust to outliers.
    -   **Variance ($\sigma^2$ or $s^2$):** The average of the squared differences from the Mean. Measures how far a set of numbers is spread out from their average value.
    -   **Standard Deviation ($\sigma$ or $s$):** The square root of the variance. It's in the same units as the original data, making it more interpretable than variance.
- Measures of Position
    -   Describe the relative position of a specific data point within the dataset.
    -   **Percentiles:** A value below which a certain percentage of observations fall. The 50th percentile is the median.
    -   **Quartiles:** Specific percentiles that divide the data into four equal parts:
        -   Q1 (First Quartile): 25th percentile.
        -   Q2 (Second Quartile): 50th percentile (the Median).
        -   Q3 (Third Quartile): 75th percentile.
- Measures of Shape
    -   Describe the shape of the data's distribution.
    -   **Skewness:** Measures the asymmetry of the probability distribution.
        -   *Positive Skew (Right-skewed):* The tail on the right side is longer or fatter. Mean > Median > Mode.
        -   *Negative Skew (Left-skewed):* The tail on the left side is longer or fatter. Mean < Median < Mode.
        -   *Zero Skew:* Symmetrical distribution (like a normal distribution).
    -   **Kurtosis:** Measures the "tailedness" of the probability distribution. It describes how heavy the tails are and how sharp the peak is compared to a normal distribution.
        -   *Leptokurtic (Kurtosis > 3):* Heavy tails, sharp peak. More outliers than normal.
        -   *Mesokurtic (Kurtosis = 3):* Normal distribution tails and peak.
        -   *Platykurtic (Kurtosis < 3):* Light tails, flat peak. Fewer outliers than normal.
        -   (Note: Often "excess kurtosis" is reported, which is Kurtosis - 3).
- Measures of Association
    -   Describe the relationship between two or more variables.
    -   **[[Correlation_vs_Covariance|Covariance]]:** Measures the direction of the linear relationship.
    -   **[[Correlation_vs_Covariance|Correlation Coefficient]]:** Measures the strength and direction of the linear relationship (standardized, from -1 to 1).

## SciPy / NumPy / Pandas Example
These libraries provide easy ways to compute these statistics.

```python
import numpy as np
import pandas as pd
from scipy import stats

# Conceptual e-commerce data: prices of products in a category
product_prices = np.array([19.99, 25.00, 25.00, 29.99, 35.50, 42.00, 50.00, 55.00, 89.99, 250.00]) # Last one is an outlier

# Using NumPy
mean_np = np.mean(product_prices)
median_np = np.median(product_prices)
std_np = np.std(product_prices)
print("--- NumPy ---")
print(f"Mean: {mean_np:.2f}, Median: {median_np:.2f}, Std Dev: {std_np:.2f}")

# Using SciPy.stats
mode_scipy = stats.mode(product_prices, keepdims=False) # keepdims=False for newer scipy
skewness_scipy = stats.skew(product_prices)
kurtosis_scipy = stats.kurtosis(product_prices) # This is excess kurtosis (Kurtosis - 3)
print("\n--- SciPy.stats ---")
print(f"Mode: {mode_scipy.mode} (Count: {mode_scipy.count})")
print(f"Skewness: {skewness_scipy:.2f} (Positive/Right-skewed due to outlier)")
print(f"Excess Kurtosis: {kurtosis_scipy:.2f}")

# Using Pandas (often the most convenient for a quick summary)
prices_series = pd.Series(product_prices)
summary_pd = prices_series.describe()
print("\n--- Pandas describe() ---")
print(summary_pd)

# The .describe() method provides count, mean, std, min, 25% (Q1), 50% (Q2/Median), 75% (Q3), and max.
```
The output clearly shows how the mean (52.25) is pulled up by the outlier (250.00), while the median (38.75) is more representative of the "typical" price in the main group. This highlights the importance of looking at multiple statistics and not just the mean.

---