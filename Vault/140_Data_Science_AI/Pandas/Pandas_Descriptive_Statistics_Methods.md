---
tags:
  - pandas
  - dataframe
  - statistics
  - correlation
  - covariance
  - unique
  - value_counts
  - rank
  - concept
aliases:
  - DataFrame Statistics
  - Correlation Matrix
  - Covariance Matrix
  - Unique Values
  - Value Counts
  - Data Ranking
related:
  - "[[Pandas_DataFrame]]"
  - "[[Pandas_Series]]"
  - "[[Pandas_sum_min_max_describe]]"
  - "[[Linear_Algebra]]"
  - "[[NumPy_Matrix_Operations_Examples]]"
worksheet:
  - WS_Pandas_Further_Topics_1
date_created: 2025-05-30
---
# Pandas Descriptive Statistics (More Depth)

Pandas provides a rich set of functions for computing descriptive statistics on [[Pandas_DataFrame]] and [[Pandas_Series]] objects. These go beyond basic sum, min, max, and mean, offering insights into relationships between columns, distributions, and rankings.

[list2tab|#Statistical Methods]
- `df.corr()`
    - **Purpose:** Compute pairwise correlation of columns, excluding NA/null values.
    - **Key Parameters:**
        - `method`: `{'pearson', 'kendall', 'spearman'}` or callable. Default: `'pearson'`.
            - `pearson`: standard correlation coefficient.
            - `kendall`: Kendall Tau correlation coefficient.
            - `spearman`: Spearman rank correlation.
            - `callable`: callable with input two 1d ndarrays and returning a float.
        - `min_periods`: `int`, optional. Minimum number of observations required per pair of columns to have a valid result.
    - **Returns:** `DataFrame` of correlation matrix.
    - **Example:**
      ```python
      import pandas as pd
      import numpy as np

      data = {'A': np.random.rand(5),
              'B': np.random.rand(5),
              'C': [1, 2, 3, 4, 5]}
      df = pd.DataFrame(data)
      df.iloc[0, 0] = np.nan # Introduce a NaN

      # Pearson correlation (default)
      corr_matrix_pearson = df.corr()
      print("Pearson correlation matrix:\n", corr_matrix_pearson)

      # Spearman rank correlation
      corr_matrix_spearman = df.corr(method='spearman')
      print("\nSpearman correlation matrix:\n", corr_matrix_spearman)
      ```
    - >[!note] Correlation indicates the strength and direction of a linear relationship between two variables. Values range from -1 (perfect negative correlation) to +1 (perfect positive correlation), with 0 indicating no linear correlation.

- `df.cov()`
    - **Purpose:** Compute pairwise covariance of columns, excluding NA/null values.
    - **Key Parameters:**
        - `min_periods`: `int`, optional. Minimum number of observations required per pair of columns to have a valid result.
        - `ddof`: `int`, default `1`. Delta Degrees of Freedom. The divisor used in calculations is `N - ddof`, where `N` represents the number of elements.
    - **Returns:** `DataFrame` of covariance matrix.
    - **Example:**
      ```python
      import pandas as pd
      import numpy as np

      data = {'A': [1, 2, 3, 4, 5],
              'B': [5, 4, 3, 2, 1],
              'C': [2, 3, 2, 5, 4]}
      df = pd.DataFrame(data)

      cov_matrix = df.cov()
      print("Covariance matrix:\n", cov_matrix)
      ```
    - >[!note] Covariance measures the joint variability of two random variables. A positive covariance indicates that the variables tend to move in the same direction, while a negative covariance indicates they tend to move in opposite directions. The magnitude is harder to interpret than correlation as it's not normalized.

- `df.nunique()` / `series.nunique()`
    - **Purpose:** Count number of distinct elements. Can be used on a Series or applied to each column or row of a DataFrame.
    - **Key Parameters:**
        - `axis`: `{0 or 'index', 1 or 'columns'}`, default `0`. The axis to use. 0 for rows (count distinct in each column), 1 for columns (count distinct in each row).
        - `dropna`: `bool`, default `True`. Don’t include NaN in the count.
    - **Returns:** `Series` (or `int` if used on a Series).
    - **Example:**
      ```python
      import pandas as pd
      import numpy as np

      data = {'A': ['apple', 'banana', 'apple', np.nan, 'orange'],
              'B': [1, 2, 1, 3, 2]}
      df = pd.DataFrame(data)

      # Number of unique values per column (default)
      unique_counts_cols = df.nunique()
      print("Unique counts per column (NaNs excluded):\n", unique_counts_cols)

      # Number of unique values per column (NaNs included)
      unique_counts_cols_incl_na = df.nunique(dropna=False)
      print("\nUnique counts per column (NaNs included):\n", unique_counts_cols_incl_na)

      # Number of unique values per row
      unique_counts_rows = df.nunique(axis=1)
      print("\nUnique counts per row:\n", unique_counts_rows)

      # On a Series
      s = pd.Series([1, 1, 2, 3, 3, 3, np.nan])
      print(f"\nUnique count in Series (NaN excluded): {s.nunique()}")
      print(f"Unique count in Series (NaN included): {s.nunique(dropna=False)}")
      ```

- `series.value_counts()`
    - **Purpose:** Return a Series containing counts of unique values in a Series. The resulting object will be in descending order so that the first element is the most frequently-occurring element. Excludes NA values by default.
    - **Key Parameters:**
        - `normalize`: `bool`, default `False`. If `True` then the object returned will contain the relative frequencies of the unique values.
        - `sort`: `bool`, default `True`. Sort by frequencies.
        - `ascending`: `bool`, default `False`. Sort in ascending order.
        - `bins`: `int`, optional. Rather than count values, group them into half-open bins, a convenience for `pd.cut`, only works with numeric data.
        - `dropna`: `bool`, default `True`. Don’t include counts of NaN.
    - **Returns:** `Series`.
    - **Example:**
      ```python
      import pandas as pd
      import numpy as np

      s = pd.Series(['A', 'B', 'A', 'C', 'A', 'B', np.nan, 'D'])
      print("Value counts:\n", s.value_counts())
      print("\nValue counts (normalized):\n", s.value_counts(normalize=True))
      print("\nValue counts (including NaN):\n", s.value_counts(dropna=False))

      # With numeric data and bins
      data_numeric = pd.Series(np.random.randint(0, 10, 100))
      print("\nValue counts with bins:\n", data_numeric.value_counts(bins=3))
      ```
    - >[!tip] `value_counts()` is extremely useful for understanding the distribution of categorical data or discrete numerical data.

- `df.rank()` / `series.rank()`
    - **Purpose:** Compute numerical data ranks (1 through n) along an axis. By default, equal values are assigned a rank that is the average of the ranks of those values.
    - **Key Parameters:**
        - `axis`: `{0 or 'index', 1 or 'columns'}`, default `0`. Axis for the function to be applied on.
        - `method`: `{'average', 'min', 'max', 'first', 'dense'}`, default `'average'`. How to rank the group of records that have the same value (i.e. ties):
            - `average`: average rank of the group
            - `min`: lowest rank in the group
            - `max`: highest rank in the group
            - `first`: ranks assigned in order they appear in the array
            - `dense`: like ‘min’, but rank always increases by 1 between groups.
        - `numeric_only`: `bool`, optional. For DataFrame objects, rank only numeric columns if set to True.
        - `na_option`: `{'keep', 'top', 'bottom'}`, default `'keep'`. How to rank NaN values:
            - `keep`: assign NaN rank to NaN values
            - `top`: assign lowest rank to NaN values
            - `bottom`: assign highest rank to NaN values
        - `ascending`: `bool`, default `True`. Whether or not the elements should be ranked in ascending order.
        - `pct`: `bool`, default `False`. Whether or not to display the returned rankings in percentile form.
    - **Returns:** `DataFrame` or `Series` with ranks.
    - **Example:**
      ```python
      import pandas as pd
      import numpy as np

      data = {'col1': [10, 20, 10, 30, 20],
              'col2': [np.nan, 5, 15, 5, 25]}
      df = pd.DataFrame(data)
      print("Original DataFrame:\n", df)

      # Default rank (average method)
      df_rank_avg = df.rank()
      print("\nRank (average method):\n", df_rank_avg)

      # Rank with 'min' method for ties
      df_rank_min = df.rank(method='min')
      print("\nRank (min method):\n", df_rank_min)

      # Rank with 'dense' method
      df_rank_dense = df.rank(method='dense')
      print("\nRank (dense method):\n", df_rank_dense)

      # Rank descending
      df_rank_desc = df.rank(ascending=False)
      print("\nRank (descending):\n", df_rank_desc)

      # Rank with NaNs at the bottom
      df_rank_na_bottom = df.rank(na_option='bottom')
      print("\nRank (NaNs at bottom):\n", df_rank_na_bottom)

      # Percentile rank
      df_rank_pct = df.rank(pct=True)
      print("\nPercentile Rank:\n", df_rank_pct)
      ```

---