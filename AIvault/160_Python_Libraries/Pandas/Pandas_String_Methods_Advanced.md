---
tags:
  - pandas
  - series
  - string
  - regex
  - text_processing
  - concept
aliases:
  - Pandas str accessor
  - str.get_dummies
  - str.extractall
  - str.match
  - Text Data Pandas
related:
  - "[[Pandas_Series]]"
  - "[[Regular_Expressions]]"
worksheet:
  - WS_Pandas_Further_Topics_1
date_created: 2025-05-30
---
# Pandas Working with Text Data (`.str` accessor - More Detail)

Pandas [[Pandas_Series]] have a `.str` accessor that provides a host of vectorized string processing methods. These methods are similar to Python's built-in string methods but operate on the entire Series at once, handling missing values (NaN) gracefully. This note explores some advanced and commonly used `.str` methods, particularly those involving [[Regular_Expressions]].

[list2tab|#Advanced String Methods]
- `.str.get_dummies(sep='|')`
    - **Purpose:** Split each string in the Series by a separator `sep` and return a [[Pandas_DataFrame]] of dummy/indicator variables.
    - **Key Parameters:**
        - `sep`: `str`, default `'|'`. String to split on.
    - **Returns:** `DataFrame` where each unique substring after splitting becomes a column, and values are 1 if the substring was present, 0 otherwise.
    - **Example:**
      ```python
      import pandas as pd

      s = pd.Series(['a|b', 'a', 'b|c', 'a|c|b', pd.NA])
      print("Original Series:\n", s)

      dummies = s.str.get_dummies(sep='|')
      print("\nDummy variables DataFrame:\n", dummies)

      # Example with a different separator
      s2 = pd.Series(['apple,orange', 'banana', 'apple,banana,grape'])
      dummies2 = s2.str.get_dummies(sep=',')
      print("\nDummy variables with comma separator:\n", dummies2)
      ```
    - >[!tip] This is very useful for converting a column containing multiple categorical labels (in a single string) into a format suitable for machine learning (similar to one-hot encoding for multi-label scenarios).

- `.str.extractall(pat, flags=0)`
    - **Purpose:** For each subject string in the Series, extract groups from all matches of a [[Regular_Expressions]] `pat`. When each subject string in the Series has exactly one match, `.str.extract(pat)` is a simpler alternative. When `pat` has more than one capture group, the result is a DataFrame with one column per group. If `pat` has only one capture group, the result is a Series.
    - **Key Parameters:**
        - `pat`: `str`. Regular expression pattern with capturing groups.
        - `flags`: `int`, default `0` (no flags). Regex flags (e.g., `re.IGNORECASE`).
    - **Returns:** A `DataFrame` with one row per match, and one column per group. The `DataFrame` has a `MultiIndex` with the first level an index from the original Series, and the second level an index indicating the match number. If the pattern does not contain any capture groups, returns a `DataFrame` with a single column named `0` containing all matches.
    - **Example:**
      ```python
      import pandas as pd

      s = pd.Series(["Name: Alice, Age: 30", "Name: Bob, Age: 25, City: NY", "No Info"])
      
      # Extract name and age
      # Pattern: "Name: (capturing group for name), Age: (capturing group for age)"
      pat_name_age = r"Name: (\w+), Age: (\d+)"
      extracted = s.str.extractall(pat_name_age)
      extracted.columns = ['Name', 'Age'] # Rename columns for clarity
      print("Extracted Name and Age:\n", extracted)

      # Example with a single capture group (returns a DataFrame with one column if using extractall)
      pat_age_only = r"Age: (\d+)"
      extracted_age = s.str.extractall(pat_age_only)
      extracted_age.columns = ['Age']
      print("\nExtracted Age (using extractall):\n", extracted_age)
      
      # Using .str.extract for single match per string (if applicable)
      # Note: .str.extract returns NaN if no match, or if multiple matches (which is why extractall is better for multiple)
      # For this specific s, extract would only get the first match if there were multiple age entries per string.
      extracted_age_single = s.str.extract(pat_age_only) 
      extracted_age_single.columns = ['Age']
      print("\nExtracted Age (using extract, first match or NaN):\n", extracted_age_single)

      # Extracting multiple occurrences of a pattern within each string
      s_emails = pd.Series(["Emails: a@b.com, c@d.com", "admin@example.com", "No emails here"])
      email_pat = r"([\w.-]+@[\w.-]+\.\w+)" # A simple email regex
      all_emails = s_emails.str.extractall(email_pat)
      all_emails.columns = ['Email']
      print("\nAll extracted emails:\n", all_emails)
      ```
    - >[!note] `extractall` is powerful for parsing structured or semi-structured text data where multiple pieces of information matching a pattern might exist within each string. The resulting `MultiIndex` helps map extracted parts back to their original Series entries and match numbers.

- `.str.match(pat, case=True, flags=0, na=nan)`
    - **Purpose:** Determine if each string *starts with* a match of a regular expression `pat`. This is essentially `re.match()` applied element-wise.
    - **Key Parameters:**
        - `pat`: `str`. Character sequence or regular expression.
        - `case`: `bool`, default `True`. If `True`, match is case-sensitive.
        - `flags`: `int`, default `0`. Regex module flags, e.g. `re.IGNORECASE`.
        - `na`: Scalar, optional. Value to return for `NaN` values in the Series.
    - **Returns:** `Series` of `bool`.
    - **Example:**
      ```python
      import pandas as pd
      import re # For re.IGNORECASE

      s = pd.Series(['ApplePie', 'appleSauce', 'Banana', 'Orange', pd.NA, 'App'])
      
      # Check if string starts with 'App' (case-sensitive)
      matches_app_case = s.str.match(r'App')
      print("Starts with 'App' (case-sensitive):\n", matches_app_case)

      # Check if string starts with 'app' (case-insensitive)
      matches_app_nocase = s.str.match(r'app', flags=re.IGNORECASE)
      print("\nStarts with 'app' (case-insensitive):\n", matches_app_nocase)

      # Using a more complex regex: starts with 'A' or 'B', followed by any letter, then 'a'
      pat_complex = r"^[AB][a-zA-Z]a" 
      matches_complex = s.str.match(pat_complex)
      print("\nStarts with A or B, then letter, then 'a':\n", matches_complex)
      ```
    - >[!question] What is the difference between `.str.match()` and `.str.contains()`?
    - `str.match(pat)` checks if the pattern `pat` matches at the *beginning* of the string.
    - `str.contains(pat)` checks if the pattern `pat` is found *anywhere* in the string.
    - If you need to check if the *entire* string matches a pattern, you would typically use `str.match(pat + '$')` where `$` is the regex anchor for the end of the string. Or more simply use `Series.str.fullmatch(pat)`.

## More Complex Regex Examples

The true power of these methods shines with more complex [[Regular_Expressions]].

**Example: Extracting components from a URL-like string**
```python
import pandas as pd

data = pd.Series([
    "product/widget_A/id_123/details",
    "category/electronics/item_456/summary",
    "product/gadget_B/id_789",
    "invalid_string",
    pd.NA
])

# Regex to capture type (product/category), name (widget_A/electronics), and optionally id (id_123/item_456)
# (?P<name>...) creates a named capture group
regex_pattern = r"^(?P<type>product|category)/(?P<item_name>[^/]+)/(?P<identifier>(id|item)_[^/]+)"

url_parts = data.str.extractall(regex_pattern)
print("Extracted URL-like parts:\n", url_parts)

# If you only want the first match per string and specific groups
# Use .str.extract() - it returns a DataFrame with columns for each capture group
url_parts_extract = data.str.extract(regex_pattern)
print("\nExtracted URL-like parts (using .str.extract):\n", url_parts_extract)
```

>[!danger] Regular Expression Complexity
>Crafting effective regular expressions can be challenging and error-prone. Always test your regex patterns thoroughly, perhaps using online tools like regex101.com, before applying them to large datasets. Complex regex can also have performance implications.

---