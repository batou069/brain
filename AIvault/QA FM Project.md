# English

  Part 1: The Whiteboard Presentation


  (You walk up to the whiteboard. The goal is to build the system diagram and concepts as you talk.)

  1. Introduction: Defining Our Role


  "Good morning. I'm here to present a production-grade movie recommendation pipeline.


  It's important to define our system's scope. We are a specialized component within a larger ecosystem. Our sole responsibility is to read user and movie data 
  from a database, train a model to understand user preferences, and write a ranked list of movie recommendations back to the database. We do not handle user
  creation or rating ingestion; we are a batch-processing system that generates predictive intelligence.


  Our core challenge is technical: How do we accurately model complex user taste from extremely sparse data, and how do we automate this process reliably?"


  2. The Core Problem: Why Standard Models Fall Short


  "Let's start with the data's fundamental nature. A user-item interaction matrix—users on one axis, movies on the other—is the classic starting point.


  [Draw a large, sparse matrix with User IDs on the Y-axis and Movie IDs on the X-axis. Fill in a few cells with ratings (e.g., '5', '3') and leave the vast 
  majority empty.]


  This matrix is >99% sparse. Any given user has rated only a tiny fraction of the available movies. This sparsity poses a major problem for many models.


  The first generation of solutions used Collaborative Filtering, which finds similar users or items. But this struggles when there's little overlap.


  The next evolution was Matrix Factorization (MF), like SVD. MF models learn a dense, low-dimensional 'latent factor' vector for each user and each movie. The
  predicted rating is simply the dot product of these two vectors.


  [On the side, write the MF equation: ŷ = uᵢ · mⱼ ]


  This is powerful, but has a critical limitation: it cannot use side features. We have rich data about our users (age, gender, occupation) and movies (genre,
  release year). An SVD model is blind to this; it only knows about the user ID and the movie ID. It can't handle a new movie with no ratings, and it learns
  nothing about a user's genre preferences explicitly."


  3. Our Solution: The Factorization Machine (FM)


  "To overcome these limitations, we chose a Factorization Machine. An FM is a general-purpose predictor that not only handles sparsity but thrives on it by
  explicitly modeling interactions between all features.


  [Write the 2-way FM equation on the board:]
  > ŷ(x) = w₀ + Σ(wᵢxᵢ) + ΣΣ(<vᵢ,vⱼ>xᵢxⱼ)


  Let's break this down:
   4. `w₀` (Global Bias): This is simply the average rating across all movies. Our baseline.
   5. `Σ(wᵢxᵢ)` (Linear Terms): This is identical to a standard linear regression. We learn a weight wᵢ for every single feature—not just user ID and movie ID, but
      also for genre=Action, occupation=Engineer, etc. This already puts us ahead of Matrix Factorization.
   6. `ΣΣ(<vᵢ,vⱼ>xᵢxⱼ)` (Interaction Terms): This is the key innovation. Instead of learning a massive, intractable weight for every possible feature pair (e.g.,
      user_A and genre=Sci-Fi), the FM learns a small, k-dimensional latent vector vᵢ for each feature. The interaction is then modeled as the dot product of these
      vectors. This allows the model to generalize. It can learn the interaction between a user and a genre they've never rated by leveraging what it knows about
      that user's relationship with other genres.


  A naive calculation of this interaction term would be O(n²k), which is too slow. However, as shown in Rendle's paper, the sum can be mathematically
  reformulated to be calculated in O(nk), linear time. My from-scratch implementation uses this reformulation, making training feasible."

  7. System Architecture: The Automated Loop


  "Now, let's look at how we operationalize this model. The entire system is a containerized, automated pipeline.


  [Draw the following flow diagram on the board:]


   8. [Box 1: PostgreSQL DB]
       * Contains raw data tables: users, movies, ratings.
       * Crucially, it also contains a Materialized View. This view pre-joins and pre-processes all the data into a single, clean, model-ready table. This offloads
         the heavy ETL from Python to the highly optimized database engine.


   9. [Arrow labeled "Read"]


   10. [Box 2: Airflow]
       * This is our orchestrator. It runs two dependent DAGs.
       * DAG 1: `refresh_data_dag`: Runs daily. Its only job is to execute REFRESH MATERIALIZED VIEW. It's fast and efficient.
       * DAG 2: `retrain_model_dag`: This is the core ML pipeline. It triggers only on the success of the first DAG.


   11. [Inside the Airflow box, list the steps of the `retrain_model_dag`:]
       * a. Load Data: A simple SELECT * from the materialized view.
       * b. Train Challenger: Trains a new FM model from scratch on this data.
       * c. Evaluate: Compares the challenger's performance against the current production model's metrics.
       * d. Promote or Discard: If the challenger is better, its model artifact (model.pkl) replaces the production one.

   12. [Arrow labeled "Write"]


   13. [Box 3: PostgreSQL DB (again, or point to the first box)]
       * The final step of the DAG uses the new production model to pre-compute the top N recommendations for every user.
       * These are written to a simple table: production_recommendations (user_id, movie_id_array).


  The API that serves these recommendations is now incredibly simple and scalable. It's just a fast, indexed SELECT statement from this final table."

  14. Evaluation and Retrospective


  "A quick note on evaluation. The pipeline currently promotes a model if its Mean Absolute Error (MAE) improves. This is a good measure of predictive accuracy.


  However, our business goal isn't to predict ratings perfectly; it's to create a high-quality ranked list. A better metric for this is NDCG (Normalized 
  Discounted Cumulative Gain), which rewards putting highly-rated movies at the top of the list. If I were to iterate on this, my first change would be to
  replace MAE with NDCG as the core promotion metric.

  Thank you. I'm ready for your questions."

  ---


  Part 2: Deep Dive Q&A

  Chapter 1: The Factorization Machine Model


  Q: You mentioned Matrix Factorization (like SVD) was used before. Why exactly is the FM better? What problem with sparsity does it solve that MF doesn't?
  The core problem with sparsity isn't just missing values; it's the effect this has on learning and generalization.
   * Matrix Factorization's Shortcoming: An MF model learns latent factors for users and items from the ratings matrix alone. It has no mechanism to incorporate
     side features (metadata). If a new movie is added, it has no ratings, so the model has no information to create a latent vector for it—this is the "cold start"
      problem. Similarly, if a user has only rated action movies, the model has no idea how they might feel about a comedy, because it can't see the "comedy"
     feature.
   * How FM Solves This: The FM's design fundamentally changes the input. Instead of a simple (user_id, movie_id) pair, the input is a high-dimensional feature
     vector x containing one-hot encoded data for everything: [user_id, movie_id, user_gender, movie_genre_1, ..., movie_genre_n]. The FM learns a latent vector v
     for every one of these features.
       * This solves the problem of feature interaction in sparse data. The model can now learn the interaction between user_A and genre=Comedy even if that user
         has never rated a comedy. It does this by leveraging the latent vectors it has learned for user_A from their other ratings (e.g., action movies) and the
         latent vector for genre=Comedy learned from other users' ratings of comedies. It learns a "concept" of what "comedy" means in the latent space and can
         project any user into that space.


  Q: Can you explain the linear time complexity calculation of the interaction term in more detail?
  Certainly. The naive approach is:
  ΣΣ(<vᵢ,vⱼ>xᵢxⱼ)
  This involves a double loop over all features n, making it O(n²k).


  The key insight from Rendle's paper is to reformulate this sum. By rearranging the terms, you can prove that the sum is equivalent to:
  0.5 * Σ( (Σ(vᵢxᵢ))² - Σ((vᵢxᵢ)²) )
  Let's analyze this new form:
   1. Σ(vᵢxᵢ): This is the sum of all feature latent vectors, scaled by their feature values xᵢ. Since our input x is sparse, we only need to sum the vectors for
      the non-zero features. This takes O(nk) if dense, but for a sparse vector with m non-zero entries, it's O(mk).
   2. The rest of the operations (squaring the sum, summing the squares, subtraction) are vector operations that are also linear with respect to k.


  Therefore, the entire calculation is dominated by the initial sum, making the complexity O(mk), where m is the number of non-zero features in the input vector.
  This is a massive improvement and makes the model practical.


  Q: How exactly does your Mini-batch Stochastic Gradient Descent (SGD) work for this model?
  SGD is an iterative optimization algorithm. For each mini-batch of training samples, we perform these steps:
   1. Prediction: For each sample x in the batch, calculate the predicted rating ŷ(x) using the current model parameters (w₀, w, V).
   2. Loss Calculation: Compute the error for that prediction, which is (ŷ(x) - y).
   3. Gradient Calculation: Calculate the partial derivative of the loss function with respect to each parameter. This tells us how to adjust each parameter to
      reduce the error. For the FM, the gradients are:
       * ∂Loss/∂w₀ = 2 * (ŷ - y)
       * ∂Loss/∂wᵢ = 2 * (ŷ - y) * xᵢ
       * ∂Loss/∂vᵢ = 2 * (ŷ - y) * (xᵢ * Σ(vⱼxⱼ) - vᵢxᵢ²) (This is the gradient for the reformulated interaction term)
   4. Parameter Update: Update each parameter by taking a small step in the opposite direction of its gradient, scaled by a learning rate α, and accounting for L2
      regularization λ:
       * w₀ ← w₀ - α * ∂Loss/∂w₀
       * wᵢ ← wᵢ - α * (∂Loss/∂wᵢ + 2λwᵢ)
       * vᵢ ← vᵢ - α * (∂Loss/∂vᵢ + 2λvᵢ)
  This process is repeated for all mini-batches for a set number of epochs, and with each pass, the model parameters converge towards values that minimize the
  overall loss.


  Q: How exactly does your Mini-batch Stochastic Gradient Descent (SGD) work for this model?
  SGD is an iterative optimization algorithm. For each mini-batch of training samples, we perform these steps:
  Chapter 2: System Architecture & Design Choices


  Q: Why did you choose to use a Materialized View in PostgreSQL? Why not just do the data processing in Python with Pandas?
  This was a critical design decision for performance, maintainability, and separation of concerns.
   * Performance: PostgreSQL's query optimizer and execution engine are written in highly optimized C. Performing complex joins and transformations on millions of
     rows inside the database is orders of magnitude faster than pulling all the raw data into a Python process and doing the same work with Pandas. The daily
     REFRESH is also very efficient.
   * Separation of Concerns: The materialized view's DDL (Data Definition Language) becomes the single source of truth for what constitutes clean training data.
     Data engineering logic is kept within the database layer, where it belongs. The machine learning script is then decoupled from this; its only job is to read
     from this clean source, not create it. This makes both parts of the system easier to maintain and debug.
   * Efficiency: The ML training script becomes much simpler and faster to start. It doesn't need to hold multiple large dataframes in memory; it just executes
     SELECT * and gets a stream of perfectly formatted data.


  Q: Why use Airflow? Why not a simple cron job?
  While a cron job could trigger a Python script, Airflow provides a far more robust and production-ready solution for orchestrating data pipelines.
   * Dependency Management: Our process has a strict dependency: the data must be refreshed before training begins. Airflow manages this dependency explicitly.
     With cron, you'd have to build fragile timing assumptions (e.g., "run the ETL at 1 AM and the training at 2 AM") which break easily.
   * Monitoring & Alerting: Airflow provides a rich UI to visualize pipeline status, logs for every task, and built-in alerting on failures. A cron job is a black
     box; debugging failures is significantly harder.
   * Backfilling & Re-running: If a run fails or we need to re-process historical data, Airflow's ability to backfill and re-run specific tasks or entire DAGs for
     specific dates is invaluable. This is impossible with cron.
   * Scalability: Airflow can scale to manage hundreds of complex pipelines, with workers distributing the load. It's built for this kind of workload.


  Q: Your system pre-computes all recommendations. How does this design scale, and what are its limitations?
  The pre-computation strategy is the key to the API's scalability.
   * How it Scales: The API itself is stateless and does a simple, indexed read from a database table. This is a very low-latency operation. We can scale
     horizontally by simply adding more instances of the API container behind a load balancer. The database can also be scaled (e.g., with read replicas). The
     bottleneck is not the serving layer; it's the offline batch job.
   * Limitations: The primary limitation is that the recommendations are not real-time. They are only as fresh as the last daily run. If a user rates 5 movies,
     they won't see the effect of those ratings on their recommendations until the next day's pipeline completes. This is a classic trade-off between latency,
     throughput, and freshness. For many applications, daily freshness is perfectly acceptable. The next evolution, as mentioned, would be a hybrid re-ranking
     system to address this.



# Hebrew

### Part 1: פרזנטציית הווייטבורד (גרסה משודרגת)

#### 1. אינטרו: למה אנחנו פה ומה המטרה

"בוקר טוב. אנחנו כאן כדי לדבר על הנכס הכי חשוב שלנו כחברה: **תשומת הלב של היוזר**. בעולם עם אינסוף תוכן, היכולת שלנו להציג את הדבר הנכון בזמן הנכון היא מה שיבדיל אותנו מהמתחרים.

**אז מה המערכת הזאת עושה?** בגדול, היא בונה מנוע פרסונליזציה שיוצר חוויה ייחודית לכל יוזר, ועוזר לו לגלות תוכן שהוא יאהב אבל לא ידע לחפש. זה הופך את המוצר שלנו מדביק (sticky) ומונע נטישה (churn).

אנחנו מתמקדים בהשפעה על מדדים עסקיים ברורים:

- **העלאת Engagement:** לגרום ליוזרים לקיים יותר אינטראקציות עם התוכן.
    
- **שיפור Retention:** לתת ליוזרים סיבה לחזור כל יום.
    
- **הרחבת גילוי התוכן (Content Discovery):** לחשוף את היוזרים לכל קטלוג הסרטים שלנו, לא רק ללהיטים.
    

כדי למדוד את זה, נתמקד ב-KPIs הבאים:

- **Main KPI:** **שיעור הקלקה (CTR) על המלצות.** זה המדד הכי ישיר להצלחה – האם היוזרים סומכים על ההמלצות שלנו ופועלים לפיהן?
    
- **Side KPIs:**
    
    - **גיוון (Diversity):** האם אנחנו ממליצים על מגוון סרטים או תקועים רק על הפופולריים?
        
    - **משך הסשן (Session Duration):** האם יוזרים שמשתמשים בהמלצות נשארים יותר זמן?
        
    - **כיסוי (Coverage):** לאיזה אחוז מהיוזרים ומהסרטים אנחנו מצליחים לייצר המלצות איכותיות?"
        

_(מכאן, ממשיכים עם הצגת הבעיה, הפתרון (FM), והארכיטקטורה כפי שהוצגו קודם)_

---
## Part 1: פרזנטציית הווייטבורד

(אתה ניגש ללוח. המטרה היא לבנות את דיאגרמת המערכת והקונספטים תוך כדי דיבור).

### 1. אינטרו: מה התפקיד שלנו פה

"בוקר טוב. אני כאן כדי להציג פייפליין המלצות סרטים ברמת פרודקשן.

חשוב להגדיר את ה-scope של המערכת שלנו. אנחנו קומפוננטה ספציפית בתוך אקוסיסטם גדול יותר. האחריות הבלעדית שלנו היא לקרוא דאטה של יוזרים וסרטים מהדאטהבייס, לאמן מודל שמבין את ההעדפות שלהם, ולכתוב חזרה לדאטהבייס רשימה מדורגת של המלצות. אנחנו **לא** מטפלים ביצירת יוזרים או קליטת דירוגים; אנחנו מערכת batch שכל תפקידה הוא לייצר אינטליגנציה חיזויית.

האתגר המרכזי שלנו הוא טכני: איך אנחנו ממדלים במדויק טעם מורכב של יוזרים מדאטה סופר דליל (sparse), ואיך אנחנו הופכים את התהליך הזה לאוטומטי ואמין?"

---

### 2. בעיית הליבה: למה מודלים סטנדרטיים לא מספיקים

"בואו נתחיל מהטבע הבסיסי של הדאטה. נקודת הפתיחה הקלאסית היא מטריצת אינטראקציות יוזר-אייטם – יוזרים בציר אחד, סרטים בציר השני.

[צייר על הלוח מטריצה גדולה וריקה עם User IDs בציר ה-Y ו-Movie IDs בציר ה-X. מלא כמה תאים בודדים עם דירוגים (למשל '5', '3') והשאר את הרוב המכריע ריק.]

המטריצה הזאת היא מעל 99% sparse. כל יוזר נתון דירג אחוז אפסי מהסרטים הקיימים. הדלילות הזאת היא בעיה ענקית עבור רוב המודלים.

הדור הראשון של הפתרונות השתמש ב-**Collaborative Filtering**, שמוצא יוזרים או אייטמים דומים. אבל זה מתקשה כשאין מספיק חפיפה.

האבולוציה הבאה הייתה **Matrix Factorization** (MF), כמו SVD. מודלי MF לומדים וקטור 'לאטנטי' (latent factor) דחוס ונמוך-מימד עבור כל יוזר ועבור כל סרט. הדירוג החזוי הוא פשוט המכפלה הסקלרית (dot product) של שני הוקטורים האלה.

[בצד, רשום את נוסחת ה-MF: y^​=ui​⋅mj​]

זה חזק, אבל יש לזה מגבלה קריטית: **זה לא יכול להשתמש ב-side features**. יש לנו דאטה עשיר על היוזרים שלנו (גיל, מגדר, מקצוע) ועל הסרטים (ז'אנר, שנת יציאה). מודל SVD עיוור לכל זה; הוא מכיר רק את ה-user ID וה-movie ID. הוא לא יכול להתמודד עם סרט חדש שאין לו דירוגים, והוא לא לומד כלום על העדפות הז'אנר של היוזר באופן מפורש."

---

### 3. הפתרון שלנו: Factorization Machine (FM)

"כדי להתגבר על המגבלות האלה, בחרנו ב-Factorization Machine. FM הוא מודל חיזוי כללי שלא רק מתמודד עם דלילות, אלא משגשג בזכותה על ידי מידול מפורש של אינטראקציות בין כל הפיצ'רים.

[רשום על הלוח את הנוסחה של 2-way FM:]

y^​(x)=w0​+∑(wi​xi​)+∑∑(⟨vi​,vj​⟩xi​xj​)

בואו נפרק את זה:

- `w₀` (**Global Bias**): זה פשוט הדירוג הממוצע בכל הסרטים. הבייסליין שלנו.
    
- `Σ(wᵢxᵢ)` (**Linear Terms**): זה זהה לרגרסיה לינארית סטנדרטית. אנחנו לומדים משקל wi​ לכל פיצ'ר בודד – לא רק user ID ו-movie ID, אלא גם ל-genre=Action, occupation=Engineer, וכו'. זה כבר שם אותנו לפני Matrix Factorization.
    
- `ΣΣ(<vᵢ,vⱼ>xᵢxⱼ)` (**Interaction Terms**): זאת החדשנות המרכזית. במקום ללמוד משקל ענק ובלתי אפשרי לכל זוג פיצ'רים אפשרי (למשל, user_A ו-genre=Sci-Fi), ה-FM לומד וקטור לאטנטי קטן, מממד k, לכל פיצ'ר. האינטראקציה מחושבת כמכפלה הסקלרית של הוקטורים האלה. זה מאפשר למודל לעשות הכללה (generalize). הוא יכול ללמוד את האינטראקציה בין יוזר לז'אנר שהוא מעולם לא דירג, על ידי מינוף מה שהוא יודע על הקשר של היוזר הזה עם ז'אנרים אחרים.
    

חישוב נאיבי של איבר האינטראקציה הזה יהיה O(n2k), שזה איטי מדי. עם זאת, כמו שהראה רנדל במאמר שלו, ניתן לנסח מחדש את הסכום מתמטית כך שיחושב בזמן לינארי, O(nk). המימוש from-scratch שלי משתמש בטריק הזה, מה שהופך את האימון לאפשרי."

---

### 4. ארכיטקטורת המערכת: הלופ האוטומטי

"עכשיו, בואו נראה איך אנחנו מתפעלים את המודל הזה (operationalize). כל המערכת היא פייפליין אוטומטי שמורץ בקונטיינר.

[צייר את הדיאגרמה הבאה על הלוח:]

- **[קופסה 1: PostgreSQL DB]**
    
    - מכיל טבלאות דאטה גולמי: users, movies, ratings.
        
    - והכי חשוב, הוא מכיל **Materialized View**. ה-view הזה עושה pre-join ו-pre-process לכל הדאטה לטבלה אחת נקייה ומוכנה למודל. זה מוריד את עבודת ה-ETL הכבדה מפייתון למנוע הדאטהבייס המאוד אופטימלי.
        
- **[חץ עם הכיתוב "Read"]**
    
- **[קופסה 2: Airflow]**
    
    - זה האורקסטרייטור שלנו. הוא מריץ שני DAGs תלויים.
        
    - **DAG 1: `refresh_data_dag`**: רץ פעם ביום. התפקיד היחיד שלו הוא להריץ `REFRESH MATERIALIZED VIEW`. זה מהיר ויעיל.
        
    - **DAG 2: `retrain_model_dag`**: זה פייפליין ה-ML המרכזי. הוא רץ רק אחרי שה-DAG הראשון מצליח.
        
- **[בתוך קופסת ה-Airflow, רשום את השלבים של `retrain_model_dag`:]**
    
    - א. **Load Data:** `SELECT *` פשוט מה-materialized view.
        
    - ב. **Train Challenger:** מאמן מודל FM חדש from scratch על הדאטה הזה.
        
    - ג. **Evaluate:** משווה את הביצועים של ה-challenger מול המטריקות של מודל הפרודקשן הנוכחי.
        
    - ד. **Promote or Discard:** אם ה-challenger טוב יותר, ה-artifact שלו (`model.pkl`) מחליף את זה של הפרודקשן.
        
- **[חץ עם הכיתוב "Write"]**
    
- **[קופסה 3: PostgreSQL DB (שוב, או להצביע לקופסה הראשונה)]**
    
    - השלב האחרון ב-DAG משתמש במודל הפרודקשן החדש כדי לחשב מראש (pre-compute) את N ההמלצות המובילות לכל יוזר.
        
    - ההמלצות נכתבות לטבלה פשוטה: `production_recommendations` (`user_id`, `movie_id_array`).
        

ה-API שמגיש את ההמלצות האלה הוא עכשיו סופר פשוט וסקיילבילי. הוא בסך הכל עושה `SELECT` מהיר עם אינדקס מהטבלה הסופית הזאת."

---

### 5. מדידה ורטרוספקטיבה

"הערה קצרה על מדידה. כרגע הפייפליין מקדם מודל אם ה-**Mean Absolute Error (MAE)** שלו משתפר. זו מטריקה טובה לדיוק החיזוי.

עם זאת, היעד העסקי שלנו הוא לא לחזות דירוגים באופן מושלם, אלא לייצר רשימה מדורגת איכותית. מטריקה טובה יותר לזה היא **NDCG** (Normalized Discounted Cumulative Gain), שמתגמלת על הצבת סרטים עם דירוג גבוה בראש הרשימה. אם הייתי עושה איטרציה על זה, השינוי הראשון שלי היה להחליף את MAE ב-NDCG כמטריקת הקידום המרכזית.

תודה. אני מוכן לשאלות."

---

---

## Part 2: Deep Dive Q&A

### פרק 1: מודל ה-Factorization Machine

**ש: ציינת שהשתמשו ב-Matrix Factorization (כמו SVD) בעבר. למה בדיוק ה-FM טוב יותר? איזו בעיית דלילות הוא פותר ש-MF לא?**

בעיית הליבה עם דלילות היא לא רק ערכים חסרים; זו ההשפעה של זה על הלמידה וההכללה.

- **החיסרון של Matrix Factorization:** מודל MF לומד latent factors ליוזרים ואייטמים ממטריצת הדירוגים בלבד. אין לו שום מנגנון לשלב side features (מטא-דאטה). אם מוסיפים סרט חדש, אין לו דירוגים, ולכן למודל אין מידע כדי ליצור עבורו וקטור לאטנטי – זו בעיית ה-**"cold start"**. באופן דומה, אם יוזר דירג רק סרטי אקשן, למודל אין מושג מה הוא עשוי לחשוב על קומדיה, כי הוא לא "רואה" את הפיצ'ר "קומדיה".
    
- **איך FM פותר את זה:** העיצוב של ה-FM משנה את האינפוט באופן יסודי. במקום זוג פשוט של (user_id, movie_id), האינפוט הוא וקטור פיצ'רים רב-ממדי x שמכיל דאטה בקידוד one-hot להכל: `[user_id, movie_id, user_gender, movie_genre_1, ..., movie_genre_n]`. ה-FM לומד וקטור לאטנטי v לכל אחד מהפיצ'רים האלה.
    
    - זה פותר את בעיית האינטראקציה בין פיצ'רים בדאטה דליל. המודל יכול עכשיו ללמוד את האינטראקציה בין user_A לבין genre=Comedy גם אם היוזר הזה מעולם לא דירג קומדיה. הוא עושה זאת על ידי מינוף הוקטורים הלאטנטיים שלמד עבור user_A מהדירוגים האחרים שלו (למשל, סרטי אקשן) והוקטור הלאטנטי של genre=Comedy שנלמד מהדירוגים של יוזרים אחרים לקומדיות. הוא לומד "קונספט" של מה זה "קומדיה" במרחב הלאטנטי ויכול להטיל (project) כל יוזר למרחב הזה.
        

**ש: תוכל להסביר יותר בפירוט את חישוב הסיבוכיות הלינארית של איבר האינטראקציה?**

בטח. הגישה הנאיבית היא:

∑∑(⟨vi​,vj​⟩xi​xj​)

זה דורש לולאה כפולה על כל n הפיצ'רים, מה שהופך את הסיבוכיות ל-O(n2k).

האינסייט המרכזי מהמאמר של רנדל הוא לנסח מחדש את הסכום הזה. על ידי סידור מחדש של האיברים, אפשר להוכיח שהסכום שקול לביטוי הבא:

0.5⋅f=1∑k​!​(i=1∑n​vi,f​xi​)2−i=1∑n​vi,f2​xi2​)

0.5⋅f=1∑k​​(i=1∑n​vi,f​xi​)2−i=1∑n​vi,f2​xi2​​​

בוא ננתח את הנוסחה החדשה הזאת:

1. ∑(vi​xi​): זה סכום כל הוקטורים הלאטנטיים של הפיצ'רים, כשהם משוקללים בערכי הפיצ'ר xi​. מכיוון שהאינפוט x שלנו הוא sparse, אנחנו צריכים לסכום רק את הוקטורים של הפיצ'רים שאינם אפס. זה לוקח O(nk) אם הוקטור דחוס, אבל עבור וקטור sparse עם m ערכים שאינם אפס, זה O(mk).
    
2. שאר הפעולות (העלאה בריבוע של הסכום, סכימת הריבועים, חיסור) הן פעולות וקטוריות שגם הן לינאריות ביחס ל-k.
    

לכן, החישוב כולו נשלט על ידי הסכום הראשוני, מה שהופך את הסיבוכיות ל-O(mk), כאשר m הוא מספר הפיצ'רים שאינם אפס בוקטור האינפוט. זה שיפור מסיבי שהופך את המודל לפרקטי.

**ש: איך בדיוק עובד ה-Mini-batch Stochastic Gradient Descent (SGD) שלך עבור המודל הזה?**

SGD הוא אלגוריתם אופטימיזציה איטרטיבי. עבור כל מיני-באץ' של דגימות אימון, אנחנו מבצעים את השלבים הבאים:

1. **חיזוי (Prediction):** לכל דגימה x בבאץ', מחשבים את הדירוג החזוי y^​(x) באמצעות הפרמטרים הנוכחיים של המודל (w0​,w,V).
    
2. **חישוב Loss:** מחשבים את השגיאה עבור החיזוי הזה, שהיא (y^​(x)−y).
    
3. **חישוב גרדיאנט:** מחשבים את הנגזרת החלקית של פונקציית ה-Loss ביחס לכל פרמטר. זה אומר לנו איך להתאים כל פרמטר כדי להקטין את השגיאה. עבור FM, הגרדיאנטים הם:
    
    - ∂w0​∂Loss​=2⋅(y^​−y)
        
    - ∂wi​∂Loss​=2⋅(y^​−y)⋅xi​
        
    - ∂vi​∂Loss​=2⋅(y^​−y)⋅(xi​∑(vj​xj​)−vi​xi2​) (זה הגרדיאנט עבור איבר האינטראקציה המנוסח מחדש)
        
4. **עדכון פרמטרים:** מעדכנים כל פרמטר על ידי צעד קטן בכיוון ההפוך לגרדיאנט שלו, מוכפל ב-learning rate α, ובהתחשב ברגולריזציית L2 λ:
    
    - w0​←w0​−α⋅∂w0​∂Loss​
        
    - wi​←wi​−α⋅(∂wi​∂Loss​+2λwi​)
        
    - vi​←vi​−α⋅(∂vi​∂Loss​+2λvi​)
        

התהליך הזה חוזר על עצמו עבור כל המיני-באצ'ים למספר קבוע של איפוקים (epochs), ובכל מעבר כזה, פרמטרי המודל מתכנסים לערכים שממזערים את ה-Loss הכולל.

---

### פרק 2: ארכיטקטורה והחלטות עיצוב

**ש: למה בחרת להשתמש ב-Materialized View ב-PostgreSQL? למה לא פשוט לעשות את עיבוד הדאטה בפייתון עם Pandas?**

זו הייתה החלטת דיזיין קריטית עבור ביצועים, תחזוקתיות והפרדת אחריויות (separation of concerns).

- **ביצועים:** האופטימייזר ומנוע ההרצה של PostgreSQL כתובים ב-C סופר-אופטימלי. ביצוע של join-ים וטרנספורמציות מורכבות על מיליוני שורות בתוך הדאטהבייס הוא מהיר בסדרי גודל מאשר למשוך את כל הדאטה הגולמי לתהליך פייתון ולעשות את אותה עבודה עם Pandas. גם ה-`REFRESH` היומי הוא מאוד יעיל.
    
- **הפרדת אחריויות:** ה-DDL (Data Definition Language) של ה-materialized view הופך להיות ה-source of truth היחיד למהו דאטה נקי לאימון. לוגיקת ה-data engineering נשארת בשכבת הדאטהבייס, איפה שהיא שייכת. סקריפט ה-ML מנותק מזה; התפקיד היחיד שלו הוא לקרוא מהמקור הנקי הזה, לא ליצור אותו. זה הופך את שני חלקי המערכת לקלים יותר לתחזוקה ודיבוג.
    
- **יעילות:** סקריפט אימון ה-ML הופך להרבה יותר פשוט ומהיר להרצה. הוא לא צריך להחזיק כמה דאטה-פריימים גדולים בזיכרון; הוא פשוט מריץ `SELECT *` ומקבל stream של דאטה בפורמט מושלם.
    

**ש: למה להשתמש ב-Airflow? למה לא cron job פשוט?**

למרות ש-cron job יכול להריץ סקריפט פייתון, Airflow מספק פתרון הרבה יותר רובסטי ומוכן לפרודקשן לאורקסטרציה של פייפליינים.

- **ניהול תלויות (Dependency Management):** לתהליך שלנו יש תלות קריטית: הדאטה חייב להתרענן לפני שהאימון מתחיל. Airflow מנהל את התלות הזו באופן מפורש. עם cron, היית צריך לבנות הנחות תזמון שבריריות (למשל, "תריץ את ה-ETL ב-1 בלילה ואת האימון ב-2 בלילה") שנשברות בקלות.
    
- **ניטור והתראות (Monitoring & Alerting):** ל-Airflow יש UI עשיר כדי לראות את סטטוס הפייפליינים, לוגים לכל טאסק, והתראות מובנות על כישלונות. cron job הוא קופסה שחורה; לדבג תקלות בו קשה משמעותית יותר.
    
- **Backfilling והרצות חוזרות:** אם ריצה נכשלת או שאנחנו צריכים לעבד מחדש דאטה היסטורי, היכולת של Airflow לעשות backfill ולהריץ מחדש טאסקים ספציפיים או DAG-ים שלמים לתאריכים מסוימים היא יקרת ערך. זה בלתי אפשרי עם cron.
    
- **סקיילביליות:** Airflow יכול לגדול ולנהל מאות פייפליינים מורכבים, עם worker-ים שמפזרים את העומס. הוא בנוי לסוג כזה של workload.
    

**ש: המערכת שלך מחשבת מראש את כל ההמלצות. איך הדיזיין הזה עומד בסקייל, ומה המגבלות שלו?**

אסטרטגיית החישוב מראש היא המפתח לסקיילביליות של ה-API.

- **איך זה סקיילבילי:** ה-API עצמו הוא stateless ועושה קריאה פשוטה עם אינדקס מטבלת דאטהבייס. זו פעולה עם low-latency. אנחנו יכולים לגדול הוריזונטלית (scale horizontally) על ידי הוספת עוד אינסטנסים של קונטיינר ה-API מאחורי load balancer. גם הדאטהבייס יכול לגדול (למשל, עם read replicas). צוואר הבקבוק הוא לא שכבת ההגשה; הוא עבודת ה-batch שרצה offline.
    
- **מגבלות:** המגבלה העיקרית היא שההמלצות הן לא real-time. הן עדכניות רק כמו הריצה היומית האחרונה. אם יוזר מדרג 5 סרטים, הוא לא יראה את ההשפעה של הדירוגים האלה על ההמלצות שלו עד שהפייפליין של מחר יסתיים. זה trade-off קלאסי בין latency, throughput ועדכניות. עבור הרבה אפליקציות, עדכניות יומית היא סבירה לחלוטין. האבולוציה הבאה, כפי שצוין, תהיה מערכת היברידית של re-ranking כדי לטפל בזה.</p>

---

## Part 2: Deep Dive Q&A (גרסה מורחבת)

### פרק 1: מודל, אופטימיזציה ומדידה

#### ש: הסברת בקצרה על Gradient Descent. אפשר לפרט יותר על איך זה עובד?

בוודאי. **Gradient Descent** הוא אלגוריתם האופטימיזציה הבסיסי ביותר ב-Machine Learning. תחשוב שאתה עומד על צלע הר בערפל סמיך, ואתה רוצה להגיע לנקודה הכי נמוכה בעמק (זו הנקודה שבה שגיאת המודל, ה-"Loss", היא מינימלית).

1. **מהו ה-Gradient?** אתה לא רואה את כל העמק, אבל אתה יכול להרגיש את השיפוע (gradient) מתחת לרגליים שלך. השיפוע אומר לך מה הכיוון הכי תלול _לעלייה_. הגרדיאנט הוא פשוט וקטור של נגזרות חלקיות של פונקציית ה-Loss, לפי כל אחד מהפרמטרים של המודל.
    
2. **הצעד:** כדי לרדת, אתה עושה צעד בדיוק בכיוון **ההפוך** לגרדיאנט.
    
3. **קצב הלמידה (Learning Rate):** גודל הצעד שאתה עושה נקבע על ידי ה-"Learning Rate" (אלפא, α). צעד גדול מדי, ואתה עלול "לדלג" מעל הנקודה הנמוכה. צעד קטן מדי, וייקח לך נצח להגיע לתחתית.
    

**Mini-Batch SGD** הוא וריאציה יעילה: במקום לחשב את השיפוע על סמך כל מיליוני הדגימות (שזה איטי) או על סמך דגימה אחת כל פעם (שזה רועש), אנחנו מחשבים אותו על קבוצה קטנה ("מיני-באץ'"), למשל 128 דגימות. זה נותן לנו אומדן מספיק טוב של השיפוע, והתהליך מתקדם מהר ויציב.

#### ש: הזכרת את הנגזרות ב-SGD. תוכל להראות איך הגעת אליהן עבור ה-Factorization Machine?

כן, זה תהליך שמתבסס על כלל השרשרת. נתחיל עם פונקציית ה-Loss שלנו, שהיא בדרך כלל Squared Error:

L=(y^​−y)2

כאשר y^​ הוא החיזוי של המודל ו-y הוא הדירוג האמיתי.

המטרה שלנו היא למצוא את הנגזרת של L לפי כל פרמטר θ במודל (θ יכול להיות w0​, wi​, או vif​).

לפי כלל השרשרת:

$$\frac{\partial L}{\partial \theta} = \frac{\partial L}{\partial ŷ} \cdot \frac{\partial ŷ}{\partial \theta} = 2(ŷ - y) \cdot \frac{\partial ŷ}{\partial \theta}$$החלק 2(y^​−y) משותף לכולם. עכשיו נמצא את הנגזרת של החיזוי y^​ לפי כל פרמטר:

y^​(x)=w0​+i=1∑n​wi​xi​+i=1∑n​j=i+1∑n​⟨vi​,vj​⟩xi​xj​

1. הנגזרת לפי w0​ (Global Bias):
    
    ∂w0​∂y^​​=1
    
    ולכן הגרדיאנט המלא הוא: ∂w0​∂L​=2(y^​−y)
    
2. הנגזרת לפי wi​ (משקל לינארי):
    
    ∂wi​∂y^​​=xi​
    
    ולכן הגרדיאנט המלא הוא: ∂wi​∂L​=2(y^​−y)xi​
    
3. הנגזרת לפי vif​ (רכיב f בוקטור הלאטנטי של פיצ'ר i):
    
    זה החלק המורכב. אנחנו צריכים לגזור רק את איבר האינטראקציה, ועדיף להשתמש בנוסחה היעילה של רנדל:
    
    i<j∑​⟨vi​,vj​⟩xi​xj​=21​f=1∑k​![](data:image/svg+xml;utf8,<svg%20xmlns="http://www.w3.org/2000/svg"%20width="0.875em"%20height="3.600em"%20viewBox="0%200%20875%203600"><path%20d="M863,9c0,-2,-2,-5,-6,-9c0,0,-17,0,-17,0c-12.7,0,-19.3,0.3,-20,1
    c-5.3,5.3,-10.3,11,-15,17c-242.7,294.7,-395.3,682,-458,1162c-21.3,163.3,-33.3,349,
    -36,557%20l0,84c0.2,6,0,26,0,60c2,159.3,10,310.7,24,454c53.3,528,210,
    949.7,470,1265c4.7,6,9.7,11.7,15,17c0.7,0.7,7,1,19,1c0,0,18,0,18,0c4,-4,6,-7,6,-9
    c0,-2.7,-3.3,-8.7,-10,-18c-135.3,-192.7,-235.5,-414.3,-300.5,-665c-65,-250.7,-102.5,
    -544.7,-112.5,-882c-2,-104,-3,-167,-3,-189
    l0,-92c0,-162.7,5.7,-314,17,-454c20.7,-272,63.7,-513,129,-723c65.3,
    -210,155.3,-396.3,270,-559c6.7,-9.3,10,-15.3,10,-18z"></path></svg>)​(i=1∑n​vif​xi​)2−i=1∑n​vif2​xi2​![](data:image/svg+xml;utf8,<svg%20xmlns="http://www.w3.org/2000/svg"%20width="0.875em"%20height="3.600em"%20viewBox="0%200%20875%203600"><path%20d="M76,0c-16.7,0,-25,3,-25,9c0,2,2,6.3,6,13c21.3,28.7,42.3,60.3,
    63,95c96.7,156.7,172.8,332.5,228.5,527.5c55.7,195,92.8,416.5,111.5,664.5
    c11.3,139.3,17,290.7,17,454c0,28,1.7,43,3.3,45l0,9
    c-3,4,-3.3,16.7,-3.3,38c0,162,-5.7,313.7,-17,455c-18.7,248,-55.8,469.3,-111.5,664
    c-55.7,194.7,-131.8,370.3,-228.5,527c-20.7,34.7,-41.7,66.3,-63,95c-2,3.3,-4,7,-6,11
    c0,7.3,5.7,11,17,11c0,0,11,0,11,0c9.3,0,14.3,-0.3,15,-1c5.3,-5.3,10.3,-11,15,-17
    c242.7,-294.7,395.3,-681.7,458,-1161c21.3,-164.7,33.3,-350.7,36,-558
    l0,-144c-2,-159.3,-10,-310.7,-24,-454c-53.3,-528,-210,-949.7,
    -470,-1265c-4.7,-6,-9.7,-11.7,-15,-17c-0.7,-0.7,-6.7,-1,-18,-1z"></path></svg>)​
    
    כאשר גוזרים את הביטוי הזה לפי vif​ ספציפי, כל שאר האיברים נופלים ונשארים רק עם:
    
    ∂vif​∂y^​​=21​(2(j=1∑n​vjf​xj​)xi​−2vif​xi2​)=xi​j=1∑n​vjf​xj​−vif​xi2​
    
    ולכן הגרדיאנט המלא הוא: ∂vif​∂L​=2(y^​−y)(xi​∑j=1n​vjf​xj​−vif​xi2​)
    

אלו בדיוק הנוסחאות שמשמשות לעדכון הפרמטרים בכל צעד של SGD.

#### ש: אמרת ש-MAE היא לא המטריקה הכי טובה. מהן המטריקות העדיפות למדידת איכות של דירוג, ולמה?

נכון. מדדים כמו MAE או RMSE (Root Mean Squared Error) מודדים **דיוק של חיזוי**. הם עונים על השאלה "בכמה טעינו בחיזוי הדירוג?". אבל הבעיה היא שהם לא מתייחסים ל**מיקום** של הטעות. מבחינתם, לטעות בכוכב אחד בסרט שבמקום הראשון ברשימה זהה לטעות בכוכב אחד בסרט שבמקום ה-50. עסקית, זה הבדל של שמיים וארץ.

אנחנו צריכים מדדי דירוג (Ranking Metrics). הפופולרי ביותר הוא **NDCG (Normalized Discounted Cumulative Gain)**.

- **Gain (G):** ערך הרלוונטיות של כל פריט. למשל, דירוג של 5 כוכבים.
    
- **Cumulative Gain (CG):** סכום הרלוונטיות של כל הפריטים ברשימה. זה עדיין לא מתייחס לסדר.
    
- **Discounted Cumulative Gain (DCG):** כאן נכנס הקסם. אנחנו נותנים "עונש" (discount) לפריטים שנמצאים נמוך יותר ברשימה. הרעיון הוא שפריט רלוונטי במקום ה-10 שווה פחות מפריט רלוונטי במקום ה-1. הנוסחה היא: DCGp​=∑i=1p​log2​(i+1)reli​​
    
- **Normalized DCG (NDCG):** כדי שהציון יהיה בין 0 ל-1 ונוכל להשוות בין יוזרים, אנחנו מחלקים את ה-DCG של הרשימה שלנו ב-DCG האידיאלי (IDCG) - כלומר, ה-DCG של רשימה שהייתה מסודרת באופן מושלם.
    

**בשורה התחתונה, NDCG מתגמל מודלים שמצליחים לשים את הפריטים הכי רלוונטיים בראש הרשימה**, וזה בדיוק מה שאנחנו רוצים עסקית. מדדים נוספים טובים הם **MAP** (Mean Average Precision) ו-**MRR** (Mean Reciprocal Rank).

---

### פרק 2: ארכיטקטורה, סקיילביליות ותפעול

#### ש: הזכרת Airflow ו-DAG. תוכל להסביר לעומק מה זה ולמה זה עדיף על cron?

**DAG** הוא ראשי תיבות של **Directed Acyclic Graph** - גרף מכוון ללא לולאות. זו הדרך הכי טובה לתאר תהליך שיש בו שלבים ותלויות. כל צומת בגרף הוא משימה (task), וכל חץ מייצג תלות - משימה ב' יכולה להתחיל רק אחרי שמשימה א' הסתיימה בהצלחה.

הפייפליין שלנו הוא DAG פשוט אך קריטי:

[Start] -> [Refresh Data View] -> [Train New Model] -> [Evaluate Model] -> [Promote if Better] -> [Pre-compute Recommendations] -> [End]

**Airflow** הוא הפלטפורמה שמריצה, מנהלת ומנטרת DAG-ים כאלה. למה זה עדיף על cron job שמריץ סקריפט?

- **ניהול תלויות מפורש:** Airflow יודע שאסור לו להתחיל לאמן מודל לפני שהדאטה התרענן. ב-cron, היית צריך להשתמש בטריקים כמו `sleep` ולקוות לטוב.
    
- **הרצה חוזרת ו-Backfills:** נניח שהייתה תקלה ביום שלישי ואנחנו רוצים להריץ מחדש את הפייפליין רק עבור אותו יום. ב-Airflow זה קליק אחד. ב-cron זה סיוט של הרצות ידניות.
    
- **ניטור והתראות:** Airflow נותן לך UI שמראה בדיוק איזה שלב נכשל, מה היו הלוגים, ושולח התראה ל-Slack. Cron שותק כשמשהו נכשל.
    
- **רובסטיות:** Airflow תומך ב-retries אוטומטיים. אם משימה נכשלת בגלל בעיה רגעית ברשת, הוא ינסה שוב לבד.
    

בקיצור, cron טוב להרצת סקריפט בודד. Airflow טוב לניהול תהליכי דאטה אמיתיים בפרודקשן.

#### ש: דיברנו על אתגר ה-real-time. מהן בעיות הסקיילביליות של המערכת הזאת באופן כללי?

הארכיטקטורה הזאת עושה trade-off מודע. חשוב להבין איפה היא חזקה ואיפה צוואר הבקבוק.

- **החלק הסקיילבילי (שירות ה-API):** הגשת ההמלצות היא **סופר סקיילבילית**. ה-API הוא stateless, וכל מה שהוא עושה זה `SELECT` מהיר מטבלה שכבר חושבה מראש. אפשר להוסיף עוד ועוד קונטיינרים של ה-API מאחורי Load Balancer והמערכת תעמוד בעומס כמעט אינסופי של קריאות.
    
- **צוואר הבקבוק (תהליך ה-Batch):** החלק הלא-סקיילבילי הוא תהליך האימון וחישוב ההמלצות מראש.
    
    1. **זמן אימון:** ככל שכמות הדאטה (יוזרים, סרטים, דירוגים) גדלה, זמן אימון המודל יתארך. בשלב מסוים, ריצה יומית עלולה לקחת יותר מ-24 שעות, ואז המודל שלנו מפסיק להיות מעודכן.
        
    2. **עומס חישוב:** חישוב המלצות מראש _לכל היוזרים_ הופך להיות משימה כבדה מאוד. אם יש לך 10 מיליון יוזרים, גם אם אתה מחשב רק 500 מועמדים לכל אחד, זה עדיין 5 מיליארד חיזויים שצריך להריץ כל יום. זה דורש מכונה חזקה ויקרה.
        

הפתרון לבעיות הסקיילביליות האלה הוא בדרך כלל לעבור למודל היברידי (כמו שהזכרנו קודם), שבו החלק הכבד נשאר ב-batch, אבל הוא מייצר תוצרי ביניים (כמו וקטורים של יוזרים/סרטים) שמאפשרים לחלק ה-real time להיות קליל ויעיל.

#### ש: מכל המדדים הטכניים (דיוק, latency, מודולריות), על מה הכי חשוב להתמקד?

אין מדד אחד, אלא יש היררכיה של מדדים שכל אחד חשוב בשלב אחר. המפתח הוא להפריד ביניהם.

1. **המדד הטכני המרכזי לאיכות המודל (Offline):** **NDCG@10**. זה הכוכב הצפוני שלנו בזמן מחקר ופיתוח. כל שינוי שאנחנו עושים במודל, בפיצ'רים או בהיפר-פרמטרים, נמדד בסופו של דבר לפי השאלה "האם זה שיפר את ה-NDCG?". המטרה היא למקסם את המדד הזה.
    
2. **המדד הטכני המרכזי לביצועי המערכת (Online):** **p99 Latency**. לא משנה כמה המודל שלנו גאוני, אם ל-API לוקח חצי שנייה להחזיר המלצות, החוויה נהרסת והיוזר נוטש. אנחנו נגדיר SLA (Service-Level Agreement) קשוח, למשל "99% מהבקשות צריכות לחזור בפחות מ-100 מיליסניות". זה המדד שה-On-call יהיה אחראי עליו.
    
3. **העיקרון הארכיטקטוני המוביל:** **מודולריות והפרדת אחריויות**. זה לא מדד שאפשר לצייר על גרף, אלא הפילוסופיה שמאפשרת לנו בכלל לייצר ולשפר את שני המדדים הקודמים. בזכות הארכיטקטורה המודולרית:
    
    - צוות הדאטה יכול לשפר את ה-Materialized View בלי לשבור את סקריפט ה-ML.
        
    - צוות ה-ML יכול לאמן מודל חדש ומורכב בלי להשפיע על ה-Latency של ה-API.
        
    - צוות ה-Backend יכול לעשות אופטימיזציה ל-API בלי לדעת כלום על Factorization Machines.
        

**לסיכום:** אנחנו מפתחים לפי **NDCG**, מפעילים את המערכת לפי **Latency**, ומתכננים אותה לפי **מודולריות**.