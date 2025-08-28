---
tags:
  - time_series
  - forecasting
  - data_analysis
  - statistics
  - moc
  - concept
aliases:
  - Time Series MOC
  - Forecasting MOC
related:
  - "[[_Data_Science_AI_MOC]]"
  - "[[200_Statistics_Probability/_Statistics_Probability_MOC|_Statistics_Probability_MOC]]"
  - "[[160_Python_Libraries/sktime/_sktime_MOC|sktime MOC]]"
  - "[[160_Python_Libraries/tsfresh/_tsfresh_MOC|tsfresh MOC]]"
  - "[[160_Python_Libraries/Statsmodels_Library|Statsmodels Library]]"
  - "[[160_Python_Libraries/Prophet/_Prophet_MOC|Prophet MOC]]"
worksheet:
date_created: 2025-08-27
---
# Time Series Analysis MOC 📈⏳

**Time Series Analysis** comprises methods for analyzing time series data in order to extract meaningful statistics and other characteristics of the data. **Time Series Forecasting** is the use of a model to predict future values based on previously observed values.

This section covers the fundamental concepts, components, models, and evaluation techniques used in time series analysis and forecasting.

## Core Concepts & Components
-   [[TS_Definition_and_Types|Time Series: Definition and Types]] (Univariate vs. Multivariate)
-   [[TS_Components_Decomposition|Components of a Time Series]] (Trend, Seasonality, Cyclicality, Residual)
-   [[TS_Stationarity|Stationarity in Time Series]]
-   [[TS_Autocorrelation_ACF_PACF|Autocorrelation (ACF) and Partial Autocorrelation (PACF)]]
-   [[TS_White_Noise_and_Random_Walks|White Noise and Random Walks]]
-   [[TS_Lag_and_Differencing|Lag and Differencing]]
-   [[TS_Forecasting_vs_Prediction|Forecasting vs. Prediction]]

## Preprocessing & Feature Engineering
-   [[TS_Handling_Missing_Values|Handling Missing Values in Time Series]]
-   [[TS_Rolling_Window_Operations|Rolling Window Operations]] (Moving Averages, etc.)
-   [[TS_Feature_Engineering_for_ML|Feature Engineering for Time Series ML]] (Lag features, date-based features)

## Classical Models & Methods
-   [[TS_Smoothing_Methods|Smoothing Methods]]
    -   [[TS_Moving_Average|Moving Average (MA) Smoothing]]
    -   [[TS_Exponential_Smoothing|Exponential Smoothing (Simple, Holt, Holt-Winters)]]
-   [[TS_ARIMA_Family_Models|ARIMA Family Models]]
    -   [[TS_Autoregressive_AR_Model|Autoregressive (AR) Model]]
    -   [[TS_Moving_Average_MA_Model|Moving Average (MA) Model]]
    -   [[TS_ARMA_Model|ARMA Model]]
    -   [[TS_ARIMA_Model|ARIMA Model]]
    -   [[TS_SARIMA_Model|Seasonal ARIMA (SARIMA)]]
-   [[TS_Decomposition_Methods|Decomposition Methods (e.g., STL)]]
-   [[TS_Multivariate_Models|Multivariate Models]]
    -   [[TS_Vector_Autoregression_VAR|Vector Autoregression (VAR)]]
    -   [[TS_Granger_Causality|Granger Causality]]
    -   [[TS_Cross_Correlation|Cross-Correlation]]
-   [[TS_Prophet_Model|Prophet Model]]

## Machine Learning for Time Series
-   [[TS_ML_for_Forecasting|Using ML Models for Forecasting]] (e.g., Random Forest, Gradient Boosting)
-   [[TS_Cross_Validation_Evaluation|Cross-Validation and Evaluation for Time Series]]
    -   [[TS_Forecast_Error_Metrics|Forecast Error Metrics]] (MAE, MSE, RMSE, MAPE)
    -   [[TS_Look_Ahead_Bias|Look-ahead Bias]]

## Notes in this Section
```dataview
LIST
FROM "140_Data_Science_AI/Time_Series_Analysis"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
```

---