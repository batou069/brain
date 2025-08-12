---
tags:
  - python
  - tensorflow
  - tf
  - tfjs
  - javascript
  - web_ml
  - browser_ml
  - nodejs_ml
  - concept
  - example
aliases:
  - TF.js
  - TensorFlow.js
  - JavaScript TensorFlow
related:
  - "[[_TensorFlow_MOC|_TensorFlow_MOC]]"
  - "[[TensorFlow_Saving_Loading_Models|Saving Keras/TF Models]]"
  - "[[Deep_Learning_Overview]]"
worksheet:
  - WS_DeepLearning_1
date_created: 2025-06-11
---
# TensorFlow.js (TF.js)

**TensorFlow.js (TF.js)** is an open-source hardware-accelerated JavaScript library for training and running machine learning models directly in the browser or in Node.js. It brings the power of TensorFlow and deep learning to the JavaScript ecosystem.

## Core Purpose and Benefits
-   **ML in the Browser:** Enables running ML models directly in the user's web browser.
    -   **Interactivity:** Models can interact with webpage content, user inputs (camera, microphone).
    -   **Privacy:** User data can remain client-side, not needing to be sent to a server for inference.
    -   **Low Latency:** Inference happens locally, avoiding network delays.
    -   **Accessibility:** No complex server-side setup needed for users to experience ML features.
-   **ML in Node.js:** Allows for server-side JavaScript ML applications using TensorFlow.
-   **Run Existing Models:** Convert pre-trained TensorFlow (Python) models to a format usable by TensorFlow.js.
-   **Train Models from Scratch:** Define, train, and run models entirely in JavaScript using an API similar to Keras.
-   **Hardware Acceleration:** Can leverage WebGL for GPU acceleration in the browser, and TensorFlow's C++ backend in Node.js.

## Key Components and APIs of TensorFlow.js

[list2tab|#TF.js Components]
- Core API (`@tensorflow/tfjs-core`)
    -   Low-level linear algebra operations (similar to NumPy/TensorFlow Python Core).
    -   Defines `tf.Tensor` objects in JavaScript.
    -   Provides operations for tensor manipulation, math, etc.
- Layers API (`@tensorflow/tfjs-layers`)
    -   A high-level API for building neural networks, modeled directly after the [[Keras_API_in_TensorFlow|Keras API]].
    -   Define models using `tf.sequential()` or the functional API `tf.model()`.
    -   Includes common layers: `tf.layers.dense()`, `tf.layers.conv2d()`, `tf.layers.lstm()`, etc.
    -   Compile models with optimizers, loss functions, and metrics.
    -   Train models using `model.fit()` or `model.fitDataset()`.
- Converter (`@tensorflow/tfjs-converter`)
    -   Tools to convert pre-trained TensorFlow SavedModels or Keras H5 models (from Python) into a format that can be loaded by TensorFlow.js.
    -   The conversion typically results in a `model.json` file (graph topology and weights manifest) and one or more binary shard files for the weights.
- Data API (`@tensorflow/tfjs-data`)
    -   Provides an API similar to `tf.data` for creating efficient input pipelines for training models in JavaScript (e.g., reading from webcams, microphones, files, DOM elements).
- Pre-trained Models (`@tensorflow-models/*`)
    -   A collection of pre-trained models for common tasks, ready to use in JavaScript applications.
    -   Examples: MobileNet (image classification), PoseNet (pose estimation), Coco-SSD (object detection), Universal Sentence Encoder (text embeddings), Speech Commands.
- Backends
    -   TensorFlow.js can run on different backends for computation:
        -   `tfjs-backend-cpu`: Runs on CPU (JavaScript).
        -   `tfjs-backend-webgl`: Uses WebGL for GPU acceleration in the browser (most common for browsers).
        -   `tfjs-backend-wasm`: Uses WebAssembly for CPU acceleration, can be faster than plain JS.
        -   `tfjs-node` (for Node.js): Binds to the TensorFlow C library for native speed on CPU.
        -   `tfjs-node-gpu` (for Node.js): Binds to TensorFlow C library with GPU support (CUDA).

## Workflow Examples

### 1. Using a Pre-trained Model (e.g., MobileNet for Image Classification in Browser)
**HTML:**
```html
<!-- <!DOCTYPE html>
<html>
<head>
    <title>TF.js Image Classification</title>
    <!-- Load TensorFlow.js and MobileNet model -->
    <!-- <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@latest/dist/tf.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@tensorflow-models/mobilenet@latest/dist/mobilenet.min.js"></script>
</head>
<body>
    <h1>Image Classifier with TF.js</h1>
    <img id="myImage" src="path/to/your/image.jpg" width="224" height="224" alt="image to classify"/> <br/>
    <input type="file" id="imageUpload" accept="image/*" />
    <div id="predictions">Loading model and making predictions...</div>

    <script>
        const imgElement = document.getElementById('myImage');
        const predictionsElement = document.getElementById('predictions');
        const imageUpload = document.getElementById('imageUpload');
        let model;

        async function loadAndPredict() {
            if (!model) {
                predictionsElement.innerText = 'Loading MobileNet model...';
                model = await mobilenet.load(); // Load the MobileNet model
                predictionsElement.innerText = 'Model loaded.';
            }
            
            if (imgElement.src && imgElement.src !== window.location.href) { // Check if src is set and not just base URL
                 try {
                    const predictions = await model.classify(imgElement);
                    predictionsElement.innerHTML = '<h3>Predictions:</h3>';
                    predictions.forEach(p => {
                        predictionsElement.innerHTML += `${p.className} : ${p.probability.toFixed(4)}<br>`;
                    });
                } catch (e) {
                    predictionsElement.innerText = 'Error during prediction. Ensure image is loaded correctly.';
                    console.error(e);
                }
            } else {
                 predictionsElement.innerText = 'Please upload an image or ensure the default image path is correct.';
            }
        }
        
        imgElement.onload = () => { // Predict when default image loads
            loadAndPredict();
        };
        if (imgElement.complete && imgElement.naturalHeight !== 0) { // If image already loaded from cache
             loadAndPredict();
        }


        imageUpload.onchange = (event) => {
            const file = event.target.files;
            if (file) {
                const reader = new FileReader();
                reader.onload = (e) => {
                    imgElement.src = e.target.result;
                    // imgElement.onload will trigger loadAndPredict after src is set
                }
                reader.readAsDataURL(file);
            }
        };
        // Initial prediction if default image is set
        // loadAndPredict(); // Call if default image src is valid
    </script>
</body>
</html> -->
```
*(Note: For the above HTML to work, `path/to/your/image.jpg` needs to be a valid image. The file upload provides interactivity.)*

### 2. Converting a Python Keras Model and Using it in Node.js (Conceptual)
**Step A: Save Keras model in Python and Convert**
```python
# Python (e.g., in a Jupyter Notebook or script)
# import tensorflow as tf
# from tensorflow import keras

# Create and train a simple Keras model (e.g., for classifying product categories)
# model = keras.Sequential([
#     keras.layers.Dense(128, activation='relu', input_shape=(50,)), # 50 features
#     keras.layers.Dense(3, activation='softmax') # 3 product categories
# ])
# model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
# Dummy training
# X_train = np.random.rand(100, 50)
# y_train = np.random.randint(0, 3, 100)
# model.fit(X_train, y_train, epochs=1, verbose=0)

# Save the model in SavedModel format
# model.save("./my_keras_model_for_tfjs")

# Convert using tensorflowjs_converter (command-line tool)
# Install: pip install tensorflowjs
# In your terminal:
# tensorflowjs_converter --input_format=tf_saved_model \
#                        ./my_keras_model_for_tfjs \
#                        ./my_tfjs_model_output
```
This creates `model.json` and weight shard files in `./my_tfjs_model_output`.

**Step B: Load and use in Node.js**
```javascript
// Node.js script (e.g., predict.js)
// const tf = require('@tensorflow/tfjs-node'); // Or tfjs-node-gpu
// const path = require('path');
// const modelPath = `file://${path.join(__dirname, 'my_tfjs_model_output', 'model.json')}`;

// async function runPrediction() {
//     try {
//         console.log('Loading model...');
//         const model = await tf.loadLayersModel(modelPath);
//         console.log('Model loaded.');
//         model.summary(); // Print model summary

//         // Create dummy input data (batch of 1, 50 features)
//         const inputTensor = tf.tensor2d(Math.random(),);
        
//         console.log('\nMaking prediction...');
//         const prediction = model.predict(inputTensor);
//         prediction.print(); // Prints the tensor

//         const predictedClass = prediction.argMax(-1).dataSync(); // Get the class with highest probability
//         console.log(`Predicted class index: ${predictedClass}`);

//     } catch (error) {
//         console.error("Error during TF.js model execution:", error);
//     }
// }
// runPrediction();
```
To run: `node predict.js` (after `npm install @tensorflow/tfjs-node path`).

## Use Cases
-   **Interactive ML Experiences in Web Browsers:** Image recognition from webcam, real-time pose estimation, style transfer, client-side text analysis.
-   **Accessibility and Reach:** Deploy ML models to anyone with a web browser without requiring them to install specific software or send data to a server.
-   **Privacy-Preserving ML:** Perform inference on user data directly in their browser.
-   **Server-Side JavaScript ML:** Use Node.js for ML tasks like API backends, data preprocessing, or batch inference.
-   **Education:** Teaching ML concepts in a more accessible environment.

TensorFlow.js significantly expands the reach of TensorFlow models to web and JavaScript environments, enabling a wide range of new applications and interactive experiences.

---