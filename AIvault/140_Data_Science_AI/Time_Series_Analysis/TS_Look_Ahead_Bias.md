---
tags:
  - time_series
  - forecasting
  - evaluation
  - bias
  - data_leakage
  - pitfall
  - concept
aliases:
  - Look-ahead Bias
  - Forward-looking Bias
related:
  - "[[TS_Cross_Validation_Evaluation]]"
  - "[[TS_Feature_Engineering_for_ML]]"
worksheet:
  - WS_TimeSeries_1
date_created: 2025-08-27
---
# Look-ahead Bias

>[!question]- What is "look-ahead bias," and how can you avoid it?

## Definition
**Look-ahead bias** is a common and serious error in time series forecasting and financial modeling. It occurs when a forecasting model is built or evaluated using information that would **not have been available** at the time the forecast was made.

This "looking into the future" leads to overly optimistic and unrealistic performance metrics, resulting in a model that performs well in backtesting but fails in real-world, live forecasting.

## Common Causes of Look-ahead Bias

[list2tab|#Causes of Look-ahead Bias]
- 1. Incorrect Cross-Validation
    -   **Cause:** Using standard k-fold cross-validation that shuffles the data. This allows the model to be trained on data from the future to predict the past.
    -   **Avoidance:** Use a proper **temporal cross-validation** strategy like [[TS_Cross_Validation_Evaluation|rolling forecast origin (sliding or expanding windows)]]. The training set must always consist of data that occurred before the test set.
- 2. Data Leakage During Preprocessing & Feature Engineering
    -   **Cause:** Calculating preprocessing parameters (like scaling means/stds, imputation values) or features using the entire dataset *before* splitting it into training and test sets.
    -   **Example:** Calculating the mean and standard deviation for `StandardScaler` from the full time series and then applying it to both train and test sets. The scaler has "seen" the test data, and this information leaks into the training process.
    -   **Avoidance:**
        -   Always split your data into training and test sets **first**.
        -   Fit all preprocessing transformers (scalers, imputers, etc.) **only on the training data**.
        -   Use the *fitted* transformers to `transform` both the training and the test data.
        -   Using `sklearn` or `sktime` Pipelines is a best practice as they automatically handle this correctly within a cross-validation loop.
- 3. Using Future Information in Feature Creation
    -   **Cause:** Creating features for a time step `t` that use information from time steps after `t`.
    -   **Example (Subtle):** Calculating a centered moving average. The value for time `t` uses values from `t-1`, `t`, and `t+1`. When predicting for time `t`, the value at `t+1` is not yet known.
    -   **Example (Obvious):** Using the closing price of a stock at 4 PM to predict the price at 10 AM of the same day.
    -   **Avoidance:**
        -   Ensure all features for predicting time `t` are created using only information available at or before time `t-1`.
        -   Use **lagged features** and **trailing rolling windows** (windows that only use past data). Pandas `.rolling()` by default uses a trailing window.
- 4. Survivorship Bias
    -   **Cause:** A form of selection bias where the dataset used for backtesting only includes "survivors" (e.g., stocks that still exist today, companies that didn't go bankrupt). The model isn't trained on the failures, leading to an overly optimistic view of performance.
    -   **Avoidance:** Use historical datasets that are point-in-time correct, including delisted stocks or failed companies, if possible.
- 5. Using Incorrect Timestamps
    -   **Cause:** Using the timestamp when data was recorded in a database rather than the timestamp when the event actually occurred. If there's a delay in data collection, you might accidentally use information that wasn't available at the event time.
    -   **Avoidance:** Be meticulous about using the correct event timestamps for all feature creation and modeling.

## How to Avoid Look-ahead Bias: A Checklist
1.  **Split Data Temporally:** Always split your data into training, validation, and test sets based on time. The test set should be the most recent data.
2.  **Use Time Series Cross-Validation:** Employ rolling or expanding window cross-validation for hyperparameter tuning and model evaluation.
3.  **Fit Preprocessors on Training Data Only:** Any data transformation that learns parameters (e.g., `StandardScaler.fit()`, `SimpleImputer.fit()`) must only be fitted on the training portion of your data.
4.  **Create Features Using Past Data Only:** When creating lag or rolling window features, ensure the window only includes data from the past relative to the point you are trying to predict.
5.  **Be Careful with Data Sources:** Ensure your dataset does not contain revised or back-filled data that would not have been available at the time.
6.  **Simulate a Live Environment:** In your backtest, loop through your data chronologically. At each step `t`, only use data available up to `t-1` to make a forecast for `t`.

Avoiding look-ahead bias is critical for building forecasting models that are trustworthy and perform as expected in a real-world production environment.

---