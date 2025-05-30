
# Anyblock list to mindmad in root to leaf format
[listroot(root((From Here)))|list2mindmap]
- To dein Tande
- To dein Mudda Sein Gesicht
	- Deine Schwesda
		- JAJ::icon(WTF)

# Anyblock Table with title

[2table|#MY THICK `TITLE`]
- Was ist das
	- JA
	- DaS
	- IST
- KACK
	- PIPI
	- FLOTZTI
	- > 123456

# Anyblock fixed height scrollable codeblock (optional to add height in px in parenthesis, 460 is default height)
[scroll(460)]
```python

import matplotlib.pyplot as plt
import numpy as np

def generate_quadratic_dataset(start=-30, stop=100, num=500, a=2, b=4, c=10, noise_std=50):
    """
    Function that generates a dataset according to a quadratic polynom, with added noise.
    Receives:
        - start (float): minimum value          (defaults to: -30)
        - stop (float): maximum value           (defaults to: 100)
        - num (int): number of elements         (defaults to: 500)
        - a (float): quadratic coefficient      (defaults to: 2)
        - b (float): linear coefficient        evsefaults to: 4)
        - c (float): constant coefficient       (defaults to: 10)
        - noise_std (float): std dev or noise   (defaults to: 50)

    """
    # Creating 500 values between -30 and 500
    x = np.linspace(start, stop, num)

    # Defining a quadratic function
    y = a * x**2 + b * x + c

    # Add random noise with normal distribution (with mean 0, std dev 50)
    noise = np.random.normal(0, noise_std, num)
    y_noise = y + noise

    # reshape(-1, 1) infers the number of rows automatically (-1) and sets 1 column.
    return x, y_noise.reshape(-1, 1)


def plot_quadratic_dataset(data, a=2, b=4, c=10, mode='show'):
    """
    Plot a quadratic dataset with noise and the original quadratic curve.

    Parameters:
    data (tuple): Tuple of (x, y_noisy) from the geometric dataset
    a (float): Quadratic coefficient (default: 2)
    b (float): Linear coefficient (default: 4)
    c (float): Constant term (default: 10)
    """
    x, y_noise = data
    y = a * x**2 + b * x + c

    # Plot
    plt.scatter(x, y_noise.flatten(), s=2, label="Noisy Data")
    plt.plot(x, y, color="red", linewidth=0.5, label="Quadratic (No Noise)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Quadratic Dataset with Noise")
    plt.legend()
    if mode == "save":
        plt.savefig('quadratic_plot.png')
    if mode == "show":
        plt.show()
    return

if __name__ == "__main__":
    dataset = generate_quadratic_dataset()
    plot_quadratic_dataset(dataset)
```

# Anyblock titled blocks

[#My Titld quote block]
> WAS N DAS
> LOL

[#My Titled List]
- First Item
	- Item A
	- Item B
- Second Item
	- Thing C
	- Thing D

# Anyblock codeblock that expands on click
[overfold]
```python

import matplotlib.pyplot as plt
import numpy as np

def generate_quadratic_dataset(start=-30, stop=100, num=500, a=2, b=4, c=10, noise_std=50):
    """
    Function that generates a dataset according to a quadratic polynom, with added noise.
    Receives:
        - start (float): minimum value          (defaults to: -30)
        - stop (float): maximum value           (defaults to: 100)
        - num (int): number of elements         (defaults to: 500)
        - a (float): quadratic coefficient      (defaults to: 2)
        - b (float): linear coefficient        evsefaults to: 4)
        - c (float): constant coefficient       (defaults to: 10)
        - noise_std (float): std dev or noise   (defaults to: 50)

    """
    # Creating 500 values between -30 and 500
    x = np.linspace(start, stop, num)

    # Defining a quadratic function
    y = a * x**2 + b * x + c

    # Add random noise with normal distribution (with mean 0, std dev 50)
    noise = np.random.normal(0, noise_std, num)
    y_noise = y + noise

    # reshape(-1, 1) infers the number of rows automatically (-1) and sets 1 column.
    return x, y_noise.reshape(-1, 1)


def plot_quadratic_dataset(data, a=2, b=4, c=10, mode='show'):
    """
    Plot a quadratic dataset with noise and the original quadratic curve.

    Parameters:
    data (tuple): Tuple of (x, y_noisy) from the geometric dataset
    a (float): Quadratic coefficient (default: 2)
    b (float): Linear coefficient (default: 4)
    c (float): Constant term (default: 10)
    """
    x, y_noise = data
    y = a * x**2 + b * x + c

    # Plot
    plt.scatter(x, y_noise.flatten(), s=2, label="Noisy Data")
    plt.plot(x, y, color="red", linewidth=0.5, label="Quadratic (No Noise)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Quadratic Dataset with Noise")
    plt.legend()
    if mode == "save":
        plt.savefig('quadratic_plot.png')
    if mode == "show":
        plt.show()
    return

if __name__ == "__main__":
    dataset = generate_quadratic_dataset()
    plot_quadratic_dataset(dataset)


```

# Anyblock reveals on mouseover

[X|addClass(ab-deco-heimu)]
- First Item
	- Item A
	- Item B
- Second Item
	- Thing C
	- Thing D

# Anyblock nested structure

[list2tab]
- Creation
	[list2tab]	
	- Conversion
		[list2card|addClass(ab-col3)]
		- Converting Python sequences to NumPy arrays
		  NumPy arrays can be defined using Python sequences such as lists and tuples. Lists and tuples are defined using [...] and (...), respectively. Lists and tuples can define ndarray creation:
		  - a list of numbers will create a 1D array,
		   - a list of lists will create a 2D array,
		   - further nested lists will create higher-dimensional arrays. In general, any array object is called an ndarray in NumPy.
		- np.array()
			  ```python
			  import numpy as np
		   	  a1D = np.array([1, 2, 3, 4])
			  a2D = np.array([[1, 2], [3, 4]])
			  a3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
			 ```

		- The default NumPy behavior is to create arrays in either 32 or 64-bit signed integers<br>(platform dependent and matches C `long` size) or double precision floating point numbers.<br>If you expect your integer arrays to be a specific type, then<br>you need to specify the dtype while you create the array.
	- 1D arrays 
		[list2mdtable]
		- Column 1:
			- Column 2:
				- Column 3:
		- np.arrange() is in col 1
			-  
			  this is col2
	     	  ```python
	     	  import numpy as np
	     	   np.arange(10)
	     	   np.arange(2, 10, dtype=float)
	     	   np.arange(2, 3, 0.1)
	     	   ```   
		     this is another row in col2 
				- col3 sub1
				  > col3 sub2
- tab2
	content2


[list2tab]
- Hi
	- Kein Ding
		- Kasdl
	- Oder
		- ADSasfjasop
	-  LOLOL
		- PEVKVK
			- aADLSFPAS
		- asdasdlkmasdn
- Jo
	- Li
	 ```python
	import pandas as pd
	import numpy as np
	```
		- Ne waslos
		- ;laksd;askd



### Additional Pandas Concepts/Commands to Consider:

[list2card|addClass(ab-col3)]

- **Sorting Data**
    
    - df.sort_values(by, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last')
        
    - df.sort_index(axis=0, level=None, ascending=True, inplace=False, kind='quicksort', na_position='last', sort_remaining=True)
        
    - Use Case: Ordering data for analysis or presentation.
        
- **Descriptive Statistics (More Depth)**
    
    - df.corr(): Compute pairwise correlation of columns.
        
    - df.cov(): Compute pairwise covariance of columns.
        
    - df.nunique(): Count distinct observations.
        
    - df.value_counts(): Return a Series containing counts of unique values.
        
    - df.rank(): Compute numerical data ranks (1 through n) along axis.
        
- **Working with Text Data (.str accessor more detail)**
    
    - .str.get_dummies(): Split strings into dummy/indicator variables.
        
    - More complex regex examples with .str.extractall(), .str.match().
        
- **Working with Dates and Times**
    
    - pd.to_datetime(): Converting strings/numbers to datetime objects.
        
    - DatetimeIndex properties: .dt.year, .dt.month, .dt.day, .dt.dayofweek, .dt.hour, etc.
        
    - df.resample(rule): Resampling time series data (e.g., daily to monthly).
        
    - df.rolling(window): Rolling window calculations (moving average, sum).
        
- **Reshaping Data (More Depth)**
    
    - df.stack(): Pivot a level of the column labels to the row index.
        
    - df.unstack(): Pivot a level of the row index to the column labels.
        
    - pd.melt(): Unpivot a DataFrame from wide to long format.
        
    - pd.get_dummies(): Convert categorical variable into dummy/indicator variables.
        
- **Advanced Indexing**
    
    - df.set_index(keys, drop=True, append=False, inplace=False, verify_integrity=False): Set DataFrame index using existing columns.
        
    - df.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill=''): Reset the index, or a level of it.
        
    - Using pd.IndexSlice for complex MultiIndex slicing.
        
- **Performance & Memory**
    
    - Using Categorical dtype for memory saving and performance with low-cardinality string columns.
        
    - df.memory_usage(deep=True): Get memory usage of each column.
        
    - Efficiently chaining operations to avoid intermediate DataFrames.
        
- **Options and Settings**
    
    - pd.set_option(), pd.get_option(): Control Pandas display options (e.g., display.max_rows, display.max_columns).
        

### Data Science Workflows/Concepts (to integrate Pandas/NumPy/Matplotlib)

[list2card|addClass(ab-col2)]

- **Exploratory Data Analysis (EDA) Workflow**
    
    - A note detailing typical steps: Loading, Inspection, Cleaning (Missing Values, Duplicates, Outliers), Univariate Analysis (histograms, box plots), Bivariate Analysis (scatter plots, correlation), deriving insights.
        
- **Feature Engineering with Pandas**
    
    - Creating new features from existing ones (e.g., binning numerical data, extracting date parts, polynomial features, interaction terms).
        
- **Data Visualization for EDA**
    
    - Using Matplotlib (and Seaborn) with Pandas DataFrames to create insightful plots (histograms, density plots, scatter matrices, heatmaps, box plots per category).
        
- **Basic Data Preprocessing for Machine Learning**
    
    - Scaling/Normalization (MinMaxScaler, StandardScaler - can be done with NumPy/Pandas or Scikit-learn).
        
    - Encoding Categorical Variables (One-Hot Encoding, Label Encoding using Pandas/Scikit-learn).
        
- **Image Processing Workflow (NumPy, Pillow, Matplotlib)**
    
    - Loading images (Pillow) -> NumPy array conversion -> Manipulations (NumPy: cropping, masking, color channel separation, intensity changes) -> Displaying results (Matplotlib).
        

### Matplotlib Advanced Styling & Exotic Plots

[list2card|addClass(ab-col2)]

- **Advanced Styling**
    
    - Customizing spines, ticks, tick labels.
        
    - Using different Matplotlib styles (plt.style.use()).
        
    - Advanced legend customization.
        
    - Adding text, annotations, arrows.
        
    - Working with colormaps in detail.
        
    - Subplot adjustments (plt.tight_layout(), GridSpec).
        
- **Exotic Plots (or more advanced standard plots)**
    
    - **3D Plotting:** Surface plots, 3D scatter, 3D bar charts (mpl_toolkits.mplot3d).
        
    - **Contour Plots:** plt.contour(), plt.contourf().
        
    - **Stream Plots:** plt.streamplot() for vector fields.
        
    - **Violin Plots:** plt.violinplot() (often better with Seaborn).
        
    - **Heatmaps:** plt.imshow() or plt.pcolormesh() for matrix data (Seaborn's heatmap is very popular).
        
    - **Radar Charts (Polar Plots):** Using polar projections.
        
    - **Financial Charts (Candlestick/OHLC):** Using libraries like mplfinance.
        
    - **Interactive Plots:** Using Matplotlib backends like ipympl in Jupyter, or integrating with libraries like Bokeh, Plotly.

```datablock

```