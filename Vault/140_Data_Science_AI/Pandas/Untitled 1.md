```
import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Alice'],
    'Age': [25, 30, 22, 35, 28, 25],
    'Score': [88, 92, 77, 95, 85, 88],
    'City': ['NY', 'SF', 'LA', 'NY', 'SF', 'NY'],
    'Date': pd.to_datetime(['2023-01-01', '2023-01-15', '2023-02-01', '2023-02-10', '2023-03-05', '2023-01-01'])
}
df = pd.DataFrame(data, index=['r1', 'r2', 'r3', 'r4', 'r5', 'r6'])

s = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'], name='MySeries')
```
