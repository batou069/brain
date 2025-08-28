## KEYWORDS

1.  **Time Series:** A sequence of data points indexed in time order.
2.  **Trend:** The long-term direction or movement of the data.
3.  **Seasonality:** A repeating, fixed-period pattern in the data (e.g., daily, weekly, yearly).
4.  **Cyclicality:** A non-fixed, longer-term pattern that is not seasonal (e.g., business cycles).
5.  **Residual (Noise):** The random, irregular component of a time series that is left over after the trend, seasonality, and cyclicality have been removed.
6.  **Stationarity:** A property of a time series where its statistical properties (like mean and variance) are constant over time.
7.  **Lag:** A past value in a time series. A lag of 1 refers to the value at the previous time step ($y_{t-1}$).
8.  **Autocorrelation (ACF):** The correlation between a time series and its own lagged values.
9.  **Partial Autocorrelation (PACF):** The partial correlation between a time series and its own lagged values, after removing the effects of the intervening lags.
10. **Forecasting vs. Prediction:** Forecasting is the process of predicting future values based on past and present data.
11. **Univariate vs. Multivariate Time Series:** Univariate involves a single time-dependent variable, while multivariate involves multiple time-dependent variables.

---
## METHODS / MODELS

1.  **Decomposition:** Separating a time series into its constituent components (Trend, Seasonality, Residual).
2.  **Differencing:** A transformation used to make a time series stationary by subtracting the previous observation from the current observation.
3.  **Moving Average (MA):** A simple forecasting method that takes the average of the last 'n' observations.
4.  **Exponential Smoothing:** A forecasting method where more recent data points are given more weight.
    * Holt-Winters Method
5.  **ARIMA Models:** A class of statistical models for analyzing and forecasting time series data.
    * **AR (Autoregressive):** A model that uses the dependent relationship between an observation and some number of lagged observations.
    * **I (Integrated):** The use of differencing to make the series stationary.
    * **MA (Moving Average):** A model that uses the dependency between an observation and a residual error from a moving average model applied to lagged observations.
6.  **SARIMA (Seasonal ARIMA):** An extension of ARIMA that explicitly supports time series data with a seasonal component.
7.  **Prophet:** A forecasting library developed by Meta that is designed to be robust to missing data, shifts in trend, and seasonal effects.
8.  **Machine Learning for Time Series:**
    * **Feature Engineering:** Creating lag features, rolling window statistics (e.g., rolling mean), and date-based features (e.g., day of the week, month).
    * Using standard regressors (e.g., Linear Regression, Random Forest) on the engineered features.
9.  **Deep Learning for Time Series:**
    * **Recurrent Neural Networks (RNN)**
    * **Long Short-Term Memory (LSTM)**
    * **Gated Recurrent Unit (GRU)**

---
## PYTHON LIBRARIES / MODULES

1.  **`pandas`:** Essential for time series data manipulation, indexing, resampling, and rolling windows.
2.  **`statsmodels`:** The primary library for statistical time series analysis in Python, including ARIMA, SARIMA, ACF/PACF plots, and decomposition.
3.  **`scikit-learn`:**
    * `TimeSeriesSplit`: A cross-validator for time series data.
    * Standard regressors (`LinearRegression`, `RandomForestRegressor`, etc.) for use with feature engineering.
4.  **`prophet`:** The official library for using the Prophet forecasting model.
5.  **`TensorFlow` / `PyTorch`:** Deep learning frameworks for implementing models like LSTMs.

---
## QUESTIONS

1.  What is the difference between seasonality and cyclicality?
2.  Why is stationarity a critical assumption for many time series models like ARIMA? How do you test for it?
3.  What is the purpose of differencing a time series?
4.  How do you interpret ACF and PACF plots to determine the parameters (p, q) for an ARIMA model?
5.  Why can't you use standard k-fold cross-validation for time series data? What is the correct approach?
6.  What is "look-ahead bias" and how can you avoid it?
7.  How can you use a model like a Random Forest, which doesn't inherently understand time, for a forecasting problem?
8.  When would you choose a statistical model like SARIMA versus a machine learning approach?
9.  What are the advantages of using a specialized library like Prophet?
10. How do you handle missing values in a time series? Why is simple mean imputation often a bad idea?

---
## EXERCISES

1.  **Data Exploration and Decomposition:**
    * [x] Load the classic "Airline Passengers" dataset. ✅ 2025-08-26
    * [x] Plot the data and visually identify its components (trend, seasonality). ✅ 2025-08-26
    * [ ] Use `statsmodels` to perform an additive and a multiplicative decomposition. Plot the results and interpret them.

2.  **Stationarity and Differencing:**
    * [ ] Check if the airline dataset is stationary using the Augmented Dickey-Fuller (ADF) test.
    * [ ] Apply first-order differencing to the data and plot the result.
    * [ ] Run the ADF test on the differenced data to see if it has become stationary.

3.  **ARIMA Modeling:**
    * [ ] Plot the ACF and PACF of the stationary (differenced) data.
    * [ ] Based on the plots, choose initial p, d, and q parameters for an ARIMA model.
    * [ ] Train an ARIMA(p, d, q) model on the first 80% of the data.
    * [ ] Generate a forecast for the remaining 20% and plot it against the actual values. Evaluate the forecast using Mean Squared Error (MSE).

4.  **Machine Learning Approach:**
    * [ ] Create a feature set for the airline dataset. Include lag features (e.g., value 12 months ago) and a time trend feature (e.g., a simple integer count).
    * [ ] Train a `RandomForestRegressor` on these features.
    * [ ] Compare the performance of the Random Forest model to your ARIMA model on the same test set.