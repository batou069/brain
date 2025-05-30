---
tags:
  - numpy
  - python
  - function
  - activation_function
  - machine_learning
  - probability
aliases:
  - Softmax Function NumPy
  - np.softmax (Conceptual - not a direct NumPy function)
related:
  - "[[NumPy_ndarray]]"
  - "[[NumPy_Universal_Functions]]" # exp, sum
  - "[[Neural_Networks]]"
  - "[[Classification_Models]]"
  - "[[Probability_Distribution]]" # Placeholder
worksheet: [WS_NumPy] # Exercise "Calculate the softmax of each vector"
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Softmax Function (Implemented with NumPy)

## Definition

The **Softmax function** is a mathematical function that converts a vector of K real numbers (often "logits" or raw scores from a model) into a probability distribution consisting of K probabilities. Each probability is in the range (0, 1], and the sum of all probabilities is equal to 1. It's widely used as the activation function in the output layer of multi-class [[Classification_Models|classification models]] in [[Machine_Learning]] and [[Neural_Networks]].

NumPy does **not** have a built-in `np.softmax()` function. It is typically implemented using existing NumPy functions like `np.exp()` and `np.sum()`.

## Formula

For a given input vector `z = [z1, z2, ..., zK]`, the softmax function `σ(z)` computes a vector `p = [p1, p2, ..., pK]` where each element `pi` is:

`pi = e^(zi) / Σ(e^(zj))` (sum over all `j` from 1 to K)

Where:
- `e^(zi)` is the exponential of the i-th element of `z`.
- `Σ(e^(zj))` is the sum of the exponentials of all elements in `z`.

## Implementation in NumPy

A common and numerically stable way to implement softmax using NumPy:

```python
import numpy as np

def softmax(x, axis=None):
    """
    Compute softmax values for each sets of scores in x.
    For numerical stability, subtract max(x) before exponentiating.
    
    Parameters:
    x (np.ndarray): Input array of scores (logits). Can be 1D or N-D.
    axis (int, optional): Axis along which softmax is computed.
                          If None, softmax is computed over the flattened array.
                          For a 2D array of shape (N, D) (N samples, D classes),
                          axis=1 computes softmax for each sample across classes.
    
    Returns:
    np.ndarray: Array of same shape as x with softmax probabilities.
    """
    # Subtracting the max for numerical stability (prevents overflow with large exponents)
    # and doesn't change the output of softmax due to e^(a-b) = e^a / e^b
    x_max = np.max(x, axis=axis, keepdims=True)
    e_x = np.exp(x - x_max)
    
    # Sum of exponentials along the specified axis
    sum_e_x = np.sum(e_x, axis=axis, keepdims=True)
    
    return e_x / sum_e_x
```

## AnyBlock Tabs: Softmax Example

[list2tab]
- 1D Vector Example
	```python
	import numpy as np
	# (Using the softmax function defined in the main text of this note)

	scores_1d = np.array() # Raw scores or logits
	probabilities_1d = softmax(scores_1d)

	print(f"Original scores (1D): {scores_1d}")
	print(f"Softmax probabilities (1D): {probabilities_1d}")
	print(f"Sum of probabilities: {np.sum(probabilities_1d)}") # Should be 1.0
	```
	**Output:**
	```
	Original scores (1D): [1. 2. 0.]
	Softmax probabilities (1D): [0.24472847 0.66524096 0.09003057]
	Sum of probabilities: 1.0
	```
- 2D Array Example (Batch of Vectors)
	```python
	import numpy as np
	# (Using the softmax function defined in the main text of this note)

	# Batch of 2 vectors, each with 3 scores
	scores_2d = np.array([
	    ,
	    
	])
	# Compute softmax along axis 1 (for each row/sample)
	probabilities_2d = softmax(scores_2d, axis=1)

	print(f"Original scores (2D):\n{scores_2d}")
	print(f"\nSoftmax probabilities (2D, along axis=1):\n{probabilities_2d}")
	print(f"\nSum of probabilities for each row: {np.sum(probabilities_2d, axis=1)}") # Should be [1. 1.]
	```
	**Output:**
	```
	Original scores (2D):
	[[1.  2.  0. ]
	 [0.5 1.5 2.5]]

	Softmax probabilities (2D, along axis=1):
	[[0.24472847 0.66524096 0.09003057]
	 [0.07832965 0.2128025  0.70886785]]

	Sum of probabilities for each row: [1. 1.]
	```

## Key Characteristics

- **Output as Probabilities:** Transforms arbitrary real-valued scores into a probability distribution over K outcomes.
- **Normalization:** The denominator `Σ(e^(zj))` normalizes the values so they sum to 1.
- **Exponentiation Amplifies Differences:** The exponential function `e^x` exaggerates differences between input scores. Larger scores get significantly higher probabilities.
- **Numerical Stability:** Subtracting the maximum value from the input scores (`x - np.max(x)`) before exponentiating is a common trick to prevent numerical overflow when dealing with very large input scores, without changing the final softmax output.
- **Derivative:** Has a convenient derivative, which is useful in training neural networks via [[Backpropagation]].

## Use Cases

- **Output Layer of Multi-class Classifiers:** Converts the raw output scores (logits) of a neural network or other model into probabilities for each class. The class with the highest probability is then chosen as the prediction.
- **Reinforcement Learning:** Used in policy gradient methods to represent a probability distribution over actions.
- **Attention Mechanisms (NLP):** Used in [[Transformers_DL|Transformer]] models to calculate attention weights.

## Related Concepts
- [[NumPy_ndarray]], [[NumPy_Universal_Functions]] (`np.exp`, `np.sum`, `np.max`)
- [[Activation_Function]] (Softmax is an activation function)
- [[Neural_Networks]], [[Classification_Models]]
- [[Probability_Distribution]]
- Logits (Raw, unnormalized scores from a model)

## Questions / Further Study
>[!question] Exercise: Calculate the softmax of each vector in a collection of vectors.
> This is demonstrated in the "2D Array Example" tab above, where `scores_2d` is a collection of vectors (each row is a vector) and `softmax(scores_2d, axis=1)` computes the softmax for each vector.

---
**Source:** Worksheet WS_NumPy, Deep Learning Book (Goodfellow, Bengio, Courville)