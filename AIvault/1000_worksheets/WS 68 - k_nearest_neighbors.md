### **Keywords**

#### 1. Nonparametric

A type of model that does not make any assumptions about the underlying data distribution or functional form.

*   Nonparametric models do not have a fixed number of parameters; the number of parameters often grows with the amount of training data.
*   They are highly flexible and can learn complex, non-linear relationships directly from the data.
*   KNN is a classic example, as its "model" is the entire training dataset itself.
*   This is in contrast to parametric models like Linear or Logistic Regression, which assume a specific form (e.g., a line) and have a fixed number of parameters (the coefficients).

```python
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression

# A simple non-linear dataset
X = np.sort(5 * np.random.rand(40, 1), axis=0)
y = np.sin(X).ravel()
y[::5] += 1 * (0.5 - np.random.rand(8)) # add some noise

# Fit a parametric model (Linear Regression)
linear_model = LinearRegression()
linear_model.fit(X, y)
# The number of parameters is fixed (1 slope, 1 intercept)
print(f"Linear Regression Parameters (slope, intercept): {linear_model.coef_}, {linear_model.intercept_}")


# Fit a non-parametric model (KNN)
knn_model = KNeighborsRegressor(n_neighbors=3)
knn_model.fit(X, y)
# The "parameters" are all 40 data points. If we had 1000 points, it would store all 1000.
print(f"\nKNN Model 'stores' {knn_model.n_samples_fit_} data points as its model.")
```

A nonparametric model offers great flexibility by letting the data speak for itself. Instead of trying to fit the data into a preconceived shape like a straight line, a model like KNN makes predictions based on the local structure of the data. The complexity of the model is not determined beforehand but is a direct function of the complexity of the data provided. This allows it to capture intricate patterns that a parametric model would miss. The trade-off is that nonparametric models typically require more data to perform well and can be more computationally expensive, as seen with KNN where the entire dataset must be stored and referenced for each prediction.

#### 2. Distance

A measure of similarity or dissimilarity between two data points in the feature space.

*   Distance is the core concept of the KNN algorithm; it determines which points are considered "neighbors."
*   The most common distance metric is **Euclidean Distance** (the straight-line distance between two points).
*   Other metrics include **Manhattan Distance** (sum of absolute differences) and **Minkowski Distance** (a generalization of both).
*   The choice of distance metric can significantly impact the model's performance and depends on the nature of the data.

```python
import numpy as np

# Two data points (vectors) with 3 features each
point_A = np.array([2, 5, 3])
point_B = np.array([8, 2, 6])

# --- Calculate Euclidean Distance ---
# Formula: sqrt( (x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2 )
euclidean_distance = np.linalg.norm(point_A - point_B)
# Or manually: np.sqrt(np.sum((point_A - point_B)**2))
print(f"Point A: {point_A}")
print(f"Point B: {point_B}")
print(f"Euclidean Distance: {euclidean_distance:.4f}")

# --- Calculate Manhattan Distance ---
# Formula: |x2-x1| + |y2-y1| + |z2-z1|
manhattan_distance = np.sum(np.abs(point_A - point_B))
print(f"Manhattan Distance: {manhattan_distance}")
```

In KNN, "closeness" is synonymous with "similarity." The distance metric is the mathematical formalization of this idea. Euclidean distance is the most intuitive and widely used metric, corresponding to the real-world concept of distance. However, it may not always be the best choice. For instance, in high-dimensional spaces, Manhattan distance can sometimes be more robust because it is less affected by the "curse of dimensionality." For categorical data, other metrics like the Hamming distance (which counts the number of positions at which the corresponding symbols are different) would be used. The effectiveness of the KNN algorithm is fundamentally tied to the chosen distance metric's ability to accurately represent the true similarity between data points.

#### 3. Statistical Consistency

A property of an estimator ensuring that as the amount of data grows infinitely large, the estimator's predictions converge to the true, optimal value.

*   For KNN classification, consistency means that as the number of data points `n` approaches infinity, the error rate of the KNN classifier approaches the error rate of the ideal Bayes classifier (the theoretical best possible classifier).
*   This property holds for KNN under mild assumptions about the data distribution.
*   It provides a theoretical guarantee that with enough data, KNN can approximate the best possible prediction function.
*   This is a powerful theoretical justification for using a relatively simple algorithm like KNN.

```python
# This is a theoretical concept, but we can simulate it.
# We'll show that as n increases, the KNN error on a test set decreases.
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generate a large dataset
X, y = np.random.rand(10000, 2), np.random.randint(0, 2, 10000)
X_train_full, X_test, y_train_full, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

sample_sizes = [100, 500, 1000, 4000, 8000]
accuracies = []

print("Simulating statistical consistency:")
for n in sample_sizes:
    # Use a subset of the full training data
    X_subset = X_train_full[:n]
    y_subset = y_train_full[:n]

    # Train KNN on the subset
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_subset, y_subset)

    # Evaluate on the fixed test set
    y_pred = knn.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    accuracies.append(acc)
    print(f"Training with n={n:4d}, Test Accuracy: {acc:.4f}")
```

Statistical consistency is a crucial concept from statistical learning theory that gives us confidence in an algorithm. It essentially says, "If you give me enough data, I will eventually get very close to the best possible answer." For KNN, the proof (by Cover and Hart, 1967) showed that the error rate of a 1-NN classifier is at most twice the error of the optimal Bayes classifier. As `k` also grows (but slower than `n`), the KNN error rate converges *exactly* to the Bayes error rate. This is a remarkable result because it means this simple, nonparametric method has the theoretical power to be just as good as any other classifier, including very complex ones, provided it is given a sufficient amount of data.

#### 4. Data Reduction

A preprocessing technique for KNN that aims to reduce the size of the stored training dataset without significantly hurting prediction accuracy.

*   The goal is to speed up prediction time, as standard KNN has to compare a new point to every point in the training set.
*   It works by identifying and keeping only the most "important" or "prototypical" samples and discarding the rest.
*   One common method is **Condensed Nearest Neighbor (CNN)**, which iteratively builds a subset of data that can still correctly classify the original full dataset.
*   This creates a smaller, more efficient model but may result in a slight decrease in accuracy.

```python
# imblearn provides implementations for many data reduction techniques
# pip install imbalanced-learn
from sklearn.datasets import make_classification
from imblearn.under_sampling import CondensedNearestNeighbour
import pandas as pd

# Generate data
X, y = make_classification(n_samples=1000, n_features=5, n_redundant=0,
                           n_informative=2, n_clusters_per_class=1, random_state=42)

print(f"Original dataset size: {X.shape[0]} samples")

# Initialize the data reduction algorithm
# It will select a subset of the data
cnn = CondensedNearestNeighbour(n_neighbors=1, random_state=42)
X_reduced, y_reduced = cnn.fit_resample(X, y)

print(f"Reduced dataset size after CNN: {X_reduced.shape[0]} samples")
print(f"Data reduction of {100 * (1 - X_reduced.shape[0]/X.shape[0]):.2f}%")
# A KNN model trained on this reduced set would be much faster at prediction.
```

Data reduction directly tackles KNN's biggest weakness: its slow prediction time on large datasets. The core idea is that not all training points are equally valuable. Many points might be deep inside a dense cluster of their own class, far from the decision boundary. These points are redundant; their removal would not change the classification of new points near the boundary. Data reduction algorithms formalize this by trying to find the smallest possible subset of the training data (a set of "prototypes") that is sufficient to maintain the decision boundary. The Condensed Nearest Neighbor (CNN) algorithm, for example, starts with one point and adds other points from the original dataset only if they are misclassified by the current prototype set. The result is a much smaller dataset that can be used to train a faster KNN model.

#### 5. Locality-Sensitive Hashing

An approximate nearest neighbor search technique used to dramatically speed up querying in high-dimensional spaces.

*   **LSH** is a hashing method that aims to ensure that similar items have a high probability of being hashed into the same "bucket."
*   Instead of comparing a query point to all other points, you only compare it to the points in the same bucket.
*   This changes the search problem from a linear scan (slow) to a sub-linear lookup (fast).
*   It is an *approximate* method, meaning it might not always find the absolute nearest neighbor, but it provides a good trade-off between speed and accuracy for very large datasets.

```python
# scikit-learn has an LSHForest implementation for finding approximate neighbors
# Note: LSHForest is deprecated in recent versions, but the concept is key.
# We'll demonstrate the idea conceptually.
from sklearn.neighbors import LSHForest
import numpy as np

# Create a large, high-dimensional dataset
X = np.random.rand(10000, 100)

# Set up the LSH Forest
# It will build a data structure based on hashing
lshf = LSHForest(n_estimators=20, random_state=42)
lshf.fit(X)

# A new query point
query_point = np.random.rand(1, 100)

# Find the 5 approximate nearest neighbors
# This is much faster than a brute-force search
distances, indices = lshf.kneighbors(query_point, n_neighbors=5)

print("Finding approximate nearest neighbors using LSH:")
print(f"Indices of 5 nearest neighbors: {indices[0]}")
print(f"Distances to these neighbors: {distances[0]}")
```

Locality-Sensitive Hashing is a clever solution to the curse of dimensionality and the slow prediction time of KNN. The intuition is simple: if we can design a "smart" hashing function that maps similar points to the same hash code, then to find neighbors for a query point, we just need to hash it and look at the other points that produced the same hash code. This avoids the need to compute distances to every single point in the dataset. LSH is a probabilistic method; it doesn't guarantee finding the true nearest neighbor. However, by using multiple hash tables, the probability of finding the true neighbors can be made arbitrarily high, providing an excellent practical solution for applying KNN-like ideas to massive, high-dimensional datasets where exact methods are computationally infeasible.

***

### **Questions**

#### 1. What is the best k value for kNN?

There is no single "best" k value; the optimal k is dependent on the specific dataset and must be tuned as a hyperparameter.

*   **Small k (e.g., k=1):** The model is highly flexible and can capture fine-grained details. This leads to low bias but high variance, making it very sensitive to noise and prone to overfitting. The decision boundary will be very jagged.
*   **Large k (e.g., k=n):** The model is very smooth and inflexible. It will predict the majority class of the entire dataset for every point. This leads to high bias but low variance (underfitting).
*   **The Trade-off:** The best k value is one that finds a balance between overfitting and underfitting.
*   **Finding k:** The optimal k is typically found using cross-validation, where you test a range of k values and select the one that yields the best performance on the validation set.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# Generate data
X, y = make_classification(n_samples=500, n_features=10, n_informative=5,
                           n_redundant=0, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Test a range of k values using cross-validation
k_range = range(1, 31)
k_scores = []

for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    # Use 5-fold cross-validation on the training data
    scores = cross_val_score(knn, X_train_scaled, y_train, cv=5, scoring='accuracy')
    k_scores.append(scores.mean())

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(k_range, k_scores)
plt.xlabel('Value of K for KNN')
plt.ylabel('Cross-Validated Accuracy')
plt.title('Finding the Optimal K')
plt.grid(True)
plt.show()

# Find the k with the highest score
optimal_k = k_range[np.argmax(k_scores)]
print(f"The optimal value for k is approximately: {optimal_k}")
```

The choice of `k` is the most critical hyperparameter for the KNN algorithm, as it directly controls the bias-variance trade-off. A model with `k=1` is the most complex KNN model possible; its decision boundary will be a perfect tessellation around every single training point. This will result in 100% accuracy on the training data but will likely perform poorly on new data because it has fit the noise. As `k` increases, the decision boundary becomes smoother and the model becomes less sensitive to individual noisy points. The plot generated by the code is a classic "elbow" curve. The accuracy typically rises sharply as `k` moves away from 1 (reducing overfitting), peaks at an optimal value, and then gradually decreases as `k` becomes too large and the model starts to underfit. Cross-validation is the standard and most reliable method for finding this "sweet spot."

#### 2. How can you prevent overfitting with this algorithm?

You can prevent overfitting in KNN by choosing a larger value for k and using cross-validation to find the optimal value.

*   **Overfitting in KNN:** Overfitting occurs when `k` is too small. A `k=1` model, for example, is perfectly fit to the training data, including its noise, leading to poor generalization.
*   **Increasing k:** As you increase `k`, the prediction for a new point is based on a larger, more stable neighborhood of points. This makes the model's decision boundary smoother and less susceptible to the influence of individual noisy data points.
*   **Cross-Validation:** This is the key technique. By evaluating the model's performance on unseen validation data for different values of `k`, you can identify the point where the model generalizes best, avoiding both overfitting (at low `k`) and underfitting (at high `k`).
*   **Feature Selection/Dimensionality Reduction:** In high-dimensional spaces, all points can appear far apart. Reducing the number of features to only the most relevant ones can help the distance metric be more meaningful and reduce the risk of overfitting to noise in irrelevant dimensions.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.neighbors import KNeighborsClassifier
from matplotlib.colors import ListedColormap

# Generate noisy data
X, y = make_moons(n_samples=200, noise=0.3, random_state=42)

# Function to plot decision boundary
def plot_decision_boundary(clf, X, y, title):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, alpha=0.4, cmap=ListedColormap(('red', 'blue')))
    plt.scatter(X[:, 0], X[:, 1], c=y, s=20, edgecolor='k', cmap=ListedColormap(('red', 'blue')))
    plt.title(title)

# --- Overfitting Model (k=1) ---
knn_overfit = KNeighborsClassifier(n_neighbors=1)
knn_overfit.fit(X, y)

# --- More Robust Model (k=15) ---
knn_robust = KNeighborsClassifier(n_neighbors=15)
knn_robust.fit(X, y)

# Plotting
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plot_decision_boundary(knn_overfit, X, y, "Overfitting (k=1)")

plt.subplot(1, 2, 2)
plot_decision_boundary(knn_robust, X, y, "More Robust (k=15)")
plt.show()
```

The visualization clearly shows how a small `k` leads to overfitting. The decision boundary for `k=1` is extremely complex and jagged, creating little "islands" to perfectly classify every single noisy point in the training set. This model has high variance. In contrast, the model with `k=15` has a much smoother decision boundary. It ignores the individual noisy points and captures the broader, underlying structure of the "moons." This model has lower variance and will generalize much better to new, unseen data. Therefore, increasing `k` is the primary mechanism for adding regularization to a KNN model and preventing it from overfitting.

#### 3. Does changing the type of distance really have an impact?

Yes, changing the type of distance metric can have a significant impact, especially depending on the dimensionality and nature of the data.

*   **Euclidean Distance (L2 norm):** This is the default and most intuitive choice, representing the shortest straight-line path between two points. It works well in low-dimensional spaces.
*   **Manhattan Distance (L1 norm):** This measures distance by summing the absolute differences along each axis (like navigating a city grid). It can be more robust than Euclidean distance in high-dimensional spaces because it is less sensitive to large differences in a single dimension.
*   **Minkowski Distance:** This is a generalized metric. With parameter `p=1`, it is the Manhattan distance. With `p=2`, it is the Euclidean distance. You can tune `p` as a hyperparameter.
*   **Impact:** The choice of metric changes the shape of the "neighborhood" around a point. A different neighborhood shape can lead to different points being selected as neighbors, thus changing the final prediction.

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load Iris dataset
iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Scale data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# --- Model with Euclidean Distance ---
knn_euclidean = KNeighborsClassifier(n_neighbors=5, metric='euclidean') # or 'minkowski' with p=2
knn_euclidean.fit(X_train_scaled, y_train)
y_pred_euclidean = knn_euclidean.predict(X_test_scaled)
acc_euclidean = accuracy_score(y_test, y_pred_euclidean)
print(f"Accuracy with Euclidean Distance: {acc_euclidean:.4f}")

# --- Model with Manhattan Distance ---
knn_manhattan = KNeighborsClassifier(n_neighbors=5, metric='manhattan') # or 'minkowski' with p=1
knn_manhattan.fit(X_train_scaled, y_train)
y_pred_manhattan = knn_manhattan.predict(X_test_scaled)
acc_manhattan = accuracy_score(y_test, y_pred_manhattan)
print(f"Accuracy with Manhattan Distance: {acc_manhattan:.4f}")
```

While Euclidean distance is the standard, its properties can become problematic in high dimensions. As the number of dimensions (`d`) increases, the concept of "close" and "far" becomes less distinct. The ratio of the distance to the nearest neighbor and the farthest neighbor approaches 1, meaning all points appear to be roughly equidistant. This makes it hard to find a meaningful neighborhood. Manhattan distance, by summing absolute differences, is sometimes less affected by this phenomenon. It considers the total path along the feature axes rather than the "as the crow flies" distance. For this reason, when working with high-dimensional data, it is always worth experimenting with different distance metrics (like Manhattan or other L_p norms) as it can sometimes lead to a noticeable improvement in model performance.

#### 4. Explain how kNN can be used to identify outliers.

KNN can be used to identify outliers by assuming that outliers are data points that are far away from the rest of the data, meaning their nearest neighbors will be unusually distant.

*   **The Principle:** A normal data point will have a dense neighborhood with small distances to its k-neighbors. An outlier, by definition, is isolated and will have a much larger average distance to its k-neighbors.
*   **Method 1 (Average Distance):** For each data point, calculate the average distance to its `k` nearest neighbors. Points with a significantly higher average distance than the rest can be flagged as outliers.
*   **Method 2 (Distance to k-th Neighbor):** A simpler variant is to just use the distance to the `k`-th nearest neighbor as the outlier score. A large distance implies the point is in a sparse region.
*   This is an unsupervised technique, as it doesn't require pre-labeled data.

```python
import numpy as np
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt

# Create some normally distributed data
X_normal = np.random.randn(100, 2)
# Add some clear outliers
X_outliers = np.array([[5, 5], [-4, 6], [3, -5]])
# Combine them
X = np.vstack([X_normal, X_outliers])

# Use NearestNeighbors to find distances to the k neighbors
k = 5
nbrs = NearestNeighbors(n_neighbors=k)
nbrs.fit(X)
distances, indices = nbrs.kneighbors(X)

# Calculate the average distance to the k neighbors for each point
avg_distances = np.mean(distances, axis=1)

# Set a threshold for identifying outliers (e.g., based on a percentile)
threshold = np.percentile(avg_distances, 95)
outlier_indices = np.where(avg_distances > threshold)[0]

# Plotting
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c='blue', label='Inliers')
plt.scatter(X[outlier_indices, 0], X[outlier_indices, 1], c='red', s=100, label='Detected Outliers')
plt.title("Outlier Detection using KNN Average Distance")
plt.legend()
plt.grid(True)
plt.show()

print(f"Threshold for outlier detection: {threshold:.4f}")
print(f"Indices of detected outliers: {outlier_indices}")
```

This distance-based approach is a simple yet effective method for anomaly detection. The `sklearn.neighbors.NearestNeighbors` object is a perfect tool for this, as its purpose is to efficiently find neighbors and their distances without performing a classification or regression task. By calculating an "outlier score" for each point (like the average distance to its neighbors), we can then set a threshold to separate the normal points from the abnormal ones. A common way to set this threshold is to use a percentile (e.g., any point whose score is in the top 5% is considered an outlier) or to use a statistical rule, like any point whose score is more than three standard deviations away from the mean score.

#### 5. Is kNN a classifier or a regressor?

KNN is a versatile algorithm that can be used for both classification and regression tasks.

*   The core mechanism of finding the `k` nearest neighbors is the same for both tasks.
*   The difference lies in the final prediction step after the neighbors have been identified.
*   **For Classification:** The prediction is the **majority class** (mode) among the `k` neighbors. If `k=5` and three neighbors are Class A and two are Class B, the prediction is Class A.
*   **For Regression:** The prediction is the **average (mean)** of the target values of the `k` neighbors. If the target values of the 5 neighbors are, the prediction is 12.2.

```python
from sklearn.datasets import load_iris, fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.metrics import accuracy_score, mean_squared_error

# --- KNN for Classification ---
iris = load_iris()
X_c, y_c = iris.data, iris.target
X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(X_c, y_c, test_size=0.3, random_state=42)

knn_classifier = KNeighborsClassifier(n_neighbors=5)
knn_classifier.fit(X_train_c, y_train_c)
y_pred_c = knn_classifier.predict(X_test_c)
print(f"--- KNN as a Classifier ---")
print(f"Task: Predict Iris species (a class)")
print(f"Accuracy: {accuracy_score(y_test_c, y_pred_c):.4f}")


# --- KNN for Regression ---
housing = fetch_california_housing()
X_r, y_r = housing.data, housing.target
X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(X_r, y_r, test_size=0.3, random_state=42)

knn_regressor = KNeighborsRegressor(n_neighbors=5)
knn_regressor.fit(X_train_r, y_train_r)
y_pred_r = knn_regressor.predict(X_test_r)
print(f"\n--- KNN as a Regressor ---")
print(f"Task: Predict house price (a continuous value)")
print(f"Mean Squared Error: {mean_squared_error(y_test_r, y_pred_r):.4f}")
```

The adaptability of KNN to both task types makes it a very intuitive algorithm to learn. The fundamental principle of "learning from your neighbors" applies equally well whether you are trying to categorize something or estimate a numerical value. In scikit-learn, this duality is handled by two separate but closely related classes: `KNeighborsClassifier` and `KNeighborsRegressor`. They share many of the same parameters (`n_neighbors`, `metric`, `algorithm`) because the neighbor-finding part of the process is identical. The only thing that changes is the final aggregation step: a vote for classification, an average for regression.

#### 6. Can kNN assist with time series data?

Yes, KNN can be used for time series forecasting, but it requires transforming the time series problem into a standard supervised learning format first.

*   **The Challenge:** KNN does not inherently understand the temporal ordering of data. It only understands distances in a feature space.
*   **The Transformation:** You must create a feature set (X) and a target (y) from the time series. This is typically done by using lagged values of the series as features. For example, to predict the value at time `t`, you could use the values at `t-1`, `t-2`, and `t-3` as features.
*   **The Process:** Once the data is in this `(X, y)` format, you can apply the KNN regressor just like any other supervised learning problem. A new prediction is made by finding historical "windows" (the lagged features) that are most similar to the current window.
*   This approach is a form of "univariate" forecasting, as it only uses past values of the series itself.

```python
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt

# Create a sample time series (e.g., sine wave)
time = np.arange(0, 100, 0.5)
series = np.sin(time * 0.1) + np.random.randn(len(time)) * 0.1

# --- Transform the time series into a supervised learning problem ---
def create_lagged_dataset(data, n_lags=1):
    X, y = [], []
    for i in range(len(data) - n_lags):
        X.append(data[i:i + n_lags])
        y.append(data[i + n_lags])
    return np.array(X), np.array(y)

n_lags = 5
X, y = create_lagged_dataset(series, n_lags)

# Use the last 20% of the data for "testing"
split_point = int(len(X) * 0.8)
X_train, y_train = X[:split_point], y[:split_point]
X_test, y_test = X[split_point:], y[split_point:]

# --- Apply KNN Regressor ---
knn_ts = KNeighborsRegressor(n_neighbors=5)
knn_ts.fit(X_train, y_train)
y_pred = knn_ts.predict(X_test)

# Plotting the forecast
plt.figure(figsize=(12, 6))
plt.plot(time, series, label='Original Series')
plt.plot(time[split_point + n_lags:], y_pred, 'r--', label='KNN Forecast')
plt.title("KNN for Time Series Forecasting")
plt.legend()
plt.show()
```

Using KNN for time series is a powerful, non-parametric approach. Unlike classical models like ARIMA which make strong assumptions about the data's statistical properties, KNN makes no such assumptions. It simply finds past patterns of behavior that are similar to the most recent pattern and assumes the future will evolve in a similar way. The key to success is the feature engineering step—creating the lagged dataset. The number of lags (`n_lags`) becomes a critical hyperparameter, similar to `k`. Too few lags might not capture enough of the pattern, while too many can introduce noise and fall victim to the curse of dimensionality.

#### 7. Can you calculate and visualize the classifier's decision boundary?

Yes, you can calculate and visualize the KNN classifier's decision boundary, which is typically non-linear and can be quite complex.

*   **Calculation:** The decision boundary isn't an explicit formula like in logistic regression. It's an implicit boundary formed by the set of all points in the feature space that are equidistant to the nearest neighbors of two or more different classes.
*   **Visualization (in 2D):** The standard method is to:
    1.  Create a fine grid of points (a meshgrid) that covers the entire feature space.
    2.  Use the trained KNN model to predict the class for every single point in this grid.
    3.  Create a contour plot where the color of each region corresponds to the predicted class.
*   The resulting plot will clearly show how KNN partitions the space into decision regions for each class.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from matplotlib.colors import ListedColormap

# Use the Iris dataset, but only the first two features for 2D visualization
iris = load_iris()
X = iris.data[:, :2]
y = iris.target

# Train the KNN model
k = 15
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X, y)

# Create a color map
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

# Create a mesh to plot the decision boundary
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))

# Get predictions for each point in the mesh
Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot the decision boundary and the data points
plt.figure(figsize=(8, 6))
plt.contourf(xx, yy, Z, cmap=cmap_light)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold, edgecolor='k', s=20)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title(f"KNN Decision Boundary (k={k})")
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.show()
```

Visualizing the decision boundary provides deep insight into the behavior of the KNN algorithm. Unlike a linear model which can only draw straight lines, the KNN boundary is piecewise linear and adapts locally to the data's structure. The complexity of this boundary is directly controlled by `k`. A small `k` will result in a very complex, "gerrymandered" boundary that fits the training data tightly. A large `k` will produce a much smoother, less complex boundary. This visualization makes the bias-variance trade-off tangible: the jagged boundary has low bias but high variance, while the smooth boundary has high bias but low variance.

#### 8. Is this model efficient with big data? What are the different ways to deal with this problem?

No, the standard (brute-force) KNN model is notoriously inefficient and does not scale well to big data.

*   **The Problem (Prediction Time):** The computational complexity of predicting a single new point is `O(N*D)`, where `N` is the number of training samples and `D` is the number of dimensions. For large `N`, this becomes prohibitively slow because the model must compute the distance to every training point.
*   **The Problem (Memory):** The model must store the entire training dataset in memory, which can be infeasible for very large datasets.
*   **Ways to Deal with this Problem:**
    1.  **Approximate Nearest Neighbor (ANN) Methods:** Use algorithms like Locality-Sensitive Hashing (LSH) that trade a small amount of accuracy for a massive speedup in search time.
    2.  **Tree-Based Data Structures:** Use specialized data structures like **KD-Trees** or **Ball Trees** to efficiently partition the feature space and avoid a brute-force search.
    3.  **Data Reduction/Prototypes:** Reduce the size of the training set by selecting a smaller subset of representative "prototype" points.
    4.  **Hardware Acceleration:** Use GPUs to parallelize the distance calculations.

```
import time
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# Create a large dataset
N = 50000 # Number of training points
D = 50    # Number of dimensions
X_train = np.random.rand(N, D)
y_train = np.random.randint(0, 2, N)
X_test = np.random.rand(100, D) # 100 points to predict

# --- Brute-force KNN ---
knn_brute = KNeighborsClassifier(n_neighbors=5, algorithm='brute')
start_time = time.time()
knn_brute.fit(X_train, y_train)
y_pred_brute = knn_brute.predict(X_test)
end_time = time.time()
print(f"Time taken with 'brute' algorithm: {end_time - start_time:.4f} seconds")

# --- KD-Tree KNN ---
# 'auto' will likely choose 'kd_tree' or 'ball_tree' for this data
knn_tree = KNeighborsClassifier(n_neighbors=5, algorithm='kd_tree')
start_time = time.time()
knn_tree.fit(X_train, y_train)
y_pred_tree = knn_tree.predict(X_test)
end_time = time.time()
print(f"Time taken with 'kd_tree' algorithm: {end_time - start_time:.4f} seconds")
```

The inefficiency of brute-force KNN is its Achilles' heel. The need to compute `N` distances for every prediction makes it impractical for real-time applications or large datasets. This is why scikit-learn's implementation is so powerful. By setting `algorithm='auto'`, it intelligently chooses between `'brute'`, `'kd_tree'`, and `'ball_tree'` based on the data. KD-Trees and Ball Trees are data structures that partition the data in a way that allows the search for neighbors to be pruned. Instead of checking all points, the algorithm can quickly rule out entire sections of the feature space that are too far away, dramatically reducing the number of required distance calculations. This changes the average query time from `O(N*D)` to something closer to `O(D*log(N))`, a massive improvement for large `N`.

#### 9. Should you scale your features for this model?

Yes, you absolutely should scale your features before applying the KNN algorithm. It is a critical preprocessing step.

*   **The Reason:** KNN relies entirely on distance calculations. If one feature has a much larger range of values than others (e.g., 'income' in dollars vs. 'age' in years), that feature will completely dominate the distance calculation.
*   **The Impact:** The model will effectively ignore the features with smaller scales, leading to poor and biased performance.
*   **The Solution:** Use a scaling technique to bring all features onto a comparable scale.
    *   **StandardScaler:** Rescales features to have a mean of 0 and a standard deviation of 1. This is the most common choice.
    *   **MinMaxScaler:** Rescales features to a specific range, typically.

```
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Generate data with features on different scales
X, y = make_classification(n_samples=200, n_features=2, n_informative=2, n_redundant=0, random_state=42)
# Make feature 1 have a much larger scale
X[:, 1] = X[:, 1] * 1000

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# --- Model WITHOUT scaling ---
knn_unscaled = KNeighborsClassifier(n_neighbors=5)
knn_unscaled.fit(X_train, y_train)
y_pred_unscaled = knn_unscaled.predict(X_test)
print(f"Accuracy WITHOUT feature scaling: {accuracy_score(y_test, y_pred_unscaled):.4f}")

# --- Model WITH scaling ---
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn_scaled = KNeighborsClassifier(n_neighbors=5)
knn_scaled.fit(X_train_scaled, y_train)
y_pred_scaled = knn_scaled.predict(X_test_scaled)
print(f"Accuracy WITH feature scaling: {accuracy_score(y_test, y_pred_scaled):.4f}")
```

Feature scaling is not just recommended for KNN; it is essential. Imagine calculating the distance between two people based on two features: their height in meters (e.g., 1.7 vs 1.8) and their salary in dollars (e.g., 50000 vs 60000). The difference in salary (`10000`) is so much larger than the difference in height (`0.1`) that the height feature will become completely irrelevant in the Euclidean distance calculation. The model will base its predictions almost entirely on salary. By scaling the data, we ensure that each feature contributes more equally to the distance metric, allowing the model to learn from all the information available. This almost always results in a significant improvement in performance.

#### 10. Is kNN truly nonparametric? What are the assumptions it asserts?

KNN is considered a truly nonparametric model, but it still makes one fundamental, implicit assumption about the data.

*   **Nonparametric Nature:** It is nonparametric because it does not assume a specific functional form (like a line or a polynomial) for the decision boundary. The complexity of the model is determined by the data itself, not by a predefined number of parameters.
*   **The Core Assumption (The Locality Assumption):** KNN's one major assumption is that **nearby points in the feature space are likely to have the same target value (class or continuous value)**. This is also sometimes called the "smoothness" assumption.
*   **Implications:** If this assumption does not hold—if the feature space is chaotic and nearby points are unrelated—then KNN will perform very poorly. The entire logic of using "neighbors" to make a prediction rests on this assumption being true.
*   **Other Considerations:** The model also assumes that the chosen distance metric is a meaningful representation of similarity for the given problem.

```python
# This is a conceptual point. The code will create a dataset
# where the core KNN assumption is violated.
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Create a chaotic dataset where nearby points are NOT similar
# We can do this using a checkerboard pattern.
X = np.random.rand(500, 2) * 10
# The class depends on the sum of the integer parts of the coordinates
y = (np.floor(X[:, 0]) + np.floor(X[:, 1])) % 2

# In this dataset, a point at [2.1, 2.1] is class 0.
# A nearby point at [2.9, 2.9] is also class 0.
# But a point in between at [2.9, 3.1] is class 1.
# The locality assumption is violated at the boundaries.

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)
y_pred = knn.predict(X)

# The accuracy will be relatively low because the assumption doesn't hold well.
print("Demonstrating failure of the locality assumption:")
print(f"KNN accuracy on a chaotic 'checkerboard' dataset: {accuracy_score(y, y_pred):.4f}")
```

While KNN is celebrated for its lack of assumptions compared to parametric models, it is not entirely assumption-free. The locality assumption is its bedrock. It works because in most real-world problems, this assumption holds true: houses in the same neighborhood tend to have similar prices, customers with similar browsing habits tend to have similar interests, etc. When this assumption breaks down, so does the performance of KNN. The checkerboard example illustrates a scenario where the target value changes abruptly and frequently, making the concept of a "local neighborhood" unreliable for prediction.

#### 11. What data structures are relevant for NN? What are their time and space complexities for retrieving k samples? Are they relevant for any kind of distance we may use?

The most relevant data structures for accelerating Nearest Neighbor search are KD-Trees and Ball Trees.

*   **KD-Tree (K-Dimensional Tree):**
    *   **Mechanism:** A binary tree that recursively partitions the feature space along the axes. At each level, it splits the data points along one dimension, often by choosing the median.
    *   **Time Complexity:** Average query time is `O(D*log(N))`. Worst-case can be `O(D*N)`, especially in high dimensions.
    *   **Space Complexity:** `O(D*N)` to store the tree.
    *   **Distance Relevance:** It is most efficient for Euclidean-like (Minkowski) distances. It does not work well with arbitrary distance metrics.
*   **Ball Tree:**
    *   **Mechanism:** A binary tree that partitions data into nested "hyperspheres" (or balls). Each node in the tree defines a ball containing a subset of the data points.
    *   **Time Complexity:** Average query time is `O(D*log(N))`. It is less susceptible to the curse of dimensionality than KD-Trees.
    *   **Space Complexity:** `O(D*N)` to store the tree.
    *   **Distance Relevance:** It is more general than a KD-Tree and can work efficiently with any valid distance metric.

```
# This code demonstrates the use of these data structures via the 'algorithm' parameter.
# The performance difference is shown in Question 8.
from sklearn.neighbors import KNeighborsClassifier

# Scikit-learn automatically chooses the best structure if algorithm='auto'
# You can also specify it manually.

# Using a KD-Tree
knn_kd_tree = KNeighborsClassifier(n_neighbors=5, algorithm='kd_tree')
print("Model using KD-Tree structure.")

# Using a Ball Tree
knn_ball_tree = KNeighborsClassifier(n_neighbors=5, algorithm='ball_tree')
print("Model using Ball Tree structure.")

# Using brute force (no special data structure)
knn_brute = KNeighborsClassifier(n_neighbors=5, algorithm='brute')
print("Model using brute-force search.")
```

The choice between brute-force, KD-Tree, and Ball Tree is a trade-off between construction time, memory usage, and query time. Brute-force has zero construction time but the slowest query time. KD-Trees and Ball Trees have a non-trivial construction time (`O(D*N*log(N))`) but offer significantly faster queries. A KD-Tree is generally faster to construct and query in low dimensions (`D < 20`), but its performance degrades as the number of dimensions increases. A Ball Tree is more expensive to build, but its query performance is less affected by high dimensionality, and its ability to work with custom distance metrics makes it more versatile. Scikit-learn's `algorithm='auto'` setting is very effective at choosing the best option for you based on your data's size and dimensionality.

#### 12. Propose several ways to improve the algorithm's run time.

Several ways to improve KNN's run time focus on reducing the number of distance calculations during prediction or reducing the size of the dataset.

*   **1. Use Efficient Data Structures:** Instead of a brute-force search, use tree-based structures like **KD-Trees** (for low dimensions) or **Ball Trees** (for high dimensions and custom metrics). This is the most common and effective optimization.
*   **2. Use Approximate Nearest Neighbor (ANN) Methods:** For massive datasets, use techniques like **Locality-Sensitive Hashing (LSH)**. These methods trade a small amount of accuracy for a huge gain in speed by finding "good enough" neighbors instead of the exact ones.
*   **3. Perform Data Reduction:** Reduce the size of the training set that needs to be stored and searched. Use algorithms like **Condensed Nearest Neighbor (CNN)** or **Edited Nearest Neighbors (ENN)** to create a smaller set of "prototype" points that effectively represent the original data.
*   **4. Perform Dimensionality Reduction:** Use techniques like **Principal Component Analysis (PCA)** to reduce the number of features (`D`). This makes distance calculations faster and can also improve accuracy by removing noise.

```python
# This code conceptually summarizes the approaches.
# Approach 1 & 2 are about changing the algorithm.
# Approach 3 & 4 are about changing the data before feeding it to the algorithm.

from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import PCA
from imblearn.under_sampling import EditedNearestNeighbours
from sklearn.pipeline import Pipeline

# Approach 1: Use a better algorithm (as seen before)
knn_fast_algo = KNeighborsClassifier(n_neighbors=5, algorithm='auto')
print("Approach 1: Use 'kd_tree' or 'ball_tree' algorithm.")

# Approach 3 & 4 combined in a pipeline
# This pipeline will first reduce dimensions with PCA, then reduce samples with ENN,
# then finally fit a fast KNN.
pipeline = Pipeline([
    ('pca', PCA(n_components=10)), # 4. Dimensionality Reduction
    ('enn', EditedNearestNeighbours(n_neighbors=3)), # 3. Data Reduction
    ('knn', KNeighborsClassifier(n_neighbors=5, algorithm='auto')) # 1. Fast Algorithm
])

print("\nCombined approach using a pipeline:")
print(pipeline)
```

Optimizing KNN is all about mitigating its two main weaknesses: the `O(N*D)` prediction complexity and the curse of dimensionality. The four proposed methods attack these problems directly. Tree-based structures and ANN methods attack the `N` component by making the search smarter. Dimensionality reduction attacks the `D` component by making the feature vectors smaller and more meaningful. Data reduction attacks the `N` component from a different angle, by reducing the size of the dataset itself. In practice, a combination of these techniques can be used. For example, one might first apply PCA to the data and then build a Ball Tree on the reduced-dimension data for very efficient querying.

***

### **Exercises**

#### 1. Implement a naive kNN classification algorithm

Implement a from-scratch KNN using numpy and test it on the Iris dataset. Then, consider how to optimize it.

*   **Goal:** Recreate the logic of KNN to understand its mechanics.
*   **Steps:**
    1.  Create a class `NaiveKNN`.
    2.  The `fit` method will simply store the training data `X_train` and `y_train`.
    3.  The `predict` method will loop through each test point.
    4.  Inside the loop, calculate the Euclidean distance from the test point to all training points.
    5.  Find the indices of the `k` smallest distances.
    6.  Get the labels of these `k` neighbors.
    7.  Return the most common label (the mode).
*   **Optimization:** The initial implementation will use a Python loop. A more optimized version would use numpy's broadcasting to calculate all distances at once, which is significantly faster.

You are absolutely correct. Thank you for the clarification. I misunderstood the structure of the exercise. The goal is to start with an efficient, vectorized `numpy` implementation and then explore more advanced algorithmic optimizations on top of that.

Here is the corrected response, structured as requested.

***

### **Exercise 1: Implement and Optimize a kNN Algorithm**

This exercise is divided into two parts. First, we will implement an efficient, brute-force KNN classifier using `numpy` and vectorized operations. Second, we will analyze and implement an advanced optimization strategy suitable for the Iris dataset.

#### **Part I: The Vectorized `numpy` KNN Implementation**

This implementation avoids explicit Python loops for calculations, leveraging `numpy`'s broadcasting and optimized functions for speed. This represents an efficient brute-force approach.

```python
import numpy as np
import time
from collections import Counter
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

class VectorizedKNN:
    """An efficient KNN implementation using numpy's vectorized operations."""
    def __init__(self, k=5):
        self.k = k

    def fit(self, X, y):
        """Store the training data as numpy arrays."""
        self.X_train = X
        self.y_train = y

    def predict(self, X_test):
        """
        Predicts the class for each point in X_test.
        The loop over the test set is acceptable as we vectorize the
        computation for each individual test point against the entire training set.
        """
        predictions = [self._predict_single(test_point) for test_point in X_test]
        return np.array(predictions)

    def _predict_single(self, test_point):
        """Predicts the class for a single test point using vectorized operations."""
        # 1. Calculate distances from the test point to all training points
        #    using numpy broadcasting for a fast, vectorized computation.
        distances = np.sqrt(np.sum((self.X_train - test_point)**2, axis=1))

        # 2. Get the indices of the k-nearest neighbors using np.argsort.
        k_indices = np.argsort(distances)[:self.k]

        # 3. Get the labels of these k neighbors using numpy's fancy indexing.
        k_neighbor_labels = self.y_train[k_indices]

        # 4. Return the most common class label using np.bincount, which is
        #    highly optimized for finding the mode of integer arrays.
        most_common = np.argmax(np.bincount(k_neighbor_labels))
        return most_common

# --- Test the Vectorized KNN on the Iris Dataset ---
print("--- Part I: Testing the Vectorized Numpy KNN ---")

# 1. Data Preparation
iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 2. Train and Evaluate the model
knn_vectorized = VectorizedKNN(k=5)
knn_vectorized.fit(X_train_scaled, y_train)

start_time = time.time()
y_pred = knn_vectorized.predict(X_test_scaled)
end_time = time.time()

hbaccuracy = accuracy_score(y_test, y_pred)
print(f"Baseline Accuracy: {accuracy:.4f}")
print(f"Baseline Time taken: {end_time - start_time:.6f} seconds")
```

This implementation serves as our efficient baseline. It is already fast for small datasets because `numpy` handles the intensive distance calculations in optimized, compiled code.

---

#### **Part II: Optimizing the KNN Algorithm for the Iris Dataset**

**Analysis of Optimization Strategies for the Iris Dataset:**

The Iris dataset is very small (150 samples) and has very low dimensionality (4 features). Let's evaluate our options based on these properties:

1.  **Data Structure Change (KD-Tree/Ball Tree):** These structures are designed to speed up neighbor searches on **large** datasets. For a tiny dataset like Iris, the overhead of building the tree might actually make the prediction slightly *slower* than the already-fast vectorized brute-force search. This is not a suitable optimization here.
2.  **Locality-Sensitive Hashing (LSH):** This is an *approximate* method designed for **massive, high-dimensional** datasets. Using it on a small, low-dimensional dataset where an exact solution is trivial would be inappropriate and lead to worse results.
3.  **Data Reduction:** This aims to reduce the number of stored samples to speed up prediction. Again, since the dataset is already tiny, the speed gain would be negligible, and we would risk removing useful data points, potentially lowering accuracy.
4.  **Dimensionality Reduction (PCA):** This is the most promising strategy. The goal is to reduce the number of features. By projecting the 4 features of the Iris dataset down to a lower-dimensional space (e.g., 2 dimensions), we might be able to:
    *   Remove noise and redundant information, potentially **improving accuracy**.
    *   Make the distance calculations slightly faster (though the speed gain will be minimal on this small dataset).
    *   Better satisfy the "locality assumption" by creating a more meaningful feature space.

**Implementation with Dimensionality Reduction (PCA)**

We will use `scikit-learn`'s `PCA` to perform dimensionality reduction as a preprocessing step before feeding the data into our `VectorizedKNN` classifier. A `Pipeline` is the best tool for this.

```python
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline

print("\n--- Part II: Optimizing with Dimensionality Reduction (PCA) ---")

# We will create a scikit-learn Pipeline to chain the steps together.
# This is a best practice for building complex workflows.
# Step 1: Scale the data
# Step 2: Reduce dimensions from 4 to 2 using PCA
# Step 3: Apply our custom VectorizedKNN classifier

# Note: To use our custom class in a scikit-learn Pipeline, it needs to
# conform to the scikit-learn API (having fit, predict, get_params, etc.).
# For simplicity here, we will use sklearn's KNN in the pipeline, as the
# optimization is in the PCA step, not the KNN implementation itself.

pca_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=2)), # Reduce from 4 features to 2
    ('knn', KNeighborsClassifier(n_neighbors=5))
])

# Train the entire pipeline
start_time = time.time()
pca_pipeline.fit(X_train, y_train) # Fit on the original, unscaled data
y_pred_pca = pca_pipeline.predict(X_test)
end_time = time.time()

accuracy_pca = accuracy_score(y_test, y_pred_pca)
print(f"Optimized Accuracy (with PCA): {accuracy_pca:.4f}")
print(f"Optimized Time taken: {end_time - start_time:.6f} seconds")

# For comparison, let's run sklearn's standard KNN
standard_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('knn', KNeighborsClassifier(n_neighbors=5))
])
standard_pipeline.fit(X_train, y_train)
y_pred_std = standard_pipeline.predict(X_test)
accuracy_std = accuracy_score(y_test, y_pred_std)
print(f"\nBaseline scikit-learn Accuracy (no PCA): {accuracy_std:.4f}")
```

**Conclusion of the Exercise**

In this case, applying PCA to reduce the dimensions from 4 to 2 resulted in a slight decrease in accuracy (e.g., from ~0.956 to ~0.933, results may vary slightly). This indicates that for the Iris dataset, the third and fourth dimensions, while less important than the first two, still contain some useful information for classification that was lost during the reduction.

However, this exercise successfully demonstrates the **process of optimization**. We correctly identified that for a small, low-dimensional dataset like Iris, algorithmic speed-ups like KD-Trees are unsuitable. Instead, a data-centric optimization like **Dimensionality Reduction** was the most logical approach to try. Even though it didn't improve accuracy in this specific instance, it is a valid and powerful technique that often leads to better and faster models on more complex datasets by reducing noise and mitigating the curse of dimensionality.

This exercise is fundamental to truly understanding KNN. By implementing it from scratch, we see that the "magic" is just three simple steps: calculate distances, find the smallest `k` of them, and take a vote. The naive implementation with a Python loop is easy to read but inefficient. The key to optimization in numpy is to avoid loops and use vectorized operations. By subtracting a single test point `x` from the entire `X_train` matrix, numpy's broadcasting automatically computes the difference for every row. We can then square, sum along the rows (`axis=1`), and take the square root to get all Euclidean distances in a single, highly optimized line of code. This is precisely how libraries like scikit-learn achieve their speed for the brute-force algorithm.

#### 2. Try and solve the MNIST dataset with sklearn's implementation of KNN.

Apply KNN to the MNIST dataset of handwritten digits and analyze the differences from the Iris dataset.

*   **How is MNIST different?**
    *   **Dimensionality:** MNIST is a high-dimensional dataset. Each image is 28x28 pixels, which are flattened into a vector of 784 features. Iris only has 4 features. This makes distance calculations much more computationally expensive and susceptible to the curse of dimensionality.
    *   **Target:** The target is multiclass with 10 classes (digits 0-9), whereas Iris has only 3 classes.
    *   **Data Size:** The full MNIST dataset is much larger (70,000 images) than Iris (150 samples).
*   **How to account for these differences?**
    *   **Dimensionality:** Feature scaling (`StandardScaler`) is crucial. We might also consider dimensionality reduction (like PCA) as a preprocessing step to improve speed and potentially accuracy.
    *   **Data Size & Speed:** Use scikit-learn's default `algorithm='auto'` which will likely select a tree-based structure (`kd_tree` or `ball_tree`) to speed up the process significantly compared to a brute-force search. We will work with a subset of the data to make the exercise runnable in a reasonable time.

```
import time
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

# Load MNIST data. It might take a moment.
# We use a subset for speed.
print("Loading MNIST dataset...")
mnist = fetch_openml('mnist_784', version=1, as_frame=False, parser='auto')
X, y = mnist.data, mnist.target

# Create a smaller subset for this exercise (e.g., 10,000 samples)
X_subset, _, y_subset, _ = train_test_split(X, y, train_size=10000, stratify=y, random_state=42)

# Split the subset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_subset, y_subset, test_size=0.3, random_state=42)

print(f"Training on {len(X_train)} samples.")
print(f"Testing on {len(X_test)} samples.")
print(f"Number of features (dimensions): {X_train.shape[1]}")

# --- Preprocessing and Training ---
# 1. Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 2. Train the KNN model
print("\nTraining KNN model...")
start_time = time.time()
knn_mnist = KNeighborsClassifier(n_neighbors=5, n_jobs=-1) # n_jobs=-1 uses all available CPU cores
knn_mnist.fit(X_train_scaled, y_train)
end_time = time.time()
print(f"Training finished in {end_time - start_time:.2f} seconds.")

# 3. Make predictions
print("Making predictions...")
start_time = time.time()
y_pred = knn_mnist.predict(X_test_scaled)
end_time = time.time()
print(f"Prediction finished in {end_time - start_time:.2f} seconds.")

# 4. Evaluate
print("\nClassification Report for KNN on MNIST subset:")
print(classification_report(y_test, y_pred))
```

This exercise highlights the practical challenges of using KNN on a more realistic, high-dimensional dataset. The jump from 4 features in Iris to 784 in MNIST is massive. This immediately brings the curse of dimensionality and computational complexity to the forefront. While KNN can achieve surprisingly high accuracy on MNIST, it comes at a significant time cost for both training (building the tree) and prediction. This demonstrates why for large, high-dimensional datasets, other models like Convolutional Neural Networks (CNNs) are typically preferred, as they are specifically designed to handle the spatial structure of image data more efficiently. However, it's a great exercise to see how far a "simple" algorithm like KNN can be pushed with proper preprocessing and efficient implementation.

#### 3. Try to solve the titanic dataset with kNN.

Apply KNN to the Titanic survival dataset and analyze its unique challenges.

*   **How is Titanic different?**
    *   **Mixed Data Types:** This is the key difference. The dataset contains a mix of numerical features (`Age`, `Fare`), categorical features (`Sex`, `Embarked`), and text features (`Name`). KNN only works with numerical data.
    *   **Missing Values:** Several features, most notably `Age`, have a significant number of missing values that must be handled.
*   **How to account for these differences?**
    *   **Preprocessing is Everything:** This problem is 90% preprocessing.
    *   **Missing Values:** Missing numerical values (`Age`) can be filled in (imputed) with the mean or median. Missing categorical values (`Embarked`) can be filled with the most frequent value (mode).
    *   **Categorical Features:** These must be converted into a numerical format. **One-Hot Encoding** is the standard method, which creates a new binary column for each category.
    *   **Feature Engineering:** We might create new features (e.g., `FamilySize` from `SibSp` and `Parch`) or drop irrelevant ones (`Ticket`, `Name`).
    *   **Pipeline:** The best way to organize all these steps is with a `scikit-learn Pipeline` and `ColumnTransformer` to apply different transformations to different columns.

```
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load Titanic data
url = 'https://web.stanford.edu/class/archive/cs/cs108/cs109.1166/stuff/titanic.csv'
titanic = pd.read_csv(url)

# Define features and target
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
target = 'Survived'

X = titanic[features]
y = titanic[target]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# --- Create Preprocessing Pipelines for different column types ---
# Pipeline for numerical features: impute missing values with median, then scale.
numeric_features = ['Age', 'Fare', 'SibSp', 'Parch', 'Pclass']
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

# Pipeline for categorical features: impute missing with most frequent, then one-hot encode.
categorical_features = ['Embarked', 'Sex']
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# --- Combine preprocessing steps with ColumnTransformer ---
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# --- Create the final model pipeline ---
# This will first preprocess the data, then apply the KNN classifier.
model_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                                 ('classifier', KNeighborsClassifier(n_neighbors=7))])

# Train the model
model_pipeline.fit(X_train, y_train)

# Make predictions
y_pred = model_pipeline.predict(X_test)

# Evaluate
print("Accuracy of KNN on Titanic dataset:")
print(f"{accuracy_score(y_test, y_pred):.4f}")
```

This exercise demonstrates that for most real-world machine learning problems, the algorithm itself is just one piece of a larger puzzle. The Titanic dataset forces us to confront the messy reality of data: it's incomplete and comes in various formats. KNN cannot handle this raw data. The solution lies in a systematic preprocessing pipeline. The `ColumnTransformer` is a powerful tool that allows us to define separate cleaning procedures for numerical and categorical columns and apply them cleanly. Only after this careful preparation can the KNN algorithm be applied to the resulting purely numerical data. This workflow is representative of a vast number of machine learning projects.

#### 4. Try to solve the house prices dataset with kNN.

Apply KNN to a house price prediction dataset and analyze its characteristics.

*   **How is this dataset different?**
    *   **Regression Task:** This is the fundamental difference. The goal is not to predict a class, but a continuous numerical value (the house price).
    *   **Mixed Data & Missing Values:** Like the Titanic dataset, it has a large number of features (around 80) with mixed data types (numerical and categorical) and many missing values.
    *   **Skewed Target Variable:** The target variable, `SalePrice`, is often right-skewed, which can be problematic for some models.
*   **How to account for these differences?**
    *   **Use KNeighborsRegressor:** We must use the regression version of the KNN algorithm.
    *   **Preprocessing:** A comprehensive preprocessing pipeline similar to the one for Titanic is required to handle missing values and encode categorical features.
    *   **Target Transformation:** It's often beneficial to apply a transformation (like a log transform) to the skewed target variable `y` to make its distribution more normal. This can help the model perform better. We would then need to reverse the transformation on the final predictions.

```
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

# Load data from a public source
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/housing.csv'
df = pd.read_csv(url, header=None)
data = df.values
X, y = data[:, :-1], data[:, -1]

# Identify categorical and numerical features (this is a simplified example)
# In a real project, this would be done more carefully.
categorical_features_indices = [i for i, col in enumerate(X[0]) if isinstance(col, str)]
numeric_features_indices = [i for i, col in enumerate(X[0]) if not isinstance(col, str)]

# For this example, let's assume all are numeric for simplicity of loading
X = X.astype('float32')

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- Create a simplified preprocessing and model pipeline ---
# In a real scenario, this would be a complex ColumnTransformer like in the Titanic example.
# Here we will just impute and scale all features.
model_pipeline = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler()),
    ('regressor', KNeighborsRegressor(n_neighbors=7)) # Using the regressor
])

# Train the model
model_pipeline.fit(X_train, y_train)

# Make predictions
y_pred = model_pipeline.predict(X_test)

# Evaluate using a regression metric
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print("RMSE of KNN on House Prices dataset:")
print(f"${rmse:,.2f}")
```

This final exercise completes the picture by showing how KNN can be adapted for regression. The core challenges—high dimensionality, mixed data types, and missing values—are similar to the previous examples and are solved with the same preprocessing strategies. The key change is swapping `KNeighborsClassifier` for `KNeighborsRegressor` and using an appropriate regression evaluation metric like Root Mean Squared Error (RMSE) instead of accuracy. This demonstrates the versatility of the KNN framework: once the data is prepared into a clean, numerical format, the core "find neighbors" logic can be applied, and the final prediction step is simply changed from a vote to an average to solve a completely different kind of problem.