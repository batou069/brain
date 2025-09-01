---
tags:
  - time_series
  - white_noise
  - random_walk
  - stochastic_process
  - stationarity
  - concept
aliases:
  - White Noise
  - Random Walk
related:
  - "[[140_Data_Science_AI/Time_Series_Analysis/_Time_Series_Analysis_MOC|_Time_Series_Analysis_MOC]]"
  - "[[TS_Stationarity]]"
  - "[[TS_Autocorrelation_ACF_PACF]]"
  - "[[TS_Lag_and_Differencing]]"
worksheet:
  - WS_TimeSeries_1
date_created: 2025-08-28
---
# White Noise and Random Walks

White Noise and Random Walks are two fundamental stochastic processes that serve as important building blocks and benchmarks in time series analysis.

## White Noise
-   **Definition:** A time series is considered **white noise** if the variables in the series are independent and identically distributed (i.i.d.) with a mean of zero.
-   **Key Properties:**
    1.  **Constant Mean:** The mean is zero ($E[Y_t] = 0$).
    2.  **Constant Variance:** The variance is constant for all time points ($\text{Var}(Y_t) = \sigma^2$).
    3.  **No Autocorrelation:** There is no correlation between the values of the series at different points in time ($Corr(Y_t, Y_{t-k}) = 0$ for all $k \neq 0$).
-   **Significance:**
    -   **Purely Random:** A white noise series is purely random and unpredictable. If you can predict it, it's not white noise.
    -   **Model Residuals:** The goal of a good time series model is to explain all the predictable patterns in the data. Therefore, the **residuals** (the errors of the model) should ideally be a white noise series. If the residuals are not white noise, it implies there is still some unexplained structure in the data that the model has failed to capture.
-   **ACF/PACF Plot:** The [[TS_Autocorrelation_ACF_PACF|ACF and PACF plots]] of a white noise series will show no significant spikes for any lag greater than zero. All correlations will be within the confidence interval bands.

**Python Example:**
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf

# Generate a white noise series
np.random.seed(42)
white_noise = pd.Series(np.random.normal(loc=0, scale=1, size=500))

# Plot the series and its ACF
# fig, axes = plt.subplots(1, 2, figsize=(12, 4))
# white_noise.plot(ax=axes, title="White Noise Series")
# plot_acf(white_noise, ax=axes, lags=40, title="ACF of White Noise")
# plt.suptitle("White Noise Characteristics", y=1.02)
# plt.tight_layout(); plt.show()
```

## Random Walk
-   **Definition:** A **random walk** is a stochastic process where the value at the next time step is the value at the current time step plus a random step (a white noise term).
-   **Equation:**
    $$ Y_t = Y_{t-1} + \epsilon_t $$
    where $\epsilon_t$ is a white noise term.
-   **Key Properties:**
    1.  **Non-Stationary:** A random walk is a classic example of a non-stationary time series. Its mean is constant (usually assumed to be zero if it starts at zero), but its **variance increases with time** ($\text{Var}(Y_t) = t \sigma^2$). It does not revert to a mean.
    2.  **Unpredictable:** The future path of a random walk is unpredictable. The best forecast for the value at time $t+1$ is simply the value at time $t$.
    3.  **Differencing:** The **first difference** of a random walk is a white noise series:
        $$ \Delta Y_t = Y_t - Y_{t-1} = \epsilon_t $$
        This is a key reason why [[TS_Lag_and_Differencing|differencing]] is used to make non-stationary series stationary.
-   **ACF/PACF Plot:** The ACF plot of a random walk will show a very slow, linear decay, which is a strong indicator of non-stationarity.
-   **Use Cases:**
    -   Modeling phenomena where the future position is a random step from the current position, such as stock prices (Efficient Market Hypothesis), the path of a molecule in a gas, or a drunkard's walk.
    -   Serves as a baseline model for many financial time series. If your complex forecasting model cannot outperform the simple random walk forecast ($\hat{y}_{t+1} = y_t$), it is not adding value.

**Python Example:**
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf

# Generate a random walk series
np.random.seed(0)
# Start with a white noise series (the steps)
steps = np.random.normal(loc=0, scale=1, size=500)
# The random walk is the cumulative sum of the steps
random_walk = pd.Series(steps).cumsum()

# Plot the series and its ACF
# fig, axes = plt.subplots(1, 2, figsize=(12, 4))
# random_walk.plot(ax=axes, title="Random Walk Series")
# plot_acf(random_walk, ax=axes, lags=40, title="ACF of Random Walk")
# plt.suptitle("Random Walk Characteristics", y=1.02)
# plt.tight_layout(); plt.show()
```

Understanding these two basic processes is crucial for diagnosing the properties of more complex time series.

---