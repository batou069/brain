---
tags:
  - data_science
  - machine_learning
  - recommender_systems
  - concept_drift
  - mlops
  - concept
aliases:
  - Model Drift
  - Data Drift
related:
  - "[[_Collaborative_Filtering_MOC]]"
  - "[[Online_Learning]]"
worksheet:
  - WS_Collaborative_Filtering_1
date_created: 2025-08-13
---
# Concept Drift in Recommender Systems

## Definition
**Concept Drift** is a phenomenon where the statistical properties of the target variable, which the model is trying to predict, change over time in unforeseen ways. In the context of recommender systems, this means that the underlying patterns of user preferences and item popularity are not static; they evolve.

A model trained on historical data may become less accurate over time because the relationships it learned are no longer representative of the current reality. This degradation of model performance over time is a key challenge in maintaining production machine learning systems (MLOps).

## Types of Drift in Recommenders
- **Changing User Preferences:**
    - A user's tastes can change. Someone who exclusively watched comedies might develop an interest in documentaries.
    - Seasonal effects: Users watch more holiday movies in December.
    - Short-term trends: A movie or genre might become temporarily popular due to a viral meme or social media event.
- **Changing Item Properties:**
    - The relevance of an item can change. A news article is highly relevant when it's published but quickly becomes outdated.
    - The context of an item can change. A movie might gain a new audience or interpretation years after its release.
- **Changing User Population:**
    - The user base of a service can evolve. A platform that initially attracted a niche audience might go mainstream, changing the overall distribution of preferences.

## Detecting Concept Drift
- **Monitoring Model Performance:** The most direct way is to continuously monitor the performance of the live recommendation model on new data. A sustained drop in key metrics like [[Normalized_Discounted_Cumulative_Gain_NDCG|NDCG]], [[Mean_Reciprocal_Rank_MRR|MRR]], or click-through rate is a strong indicator of drift.
- **Monitoring Data Distributions:** Track the statistical properties of input features and model outputs over time.
    - **Item Popularity:** A sudden shift in the most popular items can indicate a trend change.
    - **User Activity:** Changes in the average number of ratings per user or the distribution of rating values.
    - **Latent Factor Distributions:** Drastic changes in the distribution of the learned [[Latent_Factors|latent vectors]] can also signal drift.

## Handling Concept Drift

>[!question] How would you decide on the retraining schedule for your model?
>
>Deciding on a retraining schedule is a critical MLOps task that involves balancing model accuracy, computational cost, and engineering complexity. There is no one-size-fits-all answer.
>
>[list2tab|#Retraining Strategies]
>- Periodic Retraining
>    - **Strategy:** Retrain the model on a fixed schedule (e.g., daily, weekly, monthly).
>    - **Pros:** Simple to implement and automate. Predictable computational load.
>    - **Cons:** Can be inefficient. It might retrain unnecessarily if no drift has occurred, or it might be too slow to react to rapid changes in trends.
>    - **Decision Criteria:** Choose this for systems where user preferences change at a predictable pace (e.g., fashion retail with seasonal changes) and where the cost of being slightly out-of-date is low. The schedule (daily vs. weekly) is determined by business needs and observing how quickly performance degrades.
>- Trigger-Based Retraining
>    - **Strategy:** Retrain the model only when a significant concept drift is detected.
>    - **Pros:** More efficient, as it avoids unnecessary retraining. Ensures the model is updated when needed.
>    - **Cons:** Requires a robust monitoring system to detect drift accurately. Defining the "significant drop" threshold can be tricky.
>    - **Decision Criteria:** This is a more advanced and efficient approach. You would implement this if you have a mature MLOps platform capable of monitoring key metrics in near-real-time and automatically triggering a retraining pipeline when performance drops below a pre-defined threshold (e.g., if NDCG@10 drops by 5% and stays there for 24 hours).
>- Online Learning
>    - **Strategy:** Update the model incrementally as new data arrives, without full retraining.
>    - **Pros:** The model is always up-to-date and can adapt to changes very quickly.
>    - **Cons:** More complex to implement. Not all algorithms support online updates easily ([[Stochastic_Gradient_Descent_SGD_for_CF|SGD]] is more suitable than [[Alternating_Least_Squares_ALS|ALS]] for this). Can be susceptible to noise or short-term fads.
>    - **Decision Criteria:** Use this for highly dynamic environments where trends change very rapidly (e.g., news recommendations, social media feeds).
>
>**Practical Approach:** A common strategy is a hybrid one:
>1.  **Periodic Batch Retraining:** Perform a full retraining on all available data on a regular schedule (e.g., weekly) to capture broad patterns.
>2.  **Online/Incremental Updates:** Use a faster, incremental update process (e.g., daily or hourly) to incorporate the latest user interactions and keep the model fresh between full retraining cycles.
>3.  **Monitoring and Alarms:** Overlay this with a monitoring system that can trigger an emergency retraining if a sudden, severe drift is detected.

---