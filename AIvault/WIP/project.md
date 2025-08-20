# Project Briefing: A Production-Grade Movie Recommendation System

## 1. Executive Summary (The Elevator Pitch)

This project is an end-to-end, production-grade MLOps pipeline that serves personalized movie recommendations. The core of the system is a **Factorization Machine (FM) model, implemented from scratch** using only `numpy` and `scipy.sparse`, which is retrained daily on the MovieLens 1M dataset. The entire lifecycle is automated using a modern MLOps stack: **Docker** for containerization, **Airflow** for orchestration, **PostgreSQL** for data warehousing, and a **Flask** API for serving. The system is designed for scalability, reliability, and maintainability, addressing common real-world challenges like ETL bottlenecks, service dependency management, and the cold-start problem.

---

## 2. Core Technical Achievement: Factorization Machine from Scratch

A key accomplishment of this project was the from-scratch implementation of Steffen Rendle's 2010 paper on Factorization Machines. This demonstrates a first-principles understanding of the algorithm, its mathematical underpinnings, and the engineering required to make it work efficiently on sparse data.

### 2.1. Why a Factorization Machine?
Standard models like Linear Regression fail to capture interaction effects, while classic Matrix Factorization models like SVD can't incorporate side features (e.g., user age, movie genres). FMs solve both problems. They are a general-purpose regressor that excels at modeling high-order interactions in extremely sparse, high-dimensional feature spaces, which is the perfect description of a recommendation problem.

### 2.2. The Core Formula & Implementation
The model, implemented in `scripts/fm_model.py`, directly codes the 2-way FM equation:

> **ŷ(x) = w₀ + Σ(wᵢxᵢ) + ΣΣ(<vᵢ,vⱼ>xᵢxⱼ)**

-   **`w₀` (Global Bias):** A scalar that learns the average rating.
-   **`Σ(wᵢxᵢ)` (Linear Terms):** A vector `w` of weights, one for each feature. This is identical to a standard linear regression.
-   **`ΣΣ(<vᵢ,vⱼ>xᵢxⱼ)` (Interaction Terms):** This is the key innovation.
    -   Each feature `i` is assigned a k-dimensional latent vector `vᵢ`. These vectors are stored in a matrix `V` of shape `(n_features, k)`.
    -   The strength of the interaction between two features `i` and `j` is modeled as the **dot product** of their latent vectors: `<vᵢ, vⱼ>`.
    -   This approach is powerful because it allows the model to learn and generalize feature interactions even for pairs that never co-occur in the training data. For example, it can learn the interaction between a user who has never seen a "Sci-Fi" movie and the "Sci-Fi" genre by leveraging what it has learned about that user's interactions with other genres ("Action", "Thriller") and how those genres' latent vectors relate to the "Sci-Fi" vector.

### 2.3. Input & Output Deep Dive
-   **Input:** The input `X` for a single prediction is a massive, one-hot encoded binary feature vector. For a given review, it's constructed from all available features: `(user_id, movie_id, age, gender, occupation, release_year, genres...)`. This results in a vector with tens of thousands of dimensions, of which only a handful of entries are non-zero, making it **>99.9% sparse**. The implementation uses `scipy.sparse.csr_matrix` to handle this data with extreme memory efficiency.
-   **Output:** The model outputs a single floating-point number, `ŷ`, which is the predicted rating.

### 2.4. Training: Minimizing the Loss Function
The model is trained to minimize a loss function using Mini-batch Stochastic Gradient Descent (SGD).
-   **Loss Function:** The loss is the Mean Squared Error (MSE) between the predicted and actual ratings, with L2 regularization terms to prevent overfitting:
    > **Loss = (ŷ - y)² + λ_w||w||² + λ_v||V||²**
-   **Optimization:** For each batch, we compute the partial derivative (the gradient) of the loss function with respect to each model parameter (`w₀`, `w`, and `V`). We then update the parameters by taking a small step in the opposite direction of their gradient, scaled by the `learning_rate`. The gradients for the interaction term `V` are calculated efficiently without ever explicitly building the full interaction matrix, which would be computationally intractable.

### 2.5. Verification & Validation
How do we know the from-scratch implementation is correct?
1.  **Metric-based Validation:** The most direct check is observing the training process. The Mean Absolute Error (MAE) is printed every 10 epochs. A correctly implemented model will show a steady decrease in MAE as it learns.
2.  **Gradient Checking:** This is the gold standard for debugging custom ML models. It involves numerically approximating the gradient for each parameter (by slightly perturbing it and observing the change in the loss) and comparing this approximation to the analytical gradient calculated by our code. A close match provides high confidence that the backpropagation logic is correct.
3.  **Comparison with Existing Libraries:** As a final sanity check, the model's performance can be benchmarked against a well-established, optimized library like `xlearn` or `fastFM` on the same dataset. Our implementation should yield comparable accuracy metrics, validating its correctness.

---

## 3. System Architecture & Workflow

The system is a closed-loop pipeline orchestrated by Airflow:

1.  **Data Warehouse:** A PostgreSQL database holds all raw data (users, movies, reviews) and derived data products.
2.  **ETL Stage:** A daily Airflow DAG (`refresh_materialized_view`) updates a pre-computed, denormalized materialized view. This view is the single source of truth for clean training data.
3.  **Retraining Stage:** A second Airflow DAG (`retrain_fm_model`) triggers after the data is refreshed.
    *   **Load:** Loads the training data from the materialized view.
    *   **Train:** Trains a new "challenger" FM model.
    *   **Evaluate:** Compares the challenger's Mean Absolute Error (MAE) against the production "champion" model.
4.  **Deployment Stage:** If the challenger is better, it's promoted to production. The script then pre-computes personalized recommendations for all users and overwrites the `production_recommendations` table in the database.
5.  **Serving Stage:** The Flask API serves these pre-computed recommendations via a fast database lookup. It also ingests new user reviews, which are collected and merged into the main dataset during the next day's ETL run.

---

## 4. Deep Dive: Interview Q&A and Engineering Trade-offs

This section anticipates questions an interviewer might ask about the design decisions.

#### Q: Why use a Materialized View? Why not just process the data in Python with Pandas?
**Answer:** For performance and separation of concerns. Performing joins and feature engineering on 1 million+ rows in Python on every training run is an expensive bottleneck. By offloading this to a PostgreSQL Materialized View, we pre-compute the entire model-ready dataset using the database's highly optimized C-based query engine. The daily refresh is incremental and efficient. This decouples our data engineering from our machine learning. The ML pipeline's `load_data` step becomes a trivial, lightning-fast `SELECT *`, and the data transformation logic is centralized in one place (the view's DDL).

#### Q: How does your system handle the "cold start" problem for new users?
**Answer:** We use a two-tiered fallback strategy. The API's `/recommendations` endpoint first attempts to retrieve pre-computed, personalized recommendations for the given `user_id`. If the query returns no results (which it won't for a new user), it transparently executes a second, "fallback" query. This fallback query returns the most popular movies (based on the number of ratings) that the user has not yet seen. This ensures that new users get a reasonable, non-empty recommendation list, providing a good user experience until their own ratings are incorporated into the next training run.

#### Q: Your API receives 1000s of requests per second. How does it scale?
**Answer:** The key design decision for scalability was **pre-computation**. The API is not running the complex FM model on the fly. It is performing a simple, indexed `SELECT` query on the `production_recommendations` table. This is a very fast, low-latency operation that databases are built to handle. To scale further, we would:
1.  Replace the Flask development server with a production-grade WSGI server like **Gunicorn**, configured with multiple worker processes to handle concurrent requests.
2.  Run multiple replicas of the Flask API container.
3.  Place a **load balancer** (like Nginx) in front of the replicas to distribute the traffic.
Because the API is stateless and the heavy lifting is done offline by Airflow, this architecture can be scaled horizontally with ease.

#### Q: Why didn't you use the review `timestamp` as a feature?
**Answer:** That's an excellent point and a key area for future improvement. The current implementation does not model temporal effects, but the `timestamp` is a rich source of signal. It could be engineered into several powerful features:
*   **User Taste Drift:** Features like "days since user's last review" or "days since user's first review" could help the model learn how a user's taste evolves.
*   **Movie Popularity Dynamics:** Features like "days since movie release" could model how a movie's popularity waxes and wanes.
*   **Seasonal Effects:** Features like "month of review" or "day of week" could capture seasonal viewing patterns.
Incorporating these would require adding them to the materialized view and the model's feature list, but it would likely provide a significant lift in accuracy.

#### Q: Your custom FM training is CPU-intensive. How would you speed it up?
**Answer:** The >100% CPU usage indicates that the underlying `numpy` operations are already parallelized. However, the main training loop in Python is single-threaded due to the Global Interpreter Lock (GIL). To get a significant speedup, I would pursue two paths:
1.  **Parallelize the Algorithm:** Refactor the SGD implementation in `fm_model.py` to use Python's `multiprocessing` library. We could parallelize the gradient calculation step across multiple batches of data, allowing us to leverage all available CPU cores for the Python code, not just the `numpy` code.
2.  **Use an Optimized Library:** For a truly massive scale-up, the next step would be to replace the from-scratch model with a production-grade, optimized library like `LightFM` (which has a parallelized implementation) or re-implementing the model in a framework like **TensorFlow** or **PyTorch**, which would allow for GPU acceleration and distributed training. Our from-scratch implementation serves as a powerful, validated baseline for these future optimizations.

---

## 5. API Manual

The API is available at `http://localhost:5001`.

*(The API Manual section would remain the same as the previous version)*