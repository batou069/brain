---
tags:
  - time_series
  - granger_causality
  - causality
  - multivariate
  - statistics
  - concept
  - statsmodels
aliases:
  - Granger Causality Test
related:
  - "[[140_Data_Science_AI/Time_Series_Analysis/_Time_Series_Analysis_MOC|_Time_Series_Analysis_MOC]]"
  - "[[TS_Cross_Correlation]]"
  - "[[TS_Vector_Autoregression_VAR|VAR Models]]"
worksheet:
  - WS_TimeSeries_1
date_created: 2025-08-27
---
# Granger Causality

## Definition
**Granger causality** is a statistical hypothesis test for determining whether one time series is useful in forecasting another. It is based on the concept of **predictive causality**.

A time series $X$ is said to **Granger-cause** a time series $Y$ if it can be shown, through a series of statistical tests on their lagged values, that past values of $X$ contain information that helps predict the future of $Y$ *beyond the information already contained in the past values of Y alone*.

## The Core Idea
The test involves fitting and comparing two autoregressive models for a time series $Y$:
1.  **Restricted Model:** An autoregressive model for $Y$ using only its own past (lagged) values.
    $$ Y_t = \sum_{i=1}^{p} \alpha_i Y_{t-i} + \epsilon_{1t} $$
2.  **Unrestricted Model:** An autoregressive model for $Y$ using both its own past values and the past values of another series, $X$.
    $$ Y_t = \sum_{i=1}^{p} \alpha_i Y_{t-i} + \sum_{i=1}^{p} \beta_i X_{t-i} + \epsilon_{2t} $$

The Granger causality test then checks whether the coefficients for the lagged values of $X$ (the $\beta_i$ terms) are statistically significantly different from zero.

-   **Null Hypothesis ($H_0$):** The coefficients $\beta_1, \dots, \beta_p$ are all zero. This means that $X$ does not Granger-cause $Y$.
-   **Alternative Hypothesis ($H_1$):** At least one of the $\beta_i$ coefficients is not zero. This means that $X$ Granger-causes $Y$.

**Result:** If the p-value of the test is below a significance level (e.g., 0.05), we reject the null hypothesis and conclude there is evidence of Granger causality.

## Important Considerations and Limitations

>[!question]- What are the limitations of using Granger Causality to infer relationships between time series?
>Granger causality is a useful tool, but it has significant limitations and should be interpreted with caution.
>
>1.  **Correlation, Not True Causation:** The term "causality" is a misnomer. Granger causality only measures **predictive causality**, not true philosophical or scientific causation. A significant result means that one series is useful for *predicting* another, but it does not prove that one *causes* the other in a real-world sense.
>2.  **Omitted Variable Bias:** The test only considers the two specified time series. If a third, unobserved variable $Z$ is causing changes in both $X$ and $Y$, the test might incorrectly show a causal link between $X$ and $Y$ when they are both just responding to $Z$.
>3.  **Stationarity Requirement:** The Granger causality test requires that both time series be **[[TS_Stationarity|stationary]]**. Applying it to non-stationary data can produce spurious (false) results. You must first test for and correct non-stationarity (e.g., through [[TS_Lag_and_Differencing|differencing]]).
>4.  **Linearity Assumption:** The standard test is based on linear autoregressive models. It may fail to detect non-linear causal relationships.
>5.  **Choice of Lag Order:** The results of the test can be sensitive to the number of lags ($p$) included in the models. Choosing an inappropriate lag length can lead to incorrect conclusions. Lag length is often chosen using information criteria like AIC or BIC on a [[TS_Vector_Autoregression_VAR|VAR model]].
>6.  **Instantaneous Causality:** The test only checks for causality from past values. It does not account for instantaneous relationships (where $X_t$ affects $Y_t$ at the same time step).
>7.  **Directionality:** It tests for a specific direction of causality (e.g., $X \to Y$). To check for a relationship in the other direction ($Y \to X$), a separate test must be performed. It's possible to have bidirectional Granger causality or no causality in either direction.

Despite these limitations, Granger causality is a valuable tool for exploring dynamic relationships and identifying potentially useful leading indicators in multivariate time series analysis.

## Python Example
The `statsmodels` library provides an implementation of the Granger causality test.

```python
import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import grangercausalitytests

# Use the same conceptual data from the Cross-Correlation example
# Ad Spend (series_x) leads Sales (series_y) by 2 months.
np.random.seed(42)
time_index = pd.to_datetime(pd.date_range(start='2020-01-01', periods=100, freq='MS'))
series_x = pd.Series(100 + np.sin(np.linspace(0, 8 * np.pi, 100)) * 20 + np.random.randn(100) * 5, index=time_index)
series_y = pd.Series(200 + np.arange(100) * 0.5 + series_x.shift(2) * 1.5 + np.random.randn(100) * 10, index=time_index)
series_x.name = "Ad_Spend"
series_y.name = "Sales"

# Combine into a DataFrame and drop NaNs
df = pd.concat([series_y, series_x], axis=1).dropna()

# --- Make series stationary ---
df_diff = df.diff().dropna()

# --- Perform Granger Causality Test ---
# We test if 'Ad_Spend' (x) Granger-causes 'Sales' (y).
# The test is run for a range of lags. Let's test up to 4 lags.
max_lag = 4

# Test 1: Does Ad_Spend Granger-cause Sales?
# The first variable in the DataFrame is the target (y), the second is the potential cause (x).
gc_results_x_on_y = grangercausalitytests(df_diff[['Sales', 'Ad_Spend']], maxlag=max_lag, verbose=False)

print(f"--- Does Ad Spend Granger-cause Sales? ---")
for lag in range(1, max_lag + 1):
    p_value = gc_results_x_on_y[lag]['ssr_ftest']
    print(f"Lag {lag}: F-test p-value = {p_value:.4f}")
    if p_value < 0.05:
        print("  => Reject H0. Ad Spend may Granger-cause Sales at this lag.")
    else:
        print("  => Fail to reject H0.")

# Test 2: Does Sales Granger-cause Ad_Spend? (Check the other direction)
gc_results_y_on_x = grangercausalitytests(df_diff[['Ad_Spend', 'Sales']], maxlag=max_lag, verbose=False)

print(f"\n--- Does Sales Granger-cause Ad Spend? ---")
for lag in range(1, max_lag + 1):
    p_value = gc_results_y_on_x[lag]['ssr_ftest']
    print(f"Lag {lag}: F-test p-value = {p_value:.4f}")
    if p_value < 0.05:
        print("  => Reject H0. Sales may Granger-cause Ad Spend at this lag.")
    else:
        print("  => Fail to reject H0.")
```
> **Expected Result:** For the first test (Ad Spend -> Sales), we expect to see low p-values, especially around lag 2, indicating Granger causality. For the second test (Sales -> Ad Spend), we expect to see high p-values, indicating no Granger causality in that direction, which matches how we constructed the data.

---