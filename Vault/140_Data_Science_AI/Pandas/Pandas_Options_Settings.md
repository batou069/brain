---
tags:
  - pandas
  - configuration
  - display_options
  - settings
  - concept
aliases:
  - Pandas Display Settings
  - pd.set_option
  - pd.get_option
  - Pandas Options
related:
  - "[[Pandas_DataFrame]]"
  - "[[Pandas_Series]]"
worksheet:
  - WS_Pandas_Further_Topics_1
date_created: 2025-05-30
---
# Pandas Options and Settings

Pandas provides a system for controlling various aspects of its behavior, particularly how DataFrames and Series are displayed. This is useful for tailoring the output in interactive sessions (like Jupyter notebooks) or scripts to make data inspection more convenient.

[list2tab|#Options System]
- `pd.set_option(option, value)`
    - **Purpose:** Sets the value of a specified option.
    - **Key Parameters:**
        - `option`: `str`. A dot-delimited string representing the option name (e.g., `'display.max_rows'`).
        - `value`: `object`. The new value for the option.
    - **Common Display Options:**
        - `display.max_rows`: `int`. Max number of rows to display. If `None`, displays all rows.
        - `display.min_rows`: `int`. Number of rows to display in a truncated repr (when `max_rows` is exceeded).
        - `display.max_columns`: `int`. Max number of columns to display. If `None`, displays all columns.
        - `display.max_colwidth`: `int`. Max width of columns. Cells exceeding this width will be truncated. If `None`, no truncation.
        - `display.width`: `int`. Width of the display in characters. If `None`, Pandas will try to detect the window width.
        - `display.precision`: `int`. Floating point output precision (number of significant digits).
        - `display.float_format`: Callable. Formatter function for floating point numbers (e.g., `lambda x: f'{x:.2f}'` for 2 decimal places).
        - `mode.chained_assignment`: `{'warn', 'raise', None}`. Controls behavior for chained assignment, which can lead to `SettingWithCopyWarning`. Default is `'warn'`.
    - **Example:**
      ```python
      import pandas as pd
      import numpy as np

      df = pd.DataFrame(np.random.rand(20, 10)) # 20 rows, 10 columns
      # print("Default display:\n", df) # Might be truncated

      # Set max_rows and max_columns
      pd.set_option('display.max_rows', 10)
      pd.set_option('display.max_columns', 5)
      print("\nDisplay with max_rows=10, max_columns=5:\n", df)

      # Set precision for floating point numbers
      pd.set_option('display.precision', 3)
      print("\nDisplay with precision=3:\n", df)

      # Format floats to 2 decimal places
      pd.set_option('display.float_format', '{:.2f}'.format) # Using .format method
      # or pd.set_option('display.float_format', lambda x: f'{x:.2f}')
      print("\nDisplay with float_format (2 decimals):\n", df)
      
      # Increase column width
      df_text = pd.DataFrame({'Text': ['This is a very long string that might get truncated'] * 3})
      pd.set_option('display.max_colwidth', 30)
      print("\nDisplay with max_colwidth=30:\n", df_text)
      pd.set_option('display.max_colwidth', None) # Reset to no truncation for this column
      print("\nDisplay with max_colwidth=None:\n", df_text)
      ```

- `pd.get_option(option)`
    - **Purpose:** Retrieves the current value of a specified option.
    - **Key Parameters:**
        - `option`: `str`. A dot-delimited string representing the option name.
    - **Returns:** The current value of the option.
    - **Example:**
      ```python
      import pandas as pd

      current_max_rows = pd.get_option('display.max_rows')
      print(f"Current display.max_rows: {current_max_rows}")

      current_precision = pd.get_option('display.precision')
      print(f"Current display.precision: {current_precision}")
      ```

- `pd.reset_option(option)`
    - **Purpose:** Resets the value of a specified option to its default.
    - **Key Parameters:**
        - `option`: `str`. A dot-delimited string representing the option name.
    - **Example:**
      ```python
      import pandas as pd

      pd.set_option('display.max_rows', 500)
      print(f"Set display.max_rows to: {pd.get_option('display.max_rows')}")
      pd.reset_option('display.max_rows')
      print(f"Reset display.max_rows to default: {pd.get_option('display.max_rows')}")
      ```

- `pd.describe_option(option)`
    - **Purpose:** Prints the description of one or more options.
    - **Key Parameters:**
        - `option`: `str`, optional. A dot-delimited string representing the option name. If `None`, prints all options.
    - **Example:**
      ```python
      import pandas as pd

      # pd.describe_option('display.max_rows')
      # To avoid excessive output in this format, this will just show what it does:
      print("Description for 'display.max_rows':")
      # This would typically print:
      # display.max_rows : int
      #     If max_rows is exceeded, switch to truncate view. Depending on
      #     `large_repr`, objects are either centrally truncated or printed as
      #     a summary view. 'None' value means unlimited.
      #     In case python/IPython is running in a terminal and `large_repr`
      #     equals 'truncate' this can be set to 0 and pandas will auto-detect
      #     the height of the terminal and print a centrally truncated repr.
      #     [default: 60] [currently: <current_value>] # (current_value will change based on settings)
      print(pd.describe_option('display.max_rows', _print_desc=False)) # _print_desc=False returns string
      
      # To see all options (can be very long):
      # pd.describe_option()
      ```

- **Context Manager for Options (`pd.option_context`)**
    - **Purpose:** Temporarily set options within a `with` statement. The options revert to their previous values upon exiting the block. This is very useful for applying specific display settings for a small section of code without affecting global settings.
    - **Syntax:**
      ```python
      with pd.option_context(option1, value1, option2, value2, ...):
          # Code with temporary options
          ...
      # Options are reverted here
      ```
    - **Example:**
      ```python
      import pandas as pd
      import numpy as np

      df = pd.DataFrame(np.random.rand(25, 15))
      print(f"Outside context - display.max_rows: {pd.get_option('display.max_rows')}")
      print(f"Outside context - display.max_columns: {pd.get_option('display.max_columns')}")

      with pd.option_context('display.max_rows', 5, 'display.max_columns', 5, 'display.precision', 2):
          print(f"\nInside context - display.max_rows: {pd.get_option('display.max_rows')}")
          print(f"Inside context - display.max_columns: {pd.get_option('display.max_columns')}")
          print("DataFrame display inside context:\n", df)

      print(f"\nBack outside context - display.max_rows: {pd.get_option('display.max_rows')}")
      print(f"Back outside context - display.max_columns: {pd.get_option('display.max_columns')}")
      print("DataFrame display back outside context (default truncation might apply again):\n", df.head(7)) # Showing more rows to see if default truncation kicks in
      ```
    - >[!tip] `pd.option_context` is the recommended way to manage display options for specific analyses or outputs in a script or notebook, as it ensures that changes are localized and do not persist unintentionally.

---