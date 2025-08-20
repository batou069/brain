# Project Structure

```
movielens_project/
├── airflow/
│   ├── dags/
│   │   └── retraining_dag.py
│   ├── Dockerfile
│   └── logs/
│
├── data/
│   ├── u.data
│   └── (other movielens files...)
│
├── flask_app/
│   ├── app.py
│   ├── Dockerfile
│   └── entrypoint.sh
│
├── models/
│   ├── production/
│   └── staging/
│
├── scripts/
│   ├── db_init.py
│   ├── fm_model.py
│   ├── pipeline.py
│   └── retraining_logic.py
│
├── docker-compose.yml
├── environment.yml
└── .env
```

*   **`data/`**: For the downloaded MovieLens 100k dataset files here.
*   **`flask_app/`**: For API Endpoints
*   **`db_init/`**: A script to initialize the database with the 100K Movie data.
*   **`docker-compose.yml`**: The "master file" that defines and connects our services.

---

# Files
## 1. Docker Services (`docker-compose.yml`)
```yaml
services:
  # --- Application Services ---
  movielens_db:
    image: postgres:14.18
    container_name: movielens_db
    volumes:
      - movielens_data:/var/lib/postgresql/data/
    environment:
      - POSTGRES_DB=movielens
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user -d movielens"]
      interval: 5s
      timeout: 5s
      retries: 5

  movielens_api:
    build: 
      context: .
      dockerfile: ./flask_app/Dockerfile
    container_name: movielens_api
    volumes:
      - ./flask_app/app.py:/app/app.py
      - ./models:/app/models
    ports:
      - "5001:5000"
    environment:
      - FLASK_ENV=development
      - DATABASE_URL=postgresql://user:password@movielens_db:5432/movielens
      - SHARED_DIR=/app # scripts are run from /app
    depends_on:
      movielens_db:
        condition: service_healthy

  # --- Airflow Services ---
  postgres_airflow:
    image: postgres:13-alpine
    container_name: airflow_postgres
    environment:
      - POSTGRES_USER=${POSTGRES_USER:-airflow}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD:-airflow}
      - POSTGRES_DB=${POSTGRES_DB:-airflow}
    volumes:
      - airflow_db_data:/var/lib/postgresql/data/
    ports:
      - "5433:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER:-airflow} -d ${POSTGRES_DB:-airflow}"]
      interval: 5s
      timeout: 5s
      retries: 5

  airflow-standalone:
    build:
      context: .
      dockerfile: ./airflow/Dockerfile
    container_name: airflow_standalone
    depends_on:
      postgres_airflow:
        condition: service_healthy
    environment:
      - AIRFLOW__CORE__EXECUTOR=LocalExecutor
      - AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=postgresql+psycopg2://${POSTGRES_USER:-airflow}:${POSTGRES_PASSWORD:-airflow}@postgres_airflow:5432/${POSTGRES_DB:-airflow}
      - AIRFLOW__CORE__LOAD_EXAMPLES=false
      - SHARED_DIR=/opt/airflow # The DAGs run from /opt/airflow
    volumes:
      - ./airflow/dags:/opt/airflow/dags
      - ./airflow/logs:/opt/airflow/logs
      - ./scripts:/opt/airflow/scripts
      - ./models:/opt/airflow/models
    ports:
      - "8080:8080"
    user: "${AIRFLOW_UID}:${AIRFLOW_GID}"
    command: bash -c " airflow db migrate && airflow users create --username admin --password admin --firstname Anonymous --lastname User --role Admin --email admin@example.org || true; exec airflow standalone"

volumes:
  movielens_data:
  airflow_db_data:
```

---

## 2. Requirements/Conda-Environment (`environment.yml`)

We swap `scikit-surprise` for `lightfm` and add `scipy` which is a dependency for handling sparse matrices.

```yml
name: movie-rec-env
channels:
  - conda-forge
dependencies:
  - python=3.11
  - pip
  - flask=3.0.3
  - psycopg2=2.9.9
  - sqlalchemy=2.0.28
  - pandas=2.2.2
  - scikit-surprise=1.1.3
  - numpy<2
```

---

## 3. Scripts

### Database Initialization (`scripts/db_init.py`)


```python
# scripts/db_init.py

import os
import pandas as pd
from sqlalchemy import create_engine, text

def get_db_engine():
    """Creates a database engine."""
    db_url = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/movielens")
    return create_engine(db_url)

def create_tables(engine):
    """Creates all necessary tables in the database."""
    create_sql = """
        CREATE TABLE IF NOT EXISTS genres (
            genre_id INT PRIMARY KEY, name VARCHAR(255) NOT NULL UNIQUE
        );
        CREATE TABLE IF NOT EXISTS movies (
            movie_id INT PRIMARY KEY, title VARCHAR(255) NOT NULL, release_date DATE, imdb_url TEXT
        );
        CREATE TABLE IF NOT EXISTS movie_genres (
            movie_id INT REFERENCES movies(movie_id) ON DELETE CASCADE,
            genre_id INT REFERENCES genres(genre_id) ON DELETE CASCADE,
            PRIMARY KEY (movie_id, genre_id)
        );
        CREATE TABLE IF NOT EXISTS users (
            user_id INT PRIMARY KEY, age INT, gender CHAR(1), occupation VARCHAR(255), zip_code VARCHAR(20)
        );
        CREATE TABLE IF NOT EXISTS reviews (
            review_id SERIAL PRIMARY KEY,
            user_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
            movie_id INT NOT NULL REFERENCES movies(movie_id) ON DELETE CASCADE,
            rating INT NOT NULL CHECK (rating >= 1 AND rating <= 5),
            timestamp BIGINT,
            UNIQUE (user_id, movie_id)
        );
        CREATE TABLE IF NOT EXISTS new_reviews (
            review_id SERIAL PRIMARY KEY, user_id INT NOT NULL, movie_id INT NOT NULL,
            rating INT NOT NULL CHECK (rating >= 1 AND rating <= 5), timestamp BIGINT
        );
        CREATE TABLE IF NOT EXISTS production_recommendations (
            user_id INT NOT NULL, movie_id INT NOT NULL, predicted_rating FLOAT NOT NULL,
            PRIMARY KEY (user_id, movie_id)
        );
    """
    with engine.begin() as connection:
        connection.execute(text(create_sql))
    print("Tables created successfully.")

def load_data(engine):
    """Loads data from the MovieLens 100k files into the database."""
    with engine.connect() as connection:
        if connection.execute(text("SELECT COUNT(*) FROM users")).scalar() > 0:
            print("Data already loaded. Skipping.")
            return

    with engine.begin() as connection:
        print("Loading genres...")
        genre_df = pd.read_csv('./data/u.genre', sep='|', names=['name', 'genre_id'], encoding='latin-1')
        genre_df.to_sql('genres', connection, if_exists='append', index=False)

        print("Loading movies...")
        m_cols = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url'] + [f'g{i}' for i in range(19)]
        movies_df = pd.read_csv('./data/u.item', sep='|', names=m_cols, encoding='latin-1', usecols=m_cols)
        movies_df['release_date'] = pd.to_datetime(movies_df['release_date'])
        # FIX: Load the movies table FIRST.
        movies_df[['movie_id', 'title', 'release_date', 'imdb_url']].to_sql('movies', connection, if_exists='append', index=False)
        
        print("Loading movie-genre relationships...")
        movie_genres_list = []
        for _, row in movies_df.iterrows():
            for i in range(19):
                if row[f'g{i}'] == 1:
                    movie_genres_list.append({'movie_id': row['movie_id'], 'genre_id': i})
        pd.DataFrame(movie_genres_list).to_sql('movie_genres', connection, if_exists='append', index=False)

        print("Loading users...")
        users_df = pd.read_csv('./data/u.user', sep='|', names=['user_id', 'age', 'gender', 'occupation', 'zip_code'], encoding='latin-1')
        users_df.to_sql('users', connection, if_exists='append', index=False)

        print("Loading reviews...")
        reviews_df = pd.read_csv('./data/u.data', sep='\t', names=['user_id', 'movie_id', 'rating', 'timestamp'], encoding='latin-1')
        reviews_df.to_sql('reviews', connection, if_exists='append', index=False)
        
    print("All data loaded successfully.")

if __name__ == "__main__":
    db_engine = get_db_engine()
    create_tables(db_engine)
    load_data(db_engine)
```

### Retraining (`scripts/retraining_logic.py`)

```python
import shutil
import os
import pickle
import pandas as pd
from sqlalchemy import create_engine, text
from surprise import Dataset, Reader, SVD
from surprise.model_selection import cross_validate


def main():
    """
    Main logic for the training pipeline. called by the Airflow DAG.
    """
    print("--- Starting (Re)training and Deployment Pipeline (SVD) ---")

    # Use environment variables to find the shared directories
    SHARED_DIR = os.getenv("SHARED_DIR", "/opt/airflow")
    MODELS_DIR = os.path.join(SHARED_DIR, "models")
    DB_URL = "postgresql://user:password@movielens_db:5432/movielens"
    PROD_DIR = os.path.join(MODELS_DIR, "production")
    STAGING_DIR = os.path.join(MODELS_DIR, "staging")
    os.makedirs(PROD_DIR, exist_ok=True)
    os.makedirs(STAGING_DIR, exist_ok=True)

    engine = create_engine(DB_URL)
    with engine.connect() as connection:
        base_reviews_df = pd.read_sql("SELECT * FROM reviews", connection)
        new_reviews_df = pd.read_sql("SELECT * FROM new_reviews", connection)
        all_users = pd.read_sql("SELECT user_id FROM users", connection)[
            "user_id"
        ].unique()
        all_movies = pd.read_sql("SELECT movie_id FROM movies", connection)[
            "movie_id"
        ].unique()

    champion_model_exists = os.path.exists(os.path.join(PROD_DIR, "metrics.txt"))
    if new_reviews_df.empty and champion_model_exists:
        print("No new reviews found and a production model already exists. Skipping training.")
        return

    # Combine old and new data, keeping only the latest review per user/movie
    combined_df = pd.concat([base_reviews_df, new_reviews_df], ignore_index=True)
    training_df = combined_df.sort_values("timestamp").drop_duplicates(
        subset=["user_id", "movie_id"], keep="last"
    )

    # Train and evaluate the challenger model
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(training_df[["user_id", "movie_id", "rating"]], reader)
    algo = SVD(random_state=41)
    cv_results = cross_validate(algo, data, measures=["RMSE"], cv=5, verbose=True)
    challenger_rmse = cv_results["test_rmse"].mean()

    # Compare to the champion model
    try:
        with open(os.path.join(PROD_DIR, "metrics.txt"), "r", encoding="utf-8") as f:
            champion_rmse = float(f.read())
    except FileNotFoundError:
        champion_rmse = float("inf")  # If no champion, challenger always wins

    print(f"Champion RMSE: {champion_rmse}, Challenger RMSE: {challenger_rmse}")
    if challenger_rmse < champion_rmse:
        print("Challenger is better. Promoting to production.")
        trainset = data.build_full_trainset()
        algo.fit(trainset)

        # Save to staging first for safety
        with open(os.path.join(STAGING_DIR, "model.pkl"), "wb") as f:
            pickle.dump(algo, f)
        with open(os.path.join(STAGING_DIR, "metrics.txt"), "w", encoding="utf-8") as f:
            f.write(str(challenger_rmse))

        # Atomically move to production
        shutil.move(
            os.path.join(STAGING_DIR, "model.pkl"), os.path.join(PROD_DIR, "model.pkl")
        )
        shutil.move(
            os.path.join(STAGING_DIR, "metrics.txt"),
            os.path.join(PROD_DIR, "metrics.txt"),
        )

        # Pre-compute new recommendations
        rated_pairs = training_df.set_index(["user_id", "movie_id"]).index
        all_pairs = pd.MultiIndex.from_product(
            [all_users, all_movies], names=["user_id", "movie_id"]
        )
        to_predict = all_pairs.difference(rated_pairs)
        predictions = [algo.predict(uid=uid, iid=iid) for uid, iid in to_predict]
        recs_df = pd.DataFrame(
            [
                {"user_id": p.uid, "movie_id": p.iid, "predicted_rating": p.est}
                for p in predictions
            ]
        )

        # Update the database
        with engine.connect() as connection:
            connection.execute(text("TRUNCATE TABLE production_recommendations;"))
            recs_df.to_sql(
                "production_recommendations",
                engine,
                if_exists="append",
                index=False,
                chunksize=10000,
            )
            merge_sql = """
                INSERT INTO reviews (user_id, movie_id, rating, timestamp)
                SELECT user_id, movie_id, rating, timestamp FROM new_reviews
                ON CONFLICT (user_id, movie_id) DO UPDATE 
                SET rating = EXCLUDED.rating, timestamp = EXCLUDED.timestamp;
            """
            connection.execute(text(merge_sql))
            connection.execute(text("TRUNCATE TABLE new_reviews;"))
        print("System updated with new model.")
    else:
        print("Challenger is not better. Discarding.")


if __name__ == "__main__":
    main()

```

---

## 4. The API Server (`flask_app/app.py`)

```python
# flask_app/app.py

import os
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, text

app = Flask(__name__)
DATABASE_URL = os.environ.get('DATABASE_URL')
engine = create_engine(DATABASE_URL)

def make_error(status_code, message):
    response = jsonify({'status': 'error', 'message': message})
    response.status_code = status_code
    return response

@app.route('/genres', methods=['GET'])
def get_genres():
    """Returns a list of all movie genres and their IDs."""
    with engine.connect() as connection:
        result = connection.execute(text("SELECT genre_id, name FROM genres ORDER BY name;")).fetchall()
        genres = [{'genre_id': row.genre_id, 'name': row.name} for row in result]
        return jsonify(genres)
    
@app.route('/movies', methods=['GET'])
def get_movies():
    """
    Returns a list of all movie_IDs, titles, and release dates, 
    optionally filtered by first letter or release year.
    """
    first_letter = request.args.get('first_letter')
    release_year = request.args.get('release_year')
    query_str = "SELECT movie_id, title, release_date FROM movies"
    filters, params = [], {}
    if first_letter:
        filters.append("title ILIKE :letter")
        params['letter'] = f"{first_letter}%"
    if release_year:
        try:
            params['year'] = int(release_year)
            filters.append("EXTRACT(YEAR FROM release_date) = :year")
        except ValueError:
            return make_error(400, "Invalid 'release_year'. Must be an integer.")
    if filters:
        query_str += " WHERE " + " AND ".join(filters)
    query_str += " ORDER BY title;"
    with engine.connect() as connection:
        result = connection.execute(text(query_str), params).fetchall()
        movies_list = [{'movie_id': r.movie_id, 'title': r.title, 'release_date': r.release_date.isoformat() if r.release_date else None} for r in result]
        return jsonify(movies_list)

@app.route('/reviews/<int:user_id>', methods=['GET'])
def get_user_reviews(user_id):
    """
    Returns all reviews for a given user, combining both base and new reviews.
    """
    query = text("""
        SELECT movie_id, rating, timestamp, 'base' as source FROM reviews WHERE user_id = :user_id
        UNION ALL
        SELECT movie_id, rating, timestamp, 'new' as source FROM new_reviews WHERE user_id = :user_id
        ORDER BY timestamp DESC;
    """)
    with engine.connect() as connection:
        result = connection.execute(query, {'user_id': user_id}).fetchall()
        reviews_list = [{'movie_id': r.movie_id, 'rating': r.rating, 'timestamp': r.timestamp, 'source': r.source} for r in result]
        return jsonify(reviews_list)

@app.route('/reviews', methods=['POST'])
def add_review():
    """
    Function to accept a new review from a user (or update an existing one).
    Expects JSON with 'user_id', 'movie_id', and 'score' (rating).
    If 'user_id' is not provided, a new user will be created.
    """
    if not request.is_json: 
        return make_error(400, "Request must be JSON.")
    data = request.get_json()
    user_id = data.get('user_id')
    movie_id = data.get('movie_id')
    rating = data.get('score')

    if not all([movie_id, rating]):
        return make_error(400, "Missing 'movie_id' or 'score'.")

    new_user_id_response = None
    with engine.connect() as connection:
        if not user_id:
            if not all(k in data for k in ['gender', 'occupation', 'zip_code']):
                return make_error(400, "New users must provide 'gender', 'occupation', and 'zip_code'.")
            new_user_id = connection.execute(text("SELECT MAX(user_id) + 1 FROM users")).scalar()
            user_id = new_user_id
            new_user_id_response = user_id
            insert_user_query = text("INSERT INTO users (user_id, age, gender, occupation, zip_code) VALUES (:user_id, NULL, :gender, :occupation, :zip_code)")
            connection.execute(insert_user_query, {'user_id': user_id, 'gender': data['gender'], 'occupation': data['occupation'], 'zip_code': data['zip_code']})
        
        insert_review_query = text("INSERT INTO new_reviews (user_id, movie_id, rating, timestamp) VALUES (:user_id, :movie_id, :rating, extract(epoch from now()))")
        connection.execute(insert_review_query, {'user_id': user_id, 'movie_id': movie_id, 'rating': rating})
        connection.commit()

        response_data = {'status': 'success', 'message': f"Review for movie {movie_id} by user {user_id} collected."}
        if new_user_id_response:
            response_data['new_user_id'] = user_id
        return jsonify(response_data)

@app.route('/recommendations/<int:user_id>', methods=['GET'])
def get_recommendations(user_id):
    """
    Usage: /recommendations/196?limit=20&genre_id=5
    """
    limit = request.args.get('limit', default=10, type=int)
    genre_id = request.args.get('genre_id', default=None, type=int)
    
    recommendations = []
    params = {'user_id': user_id, 'limit': limit}
    
    with engine.connect() as connection:
        # Base query strings
        recs_query_base = "SELECT m.movie_id, m.title, pr.predicted_rating FROM production_recommendations pr JOIN movies m ON pr.movie_id = m.movie_id"
        fallback_query_base = "SELECT m.movie_id, m.title, COUNT(r.movie_id) as num_ratings FROM movies m JOIN reviews r ON m.movie_id = r.movie_id"

        # Dynamic parts for genre filtering
        genre_join = ""
        genre_where = ""
        if genre_id is not None:
            genre_join = "JOIN movie_genres mg ON m.movie_id = mg.movie_id"
            genre_where = "AND mg.genre_id = :genre_id"
            params['genre_id'] = genre_id

        # Build and execute personalized query
        recs_query_str = f"{recs_query_base} {genre_join} WHERE pr.user_id = :user_id {genre_where} ORDER BY pr.predicted_rating DESC LIMIT :limit;"
        result = connection.execute(text(recs_query_str), params).fetchall()
        
        if result:
            recommendations = [{'movie_id': r.movie_id, 'title': r.title, 'reason': f"Personalized score: {r.predicted_rating:.2f}"} for r in result]
        else:
            # Build and execute fallback query
            fallback_where = f"WHERE m.movie_id NOT IN (SELECT movie_id FROM reviews WHERE user_id = :user_id) {genre_where}"
            fallback_query_str = f"{fallback_query_base} {genre_join} {fallback_where} GROUP BY m.movie_id, m.title ORDER BY num_ratings DESC, m.title ASC LIMIT :limit;"
            fallback_result = connection.execute(text(fallback_query_str), params).fetchall()
            recommendations = [{'movie_id': r.movie_id, 'title': r.title, 'reason': f"Popularity-based ({r.num_ratings} ratings)"} for r in fallback_result]

    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
```

---

## 5. The Airflow Retraining DAG (`airflow/dags/retraining_dag.py`)

```python
# airflow/dags/retraining_dag.py

from __future__ import annotations
import pendulum
from airflow.decorators import dag
from airflow.operators.bash import BashOperator

@dag(
    dag_id="retrain_svd_model",
    schedule_interval="0 0 */2 * *",
    start_date=pendulum.datetime(2024, 1, 1, tz="UTC"),
    catchup=False,
    tags=["recommendation", "svd"],
)
def retraining_dag():
    BashOperator(
        task_id="train_and_deploy_if_better",
        bash_command="conda run -n movie-rec-env python /opt/airflow/scripts/retraining_logic.py"
    )

retraining_dag()
```

---

# The User Lifecycle

## Lifecycle for a new user:

1.  **First Interaction (Cold Start):** A new user submits their first review. The system has no personalized data for them yet. When they ask for recommendations, the API's fallback logic kicks in, and they receive a list of the **most popular movies** across the entire platform.
2.  **Collecting More Data:** The user continues to rate more movies. Each new rating is saved to the `new_reviews` table. During this period, they will **still receive popularity-based recommendations** because the main production model has not been updated with their new ratings yet.
3.  **The Retraining Event:** The Airflow DAG runs (either on its 2-day schedule or via a manual trigger).
    *   It takes all the new ratings from the `new_reviews` table.
    *   It combines them with the base data and retrains the SVD model. The model now learns this new user's specific tastes from their rating history.
    *   It pre-computes a brand new set of personalized recommendations for **all users**, including this new user.
    *   It populates the `production_recommendations` table with these new, personalized scores.
4.  **Personalized Experience:** From this point forward, whenever the user requests recommendations, the API will find their pre-computed scores in the `production_recommendations` table and serve them a list of movies tailored specifically to their learned preferences.

**In short: The recommendations get smarter and more personalized for a user every time the Airflow DAG runs and incorporates their new reviews.**

---

## API Usage Guide with `curl` Examples

Here is a complete walkthrough of every API action, from a new user's perspective.

#### A) A New User Explores the Movie Catalog

First, a new user needs to find some movies to rate.

**1. Get a list of all movies:**
```bash
curl http://localhost:5001/movies
```

**2. Get a list of all genres (to know how to filter):**
```bash
curl http://localhost:5001/genres
```
*(This might return `[{"genre_id": 1, "name": "Action"}, ...]`)*

**3. Get a filtered list of movies (e.g., Sci-Fi movies from 1982):**
*(Let's assume from the previous call we know Sci-Fi has `genre_id=15`)*
```bash
curl "http://localhost:5001/movies?release_year=1982&genre_id=15"
```

#### B) The New User Creates an Account and Submits Their First Review

The user decides to rate "Blade Runner" (movie_id 172) a 5. They submit their demographic data. **Crucially, they do not provide a `user_id`.**

```bash
curl -X POST http://localhost:5001/reviews \
-H "Content-Type: application/json" \
-d '{
    "movie_id": 172,
    "score": 5,
    "gender": "M",
    "occupation": "engineer",
    "zip_code": "90210"
}'
```
**Expected Response:**
```json
{
  "message": "Review for movie 172 by user 944 collected.",
  "new_user_id": 944,
  "status": "success"
}
```
The user's application should now save `944` as their user ID.

#### C) The New User Gets Their First (Fallback) Recommendations

Now identified as user 944, they ask for recommendations.

```bash
curl http://localhost:5001/recommendations/944
```
**Expected Response:** A list of popular movies, because the model hasn't been trained on user 944's data yet.
```json
[
  {
    "movie_id": 50,
    "reason": "Popularity-based (583 ratings)",
    "title": "Star Wars (1977)"
  },
  ...
]
```

#### D) The Existing User Submits Another Review

The user now rates "Contact" (movie_id 257) a 4. This time, they **provide their `user_id`**.

```bash
curl -X POST http://localhost:5001/reviews \
-H "Content-Type: application/json" \
-d '{
    "user_id": 944,
    "movie_id": 257,
    "score": 4
}'
```
**Expected Response:**
```json
{
  "message": "Review for movie 257 by user 944 collected.",
  "status": "success"
}
```

#### E) The Existing User Checks Their Review History

```bash
curl http://localhost:5001/reviews/944
```
**Expected Response:** A list of the two reviews they have submitted.
```json
[
  {
    "movie_id": 257,
    "rating": 4,
    "source": "new",
    "timestamp": 1754256000
  },
  {
    "movie_id": 172,
    "rating": 5,
    "source": "new",
    "timestamp": 1754255000
  }
]
```

#### F) The MLOps Pipeline Runs

At this point, we would go to the Airflow UI (`http://localhost:8080`), unpause the `retrain_svd_model` DAG, and manually trigger it. We would monitor the run until it succeeds.

#### G) The Existing User Gets Personalized Recommendations

After the DAG run is complete, the user makes the **exact same API call** as before.

**1. Get general personalized recommendations (with a limit of 5):**
```bash
curl "http://localhost:5001/recommendations/944?limit=5"
```
**Expected Response:** A new list of movies, based on the SVD model's predictions.
```json
[
  {
    "movie_id": 127,
    "reason": "Personalized score: 4.87",
    "title": "Godfather, The (1972)"
  },
  ...
]
```

**2. Get personalized recommendations for a specific genre (e.g., Action, `genre_id=1`):**
```bash
curl "http://localhost:5001/recommendations/944?genre_id=1"
```

**Expected Response:** A list of Action movies that the model predicts user 944 will like the most.


# Benefit of movie-genre pairs (SQL)

The  approach of using a separate movie_genres "junction" table instead of putting many one-hot encoded columns in the movies table is a core principle of database normalization, and it offers several significant benefits.


Let's compare the two approaches:

Approach 1: One-Hot Encoded Columns (The "Wide" Table)

Here, the movies table would look like this:

| movie\_id | title     | is\_Action | is\_Comedy | is\_Drama | ... |
| :-------- | :-------- | :--------- | :--------- | :-------- | :-- |
| 1         | Toy Story | 0          | 1          | 0         | ... |
| 2         | GoldenEye | 1          | 0          | 0         | ... |

  Approach 2: Normalized Tables (The Relational Approach)

  Here, we have three tables:

  `movies` table:

| movie\_id | title     |
| :-------- | :-------- |
| 1         | Toy Story |
| 2         | GoldenEye |


  `genres` table:

| genre\_id | name   |
| :-------- | :----- |
| 1         | Action |
| 2         | Comedy |

  `movie_genres` (junction) table:

| movie\_id | genre\_id |
| :--- | :--- |
| 1 | 2 |
| 2 | 1 |

  ---

  The Benefits of the Relational Approach


   1. Flexibility and Scalability (The Biggest Advantage):
* Adding a New Genre: Imagine a new genre, "Super Hero," is created.
%%             %%* In the Wide Table, you would have to add a new column (is_Super_Hero) to
             the movies table. This is a major, expensive schema change that requires
             modifying a potentially huge table.
           * In the Relational Approach, you simply INSERT a new row into the genres
             table: (3, 'Super Hero'). No schema change is needed. You can then start
             adding (movie_id, 3) pairs to the movie_genres table. This is trivial and
             scalable.


   2. Data Integrity and Consistency:
       * The genres table becomes the single source of truth for all possible genres.
         This prevents typos and inconsistencies. You can't accidentally insert a movie
         with the genre "Comdy" in the relational model because the genre_id wouldn't
         exist.
       * In the wide table, there's nothing stopping someone from creating a new column
         called is_Comdy, leading to fragmented and incorrect data.


   3. Storage Efficiency:
       * While it seems like more tables would take up more space, the opposite is often
         true, especially as the number of genres grows. The movie_genres table stores
         only two integers per link.
       * The wide table stores an integer (0 or 1) for every single genre for every
         single movie, leading to a massive number of zeros being stored, which can be
         inefficient.


   4. Querying Power and Simplicity:
       * The relational model makes certain queries much more elegant and efficient.
       * "Find all Action movies":
           * Wide Table: SELECT title FROM movies WHERE is_Action = 1; (This is simple).
           * Relational: SELECT m.title FROM movies m JOIN movie_genres mg ON m.movie_id
             = mg.movie_id JOIN genres g ON mg.genre_id = g.genre_id WHERE g.name =
             'Action'; (More complex, but very powerful).
       * "Count how many movies are in each genre" (Harder Query):
           * Wide Table: This is very awkward. You'd have to do SELECT SUM(is_Action),
             SUM(is_Comedy), ... FROM movies;, which is not scalable if you add new
             genres.
           * Relational: This is incredibly simple and scalable: SELECT g.name,
             COUNT(mg.movie_id) FROM genres g JOIN movie_genres mg ON g.genre_id =
             mg.genre_id GROUP BY g.name;

  In summary, while the one-hot encoded approach seems simpler at first glance, the
  normalized, relational approach is far superior for long-term maintainability,
  data integrity, and query flexibility. It's the standard and best practice for
  representing this kind of "many-to-many" relationship (one movie can have many
  genres, and one genre can apply to many movies).