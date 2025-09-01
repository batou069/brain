# Worksheet
## Keywords

### 1\. Dimension

  * **Short Description:** A dimension is a feature, attribute, or variable in a dataset.
  * **What is it good for?** Dimensions describe the properties of each data point, allowing us to characterize and differentiate between them.
  * **Details:**
      * In a typical data table (like a spreadsheet), each **column represents a dimension**, and each row is a data point.
      * The total number of dimensions is simply the total number of features used to describe the data.
      * For example, in a dataset about people, the dimensions could be `height`, `weight`, `age`, and `income`.
      * In an image dataset, each pixel's color value can be treated as a separate dimension.
  * **Example (Analogy):**
    Imagine you're describing cars. The dimensions you might use are `horsepower`, `weight`, `number of doors`, and `price`. A specific car, like a "2025 Ford Mustang," is a single point defined by its values in this 4-dimensional space.

### 2\. Curse of Dimensionality

  * **Short Description:** The "Curse of Dimensionality" refers to a set of problems that arise when working with data in high-dimensional spaces.
  * **Why is it important?** It explains why having more features is not always better and is the primary motivation for using dimensionality reduction.
  * **Details:**
      * **Data Sparsity:** As you add more dimensions, the volume of the feature space increases exponentially. This makes your data become "sparse," meaning the data points are very far away from each other.
      * **Algorithm Performance:** This sparsity makes it harder for machine learning algorithms to find meaningful patterns. For example, the concept of a "nearest neighbor" becomes less useful if all neighbors are far away.
      * **Overfitting:** With too many features (dimensions) relative to the number of data points, a model is more likely to learn the noise in the training data instead of the true underlying relationships, leading to poor performance on new data.
      * **Computational Cost:** More dimensions mean more data to store and more calculations to perform, which drastically increases the time and memory required to train models.
  * **Example (Analogy):**
    Imagine you lost your keys on a 100-meter-long paved path (1-dimension). It's relatively easy to find them. Now, imagine you lost them in a 100m x 100m square park (2-dimensions). The search is much harder. If you lost them in a 100m x 100m x 100m cube-shaped building (3-dimensions), the search space becomes immense. The "curse" is this exponential explosion of volume (and difficulty) as you add dimensions.

-----

## Dimensionality Reduction Techniques

### 1\. Principal Component Analysis (PCA)

  * **Short Description:** PCA is an **unsupervised, linear** technique that finds new, uncorrelated dimensions called "principal components" that capture the maximum variance in the data.
  * **What is it good for?** It's a go-to method for data compression, noise reduction, and visualizing high-dimensional data.
  * **Details:**
      * PCA creates new dimensions (principal components) that are linear combinations of the original features (e.g., `new_dimension_1 = 0.7*feature_A + 0.3*feature_B - 0.1*feature_C`).
      * The first principal component is the direction in which the data varies the most. The second is the next most important direction, orthogonal (at a right angle) to the first.
      * To reduce dimensionality, you keep only the first few principal components that capture a significant percentage of the total information (variance), like 95%.
  * **Example (Python Code):**
    ```python
    from sklearn.decomposition import PCA
    import numpy as np

    # Sample data with 4 features (4D)
    X = np.random.rand(100, 4)

    # Initialize PCA to reduce the data to 2 dimensions
    pca = PCA(n_components=2)

    # Fit PCA to the data and transform it
    X_reduced = pca.fit_transform(X)

    print("Original data shape:", X.shape) # Output: (100, 4)
    print("Reduced data shape:", X_reduced.shape) # Output: (100, 2)
    ```

### 2\. Factor Analysis (FA)

  * **Short Description:** Factor Analysis is a technique used to identify unobserved, underlying "factors" that can explain the correlations among a set of observed variables.
  * **What is it good for?** It's ideal for data exploration, helping to uncover latent (hidden) structures in survey data or psychological tests.
  * **Details:**
      * FA assumes that the observed features are influenced by a smaller number of hidden factors plus some unique, random noise for each feature.
      * Unlike PCA which explains total variance, FA focuses only on explaining the **common variance** (the part of a variable's variance that is shared with other variables).
      * It is widely used in social sciences and marketing to measure abstract concepts like "brand loyalty" or "intelligence" from a series of related survey questions.
  * **Example (Conceptual):**
    A psychologist administers a test with questions about vocabulary, logic puzzles, and spatial reasoning. Factor Analysis could be used to see if an underlying latent factor, which we might label "general intelligence," is responsible for the performance across all these different types of questions.

### 3\. Linear Discriminant Analysis (LDA)

  * **Short Description:** LDA is a **supervised, linear** technique that finds the feature combinations that best separate two or more classes of data.
  * **What is it good for?** Its primary use is as a preprocessing step for classification models to maximize class separability.
  * **Details:**
      * Because LDA is **supervised**, it requires the data to have class labels (e.g., 'cat' vs. 'dog', 'spam' vs. 'not-spam').
      * Its goal is to project the data onto a lower-dimensional space in a way that maximizes the distance *between* the means of the different classes while minimizing the variance *within* each class.
      * You can reduce the data to at most `c - 1` dimensions, where `c` is the number of classes.
  * **Example (Analogy):**
    Imagine you have data on two groups of people, basketball players and gymnasts, plotted by `height` and `weight`.
      * **PCA** would find the axis where the combined data is most spread out.
      * **LDA**, knowing the group labels, would specifically find the axis that, when you project the points onto it, makes the cluster of basketball players and the cluster of gymnasts as distinct and far apart as possible.

### 4\. t-distributed Stochastic Neighbor Embedding (t-SNE)

  * **Short Description:** t-SNE is a **nonlinear** dimensionality reduction technique used primarily for visualizing high-dimensional datasets in 2D or 3D.
  * **What is it good for?** It excels at revealing the underlying local structure and clusters within complex data, making it a powerful tool for exploratory data analysis. 🔮
  * **Details:**
      * t-SNE models the similarity between high-dimensional points as a probability distribution and then finds a low-dimensional embedding that preserves these similarities.
      * It is particularly effective at keeping points that are close in the high-dimensional space close together in the low-dimensional map.
      * **Important Caveat:** The global geometry, like the relative sizes of and distances between clusters in a t-SNE plot, is often not meaningful. It's best used for visualization, not for preprocessing a model.
  * **Example (Conceptual):**
    If you apply t-SNE to a dataset of thousands of images of animals, the resulting 2D plot would likely show clear, distinct clusters for 'cats', 'dogs', 'birds', etc., making the structure of the dataset instantly visible.

### 5\. Autoencoder

  * **Short Description:** An autoencoder is a type of neural network that learns to compress data into a low-dimensional code and then uncompress it back to its original form.
  * **What is it good for?** Learning powerful, **nonlinear** compressions of complex data like images, audio, or text.
  * **Details:**
      * It's composed of two parts: an **encoder** that maps the input to a low-dimensional representation (the "bottleneck" or "latent space"), and a **decoder** that reconstructs the original input from this representation.
      * The network is trained by minimizing the **reconstruction error**—the difference between the original input and the reconstructed output.
      * Once the network is trained, the encoder part can be used on its own as a powerful dimensionality reduction tool.
  * **Example (Analogy):**
    Think of it like creating a summary of a book. The **encoder** reads the entire book (high-dimensional input) and produces a short, one-paragraph summary (low-dimensional code). The **decoder** then tries to rewrite the entire book using only that summary. The better the summary captures the book's essence, the more accurate the reconstructed book will be.

-----

## Questions

### 1\. Why would you want to reduce dimensionality?

  * **Short Answer:** To make data faster to process, easier to visualize, and to improve the performance of machine learning models by removing noise and redundancy.
  * **Long Answer:** The primary motivations are:
      * **Faster Computation:** Fewer dimensions mean less data, which makes algorithms train faster and use less memory.
      * **Curse of Dimensionality:** It helps combat the negative effects of having too many features, such as data sparsity and model overfitting.
      * **Better Model Performance:** By removing irrelevant "noise" features and combining redundant ones, it can help a model focus on the most important signals, leading to better accuracy.
      * **Data Visualization:** Our brains can't comprehend more than 3 dimensions. Reducing data to 2D or 3D is essential for visual exploration and finding patterns.

### 2\. What kind of problems can you solve with dimensionality reduction?

  * **Short Answer:** Problems in data visualization, data compression, and feature extraction for improving predictive models.
  * **Long Answer:** Dimensionality reduction is applied to a wide range of problems:
      * **Data Visualization:** Compressing data like customer profiles or genetic markers into 2D scatter plots to visually identify clusters and outliers.
      * **Feature Extraction:** Creating new, potent features to feed into a machine learning model. For example, using an autoencoder to turn an entire image into a dense vector representation for an image classification task.
      * **Data Compression:** Reducing the storage footprint of large datasets, like compressing a large library of high-resolution images.
      * **Noise Reduction:** In fields like signal processing, it can be used to isolate a clear signal from background noise by discarding the dimensions associated with the noise.

### 3\. Is it enough to just drop the least relevant columns?

  * **Short Answer:** No, this is often a poor strategy because you lose all information from that column, including how it interacts with other columns.
  * **Long Answer:** The method of dropping columns is called **Feature Selection**. It can be useful, but it has a major drawback: it's an all-or-nothing approach. A column might seem irrelevant on its own but could be very important when combined with another feature. For example, 'height in cm' and 'weight in kg' might individually be weak predictors of health, but their combination into a 'BMI' feature is very powerful. **Feature Extraction** techniques like PCA create new dimensions that are combinations of the original ones, allowing them to preserve the most important information from *all* original columns, which is a more nuanced and often more effective approach.

### 4\. What is the difference between supervised and unsupervised dimensionality reduction?

  * **Short Answer:** Supervised methods use class labels to guide the dimension reduction, while unsupervised methods work with the features alone.
  * **Long Answer:**
      * **Unsupervised methods** (like PCA, t-SNE, Autoencoders) do not know the "answer" or the target variable. Their goal is to find structure within the features themselves, such as the axes of greatest variance (PCA) or the local neighborhood structures (t-SNE). They are used for general data exploration and preprocessing.
      * **Supervised methods** (like LDA) use the target labels. Their goal is not just to find *any* structure, but to find the low-dimensional structure that is most useful for separating the known classes. They optimize the projection to make a subsequent classification task easier.

### 5\. What is the difference between linear and nonlinear dimensionality reduction?

  * **Short Answer:** Linear methods find a flat projection of the data (like a shadow), while nonlinear methods can "unroll" complex, curved data structures.
  * **Long Answer:**
      * **Linear techniques** (like PCA and LDA) assume the data lies on or near a linear subspace (a line, a plane, or a hyperplane). They perform a geometric transformation (rotation and projection) to find this subspace. They are computationally fast and work well when the underlying structure is simple.
      * **Nonlinear techniques** (like t-SNE, Isomap, and Autoencoders) are used when the data lies on a more complex, curved surface called a manifold. For example, if your data points follow the shape of a Swiss roll, a linear method would fail to capture the true structure, while a nonlinear method could "unroll" it into a flat rectangle, preserving the neighbor relationships. These methods are more powerful but also more computationally intensive.

### 6\. What criteria should be considered when choosing a dimensionality reduction method?

  * **Short Answer:** Your primary goal (visualization vs. preprocessing), whether the data is linear or not, and if you have access to class labels.
  * **Long Answer:** Key considerations include:
      * **Goal:** For **visualization**, t-SNE is a top choice. For **feature extraction** before modeling, PCA is a strong default, and LDA is excellent if your final goal is classification.
      * **Supervised vs. Unsupervised:** Do you have **class labels**? If yes, a supervised method like LDA is specifically designed to use them to your advantage. If no, you must use an unsupervised method like PCA.
      * **Data Structure:** Try to get a sense if your data is **linear or nonlinear**. You can visualize it or test simple models. For linear data, PCA is efficient. For complex, nonlinear data, you may need an Autoencoder or t-SNE.
      * **Computational Resources:** For very large datasets, the speed and efficiency of linear methods like PCA are a significant advantage over more complex methods.

### 7\. How do you know if your data is linear or not?

  * **Short Answer:** There's no single test, but you can get clues by visualizing the data and comparing the performance of linear versus nonlinear models.
  * **Long Answer:** Determining this is an exploratory process:
      * **Visualize:** Create scatter plots of different feature pairs. If you consistently see straight-line relationships, the data is likely linear. If you see curves, spirals, or clusters, it's a sign of nonlinearity.
      * **Run PCA:** Perform PCA and look at the cumulative explained variance plot. If the first two or three components capture almost all the variance (e.g., \>95%), the data has a strong linear structure.
      * **Compare Model Performance:** Train a linear model (like Linear Regression) and a nonlinear model (like a Random Forest) on the same task. If the nonlinear model is dramatically better, your data likely contains important nonlinear relationships.
      * **Compare Reconstruction Error:** Apply both PCA and an Autoencoder to reduce to the same number of dimensions. If the Autoencoder has a significantly lower reconstruction error, it's effectively capturing nonlinear structures that PCA cannot.

### 8\. How can you test your dimensionality reduction?

  * **Short Answer:** By either measuring the reconstruction error or by evaluating the performance of a machine learning model built on the reduced data.
  * **Long Answer:** There are two main ways to evaluate the result:
    1.  **Intrinsic Evaluation (Information Loss):** This checks how well you can reconstruct the original data from the compressed version. For PCA, the "explained variance" tells you how much information is preserved. For autoencoders, you can calculate the reconstruction error directly. A lower error or higher explained variance is better.
    2.  **Extrinsic Evaluation (Downstream Task):** This is the most practical test. Use the reduced-dimension data to train your final machine learning model (e.g., a classifier). Compare its performance (accuracy, F1-score, etc.) and training time to a model trained on the original, high-dimensional data. If your performance is similar or better, and the training is faster, the reduction was a success.

### 9\. Can dimensionality reduction help reduce picture size for CV problems?

  * **Short Answer:** Yes, absolutely. Dimensionality reduction is the fundamental principle behind image compression.
  * **Long Answer:** Yes. An image is a very high-dimensional object (each pixel is a dimension). Techniques like the JPEG compression standard are fundamentally dimensionality reduction algorithms (using a method called Discrete Cosine Transform, which is related to PCA). In machine learning:
      * **Autoencoders** are state-of-the-art for this. A trained encoder can compress a large image into a much smaller latent vector, achieving high compression ratios. The decoder then reconstructs the image for viewing.
      * **PCA** can also be used, though it is often less effective than specialized methods. It can find the "principal components" of image patches to store them more efficiently.

### 10\. How many dimensions is too many?

  * **Short Answer:** It's not a fixed number; it's relative to the number of data points you have. Problems begin when the number of dimensions starts to get close to the number of samples.
  * **Long Answer:** There is no magic number like "50 dimensions is too many." The "curse of dimensionality" depends on the **ratio of dimensions ($p$) to samples ($n$)**.
      * **A Rough Rule of Thumb:** Many statisticians suggest you should have at least 5 to 10 data samples for every dimension (`n > 5p`) to build a reliable model. If your number of dimensions approaches or exceeds your number of samples (`p >= n`), you are in a very high-dimensional setting where the curse is a major problem.
      * **Context is Key:** In genomics, having 20,000 dimensions (genes) for 200 samples (patients) is normal. In business analytics, 50 dimensions for 5 million customers is considered low-dimensional. It's all about whether your data points are sufficient to populate the feature space without it becoming sparse.

### 11\. How is PCA different from "Reconstruction Error Minimization" you recently implemented?

  * **Short Answer:** They are two sides of the same coin. The goal of PCA *is* to find the projection that minimizes reconstruction error.

  * **Long Answer:** Principal Component Analysis (PCA) has two definitions that are mathematically equivalent:

    1.  **Maximum Variance Perspective:** Find the projection that maximizes the variance of the projected data.
    2.  **Minimum Error Perspective:** Find the projection that minimizes the sum of squared distances from the original points to their projections on the lower-dimensional surface. This sum of distances **is** the reconstruction error.

    Therefore, an algorithm that finds a **linear** projection by minimizing reconstruction error is, by definition, performing PCA. The two are not different methods; they are different ways of describing the same underlying mathematical objective.

# Autoencoder Variations

- **Variational Autoencoder (VAE):** This type learns a probability distribution for the latent space rather than a single fixed point, which allows it to function as a **generative model** capable of creating new data samples.
    
- **Sparse Autoencoder (SAE):** An SAE is constrained so that only a small number of its hidden neurons are active at any given time, forcing it to learn a **sparse representation** of the input data, which can improve classification performance.
    
- **Denoising Autoencoder (DAE):** A DAE is trained to reconstruct a clean, original input from a version that has been intentionally corrupted with noise. This forces the model to learn **robust features** that are not sensitive to noisy data.
    
- **Contractive Autoencoder (CAE):** This variant adds a penalty to the loss function to ensure that small changes in the input data result in a stable and nearly identical latent representation, making the learned encoding **resistant to small perturbations**.
    
- **Minimum Description Length Autoencoder (MDL-AE):** Leveraging information theory, this autoencoder seeks the most efficient representation by minimizing the combined "length" of the compressed code and the reconstruction error.
    
- **Concrete Autoencoder:** This model is explicitly designed for **discrete feature selection**, as it learns to identify and use an optimal subset of the original input features within its latent layer.

# Dimensionality Reduction: PCA, FA, and LDA

This document provides a deep dive into three fundamental dimensionality reduction techniques: Principal Component Analysis (PCA), Factor Analysis (FA), and Linear Discriminant Analysis (LDA). Each technique is broken down into three levels of detail:

1.  **High-Level:** The core idea and goal.
2.  **Mid-Level:** A more detailed explanation with mathematical intuition and `scikit-learn` examples.
3.  **Low-Level:** The complete mathematical derivation and a from-scratch implementation in Python.

---

## 1. Principal Component Analysis (PCA)

PCA is an **unsupervised** linear technique used to reduce the dimensionality of a dataset while preserving as much of the original "variance" (information) as possible.

### High-Level Concept

* **Goal:** To find a new set of dimensions (axes) called "Principal Components" that are ordered by how much variance of the data they capture.
* **How it Works (Analogy):** Imagine a 3D cloud of data points shaped like an American football. PCA finds the best "shadow" of this cloud. The first principal component is the axis running along the football's length—projecting the data onto this line (casting a shadow) preserves the most spread. The second component is the axis across its width, and the third is across its thickness. To reduce dimensions, we simply keep the axes that capture the most spread (e.g., the first and second) and discard the rest.

### Mid-Level Explanation

PCA performs a change of basis to a new coordinate system where the axes (Principal Components) are:
1.  Orthogonal (at right angles) to each other.
2.  Aligned with the directions of maximum variance in the data.
3.  Ordered by the amount of variance they explain.

The first principal component ($PC_1$) is a linear combination of the original features that explains the most variance. The second ($PC_2$) is orthogonal to the first and explains the most *remaining* variance, and so on.

Mathematically, this is achieved by finding the **eigenvectors** of the data's **covariance matrix**. The eigenvector with the largest corresponding **eigenvalue** is the first principal component.

#### Library Implementation (`scikit-learn`)

```python
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# 1. Generate sample data
np.random.seed(42)
X = np.dot(np.random.rand(2, 2), np.random.randn(2, 200)).T

# 2. Standardize the data (important for PCA)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Initialize and fit PCA
# We want to reduce from 2D to 1D
pca = PCA(n_components=1)
X_pca = pca.fit_transform(X_scaled)

print("Original shape:", X_scaled.shape)
print("Reduced shape:", X_pca.shape)

# Explained variance
print(f"Explained variance by PC1: {pca.explained_variance_ratio_[0]:.2f}")

# To see the principal component vector
print("Principal Component (Eigenvector):", pca.components_[0])

# Plotting
plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.scatter(X_scaled[:, 0], X_scaled[:, 1])
plt.title("Original Data")
plt.axis('equal')

# Plot the principal component vector
origin = [0, 0]
plt.quiver(*origin, *pca.components_[0], color=['r'], scale=3, label='PC1')
plt.legend()


plt.subplot(1, 2, 2)
# Create a y-axis of zeros for plotting the 1D data
y_pca = np.zeros(X_pca.shape[0])
plt.scatter(X_pca, y_pca)
plt.title("Data Projected onto PC1")
plt.show()
```

### Low-Level: Math and From-Scratch Code

#### Mathematical Formulation

Let $\mathbf{X}$ be our $n \times p$ data matrix, where $n$ is the number of samples and $p$ is the number of features. We assume $\mathbf{X}$ is centered (mean of each column is 0).

**Objective:** Find a unit vector $\mathbf{w}$ (a direction) such that the variance of the data projected onto this vector is maximized. The projection of a data point $\mathbf{x}_i$ onto $\mathbf{w}$ is $\mathbf{x}_i^T \mathbf{w}$. The variance of all projected points is:

$$ \text{Var}(\mathbf{Xw}) = \frac{1}{n-1} (\mathbf{Xw})^T (\mathbf{Xw}) = \mathbf{w}^T \left( \frac{\mathbf{X}^T \mathbf{X}}{n-1} \right) \mathbf{w} = \mathbf{w}^T \mathbf{C} \mathbf{w} $$

Where $\mathbf{C} = \frac{1}{n-1}\mathbf{X}^T \mathbf{X}$ is the $p \times p$ covariance matrix.

We want to maximize $\mathbf{w}^T \mathbf{C} \mathbf{w}$ subject to the constraint that $\mathbf{w}$ is a unit vector, i.e., $\mathbf{w}^T \mathbf{w} = 1$. This is a constrained optimization problem that can be solved using a Lagrange multiplier $\lambda$:

$$ \mathcal{L}(\mathbf{w}, \lambda) = \mathbf{w}^T \mathbf{C} \mathbf{w} - \lambda(\mathbf{w}^T \mathbf{w} - 1) $$

Taking the derivative with respect to $\mathbf{w}$ and setting it to zero gives:

$$ \frac{\partial \mathcal{L}}{\partial \mathbf{w}} = 2\mathbf{C}\mathbf{w} - 2\lambda\mathbf{w} = 0 \implies \mathbf{C}\mathbf{w} = \lambda\mathbf{w} $$

This is the fundamental **eigenvalue equation**. The vectors $\mathbf{w}$ that solve this are the **eigenvectors** of the covariance matrix $\mathbf{C}$, and the scalars $\lambda$ are the corresponding **eigenvalues**. To maximize the variance, we choose the eigenvector corresponding to the largest eigenvalue. This is our first principal component. The second principal component is the eigenvector for the second-largest eigenvalue, and so on.

#### From-Scratch Implementation

```python
import numpy as np

class MyPCA:
    def __init__(self, n_components):
        self.n_components = n_components
        self.components = None
        self.mean = None

    def fit(self, X):
        # 1. Center the data
        self.mean = np.mean(X, axis=0)
        X_centered = X - self.mean

        # 2. Calculate the covariance matrix
        # (n_samples - 1) is the degrees of freedom
        cov_matrix = np.cov(X_centered, rowvar=False)

        # 3. Calculate eigenvalues and eigenvectors
        eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

        # 4. Sort eigenvectors by descending eigenvalues
        # eigenvectors are columns in the output of np.linalg.eig
        eigenvectors = eigenvectors.T
        idxs = np.argsort(eigenvalues)[::-1]
        eigenvalues = eigenvalues[idxs]
        eigenvectors = eigenvectors[idxs]

        # 5. Store the first n_components eigenvectors (our principal components)
        self.components = eigenvectors[0:self.n_components]

    def transform(self, X):
        # Center the data
        X_centered = X - self.mean
        # Project data onto the principal components
        return np.dot(X_centered, self.components.T)

# --- Testing the from-scratch implementation ---
# Use the same data as the sklearn example
np.random.seed(42)
X = np.dot(np.random.rand(2, 2), np.random.randn(2, 200)).T

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Fit our custom PCA
my_pca = MyPCA(n_components=1)
my_pca.fit(X_scaled)
X_my_pca = my_pca.transform(X_scaled)

print("--- From-Scratch PCA ---")
print("Original shape:", X_scaled.shape)
print("Reduced shape:", X_my_pca.shape)
# Note: The sign of the eigenvector can be flipped, this is normal.
# The direction is the same.
print("Principal Component (Eigenvector):", my_pca.components[0])
```

---

## 2. Factor Analysis (FA)

FA is an **unsupervised** linear technique used to describe the correlations among observed variables in terms of a smaller number of unobserved, underlying variables called **factors**.

### High-Level Concept

* **Goal:** To explain the *common variance* (shared variance) among a set of observed variables, assuming they are influenced by one or more hidden (latent) factors.
* **How it Works (Analogy):** Imagine you conduct a survey with questions about `vocabulary size`, `reading speed`, and `grammar skill`. These are your observed variables. FA tries to determine if there's a latent factor, like "Verbal Intelligence," that *causes* the scores on these three variables to be correlated. It separates the variance of each question into two parts: **common variance** (explained by the latent factor) and **unique variance** (noise or specificity unique to that question).

### Mid-Level Explanation

FA models the observed data as a linear combination of potential latent factors plus an error term.

$$ \mathbf{x} = \mathbf{L}\mathbf{f} + \mathbf{\epsilon} $$

* $\mathbf{x}$ is a vector of $p$ observed variables.
* $\mathbf{f}$ is a vector of $k$ common (latent) factors ($k < p$).
* $\mathbf{L}$ is the $p \times k$ matrix of **factor loadings**. $L_{ij}$ represents how much observed variable $i$ is "loaded" onto common factor $j$.
* $\mathbf{\epsilon}$ is a vector of $p$ unique factors or errors, assumed to be uncorrelated with each other and with the common factors.

**Key Difference from PCA:**
* **PCA** aims to explain the **total variance** in the data. The components are mathematical constructs.
* **FA** aims to explain the **common variance** (covariance/correlation). The factors are assumed to be real, underlying causal variables.

#### Library Implementation (`scikit-learn`)

```python
import numpy as np
from sklearn.decomposition import FactorAnalysis
from sklearn.preprocessing import StandardScaler

# Generate data where two latent factors influence 5 observed variables
np.random.seed(42)
n_samples, n_features, n_factors = 1000, 5, 2
# Latent variables
latents = np.random.randn(n_samples, n_factors)
# Factor loadings (how latents influence observed vars)
loadings = np.array([
    [0.9, 0.1],
    [0.8, 0.2],
    [0.1, 0.9],
    [0.2, 0.8],
    [0.5, 0.5]
])
# Observed variables = loadings * latents + noise
X = np.dot(latents, loadings.T) + np.random.randn(n_samples, n_features) * 0.1

# Standardize
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Initialize and fit Factor Analysis
fa = FactorAnalysis(n_components=2, random_state=0)
X_fa = fa.fit_transform(X_scaled) # This gives the factor scores

print("Original shape:", X_scaled.shape)
print("Reduced shape (factor scores):", X_fa.shape)

# The factor loadings matrix (L) is the key output
print("\nFactor Loadings (L matrix):")
print(np.round(fa.components_.T, 2))
# We can see Var1 & Var2 load on Factor 1
# Var3 & Var4 load on Factor 2
# Var5 loads on both
```

### Low-Level: Math and From-Scratch Code

#### Mathematical Formulation

The core assumption of FA is that the covariance matrix of the observed variables, $\mathbf{\Sigma}$, can be decomposed as:

$$ \mathbf{\Sigma} = \mathbf{L}\mathbf{L}^T + \mathbf{\Psi} $$

* $\mathbf{\Sigma}$ is the $p \times p$ covariance matrix of the observed variables.
* $\mathbf{L}$ is the $p \times k$ factor loading matrix.
* $\mathbf{\Psi}$ (Psi) is a $p \times p$ diagonal matrix of **uniquenesses** (or unique variances, $\epsilon_i$). The diagonal elements represent the portion of the variance of each variable that is *not* explained by the common factors.

The diagonal of $\mathbf{L}\mathbf{L}^T$ is called the **communality** for each variable—the proportion of its variance explained by the common factors.
$$ \text{Communality}_i + \text{Uniqueness}_i = \text{Total Variance}_i (=1 \text{ if standardized}) $$

Solving for $\mathbf{L}$ and $\mathbf{\Psi}$ is complex and typically requires iterative methods like Maximum Likelihood Estimation (MLE) or **Principal Axis Factoring (PAF)**. We will implement PAF.

**Principal Axis Factoring (PAF) Algorithm:**
1.  **Estimate initial communalities.** A common starting point is the squared multiple correlation (SMC) of each variable with all others. For simplicity, we can start with `1 - 1/diag(inv(R))`, where `R` is the correlation matrix.
2.  Replace the diagonal of the correlation matrix `R` with these communality estimates. This gives a "reduced" correlation matrix, `R_reduced`.
3.  Perform an eigenvalue decomposition on `R_reduced`.
4.  Calculate a new factor loading matrix $\mathbf{L}$ using the $k$ largest eigenvalues and their corresponding eigenvectors. $\mathbf{L} = \mathbf{V}_k \sqrt{\mathbf{D}_k}$ where $\mathbf{V}_k$ are the eigenvectors and $\mathbf{D}_k$ is a diagonal matrix of eigenvalues.
5.  Calculate new communality estimates from the new loading matrix: $\text{communality}_i = \sum_{j=1}^k L_{ij}^2$.
6.  Repeat steps 2-5 until the communality estimates converge.

#### From-Scratch Implementation (PAF)

```python
import numpy as np

class MyFactorAnalysis:
    def __init__(self, n_factors, max_iter=100, tol=1e-4):
        self.n_factors = n_factors
        self.max_iter = max_iter
        self.tol = tol
        self.loadings_ = None

    def fit(self, X):
        # 1. Standardize data and get correlation matrix
        X_std = (X - np.mean(X, axis=0)) / np.std(X, axis=0)
        R = np.corrcoef(X_std, rowvar=False)
        
        # 2. Initial communality estimates (SMC)
        # For simplicity, we'll use a simpler starting point if inv fails
        try:
            R_inv_diag = np.diag(np.linalg.inv(R))
            communalities = 1 - 1 / R_inv_diag
        except np.linalg.LinAlgError:
            communalities = np.ones(R.shape[0]) * 0.5

        old_communalities = np.zeros_like(communalities)

        for i in range(self.max_iter):
            if np.sum((communalities - old_communalities)**2) < self.tol:
                break
            
            old_communalities = np.copy(communalities)

            # 3. Replace diagonal with communalities
            R_reduced = np.copy(R)
            np.fill_diagonal(R_reduced, communalities)

            # 4. Eigen decomposition
            eigenvalues, eigenvectors = np.linalg.eig(R_reduced)
            
            # Sort and select top k factors
            idxs = np.argsort(eigenvalues)[::-1]
            eigenvalues = eigenvalues[idxs][:self.n_factors]
            eigenvectors = eigenvectors[:, idxs][:, :self.n_factors]
            
            # Ensure eigenvalues are non-negative for sqrt
            eigenvalues[eigenvalues < 0] = 0

            # 5. Calculate new loadings
            self.loadings_ = eigenvectors @ np.diag(np.sqrt(eigenvalues))

            # 6. Calculate new communalities
            communalities = np.sum(self.loadings_**2, axis=1)

        if i == self.max_iter - 1:
            print("Warning: Factor Analysis did not converge.")

# --- Testing the from-scratch implementation ---
# Use the same data as the sklearn example
np.random.seed(42)
n_samples, n_features, n_factors = 1000, 5, 2
latents = np.random.randn(n_samples, n_factors)
loadings = np.array([[0.9, 0.1], [0.8, 0.2], [0.1, 0.9], [0.2, 0.8], [0.5, 0.5]])
X = np.dot(latents, loadings.T) + np.random.randn(n_samples, n_features) * 0.1

my_fa = MyFactorAnalysis(n_factors=2)
my_fa.fit(X)

print("\n--- From-Scratch Factor Analysis (PAF) ---")
# Note: Factor signs and order might be flipped. This is called "Factor Indeterminacy" and is normal.
# We can try to align them for better comparison.
print("Factor Loadings (L matrix):")
print(np.round(my_fa.loadings_, 2))
```

---

## 3. Linear Discriminant Analysis (LDA)

LDA is a **supervised** linear technique used to find a feature subspace that maximizes the separability between two or more classes.

### High-Level Concept

* **Goal:** To find a new set of dimensions (axes) that best separate the known classes in the data.
* **How it Works (Analogy):** Imagine a 2D scatter plot with two clusters of points, 'red' and 'blue'. PCA would find the axis of greatest overall spread, which might not be good for telling red from blue. LDA, because it knows the class labels, will specifically find the axis that, when you project the points onto it, makes the red and blue clusters as far apart as possible and each cluster as tight (low variance) as possible.

### Mid-Level Explanation

LDA aims to find a transformation that maximizes the ratio of **between-class variance** to **within-class variance**.

* **Between-Class Variance:** How far apart are the means (centroids) of the different classes? We want this to be large.
* **Within-Class Variance:** How spread out is the data within each individual class? We want this to be small.

The number of dimensions LDA can reduce to is at most $c-1$, where $c$ is the number of classes. For a binary classification problem, LDA reduces the data to 1 dimension.

#### Library Implementation (`scikit-learn`)

```python
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt

# 1. Generate sample data with 3 classes
X, y = make_classification(n_samples=500, n_features=2, n_informative=2,
                           n_redundant=0, n_clusters_per_class=1,
                           n_classes=3, random_state=42)

# 2. Initialize and fit LDA
# Reduce to c-1 = 3-1 = 2 dimensions (though we start with 2D, so this shows the new axes)
# If we had more features, we would set n_components=2
lda = LinearDiscriminantAnalysis(n_components=2)
X_lda = lda.fit_transform(X, y)

print("Original shape:", X.shape)
print("Reduced shape:", X_lda.shape)

# Plotting
plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', edgecolor='k')
plt.title("Original Data")

plt.subplot(1, 2, 2)
plt.scatter(X_lda[:, 0], X_lda[:, 1], c=y, cmap='viridis', edgecolor='k')
plt.title("Data Projected by LDA")
plt.xlabel("LD1")
plt.ylabel("LD2")
plt.show()
```

### Low-Level: Math and From-Scratch Code

#### Mathematical Formulation

Let's define two scatter matrices:

1.  **Within-Class Scatter Matrix ($S_W$)**: Measures the spread of data within each class.
    $$ S_W = \sum_{i=1}^{c} \sum_{\mathbf{x} \in D_i} (\mathbf{x} - \mathbf{\mu}_i)(\mathbf{x} - \mathbf{\mu}_i)^T $$
    Where $c$ is the number of classes, $D_i$ is the set of samples for class $i$, and $\mathbf{\mu}_i$ is the mean vector for class $i$.

2.  **Between-Class Scatter Matrix ($S_B$)**: Measures the spread between the class means.
    $$ S_B = \sum_{i=1}^{c} N_i (\mathbf{\mu}_i - \mathbf{\mu})(\mathbf{\mu}_i - \mathbf{\mu})^T $$
    Where $N_i$ is the number of samples in class $i$, and $\mathbf{\mu}$ is the overall mean of all data.

**Objective:** Find a transformation matrix $\mathbf{W}$ that maximizes the ratio of the determinant of the between-class scatter to the within-class scatter in the transformed space.

$$ J(\mathbf{W}) = \frac{|\mathbf{W}^T S_B \mathbf{W}|}{|\mathbf{W}^T S_W \mathbf{W}|} $$

This optimization problem can be solved by finding the eigenvectors of the matrix $S_W^{-1}S_B$. This is a **generalized eigenvalue problem**. The eigenvectors corresponding to the largest eigenvalues are the linear discriminants (our new axes).

$$ S_W^{-1}S_B \mathbf{w} = \lambda \mathbf{w} $$

The columns of our transformation matrix $\mathbf{W}$ are the $c-1$ eigenvectors corresponding to the largest eigenvalues.

#### From-Scratch Implementation

```python
import numpy as np

class MyLDA:
    def __init__(self, n_components):
        self.n_components = n_components
        self.linear_discriminants = None

    def fit(self, X, y):
        n_features = X.shape[1]
        class_labels = np.unique(y)

        # 1. Calculate Scatter Matrices
        # Calculate overall mean
        mean_overall = np.mean(X, axis=0)
        
        # Initialize S_W and S_B
        S_W = np.zeros((n_features, n_features))
        S_B = np.zeros((n_features, n_features))

        for c in class_labels:
            X_c = X[y == c]
            mean_c = np.mean(X_c, axis=0)
            
            # Calculate S_W
            # (X_c - mean_c).T is (p x n_c), (X_c - mean_c) is (n_c x p)
            S_W += (X_c - mean_c).T.dot(X_c - mean_c)
            
            # Calculate S_B
            n_c = X_c.shape[0]
            mean_diff = (mean_c - mean_overall).reshape(n_features, 1)
            S_B += n_c * (mean_diff).dot(mean_diff.T)

        # 2. Solve the generalized eigenvalue problem for S_W^-1 * S_B
        A = np.linalg.inv(S_W).dot(S_B)
        eigenvalues, eigenvectors = np.linalg.eig(A)

        # 3. Sort eigenvectors by descending eigenvalues
        eigenvectors = eigenvectors.T
        idxs = np.argsort(abs(eigenvalues))[::-1]
        eigenvalues = eigenvalues[idxs]
        eigenvectors = eigenvectors[idxs]

        # 4. Store the first n_components eigenvectors
        self.linear_discriminants = eigenvectors[0:self.n_components]

    def transform(self, X):
        # Project data onto the linear discriminants
        return np.dot(X, self.linear_discriminants.T)

# --- Testing the from-scratch implementation ---
# Use the same data as the sklearn example
X, y = make_classification(n_samples=500, n_features=2, n_informative=2,
                           n_redundant=0, n_clusters_per_class=1,
                           n_classes=3, random_state=42)

my_lda = MyLDA(n_components=2)
my_lda.fit(X, y)
X_my_lda = my_lda.transform(X)

print("\n--- From-Scratch LDA ---")
print("Original shape:", X.shape)
# Note: The output values can be scaled differently and signs can be flipped
# compared to sklearn, but the separating structure will be the same.
print("Reduced shape:", X_my_lda.shape)

# Plotting the result to visually confirm it works
plt.figure(figsize=(6, 6))
plt.scatter(X_my_lda[:, 0], X_my_lda[:, 1], c=y, cmap='viridis', edgecolor='k')
plt.title("Data Projected by From-Scratch LDA")
plt.xlabel("LD1")
plt.ylabel("LD2")
plt.show()
```

---

# Exercise: Test MNIST with and without Dimensionality Reduction

## As a classification Problem

```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, label_binarize
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import (classification_report, accuracy_score, f1_score,
                             confusion_matrix, roc_curve, auc)
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import seaborn as sns
from itertools import cycle

# --- Helper Functions ---

def evaluate_model(model, X_train, y_train, X_test, y_test):
    """
    Trains a model and returns key performance metrics.
    Now includes Macro F1-Score.
    """
    start_time = time.time()
    model.fit(X_train, y_train)
    end_time = time.time()

    preds = model.predict(X_test)
    
    training_time = end_time - start_time
    accuracy = accuracy_score(y_test, preds)
    # Macro F1-score treats all classes equally, good for balanced datasets
    f1 = f1_score(y_test, preds, average='macro')
    
    print(f"Training time: {training_time:.4f} seconds")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Macro F1-Score: {f1:.4f}")

    return {
        'Accuracy': accuracy,
        'F1-Score (Macro)': f1,
        'Training Time (s)': training_time,
        'Predictions': preds,
        'Model': model # Return the trained model for ROC analysis
    }

# --- 1. Load and Prepare the Data ---
digits = load_digits()
X, y = digits.data, digits.target
class_names = digits.target_names
n_classes = len(class_names)

print(f"Original data shape: {X.shape}")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

results = {}
model_outputs = {} # To store results for ROC curve
# Arguments for the base Logistic Regression model, without multi_class
classifier_args = {'solver': 'liblinear', 'random_state': 42}

# --- 2. Baseline: Classification on Original Scaled Data ---
print("\n--- Baseline: Training on all 64 scaled features ---")
# Wrap the logistic regression model in OneVsRestClassifier for multi-class handling
baseline_model = OneVsRestClassifier(LogisticRegression(**classifier_args))
model_outputs['Baseline'] = evaluate_model(baseline_model, X_train_scaled, y_train, X_test_scaled, y_test)
results['Baseline'] = {
    'Accuracy': model_outputs['Baseline']['Accuracy'],
    'F1-Score (Macro)': model_outputs['Baseline']['F1-Score (Macro)'],
    'Training Time (s)': model_outputs['Baseline']['Training Time (s)'],
    'Features': X_train_scaled.shape[1]
}

# --- 3. Classification with PCA ---
print("\n--- Experiment 1: Using PCA for Dimensionality Reduction ---")
pca = PCA(n_components=0.95)
X_train_pca = pca.fit_transform(X_train_scaled)
X_test_pca = pca.transform(X_test_scaled)
n_pca_components = X_train_pca.shape[1]
print(f"PCA reduced features to {n_pca_components}")

pca_model = OneVsRestClassifier(LogisticRegression(**classifier_args))
model_outputs['PCA'] = evaluate_model(pca_model, X_train_pca, y_train, X_test_pca, y_test)
results['PCA'] = {
    'Accuracy': model_outputs['PCA']['Accuracy'],
    'F1-Score (Macro)': model_outputs['PCA']['F1-Score (Macro)'],
    'Training Time (s)': model_outputs['PCA']['Training Time (s)'],
    'Features': n_pca_components
}

# --- 4. Classification with LDA ---
print("\n--- Experiment 2: Using LDA for Dimensionality Reduction ---")
n_lda_components = n_classes - 1
lda = LinearDiscriminantAnalysis(n_components=n_lda_components)
X_train_lda = lda.fit_transform(X_train_scaled, y_train)
X_test_lda = lda.transform(X_test_scaled)
print(f"LDA reduced features to {X_train_lda.shape[1]}")

lda_model = OneVsRestClassifier(LogisticRegression(**classifier_args))
model_outputs['LDA'] = evaluate_model(lda_model, X_train_lda, y_train, X_test_lda, y_test)
results['LDA'] = {
    'Accuracy': model_outputs['LDA']['Accuracy'],
    'F1-Score (Macro)': model_outputs['LDA']['F1-Score (Macro)'],
    'Training Time (s)': model_outputs['LDA']['Training Time (s)'],
    'Features': n_lda_components
}

# --- 5. Final Comparison Table ---
print("\n--- Final Results Summary ---")
results_df = pd.DataFrame.from_dict(results, orient='index')
print(results_df)

# --- 6. Confusion Matrix for Best Model (LDA) ---
print("\n--- Confusion Matrix for LDA Predictions ---")
cm = confusion_matrix(y_test, model_outputs['LDA']['Predictions'])
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=class_names, yticklabels=class_names)
plt.title('Confusion Matrix for LDA Model')
plt.ylabel('Actual Label')
plt.xlabel('Predicted Label')
plt.show()

# --- 7. ROC Curves for All Models ---
print("\n--- ROC Curve Comparison ---")
# Binarize the labels for multi-class ROC analysis
y_test_bin = label_binarize(y_test, classes=range(n_classes))

plt.figure(figsize=(10, 8))

# Data structures to hold the test data for each model
X_test_dict = {
    'Baseline': X_test_scaled,
    'PCA': X_test_pca,
    'LDA': X_test_lda
}

colors = cycle(['aqua', 'darkorange', 'cornflowerblue'])
for model_name, color in zip(model_outputs.keys(), colors):
    model = model_outputs[model_name]['Model']
    X_test_data = X_test_dict[model_name]
    
    # Get prediction probabilities
    y_score = model.predict_proba(X_test_data)
    
    # Compute ROC curve and ROC area for each class
    fpr = dict()
    tpr = dict()
    roc_auc = dict()
    for i in range(n_classes):
        fpr[i], tpr[i], _ = roc_curve(y_test_bin[:, i], y_score[:, i])
        roc_auc[i] = auc(fpr[i], tpr[i])

    # Compute micro-average ROC curve and ROC area
    fpr["micro"], tpr["micro"], _ = roc_curve(y_test_bin.ravel(), y_score.ravel())
    roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])
    
    plt.plot(fpr["micro"], tpr["micro"], color=color, lw=2,
             label=f'{model_name} (AUC = {roc_auc["micro"]:0.3f})')

plt.plot([0, 1], [0, 1], 'k--', lw=2)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Multi-Class ROC Curve Comparison (Micro-Average)')
plt.legend(loc="lower right")
plt.grid(True)
plt.show()

```

## As a clustering problem

```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
from sklearn.datasets import load_digits
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score, normalized_mutual_info_score
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.manifold import TSNE

# --- Helper Function for Clustering Evaluation ---

def evaluate_clustering(X, true_labels, n_clusters):
    """
    Performs KMeans clustering and evaluates the result against true labels.
    """
    # KMeans is sensitive to initialization, n_init helps find a stable result
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    
    start_time = time.time()
    cluster_labels = kmeans.fit_predict(X)
    end_time = time.time()
    
    processing_time = end_time - start_time
    
    ari = adjusted_rand_score(true_labels, cluster_labels)
    nmi = normalized_mutual_info_score(true_labels, cluster_labels)
    
    print(f"Processing time: {processing_time:.4f} seconds")
    print(f"Adjusted Rand Index (ARI): {ari:.4f}")
    print(f"Normalized Mutual Info (NMI): {nmi:.4f}")
    
    return {
        'ARI': ari,
        'NMI': nmi,
        'Time (s)': processing_time,
        'Features': X.shape[1]
    }

# --- 1. Load and Prepare the Data ---
digits = load_digits()
# We use 'y' ONLY for evaluation at the end. It's not used for training.
X, y_true = digits.data, digits.target
n_clusters = len(np.unique(y_true))

print(f"Original data shape: {X.shape}")
print(f"Number of clusters to find: {n_clusters}")

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

results = {}

# --- 2. Baseline: Clustering on Original Data ---
print("\n--- Baseline: Clustering on all 64 features ---")
results['Baseline'] = evaluate_clustering(X_scaled, y_true, n_clusters)

# --- 3. Clustering with PCA ---
print("\n--- Experiment 1: PCA + Clustering ---")
# Using a fixed number of components for consistency
pca = PCA(n_components=0.95)
X_pca = pca.fit_transform(X_scaled)
print(f"PCA reduced features to {X_pca.shape[1]}")
results['PCA'] = evaluate_clustering(X_pca, y_true, n_clusters)

# --- 4. Clustering with LDA ---
print("\n--- Experiment 2: LDA + Clustering ---")
print("NOTE: LDA is supervised, so this is a 'cheat' that uses labels for projection.")
lda = LinearDiscriminantAnalysis(n_components=n_clusters - 1)
# Here, we use y_true to create the best possible projection for clustering
X_lda = lda.fit_transform(X_scaled, y_true)
print(f"LDA reduced features to {X_lda.shape[1]}")
results['LDA (Supervised)'] = evaluate_clustering(X_lda, y_true, n_clusters)

# --- 5. Clustering with t-SNE ---
print("\n--- Experiment 3: t-SNE + Clustering ---")
# t-SNE is computationally intensive, so it can be slow
# It's a non-linear method, great for finding cluster structures
tsne = TSNE(n_components=2, random_state=42, perplexity=30, n_iter=1000)
X_tsne = tsne.fit_transform(X_scaled)
print(f"t-SNE reduced features to {X_tsne.shape[1]}")
results['t-SNE'] = evaluate_clustering(X_tsne, y_true, n_clusters)


# --- 6. Final Comparison ---
print("\n--- Final Clustering Results Summary ---")
results_df = pd.DataFrame.from_dict(results, orient='index')
print(results_df)

# Plotting the results
fig, ax = plt.subplots(1, 2, figsize=(15, 6))
results_df[['ARI', 'NMI']].plot(kind='bar', ax=ax[0], title='Clustering Quality Scores')
ax[0].set_ylabel('Score (Higher is Better)')
ax[0].set_xticklabels(results_df.index, rotation=45, ha='right')

results_df['Time (s)'].plot(kind='bar', ax=ax[1], color='salmon', title='Processing Time')
ax[1].set_ylabel('Time (seconds)')
ax[1].set_xticklabels(results_df.index, rotation=45, ha='right')

plt.tight_layout()
plt.show()

```