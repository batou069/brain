# Project Structure

```
movielens_project/
├── airflow/
│   ├── dags/
│   │   └── retraining_dag.py
│   └── logs/
│
├── data/
│   ├── u.data
│   └── (other movielens files...)
│
├── flask_app/
│   ├── app.py
│   ├── Dockerfile
│   ├── entrypoint.sh
│   └── requirements.txt
│
├── models/
│   ├── production/
│   └── staging/
│
├── scripts/
│   ├── db_init.py
│   └── initial_training.py
│
├── .env
└── docker-compose.yml
```

*   **`data/`**: For the downloaded MovieLens 100k dataset files here.
*   **`flask_app/`**: For API Endpoints
*   **`db_init/`**: A script to initialize the database with the 100K Movie data.
*   **`docker-compose.yml`**: The "master file" that defines and connects our services.

---

# Docker Services

This file is the heart of our containerized setup. It defines two services: `db` for our PostgreSQL database and `web` for our Flask application.

**docker-compose.yml**
```yaml
services:
  db:
    image: postgres:13-alpine
    volumes:
      - postgres_data:/var/lib/postgresql/data/
    environment:
      - POSTGRES_DB=movielens
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
    ports:
      - "5432:5432"

  web:
    build: ./flask_app
    volumes:
      - ./flask_app:/app
      - ./data:/app/data  # Mount data folder to be accessible by init script
      - ./db_init:/app/db_init
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=development
      - DATABASE_URL=postgresql://user:password@db:5432/movielens
    depends_on:
      - db

volumes:
  postgres_data:
```

*   `volumes: - postgres_data:...` ensures that our database data persists even if we stop and restart the containers.
*   `web` service is built using the `Dockerfile` in our `flask_app` directory.
*   `volumes: - ./flask_app:/app` creates a live link. Allows me to change the code, and the server will restart automatically without needing to rebuild the container.
*   `depends_on: - db` ensures that the Flask app will only start after the database is ready.

---

# Db Init Script

**db_init/load_data.py**
```python
import os
import pandas as pd
from sqlalchemy import create_engine, text
import time

# Wait for the database service to be ready
time.sleep(10)

# Database connection details from environment variables
DB_URL = os.getenv("DATABASE_URL")
engine = create_engine(DB_URL)

# --- Define Schema and Create Tables ---
def create_tables():
    with engine.connect() as connection:
        connection.execute(text("""
        -- Look-up table for genres, populated from u.genre
        -- This is the correct way to handle the 19 binary columns from u.item
        CREATE TABLE IF NOT EXISTS genres (
            genre_id INT PRIMARY KEY,
            name VARCHAR(255) NOT NULL UNIQUE
        );
    
        -- Table for movie information, populated from u.item
        CREATE TABLE IF NOT EXISTS movies (
            movie_id INT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            release_date DATE,
            imdb_url TEXT
        );
    
        -- This is a "linking" or "junction" table.
        -- It connects movies to genres in a many-to-many relationship.
        CREATE TABLE IF NOT EXISTS movie_genres (
            movie_id INT REFERENCES movies(movie_id) ON DELETE CASCADE,
            genre_id INT REFERENCES genres(genre_id) ON DELETE CASCADE,
            PRIMARY KEY (movie_id, genre_id)
        );
    
        -- Table for user information, populated from u.user
        CREATE TABLE IF NOT EXISTS users (
            user_id INT PRIMARY KEY,
            age INT,
            gender CHAR(1),
            occupation VARCHAR(255),
            zip_code VARCHAR(20)
        );
    
        -- The core transactional data, populated from u.data
        -- This table holds the "ground truth" data for model training.
        CREATE TABLE IF NOT EXISTS reviews (
            review_id SERIAL PRIMARY KEY,
            user_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
            movie_id INT NOT NULL REFERENCES movies(movie_id) ON DELETE CASCADE,
            rating INT NOT NULL CHECK (rating >= 1 AND rating <= 5),
            timestamp BIGINT,
            -- A user can only rate a specific movie once.
            UNIQUE (user_id, movie_id)
        );
    
        -- This table collects all NEW reviews from the API.
        -- It is kept separate to ensure the production model's integrity.
        CREATE TABLE IF NOT EXISTS new_reviews (
            review_id SERIAL PRIMARY KEY,
            user_id INT NOT NULL,
            movie_id INT NOT NULL,
            rating INT NOT NULL CHECK (rating >= 1 AND rating <= 5),
            timestamp BIGINT
        );
    
        -- This table stores the output of the production model.
        -- The API reads from here to provide instant recommendations.
        CREATE TABLE IF NOT EXISTS production_recommendations (
            user_id INT NOT NULL,
            movie_id INT NOT NULL,
            predicted_rating FLOAT NOT NULL,
            PRIMARY KEY (user_id, movie_id)
        );
        """))
        print("Tables created (if they didn't exist).")

# --- Load Data Functions ---
def load_genres():
    # Load from u.genre
    genre_df = pd.read_csv(
        './data/u.genre', sep='|', names=['name', 'genre_id'], encoding='latin-1'
    )
    with engine.connect() as connection:
        # Check if genres table is empty
        result = connection.execute(text("SELECT COUNT(*) FROM genres;")).scalar()
        if result == 0:
            genre_df.to_sql('genres', engine, if_exists='append', index=False)
            print(f"{len(genre_df)} genres loaded.")

def load_movies_and_movie_genres():
    # Load from u.item
    m_cols = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url'] + [f'g{i}' for i in range(19)]
    movies_df = pd.read_csv(
        './data/u.item', sep='|', names=m_cols, encoding='latin-1', usecols=['movie_id', 'title', 'release_date'] + [f'g{i}' for i in range(19)]
    )
    movies_df['release_date'] = pd.to_datetime(movies_df['release_date'])
    
    with engine.connect() as connection:
        # Check if movies table is empty
        result = connection.execute(text("SELECT COUNT(*) FROM movies;")).scalar()
        if result == 0:
            movies_df[['movie_id', 'title', 'release_date']].to_sql('movies', engine, if_exists='append', index=False)
            print(f"{len(movies_df)} movies loaded.")

            # Prepare movie_genres data
            movie_genres_list = []
            for index, row in movies_df.iterrows():
                for i in range(19):
                    if row[f'g{i}'] == 1:
                        movie_genres_list.append({'movie_id': row['movie_id'], 'genre_id': i})
            
            movie_genres_df = pd.DataFrame(movie_genres_list)
            movie_genres_df.to_sql('movie_genres', engine, if_exists='append', index=False)
            print(f"{len(movie_genres_df)} movie-genre relationships loaded.")

def load_users():
    # Load from u.user
    u_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
    users_df = pd.read_csv('./data/u.user', sep='|', names=u_cols, encoding='latin-1')
    with engine.connect() as connection:
        result = connection.execute(text("SELECT COUNT(*) FROM users;")).scalar()
        if result == 0:
            users_df.to_sql('users', engine, if_exists='append', index=False)
            print(f"{len(users_df)} users loaded.")

def load_reviews():
    # Load from u.data
    r_cols = ['user_id', 'movie_id', 'rating', 'timestamp']
    reviews_df = pd.read_csv('./data/u.data', sep='\t', names=r_cols, encoding='latin-1')
    with engine.connect() as connection:
        result = connection.execute(text("SELECT COUNT(*) FROM reviews;")).scalar()
        if result == 0:
            reviews_df.to_sql('reviews', engine, if_exists='append', index=False)
            print(f"{len(reviews_df)} reviews loaded.")


if __name__ == "__main__":
    try:
        create_tables()
        load_genres()
        load_movies_and_movie_genres()
        load_users()
        load_reviews()
        print("Database initialization complete.")
    except Exception as e:
        print(f"An error occurred during DB initialization: {e}")

```

---

# Flask App

- Python script
- its dependencies
-  the HTML templates
- the `Dockerfile` to containerize it

## flask_app/requirements.txt
```
Flask==3.1.1
psycopg2-binary==2.9.10
SQLAlchemy==2.0.42
pandas==2.3.1
scikit-surprise==1.1.4
```

## flask_app/Dockerfile
```dockerfile
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code into the container at /app
COPY . .

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]
```

## API Endpoint Flask 'App'
```python
import os
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, text
import time

app = Flask(__name__)

# Database connection
DATABASE_URL = os.environ.get('DATABASE_URL')
engine = create_engine(DATABASE_URL)

# Helper function for error responses
def make_error(status_code, message):
    response = jsonify({'status': 'error', 'message': message})
    response.status_code = status_code
    return response

@app.route('/movies', methods=['GET'])
def get_movies():
    """
    Returns a list of movies, with optional filters.
    Query Params:
        first_letter (str, optional): Filters movies by the first letter of the title (case-insensitive).
        release_year (int, optional): Filters movies by the exact release year.
    """
    first_letter = request.args.get('first_letter')
    release_year = request.args.get('release_year')

    query_str = "SELECT movie_id, title, release_date FROM movies"
    filters = []
    params = {}

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
        # Convert rows to a list of dictionaries
        movies_list = [
            {'movie_id': row.movie_id, 'title': row.title, 'release_date': row.release_date.isoformat() if row.release_date else None} 
            for row in result
        ]
        return jsonify(movies_list)

@app.route('/recommendations', methods=['POST'])
def get_recommendations():
    """
    Adds/updates a user review and returns movie recommendations.
    JSON Body:
        movie_id (int): The ID of the movie being reviewed.
        score (int): The rating (1-5).
        gender (str): User's gender ('M', 'F', 'O', etc.).
        occupation (str): User's occupation.
        zip_code (str): User's zip code.
        user_id (int, optional): The user's ID if they are an existing user.
    """
    if not request.is_json:
        return make_error(400, "Request must be JSON.")

    data = request.get_json()
    required_fields = ['movie_id', 'score', 'gender', 'occupation', 'zip_code']
    if not all(field in data for field in required_fields):
        return make_error(400, f"Missing required fields. Must include: {', '.join(required_fields)}")

    user_id = data.get('user_id')
    new_user_id_response = None

    with engine.connect() as connection:
        # --- User Handling ---
        if user_id:
            # Existing user: check if they exist
            user_exists = connection.execute(text("SELECT 1 FROM users WHERE user_id = :user_id"), {'user_id': user_id}).scalar()
            if not user_exists:
                return make_error(404, f"User with user_id {user_id} not found.")
        else:
            # New user: create a new user_id and insert the user
            new_user_id = connection.execute(text("SELECT MAX(user_id) + 1 FROM users")).scalar()
            user_id = new_user_id
            new_user_id_response = user_id # To include in the final response

            insert_user_query = text("""
                INSERT INTO users (user_id, age, gender, occupation, zip_code)
                VALUES (:user_id, NULL, :gender, :occupation, :zip_code)
            """)
            connection.execute(insert_user_query, {
                'user_id': user_id,
                'gender': data['gender'],
                'occupation': data['occupation'],
                'zip_code': data['zip_code']
            })

        # --- Review Handling (Upsert) ---
        upsert_review_query = text("""
            INSERT INTO reviews (user_id, movie_id, rating, timestamp)
            VALUES (:user_id, :movie_id, :rating, extract(epoch from now()))
            ON CONFLICT (user_id, movie_id)
            DO UPDATE SET rating = EXCLUDED.rating, timestamp = extract(epoch from now());
        """)
        connection.execute(upsert_review_query, {
            'user_id': user_id,
            'movie_id': data['movie_id'],
            'rating': data['score']
        })
        
        # --- Recommendation Logic (Placeholder) ---
        # Recommending top 5 most rated movies the user hasn't seen yet.
        # This is where the real ML model's output would be queried.
        recommendations_query = text("""
            SELECT m.movie_id, m.title, COUNT(r.movie_id) as num_ratings
            FROM movies m
            JOIN reviews r ON m.movie_id = r.movie_id
            WHERE m.movie_id NOT IN (SELECT movie_id FROM reviews WHERE user_id = :user_id)
            GROUP BY m.movie_id, m.title
            ORDER BY num_ratings DESC
            LIMIT 5;
        """)
        recommendations_result = connection.execute(recommendations_query, {'user_id': user_id}).fetchall()
        recommendations = [
            {'movie_id': row.movie_id, 'title': row.title, 'reason': f"Popularity ({row.num_ratings} ratings)"}
            for row in recommendations_result
        ]

        # --- Commit transaction and build response ---
        connection.commit()

        response_data = {'recommendations': recommendations}
        if new_user_id_response:
            response_data['new_user_id'] = new_user_id_response
            response_data['message'] = "New user created and review recorded."
        else:
            response_data['message'] = "Review recorded for existing user."
        
        return jsonify(response_data)

if __name__ == '__main__':
    # A short delay to ensure the DB is ready when running locally without docker-compose
    # In docker-compose, `depends_on` handles this.
    if os.environ.get("FLASK_ENV") == "development":
        time.sleep(5)
    app.run(host='0.0.0.0')
```

---

# Running Everything

1.  **Start the Services:** Open a terminal in the root of your `movielens_project` directory and run:
    ```bash
    docker-compose up --build
    ```
    This will build the Flask image, pull the Postgres image, and start both containers. You will see logs from both services in your terminal.

2.  **Initialize the Database:** This only needs to be done **once**. While the services are running, open a **second terminal** and run the following command to execute our data loading script inside the `web` container:
    ```bash
    docker-compose exec web python db_init/load_data.py
    ```
    You should see output like "Tables created...", "19 genres loaded.", "1682 movies loaded.", etc.

3.  **Use the Application:**
    *   Open your web browser and go to `http://localhost:5000`.
    *   You will see the login page. Enter a user ID from the dataset (e.g., `196`, `186`, `22`).
    *   You will be redirected to the user's main page, where you can see their past reviews, add new ones, and see the placeholder recommendations.
    *   Test the genre filter.

You now have a fully functional, containerized web application with a frontend and a robust PostgreSQL backend, ready for the next steps of integrating the real ML model and the Airflow orchestration pipeline.

---

# Run everything last

### Step 4: How to Run and Test the API

The process is the same as before, but your interaction will be with an API client (like `curl` or Postman) instead of a browser.

1.  **Start the Services:** In the project root, run:
    ```bash
    docker-compose up --build
    ```

2.  **Initialize the Database (if you haven't already):** In a second terminal, run:
    ```bash
    docker-compose exec web python db_init/load_data.py
    ```

3.  **Test the API Endpoints:**

    **A) Get a list of all movies:**
    ```bash
    curl http://localhost:5000/movies
    ```

    **B) Get movies starting with 'T' released in 1995:**
    ```bash
    # Note: URLs with '&' should be quoted
    curl "http://localhost:5000/movies?first_letter=T&release_year=1995"
    ```

    **C) Get recommendations for an EXISTING user (user 196 rates movie 242 a 5):**
    ```bash
    curl -X POST http://localhost:5000/recommendations \
    -H "Content-Type: application/json" \
    -d '{
        "user_id": 196,
        "movie_id": 242,
        "score": 5,
        "gender": "M",
        "occupation": "writer",
        "zip_code": "94121"
    }'
    ```    *Expected Response:* A JSON object with a `recommendations` list and a `message`.

    **D) Get recommendations for a NEW user (who rates movie 313 a 4):**
    ```bash
    curl -X POST http://localhost:5000/recommendations \
    -H "Content-Type: application/json" \
    -d '{
        "movie_id": 313,
        "score": 4,
        "gender": "F",
        "occupation": "engineer",
        "zip_code": "90210"
    }'
    ```
    *Expected Response:* A JSON object with a `recommendations` list, a `message`, and a `new_user_id` key (e.g., `"new_user_id": 944`).


# Code Explanation

### 1. `scripts/db_init.py`

This script is a foundational, one-time setup utility. Its sole purpose is to prepare the MovieLens database by creating the required table structure (schema) and loading the initial 100k dataset from the flat files. It is executed automatically by the `entrypoint.sh` script when the `web` container starts for the first time.

#### Granularity Level: Functions

*   **`get_db_engine()`**: A helper function that reads the database connection URL from the environment variables and creates a SQLAlchemy `Engine` object. This engine manages connections to the PostgreSQL database.
*   **`create_tables(engine)`**: Takes the database engine as input and executes a large SQL string to create all seven tables (`genres`, `movies`, `users`, `reviews`, etc.) if they don't already exist. This defines the entire data architecture.
*   **`load_data(engine)`**: The main data ingestion function. It uses the `pandas` library to read the `u.data`, `u.item`, and `u.user` files and loads their contents into the appropriate, newly created database tables. It includes a check to prevent loading the data more than once.
*   **`if __name__ == "__main__"`**: The standard Python entry point. When the script is run directly, it creates the database engine and then calls `create_tables` and `load_data` in the correct sequence.

#### Granularity Level: Functional Code Blocks & Line-by-Line

```python
import os
import pandas as pd
from sqlalchemy import create_engine, text

def get_db_engine():
    # Line 6: Reads the DATABASE_URL from the container's environment variables.
    # If it's not found (e.g., running locally), it uses a default value.
    db_url = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/movielens")
    # Line 8: Creates the SQLAlchemy Engine, which manages a pool of connections to the database.
    return create_engine(db_url)

def create_tables(engine):
    # Line 12: A multi-line string holding all the SQL commands to create our database schema.
    create_sql = """
        # Lines 14-16: Creates a lookup table for genre names and their IDs.
        CREATE TABLE IF NOT EXISTS genres (...);
        # Lines 17-19: Creates the table for core movie information.
        CREATE TABLE IF NOT EXISTS movies (...);
        # Lines 21-25: Creates a "junction table" to link movies and genres, solving the many-to-many relationship.
        # ON DELETE CASCADE means if a movie is deleted, its genre links are also removed.
        CREATE TABLE IF NOT EXISTS movie_genres (...);
        # Lines 26-28: Creates the table for user demographic data.
        CREATE TABLE IF NOT EXISTS users (...);
        # Lines 30-36: The main table for the initial 100k reviews.
        # UNIQUE (user_id, movie_id) ensures a user cannot rate the same movie twice in the base dataset.
        CREATE TABLE IF NOT EXISTS reviews (...);
        # Lines 37-41: A separate table to collect all incoming reviews from the API. This keeps the training data stable.
        CREATE TABLE IF NOT EXISTS new_reviews (...);
        # Lines 42-50: A denormalized table to store the pre-calculated recommendations for fast API lookups.
        # It includes boolean flags for genres to allow for easy filtering on the API side.
        CREATE TABLE IF NOT EXISTS production_recommendations (...);
    """
    # Line 52: Opens a connection from the engine's pool.
    with engine.connect() as connection:
        # Line 54: Executes the entire SQL block to create the tables.
        connection.execute(text(create_sql))
    print("Tables created successfully.")

def load_data(engine):
    with engine.connect() as connection:
        # Lines 60-63: A crucial guardrail. It checks if the 'users' table has any data.
        # If it does, it assumes the data has already been loaded and exits the function to prevent duplication.
        if connection.execute(text("SELECT COUNT(*) FROM users")).scalar() > 0:
            print("Data already loaded. Skipping.")
            return

        # Lines 66-68: Reads the u.genre file using pandas and loads it directly into the 'genres' table.
        genre_df = pd.read_csv('./data/u.genre', sep='|', names=['name', 'genre_id'])
        genre_df.to_sql('genres', engine, if_exists='append', index=False)

        # Lines 71-75: Reads the complex u.item file.
        m_cols = [...]
        movies_df = pd.read_csv(...)
        # Line 76: Converts the release date string to a proper datetime object.
        movies_df['release_date'] = pd.to_datetime(movies_df['release_date'])
        # Line 77: Loads only the core movie info into the 'movies' table.
        movies_df[['movie_id', 'title', 'release_date', 'imdb_url']].to_sql('movies', engine, if_exists='append', index=False)
        
        # Lines 79-84: This block processes the 19 binary genre columns.
        # It iterates through each movie and each genre column. If a genre flag is 1,
        # it creates a dictionary {'movie_id': X, 'genre_id': Y} and appends it to a list.
        # This transforms the wide format into a "long" format suitable for the movie_genres table.
        movie_genres_list = []
        for _, row in movies_df.iterrows():
            for i in range(19):
                if row[f'g{i}'] == 1:
                    movie_genres_list.append({'movie_id': row['movie_id'], 'genre_id': i})
        # Line 85: Converts the list of dictionaries to a DataFrame and loads it into the database.
        pd.DataFrame(movie_genres_list).to_sql('movie_genres', engine, if_exists='append', index=False)

        # Lines 88-90: Loads user data from u.user into the 'users' table.
        users_df = pd.read_csv(...)
        users_df.to_sql('users', engine, if_exists='append', index=False)

        # Lines 93-95: Loads the 100,000 ratings from u.data into the 'reviews' table.
        reviews_df = pd.read_csv(...)
        reviews_df.to_sql('reviews', engine, if_exists='append', index=False)
        
        print("All data loaded successfully.")

if __name__ == "__main__":
    # Lines 99-101: The script's entry point, orchestrating the setup process.
    db_engine = get_db_engine()
    create_tables(db_engine)
    load_data(db_engine)
```

---

### 2. `scripts/initial_training.py`

This is another one-time setup script that runs immediately after `db_init.py`. Its purpose is to create the first "champion" model, evaluate its baseline performance, and pre-calculate recommendations for every user so the API is functional from the very beginning.

#### Granularity Level: Functions

*   **`get_db_engine()`**: The same helper function to connect to the database.
*   **`main()`**: The main function that orchestrates the entire initial training process, from loading data to training the model, evaluating it, and finally storing the pre-computed recommendations back into the database.

#### Granularity Level: Functional Code Blocks & Line-by-Line

```python
import os
import pandas as pd
from sqlalchemy import create_engine, text
from surprise import Dataset, Reader, SVD
from surprise.model_selection import cross_validate
import pickle

def get_db_engine():
    # ... (same as db_init.py)
    pass

def main():
    print("--- Starting Initial Model Training ---")
    engine = get_db_engine()

    # Lines 16-20: Defines file paths for the production model and its performance metric.
    # It ensures the necessary directories exist before trying to save files to them.
    MODELS_DIR = "models"
    PROD_MODEL_PATH = os.path.join(MODELS_DIR, "production", "model.pkl")
    PROD_METRICS_PATH = os.path.join(MODELS_DIR, "production", "metrics.txt")
    os.makedirs(os.path.join(MODELS_DIR, "production"), exist_ok=True)
    os.makedirs(os.path.join(MODELS_DIR, "staging"), exist_ok=True)

    # Lines 23-34: This block loads all necessary data from the database for training and recommendation generation.
    # It gets the base reviews, lists of all users and movies, and the genre information for each movie.
    # The movie_genre_pivoted DataFrame is created to easily add the boolean genre flags to the final recommendations table.
    with engine.connect() as connection:
        reviews_df = pd.read_sql("SELECT user_id, movie_id, rating FROM reviews", connection)
        # ...
        movie_genre_pivoted = movie_genres_df.pivot_table(...)
        # ...

    # Lines 37-44: This is the core model evaluation block.
    # Line 38: `Reader` tells Surprise that our ratings are on a scale of 1 to 5.
    # Line 39: `Dataset.load_from_df` converts the pandas DataFrame into Surprise's internal data format.
    # Line 42: `cross_validate` performs a robust 5-fold cross-validation. It trains and tests the model 5 times on different subsets of the data.
    # Line 43: `rmse` calculates the average Root Mean Squared Error from the 5 folds. A lower RMSE is better.
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(...)
    algo = SVD()
    cv_results = cross_validate(...)
    rmse = cv_results['test_rmse'].mean()
    print(f"Initial Model Mean RMSE: {rmse}")

    # Lines 47-53: This block saves the production-ready model.
    # Line 48: `data.build_full_trainset()` creates a training set from ALL the available data (not just a fold).
    # Line 49: `algo.fit(trainset)` trains the final model on this complete dataset.
    # Line 51: `pickle.dump` serializes the trained model object and saves it to a file.
    # Line 52: The model's RMSE score is saved to a text file. This file acts as the "memory" of the champion model's performance.
    print("Training final model on all data...")
    trainset = data.build_full_trainset()
    algo.fit(trainset)
    with open(PROD_MODEL_PATH, 'wb') as f: pickle.dump(algo, f)
    with open(PROD_METRICS_PATH, 'w') as f: f.write(str(rmse))
    print(f"Model saved to {PROD_MODEL_PATH}")

    # Lines 56-65: This block pre-computes recommendations for every user for every movie they haven't seen.
    # It iterates through every user, finds the movies they haven't rated, and uses the trained model (`algo.predict`)
    # to generate a predicted score for each one. This is computationally expensive, which is why we do it offline.
    print("Pre-computing all recommendations...")
    recs_to_insert = []
    for user_id in all_users:
        rated_movies = reviews_df[reviews_df['user_id'] == user_id]['movie_id']
        movies_to_predict = [m for m in all_movies if m not in rated_movies.values]
        for movie_id in movies_to_predict:
            prediction = algo.predict(uid=user_id, iid=movie_id)
            recs_to_insert.append({'user_id': user_id, 'movie_id': movie_id, 'predicted_rating': prediction.est})
    
    # Lines 67-68: The generated recommendations are merged with the genre flags.
    recs_df = pd.DataFrame(recs_to_insert)
    recs_df = pd.merge(recs_df, movie_genre_pivoted, on='movie_id', how='left').fillna(0)

    # Lines 70-74: This block loads the pre-computed recommendations into the database.
    # Line 71: `TRUNCATE TABLE` completely clears the table to ensure no old data remains.
    # Line 72: `recs_df.to_sql` performs a highly efficient bulk insert of the new recommendations.
    # Line 73: `connection.commit()` finalizes the transaction.
    with engine.connect() as connection:
        connection.execute(text("TRUNCATE TABLE production_recommendations;"))
        recs_df.to_sql('production_recommendations', engine, if_exists='append', index=False)
        connection.commit()
    print(f"Loaded {len(recs_df)} recommendations into the database.")
    print("--- Initial Training Complete ---")

if __name__ == "__main__":
    main()
```

---

### 3. `flask_app/app.py`

This is the live API server. Its only job is to respond to HTTP requests quickly. It achieves this by only performing simple, fast database queries and never doing any heavy computation itself.

#### Granularity Level: Functions

*   **`make_error(status_code, message)`**: A utility function that creates a standardized JSON error response with a given HTTP status code and message.
*   **`get_movies()`**: Implements the `GET /movies` endpoint. It fetches a list of movies from the database and can optionally filter them by the first letter of the title and/or the release year.
*   **`get_user_reviews(user_id)`**: Implements the `GET /reviews/<user_id>` endpoint. It fetches all reviews (both old and new) for a specific user.
*   **`add_review()`**: Implements the `POST /reviews` endpoint. This is the main interactive endpoint. It handles the logic for creating a new user if no `user_id` is provided and then records the new movie review into the `new_reviews` table.

#### Granularity Level: Functional Code Blocks & Line-by-Line

```python
import os
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, text

app = Flask(__name__)
DATABASE_URL = os.environ.get('DATABASE_URL')
engine = create_engine(DATABASE_URL)

def make_error(status_code, message):
    # ... (creates a JSON error object)
    pass

@app.route('/movies', methods=['GET'])
def get_movies():
    # Lines 16-18: Retrieves optional filter parameters from the URL's query string (e.g., ?first_letter=T).
    first_letter = request.args.get('first_letter')
    release_year = request.args.get('release_year')
    # Lines 19-20: Starts building the SQL query.
    query_str = "SELECT movie_id, title, release_date FROM movies"
    filters, params = [], {}
    # Lines 21-23: If a first_letter is provided, it adds a WHERE clause for a case-insensitive search (ILIKE).
    if first_letter:
        filters.append("title ILIKE :letter")
        params['letter'] = f"{first_letter}%"
    # Lines 24-29: If a release_year is provided, it adds a WHERE clause to filter by year.
    if release_year:
        # ...
        filters.append("EXTRACT(YEAR FROM release_date) = :year")
    # Lines 30-32: If any filters were added, it appends the complete WHERE clause to the query string.
    if filters:
        query_str += " WHERE " + " AND ".join(filters)
    query_str += " ORDER BY title;"
    # Lines 34-37: Executes the dynamically built query and formats the result as a JSON list.
    with engine.connect() as connection:
        result = connection.execute(text(query_str), params).fetchall()
        movies_list = [...]
        return jsonify(movies_list)

@app.route('/reviews/<int:user_id>', methods=['GET'])
def get_user_reviews(user_id):
    # Lines 41-46: This SQL query uses UNION ALL to combine results from two tables.
    # It gets all reviews for the user from the base 'reviews' table and all reviews from the 'new_reviews' table.
    # This gives the user a complete view of their rating history.
    query = text("""
        SELECT movie_id, rating, timestamp, 'base' as source FROM reviews WHERE user_id = :user_id
        UNION ALL
        SELECT movie_id, rating, timestamp, 'new' as source FROM new_reviews WHERE user_id = :user_id
        ORDER BY timestamp DESC;
    """)
    # Lines 47-50: Executes the query and returns the combined list as JSON.
    with engine.connect() as connection:
        result = connection.execute(query, {'user_id': user_id}).fetchall()
        reviews_list = [...]
        return jsonify(reviews_list)

@app.route('/reviews', methods=['POST'])
def add_review():
    # Lines 54-61: Basic validation to ensure the request is JSON and contains the required fields.
    if not request.is_json: return make_error(400, "Request must be JSON.")
    data = request.get_json()
    user_id = data.get('user_id')
    # ...

    with engine.connect() as connection:
        # Lines 64-71: This block handles new user creation.
        # If no user_id is provided in the request, it checks for demographic data,
        # generates a new unique user_id (by taking the current max ID + 1),
        # and inserts the new user into the 'users' table.
        if not user_id:
            if not all(k in data for k in ['gender', 'occupation', 'zip_code']):
                return make_error(400, "New users must provide 'gender', 'occupation', and 'zip_code'.")
            new_user_id = connection.execute(text("SELECT MAX(user_id) + 1 FROM users")).scalar()
            user_id = new_user_id
            insert_user_query = text("INSERT INTO users (...) VALUES (...)")
            connection.execute(insert_user_query, {...})
        
        # Line 73: This is the most critical line for data collection.
        # It inserts the new review ONLY into the 'new_reviews' table.
        insert_review_query = text("INSERT INTO new_reviews (...) VALUES (...)")
        # Line 74: Executes the insert.
        connection.execute(insert_review_query, {'user_id': user_id, 'movie_id': movie_id, 'rating': rating})
        # Line 75: Commits the transaction to save the changes.
        connection.commit()

        # Lines 77-80: Builds a success response, including the new_user_id if one was just created.
        response_data = {'status': 'success', 'message': f"Review for movie {movie_id} by user {user_id} collected."}
        if not data.get('user_id'):
            response_data['new_user_id'] = user_id
        return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
```

---

### 4. `airflow/dags/retraining_dag.py`

This file defines the automated, scheduled retraining pipeline. It is not run directly but is read by the Airflow scheduler, which then executes the defined task (`train_and_deploy_if_better`) every two days.

#### Granularity Level: Functions

*   **`retraining_dag()`**: The main function that defines the DAG. The `@dag` decorator tells Airflow that this function describes a workflow, including its ID, schedule, and other metadata.
*   **`train_and_deploy_if_better()`**: The single task within the DAG, marked by the `@task` decorator. This function contains the entire "Champion-Challenger" logic: it loads all data, trains a new model, compares it to the production model, and only deploys it (and updates the database) if it's better.

#### Granularity Level: Functional Code Blocks & Line-by-Line

```python
from __future__ import annotations
import pendulum
from airflow.decorators import dag, task
# ... (other imports)

# Lines 10-13: Defines constants for database URL and model directories.
# Note the path `/opt/airflow/models`, which is the path *inside* the Airflow containers.
DB_URL = "postgresql://user:password@movielens_db:5432/movielens"
MODELS_DIR = "/opt/airflow/models"
# ...

@dag(
    # Lines 16-21: The DAG decorator.
    # `dag_id`: A unique identifier for this workflow in the Airflow UI.
    # `schedule_interval`: A cron expression meaning "at minute 0, hour 0, every 2nd day of the month".
    # `start_date`: When the schedule should become active.
    # `catchup=False`: Prevents the DAG from running for all past, missed schedules upon deployment.
    dag_id="retrain_recommendation_model",
    schedule_interval="0 0 */2 * *",
    start_date=pendulum.datetime(2024, 1, 1, tz="UTC"),
    catchup=False,
    tags=["recommendation", "mlops"],
)
def retraining_dag():
    @task()
    def train_and_deploy_if_better():
        # Lines 29-40: Loads all data required for the pipeline.
        # It loads the base reviews, the new reviews, and metadata.
        # If there are no new reviews, the pipeline exits early to save resources.
        engine = create_engine(DB_URL)
        with engine.connect() as connection:
            base_reviews_df = pd.read_sql("SELECT * FROM reviews", connection)
            new_reviews_df = pd.read_sql("SELECT * FROM new_reviews", connection)
            if new_reviews_df.empty:
                print("No new reviews found. Skipping training.")
                return
            # ... (loads other metadata)

        # Lines 43-45: This is a key data manipulation step.
        # It combines old and new reviews, sorts them by timestamp, and then removes duplicates based on user/movie,
        # keeping only the LAST entry. This correctly handles cases where a user updated their rating.
        combined_df = pd.concat([base_reviews_df, new_reviews_df], ignore_index=True)
        training_df = combined_df.sort_values('timestamp').drop_duplicates(subset=['user_id', 'movie_id'], keep='last')

        # Lines 48-52: Trains the "Challenger" model and evaluates its performance using 5-fold cross-validation,
        # just like in the initial training script.
        reader = Reader(rating_scale=(1, 5))
        data = Dataset.load_from_df(...)
        algo = SVD()
        cv_results = cross_validate(...)
        challenger_rmse = cv_results['test_rmse'].mean()

        # Lines 55-60: Reads the performance metric of the current "Champion" model from its metrics file.
        # It uses a try/except block to handle the case where no production model exists yet.
        try:
            with open(os.path.join(PROD_MODEL_DIR, "metrics.txt"), 'r') as f:
                champion_rmse = float(f.read())
        except FileNotFoundError:
            champion_rmse = float('inf')

        print(f"Champion RMSE: {champion_rmse}, Challenger RMSE: {challenger_rmse}")
        # Line 63: The "Promotion Gate". The code inside this `if` block only runs if the new model is strictly better.
        if challenger_rmse < champion_rmse:
            print("Challenger is better. Promoting to production.")
            # Lines 65-73: The challenger model is retrained on all available data and saved to the staging directory first.
            # This is a safety measure.
            trainset = data.build_full_trainset()
            algo.fit(trainset)
            # ... (save to staging)
            
            # Lines 74-75: `shutil.move` performs an atomic "move" operation. This is very fast and safe.
            # It instantly replaces the old production model with the new one from staging.
            shutil.move(staging_model_path, os.path.join(PROD_MODEL_DIR, "model.pkl"))
            shutil.move(staging_metrics_path, os.path.join(PROD_MODEL_DIR, "metrics.txt"))

            # Lines 78-99: This block activates the new model by updating the database.
            # It pre-computes all new recommendations using the better model.
            # It then truncates the production_recommendations table and bulk-loads the new ones.
            # Finally, it merges the data from `new_reviews` into the base `reviews` table using an `INSERT ... ON CONFLICT`
            # query, which correctly handles both new and updated reviews.
            # The last step is to truncate `new_reviews`, resetting the system for the next 2-day cycle.
            # ... (recommendation generation)
            with engine.connect() as connection:
                connection.execute(text("TRUNCATE TABLE production_recommendations;"))
                recs_df.to_sql(...)
                merge_sql = """..."""
                connection.execute(text(merge_sql))
                connection.execute(text("TRUNCATE TABLE new_reviews;"))
                connection.commit()
            print("System updated with new model.")
        else:
            # Lines 101-102: If the new model isn't better, nothing is changed. The old model remains active,
            # and the collected `new_reviews` are kept to be used in the next training attempt in two days.
            print("Challenger is not better. Discarding.")

    train_and_deploy_if_better()

retraining_dag()
```


# Using LightFM

Of course. This is the right approach. We will refactor the Python scripts to use `LightFM`, creating a single, powerful hybrid model. The goal is clean, readable, and straightforward code that is easy to understand and maintain.

The overall architecture (Docker, Airflow, Postgres) remains the same. The changes are focused on the Python scripts that handle data preparation and model training.

---

### 1. Updated Requirements (`flask_app/requirements.txt`)

We swap `scikit-surprise` for `lightfm` and add `scipy` which is a dependency for handling sparse matrices.

```
Flask==2.2.2
psycopg2-binary==2.9.5
SQLAlchemy==1.4.45
pandas==1.5.2
scipy==1.10.1
lightfm==1.17
```

---

### 2. Database Initialization (`scripts/db_init.py`)

**No changes are needed here.** The database schema we designed is already perfect for this hybrid approach. It correctly normalizes and stores all the user features, item features, and interactions we need. The existing `db_init.py` file can be used as-is.

```python
# scripts/db_init.py
# THIS FILE IS UNCHANGED

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
            is_unknown INT, is_action INT, is_adventure INT, is_animation INT,
            is_childrens INT, is_comedy INT, is_crime INT, is_documentary INT,
            is_drama INT, is_fantasy INT, is_film_noir INT, is_horror INT,
            is_musical INT, is_mystery INT, is_romance INT, is_sci_fi INT,
            is_thriller INT, is_war INT, is_western INT,
            PRIMARY KEY (user_id, movie_id)
        );
    """
    with engine.connect() as connection:
        connection.execute(text(create_sql))
    print("Tables created successfully.")

def load_data(engine):
    """Loads data from the MovieLens 100k files into the database."""
    with engine.connect() as connection:
        if connection.execute(text("SELECT COUNT(*) FROM users")).scalar() > 0:
            print("Data already loaded. Skipping.")
            return

        genre_df = pd.read_csv('./data/u.genre', sep='|', names=['name', 'genre_id'])
        genre_df.to_sql('genres', engine, if_exists='append', index=False)

        m_cols = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url'] + [f'g{i}' for i in range(19)]
        movies_df = pd.read_csv('./data/u.item', sep='|', names=m_cols, encoding='latin-1', usecols=m_cols)
        movies_df['release_date'] = pd.to_datetime(movies_df['release_date'])
        movies_df[['movie_id', 'title', 'release_date', 'imdb_url']].to_sql('movies', engine, if_exists='append', index=False)
        
        movie_genres_list = []
        for _, row in movies_df.iterrows():
            for i in range(19):
                if row[f'g{i}'] == 1:
                    movie_genres_list.append({'movie_id': row['movie_id'], 'genre_id': i})
        pd.DataFrame(movie_genres_list).to_sql('movie_genres', engine, if_exists='append', index=False)

        users_df = pd.read_csv('./data/u.user', sep='|', names=['user_id', 'age', 'gender', 'occupation', 'zip_code'])
        users_df.to_sql('users', engine, if_exists='append', index=False)

        reviews_df = pd.read_csv('./data/u.data', sep='\t', names=['user_id', 'movie_id', 'rating', 'timestamp'])
        reviews_df.to_sql('reviews', engine, if_exists='append', index=False)
        
        print("All data loaded successfully.")

if __name__ == "__main__":
    db_engine = get_db_engine()
    create_tables(db_engine)
    load_data(db_engine)
```

---

### 3. The API Server (`flask_app/app.py`)

The API becomes simpler. We remove the complex fallback logic because the LightFM model can generate recommendations for any user, new or old.

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

@app.route('/movies', methods=['GET'])
def get_movies():
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
    if not request.is_json: return make_error(400, "Request must be JSON.")
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
    Gets pre-computed recommendations for a user.
    This is now a simple, universal endpoint.
    """
    recs_query = text("""
        SELECT m.movie_id, m.title, pr.predicted_rating
        FROM production_recommendations pr
        JOIN movies m ON pr.movie_id = m.movie_id
        WHERE pr.user_id = :user_id
        ORDER BY pr.predicted_rating DESC
        LIMIT 10;
    """)
    with engine.connect() as connection:
        result = connection.execute(recs_query, {'user_id': user_id}).fetchall()
        if not result:
            return make_error(404, f"Recommendations not generated yet for user {user_id}. Please wait for the next training cycle.")
        
        recommendations = [{'movie_id': r.movie_id, 'title': r.title, 'predicted_rating': f"{r.predicted_rating:.2f}"} for r in result]
        return jsonify(recommendations)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
```

---

### 4. Initial Training Script (`scripts/initial_training.py`)

This is where the major changes happen. We introduce the data preparation logic for LightFM.

```python
# scripts/initial_training.py

import os
import pandas as pd
import numpy as np
import pickle
from sqlalchemy import create_engine, text
from scipy.sparse import coo_matrix
from lightfm import LightFM
from lightfm.evaluation import precision_at_k

# --- Helper Functions for LightFM ---

def create_feature_name(col, value):
    """Creates a standard feature name string."""
    return f"{col}:{value}"

def build_feature_mappings(users_df, movies_df, genres_df):
    """Creates mappings from feature names to integer indices."""
    user_feature_map = {}
    item_feature_map = {}

    # User features
    for _, user in users_df.iterrows():
        uid_feature = create_feature_name('user_id', user['user_id'])
        if uid_feature not in user_feature_map: user_feature_map[uid_feature] = len(user_feature_map)
        
        gender_feature = create_feature_name('gender', user['gender'])
        if gender_feature not in user_feature_map: user_feature_map[gender_feature] = len(user_feature_map)
        
        occ_feature = create_feature_name('occupation', user['occupation'])
        if occ_feature not in user_feature_map: user_feature_map[occ_feature] = len(user_feature_map)

    # Item features
    for _, movie in movies_df.iterrows():
        mid_feature = create_feature_name('movie_id', movie['movie_id'])
        if mid_feature not in item_feature_map: item_feature_map[mid_feature] = len(item_feature_map)

    for _, genre in genres_df.iterrows():
        genre_feature = create_feature_name('genre', genre['name'])
        if genre_feature not in item_feature_map: item_feature_map[genre_feature] = len(item_feature_map)
        
    return user_feature_map, item_feature_map

def build_feature_matrix(df, feature_map, is_user_matrix):
    """Builds a sparse feature matrix."""
    rows, cols, data = [], [], []
    
    id_col = 'user_id' if is_user_matrix else 'movie_id'
    
    for _, item in df.iterrows():
        item_id = item[id_col]
        
        # Add ID feature
        id_feature = create_feature_name(id_col, item_id)
        if id_feature in feature_map:
            rows.append(item_id - 1)
            cols.append(feature_map[id_feature])
            data.append(1)
        
        # Add other features
        if is_user_matrix:
            gender_feature = create_feature_name('gender', item['gender'])
            if gender_feature in feature_map:
                rows.append(item_id - 1)
                cols.append(feature_map[gender_feature])
                data.append(1)
            
            occ_feature = create_feature_name('occupation', item['occupation'])
            if occ_feature in feature_map:
                rows.append(item_id - 1)
                cols.append(feature_map[occ_feature])
                data.append(1)
        else: # is_item_matrix
            for genre in item.get('genres', []):
                genre_feature = create_feature_name('genre', genre)
                if genre_feature in feature_map:
                    rows.append(item_id - 1)
                    cols.append(feature_map[genre_feature])
                    data.append(1)

    num_items = len(df)
    num_features = len(feature_map)
    return coo_matrix((data, (rows, cols)), shape=(num_items, num_features))


# --- Main Script ---

def main():
    print("--- Starting Initial Model Training with LightFM ---")
    engine = create_engine(os.getenv("DATABASE_URL"))

    # --- Load all data from DB ---
    with engine.connect() as connection:
        reviews_df = pd.read_sql("SELECT * FROM reviews", connection)
        users_df = pd.read_sql("SELECT * FROM users", connection)
        movies_df = pd.read_sql("SELECT * FROM movies", connection)
        genres_df = pd.read_sql("SELECT * FROM genres", connection)
        movie_genres_df = pd.read_sql("SELECT * FROM movie_genres", connection)

    # --- Prepare Data for LightFM ---
    print("Building feature mappings and matrices...")
    user_map, item_map = build_feature_mappings(users_df, movies_df, genres_df)
    
    # Aggregate genres into a list for each movie
    movie_genres_agg = movie_genres_df.merge(genres_df, on='genre_id').groupby('movie_id')['name'].apply(list).reset_index(name='genres')
    movies_with_genres = movies_df.merge(movie_genres_agg, on='movie_id', how='left')

    user_features = build_feature_matrix(users_df, user_map, is_user_matrix=True)
    item_features = build_feature_matrix(movies_with_genres, item_map, is_user_matrix=False)

    # Build interaction matrix
    reviews_df['rating_binary'] = 1 # LightFM works best with implicit feedback
    interactions = coo_matrix((reviews_df['rating_binary'].values, 
                               (reviews_df['user_id'].values - 1, reviews_df['movie_id'].values - 1)),
                              shape=(len(users_df), len(movies_df)))

    # --- Train and Evaluate Model ---
    print("Training LightFM model...")
    model = LightFM(loss='warp', random_state=42) # WARP is a good default loss
    model.fit(interactions,
              user_features=user_features,
              item_features=item_features,
              epochs=10,
              num_threads=4)

    # Evaluate using Precision@K
    # This metric measures: "out of K recommended items, how many did the user actually interact with?"
    # Higher is better.
    train_precision = precision_at_k(model, interactions, k=10, user_features=user_features, item_features=item_features).mean()
    print(f"Initial Model Training Precision@10: {train_precision}")

    # --- Save Production Model and Mappings ---
    MODELS_DIR = "models"
    PROD_DIR = os.path.join(MODELS_DIR, "production")
    os.makedirs(PROD_DIR, exist_ok=True)
    os.makedirs(os.path.join(MODELS_DIR, "staging"), exist_ok=True)

    with open(os.path.join(PROD_DIR, "model.pkl"), 'wb') as f: pickle.dump(model, f)
    with open(os.path.join(PROD_DIR, "mappings.pkl"), 'wb') as f: pickle.dump({'user_map': user_map, 'item_map': item_map}, f)
    with open(os.path.join(PROD_DIR, "metrics.txt"), 'w') as f: f.write(str(train_precision))
    print("Model and mappings saved to production.")

    # --- Pre-compute and Store Recommendations ---
    print("Pre-computing all recommendations...")
    all_user_ids = users_df['user_id'].values
    all_movie_ids = movies_df['movie_id'].values
    
    # Predict scores for all user-movie pairs
    scores = model.predict(np.repeat(all_user_ids - 1, len(all_movie_ids)),
                           np.tile(all_movie_ids - 1, len(all_user_ids)),
                           user_features=user_features,
                           item_features=item_features)
    
    # Reshape scores into a DataFrame
    recs_df = pd.DataFrame({
        'user_id': np.repeat(all_user_ids, len(all_movie_ids)),
        'movie_id': np.tile(all_movie_ids, len(all_user_ids)),
        'predicted_rating': scores
    })

    # Get genre flags for the recommendations table
    movie_genre_pivoted = movie_genres_df.merge(genres_df, on='genre_id').pivot_table(index='movie_id', columns='name', aggfunc=len, fill_value=0).reset_index()
    genre_cols = [f'is_{g.lower().replace("-", "_")}' for g in movie_genre_pivoted.columns[1:]]
    movie_genre_pivoted.columns = ['movie_id'] + genre_cols
    recs_df = pd.merge(recs_df, movie_genre_pivoted, on='movie_id', how='left').fillna(0)

    with engine.connect() as connection:
        connection.execute(text("TRUNCATE TABLE production_recommendations;"))
        recs_df.to_sql('production_recommendations', engine, if_exists='append', index=False, chunksize=10000)
        connection.commit()
    print(f"Loaded {len(recs_df)} recommendations into the database.")

if __name__ == "__main__":
    main()
```

---

### 5. The Airflow Retraining DAG (`airflow/dags/retraining_dag.py`)

This script is refactored to use the same LightFM logic as the initial training script. The core "Champion-Challenger" logic remains, but the evaluation metric is now `precision_at_k` (higher is better).

```python
# airflow/dags/retraining_dag.py

from __future__ import annotations
import pendulum
from airflow.decorators import dag, task
import pandas as pd
import numpy as np
import pickle
from sqlalchemy import create_engine, text
from scipy.sparse import coo_matrix
from lightfm import LightFM
from lightfm.evaluation import precision_at_k
import os
import shutil

# --- Constants and Helper Functions (can be moved to a separate file) ---
DB_URL = "postgresql://user:password@movielens_db:5432/movielens"
MODELS_DIR = "/opt/airflow/models"
PROD_DIR = os.path.join(MODELS_DIR, "production")
STAGING_DIR = os.path.join(MODELS_DIR, "staging")

def create_feature_name(col, value):
    return f"{col}:{value}"

def build_feature_mappings(users_df, movies_df, genres_df):
    user_feature_map, item_feature_map = {}, {}
    for _, user in users_df.iterrows():
        for col in ['user_id', 'gender', 'occupation']:
            feature = create_feature_name(col, user[col])
            if feature not in user_feature_map: user_feature_map[feature] = len(user_feature_map)
    for _, movie in movies_df.iterrows():
        feature = create_feature_name('movie_id', movie['movie_id'])
        if feature not in item_feature_map: item_feature_map[feature] = len(item_feature_map)
    for _, genre in genres_df.iterrows():
        feature = create_feature_name('genre', genre['name'])
        if feature not in item_feature_map: item_feature_map[feature] = len(item_feature_map)
    return user_feature_map, item_feature_map

def build_feature_matrix(df, feature_map, is_user_matrix):
    rows, cols, data = [], [], []
    id_col = 'user_id' if is_user_matrix else 'movie_id'
    for _, item in df.iterrows():
        item_id = item[id_col]
        id_feature = create_feature_name(id_col, item_id)
        if id_feature in feature_map:
            rows.append(item_id - 1); cols.append(feature_map[id_feature]); data.append(1)
        if is_user_matrix:
            for col in ['gender', 'occupation']:
                feature = create_feature_name(col, item[col])
                if feature in feature_map:
                    rows.append(item_id - 1); cols.append(feature_map[feature]); data.append(1)
        else:
            for genre in item.get('genres', []):
                feature = create_feature_name('genre', genre)
                if feature in feature_map:
                    rows.append(item_id - 1); cols.append(feature_map[feature]); data.append(1)
    return coo_matrix((data, (rows, cols)), shape=(len(df), len(feature_map)))

# --- Airflow DAG Definition ---
@dag(
    dag_id="retrain_lightfm_model",
    schedule_interval="0 0 */2 * *",
    start_date=pendulum.datetime(2024, 1, 1, tz="UTC"),
    catchup=False,
    tags=["recommendation", "lightfm"],
)
def retraining_dag():
    @task()
    def train_and_deploy_if_better():
        engine = create_engine(DB_URL)
        with engine.connect() as connection:
            base_reviews_df = pd.read_sql("SELECT * FROM reviews", connection)
            new_reviews_df = pd.read_sql("SELECT * FROM new_reviews", connection)
            if new_reviews_df.empty:
                print("No new reviews found. Skipping training.")
                return
            users_df = pd.read_sql("SELECT * FROM users", connection)
            movies_df = pd.read_sql("SELECT * FROM movies", connection)
            genres_df = pd.read_sql("SELECT * FROM genres", connection)
            movie_genres_df = pd.read_sql("SELECT * FROM movie_genres", connection)

        # --- Data Prep ---
        combined_df = pd.concat([base_reviews_df, new_reviews_df], ignore_index=True)
        training_df = combined_df.sort_values('timestamp').drop_duplicates(subset=['user_id', 'movie_id'], keep='last')
        
        user_map, item_map = build_feature_mappings(users_df, movies_df, genres_df)
        movie_genres_agg = movie_genres_df.merge(genres_df, on='genre_id').groupby('movie_id')['name'].apply(list).reset_index(name='genres')
        movies_with_genres = movies_df.merge(movie_genres_agg, on='movie_id', how='left')
        user_features = build_feature_matrix(users_df, user_map, is_user_matrix=True)
        item_features = build_feature_matrix(movies_with_genres, item_map, is_user_matrix=False)
        
        training_df['rating_binary'] = 1
        interactions = coo_matrix((training_df['rating_binary'].values, 
                                   (training_df['user_id'].values - 1, training_df['movie_id'].values - 1)),
                                  shape=(len(users_df), len(movies_df)))

        # --- Train and Evaluate Challenger ---
        challenger_model = LightFM(loss='warp', random_state=42)
        challenger_model.fit(interactions, user_features=user_features, item_features=item_features, epochs=10, num_threads=4)
        challenger_precision = precision_at_k(challenger_model, interactions, k=10, user_features=user_features, item_features=item_features).mean()

        # --- Compare with Champion ---
        try:
            with open(os.path.join(PROD_DIR, "metrics.txt"), 'r') as f:
                champion_precision = float(f.read())
        except FileNotFoundError:
            champion_precision = -1.0 # Lower is worse

        print(f"Champion Precision: {champion_precision}, Challenger Precision: {challenger_precision}")
        if challenger_precision > champion_precision:
            print("Challenger is better. Promoting to production.")
            
            # Save to staging then move
            with open(os.path.join(STAGING_DIR, "model.pkl"), 'wb') as f: pickle.dump(challenger_model, f)
            with open(os.path.join(STAGING_DIR, "mappings.pkl"), 'wb') as f: pickle.dump({'user_map': user_map, 'item_map': item_map}, f)
            with open(os.path.join(STAGING_DIR, "metrics.txt"), 'w') as f: f.write(str(challenger_precision))
            
            shutil.move(os.path.join(STAGING_DIR, "model.pkl"), os.path.join(PROD_DIR, "model.pkl"))
            shutil.move(os.path.join(STAGING_DIR, "mappings.pkl"), os.path.join(PROD_DIR, "mappings.pkl"))
            shutil.move(os.path.join(STAGING_DIR, "metrics.txt"), os.path.join(PROD_DIR, "metrics.txt"))

            # --- Update Recommendations and Merge Data ---
            all_user_ids = users_df['user_id'].values
            all_movie_ids = movies_df['movie_id'].values
            scores = challenger_model.predict(np.repeat(all_user_ids - 1, len(all_movie_ids)),
                                              np.tile(all_movie_ids - 1, len(all_user_ids)),
                                              user_features=user_features, item_features=item_features)
            recs_df = pd.DataFrame({'user_id': np.repeat(all_user_ids, len(all_movie_ids)), 'movie_id': np.tile(all_movie_ids, len(all_user_ids)), 'predicted_rating': scores})
            
            movie_genre_pivoted = movie_genres_df.merge(genres_df, on='genre_id').pivot_table(index='movie_id', columns='name', aggfunc=len, fill_value=0).reset_index()
            genre_cols = [f'is_{g.lower().replace("-", "_")}' for g in movie_genre_pivoted.columns[1:]]
            movie_genre_pivoted.columns = ['movie_id'] + genre_cols
            recs_df = pd.merge(recs_df, movie_genre_pivoted, on='movie_id', how='left').fillna(0)

            with engine.connect() as connection:
                connection.execute(text("TRUNCATE TABLE production_recommendations;"))
                recs_df.to_sql('production_recommendations', engine, if_exists='append', index=False, chunksize=10000)
                merge_sql = """
                    INSERT INTO reviews (user_id, movie_id, rating, timestamp)
                    SELECT user_id, movie_id, rating, timestamp FROM new_reviews
                    ON CONFLICT (user_id, movie_id) DO UPDATE 
                    SET rating = EXCLUDED.rating, timestamp = EXCLUDED.timestamp;
                """
                connection.execute(text(merge_sql))
                connection.execute(text("TRUNCATE TABLE new_reviews;"))
                connection.commit()
            print("System updated with new model.")
        else:
            print("Challenger is not better. Discarding.")

    train_and_deploy_if_better()

retraining_dag()
```

# User flow
Of course. These are the perfect final questions to ask to understand the complete behavior of the system and how to interact with it.

Let's break down each point in detail.

---

### 1. The New User Recommendation Lifecycle

**"Will the recommendation change the more the user makes reviews?"**

**Yes, absolutely.** This is the core purpose of our MLOps pipeline. However, it's crucial to understand that the change is **not instantaneous**. It happens in a batch cycle.

Here is the complete lifecycle for a new user:

1.  **First Interaction (Cold Start):** A new user submits their first review. The system has no personalized data for them yet. When they ask for recommendations, the API's fallback logic kicks in, and they receive a list of the **most popular movies** across the entire platform.
2.  **Collecting More Data:** The user continues to rate more movies. Each new rating is saved to the `new_reviews` table. During this period, they will **still receive popularity-based recommendations** because the main production model has not been updated with their new ratings yet.
3.  **The Retraining Event (The Magic Step):** The Airflow DAG runs (either on its 2-day schedule or via a manual trigger).
    *   It takes all the new ratings from the `new_reviews` table.
    *   It combines them with the base data and retrains the SVD model. The model now learns this new user's specific tastes from their rating history.
    *   It pre-computes a brand new set of personalized recommendations for **all users**, including this new user.
    *   It populates the `production_recommendations` table with these new, personalized scores.
4.  **Personalized Experience:** From this point forward, whenever the user requests recommendations, the API will find their pre-computed scores in the `production_recommendations` table and serve them a list of movies tailored specifically to their learned preferences.

**In short: The recommendations get smarter and more personalized for a user every time the Airflow DAG runs and incorporates their new reviews.**

---

### 2. How the `entrypoint.sh` Script is Launched

**"Is the entrypoint.sh script launched just by 'mounting' it?"**

No, and this is a critical Docker concept. Mounting a file and executing it are two separate actions.

1.  **`volumes: - ./airflow/entrypoint.sh:/opt/airflow/entrypoint.sh`**
    *   This line **makes the file available** inside the container. It's like putting a recipe book on the kitchen counter. The file is now present at the path `/opt/airflow/entrypoint.sh` inside the container.

2.  **`entrypoint: /opt/airflow/entrypoint.sh`**
    *   This line **tells Docker to execute the file** as the very first thing when the container starts. It is the primary process. This is the instruction to the chef: "When you start your shift, the first thing you must do is open the recipe book at this location and follow its instructions."

So, you need both: the `volumes` directive to place the script inside the container, and the `entrypoint` directive to tell the container to run it.

---

### 3. Complete API Usage Guide with `curl` Examples

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
```**Expected Response:** A list of Action movies that the model predicts user 944 will like the most.