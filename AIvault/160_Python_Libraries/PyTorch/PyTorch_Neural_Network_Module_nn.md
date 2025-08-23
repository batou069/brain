---
tags:
  - python
  - pytorch
  - torch
  - neural_networks
  - nn_module
  - layers
  - loss_functions
  - concept
  - example
aliases:
  - torch.nn
  - PyTorch nn.Module
  - PyTorch Layers
related:
  - "[[160_Python_Libraries/PyTorch/_PyTorch_MOC|_PyTorch_MOC]]"
  - "[[PyTorch_Tensors]]"
  - "[[PyTorch_Autograd]]"
  - "[[PyTorch_Optimizers]]"
  - "[[PyTorch_Training_Loop]]"
worksheet:
  - WS_DeepLearning_1
date_created: 2025-08-20
---
# PyTorch: Neural Network Module (`torch.nn`)

The `torch.nn` module is the foundation for building neural networks in PyTorch. It provides a set of powerful building blocks (like layers, activation functions, and loss functions) that are designed to be composed into complex models. The central class is **`nn.Module`**.

## `nn.Module`: The Base Class for All Models
When you create a custom model, you typically:
1.  Inherit from `nn.Module`.
2.  Define the layers of your network as attributes in the `__init__` method.
3.  Implement the `forward(self, x)` method, which defines how an input `x` is passed through the layers to produce an output.

## Example: Building a Simple Neural Network
Let's build a simple multi-layer perceptron (MLP) for classifying e-commerce product data (e.g., predicting a product's category based on numerical features like price, weight, and rating).

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

# 1. Define the Network Architecture by subclassing nn.Module
class ProductClassifier(nn.Module):
    def __init__(self, input_size, num_classes):
        # Call the constructor of the parent class (nn.Module)
        super(ProductClassifier, self).__init__()
        
        # Define the layers of the network
        self.fc1 = nn.Linear(input_size, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, num_classes)
        self.dropout = nn.Dropout(p=0.3)

    def forward(self, x):
        # Define the forward pass: how data flows through the layers
        x = self.fc1(x)
        x = F.relu(x)
        
        x = self.fc2(x)
        x = F.relu(x)
        x = self.dropout(x)
        
        # No activation here because nn.CrossEntropyLoss expects raw logits
        x = self.fc3(x)
        
        return x

# 2. Instantiate the model
# Assume we have 3 input features (price, weight, rating) and 5 product categories
input_features = 3
output_classes = 5
model = ProductClassifier(input_size=input_features, num_classes=output_classes)

# 3. Print the model structure
print(model)

# 4. Inspect model parameters
print("\n--- Model Parameters ---")
for name, param in model.named_parameters():
    if param.requires_grad:
        print(f"Parameter: {name}, Size: {param.size()}")

# 5. Perform a forward pass with dummy data
# Create a dummy batch of 10 products, each with 3 features
dummy_input = torch.randn(10, input_features) # (batch_size, num_features)
output_logits = model(dummy_input)

print("\nShape of output logits:", output_logits.shape) # Should be (10, 5)
print("Example output logits (first sample):\n", output_logits)```

---