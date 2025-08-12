# Keywords

## 1. Generalized Linear Model

A **Generalized Linear Model (GLM)** is a flexible framework that extends ordinary linear regression to handle different types of response variables (e.g., counts, binary outcomes) by using a link function.

- A GLM consists of three core components:

    1. **Random Component**: The probability distribution of the response variable (e.g., Normal, Poisson, Binomial).

    2. **Systematic Component**: The linear predictor, which is a linear combination of the input features (eta=beta_0+beta_1x_1+...).

    3. **Link Function**: A function g(.) that connects the expected value of the response to the linear predictor: g(E[y])=eta.

- This framework allows a single, unified theory for many important models, including Linear Regression, Logistic Regression, and Poisson Regression.

Python

```python
import statsmodels.api as sm
import numpy as np

# Example of a GLM for count data (Poisson Regression)
# We model the number of students late to class based on hours of sleep.
hours_sleep = np.array([4, 5, 5, 6, 6, 7, 7, 8, 8, 9])
students_late = np.array([5, 4, 3, 3, 2, 1, 0, 1, 0, 0])

# Add a constant for the intercept
X = sm.add_constant(hours_sleep)

# Specify the GLM:
# family=sm.families.Poisson() -> This is the Random Component.
# The Link function is automatically chosen as log for Poisson, but can be specified.
glm_poisson = sm.GLM(students_late, X, family=sm.families.Poisson())
results = glm_poisson.fit()

print(results.summary())
```

A **Generalized Linear Model (GLM)** provides a powerful extension to the familiar linear regression model. Standard linear regression is limited because it assumes the response variable is continuous and its errors are normally distributed. GLMs break free from this constraint. They work by first creating a standard linear combination of the features (the systematic component, eta=Xbeta). Then, instead of assuming this directly equals the response, it's connected to the _expected value_ of the response via a **link function**. By choosing different probability distributions for the response (the random component) and different link functions, you can create models suited for a wide variety of data types. For instance, using a Binomial distribution and a logit link function gives you Logistic Regression, perfect for binary outcomes.

---

## 2. Link function

A **link function** is the component of a GLM that connects the random, non-linear world of the response variable to the systematic, linear world of the feature effects.

- The link function, g(.), is applied to the expected value of the response variable, E[y]=mu, to make it equal to the linear predictor: $g(\mu)=X\beta$.

- This transformation allows us to model a non-linear relationship while still using a linear equation.

- For example, in Logistic Regression, the probability mu is bounded between 0 and 1. The **logit** link function, $g(\mu) = \log\left(\frac{\mu}{1 - \mu}\right)$, transforms this probability from the `[0, 1]` range to the `(-∞, +∞)` range, which can then be modeled by the unbounded linear predictor.

Python

```python
import numpy as np
import matplotlib.pyplot as plt

# The logit link function takes a probability (0 to 1) and maps it to all real numbers.
def logit_link_function(p):
    return np.log(p / (1 - p))

# Probabilities to test
probabilities = np.linspace(0.01, 0.99, 100) # Avoid 0 and 1 due to log(0)
linear_output = logit_link_function(probabilities)

# Visualize the mapping
plt.figure(figsize=(8, 4))
plt.plot(probabilities, linear_output)
plt.xlabel("Probability (μ)")
plt.ylabel("Linear Predictor (η = Xβ)")
plt.title("Logit Link Function: Mapping Probability to Linear Space")
plt.grid(True)
plt.show()
```

The **link function** is the clever bridge in a Generalized Linear Model. The model's core is a simple linear equation, eta=Xbeta, which can produce any value from negative to positive infinity. However, your target variable might be constrained—for example, a probability must be between 0 and 1. The link function's job is to transform the mean of your target variable so that it can be properly equated with the linear predictor. For a probability p, the logit link function calculates the log-odds, log(p/(1−p)), which stretches the `[0, 1]` interval to cover the entire real number line. This allows the constrained mean of the response to be "linked" to the unconstrained linear model.

---

## 3. Sigmoid

A **sigmoid function** is any mathematical function having a characteristic "S"-shaped or sigmoid curve, but it most often refers to the standard logistic function used in machine learning.

- The standard logistic function is defined as $\sigma(z) = \frac{1}{1 + e^{-z}}$.

- It takes any real-valued number $z$ and "squashes" it into a value between 0 and 1.

- This property makes it extremely useful for converting the output of a linear model into a probability.

- The sigmoid function is the inverse of the **logit** link function.

Python

```python
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Input values (output from a linear model, for example)
z = np.linspace(-10, 10, 100)
# Output probabilities
probabilities = sigmoid(z)

plt.figure(figsize=(8, 4))
plt.plot(z, probabilities)
plt.xlabel("Linear Predictor (z = Xβ)")
plt.ylabel("Probability")
plt.title("Sigmoid (Logistic) Function")
plt.grid(True)
plt.show()
```

The **sigmoid function**, specifically the logistic function sigma(z)=1/(1+e−z), is the workhorse of logistic regression. Think of it as a "probability converter." A linear model, z=Xbeta, can output any number, like -10, 0.5, or 500. This raw output isn't a valid probability. The sigmoid function takes this raw number `z` as input and elegantly squashes it into the `[0, 1]` range. Large negative inputs get mapped close to 0, large positive inputs get mapped close to 1, and an input of 0 gets mapped to exactly 0.5. It provides the perfect, smooth transition from a linear score to a probabilistic estimate.

---

## 4. Logit function

The **logit function** is the link function used in logistic regression, which calculates the $\log$ of the odds of a given probability.

- It is defined as $\text{logit}(p) = \log\left(\frac{p}{1 - p}\right)$, where $p$ is a probability.
- The term "odds" is the ratio of the probability of an event happening to the probability of it not happening, $\frac{p}{1 - p}$.
- The logit function takes a probability from the range $[0, 1]$ and maps it to the entire real number range $(-\infty, +\infty)$.
- It is the inverse of the sigmoid (logistic) function.

Python

```python
import numpy as np

# Note: This is the same as the "Link function" code example,
# as the logit is the primary link function discussed.
def logit(p):
    # Add a small epsilon to avoid log(0) for numerical stability
    epsilon = 1e-10
    p = np.clip(p, epsilon, 1 - epsilon)
    return np.log(p / (1 - p))

# Probabilities
p1 = 0.10 # low probability
p2 = 0.50 # even odds
p3 = 0.95 # high probability

# Corresponding log-odds (logit)
logit1 = logit(p1)
logit2 = logit(p2)
logit3 = logit(p3)

print(f"Logit of 0.10 (low odds): {logit1:.2f}")
print(f"Logit of 0.50 (even odds): {logit2:.2f}")
print(f"Logit of 0.95 (high odds): {logit3:.2f}")
```

The **logit function** is the mathematical engine that connects probability to the linear model in logistic regression. It takes a probability `p` and performs two steps. First, it calculates the **odds**, which is the ratio of success to failure, p/(1−p). An 80% probability means the odds are 0.8 / 0.2 = 4 (or "4 to 1"). Second, it takes the **natural logarithm** of these odds. This two-step process, log(textodds), transforms a value constrained between 0 and 1 into an unconstrained value that can span from negative to positive infinity. This unconstrained value is what a linear model can then predict.

---

## 5. Perceptron

The **Perceptron** is the simplest form of a neural network, consisting of a single neuron that takes weighted inputs, sums them, and applies a step function to produce a binary output.

- It was one of the earliest supervised learning algorithms for binary classification.

- The activation function is a simple **Heaviside step function**: if the weighted sum $z = w \cdot x + b$ is above a certain threshold (usually 0), it outputs 1; otherwise, it outputs 0.

- The Perceptron learning algorithm updates the weights only when it makes a misclassification.

- A single perceptron can only learn **linearly separable** patterns. The famous XOR problem cannot be solved by a single perceptron.

```python
import numpy as np
from sklearn.linear_model import Perceptron

# Sample data (linearly separable)
X = np.array([[1, 2], [2, 3], [3, 1], [4, 2], [-1, -2], [-2, -3], [-3, -1], [-4, -2]])
y = np.array([1, 1, 1, 1, 0, 0, 0, 0])

# Initialize and train the Perceptron model
perceptron_model = Perceptron(max_iter=100, tol=1e-3, random_state=42)
perceptron_model.fit(X, y)

# Predict a new point
new_point = np.array([[2.5, 2]])
prediction = perceptron_model.predict(new_point)

print(f"Perceptron prediction for {new_point}: {prediction[0]}")
print(f"Model weights: {perceptron_model.coef_}")
print(f"Model bias/intercept: {perceptron_model.intercept_}")
```

The **Perceptron** is a foundational algorithm in machine learning and the direct precursor to modern neural networks. It mimics a single biological neuron. It receives multiple input signals, each multiplied by a specific weight representing its importance. These weighted signals are summed up along with a bias term. The final result is then passed through a very simple decision rule: a **step function**. If the sum exceeds a certain threshold, the perceptron "fires" and outputs 1; otherwise, it outputs 0. While simple, its learning rule guarantees that if the data is linearly separable, the perceptron will find a decision boundary that perfectly separates the two classes.

---

## 6. Decision boundary

A **decision boundary** is the line or surface in the feature space that separates the different classes predicted by a classifier.

- In logistic regression, the decision boundary is typically where the predicted probability is 0.5.

- This corresponds to the point where the linear combination of inputs, $z = X \beta$, equals 0.

- For a model with two features ($x_1, x_2$), the decision boundary is a **line**. For three features, it's a **plane**, and for more, it's a **hyperplane**.

- The boundary itself is linear for logistic regression and perceptrons, but it can be non-linear for more complex models like SVMs with kernels or decision trees.

Python

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# Generate linearly separable data
X, y = make_blobs(n_samples=100, centers=2, random_state=42, cluster_std=1.2)
model = LogisticRegression().fit(X, y)

# Plot the data points
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', edgecolors='k')

# Create a mesh to plot the decision boundary
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()
xx, yy = np.meshgrid(np.linspace(xlim[0], xlim[1], 50),
                     np.linspace(ylim[0], ylim[1], 50))
Z = model.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]
Z = Z.reshape(xx.shape)

# Plot the boundary (where probability is 0.5) and the probability contours
plt.contour(xx, yy, Z, levels=[0.5], colors='red', linestyles='--')
plt.title("Decision Boundary for Logistic Regression")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()
```

A **decision boundary** is the invisible line that a classification model draws in the data to separate one class from another. Imagine plotting your data points on a 2D graph, with each class represented by a different color. The decision boundary is the line you would draw to divide the red points from the blue points. For any new data point that falls on one side of the line, the model will assign it to the red class; if it falls on the other side, it's assigned to the blue class. In logistic regression, this boundary is linear and occurs precisely where the model is most uncertain—that is, where the predicted probability of being in either class is exactly 50%.

# Questions

## 1. Why is Logistic Regression called logistic?

Logistic Regression is called "logistic" because it is based on the **logistic function**, which is another name for the sigmoid function it uses to model probabilities.

- The term "logistic" was coined in the 19th century in the context of population growth models, which exhibited the same S-shaped curve.

- The model uses a linear equation to predict the **logit** of the probability.

- The inverse of the logit function is the **logistic** (sigmoid) function.

- So, the name directly refers to the core mathematical function that defines the model's output.

Logistic Regression gets its name directly from its core component: the logistic function, $\sigma(z) = \frac{1}{1 + e^{-z}}$. This S-shaped function transforms the output of a linear equation into a value between 0 and 1, interpretable as a probability. The model predicts the logit of the probability (the log-odds), and since the logistic function is the inverse of the logit, the name became associated with the entire regression procedure.

---

## 2. Is Logistic Regression a regressor or a classifier?

Despite its name, Logistic Regression is fundamentally a **classifier**.

- Its goal is to predict a discrete, categorical outcome (e.g., Yes/No, Class A/B/C).

- The reason for the "regression" in its name is that its underlying mechanics are based on linear regression—it finds a linear relationship between the features and the _logit of the probability_ of the outcome.

- While it does produce a continuous probability (a regression-like output), this probability is then used to make a final classification decision by applying a threshold (usually 0.5).

Python

```python
from sklearn.linear_model import LogisticRegression
import numpy as np

# Sample data
X = np.array([[1], [2], [3], [4], [8], [9], [10], [11]]) # e.g., hours studied
y = np.array([0, 0, 0, 0, 1, 1, 1, 1]) # 0 = Fail, 1 = Pass

model = LogisticRegression()
model.fit(X, y)

# It predicts a continuous probability...
prob_output = model.predict_proba([[5.5]])
print(f"Probability output for 5.5 hours: {prob_output}")

# ...but its final output is a discrete class.
class_output = model.predict([[5.5]])
print(f"Classification output for 5.5 hours: Class {class_output[0]}")
```

Logistic Regression is a **classifier**, which is one of the most confusing naming conventions in machine learning. The confusion arises because the algorithm's internal machinery looks very much like linear regression. It calculates a weighted sum of inputs to produce a score. However, its final purpose is not to predict that score, but to use that score to estimate the probability of a data point belonging to a certain class. This probability is then used to assign a discrete class label (like "spam" or "not spam"), making it a classification algorithm.

---

## 3. The choice of sigmoid function seems arbitrary. What makes this function so particular?

The choice of the sigmoid function is not arbitrary; it's chosen because it is the **inverse of the logit link function**, which has excellent statistical and mathematical properties.

- **Probabilistic Interpretation**: The logit function models the log-odds of an event, which is a natural way to represent class probability in the context of GLMs and the binomial distribution. The sigmoid function directly translates the model's linear output back into this probability.

- **Differentiability**: The sigmoid function has a very simple and convenient derivative: sigma′(z)=sigma(z)(1−sigma(z)). This makes the gradient calculations required for optimization (like gradient descent) mathematically clean and computationally efficient.

- **Smoothness**: It provides a smooth, gradual transition between 0 and 1, which is a desirable property for modeling probabilities that change in response to feature values.

The sigmoid function is special for two main reasons. First, it has a direct, meaningful statistical interpretation: it's the inverse of the logit (log-odds) function. In the framework of Generalized Linear Models, the logit is the canonical link function for data following a Binomial distribution, making the sigmoid the natural choice for converting a linear model's output back to a probability. Second, it's mathematically convenient. Its derivative is exceptionally simple and can be expressed in terms of the function itself, which simplifies the math and speeds up the optimization process used to train the model.

---

## 4. What happens if you replace sigmoid with another function? What other link functions can/should you use and when?

If you replace the sigmoid function, you essentially create a different type of binary classification model with different assumptions.

- Replacing sigmoid changes the link function that connects the linear predictor to the class probability.

- For example, using the cumulative distribution function (CDF) of the standard normal distribution instead of the sigmoid function results in a **Probit Regression** model.

- The choice of function affects the model's assumptions about the rate at which probabilities change and can make it more or less sensitive to outliers or misclassifications.

**Other link functions and when to use them:**

- **Probit**: Uses the normal CDF as the link. It's very similar to logit/sigmoid but assumes the underlying latent variable is normally distributed. The tails approach 0 and 1 slightly faster than the logistic function. It's often used in econometrics.

- **Cauchit**: Uses the Cauchy distribution's CDF. This link has much "heavier" tails, making the model more robust to outliers or extreme misclassifications, as it's less confident in its predictions for points far from the boundary.

- **Complementary Log-Log (cloglog)**: Asymmetric. Useful when the probability of one class approaches 0 or 1 much faster than the other. For example, modeling the probability of an event that is very rare or very common.

If you swap the sigmoid function for another S-shaped curve, you're fundamentally changing the assumed relationship between your features and the outcome probability. Using the normal distribution's CDF gives you **Probit Regression**, which is very similar to Logistic Regression but can produce slightly different results, especially with imbalanced data. The choice of link function depends on your assumptions about the data. If you believe the underlying probability distribution is symmetric, **logit** (for logistic regression) and **probit** are standard choices. If you suspect an asymmetric relationship—for instance, where the probability of an event happening increases slowly at first and then very rapidly—the **complementary log-log** (cloglog) link might be more appropriate.

---

## 5. Can you generalize Logistic Regression for multiclass/multilabel classification?

Yes, Logistic Regression can be generalized for both **multiclass** (choose one of N labels) and **multilabel** (choose any of N labels) classification.

- **Multiclass Classification**:

  - **One-vs-Rest (OvR)** or **One-vs-All (OvA)**: This strategy trains `N` separate binary logistic regression classifiers, one for each class against all other classes. For a new data point, the classifier with the highest confidence score wins.

  - **Multinomial (Softmax) Regression**: This is a direct generalization. It uses the softmax function instead of the sigmoid to output a probability distribution over all `N` classes simultaneously. It's often more theoretically sound and computationally efficient than OvR.

- **Multilabel Classification**:

  - This is typically handled by training `N` independent binary logistic regression classifiers, one for each label. Each classifier decides whether its specific label should be applied to the data point, and multiple labels can be assigned.

Python

```python
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification

# Create a multiclass dataset (3 classes)
X, y = make_classification(n_samples=100, n_features=10, n_informative=5,
                           n_redundant=0, n_classes=3, n_clusters_per_class=1,
                           random_state=42)

# One-vs-Rest (OvR) approach
ovr_model = LogisticRegression(multi_class='ovr', solver='liblinear')
ovr_model.fit(X, y)
print(f"OvR Prediction for first sample: {ovr_model.predict(X[0].reshape(1, -1))}")

# Multinomial (Softmax) approach
softmax_model = LogisticRegression(multi_class='multinomial', solver='lbfgs')
softmax_model.fit(X, y)
print(f"Softmax Prediction for first sample: {softmax_model.predict(X[0].reshape(1, -1))}")
```

Logistic Regression is easily extended beyond simple binary problems. For **multiclass classification**, where an item can only belong to one of three or more classes (e.g., classifying a news article as "Sports," "Politics," or "Technology"), you can use two main strategies. The **One-vs-Rest (OvR)** approach builds a separate binary classifier for each class to distinguish it from all others. A more elegant solution is **Multinomial Regression**, which uses the softmax function to directly output a single probability distribution across all classes. For **multilabel classification**, where an item can have multiple labels (e.g., a movie tagged as "Action," "Comedy," and "Sci-Fi"), the standard approach is to train independent binary classifiers for each possible label.

---

## 6. What if the two classes you are trying to classify are not linearly separable?

If the classes are not linearly separable, a standard Logistic Regression model will fail to find a perfect boundary and will have a low accuracy.

- The model will find the "best fit" linear boundary that minimizes the loss, but this line will inevitably misclassify some points.

- **Solution 1: Feature Engineering**: Create non-linear features. For example, by adding **polynomial features** (e.g., x_12,x_22,x_1x_2), you can create a linear boundary in a higher-dimensional space, which corresponds to a non-linear (e.g., circular or curved) boundary in the original feature space.

- **Solution 2: Use a Kernel**: This is the principle behind Support Vector Machines (SVMs). While not logistic regression, the "kernel trick" implicitly maps data to a higher dimension to find a linear separator.

- **Solution 3: Use a Non-linear Model**: Switch to a model that can inherently learn non-linear boundaries, such as a Decision Tree, Random Forest, or a Neural Network.

Python

```python
from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline

# Create non-linearly separable data (two concentric circles)
X, y = make_circles(n_samples=100, factor=0.5, noise=0.1, random_state=42)

# 1. Standard Logistic Regression fails
model_linear = LogisticRegression().fit(X, y)
print(f"Accuracy with standard LR: {model_linear.score(X, y):.2f}")

# 2. Logistic Regression with Polynomial Features succeeds
# Create a pipeline to first create degree-3 polynomial features, then classify
model_poly = Pipeline([
    ('poly', PolynomialFeatures(degree=3)),
    ('clf', LogisticRegression())
])
model_poly.fit(X, y)
print(f"Accuracy with Polynomial LR: {model_poly.score(X, y):.2f}")
```

A standard logistic regression model can only draw a straight line (or a flat plane) as its decision boundary. If your data classes can't be separated by such a line (e.g., one class forms a circle inside another), the model will perform poorly. The most common way to solve this while still using logistic regression is through **feature engineering**. By creating new features from your existing ones, such as polynomial terms (like x2 and y2), you effectively transform the feature space. A straight-line boundary in this new, higher-dimensional space can correspond to a curved or circular boundary in the original space, allowing the model to correctly separate the classes. Alternatively, you could switch to a more powerful, non-linear classifier like a Random Forest or a neural network.

---

## 7. How and when would you choose the Decision Boundary threshold?

You would adjust the decision boundary threshold away from the default of 0.5 when you need to prioritize either **Precision** or **Recall** due to imbalanced costs of misclassification.

- **Default Threshold**: By default, the threshold is 0.5. If the predicted probability is > 0.5, the sample is classified as class 1; otherwise, it's class 0.

- **When to Change**: Change the threshold when False Positives and False Negatives have different business costs.

  - **Increase threshold (e.g., to 0.8)**: To increase **Precision**. You become more selective about classifying as positive. This is useful when the cost of a False Positive is high (e.g., diagnosing a healthy person with a severe disease). You reduce False Positives but increase False Negatives.

  - **Decrease threshold (e.g., to 0.2)**: To increase **Recall**. You try to capture as many true positives as possible. This is useful when the cost of a False Negative is high (e.g., failing to detect a fraudulent transaction). You reduce False Negatives but increase False Positives.

- **How to Choose**: Use a **Precision-Recall Curve** or an **ROC Curve** to visualize the trade-off and select a threshold that meets your specific business needs.

Python

```python
from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

X, y = make_classification(n_samples=1000, n_features=10, n_classes=2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

model = LogisticRegression().fit(X_train, y_train)
y_scores = model.predict_proba(X_test)[:, 1] # Get probabilities for the positive class

precision, recall, thresholds = precision_recall_curve(y_test, y_scores)

# Plot the curve
plt.plot(thresholds, precision[:-1], label='Precision')
plt.plot(thresholds, recall[:-1], label='Recall')
plt.xlabel("Decision Threshold")
plt.title("Precision-Recall Trade-off")
plt.legend()
plt.grid(True)
plt.show()
```

The decision threshold in logistic regression is the "cut-off" probability for making a classification. While the default is 0.5, this is often not optimal. The right threshold depends entirely on the **business context** and the relative cost of different errors. For example, in airport security screening (predicting 'threat' vs 'no threat'), a False Negative (letting a threat through) is catastrophic. To minimize this, you would **lower the threshold** (e.g., to 0.1), making the system highly sensitive and flagging more items for manual inspection. Conversely, in email marketing (predicting 'will buy' vs 'won't buy'), a False Positive (sending an ad to someone who won't buy) is a low-cost error. You might **raise the threshold** (e.g., to 0.9) to only target very likely customers. The Precision-Recall curve is the ideal tool for visualizing this trade-off and picking the threshold that aligns with your specific goal.

---

## 8. Why do you need gradient descent for Logistic Regression?

Gradient Descent is needed for Logistic Regression because there is **no direct analytical (closed-form) solution** to find the optimal model weights that minimize its loss function.

- Unlike Ordinary Least Squares (OLS) in linear regression, which has the Normal Equation as a direct solution, the loss function for logistic regression (Log Loss or Binary Cross-Entropy) is more complex.

- The system of equations that results from setting the gradient of the Log Loss to zero cannot be solved algebraically for the weights (beta).

- Therefore, an iterative optimization algorithm like Gradient Descent is required to start with an initial guess and progressively step towards the set of weights that minimizes the loss.

Because there is no simple formula like the Normal Equation to directly calculate the best weights for logistic regression, we must rely on an iterative search method. **Gradient Descent** is that method. It works by calculating the "slope" (gradient) of the loss function with respect to each model weight. This slope tells us the direction of the steepest increase in error. The algorithm then takes a small step in the exact opposite direction—"downhill"—to reduce the error. By repeating this process many times, it progressively walks down the error surface until it settles at the bottom, which corresponds to the set of optimal weights that best fit the training data.

---

## 9. Is there another way to optimize this model? Can you somehow use OLS?

Yes, there are other, often more advanced, optimization methods; however, you **cannot use OLS** directly.

- **OLS is unsuitable**: OLS (Ordinary Least Squares) is designed to minimize the sum of squared errors for a continuous target variable. Applying it to a binary (0/1) target violates key assumptions (like homoscedasticity and normality of errors) and would produce a poor model that can predict probabilities outside the `[0, 1]` range.

- **Other Optimization Algorithms**: Gradient Descent is just one of many iterative optimizers. Others are often used in practice because they are more efficient:

  - **L-BFGS**: A "quasi-Newton" method that approximates the second derivative (Hessian matrix) to take more intelligent steps toward the minimum. It often converges much faster than standard gradient descent. This is the default solver in scikit-learn's `LogisticRegression`.

  - **Newton's Method**: Uses the true second derivative, which is computationally expensive but converges very quickly.

  - **SAG / SAGA**: Stochastic Average Gradient methods that are very efficient for large datasets.

You cannot use OLS to optimize logistic regression because OLS minimizes a completely different loss function (Mean Squared Error) which is inappropriate for a binary classification problem. However, Gradient Descent is far from the only iterative option. Professional software libraries like scikit-learn often use more advanced and faster optimizers by default. For example, the **L-BFGS** algorithm is a popular choice. It's a "quasi-Newton" method, meaning it not only uses the slope (first derivative) like Gradient Descent but also approximates the curvature (second derivative) of the loss function. This allows it to take more direct and intelligent steps towards the minimum, leading to much faster convergence than standard Gradient Descent.

---

## 10. Why are the logit function and the sigmoid function relevant for LR? How are they related to the logistic function?

The logit and sigmoid functions are two sides of the same coin and are central to how Logistic Regression connects a linear model to a probability. The **logistic function _is_ the sigmoid function**.

- **Relationship**: They are **inverses** of each other.

  - **Logit function**: Takes a probability and converts it into log-odds (`probability -> log-odds`). It's the **link function** that maps the output space `[0, 1]` to the linear predictor space `(-∞, +∞)`.

  - **Sigmoid (Logistic) function**: Takes log-odds (the output of the linear model) and converts it back into a probability (`log-odds -> probability`). It's the **activation or inverse link function**.

- **Relevance**:

  - The **logit** function provides the theoretical justification within the GLM framework for modeling a linear relationship with the log-odds.

  - The **sigmoid** function provides the practical mechanism for turning the model's raw linear output into a meaningful probability that can be used for classification.

The logit and sigmoid functions are the core mathematical duo of Logistic Regression. They are inverses, meaning one undoes the other. The model starts by assuming a linear relationship exists between the features and the **logit** (log-odds) of the outcome. This is the "regression" part. However, we need a probability, not log-odds. So, we apply the inverse of the logit function—which is the **sigmoid (or logistic) function**—to the linear model's output. In short: the **logit function** justifies the model's structure, and the **sigmoid function** executes the final conversion to a usable probability.

---

## 11. What are `logit(0)` and `logit(1)` ,and how does this affect us?

`logit(0)` and `logit(1)` are **undefined**, as they result in log-odds of negative and positive infinity, respectively.

- `logit(p) = log(p / (1-p))`

- `logit(1) = log(1 / 0) = log(∞) = ∞`

- `logit(0) = log(0 / 1) = log(0) = -∞`

- **How it affects us**: This mathematical property is critical for the loss function. The **Log Loss** (Binary Cross-Entropy) is `- [y * log(p) + (1-y) * log(1-p)]`.

  - If the true label `y` is 1, the loss is `-log(p)`. If the model confidently predicts a probability `p` of 0 for this sample, the loss becomes `-log(0)`, which is **infinite**.

  - Similarly, if `y` is 0 and the model predicts `p=1`, the loss is `-log(1-1) = -log(0)`, also **infinite**.

- This means the model is infinitely penalized for being perfectly confident and perfectly wrong, which creates a very strong gradient that forces the model to correct its weights.

The values `logit(0)` and `logit(1)` are undefined in standard mathematics, resolving to negative and positive infinity. This has a profound and useful effect on how logistic regression learns. The model's loss function, Log Loss, heavily penalizes predictions that are both confident and wrong. If the correct answer is '1' but the model predicts a probability of 0, the loss function effectively tries to compute `-log(0)`, resulting in an infinite penalty. This infinite penalty creates an extremely strong "learning signal" (gradient) that forces the model to drastically adjust its weights to move the prediction away from such a disastrously wrong and certain answer. It's the mathematical mechanism that punishes absolute certainty when it's wrong.

---

## 12. How would you build a GLM if the target variable is drawn from Binomial distribution? Describe a case when such a GLM might be useful

You would build this GLM by specifying the **Binomial distribution** as the random component and the **logit function** as the link function; this model is precisely Logistic Regression.

- **Random Component**: `family = Binomial()`. This tells the model that the response variable represents the number of "successes" in a fixed number of "trials."

- **Link Function**: `link = logit()`. This connects the probability of success `p` to the linear predictor via its log-odds.

- **Standard Logistic Regression** is the special case where each observation has only one trial (`n=1`).

- **Binomial Regression** is the more general case where the response can be the number of successes in `n > 1` trials.

A useful case for such a GLM:

Imagine you are a doctor testing the effectiveness of a new drug. You give the drug to 20 different groups of 50 patients each. For each group, you record the dosage level (the feature x) and the number of patients who recovered (the response y). Here, y is a count of successes out of n=50 trials and is therefore binomially distributed. A Binomial GLM (Binomial Regression) would be the perfect tool to model how the dosage level affects the proportion of patients who recover.

To build a GLM for a binomially distributed target, you specify two key components: the distribution itself (Binomial) and the link function (logit). This setup is known as **Binomial Regression**, of which standard Logistic Regression is a special case. This model is incredibly useful when your outcome isn't just a single success/failure, but a count of successes out of a known number of trials. For example, if you're an ecologist studying the effect of pollution on seed germination, you might plant 100 seeds in various soil samples with different pollution levels. Your response variable would be the _number of seeds that germinated_ out of 100 in each sample. A Binomial GLM would be the ideal model to analyze this type of proportional data.

---

## 13. What is the difference between scikit-learn's `LogisticRegression` and `SGDClassifier` with `loss='log_loss'` ?

The main difference lies in the **optimization algorithm (solver)** used to find the best model weights.

- `LogisticRegression`: Uses advanced, deterministic solvers like **'lbfgs'**, 'liblinear', or 'newton-cg' by default. These solvers consider the entire dataset at each step and often converge faster and to a more precise solution on smaller datasets.

- `SGDClassifier(loss='log_loss')`: Explicitly uses **Stochastic Gradient Descent (SGD)**. SGD is an iterative optimizer that updates the model weights using only a single sample (or a small mini-batch) at a time.

- **When to use which**:

  - `LogisticRegression` is the standard, go-to choice for most problems, especially if the dataset fits in memory. It's generally faster and more stable.

  - `SGDClassifier` is highly effective for **very large datasets** (that may not fit in memory) because it can learn incrementally. It's also useful for online learning where the model needs to be updated as new data arrives. Its performance can be very sensitive to feature scaling and hyperparameter tuning (like the learning rate).

Python

```python
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=1000, n_features=20, random_state=42)

# SGD requires scaled features for good performance
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Standard Logistic Regression with its default solver
lr = LogisticRegression(random_state=42)
lr.fit(X_scaled, y)
print(f"LR Score: {lr.score(X_scaled, y):.4f}")

# Logistic Regression implemented via Stochastic Gradient Descent
sgd_lr = SGDClassifier(loss='log_loss', random_state=42, max_iter=1000, tol=1e-3)
sgd_lr.fit(X_scaled, y)
print(f"SGD Score: {sgd_lr.score(X_scaled, y):.4f}")
    # Note: The scores are very similar, but the method to find the weights was different.
```

While both `LogisticRegression` and `SGDClassifier(loss='log_loss')` fit the same type of model, they get there using different paths. `LogisticRegression` uses powerful, batch optimization algorithms (like 'lbfgs') that look at the entire dataset to compute the next step. This is like a careful hiker planning their route by looking at a full map. It's very effective and usually converges quickly on datasets that fit in memory. `SGDClassifier`, on the other hand, uses Stochastic Gradient Descent. It's like a hiker in a dense fog who only looks at the ground right under their feet to decide which way is "down." It takes one data point, updates its weights, takes the next, and so on. This approach is much faster per step and scales incredibly well to massive datasets that can't be loaded all at once.

# Exercises

## 1. Write all the equations of a Logistic Regression

This exercise is to formalize the mathematical components of the Logistic Regression model.

- **Linear Function**: The model starts with a linear combination of the input features $x$ and weights $\beta$, plus an intercept $\beta_0$. This is the raw output, often denoted as $z$.

- **Link/Activation Function**: The linear output $z$ is passed through the sigmoid (logistic) function, $\sigma(z)$, to convert it into a probability $p$.

- **Loss Function**: The error for a single prediction is calculated using the Log Loss (Binary Cross-Entropy) function, which penalizes confident wrong answers heavily.

- **Gradient Descent Formulas**: To minimize the loss, you need the partial derivative of the loss function with respect to each weight $\beta_j$. This derivation simplifies to the error ($p - y$) times the corresponding feature value $x_j$.

### Code snippet

$$
\text{1. Linear Function (Log-odds):} \\
z = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_n x_n = \beta^T x
$$

$$
\text{2. Sigmoid Function (Predicted Probability):} \\
p = \sigma(z) = \frac{1}{1 + e^{-(\beta^T x)}}
$$

$$
\text{3. Loss Function (Binary Cross-Entropy for one sample):} \\
L(p, y) = -[y \log(p) + (1-y) \log(1-p)]
$$

$$
\text{4. Gradient of the Loss Function (for one sample w.r.t. one weight } \beta_j \text{):} \\
\frac{\partial L}{\partial \beta_j} = (p - y) x_j
$$

This exercise asks you to lay out the mathematical foundation of logistic regression. First is the **linear function**, $z = \beta^T x$, which computes a score based on a weighted sum of the input features. This score, $z$, represents the log-odds of the positive class. Second, this score is passed through the **sigmoid function**, $p = \frac{1}{1 + e^{-z}}$, to transform the log-odds into a valid probability $p$ between 0 and 1. Third, to measure the model's error, we use the **Log Loss function**, $L = -[y \log(p) + (1-y) \log(1-p)]$, which quantifies how "surprised" the model is by the true label $y$ given its predicted probability $p$. Finally, to train the model, we use gradient descent, which requires finding the partial derivative of the loss with respect to each weight. Through calculus, this derivative simplifies to a remarkably elegant form: (prediction - actual) $\times$ feature_value, or $(p - y) x_j$.

---

## 2. Implement Logistic Regression with `n` inputs and `L1` regularization

The goal is to build a working Logistic Regression classifier from scratch using only NumPy, including L1 regularization and an early stopping mechanism.

- **Initialize**: Start with a class structure. The `__init__` method should store hyperparameters like learning rate (`eta`), number of iterations, L1 penalty strength (`alpha`), and early stopping tolerance (`tol`). Initialize weights and bias to zero or small random numbers.

- **Core Functions**: Implement the `_sigmoid` function and a function to calculate the net input (`z = X @ w + b`).

- **Loss and Gradient**: The cost function must include the L1 penalty term: `Cost = LogLoss + alpha * sum(abs(weights))`. The gradient calculation must also be adjusted to include the derivative of the L1 term, which is `alpha * sign(weights)`.

- **Training Loop (`fit` method)**: Iterate a set number of times. In each iteration, calculate the output `p`, compute the cost, and update the weights and bias using the gradients. Check for early stopping by comparing the change in cost between epochs to the tolerance `tol`.

- **Prediction**: Implement `predict_proba` (returns the sigmoid output) and `predict` (returns the class label based on a 0.5 threshold).

```python
import numpy as np

class LogisticRegressionL1:
    def __init__(self, eta=0.01, n_iter=1000, alpha=0.1, tol=1e-4, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.alpha = alpha # L1 penalty strength
        self.tol = tol # Early stopping tolerance
        self.random_state = random_state
        self.w_ = None
        self.b_ = 0.

    def _sigmoid(self, z):
        return 1. / (1. + np.exp(-np.clip(z, -250, 250)))

    def fit(self, X, y):
        # Initialize weights
        self.w_ = np.zeros(X.shape[1])
        self.b_ = 0.
        self.costs_ = []
        last_cost = np.inf

        for i in range(self.n_iter):
            # 1. Calculate net input and output
            net_input = np.dot(X, self.w_) + self.b_
            output = self._sigmoid(net_input)

            # 2. Calculate gradients
            errors = (output - y)
            dw = X.T.dot(errors) / X.shape[0]
            db = np.mean(errors)

            # 3. Add L1 regularization gradient component
            dw += self.alpha * np.sign(self.w_)

            # 4. Update weights
            self.w_ -= self.eta * dw
            self.b_ -= self.eta * db

            # 5. Calculate loss and check for early stopping
            log_loss = -np.mean(y * np.log(output + 1e-9) + (1 - y) * np.log(1 - output + 1e-9))
            l1_penalty = self.alpha * np.sum(np.abs(self.w_))
            cost = log_loss + l1_penalty

            if abs(last_cost - cost) < self.tol:
                print(f"Early stopping at iteration {i}")
                break

            last_cost = cost
            self.costs_.append(cost)
        return self
```

This exercise requires you to build a classifier from the ground up. You'll create a Python class that encapsulates the model's logic. The core of the `fit` method is the gradient descent loop. In each iteration, you'll compute the model's current predicted probabilities using the sigmoid function. Then, you'll calculate the gradient (the direction of steepest error) and add the L1 regularization term, which pushes weights towards zero. You will update the model's weights by taking a small step in the opposite direction of this gradient. A key addition is early stopping: you'll monitor the cost function, and if it stops improving by a meaningful amount, you'll stop the training process to save time and prevent minor oscillations.

---

## 3. Use `sklearn.datasets.make_blobs` to create a toy dataset

This exercise is about applying and comparing your custom-built classifier with scikit-learn's professional implementation on a controlled, simple dataset.

- **Create Dataset**: Use `make_blobs` with `centers=2` to generate two distinct, linearly separable clusters of data points. This creates an ideal test case for your model.

- **Split Data**: Divide the generated data into a training set and a testing set using `train_test_split`.

- **Solve with Your Classifier**: Instantiate the `LogisticRegressionL1` class you built in the previous exercise. Train it on the training data using the `.fit()` method. Evaluate its accuracy on the test data.

- **Solve with Scikit-learn**: Import and instantiate `sklearn.linear_model.LogisticRegression`. Train it on the same training data. Evaluate its accuracy on the same test data.

- **Compare**: The accuracies should be very similar (likely identical or near-identical on this simple problem), validating that your implementation is correct.

Python

```
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression as SklearnLogisticRegression
from sklearn.metrics import accuracy_score

# 1. Create the dataset
X, y = make_blobs(n_samples=200, centers=2, random_state=42, cluster_std=2.0)

# 2. Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# 3. Solve with your custom classifier (assuming LogisticRegressionL1 class from above)
my_lr = LogisticRegressionL1(eta=0.1, n_iter=100, alpha=0.01)
my_lr.fit(X_train, y_train)
my_preds = (my_lr._sigmoid(np.dot(X_test, my_lr.w_) + my_lr.b_) >= 0.5).astype(int)
my_accuracy = accuracy_score(y_test, my_preds)
print(f"My Classifier Accuracy: {my_accuracy:.4f}")

# 4. Solve with scikit-learn's implementation
sklearn_lr = SklearnLogisticRegression(random_state=1)
sklearn_lr.fit(X_train, y_train)
sklearn_preds = sklearn_lr.predict(X_test)
sklearn_accuracy = accuracy_score(y_test, sklearn_preds)
print(f"Scikit-learn Accuracy: {sklearn_accuracy:.4f}")
```

This exercise serves as a unit test for the classifier you just built. First, you'll use scikit-learn's `make_blobs` function to generate a simple, clean dataset where two groups of points are clearly separable by a straight line. After splitting this data, you'll train your own `LogisticRegressionL1` classifier on the training portion and measure its performance on the unseen test portion. Then, you'll do the exact same thing using scikit-learn's industrial-strength `LogisticRegression` implementation. The final step is to compare the accuracy scores. If they match, it provides strong evidence that your from-scratch implementation of the algorithm, its cost function, and the gradient descent process is correct.

---

## 4. Load the 1D and 2D CSV data and apply polynomial solutions

This exercise demonstrates how to handle non-linearly separable data by creating polynomial features.

- **Load and Visualize**: Load the 1D CSV file. It will contain one feature `x` and a boolean target `y`. Plot `y` vs `x`. You'll observe that the classes are not separable by a single threshold (e.g., the positive class might be in the middle of the range).

- **Manual Polynomial Solution (1D)**: By looking at the plot, determine the shape of a curve that could separate the classes. A parabola (a degree-2 polynomial) might work. Manually write an equation like ax2+bx+c=0 and find coefficients `a, b, c` that correctly classify all points.

- **Scikit-learn Polynomial Solution (1D)**: Use a `Pipeline`. The first step will be `PolynomialFeatures(degree=2)` to automatically create the x2 term. The second step will be `LogisticRegression`. Train this pipeline and verify it achieves 100% accuracy. Find the lowest degree that works.

- **Repeat for 2D**: Repeat the entire process for the 2D dataset. Visualization will now be a 2D scatter plot. The manual solution will be an equation of a circle or ellipse. The scikit-learn pipeline will require finding the lowest degree of polynomial features (e.g., x2,y2,xy) that allows the logistic regression to draw a separating boundary.

- **Observe Higher Degrees**: Increase the polynomial degree significantly (e.g., to 10 or 20) and observe how the decision boundary becomes overly complex and contorted. This demonstrates the concept of **overfitting**.

Python

```
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt

# This conceptual code focuses on the 1D case
# 1. Load and visualize (assuming 'data_1d.csv' exists)
# data = pd.read_csv('data_1d.csv')
# plt.scatter(data['x'], data['y'], c=data['y'])
# plt.show() # You would see something like a U-shape for one class.

# 2. Use scikit-learn's Pipeline to find the solution
# X = data[['x']]
# y = data['y']
# The key part of the solution is this pipeline:
poly_lr_pipeline = Pipeline([
    ('poly', PolynomialFeatures(degree=2)), # We hypothesize degree 2 is needed
    ('clf', LogisticRegression())
])
# poly_lr_pipeline.fit(X, y)
# accuracy = poly_lr_pipeline.score(X, y)
# print(f"Accuracy with degree 2 polynomial features: {accuracy}")
```

This exercise is designed to give you a deep, intuitive understanding of how to solve non-linear classification problems. After loading and visualizing the 1D data, you will notice that a simple vertical line cannot separate the classes. You'll need a curve. By manually constructing a quadratic equation, you'll see how a parabola can serve as a decision boundary. You'll then automate this process using scikit-learn's `PolynomialFeatures` combined with `LogisticRegression` in a `Pipeline`, confirming that a degree-2 polynomial is sufficient. Repeating this for the 2D data will extend this concept from a parabola to a circle or ellipse. Finally, by experimenting with excessively high degrees, you will visually see the model's decision boundary contort to fit every single training point, a classic illustration of overfitting.

---

## 5. Solve the Montreal Bike Lanes dataset

This is a real-world data science problem requiring you to apply the full classification workflow to predict the presence of cyclists on a bike path.

- **Load and EDA**: Load the dataset. The target is likely a column indicating if the bike count on a given day is above a certain threshold (or you might need to create this binary target yourself, e.g., `is_busy = count > median_count`). Perform Exploratory Data Analysis (EDA). Pay close attention to the `Date` column and any weather-related features.

- **Feature Engineering**: This is the most critical step. The `Date` column is not usable as-is. You must extract meaningful features from it, such as:

  - Day of the week (e.g., `pd.to_datetime(df['Date']).dt.dayofweek`)

  - Month

  - Is it a weekend?

  - Season

- **Preprocessing**: Select your features (the ones you engineered plus relevant weather data). Handle any missing values. Scale numerical features using `StandardScaler`.

- **Modeling**: Split your data into training and testing sets. Train a `LogisticRegression` model.

- **Evaluation and Interpretation**: Evaluate the model's accuracy, precision, and recall on the test set. Look at the model's coefficients (`model.coef_`) to understand which features are most important for predicting cyclist presence. For example, you would expect "is_weekend" and sunny weather to have positive coefficients, while rain and cold temperatures would have negative coefficients.

Python

```
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Conceptual code for the workflow
# 1. Load data
df = pd.read_csv('montreal_bike_lanes.csv')

# 2. Create target variable and engineer features
df['date'] = pd.to_datetime(df['Date'])
df['day_of_week'] = df['date'].dt.dayofweek
df['month'] = df['date'].dt.month
median_count = df['total_cyclists'].median()
df['is_busy'] = (df['total_cyclists'] > median_count).astype(int)

# 3. Define features and preprocessor
numeric_features = ['temperature', 'humidity']
categorical_features = ['day_of_week', 'month']
preprocessor = ColumnTransformer(transformers=[
    ('num', StandardScaler(), numeric_features),
    ('cat', OneHotEncoder(), categorical_features)])

# 4. Create the full pipeline
model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression())
])

# 5. Split data and train
X = df[numeric_features + categorical_features]
y = df['is_busy']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model_pipeline.fit(X_train, y_train)
print(f"Model accuracy: {model_pipeline.score(X_test, y_test)}")
```

This exercise challenges you to apply your skills to a practical, real-world dataset. Your goal is to predict whether a bike lane in Montreal will be busy on a given day. The key to success is **feature engineering**. You cannot simply feed the raw data into the model. You must transform the 'Date' column into useful predictive features like the month, the day of the week, and whether it's a weekend. You will then combine these with weather data, preprocess everything correctly (e.g., scaling numbers, one-hot encoding categories), and build a `Pipeline` to train a logistic regression model. Finally, you will evaluate your model's performance and interpret its coefficients to draw conclusions about what factors drive cyclist traffic in Montreal.



# Math Stuff

Linear Function: $t=\beta_0+\beta_1x$
Link Function: $g(p)=logit\ p=ln(\frac{p}{1-p})$
Loss Function: $l=\sum_{i=0}$
Gradient Descent:

##### 1. Linear Function (Log-odds):
$$z = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_n x_n = \beta^T x$$
##### 2. Sigmoid Function (Predicted Probability):

$$p = \sigma(z) = \frac{1}{1 + e^{-(\beta^T x)}}$$
##### 3. Loss Function (Binary Cross-Entropy for one sample):
$$L(p, y) = -[y \log(p) + (1-y) \log(1-p)] (optional: + Lasso)$$
##### 4. Linear Function (Log-odds) for one sample w.r.t. one weight:
$$\frac{\partial L}{\partial \beta_j} = \sum_{i=0}^{n} (p_i - y_i) x_j$$
$$\frac{\partial L}{\partial \beta_j} = \frac{\partial L}{\partial p}*\frac{\partial p}{\partial z}* \frac{\partial z}{\partial \beta_j}$$
$$\frac{\partial L}{\partial p} = \frac{1-y}{1-p}-\frac{y}{p} = \frac{p-y}{p-p^2}$$
$$\frac{\partial p}{\partial z} = \frac{e^{-z}}{(1+e^{-z})^2} = p (\frac{e^{-z}}{1+e^{-z}})=p\ * (1-p) $$
$$\frac{\partial z}{\partial \beta_j} = x_j$$
$$\frac{\partial L}{\partial p}*\frac{\partial p}{\partial z}* \frac{\partial z}{\partial \beta_j} = x_j * p * (1-p) * \frac{p-y}{p-p^2}= x_j * {p-y} (optional: + Lasso) $$