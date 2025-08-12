# Movie Recommender System MLOps Infrastructure

This project implements a complete, end-to-end MLOps pipeline for a movie recommendation system based on the MovieLens 100k dataset. It is designed to be a fully automated, containerized application that handles data ingestion, model training, evaluation, deployment, and serving via a REST API.

The core focus is on the **infrastructure and automation**, demonstrating a robust "Champion-Challenger" model deployment strategy orchestrated by Apache Airflow.

## Project Overview

The system consists of three primary components working in harmony:

1.  **A Live REST API (Flask):** A user-facing service that allows users to submit movie ratings and receive movie recommendations.
2.  **A Data Store (PostgreSQL):** A robust database that stores all user data, movie metadata, and the pre-computed recommendations.
3.  **An Orchestration Engine (Apache Airflow):** The automated brain of the system, responsible for periodically retraining the recommendation model on new data and deploying it to production only if it performs better than the current model.

## Project Structure

```
movielens_project/
├── airflow/
│   ├── dags/
│   │   └── retraining_dag.py   # Defines the Airflow workflow schedule
│   └── Dockerfile              # Builds a custom Airflow image with dependencies
├── data/
│   ├── u.data                  # The raw MovieLens dataset files
│   └── ...
├── flask_app/
│   ├── app.py                  # The main Flask API application
│   ├── Dockerfile              # Builds the Flask API image
│   ├── entrypoint.sh           # Script to initialize the database on startup
│   └── environment.yml         # Dependencies like Python version, Python libraries an version
├── models/
│   └── (This will be populated by training runs)version
├── scripts/
│   ├── db_init.py              # One-time script to create and populate the DB schema
│   └── retraining_logic.py     # The core model training and deployment logic
├── .env                        # Environment variables for Docker Compose
├── docker-compose.yml          # The master file to define and run all services
└── environment.yml             # Conda environment definition for reliable installs
```

## Core Components & Roles

### Flask API (`movielens_api` service)

This is the "Online Transaction Processing" (OLTP) part of our system. It's designed to be fast, responsive, and simple.

-   **Role:** To handle live user interactions.
-   **Functionality:**
    -   Provides endpoints to get lists of movies and genres.
    -   Accepts new user movie ratings via a `POST` request.
    -   Serves pre-computed movie recommendations for users.
    -   Handles the "cold start" problem by serving popularity-based recommendations to new users or any user for whom personalized recommendations are not yet available.

### PostgreSQL Databases

The project uses two completely isolated PostgreSQL containers for stability and separation of concerns.

1.  **`movielens_db` service:** This is the application's database.
    -   **Role:** To act as the single source of truth for all application data.
    -   **Key Tables:**
        -   `users`, `movies`, `genres`: Store the core metadata.
        -   `reviews`: Stores the base "ground truth" ratings used for training.
        -   `new_reviews`: A temporary holding table that collects all incoming ratings from the API, isolating the stable training data from live updates.
        -   `production_recommendations`: A simple lookup table containing pre-computed recommendations. The API queries this table to provide instant responses.

2.  **`postgres_airflow` service:** This is the metadata backend for Airflow.
    -   **Role:** To store the state of all DAGs, task runs, logs, and other internal Airflow data. It is managed entirely by Airflow.

### Apache Airflow (`airflow-standalone` service)

This is the "Online Analytical Processing" (OLAP) part of our system. It's the automated, offline data processing and MLOps engine.

-   **Role:** To orchestrate the entire model lifecycle without human intervention.
-   **Functionality:**
    -   A DAG (`retraining_svd_model`) is scheduled to run every two days.
    -   When triggered, it executes the `retraining_logic.py` script.
    -   This script trains a new "challenger" model on all available data (base + new reviews).
    -   It compares the challenger's performance (RMSE) against the current "champion" model.
    -   If the challenger is better, it is "promoted" to production, and the `production_recommendations` table is updated with its new, smarter predictions.

## Key Architectural and Technology Decisions

This section answers the "why" behind the project's design.

> #### Why Docker and Docker Compose?
> To ensure a **reproducible and isolated environment**. The entire complex application, including two databases and multiple Python environments, can be brought online with a single command (`docker compose up`). This eliminates "it works on my machine" problems and standardizes the development and deployment process.

> #### Why Two Different PostgreSQL Versions?
> The two applications (our API and Airflow) are completely separate.
> -   **`postgres_airflow` uses `postgres:13-alpine`** because it is the version officially tested and recommended by the Airflow team for our version of Airflow, ensuring maximum stability.
> -   **`movielens_db` uses `postgres:14.18`** because it is a more modern, full-featured version that we control for our own application's needs. This separation guarantees stability for third-party tools while allowing flexibility for our own code.

> #### Why Apache Airflow?
> For **robust orchestration**. While a simple cron job could run a script, Airflow provides a rich UI, logging, alerting, and resilience. It allows us to monitor, trigger, and debug our MLOps pipeline professionally. The use of the `standalone` command is a modern approach for local development that simplifies the otherwise complex multi-service setup.

> #### Why `scikit-surprise`?
> It is the **right tool for the job**. The SVD algorithm is a powerful and standard method for collaborative filtering on sparse matrices (like user ratings). `scikit-surprise` provides a clean, efficient, and easy-to-use implementation specifically for this task, as demonstrated by its use in the library's own documentation on this very dataset.

> #### Why Conda for Installation?
> For **reliability**. We discovered through extensive debugging that installing scientific libraries with C extensions (like `scikit-surprise`) can be very difficult with `pip` inside minimal Docker containers, leading to `gcc` compilation errors. **Conda solves this definitively** by installing pre-compiled binaries from the `conda-forge` channel, completely bypassing the need for system-level compilers and eliminating a major source of build failures.

> #### Why a "DAG-First" Architecture?
> For **code purity and consistency**. We intentionally removed the separate `initial_training.py` script in favor of a single, robust `retraining_logic.py` script. This script is smart enough to handle the very first run (when no "champion" model exists) and all subsequent maintenance runs. This follows the DRY (Don't Repeat Yourself) principle, makes the system easier to maintain, and ensures there is only one source of truth for the training logic. The system is bootstrapped via a one-time manual DAG trigger, which is a clean and explicit way to initialize the model.

### Core Libraries and Tools

A few key libraries play crucial, less obvious roles in the project:

-   **`pickle`**: A standard Python library for serializing Python objects. In our project, a trained SVD model is a complex object in memory. We use `pickle.dump()` to "freeze-dry" this object and save it to a `model.pkl` file. This allows our Airflow task to store the trained model artifact.

-   **`shutil`**: The Shell Utilities library. Its role is critical for the safe promotion of a new model. We use `shutil.move()` to atomically replace the old `model.pkl` with the new one. This is safer than a copy-then-delete operation, preventing a state where the model might be momentarily unavailable.

-   **`pendulum`**: A library for cleaner date and time handling. Airflow requires timezone-aware datetimes for scheduling to be reliable. We use `pendulum.datetime(...)` to define a precise `start_date` for our DAG, ensuring there is no ambiguity related to timezones or daylight saving.

-   **`from __future__ import annotations`**: A special directive in Python. It's an Airflow best practice included at the top of the DAG file. It postpones the evaluation of type hints, preventing potential errors during Airflow's complex DAG parsing process and making the DAG file more robust.

---

## Technical Deep Dive

### The MLOps Lifecycle

The project implements a full "Champion-Challenger" MLOps loop:

1.  **Data Collection:** A user rates a movie. The Flask API writes this rating to the `new_reviews` table.
2.  **Scheduled Trigger:** The Airflow DAG runs every two days.
3.  **Data Preparation:** The `retraining_logic.py` script reads all data from both the `reviews` and `new_reviews` tables. It handles updated ratings by only keeping the latest one for any user-movie pair.
4.  **Training & Evaluation:** A new "challenger" model is trained on this combined dataset. Its performance is measured using 5-fold cross-validation to get a reliable RMSE score.
5.  **Comparison:** The challenger's RMSE is compared to the RMSE of the current champion, which is stored in `models/production/metrics.txt`.
6.  **Deployment (Promotion):**
    -   **If Challenger Wins (`new_rmse < old_rmse`):** The new model file and metrics file replace the old ones. The script then pre-computes recommendations for all users and overwrites the `production_recommendations` table. Finally, it merges the data from `new_reviews` into the main `reviews` table and clears `new_reviews` for the next cycle.
    -   **If Challenger Loses:** The script does nothing. The old model remains in production, and the new data is kept in `new_reviews` for the next attempt.

### The "Cold Start" Problem

The system is designed to gracefully handle new users:
-   A new user is created in the `users` table upon their first rating.
-   Initially, they are served **popularity-based recommendations** from a fallback SQL query.
-   After the next successful Airflow DAG run, their ratings are incorporated into the model, and they begin receiving **personalized recommendations**.

---

## Getting Started & API Usage Guide

### Prerequisites
- Docker
- Docker Compose

### First-Time Setup
1.  **Clone the repository.**
2.  **Create the `.env` file:** In the project root, create a `.env` file and set your user ID to avoid permission issues with Airflow's mounted volumes.
    ```
    # Get your user ID by running `id -u` in your terminal
    AIRFLOW_UID=1000 
    AIRFLOW_GID=0
    ```
3.  **Build and Start All Services:**
    ```bash
    docker compose up --build
    ```
    This will take several minutes the first time as it builds the Conda environments.

### Bootstrapping the System (One-Time Manual Step)
The system starts in a "cold" state. To activate personalized recommendations, you must trigger the first training run.
1.  Open the Airflow UI at **`http://localhost:8080`**.
2.  Log in with username `admin` and password `admin`.
3.  On the main dashboard, find the `retrain_svd_model` DAG.
4.  Click the toggle switch to **unpause** it.
5.  Click the **play button (▶️)** to manually trigger the first run.
6.  You can monitor the run by clicking on the DAG name and viewing the task logs. Once it succeeds, the system is fully operational.

### API Endpoints

#### 1. Get All Genres
-   **Method:** `GET`
-   **Endpoint:** `/genres`
-   **Example:**
    ```bash
    curl http://localhost:5001/genres
    ```

#### 2. Get Movies (with optional filters)
-   **Method:** `GET`
-   **Endpoint:** `/movies`
-   **Example (All Movies):**
    ```bash
    curl http://localhost:5001/movies
    ```

#### 3. Create a New User and Submit First Review
-   **Method:** `POST`
-   **Endpoint:** `/reviews`
-   **Body (must not include `user_id`):**
    ```bash
    curl -X POST http://localhost:5001/reviews \
    -H "Content-Type: application/json" \
    -d '{
        "movie_id": 50,
        "score": 5,
        "gender": "F",
        "occupation": "scientist",
        "zip_code": "12345"
    }'
    ```

#### 4. Submit a Review for an Existing User
-   **Method:** `POST`
-   **Endpoint:** `/reviews`
-   **Body (must include `user_id`):**
    ```bash
    curl -X POST http://localhost:5001/reviews \
    -H "Content-Type: application/json" \
    -d '{
        "user_id": 196,
        "movie_id": 302,
        "score": 4
    }'
    ```

#### 5. Get a User's Full Review History
-   **Method:** `GET`
-   **Endpoint:** `/reviews/<user_id>`
-   **Example:**
    ```bash
    curl http://localhost:5001/reviews/196
    ```

#### 6. Get Recommendations for a User
-   **Method:** `GET`
-   **Endpoint:** `/recommendations/<user_id>`
-   **Query Parameters (optional):**
    -   `limit` (integer, default: 10)
    -   `genre_id` (integer)
-   **Example (General):**
    ```bash
    curl "http://localhost:5001/recommendations/196?limit=5"
    ```
-   **Example (Filtered by Genre):**
    ```bash
    # Get top Action (genre_id=1) recommendations for user 196
    curl "http://localhost:5001/recommendations/196?genre_id=1"
    ```