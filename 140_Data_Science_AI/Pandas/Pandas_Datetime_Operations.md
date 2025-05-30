---
tags:
  - pandas
  - datetime
  - timeseries
  - resampling
  - rolling_window
  - concept
aliases:
  - Pandas Time Series
  - to_datetime
  - DatetimeIndex
  - Resample
  - Rolling Calculations
related:
  - "[[Pandas_DataFrame]]"
  - "[[Pandas_Series]]"
  - "[[Pandas_Index_Object]]"
  - "[[NumPy_Data_Types]]"
worksheet:
  - WS_Pandas_Further_Topics_1
date_created: 2025-05-30
---
# Pandas Working with Dates and Times

Pandas has powerful capabilities for working with time series data. This starts with converting string or numerical data into datetime objects, accessing components of these datetimes, and performing operations like resampling and rolling window calculations.

[list2tab|#Datetime Operations]
- `pd.to_datetime()`
    - **Purpose:** Convert argument to datetime. This function is flexible and can parse many different date/time string formats or convert numerical timestamps.
    - **Key Parameters:**
        - `arg`: `int`, `float`, `str`, `datetime`, `list`, `tuple`, `1-d array`, `Series`, `DataFrame/dict-like`. The object to convert.
        - `errors`: `{'ignore', 'raise', 'coerce'}`, default `'raise'`.
            - `raise`: invalid parsing will raise an exception.
            - `coerce`: invalid parsing will be set as `NaT` (Not a Time).
            - `ignore`: invalid parsing will return the input.
        - `format`: `str`, default `None`. The strftime to parse time, e.g. `"%d/%m/%Y"`. See Python's `strftime` documentation. If `None`, pandas will try to infer the format.
        - `unit`: `str`, default `'ns'`. The unit of the arg (D, s, ms, us, ns) denote the unit, which is an integer or float number. This will be based off the origin. E.g., with `unit='s'` and `origin='unix'`, this would calculate the number of seconds when parsing an integer.
        - `origin`: `scalar`, default `'unix'`. Define the reference date. The numeric values would be parsed as number of units (defined by `unit`) since this reference date. If `'unix'` (or POSIX) time; origin is `1970-01-01`.
    - **Returns:** `datetime` if parsing successful, `NaT` if parsing failed and `errors='coerce'`, or `Series` or `DatetimeIndex` if input is a Series or list-like.
    - **Example:**
      ```python
      import pandas as pd

      # From strings
      date_str1 = pd.to_datetime('2023-10-26')
      print(f"Parsed date string 1: {date_str1}, type: {type(date_str1)}")

      date_series = pd.to_datetime(['2023/01/15', '2024.02.20', None, 'invalid_date'], errors='coerce')
      print("\nParsed date series (with coerce):\n", date_series)

      # With specific format
      date_custom_fmt = pd.to_datetime('10-Dec-2023 14:30', format='%d-%b-%Y %H:%M')
      print(f"\nParsed custom format: {date_custom_fmt}")

      # From numeric (e.g., Unix timestamps in seconds)
      timestamps_s = [1672531200, 1675209600] # 2023-01-01, 2023-02-01
      dt_from_ts = pd.to_datetime(timestamps_s, unit='s')
      print("\nParsed from Unix timestamps (seconds):\n", dt_from_ts)
      ```
    - >[!tip] `pd.to_datetime()` is the cornerstone of time series analysis in Pandas. Setting `errors='coerce'` is often useful for handling messy real-world date data.

- `DatetimeIndex` Properties (`.dt` accessor)
    - **Purpose:** Once a Series contains datetime objects (its `dtype` is `datetime64[ns]`), the `.dt` accessor provides access to various properties of the datetimes.
    - **Common Properties:** `.dt.year`, `.dt.month`, `.dt.day`, `.dt.hour`, `.dt.minute`, `.dt.second`, `.dt.microsecond`, `.dt.nanosecond`, `.dt.date`, `.dt.time`, `.dt.dayofweek` (Monday=0, Sunday=6), `.dt.day_name()`, `.dt.month_name()`, `.dt.dayofyear`, `.dt.weekofyear` (or `.dt.isocalendar().week`), `.dt.quarter`, `.dt.is_leap_year`, etc.
    - **Example:**
      ```python
      import pandas as pd

      s = pd.Series(pd.to_datetime(['2023-01-15 10:30:00', '2024-06-20 22:15:45', pd.NaT]))
      print("Original Datetime Series:\n", s)

      print("\nYear:\n", s.dt.year)
      print("Month:\n", s.dt.month)
      print("Day:\n", s.dt.day)
      print("Day of Week (Mon=0):\n", s.dt.dayofweek)
      print("Day Name:\n", s.dt.day_name())
      print("Hour:\n", s.dt.hour)
      print("Date part:\n", s.dt.date)
      ```
    - >[!note] These `.dt` accessors are crucial for [[Feature_Engineering_Pandas|feature engineering]] with time series data, allowing you to extract components that might be relevant for modeling.

- `df.resample(rule, axis=0, ...)`
    - **Purpose:** Resample time-series data. Convenience method for frequency conversion and resampling of time series. Object must have a datetime-like index (`DatetimeIndex`, `PeriodIndex`, or `TimedeltaIndex`).
    - **Key Parameters:**
        - `rule`: `str` or `DateOffset`. The offset string or object representing target conversion (e.g., `'D'` for daily, `'M'` for month end, `'MS'` for month start, `'H'` for hourly, `'5T'` for 5-minute).
        - `axis`: `{0 or 'index', 1 or 'columns'}`, default `0`.
        - `on`: `str`, optional. For a DataFrame, column to use instead of index for resampling. Column must be datetime-like.
        - `level`: `str` or `int`, optional. For a MultiIndex, level to use for resampling.
    - **Returns:** `Resampler` object, which you can then apply aggregation functions to (e.g., `.sum()`, `.mean()`, `.count()`, `.ohlc()`).
    - **Example:**
      ```python
      import pandas as pd
      import numpy as np

      # Create a sample DataFrame with a DatetimeIndex
      rng = pd.date_range('2023-01-01', periods=100, freq='H') # 100 hourly periods
      df = pd.DataFrame({'value': np.random.randn(len(rng))}, index=rng)
      print("Original DataFrame (first 5 rows):\n", df.head())

      # Resample to daily sum
      daily_sum = df.resample('D').sum()
      print("\nDaily sum:\n", daily_sum.head())

      # Resample to monthly mean
      monthly_mean = df.resample('M').mean()
      print("\nMonthly mean:\n", monthly_mean.head())

      # Resample to 2-hourly Open-High-Low-Close (OHLC)
      ohlc_2h = df['value'].resample('2H').ohlc()
      print("\n2-Hourly OHLC:\n", ohlc_2h.head())
      ```
    - >[!tip] `resample()` is fundamental for aggregating or changing the granularity of time series data, e.g., converting tick data to 1-minute bars, or daily data to monthly summaries.

- `df.rolling(window, min_periods=None, center=False, win_type=None, on=None, axis=0, ...)`
    - **Purpose:** Provide rolling window calculations.
    - **Key Parameters:**
        - `window`: `int`, `offset`, or `BaseIndexer subclass`. Size of the moving window.
            - If an `int`, the number of observations used for calculating the statistic.
            - If an `offset` (e.g., `'2D'`), the time period of the window. Each window will be a variable sized based on the observations included in the time-period. This is only valid for datetimelike indexes.
        - `min_periods`: `int`, default `None`. Minimum number of observations in window required to have a value; otherwise, result is `np.nan`. For a window identified by an offset, `min_periods` will default to `1`.
        - `center`: `bool`, default `False`. If `False`, set the window labels as the right edge of the window index. If `True`, set the window labels as the center of the window index.
        - `win_type`: `str`, default `None`. If `None`, all points are evenly weighted. If a string, it must be a valid `scipy.signal window function` (e.g., `'gaussian'`, `'triang'`).
        - `on`: `str`, optional. For a DataFrame, column to calculate the rolling window over. If `None`, it calculates over all numeric columns.
    - **Returns:** `Rolling` object, which you can then apply aggregation functions to (e.g., `.sum()`, `.mean()`, `.std()`, `.corr()`, `.apply()`).
    - **Example:**
      ```python
      import pandas as pd
      import numpy as np

      s = pd.Series(np.random.randn(20), index=pd.date_range('2023-01-01', periods=20, freq='D'))
      print("Original Series:\n", s.head())

      # Rolling mean with a window of 3 observations
      rolling_mean_3obs = s.rolling(window=3).mean()
      print("\nRolling mean (3 observations):\n", rolling_mean_3obs.head(5))

      # Rolling sum with a time-based window of 3 days (index must be datetime-like)
      rolling_sum_3d = s.rolling(window='3D').sum() # Window includes current day and previous 2 days
      print("\nRolling sum (3-day window):\n", rolling_sum_3d.head(5))
      
      # Rolling standard deviation with min_periods
      rolling_std_min_periods = s.rolling(window=5, min_periods=2).std()
      print("\nRolling std (window 5, min_periods 2):\n", rolling_std_min_periods.head())

      # Applying a custom function (e.g., range)
      rolling_range = s.rolling(window=3).apply(lambda x: x.max() - x.min(), raw=True)
      print("\nRolling range (window 3):\n", rolling_range.head())
      ```
    - >[!note] Rolling calculations are essential for smoothing time series, detecting trends (e.g., moving averages), and calculating volatility (e.g., rolling standard deviation). The `window` can be a fixed number of observations or a time offset.

---