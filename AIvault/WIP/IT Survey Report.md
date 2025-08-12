# Initial Inspection
```
df.info()
```

RangeIndex: 1253 entries, 0 to 1252
Data columns (total 23 columns):

| #   | Column                                                                                                                  | Non-Null Count | Dtype   |
| --- | ----------------------------------------------------------------------------------------------------------------------- | -------------- | ------- |
| 0   | Timestamp                                                                                                               | 1253 non-null  | object  |
| 1   | Age                                                                                                                     | 1226 non-null  | float64 |
| 2   | Gender                                                                                                                  | 1243 non-null  | object  |
| 3   | City                                                                                                                    | 1253 non-null  | object  |
| 4   | Position                                                                                                                | 1247 non-null  | object  |
| 5   | Total years of experience                                                                                               | 1237 non-null  | object  |
| 6   | Years of experience in Germany                                                                                          | 1221 non-null  | object  |
| 7   | Seniority level                                                                                                         | 1241 non-null  | object  |
| 8   | Your main technology / programming language                                                                             | 1126 non-null  | object  |
| 9   | Other technologies/programming languages you use often                                                                  | 1096 non-null  | object  |
| 10  | Yearly brutto salary (without bonus and stocks) in EUR                                                                  | 1253 non-null  | float64 |
| 11  | Yearly bonus + stocks in EUR                                                                                            | 829 non-null   | object  |
| 12  | Annual brutto salary (without bonus and stocks) one year ago. Only answer if staying in the same country                | 885 non-null   | float64 |
| 13  | Annual bonus+stocks one year ago. Only answer if staying in same country                                                | 614 non-null   | object  |
| 14  | Number of vacation days                                                                                                 | 1185 non-null  | object  |
| 15  | Employment status                                                                                                       | 1236 non-null  | object  |
| 16  | Сontract duration                                                                                                       | 1224 non-null  | object  |
| 17  | Main language at work                                                                                                   | 1237 non-null  | object  |
| 18  | Company size                                                                                                            | 1235 non-null  | object  |
| 19  | Company type                                                                                                            | 1228 non-null  | object  |
| 20  | Have you lost your job due to the coronavirus outbreak?                                                                 | 1233 non-null  | object  |
| 21  | Have you been forced to have a shorter working week (Kurzarbeit)? If yes, how many hours per week                       | 373 non-null   | float64 |
| 22  | Have you received additional monetary support from your employer due to Work From Home? If yes, how much in 2020 in EUR | 462 non-null   | object  |

## Renaming columns into shorter lowercase names

```python
df = df.rename(columns=str.lower, copy=True)

df = df.rename(columns={
  "position ": "position",
  "total years of experience": "exp_years_total",
  "years of experience in germany": "exp_years_de",
  "seniority level": "seniority_lvl",
  "your main technology / programming language": "tech_main",
  "other technologies/programming languages you use often": "tech_other",
  "yearly brutto salary (without bonus and stocks) in eur": "salary_2020_noextras",
  "yearly bonus + stocks in eur": "salary_2020_extras",
  "annual brutto salary (without bonus and stocks) one year ago. only answer if staying in the same country": "salary_2019_noextras",
  "annual bonus+stocks one year ago. only answer if staying in same country": "salary_2019_extras",
  "number of vacation days": "vacation_days",
  "employment status": "status_employment",
  "сontract duration": "duration_contract",
  "main language at work": "main_work_language",
  "company size": "company_size",
  "company type": "company_type",
  "have you lost your job due to the coronavirus outbreak?": "corona_jobloss",
  "have you been forced to have a shorter working week (kurzarbeit)? if yes, how many hours per week": "kurzarbeit_weekly_h",
  "have you received additional monetary support from your employer due to work from home? if yes, how much in 2020 in eur": "monetary_support",
}, copy = True)
```

New names:
```
['timestamp', 'age', 'gender', 'city', 'position', 'exp_years_total', 'exp_years_de', 'seniority_lvl', 'tech_main', 'tech_other', 'salary_2020_noextras', 'salary_2020_extras', 'salary_2019_noextras', 'salary_2019_extras', 'vacation_days', 'status_employment', 'duration_contract', 'main_work_language', 'company_size', 'company_type', 'corona_jobloss', 'kurzarbeit_weekly_h', 'monetary_support']
```
# Missing Values

```python
{col: [df[col].isnull().sum(), f'% {np.round(np.mean(df[col].isnull()*100))}'] for col in df.columns if df[col].isnull().any()}
```

Output:
```
{'age': [np.int64(27), '% 2.0'],
 'gender': [np.int64(10), '% 1.0'],
 'position': [np.int64(6), '% 0.0'],
 'exp_years_total': [np.int64(16), '% 1.0'],
 'exp_years_de': [np.int64(32), '% 3.0'],
 'seniority_lvl': [np.int64(12), '% 1.0'],
 'tech_main': [np.int64(127), '% 10.0'],
 'tech_other': [np.int64(157), '% 13.0'],
 'salary_2020_extras': [np.int64(424), '% 34.0'],
 'salary_2019_noextras': [np.int64(368), '% 29.0'],
 'salary_2019_extras': [np.int64(639), '% 51.0'],
 'vacation_days': [np.int64(68), '% 5.0'],
 'status_employment': [np.int64(17), '% 1.0'],
 'duration_contract': [np.int64(29), '% 2.0'],
 'main_work_language': [np.int64(16), '% 1.0'],
 'company_size': [np.int64(18), '% 1.0'],
 'company_type': [np.int64(25), '% 2.0'],
 'corona_jobloss': [np.int64(20), '% 2.0'],
 'kurzarbeit_weekly_h': [np.int64(880), '% 70.0'],
 'monetary_support': [np.int64(791), '% 63.0']}
 
```

# Outliers

## Numerical Variables

Creating a function to clean and convert categorical variables into quantitive ones, since some categorical ones should be numerical ones:

```python
def clean_and_convert_to_numeric(df, column_name):
    """Cleans a column by removing non-numeric characters and converts it to numeric."""
    # Remove any non-numeric characters (except decimal points and hyphens)
    df[column_name] = df[column_name].astype(str).str.replace(r'[^\d.-]', '', regex=True)
    # Convert to numeric, setting errors='coerce' will turn non-convertible values into NaN
    df[column_name] = pd.to_numeric(df[column_name], errors='coerce')
    return df

columns_to_clean = ['exp_years_total', 'exp_years_de', 'salary_2020_extras', 'vacation_days', 'salary_2019_noextras']

for col in columns_to_clean:
    df = clean_and_convert_to_numeric(df, col)

# Check the info again to see the data types
df.info()
```


Detecting outliers using visual methods for columns: 'age', 'exp_years_total', 'exp_years_de', 'salary_2020_noextras', 'salary_2020_extras', 'vacation_days'

```python
dists = ['age', 'exp_years_total', 'exp_years_de', 'salary_2020_noextras', 'salary_2020_extras', 'vacation_days', 'salary_2019_noextras']

for col in dists:
  plt.figure(figsize=(8, 6))
  sns.boxplot(x=df[col])
  plt.title(f'Box plot of {col}')
  plt.show()
```

### Observations

From looking at boxplots:

age: Outliers above age ~43/44
exp_years_total: Many outliers close to non-outlier-max still < 50, and some wrong values > 100
exp_years_de: local maximum slighly over 10, outliers up to ~50
salary_2020_noextras: huge outlier at ~100000000000 that distorts the whole boxplot
salary_2020_extras: huge outlier at ~5000000000 that distorts the whole boxplot
vacation_days: outliers in both direction, from 0 to local_min, and from local_max to over 350
salary_2019_noextras: one huge outlier at ~100000000 that distorts the whole boxplot

### Actions

Removing outliers, ot capping/replacing and  with a logical maximum value

```python

# exp_years_total (anything above 50 gets the max value under 50)
max_below_50 = df.loc[df['exp_years_total'] <= 50, 'exp_years_total'].max()
df.loc[df['exp_years_total'] > 50, 'exp_years_total'] = max_below_50

# salary_2020_noextras (replacing the 3 highest values and replace with 4th highest value)
fourth_highest_salary_noextras = df['salary_2020_noextras'].nlargest(4).iloc[-1]
highest_salaries_noextras = df['salary_2020_noextras'].nlargest(3).index
df.loc[highest_salaries_noextras, 'salary_2020_noextras'] = fourth_highest_salary_noextras

# salary_2020_extras (replace max value with second highest value)
second_highest_salary_extras = df['salary_2020_extras'].nlargest(2).iloc[-1]
highest_salary_extras_index = df['salary_2020_extras'].nlargest(1).index
df.loc[highest_salary_extras_index, 'salary_2020_extras'] = second_highest_salary_extras

# vacation_days (replace the two second highest values with third highest value)
fourth_highest_vacation_days = df['vacation_days'].nlargest(4).iloc[-1]
top_three_indices = df['vacation_days'].nlargest(3).index
df.loc[top_three_indices, 'vacation_days'] = fourth_highest_vacation_days


# Removing 2019 salary outlier of 50000000
df = df.drop(df[df['salary_2019_noextras'] >= 10000000].index)
df = df.drop(df[df['salary_2019_noextras'] == '-'].index)
```

Then creating histograms to have a 2nd look:

```python
cols_to_plot = ['exp_years_total', 'salary_2020_noextras', 'salary_2020_extras', 'vacation_days', 'salary_2019_extras']

for col in cols_to_plot:
    plt.figure(figsize=(8, 6))
    ax = sns.histplot(df[col], kde=True).axes # Get the axes object
    plt.title(f'Histogram of {col} after outlier replacement')
    # Use ScalarFormatter for the x-axis
    formatter = ScalarFormatter()
    formatter.set_scientific(False)
    ax.xaxis.set_major_formatter(formatter)
    plt.show()
```

exp_years_total: looking ok, like a lightly left skewed gaussian. Makes sense given the context
salary_2020_noextras: looks good,  normal distribution
salary_2020_extras: still having outliers, and most people have 0 bonus
vacation_days: 
salary_2019_extras: better visibility, still have some unique with ~3x higher  bonus compared to the "normal zone" but this still makes sense

# Univariate Analysis

## Quantitative Variables

Checking for central tendencies and spread

```python
from scipy.stats import iqr

for col in dists:
  if col in df.columns:
    print(f"\nAnalysis for column: {col}")

    # Central Tendencies
    mean_val = df[col].mean()
    median_val = df[col].median()
    print(f"  Mean: {mean_val:.3f}")
    print(f"  Median: {median_val:.3f}")

    # Spread
    std_dev = df[col].std()
    iqr_val = iqr(df[col].dropna()) # IQR requires no NaN values
    print(f"  Standard Deviation: {std_dev:.3f}")
    print(f"  IQR: {iqr_val:.3f}")
  else:
    print(f"\nColumn '{col}' not found in the DataFrame.")
```

Output:
```
Analysis for column: age
  Mean: 32.510
  Median: 32.000
  Standard Deviation: 5.664
  IQR: 6.000
  Comment: Looking fine and logical

Analysis for column: exp_years_total
  Mean: 8.871
  Median: 8.000
  Standard Deviation: 5.504
  IQR: 7.000
  Comment: IQR > SD indicated we have skewed data or heavy tails

Analysis for column: exp_years_de
  Mean: 3.966
  Median: 3.000
  Standard Deviation: 4.310
  IQR: 4.000
  Comment: IQR < SD indicates we still have some outliers or tails

Analysis for column: salary_2020_noextras
  Mean: 71580.489
  Median: 70000.000
  Standard Deviation: 26765.088
  IQR: 21200.000

Analysis for column: salary_2020_extras
  Mean: 15063.370
  Median: 0.000
  Standard Deviation: 54903.390
  IQR: 9400.000
  Comment: IQR << SD indicating heavy outliers or tails (most get 0)

Analysis for column: vacation_days
  Mean: 28.021
  Median: 28.000
  Standard Deviation: 3.869
  IQR: 3.000

Analysis for column: salary_2019_noextras
  Mean: 632245.872
  Median: 65000.000
  Standard Deviation: 16805081.752
  IQR: 20000.000
  Comment: IQR << SD indicating heavy outliers or tails (maybe capping wasnt the best approach VS dropping)
```

### Cleaning up

```python
# Removing final outliers that make little sense or just disturbs the graph visually
df = df.drop(df[df['vacation_days'] < 10].index)
df = df.drop(df[df['salary_2020_extras'] > 200000].index)
df = df.drop(df[df['salary_2020_noextras'] > 175000].index)
df = df.drop(df[df['exp_years_de'] > 30].index)
df = df.drop(df[df['exp_years_total'] >= 25].index)
df = df.drop(df[df['age'] >= 50].index)
```

## Categorical Variables

Looking at unique values with

```python
print("gender: ", df["gender"].unique())
print("\ncity: ", df["city"].unique())
print("\nposition: ", df["position"].unique())
print("\nseniority_lvl: ", df["seniority_lvl"].unique())
print("\ntech_main: ", df["tech_main"].unique())
print("\ntech_other: ", df["tech_other"].unique())
print("\nvacation_days: ", df["vacation_days"].unique())
print("\nstatus_employment: ", df["status_employment"].unique())
print("\nduration_contract: ", df["duration_contract"].unique())
print("\nmain_work_language: ", df["main_work_language"].unique())
print("\ncompany_size: ", df["company_size"].unique())
print("\ncompany_type: ", df["company_type"].unique())
```

Creating frequency tables and frequency plot with

```python
# Frequency Table & Bar Charts

categorical_cols = [
    'gender',
    'city',
    'position',
    'seniority_lvl',
    'tech_main',
    'tech_other',
    'status_employment',
    'duration_contract',
    'main_work_language',
    'company_size',
    'company_type'
]

for col in categorical_cols:
    if col in df.columns:
        print(f"\nFrequency Table for '{col}':")
        freq_table = df[col].value_counts()
        print(freq_table)

        plt.figure(figsize=(12, 6))
        freq_table.plot(kind='bar')
        plt.title(f'Frequency of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    else:
        print(f"\nColumn '{col}' not found in the DataFrame.")
```

### gender

We see: 
- Male: 700
- Female: 117
- Diverse: 2

we could replace the 2 diverse genders with the variables mode (male), or remove them if those lines are problematic

looking at ALL columns of these two with (without pandas replacing columns with "...")

```python
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 120) # Widen display for better column layout
print(df[df['gender'] == 'Diverse'].to_string())
```

```
318  24/11/2020 17:03:03 33.000  Diverse  Hamburg  Software Engineer            1.000         6.000        Middle     Scala  Python, SQL, Kubernetes, Docker            130000.000                   0                   NaN                NaN            NaN  Full-time employee  Unlimited contract            English        1000+      Product             No                  NaN              NaN
727  26/11/2020 05:53:19 22.000  Diverse  Cologne        QA Engineer            1.000         1.000          Head     Cobol                             Perl            159000.000               35000             98000.000              23000         45.000  Full-time employee  Unlimited contract             German        1000+      Product             No               30.000             2000

```

We replace their gender with module of gender:
```python
df.loc[df['gender'] == 'Diverse', 'gender'] = df['gender'].mode()[0]
```

### tech_main and tech_other

Looking into tech_main and tech_others. We see some values are single-values and others are seperated (comma, slash, semicolon) values. Thinking forward i think it would make sense to One-Hot Encode those columns or more precisely Multi-Label Binarization or Feature Extraction, by converting the single-choice into a multi-label option over multiple binary columns.

#### Do we combine the values from main and other tech, or keep them seperate?

Combining:

Pros:
- Simplicity: Creates one unified set of skill features (e.g., has_python, has_aws).
- Comprehensive: Captures the person's full tech stack in one place.
Cons:
- We lose the important context of whether a technology is a primary, core skill or a secondary, frequently used one. A person whose main tech is 'python' is likely different from someone whose main tech is 'java' but who also uses 'python' for scripting.

Keeping them separate:

Pros:
- Preserves Context: A future model could distinguish between someone who is a primary Python developer (main_has_python=1, other_has_python=0) versus a Java developer who also uses Python (main_has_java=1, other_has_python=1). This could be very rich information.
- More Granular Insights allows for more complex patterns to be learned. For example, maybe "main" AWS users have much higher salaries than "other" AWS users.
Cons:
- This will create twice as many columns, which can be a consideration for some simpler models.
#### Decision
I decide for keeping them seperate, while it might introduce the "curse of dimensionality" for simpler models, the risks are manageable with the right choice of model. Using a tree-based algorithm like XGBoost or Random Forest should be able to handle this.

#### Action

Looking into the frequency of each technology/programming language

```python
# Counting occurences for tech_main and tech_other

import re
from collections import Counter

def get_tech_frequencies(tech_column: pd.Series) -> pd.Series:

    tech_counter = Counter()
    for entry in tech_column.dropna():
        technologies = re.split(r'[,/;]', str(entry))
        cleaned_techs = [tech.strip().lower() for tech in technologies if tech and tech.strip()]
        tech_counter.update(cleaned_techs)
        
    if not tech_counter: # Handle case where column is all empty
        return pd.Series(dtype=int)
        
    return pd.Series(tech_counter).sort_values(ascending=False)

main_tech_frequencies = get_tech_frequencies(df['tech_main'])
other_tech_frequencies = get_tech_frequencies(df['tech_other'])

main_df = main_tech_frequencies.reset_index()
main_df.columns = ['Main Tech', 'Main Freq']

other_df = other_tech_frequencies.reset_index()
other_df.columns = ['Other Tech', 'Other Freq']


comparison_df = pd.concat([main_df, other_df], axis=1)


print("--- Full Frequency Counts of Technologies ---")

# This is the key part to prevent truncation
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 120) # Widen display for better column layout

print(comparison_df.to_string(index=False)) # .to_string() gives a clean text output
```

I see that many values exist only once or other single-digit numbers. I decide to only create columns for values with a frequency of at least 10
```python
# --- 1. Function to get frequencies from a column ---

def get_tech_frequencies(tech_column: pd.Series) -> pd.Series:
    """
    Reads a pandas Series, splits/cleans strings, and returns frequency counts.
    """
    tech_counter = Counter()
    for entry in tech_column.dropna():
        technologies = re.split(r'[,/;]', str(entry))
        cleaned_techs = [tech.strip().lower() for tech in technologies if tech and tech.strip()]
        tech_counter.update(cleaned_techs)
    if not tech_counter:
        return pd.Series(dtype=int)
    return pd.Series(tech_counter).sort_values(ascending=False)

# --- 2. Identifying keywords based on (combined, main + other) count >= 10 ---

# Get frequencies for each column separately
main_freqs = get_tech_frequencies(df['tech_main'])
other_freqs = get_tech_frequencies(df['tech_other'])

# Combining the two frequency lists to get a total count.
# .add() is used to sum them, fill_value=0 handles cases where a tech is in one list but not the other.
total_freqs = main_freqs.add(other_freqs, fill_value=0)

# Applying filter: count >= 10
frequent_techs = total_freqs[total_freqs >= 10]

# Removing 'nan' values
if 'nan' in frequent_techs:
    frequent_techs = frequent_techs.drop('nan')

# Final list of keywords to create columns for
keywords_to_create = frequent_techs.index.tolist()


# --- 3. Creating new binary columns in the DataFrame ---

# Creating normalized, lowercase versions of the tech columns for consistency.
# .fillna('') for avoiding error for rows with missing info.

df['tech_main_norm'] = df['tech_main'].str.lower().fillna('')
df['tech_other_norm'] = df['tech_other'].str.lower().fillna('')

# Looping through our final list of important keywords
for tech in keywords_to_create:
    # We must escape characters that have special meaning in regex, like '+' or '#'
    safe_tech_regex = re.escape(tech)
    
    # `\b` ensures we match whole words only (e.g., 'r' doesn't match inside 'react')
    regex_pattern = r'\b' + safe_tech_regex + r'\b'

    # Creating the 'main_has_*' columns
    df[f'main_has_{tech}'] = df['tech_main_norm'].str.contains(regex_pattern, regex=True).astype(int)
    
    # Creating the 'other_has_*' columns
    df[f'other_has_{tech}'] = df['tech_other_norm'].str.contains(regex_pattern, regex=True).astype(int)

# --- 4. Final Cleanup and Display ---

# Dropping the temporary columns (no longer needed)
df.drop(columns=['tech_main_norm', 'tech_other_norm'], inplace=True)
```

# Bivariate and Multivariate Analysis

```python
# Creating a pairplot for the quantitative variables

sns.pairplot(df[dists].dropna()) # Using dropna to handle missing values for plotting
plt.suptitle('Pairwise Scatter Plots of Quantitative Variables', y=1.02) # Add a suptitle above the grid
plt.show()
```

seeing a slight positive correlation between age and both salary_2020_extras and salary_2020_noextras 