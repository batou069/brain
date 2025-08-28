# Worksheet: Time Series

## Class Decision

## Time Series Analysis
## Keywords
1. Time Series
2. Trend
3. Seasonality
4. Cyclicality
5. Stationarity
6. Irregularity, Noise, Residuals
7. Autocorrelation, Partial Autocorrelation
8. Rolling Correlation
9. Decomposition Methods
10. Differencing / Box-Cox Transformations
11. Granger Causality Test

## Models
1. Naive Model
2. Exponential Smoothing (Simple, Holt, Holt-Winters)
3. Autoregression (AR, ARMA, ARIMA, SARIMA, VAR)
4. Dynamic Regression
5. Tree Models for Time Series
6. Theta Model


## Libraries
- **statsmodels.tsa**: Excels in statistical modeling (e.g., ARIMA, VAR) and diagnostics, but lacks machine learning integration and is less versatile for non-forecasting tasks; overlaps with sktime in forecasting.
- **Prophet**: Ideal for quick, robust seasonal forecasting with minimal setup, but limited to forecasting and lacks classification/clustering; overlaps with sktime in forecasting.
- **sktime**: Comprehensive for forecasting, classification, and regression with strong sklearn integration, but complex for beginners; overlaps with statsmodels.tsa and Prophet in forecasting, tslearn/tsfresh in ML tasks.
- **tslearn**: Specializes in time series clustering and classification with metrics like DTW, but lacks forecasting capabilities; overlaps with sktime and tsfresh in ML applications.
- **tsfresh**: Automates feature extraction for time series ML tasks, but doesn’t support forecasting or modeling; overlaps with sktime and tslearn in preprocessing and ML integration.

## Questions
1) Is there an importance to Train-Test Split?
2) What is the difference between predicting and forecasting?
3) What's the difference between univariate and multivariate in Time Series Analysis?
4) What are the considerations for Time Series Preprocessing
    - Scaling
    - Outliers
    - Feature Engineering
5) How do you determine the appropriate lag order for an autoregressive model?
6) How do you handle missing values and why is simple mean imputation not always a good idea?
7) How do you visualize a time series?
8) What evaluation metrics do you know for Time Series Analysis?
9) What is "Look-Ahead-Bias" and how do you avoid it?
10) What are the pros and cons of using a sliding window?
11) Why can't you use standard k-fold cross-validation for time series data, and what is the correct approach?
12) Provide 5 practical real world use cases for Time Series Analysis for each: Regression and Classification


## Keywords

### 1. Time Series

#### About
A time series is a sequence of data points collected, recorded, or measured at successive, evenly-spaced time intervals.
Each data point represents observations or measurements taken over time, such as stock prices, temperature readings, or sales figures. Time series data is commonly represented graphically with time on the horizontal axis and the variable of interest on the vertical axis, allowing analysts to identify trends, patterns, and changes over time.

#### Importance of Time Series Analysis

1. ****Predict Future Trends:**** Time series analysis enables the prediction of future trends, allowing businesses to anticipate market demand, stock prices, and other key variables, facilitating proactive decision-making.
2. ****Detect Patterns and Anomalies:**** By examining sequential data points, time series analysis helps detect recurring patterns and anomalies, providing insights into underlying behaviors and potential outliers.
3. ****Risk Mitigation:**** By spotting potential risks, businesses can develop strategies to mitigate them, enhancing overall risk management.
4. ****Strategic Planning:**** Time series insights inform long-term strategic planning, guiding decision-making across finance, healthcare, and other sectors.
5. ****Competitive Edge:**** Time series analysis enables businesses to optimize resource allocation effectively, whether it's inventory, workforce, or financial assets. By staying ahead of market trends, responding to changes, and making data-driven decisions, businesses gain a competitive edge.

### 2. Stationarity
A statistical property where the series' properties (mean, variance, autocorrelation) are constant over time.

Seasonality refers to periodic fluctuations or patterns that occur at regular intervals within the time series. These cycles often repeat annually, quarterly, monthly, or weekly and are typically influenced by factors such as seasons, holidays, or business cycles.
Seasonality in time series is recurring and regular patterns at a set interval, which is caused by weather, holidays or business cycles. Ice cream sales usually reach their peak during summer and decrease during winter. Seasonality can happen at any time interval, for instance, daily, weekly or yearly, and can have patterns such as increased weekend sales. Determining these regular patterns is necessary for precise time series forecasting

When it comes to identifying if the data is stationary, it means identifying the fine-grained notions of stationarity in the data. The types of stationarity observed in time series data include

1. **Trend Stationary -**  A time series that does not show a trend.
2. **Seasonal Stationary -** A time series that does not show seasonal changes.
3. **Strictly Stationary -** The joint distribution of observations is invariant to time shift.

https://www.geeksforgeeks.org/machine-learning/seasonality-detection-in-time-series-data/
https://www.geeksforgeeks.org/python/how-to-check-if-time-series-data-is-stationary-with-python/
### 3. Autocorrelation
The correlation of the series with its own past values (lags).

A statistical method to measure the correlation between a time series and a lagged version of itself at different time lags. It helps identify patterns and dependencies within the time series data.
Autocorrelation is a fundamental concept in time series analysis. Autocorrelation is a statistical concept that assesses the degree of correlation between the values of variable at different time points. The article aims to discuss the fundamentals and working of Autocorrelation. 
https://www.geeksforgeeks.org/machine-learning/autocorrelation/
### 4. Partial Autocorrelation
PACF measures the correlation between a time series and its lagged values, controlling for intermediate lags, aiding in identifying direct relationships between variables.
In time series analysis, the partial autocorrelation function (PACF) gives the partial correlation of a stationary time series with its own lagged values, regressed the values of the time series at all shorter lags. It is different from the autocorrelation function, which does not control other lags.

Partial correlation quantifies the relationship between a specific observation and its lagged values. This helps us to examine the direct influence of past time point on the current time point, excluding the indirect influence through the other lagged values. It seeks to determine the unique correlation between a specific time point and another time point, accounting for the influence of the time points in between.

https://www.geeksforgeeks.org/machine-learning/understanding-partial-autocorrelation-functions-pacf-in-time-series-data/
### 5. Trend
The long-term direction of the series

Trend represents the long-term movement or directionality of the data over time. It captures the overall tendency of the series to increase, decrease, or remain stable. Trends can be linear, indicating a consistent increase or decrease, or nonlinear, showing more complex patterns.

Trend is a pattern in data that shows the movement of a series to relatively higher or lower values over a long period of time. In other words, a trend is observed when there is an increasing or decreasing slope in the time series. Trend usually happens for some time and then disappears, it does not repeat. For example, some new song comes, it goes trending for a while, and then disappears. There is fairly any chance that it would be trending again.

https://www.geeksforgeeks.org/python/what-is-a-trend-in-time-series/
### 6. Seasonality
Regular, predictable patterns that repeat over a fixed period (e.g., daily, weekly, yearly).

Seasonal variations refer to the predictable fluctuations or patterns that occur at specific intervals, often corresponding to certain times of the year, months, weeks, or days. These patterns can obscure the underlying trends and make it challenging to analyze the true behavior of the data.
https://www.geeksforgeeks.org/machine-learning/seasonal-adjustment-and-differencing-in-time-series/
https://www.geeksforgeeks.org/machine-learning/seasonality-detection-in-time-series-data/
### 7. Cyclicality
Patterns that are not of a fixed period, often related to longer-term economic or business cycles.

Cyclical variations are longer-term fluctuations in the time series that do not have a fixed period like seasonality. These fluctuations represent economic or business cycles, which can extend over multiple years and are often associated with expansions and contractions in economic activity.
### 8. Residual (Noise)
Irregularity, also known as noise or randomness, refers to the unpredictable or random fluctuations in the data that cannot be attributed to the trend, seasonality, or cyclical variations. These fluctuations may result from random events, measurement errors, or other unforeseen factors. Irregularity makes it challenging to identify and model the underlying patterns in the time series data.
### 9. Differencing
#### Seasonal Differencing

The process of calculating the differences between successive observations in a given time series is known as differencing. Higher-order differences may be obtained by further differentiating the resultant series, which is referred to as the first difference.

The main goal of differencing is to remove non-constant variation and trends from a time series while also stabilizing the mean. When working with non-stationary data—where the statistical characteristics of the series fluctuate over time.

Difference is used in time series analysis to adjust the mean and remove trends or time periods in the data, idea is to calculate the difference between a series of observations at timeline intervals resulting in a new series of data points that represent changes from one period to another rather than absolute values. Differences are useful when dealing with nonstationary time series data, where the mean, variance, or other statistical features change over time The observation and analysis of nonstationary data can be more complicated, and differentiation is a common method of converting such information into a stable form.Each value in the time series is subtracted from the preceding value in first-order differencing.

As a result, a new series is created that symbolizes the transition from one era to the next. Subtracting the second-lag value from the present value is the process of higher-order differencing, and so on.

#### Types of Seasonal Differencing

##### First-order differencing

The first-order differencing for a time series ⁬YtYt​​  may be expressed as follows:

Yt′=Yt−Yt−1Yt′​=Yt​−Yt−1​

Where,

- Yt′Yt′​ is the first-order differenced value at time t
- YtYt​ is the original value at time t
- Yt−1Yt−1​ is the original value at time t-1

First-order differencing removes the immediate trend from the data. It reveals the rate of change between consecutive observations, making it easier to analyze seasonality and cyclical patterns.

##### Second-order differencing

The Second-order differencing for a time series ⁬YtYt​ applies first-order differencing again to the already differenced data, expressed as follows:

Yt′′=Yt′−Yt−1′Yt′′​=Yt′​−Yt−1′​

Second-order differencing removes the trend in the rate of change, highlighting any underlying seasonality or long-term cycles. However, it also removes some information about the original data and can increase variance, making it susceptible to noise.

The general form for differencing of any order d for a time series ⁬Yt⁬Yt​ may be expressed as follows:

Yt(d)=Yt−Yt−(d−1)Yt(d)=Yt−Yt−(d−1)

Where, Yt-(d-1) is the (d-1)th-order differenced value at time t.

Increasing the differencing order further removes higher-frequency components like short-term seasonality and cyclical patterns. However, it can also lead to loss of information and increased vulnerability to noise.

#### ****Choosing the Appropriate**** Seasonal Differencing ****Order****

The appropriate differencing order depends on the specific factors of time series data like:

- ****Trend:**** How strong is the trend? First-order differencing will be enough to remove it.
- ****Seasonality:**** Does the data exhibit seasonal patterns? Second-order differencing will be needed for these.
- ****Noise:**** How much noise is present in the data? Higher orders of differencing can amplify noise.

#### Why is Seasonal Differencing important?

****Differentiating is crucial for a number of reasons.****

- The assumption of stationarity is a fundamental feature of many statistical models, including autoregressive and ARIMA models. Differencing is appropriate for these models since it can convert a non-stationary series into a stationary one.
- Forecasting Accuracy: By eliminating autocorrelation—the association between values in a time series at various lags—differencing may increase the precision of forecasting models. Distancing aids in mitigating the forecasting bias that autocorrelation may cause.
- Trend and Cycle Analysis: By eliminating short-term changes from a time series, differencing may assist in identifying patterns and cycles. In the analysis of economic data, where seasonal and irregular variables might obscure underlying patterns, this can be very helpful.

#### Advantages of Seasonal Differencing

- ****Stationarity:**** By helping to achieve stationarity, differencing facilitates the use of many statistical approaches that presume constant statistical features in the modeling and analysis of time series data.
- ****Trend Removal:**** Differencing efficiently eliminates the impact of trends by calculating the differences between successive data, giving rise to a more lucid picture of the irregular and cyclical components.
- ****Simplicity:**** Variance is a somewhat easy approach that may be used by a wide variety of users, since it doesn't need advanced statistical understanding.

#### DisadvantagesSeasonal Differencing

- ****Information Loss:**** More complex differencing may result in information loss and increase the difficulty of interpreting the changed data.
- ****Sensitivity to Parameter Selection:**** The choice of the differencing parameter might have an impact on how successful differencing is; choosing the wrong value could result in either over-differencing or insufficient trend removal.
- ****Inability to Address Seasonality:**** Seasonality in the data may need to be addressed using other approaches, such as seasonal adjustment, if differencing is found to be insufficient.
### 10. Moving Average
Moving Average Models are a type of [time series analysis](https://www.geeksforgeeks.org/r-language/time-series-analysis-in-r/) model usually used in econometrics to forecast trends and understand patterns in time series data. In moving average models the present value of the time series depends on the linear combination of the past white noise error terms of the time series. In time series analysis [moving average](https://www.geeksforgeeks.org/pandas/how-to-calculate-moving-average-in-a-pandas-dataframe/) is denoted by the letter "**q**" which represents the order of the moving average model, or in simple words we can say the current value of the time series will depend on the past q error terms. Therefore, the moving average model of order q could be represented as:

Xt=c+ϵt+θ1.ϵt−1+θ2.ϵt−2+...+θq.ϵt−qXt​=c+ϵt​+θ1​.ϵt−1​+θ2​.ϵt−2​+...+θq​.ϵt−q​

Here,

- XtXt​ is the value of time series at time t
- **c** is a constant or the mean of the time series
- ϵt,ϵt−1,ϵt−2,...,ϵt−qϵt​,ϵt−1​,ϵt−2​,...,ϵt−q​ are the white noise terms associated with the time series at time t, t-1, t-2, ... , t-q.
- θ1,θ2,...,θqθ1​,θ2​,...,θq​ are the moving average constants.

For example, if we consider MA(1) model, in this model the present value of the time series will only depend on a single past error term and the time series becomes:

Xt=c+ϵt+θ1.ϵt−1Xt​=c+ϵt​+θ1​.ϵt−1​

From this observation we can also conclude one of the most important aspects of moving average models that the higher the value of the order of moving average model (**q**), the model will have longer memory and dependence on the past values.
https://www.geeksforgeeks.org/machine-learning/understanding-the-moving-average-ma-in-time-series-data/
### 11. Autoregressive Model
Autoregressive models (AR models) are a concept in time series analysis and forecasting that captures the relationship between an observation and several lagged observations i.e previous time steps. Its idea is that the current value of a time series data can be expressed as a linear combination of its past values with some random noise.
https://www.geeksforgeeks.org/data-analysis/autoregressive-ar-model-for-time-series-forecasting/

### 12. White Noise
If a time series is white noise, it is a sequence of random numbers and cannot be predicted. If the series of forecast errors are not white noise, it suggests improvements could be made to the predictive model.
A time series is white noise if the variables are independent and identically distributed with a mean of zero.

This means that all variables have the same variance (_sigma^2_) and each value has a zero correlation with all other values in the series.

If the variables in the series are drawn from a Gaussian distribution, the series is called Gaussian white noise.
https://machinelearningmastery.com/white-noise-time-series-python/
### 13. Lag
### 14. Rolling Window

https://www.geeksforgeeks.org/machine-learning/understanding-the-moving-average-ma-in-time-series-data/
### 15. Exponential Smoothing
Exponential smoothing is a popular time series forecasting method known for its simplicity and accuracy in predicting future trends based on historical data. It assumes that future patterns will be similar to recent past data and focuses on learning the average demand level over time.

It gives more weight to the most recent observations and reduces exponentially as the distance from the observations rises with the premise that the future will be similar to the recent past. The word "exponential smoothing" refers to the fact that each demand observation is assigned an exponentially diminishing weight.

- This technique captures the general pattern and can be expanded to include trends and seasonal variations, allowing for precise time series forecasts using past data.
- This method gives a bit of erroneous long-term forecasts.
- It works well with the technique of smoothing when the parameters of the time series change gradually over time.

#### Types of Exponential Smoothing

Exponential smoothing forecasting can be divided into three main types:

##### 1. Simple or Single Exponential Smoothing

Simple Smoothing is a forecasting method used for time series data that does not exhibit a trend or seasonality. It relies on univariate data and uses a single parameter called alpha (αα) or the smoothing factor.

Key points:

- αα determines how much weight is given to the current observation versus the past estimates.
- A smaller αα gives more importance to past predictions, while a larger αα emphasizes recent observations.
- The value of αα typically ranges from 0 to 1.

The smoothing process balances past and present data to provide more stable forecasts. The formula for simple smoothing is as follows:

> st=αxt+(1−α)st−1=st−1+α(xt−st−1)st​=αxt​+(1−α)st−1​=st−1​+α(xt​−st−1​)

**Where:**

- stst​ = smoothed statistic (simple weighted average of current observation xtxt​)
- st−1st−1​ = previous smoothed statistic
- αα = smoothing factor of data; 0<α<10<α<1
- tt = time period

##### 2. Double Exponential Smoothing

Double Exponential Smoothing, also called Holt’s Trend Model, second-order smoothing or Holt’s Linear Smoothing which is a method used to forecast the trend of a time series that does not have seasonality.

- It accounts for trends in the data by introducing a trend component.
- It uses alpha αα to smooth the level of the series.
- It uses beta ββ to smooth the trend or rate of change.
- It supports both additive and multiplicative trends.

Double exponential smoothing works better than simple smoothing when a time series shows a trend but no seasonal pattern.

The formulas for Double exponential smoothing are as follows:

> st=αxt+(1−α)(st−1+bt−1)st​=αxt​+(1−α)(st−1​+bt−1​)

> βt=β(st−st−1)+(1−β)bt−1βt​=β(st​−st−1​)+(1−β)bt−1​

**Where:**

- btbt​ = best estimate of the trend at time tt
- ββ = trend smoothing factor; 0<β<10<β<1

##### 3. Holt-Winters’ Exponential Smoothing

Triple exponential smoothing (also known as Holt-Winters smoothing) is a smoothing method used to predict time series data with both a trend and seasonal component. New smoothing parameter, gamma (γγ), is used to control the effect of seasonal component.

The technique uses exponential smoothing applied three times:

1. (α)(α) the level (intercept),
2. (β)(β) the trend and
3. (γ)(γ) the seasonal component.

This method can be divided into two categories, depending on the seasonality.

- Holt-Winter’s Additive Method (HWIM) is used for addictive seasonality.
- Holts-Winters Multiplicative method (MWM) is used for multiplicative seasonality.

The formulas for the triple exponential smoothing are as follows:

> s0=x0s0​=x0​

> st=α(xt/ct−L)+(1−α)(st−1+bt−1)st​=α(xt​/ct−L​)+(1−α)(st−1​+bt−1​)

> bt=β(st−st−1)+(1−β)bt−1bt​=β(st​−st−1​)+(1−β)bt−1​

> ct=γxt/st+(1−γ)ct−Lct​=γxt​/st​+(1−γ)ct−L​

****Where:****

- stst​ = smoothed statistic
- st−1st−1​ = previous smoothed statistic
- αα = smoothing factor of data (0<α<1)(0<α<1)
- tt = time period
- btbt​ = best estimate of a trend at time t
- ββ = trend smoothing factor (0<β<1)(0<β<1)
- ctct​ = seasonal component at time tt
- γγ = seasonal smoothing parameter (0<γ<1)(0<γ<1)

The Holt-Winters method is the most precise of the three, but it is also the most complicated. It involves more data and more calculations than the others.
https://www.geeksforgeeks.org/artificial-intelligence/exponential-smoothing-for-time-series-forecasting/
### 16. ARIMA
[ARIMA](https://www.geeksforgeeks.org/machine-learning/python-arima-model-for-time-series-forecasting/) modelling or Autoregressive Integrated Moving Average is a time series analysis and forecasting method, the ARIMA model is a combination of autoregression, differencing and moving average which are used in the modelling of time series. Let's break it down and discuss the different components one by one:

- **Autoregressive (AR) Component**: The autoregressive component involves modeling the relationship between an observation and several lagged observations (previously observed points). This component gives us the idea that the current value of the time series is related to the previous values of the series. The term "autoregressive" signifies that the model uses the relationship of the variable with its own past values. The AR component is denoted by ****p**** which can be expressed as:

> Xt=c+ϕ1.Xt−1+ϕ2.Xt−2+...+ϕp.Xt−p+ϵtXt​=c+ϕ1​.Xt−1​+ϕ2​.Xt−2​+...+ϕp​.Xt−p​+ϵt​
> 
> Where:
> 
> - XtXt​ is the value of time series on time t.
> - c is a constant value.
> - ϕ1,ϕ2,...,ϕpϕ1​,ϕ2​,...,ϕp​ are autoregressive coefficients.
> - ϵtϵt​ is error at time t.

- **Integrated(I) Component**: Integrated component makes the time series stationary by differencing; it means that the statistical properties of the time series do not change over time. It helps in stabilizing the mean and removing trends from the time series. Differencing is denoted by d, and dYt=Yt−Yt−1dYt​=Yt​−Yt−1​ represents first order differencing. We can further increase the order of differencing through d2Ytd2Yt​, d3Ytd3Yt​ etc.  
    

- **Moving Average (MA) Component**: This component represents the effect of past error terms on the current value of the time series. The moving average component can be represented as q, which is also known as the order of moving average. The moving average process can also be represented as:

> Xt=c+ϵt+θ1.ϵt−1+θ2.ϵt−2+...+θq.ϵt−qXt​=c+ϵt​+θ1​.ϵt−1​+θ2​.ϵt−2​+...+θq​.ϵt−q​
> 
> Where:
> 
> - XtXt​ is the value of time series at time t.
> - c is a constant.
> - ϵt,ϵt−1,...,ϵt−qϵt​,ϵt−1​,...,ϵt−q​ are the noise terms or the error terms.
> - θ1,θ2,...,θqθ1​,θ2​,...,θq​ are the moving average constants.

### ARIMA(p,d,q):

ARIMA model combines all the AR, I, MA components in it. ARIMA modelling combines all the components mentioned above and its general form is given by:

> Xt=c+ϕ1.Xt−1+ϕ2.Xt−2+...+ϕp.Xt−p+ϵt+θ1.ϵt−1+θ2.ϵt−2+...+θq.ϵt−qXt​=c+ϕ1​.Xt−1​+ϕ2​.Xt−2​+...+ϕp​.Xt−p​+ϵt​+θ1​.ϵt−1​+θ2​.ϵt−2​+...+θq​.ϵt−q​

The general ARIMA forecasting process involves selecting appropriate values for p, d, and q, estimating the model parameters, and using the model to make predictions. The Box-Jenkins methodology is often used for identifying and fitting ARIMA models to time series data.
### 17. SARIMA
SARIMA or Seasonal Autoregressive Integrated Moving Average is an extension of the traditional [ARIMA model](https://www.geeksforgeeks.org/r-language/model-selection-for-arima/), specifically designed for time series data with seasonal patterns. While ARIMA is great for non-seasonal data, SARIMA introduces seasonal components to handle periodic fluctuations and provides better forecasting capabilities for seasonal data.

#### Understanding the Components of SARIMA

SARIMA consists of several components that help capture both short-term and long-term dependencies within a time series:

- ****Seasonal Component****: Represents the repeating patterns or cycles in the data at regular intervals like yearly, monthly, daily, etc. This allows SARIMA to model seasonality effectively.
- ****Autoregressive (AR) Component****: Models the relationship between current and past observations. It captures the autocorrelation of the data over time.
- ****Integrated (I) Component****: Addresses non-stationarity by differencing the data to make it stationary which is crucial for time series analysis.
- ****Moving Average (MA) Component****: Models the relationship between current observations and past residual errors. It helps in capturing short-term fluctuations.

##### SARIMA Notation

The SARIMA model is represented as:

> ****SARIMA(p, d, q)(P, D, Q, s)****

****Parameters:****

- ****p****: Autoregressive order
- ****d****: Number of non-seasonal differences
- ****q****: Moving average order
- ****P****: Seasonal autoregressive order
- ****D****: Seasonal differencing order
- ****Q****: Seasonal moving average order
- ****s****: Length of the seasonal period (e.g., 12 for monthly data)

Before applying SARIMA, seasonal differencing is often required to make the data stationary. This process involves subtracting the current observation from one that corresponds to the same season in the previous cycle. Seasonal differencing helps remove the seasonal pattern from the data, enabling more accurate forecasting.

#### Understanding Mathematical Representation of SARIMA

The SARIMA model can be expressed mathematically as:

> (1−ϕ1B)(1−Φ1Bs)(1−B)(1−Bs)yt=(1+θ1B)(1+Θ1Bs)ϵt(1−ϕ1​B)(1−Φ1​Bs)(1−B)(1−Bs)yt​=(1+θ1​B)(1+Θ1​Bs)ϵt​

****Parameters:****

- ytyt​: The observed time series at time tt
- BB: The backshift operator (lag operator)
- ϕ1ϕ1​: Non-seasonal autoregressive coefficient
- Φ1Φ1​: Seasonal autoregressive coefficient
- θ1θ1​: Non-seasonal moving average coefficient
- Θ1Θ1​: Seasonal moving average coefficient
- ss: Seasonal period
- ϵtϵt​: The white noise error term
https://www.geeksforgeeks.org/machine-learning/sarima-seasonal-autoregressive-integrated-moving-average/
### 18. Granger Causality
Granger causality analysis determines whether one time series can predict future values of another time series. It helps infer causal relationships between variables in time series data, providing insights into the direction of influence.
### 19. Time Series Decomposition
Decomposition separates a time series into its constituent components, typically trend, seasonality, and residual (error). This technique helps isolate and analyze each component individually, making it easier to understand and model the underlying patterns.
Time series decomposition helps us break down a time series dataset into three main components:

1. ***Trend:*** The trend component represents the long-term movement in the data, representing the underlying pattern.
2. ***Seasonality:*** The seasonality component represents the repeating, short-term fluctuations caused by factors like seasons or cycles.
3. ***Residual (Noise):*** The residual component represents random variability that remains after removing the trend and seasonality.
https://www.geeksforgeeks.org/python/time-series-decomposition-techniques/
### 20. Cross-Correlation
### 21. Forecast Error
### 22. Mean Absolute Percentage Error (MAPE)
Calculates the average percentage difference between predicted and actual values. 
https://www.geeksforgeeks.org/python/how-to-calculate-mape-in-python/

### 23. Forecasting vs. Prediction
### 24. Univariate vs. Multivariate Time Series

## Methods/Models

### 1. Autoregressive (AR) Model
Autoregressive (AR) model is a type of time series model that predicts future values based on linear combinations of past values of the same time series. In an AR(p) model, the current value of the time series is modeled as a linear function of its previous p values, plus a random error term. The order of the autoregressive model (p) determines how many past values are used in the prediction.
### 2. Moving Average (MA) Model
Moving Average Models are a type of [time series analysis](https://www.geeksforgeeks.org/r-language/time-series-analysis-in-r/) model usually used in econometrics to forecast trends and understand patterns in time series data. In moving average models the present value of the time series depends on the linear combination of the past white noise error terms of the time series. In time series analysis [moving average](https://www.geeksforgeeks.org/pandas/how-to-calculate-moving-average-in-a-pandas-dataframe/) is denoted by the letter "**q**" which represents the order of the moving average model, or in simple words we can say the current value of the time series will depend on the past q error terms. Therefore, the moving average model of order q could be represented as:

Xt=c+ϵt+θ1.ϵt−1+θ2.ϵt−2+...+θq.ϵt−qXt​=c+ϵt​+θ1​.ϵt−1​+θ2​.ϵt−2​+...+θq​.ϵt−q​

Here,

- **XtXt​** is the value of time series at time t
- **c** is a constant or the mean of the time series
- ϵt,ϵt−1,ϵt−2,...,ϵt−qϵt​,ϵt−1​,ϵt−2​,...,ϵt−q​ are the white noise terms associated with the time series at time t, t-1, t-2, ... , t-q.
- θ1,θ2,...,θqθ1​,θ2​,...,θq​ are the moving average constants.
https://www.geeksforgeeks.org/machine-learning/understanding-the-moving-average-ma-in-time-series-data/
### 3. Autoregressive Moving Average (ARMA)
### 4. Autoregressive Integrated Moving Average (ARIMA)
Autoregressive Integrated Moving Average (ARIMA): ARIMA is a widely used statistical method for time series forecasting. It models the next value in a time series based on linear combination of its own past values and past forecast errors. The model parameters include the order of autoregression (p), differencing (d), and moving average (q).
### 5. Seasonal ARIMA (SARIMA)
- Seasonal Autoregressive Integrated Moving Average (SARIMA): SARIMA extends ARIMA by incorporating seasonality into the model. It includes additional seasonal parameters (P, D, Q) to capture periodic fluctuations in the data.
### 6. Exponential Smoothing (Simple, Holt, Holt-Winters)
Exponential smoothing methods, such as Simple Exponential Smoothing (SES) and Holt-Winters, forecast future values by exponentially decreasing weights for past observations. These methods are particularly useful for data with trend and seasonality.
### 7. Vector Autoregression (VAR)
VAR models extend autoregression to multivariate time series data by modeling each variable as a linear combination of its past values and the past values of other variables. They are suitable for analyzing and forecasting interdependencies among multiple time series.
### 8. Seasonal-Trend Decomposition (STL)
### 9. Dynamic Regression
### 10. Theta Model
A simple and intuitive forecasting technique based on extrapolation and trend fitting.
### 11. Prophet
Prophet is a forecasting tool developed by Facebook that is specifically designed for time series forecasting at scale. It provides a simple yet powerful interface for fitting and forecasting time series data, with built-in support for handling seasonality, holidays, and trend changes.

## Python Libraries/Modules

1. `sktime'
2. `tsfresh`

## Questions

### 1. What is the difference between a stationary and non-stationary time series?
### 2. How can you test for stationarity in a time series dataset?
### 3. Why is differencing used in time series analysis, and how does it affect the data?
### 4. What is the role of autocorrelation and partial autocorrelation in identifying time series model parameters?
### 5. When would you choose SARIMA over ARIMA for modeling a time series?
### 6. How does exponential smoothing differ from moving average models in handling time series data?
### 7. What are the limitations of using Granger Causality to infer relationships between time series?
### 8. How can time series decomposition help in understanding and forecasting a time series?
### 9. What are the advantages and disadvantages of using a rolling window for time series analysis?
### 10. How do you determine the appropriate lag order for an autoregressive model?
### 11. Why is Mean Absolute Percentage Error (MAPE) a useful metric for evaluating time series forecasts?
### 12. How can cross-correlation be used to identify relationships between two time series?
### 13. What is the difference between seasonality and cyclicality?
### 14. Why can't you use standard k-fold cross-validation for time series data, and what is the correct approach?
### 15. What is "look-ahead bias," and how can you avoid it?
### 16. How can you use a model like Random Forest, which doesn't inherently understand time, for a forecasting problem?
### 17. What are the advantages of using a specialized library like Prophet?
### 18. How do you handle missing values in a time series, and why is simple mean imputation often a bad idea?
https://www.geeksforgeeks.org/python/how-to-deal-with-missing-values-in-a-timeseries-in-python/

## Exercises

### Exercise 1: Air Passengers Dataset - ARIMA Modeling and Decomposition
- **Dataset**: Use the "Air Passengers" dataset, available in Python through the `
` library (`from statsmodels.datasets import get_rdataset; air_passengers = get_rdataset("AirPassengers").data`).
- **Task**:
  - Load the Air Passengers dataset, which contains monthly totals of international airline passengers from 1949 to 1960.
  - Perform exploratory data analysis (EDA) to identify trends, seasonality, and stationarity. Visualize the time series using a line plot and compute the autocorrelation function (ACF) and partial autocorrelation function (PACF).
  - Use `statsmodels.tsa.seasonal.Decompose` to perform both additive and multiplicative decomposition. Plot the trend, seasonal, and residual components, and interpret the differences between the two decomposition methods.
  - Apply differencing and/or transformations (e.g., log transformation) to make the series stationary, and confirm stationarity using the Augmented Dickey-Fuller (ADF) test.
  - Fit an ARIMA model to the data using the `statsmodels.tsa.arima.model.ARIMA` class, selecting appropriate ARIMA(p,d,q) parameters based on ACF and PACF plots.
  - Generate a 12-month forecast and evaluate the model’s performance using Mean Absolute Percentage Error (MAPE) on a held-out test set (e.g., the last 12 months of data).
  - Visualize the forecast against the actual data and discuss the model’s ability to capture trends and seasonality.

### Exercise 2: Sunspots Dataset - SARIMA and Random Forest Comparison

- **Dataset**: Use the "Sunspots" dataset, available in Python through the statsmodels library (from statsmodels.datasets import get_rdataset; sunspots = get_rdataset("sunspot.month").data).
- **Task**:
    - Load the Sunspots dataset, which contains monthly sunspot numbers from 1749 to 1983.
    - Conduct exploratory data analysis to examine the time series for trends, seasonality, and periodicity. Plot the time series and compute basic statistics.
    - Perform seasonal-trend decomposition using the STL method (statsmodels.tsa.seasonal.STL) to separate the series into trend, seasonal, and residual components. Visualize each component.
    - Fit a Seasonal ARIMA (SARIMA) model using the statsmodels.tsa.statespace.sarimax.SARIMAX class, selecting parameters based on decomposition and ACF/PACF plots.
    - Create a feature set for the dataset, including lag features (e.g., values at lags 1, 12, 24) and rolling window statistics (e.g., rolling mean over 12 months).
    - Train a RandomForestRegressor on the engineered features using sklearn.ensemble.RandomForestRegressor.
    - Generate a 24-month forecast for both the SARIMA and Random Forest models, evaluating performance using Mean Squared Error (MSE) and Mean Absolute Error (MAE) on a held-out test set (e.g., the last 24 months).
    - Compare the performance of the two models and discuss their ability to capture cyclical patterns in sunspot activity.

### Exercise 3: Energy Consumption Forecasting with Kaggle Dataset

- **Dataset**: Use the "Household Electric Power Consumption" dataset from Kaggle (available at: https://www.kaggle.com/datasets/uciml/electric-power-consumption-data-set). 
- **Task**: 
- Download and load the Household Electric Power Consumption dataset, which contains measurements of electric power consumption in one household with a one-minute sampling rate over several years. 
- Perform exploratory data analysis (EDA) to investigate trends, seasonality, and potential stationarity in the time series. Aggregate the data to a daily or hourly level (e.g., using `pandas` resampling) to reduce noise and computational complexity. 
- Visualize the time series (e.g., global active power) and compute the autocorrelation function (ACF) to identify potential seasonal patterns. 
- Apply a seasonal decomposition using the STL method (`statsmodels.tsa.seasonal.STL`) to separate the series into trend, seasonal, and residual components. Plot and interpret the results. 
- Fit a SARIMA model to the data using `statsmodels.tsa.statespace.sarimax.SARIMAX`, selecting parameters based on ACF/PACF plots and the observed seasonality (e.g., daily or weekly cycles). 
- Generate a forecast for the next 7 days (or 168 hours if using hourly data) and evaluate the model’s performance using Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE) on a held-out test set (e.g., the last 7 days of data). 
- Visualize the forecast against the actual data and discuss the model’s ability to capture daily or weekly consumption patterns, suggesting potential improvements.



# New Worksheet

# Time Series Analysis
## Keywords

---

### 1. Time Series
1.  **Short Description:** A time series is a sequence of data points collected at successive, equally spaced points in time.
2.  **What is it good for?:** Analyzing a time series allows us to understand the underlying patterns in the data, such as trends and seasonality, which is essential for making forecasts about future values.
3.  **Details:**
    * The two main goals of time series analysis are **identifying the nature of the phenomenon** represented by the sequence of observations, and **forecasting** (predicting future values).
    * Time series data has a natural temporal ordering, which distinguishes it from other types of data. This order is crucial and cannot be ignored.
    * It can be **univariate** (a single variable observed over time, like temperature) or **multivariate** (multiple variables observed over time, like a stock's price, volume, and P/E ratio).
    * Measurements can be taken at any frequency: hourly, daily, monthly, yearly, etc.
4.  **Examples:**
    * **Conceptual:** The daily closing price of a stock, the monthly rainfall in a city, the hourly number of visitors to a website, a patient's heart rate measured every second.
    * **Analogy:** A time series is like a movie. Each data point is a single frame. To understand the story (the underlying patterns), you must watch the frames in the correct order. Shuffling the frames would make the story incomprehensible.
    * **Python Code:**
    ```python
    import pandas as pd
    import numpy as np

    # Create a simple time series
    date_rng = pd.date_range(start='2023-01-01', end='2023-01-10', freq='D')
    data = np.random.randint(20, 50, size=(len(date_rng)))
    time_series = pd.Series(data, index=date_rng)
    print(time_series)
    ```

---

### 2. Trend
1.  **Short Description:** A trend is the long-term, underlying direction (an increase, decrease, or stagnation) in a time series.
2.  **What is it good for?:** Identifying the trend is the first step in understanding the long-term behavior of a series. It must often be removed or modeled before other patterns like seasonality can be accurately analyzed.
3.  **Details:**
    * A trend represents the "big picture" movement, ignoring the short-term fluctuations.
    * Trends can be **deterministic** (following a consistent path, like a straight line) or **stochastic** (the direction itself can change over time).
    * Common types of trends include **linear** (a straight line) and **exponential** (a curve that increases or decreases at an accelerating rate).
    * The presence of a trend is a major cause of non-stationarity in a time series.
4.  **Examples:**
    * **Conceptual:** The steady increase in global population over the last century, the decline in the price of computer memory over the last 30 years.
    * **Analogy:** A trend is like the overall trajectory of a rocket launch. While there might be small wobbles (noise) and planned stage separations (seasonality), the overall direction is consistently upward. 

---

### 3. Seasonality
1.  **Short Description:** Seasonality refers to predictable, repeating patterns or fluctuations in a time series that occur at **fixed calendar intervals** (e.g., daily, weekly, yearly).
2.  **What is it good for?:** Modeling seasonality is crucial for accurate short-term and medium-term forecasting, as these patterns are expected to repeat in the future. It helps in planning for predictable peaks and troughs in demand, traffic, etc.
3.  **Details:**
    * The period of the seasonality is fixed and known. For example, monthly data often has a seasonality of 12 months.
    * Seasonality is caused by factors such as weather, holidays, and social customs (e.g., retail sales peaking in December).
    * It can be **additive** (the magnitude of the seasonal swing is constant over time) or **multiplicative** (the magnitude of the seasonal swing increases or decreases along with the trend).
    * It is a common source of non-stationarity.
4.  **Examples:**
    * **Conceptual:** Retail sales peaking every December, electricity demand increasing every summer due to air conditioning, website traffic peaking on weekdays and dropping on weekends.
    * **Analogy:** Seasonality is like the regular opening and closing times of a shop. You know with certainty that it will be busy during the day and quiet at night, and this pattern repeats every single day.

---

### 4. Cyclicality
1.  **Short Description:** Cyclicality refers to fluctuations in a time series that are not of a fixed period, often occurring over longer timeframes.
2.  **What is it good for?:** Identifying cycles is important for understanding long-term business and economic trends. However, they are much harder to model and forecast than seasonality because their duration and magnitude are not constant.
3.  **Details:**
    * The key difference from seasonality is that cycles have **variable and unknown periods**. A business cycle, for example, might last anywhere from 2 to 10 years.
    * Cycles are often associated with economic or business conditions, like periods of expansion followed by periods of contraction.
    * Because of their irregularity, cycles are often analyzed as part of the "trend" component or are left in the "residual" component after trend and seasonality are removed.
4.  **Examples:**
    * **Conceptual:** The boom-and-bust cycles of the stock market, the multi-year cycles in the housing market, the El Niño weather patterns which occur every 2-7 years.
    * **Analogy:** If seasonality is the predictable daily tide, cyclicality is like a tsunami. You know it's a wave-like pattern, but you don't know exactly when the next one will come or how big it will be.

---

### 5. Stationarity
1.  **Short Description:** A time series is stationary if its statistical properties—specifically its mean, variance, and autocorrelation—are all constant over time.
2.  **What is it good for?:** Stationarity is a critical assumption for many statistical time series models, particularly ARIMA models. These models are designed to work on stationary data, so non-stationary data must be transformed first.
3.  **Details:**
    * **Constant Mean:** The series does not have a trend. It fluctuates around a consistent average value.
    * **Constant Variance:** The volatility or spread of the series does not change over time.
    * **Constant Autocovariance:** The relationship between the series and its lagged values is consistent over time.
    * A stationary series is easier to model because its past behavior is a good predictor of its future behavior. Non-stationary series have patterns that change over time, making them unpredictable.
4.  **Examples:**
    * **Conceptual:** The noise from an un-tuned radio is a stationary series. Its average volume and the range of its static don't change no matter when you listen. A stock price, which trends upward over time, is non-stationary.
    * **Python Code (ADF Test):** The Augmented Dickey-Fuller (ADF) test is a statistical test for stationarity. The null hypothesis is that the series is non-stationary.
    ```python
    from statsmodels.tsa.stattools import adfuller
    
    # Assuming 'time_series' is a pandas Series
    result = adfuller(time_series.dropna())
    print(f'ADF Statistic: {result[0]}')
    print(f'p-value: {result[1]}')
    # A p-value <= 0.05 indicates the series is likely stationary
    ```
5.  **The Math Corner:**
    A time series $\{Y_t\}$ is (weakly) stationary if for all time points $t$ and any lag $k$:
    1.  The mean is constant: $E[Y_t] = \mu$
    2.  The variance is constant: $Var(Y_t) = \sigma^2 < \infty$
    3.  The autocovariance is constant: $Cov(Y_t, Y_{t-k}) = \gamma_k$
    This means the mean, variance, and how the series relates to its past values do not depend on *when* you look at the series.

---

### 6. Irregularity, Noise, Residuals
1.  **Short Description:** The residual (also called irregularity or noise) is the random, unpredictable component of a time series that remains after the trend and seasonal components have been removed.
2.  **What is it good for?:** Analyzing the residuals is a crucial diagnostic step. A good model should leave behind residuals that are random noise (resembling a stationary series with no patterns). If there are patterns left in the residuals, it means the model has failed to capture all the predictable information in the data.
3.  **Details:**
    * In an ideal decomposition, the residuals should have a mean of zero, constant variance, and no autocorrelation.
    * Residuals represent the effects of short-term, unforeseen, and non-repeating events.
    * Outliers in the original time series will often appear clearly in the residual component.
4.  **Examples:**
    * **Conceptual:** In a model of monthly retail sales, the trend is the year-over-year growth and the seasonality is the Christmas peak. The residual might be a small, unpredictable blip in sales in a random month due to a one-off local event.
    * **Analogy:** If you're listening to a radio station (the signal), the trend is the volume slowly increasing, and seasonality is the predictable ad break every 15 minutes. The residual is the random crackle of static that you can't predict or explain.

---

### 7. Autocorrelation, Partial Autocorrelation
1.  **Short Description:** **Autocorrelation (ACF)** is the correlation between a time series and its own past values (lags), while **Partial Autocorrelation (PACF)** is the correlation between the series and a lag after removing the effects of the intervening lags.
2.  **What is it good for?:** Plotting the ACF and PACF is the primary method for identifying the appropriate parameters (p, q) for AR and MA components in ARIMA models.
3.  **Details:**
    * **ACF** tells you the *total* correlation (direct and indirect) between a point and its lags. For example, the correlation at lag 3 is influenced by the correlations at lags 1 and 2.
    * **PACF** tells you only the *direct* correlation between a point and a specific lag. It removes the influence of the shorter lags.
    * For an **AR(p) model**, the ACF will tail off gradually, while the PACF will have a sharp cutoff after lag `p`.
    * For an **MA(q) model**, the ACF will have a sharp cutoff after lag `q`, while the PACF will tail off gradually.
4.  **Examples:**
    * **Analogy:** Imagine a line of dominoes.
        * **ACF** at lag 3 asks: "If I know the first domino fell, how much does that tell me about the fourth domino falling?" The answer is "a lot," but this is an *indirect* effect; the first domino causes the second to fall, which causes the third, which causes the fourth.
        * **PACF** at lag 3 asks: "If I already know what dominoes 2 and 3 did, how much *extra* information does knowing about domino 1 give me about domino 4?" The answer is "almost none," because the direct effect is from domino 3 to 4. The PACF isolates this direct link.
    * **Python Code:**
    ```python
    from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
    
    # Assuming 'stationary_series' is a pandas Series
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    plot_acf(stationary_series, ax=ax1, lags=40)
    plot_pacf(stationary_series, ax=ax2, lags=40)
    plt.show()
    ```

---

### 8. Rolling Correlation
1.  **Short Description:** Rolling correlation is a measure of the correlation between two time series over a moving window of time.
2.  **What is it good for?:** It is used to determine if the relationship between two variables is stable over time. A stable correlation is desirable for many models, while a changing correlation can signal a structural break or a dynamic relationship that needs to be modeled differently.
3.  **Details:**
    * It is calculated by defining a window size (e.g., 30 days) and then sliding that window across the time series, calculating the correlation between the two series within the window at each step.
    * The result is a new time series that shows how the correlation itself evolves.
    * It's a useful tool in finance to see if the correlation between two assets (e.g., stocks and bonds) changes during market stress.
4.  **Python Code:**
    ```python
    # Assuming 'series1' and 'series2' are two pandas Series
    window_size = 30
    rolling_corr = series1.rolling(window=window_size).corr(series2)
    rolling_corr.plot(title=f'Rolling {window_size}-Day Correlation')
    plt.show()
    ```

---

### 9. Decomposition Methods
1.  **Short Description:** Decomposition is the process of splitting a time series into its constituent components: Trend (T), Seasonality (S), and Residual (R).
2.  **What is it good for?:** It provides a structured way to understand the underlying patterns in the data. By isolating the components, we can better model them or remove them to focus on a specific aspect of the series.
3.  **Details:**
    * There are two primary models for decomposition:
        * **Additive:** Assumes the components are added together. Best for series where the seasonal variation is constant over time.
        * **Multiplicative:** Assumes the components are multiplied. Best for series where the seasonal variation increases or decreases with the trend.
    * The first step in decomposition is often to estimate the trend, usually with a moving average. Then, the seasonal component is estimated from the detrended series.
4.  **The Math Corner:**
    * **Additive Model:** $Y_t = T_t + S_t + R_t$
    * **Multiplicative Model:** $Y_t = T_t \times S_t \times R_t$
    A multiplicative model can often be converted to an additive one by taking the logarithm: $\log(Y_t) = \log(T_t) + \log(S_t) + \log(R_t)$.

---

### 10. Differencing / Box-Cox Transformations
1.  **Short Description:** Differencing and Box-Cox are two common data transformations used to make a time series stationary.
2.  **What is it good for?:**
    * **Differencing** is used to remove a trend and stabilize the mean of a series.
    * **Box-Cox Transformation** is used to stabilize the variance of a series.
3.  **Details:**
    * **Differencing:** This involves creating a new series where the value at any time $t$ is the difference between the original value at time $t$ and the value at time $t-1$. This is called first-order differencing. If the series is still not stationary, it can be differenced again (second-order). Seasonal differencing involves subtracting the value from the previous season (e.g., 12 months ago).
    * **Box-Cox Transformation:** This is a family of power transformations that includes the logarithm and square root as special cases. It is only applicable to strictly positive data. It finds the best exponent ($\lambda$) to transform the data to make its variance more constant.
4.  **The Math Corner:**
    * **First-Order Differencing:** $Y'_t = Y_t - Y_{t-1}$
    * **Box-Cox Transformation:**
        $$
        y_t^{(\lambda)} = \begin{cases} \frac{y_t^\lambda - 1}{\lambda} & \text{if } \lambda \neq 0 \\ \log(y_t) & \text{if } \lambda = 0 \end{cases}
        $$

---

### 11. Granger Causality Test
1.  **Short Description:** The Granger Causality Test is a statistical hypothesis test to determine whether one time series is useful in forecasting another.
2.  **What is it good for?:** It helps to identify potentially useful leading indicators or exogenous variables for a forecasting model.
3.  **Details:**
    * The test checks if the lagged values of series X can improve the prediction of the future values of series Y, beyond what the lagged values of Y itself can already provide.
    * **Important:** It tests for **predictive causality**, not true philosophical causality. If X Granger-causes Y, it doesn't mean X *causes* Y; it just means X is a statistically useful predictor for Y.
    * The null hypothesis is that series X does not Granger-cause series Y. A low p-value (< 0.05) leads to rejecting the null hypothesis.
    * The test requires the time series to be stationary.

## Models

---

### 1. Naive Model
1.  **Short Description:** The Naive Model is the simplest forecasting method where the forecast for the next period is simply the value from the current period.
2.  **What is it good for?:** It serves as a crucial **baseline** for evaluating more complex models. If your sophisticated model cannot perform better than the naive forecast, it is not adding any value.
3.  **Details:**
    * For seasonal data, a **Seasonal Naive Model** is often used, where the forecast for the next period is the value from the same period in the previous season (e.g., the forecast for this December is the value from last December).
    * It assumes that the most recent observation is the only important one.
    * It is optimal for data that follows a true random walk.
4.  **The Math Corner:**
    * **Standard Naive:** $\hat{Y}_{t+1} = Y_t$
    * **Seasonal Naive:** $\hat{Y}_{t+1} = Y_{t+1-m}$ (where $m$ is the seasonal period)

---

### 2. Exponential Smoothing (Simple, Holt, Holt-Winters)
1.  **Short Description:** Exponential Smoothing is a family of forecasting methods where the forecast is a weighted average of past observations, with the weights decreasing exponentially as the observations get older.
2.  **What is it good for?:** It's a versatile and widely used set of methods that can be adapted to data with different characteristics (no trend, trend, and seasonality).
3.  **Details:**
    * **Simple Exponential Smoothing (SES):** Used for data with no trend or seasonality. It has one smoothing parameter, $\alpha$ (alpha), for the level.
    * **Holt's Linear Trend Method:** An extension of SES that adds a second smoothing parameter, $\beta$ (beta), to model the trend.
    * **Holt-Winters' Seasonal Method:** An extension of Holt's method that adds a third smoothing parameter, $\gamma$ (gamma), to model seasonality. It can be additive or multiplicative.
4.  **The Math Corner (Holt-Winters Additive):**
    The method involves three smoothing equations:
    * **Level:** $L_t = \alpha(Y_t - S_{t-m}) + (1-\alpha)(L_{t-1} + T_{t-1})$
    * **Trend:** $T_t = \beta(L_t - L_{t-1}) + (1-\beta)T_{t-1}$
    * **Seasonal:** $S_t = \gamma(Y_t - L_t) + (1-\gamma)S_{t-m}$
    * **Forecast:** $\hat{Y}_{t+h} = L_t + h \cdot T_t + S_{t-m+h}$
    Where $\alpha, \beta, \gamma$ are the smoothing parameters, and $m$ is the seasonal period.

---

### 3. Autoregression (AR, ARMA, ARIMA, SARIMA, VAR)

---

#### • Moving Average (MA) Model
1.  **Short Description:** A Moving Average (MA) model is a time series model that assumes the current value is a linear combination of past forecast errors.
2.  **What is it good for?:** It is used to model shocks or unexpected events whose effects are felt for a short, finite period. It is a key component of ARMA and ARIMA models.
3.  **Details:**
    * It is fundamentally different from a "moving average" used for smoothing. An MA model is a regression-like model on past errors.
    * The "order" of the model, $q$, specifies how many past error terms are included. An MA(q) model's memory is limited to $q$ periods.
    * An MA model is always stationary.
4.  **The Math Corner:**
    An MA(q) model is defined as:
    $$
    Y_t = \mu + \epsilon_t + \theta_1 \epsilon_{t-1} + ... + \theta_q \epsilon_{t-q}
    $$
    Where $\mu$ is the mean of the series, $\epsilon_t$ is the current error term (white noise), and $\theta_i$ are the model parameters.

---

1.  **Short Description:** This is a large family of statistical models that use past values and/or past forecast errors in the series to predict future values.
2.  **What is it good for?:** These models are the workhorses of classical time series forecasting, providing a powerful framework for modeling stationary time series with various correlation structures.
3.  **Details:**
    * **AR (Autoregressive):** The model assumes the current value is a linear combination of its own past values. The order `p` defines how many lags are used.
    * **ARMA (Autoregressive Moving Average):** Combines AR and MA models. It models the current value using both past values (AR part) and past forecast errors (MA part).
    * **ARIMA (Autoregressive Integrated Moving Average):** An extension of ARMA that includes an "Integrated" component, `d`, which refers to the order of differencing applied to the series to make it stationary. This allows the model to handle trends.
    * **SARIMA (Seasonal ARIMA):** An extension of ARIMA that adds seasonal components (P, D, Q, m) to model seasonality.
    * **VAR (Vector Autoregression):** A multivariate extension where multiple time series are modeled together. Each variable is modeled as a linear combination of its own past values and the past values of the other variables in the system.
4.  **The Math Corner (ARIMA(p,d,q)):**
    An ARIMA model combines the AR(p) model, MA(q) model, and d-order differencing. An AR(p) model is:
    $$
    Y_t = c + \phi_1 Y_{t-1} + ... + \phi_p Y_{t-p} + \epsilon_t
    $$
    The full ARIMA model is a complex equation that applies this logic to a d-times differenced series.

---

### 4. Dynamic Regression
1.  **Short Description:** A dynamic regression model is a standard regression model that includes time series components, typically by modeling the errors with an ARIMA process.
2.  **What is it good for?:** It allows you to build a regression model that includes external predictors (exogenous variables) while also accounting for the autocorrelation in the data that a standard regression model would ignore.
3.  **Details:**
    * It's also known as an ARIMAX model or Regression with ARIMA Errors.
    * The model has two parts: a standard regression equation and an ARIMA model for the error term.
    * This is useful for modeling things like sales, where you have predictors like advertising spend, but the sales data itself also has a time series structure (trend, seasonality, etc.).
4.  **The Math Corner:**
    The model can be written as:
    1.  **Regression Part:** $Y_t = \beta_0 + \beta_1 X_{1,t} + ... + \eta_t$
    2.  **Error Part:** $\eta_t$ is modeled as an ARIMA(p,d,q) process.

---

### 5. Tree Models for Time Series
1.  **Short Description:** Tree-based models like Random Forest or Gradient Boosting can be used for time series forecasting by transforming the problem into a standard regression problem through feature engineering.
2.  **What is it good for?:** They are very powerful for capturing complex, non-linear relationships and interactions between features. They can easily incorporate exogenous variables.
3.  **Details:**
    * The model itself does not inherently understand time. Its understanding comes from the features you create.
    * **Feature Engineering** is key:
        * **Lag Features:** Past values of the series (e.g., $Y_{t-1}, Y_{t-2}, ...$).
        * **Rolling Window Features:** Statistics over a past window (e.g., 7-day rolling average, 30-day rolling standard deviation).
        * **Date-based Features:** Day of the week, month, year, week of the year, is_holiday, etc.
    * Once the feature set is created, you can train a model like a RandomForestRegressor to predict $Y_t$ based on these features.

---

### 6. Theta Model
1.  **Short Description:** The Theta model is a simple yet surprisingly effective forecasting method based on decomposing a time series into two "theta-lines" and then combining their forecasts.
2.  **What is it good for?:** It has performed very well in forecasting competitions, often outperforming more complex models. It is particularly good for data with trends.
3.  **Details:**
    * The original series is first tested for seasonality. If present, it is deseasonalized.
    * The core idea is to modify the local curvature of the time series. This is controlled by a parameter, $\theta$.
    * The standard Theta method (with $\theta=2$) creates two lines: one is the linear regression of the data, and the other is created by "doubling" the curvature of the data.
    * Each of these two new series is forecasted separately using Simple Exponential Smoothing, and their results are combined to produce the final forecast.

## Libraries
* **statsmodels.tsa:** Excels in statistical modeling (e.g., ARIMA, VAR) and diagnostics, but lacks machine learning integration and is less versatile for non-forecasting tasks; overlaps with sktime in forecasting.
* **Prophet:** Ideal for quick, robust seasonal forecasting with minimal setup, but limited to forecasting and lacks classification/clustering; overlaps with sktime in forecasting.
* **sktime:** Comprehensive for forecasting, classification, and regression with strong sklearn integration, but complex for beginners; overlaps with statsmodels.tsa and Prophet in forecasting, tslearn/tsfresh in ML tasks.
* **tslearn:** Specializes in time series clustering and classification with metrics like DTW, but lacks forecasting capabilities; overlaps with sktime and tsfresh in ML applications.
* **tsfresh:** Automates feature extraction for time series ML tasks, but doesn’t support forecasting or modeling; overlaps with sktime and tslearn in preprocessing and ML integration.

## Questions

---

### 1) Is there an importance to Train-Test Split?
* **Short Answer:** Yes, it is absolutely critical, but it must be done differently than in standard machine learning.
* **Long Answer:** A train-test split is essential to evaluate how well your model will perform on unseen, future data. However, for time series, you **cannot** do a random split. This would cause **data leakage**, where the model is trained on data from the future and tested on data from the past, which is impossible in a real-world scenario. The correct approach is a **chronological split**. You choose a point in time and use all data *before* that point for training and all data *after* that point for testing.

---

### 2) What is the difference between predicting and forecasting?
* **Short Answer:** In the context of time series, the terms are often used interchangeably, but "forecasting" is more specific.
* **Long Answer:**
    * **Prediction** is a general term for estimating an outcome for a new observation, regardless of time. For example, predicting if a customer will churn based on their current attributes.
    * **Forecasting** specifically refers to predicting future values of a time series. It inherently involves the dimension of time and the assumption that the future will behave similarly to the past. All forecasting is a type of prediction, but not all prediction is forecasting.

---

### 3) What's the difference between univariate and multivariate in Time Series Analysis?
* **Short Answer:** Univariate analysis involves a single time-dependent variable, while multivariate analysis involves two or more.
* **Long Answer:**
    * **Univariate:** You are modeling and forecasting a single series based only on its own past values (e.g., forecasting next month's temperature using only historical temperature data). Models like ARIMA and Exponential Smoothing are primarily for univariate analysis.
    * **Multivariate:** You are modeling multiple variables simultaneously, allowing for the relationships between them to be considered. For example, forecasting sales based on past sales, past advertising spend, and past competitor prices. Models like VAR and dynamic regression are used for multivariate analysis.

---

### 4) What are the considerations for Time Series Preprocessing
* **Short Answer:** Key considerations are scaling, handling outliers, and creating meaningful features, all while respecting the temporal order of the data.
* **Long Answer:**
    * **Scaling:** For many models (especially neural networks and some statistical models), features should be scaled to a common range (e.g., 0 to 1 with `MinMaxScaler` or a standard normal distribution with `StandardScaler`). It's crucial to fit the scaler **only on the training data** and then use it to transform both the training and test data to avoid look-ahead bias.
    * **Outliers:** Outliers can heavily skew statistical models. They should be investigated. They might be data errors that can be corrected or removed, or they might be genuine extreme events that need to be kept. Techniques like clipping (capping values at a certain percentile) can be used, but this should be done with caution.
    * **Feature Engineering:** This is often the most important step. It involves creating variables that help the model understand the time series patterns. This includes creating lag features, rolling window statistics (mean, std, min, max), and date-based features (day of week, month, is_holiday).

---

### 5) How do you determine the appropriate lag order for an autoregressive model?
* **Short Answer:** By inspecting the Partial Autocorrelation (PACF) plot of the stationary time series.
* **Long Answer:** For a pure Autoregressive (AR) model, the process is as follows:
    1.  Make the time series stationary (e.g., by differencing).
    2.  Plot the PACF of the stationary series.
    3.  Look for a "sharp cutoff" in the plot. The lag at which the PACF plot cuts off (i.e., the bars become statistically insignificant and fall inside the confidence interval) is the suggested order, `p`, for the AR model. For example, if the PACF has a significant spike at lag 1 and lag 2, and then cuts off, you would choose `p=2`.

---

### 6) How do you handle missing values and why is simple mean imputation not always a good idea?
* **Short Answer:** Missing values can be handled by forward-fill, backward-fill, or interpolation. Simple mean imputation is often a bad idea because it ignores the temporal structure of the data.
* **Long Answer:**
    * **Why Mean Imputation is Bad:** Replacing a missing value with the global mean of the entire series ignores the time context. If the series has a trend, the global mean will be an unrealistic value for points at the beginning or end of the series. It creates an artificial flat spot that disrupts the autocorrelation structure.
    * **Better Methods:**
        * **Forward-Fill (`ffill`):** Fills the missing value with the last known observation. Good for series where values don't change rapidly.
        * **Backward-Fill (`bfill`):** Fills with the next known observation.
        * **Linear Interpolation:** Fills the missing value by drawing a straight line between the last known point and the next known point. This is often a very effective and reasonable approach.
        * **Seasonal Imputation:** For seasonal data, you could fill a missing value with the value from the same period in the previous season.

---

### 7) How do you visualize a time series?
* **Short Answer:** The most important visualization is a simple **line plot** against time. Other useful plots include decomposition plots, ACF/PACF plots, and seasonal plots.
* **Long Answer:**
    * **Line Plot:** The primary tool. Plotting the data over time reveals trends, seasonality, cycles, and outliers at a glance.
    * **Seasonal Plot:** A plot where the data for each "season" (e.g., each year) is overlaid on top of each other. This makes it very easy to see the seasonal pattern and identify any years where the pattern changed.
    * **Decomposition Plot:** A plot showing the separated trend, seasonal, and residual components, as generated by a decomposition method.
    * **ACF/PACF Plots:** Used for model identification, as described earlier.
    * **Box Plots by Season:** A box plot for each month or day of the week can help visualize the distribution and stability of the seasonal pattern.

---

### 8) What evaluation metrics do you know for Time Series Analysis?
* **Short Answer:** Common metrics include Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and Mean Absolute Percentage Error (MAPE).
* **Long Answer:**
    * **Scale-Dependent Errors:** These are in the same units as the original data.
        * **MAE (Mean Absolute Error):** Easy to interpret, less sensitive to outliers.
        * **MSE (Mean Squared Error):** Penalizes large errors more heavily. Not in the original units.
        * **RMSE (Root Mean Squared Error):** The square root of MSE, so it's back in the original units. The most common metric.
    * **Percentage Errors:** These are unit-free, making them useful for comparing forecasts across different datasets.
        * **MAPE (Mean Absolute Percentage Error):** Very intuitive ("we were off by X% on average"), but can be problematic if the true values are close to zero.
    * **Scaled Errors:**
        * **MASE (Mean Absolute Scaled Error):** A more robust measure that scales the error based on the in-sample error of a naive forecast. A MASE < 1 means the model is better than a naive forecast.

---

### 9) What is "Look-Ahead-Bias" and how do you avoid it?
* **Short Answer:** Look-ahead bias is when your model accidentally uses information from the future to make its predictions, leading to unrealistically good performance. You avoid it by strictly separating past and future data in all preprocessing and validation steps.
* **Long Answer:** This is one of the most dangerous pitfalls in time series analysis. It occurs when information that would not have been available at the time of the forecast is used in the model.
    * **Examples:**
        * Calculating the mean or standard deviation for scaling using the *entire* dataset, including the test set.
        * Imputing a missing value in the training set using information from the test set.
        * Using a rolling average that is centered instead of one that only uses past data.
    * **How to Avoid It:**
        * **Strict Chronological Splits:** Always split your data into train/validation/test sets based on time.
        * **Fit on Train Only:** Any preprocessing step that learns parameters from the data (like a `StandardScaler` or an imputer) must be `fit` **only on the training data** and then used to `transform` the validation and test sets.
        * **Use a Pipeline:** Encapsulating your preprocessing and modeling steps in a pipeline can help prevent accidental data leakage.

---

### 10) What are the pros and cons of using a sliding window?
* **Short Answer:** Pros: It's a powerful way to structure time series data for ML models. Cons: It can be computationally expensive and requires choosing an appropriate window size.
* **Long Answer:** A sliding (or rolling) window is a technique used to create features for machine learning models.
    * **Pros:**
        * **Feature Creation:** It allows you to create rich features like rolling means, standard deviations, min, max, etc., which capture recent trends and volatility.
        * **Structure for ML:** It transforms a time series problem into a standard supervised learning problem format (a table of features X and a target y) that models like Random Forest can use.
    * **Cons:**
        * **Computational Cost:** Calculating statistics over many windows for a large dataset can be slow.
        * **Choice of Window Size:** The size of the window is a critical hyperparameter. A window that is too short might be too noisy, while one that is too long might obscure recent changes. The optimal size often needs to be found through experimentation.
        * **Information Loss:** At the beginning of the series, you will have `NaN` values until the first full window is available, leading to a loss of some initial data.

---

### 11) Why can't you use standard k-fold cross-validation for time series data, and what is the correct approach?
* **Short Answer:** Standard k-fold cross-validation shuffles the data, which destroys the temporal order and causes look-ahead bias. The correct approach is a "walk-forward" or "rolling forecast origin" validation.
* **Long Answer:**
    * **Why it Fails:** Standard k-fold CV randomly partitions the data into k folds. In one iteration, it might train on data from 2020 and 2022 and be asked to validate on data from 2021. This is unrealistic and leads to an overly optimistic performance estimate.
    * **The Correct Approach: Walk-Forward Validation:** This method respects the chronological order.
        1.  Start with a small subset of data for training (e.g., the first year).
        2.  Forecast the next step (or N steps).
        3.  Record the error.
        4.  **Slide the window forward:** Add the forecasted data point(s) to the training set.
        5.  Repeat from step 2.
    This process simulates how a model would actually be used in production: train on all available history, make a forecast, wait for new data, retrain, and forecast again. Scikit-learn provides a `TimeSeriesSplit` object that implements this logic.

---

### 12) Provide 5 practical real world use cases for Time Series Analysis for each: Regression and Classification
* **Short Answer:** Regression focuses on forecasting continuous values, while classification focuses on identifying patterns or events.
* **Long Answer:**
    * **Regression (Forecasting) Use Cases:**
        1.  **Retail:** Forecasting weekly sales for a specific product to optimize inventory.
        2.  **Finance:** Forecasting the daily closing price of a stock or an exchange rate.
        3.  **Energy:** Forecasting hourly electricity demand for a city to manage the power grid.
        4.  **Logistics:** Forecasting the number of packages that will arrive at a sorting facility each day.
        5.  **Web Analytics:** Forecasting daily active users for a website to plan server capacity.
    * **Classification Use Cases:**
        1.  **Manufacturing (Predictive Maintenance):** Classifying sensor data from a machine as "normal operation" or "impending failure."
        2.  **Healthcare:** Classifying a patient's EKG signal segment as "normal heartbeat" or "arrhythmia."
        3.  **Cybersecurity:** Classifying a sequence of network requests as "benign user activity" or "denial-of-service attack."
        4.  **Finance (Fraud Detection):** Classifying a sequence of credit card transactions as "legitimate" or "fraudulent."
        5.  **Audio Processing:** Classifying a short audio clip of speech into spoken keywords (e.g., "Hey Siri").


# Datasets

Below is a list of time series datasets available on Kaggle that can be used for time series problems, along with a brief description of each, including whether they are univariate or multivariate. These datasets are suitable for practicing time series analysis and forecasting, as outlined in the "Time Series" worksheet context. The selection focuses on datasets relevant for statistical and machine learning approaches, excluding neural network-specific applications as per your requirements.

## Time Series Datasets on Kaggle

1. **Acea Smart Water Analytics**  
   - **Link**: https://www.kaggle.com/datasets/acea-smart-water-analytics  
   - **Description**: This dataset contains time series data related to water management, including measurements like water flow, pressure, and quality metrics from various sensors in a water distribution network.  
   - **Type**: Multivariate (multiple variables such as flow rate, pressure, and other water-related metrics recorded over time).  
   - **Use Case**: Forecasting water demand or detecting anomalies in water distribution systems.  [](https://www.kaggle.com/code/andreshg/timeseries-analysis-a-complete-guide)

2. **Seattle Burke Gilman Trail**  
   - **Link**: https://www.kaggle.com/datasets/city-of-seattle/seattle-burke-gilman-trail  
   - **Description**: This dataset tracks the number of pedestrians and cyclists on the Burke-Gilman Trail in Seattle, recorded hourly, along with additional features like weather conditions (temperature, precipitation).  
   - **Type**: Multivariate (includes count of users, weather variables, and temporal features like hour and day).  
   - **Use Case**: Forecasting trail usage or analyzing the impact of weather on pedestrian and cyclist activity.  [](https://www.kaggle.com/code/ritesh11/multivariate-time-series-forecasting)

3. **Store Sales - Time Series Forecasting**  
   - **Link**: https://www.kaggle.com/competitions/store-sales-time-series-forecasting  
   - **Description**: A Kaggle competition dataset with daily sales data for various products across multiple stores, including additional features like store location, product type, and promotional events.  
   - **Type**: Multivariate (sales as the target variable, with features like store ID, product category, and promotions).  
   - **Use Case**: Forecasting daily sales for retail planning and inventory management.  

4. **Air Quality Data in India (2015-2020)**  
   - **Link**: https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india  
   - **Description**: This dataset contains hourly air quality measurements (e.g., PM2.5, PM10, NO2, CO) across multiple cities in India, along with meteorological data like temperature and humidity.  
   - **Type**: Multivariate (multiple air quality and weather variables recorded over time).  
   - **Use Case**: Forecasting air pollution levels or detecting anomalies in air quality trends.  

5. **Bike Sharing Demand**  
   - **Link**: https://www.kaggle.com/competitions/bike-sharing-demand  
   - **Description**: A Kaggle competition dataset with hourly bike rental counts in Washington, D.C., including features like weather (temperature, humidity, wind speed), and temporal features (day, hour, season).  
   - **Type**: Multivariate (bike rental count as the target, with weather and temporal features).  
   - **Use Case**: Forecasting bike rental demand for optimizing bike-sharing systems.  

6. **Daily Climate Time Series Data**  
   - **Link**: https://www.kaggle.com/datasets/sumanthvrao/daily-climate-time-series-data  
   - **Description**: This dataset contains daily weather measurements (temperature, humidity, wind speed, and pressure) for a specific location over several years.  
   - **Type**: Multivariate (multiple weather-related variables).  
   - **Use Case**: Forecasting weather variables or analyzing seasonal patterns in climate data.  

7. **Global Temperature Time Series**  
   - **Link**: https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data  
   - **Description**: This dataset includes monthly global and regional temperature records, with variables like average temperature, temperature uncertainty, and geographic data.  
   - **Type**: Univariate (if focusing solely on temperature) or Multivariate (if including additional variables like uncertainty or location).  
   - **Use Case**: Forecasting global temperature trends or analyzing climate change patterns.  

8. **PJME Hourly Energy Consumption**  
   - **Link**: https://www.kaggle.com/datasets/robikscube/hourly-energy-consumption  
   - **Description**: This dataset provides hourly energy consumption data (in megawatts) for the PJM Interconnection region in the U.S., with timestamps as the primary feature.  
   - **Type**: Univariate (energy consumption as the single time series variable).  
   - **Use Case**: Forecasting energy consumption for grid management or load balancing.  

9. **Web Traffic Time Series Forecasting**  
   - **Link**: https://www.kaggle.com/competitions/web-traffic-time-series-forecasting  
   - **Description**: A Kaggle competition dataset with daily page views for thousands of Wikipedia articles, where each article’s page views form a separate time series.  
   - **Type**: Univariate (each article’s page views) or Multivariate (if combining multiple articles or metadata like article category).  
   - **Use Case**: Forecasting web traffic for content planning or server load optimization.  

10. **M5 Forecasting - Accuracy**  
    - **Link**: https://www.kaggle.com/competitions/m5-forecasting-accuracy  
    - **Description**: A Kaggle competition dataset with daily sales data for products across multiple Walmart stores, including features like item ID, department, store location, and temporal data (e.g., holidays, events).  
    - **Type**: Multivariate (sales as the target, with additional features like item and store metadata).  
    - **Use Case**: Forecasting product sales for retail inventory and supply chain optimization.  
