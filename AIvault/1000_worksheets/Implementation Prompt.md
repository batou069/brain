Hello! Your task is to implement a 2-way Factorization Machine (FM) for regression, as described in Steffen Rendle's 2010 paper, "Factorization Machines". You must use **only the NumPy library** for all numerical operations and implement the model from scratch.

Please structure your implementation within a Python class. The focus should be on creating an efficient, vectorized implementation where possible. Below is the mathematical foundation for the model and its training process.

### **1. Model Definition and Parameters**

A 2-way Factorization Machine models the target variable `y` using a feature vector `x` by capturing both linear (1st-order) and pairwise (2nd-order) feature interactions.

The model has three sets of parameters to learn:

- A global bias: $w_0 \in \mathbb{R}$
    
- Linear weights for each feature: $\mathbf{w} \in \mathbb{R}^n$
    
- A factor matrix to model pairwise interactions: $\mathbf{V} \in \mathbb{R}^{n \times k}$
    

Here, $n$ is the number of features and $k$ is a hyperparameter defining the dimensionality of the factorization.

### **2. Prediction Function**

The core of the FM is its prediction function. To ensure an efficient implementation with linear complexity $O(kn)$, you must use the reformulated equation. The prediction $\hat{y}$ for a single feature vector $\mathbf{x}$ should be calculated using the following vectorized formula:

$\hat{y}(\mathbf{x}) = w_0 + \mathbf{w}^T \mathbf{x} + \frac{1}{2} \sum_{f=1}^{k} \left( \left( \sum_{i=1}^{n} v_{i,f}x_i \right)^2 - \sum_{i=1}^{n} v_{i,f}^2 x_i^2 \right)$

In matrix notation, this is:

$\hat{y}(\mathbf{x}) = w_0 + \mathbf{w}^T \mathbf{x} + \frac{1}{2} \sum \left( (\mathbf{V}^T \mathbf{x})^{\circ 2} - (\mathbf{V}^{\circ 2})^T (\mathbf{x}^{\circ 2}) \right)$

Where $\circ 2$ denotes the element-wise square of a vector, and the final $\sum$ sums the elements of the resulting $k$-dimensional vector.

### **3. Training with Stochastic Gradient Descent (SGD)**

You will train the model by minimizing a loss function using Stochastic Gradient Descent (SGD). For this regression task, use the **Mean Squared Error (MSE)** loss function with **L2 regularization** on the parameters $\mathbf{w}$ and $\mathbf{V}$ to prevent overfitting.

For a batch of $m$ samples, the loss $L$ is:

$L = \frac{1}{m} \sum_{j=1}^{m} (\hat{y}(\mathbf{x}_j) - y_j)^2 + \lambda_w ||\mathbf{w}||_2^2 + \lambda_V ||\mathbf{V}||_F^2$

Where $\lambda_w$ and $\lambda_V$ are regularization hyperparameters.

### **4. Gradient Calculation for SGD Updates**

To perform SGD, you need the gradient of the loss function with respect to each parameter. The update rule for any parameter $\theta$ is $\theta \leftarrow \theta - \alpha \cdot \nabla_{\theta}L$, where $\alpha$ is the learning rate.

Here are the vectorized gradients for a batch of $m$ samples, where $\mathbf{X}$ is the $m x n$ feature matrix and $\mathbf{e} = \hat{\mathbf{y}} - \mathbf{y}$ is the $m x 1$ error vector.

- **Gradient for $w_0$ (Global Bias):** $\nabla_{w_0}L = \frac{2}{m}\sum_{j=1}^{m}e_j$
- **Gradient for $w$ (Linear Weights):** $\nabla_{\mathbf{w}}L = \frac{2}{m}\mathbf{X}^T\mathbf{e} + 2\lambda_w\mathbf{w}$ 
- **Gradient for $V$ (Factor Matrix):** This gradient is best implemented by summing the individual gradients for each sample in the batch, as it cannot be fully vectorized into a single matrix operation. $\nabla_{\mathbf{V}}L = \frac{2}{m}\sum_{j=1}^{m} e_j \left( \mathbf{x}_j(\mathbf{x}_j^T\mathbf{V}) - \mathbf{V} \circ (\mathbf{x}_j^{\circ 2}\mathbf{1}_k^T) \right) + 2\lambda_V\mathbf{V}$
    

### **5. Implementation Structure**

Please implement this in a class named `FactorizationMachine`.

- The `__init__` method should initialize the model's hyperparameters and parameters.
    
    - Hyperparameters: $k$ (factor dimensions), `learning_rate`, `n_epochs`, `lambda_w`, `lambda_v`.
        
    - Parameters ($w_0$, $w$, $V$) should be initialized with small random values.
        
- A `predict(X)` method that takes a feature matrix `X` and returns the predictions.
    
- A `fit(X, y)` method that implements the SGD training loop over the specified number of epochs. This method should handle batching of the training data.
    

Please proceed with the implementation based on this mathematical framework.