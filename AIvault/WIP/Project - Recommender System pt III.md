candidate generation followed by ranking

# Chosen Architecture
Candidates:
- [A Dual Augmented Two-tower Model for Online Large-scale Recommendation (Meituan)](https://dlp-kdd.github.io/assets/pdf/DLP-KDD_2021_paper_4.pdf)
- [Mixed Negative Sampling for Learning Two-tower Neural Networks in Recommendations (Google)](https://storage.googleapis.com/gweb-research2023-media/pubtools/6090.pdf)
- [Building a Two Tower Recommendation System with RedisVL (Redis)](https://redis.io/learn/building-a-two-tower-recommendation-system-with-redis-vl)
- [Learning Deep Structured Semantic Models for Web Search using Clickthrough Data (Microsoft)](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/cikm2013_DSSM_fullversion.pdf)



# cloud.zilliz.com
user: db_db78c6e2703d3e1
pwd: Zt2+]8h2S{b}F7;u

# Vector DB

|             | FAISS                                                                                                                                                                                                                                                                  | Milvus (via pymilvus)                                                                                                                                                                                                                                                               | RedisVL                                                                                                                                                                                                                      |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| What is it? | A C++ library with Python bindings that contains the core, high-performance ANN algorithms.                                                                                                                                                                            | A full-featured, standalone vector database system built for production. It often uses FAISS internally.                                                                                                                                                                            | A module for Redis that adds vector search capabilities to the popular in-memory key-value store.                                                                                                                            |
| Pros        | - Maximum Performance: The fastest option if you build a service around it.<br>- Total Control: Huge variety of indexing algorithms to precisely tune the speed/accuracy/memory trade-off.<br>- GPU Support: Can use GPUs to accelerate search by orders of magnitude. | -Production Ready: It's a complete, scalable, and reliable service.<br>- Easy API: pymilvus provides a simple, high-level API for managing and searching vectors.<br>- Dynamic & Hybrid: Easily add/delete vectors and filter results based on other metadata (e.g., genre, price). | -Convenient: If you already use Redis, adding vector search is simple.<br>- Unified Store: Store vector embeddings and item metadata together in one place.<br>- Real-time: Also supports dynamic data and hybrid filtering. |
| Cons        | - It's a Library, Not a Service: You have to write your own server, manage data persistence, and handle scaling.<br>- Complex: The number of options can be overwhelming.                                                                                              | - More Infrastructure: It's a distributed system with its own components that need to be managed.<br>- Less Low-Level Control: Abstracts away some of the finer details that FAISS exposes.                                                                                         | - Newer: Vector search is a newer feature for Redis compared to databases built from the ground up for it.<br>- In-Memory Focus: Primarily designed as an in-memory system, which can affect cost at massive scale.          |
| Use When... | You are building a custom, high-performance vector search service from scratch and need maximum control.                                                                                                                                                               | You need a scalable, production-grade, "turn-key" solution for vector search and want to get started quickly.                                                                                                                                                                       | You already have a Redis-based infrastructure and want to add vector search capabilities without deploying a new database.                                                                                                   |
# Diagrams



```mermaid
graph TD
    subgraph User Tower
        direction LR
        subgraph Input Layer
            U_ID[User ID]
            U_Sex[Sex]
            U_Age[Age]
            U_Occ[Occupation]
        end
        subgraph Embedding Layer
            direction LR
            E_UID[("Embedding(vocab, 32)")]
            E_Sex[("Embedding(vocab, 8)")]
            E_Age[("Embedding(vocab, 8)")]
            E_Occ[("Embedding(vocab, 16)")]
        end
        subgraph MLP
            direction TB
            MLP_Concat(Concatenate)
            MLP_L1(Linear_64_128) --> MLP_A1(ReLU) --> MLP_D1(Dropout)
            MLP_D1 --> MLP_L2(Linear_128_64) --> MLP_A2(ReLU) --> MLP_D2(Dropout)
            MLP_D2 --> MLP_L3(Linear_64_32)
        end
        subgraph Output
            direction LR
            User_Emb(User Embedding_32)
            L2_Norm((L2 Norm))
        end
        U_ID --> E_UID
        U_Sex --> E_Sex
        U_Age --> E_Age
        U_Occ --> E_Occ
        E_UID -->|"dim: 32"| MLP_Concat
        E_Sex -->|"dim: 8"| MLP_Concat
        E_Age -->|"dim: 8"| MLP_Concat
        E_Occ -->|"dim: 16"| MLP_Concat
        MLP_Concat -->|"dim: 64"| MLP_L1
        MLP_L3 --> L2_Norm
        L2_Norm --> User_Emb
    end
```



```mermaid
graph TD
    subgraph Item Tower
        direction LR
        subgraph Input Layer
            I_ID[Movie ID]
            I_Genres[Genres Multi-hot]
            I_Year[Release Year]
        end
        subgraph Embedding Layer
            direction LR
            E_IID[("Embedding(vocab, 32)")]
            E_Genres[("Linear(vocab, 32)")]
            E_Year[("Embedding(vocab, 8)")]
        end
        subgraph MLP
            direction TB
            MLP_Concat(Concatenate)
            MLP_L1(Linear_72_128) --> MLP_A1(ReLU) --> MLP_D1(Dropout)
            MLP_D1 --> MLP_L2(Linear_128_64) --> MLP_A2(ReLU) --> MLP_D2(Dropout)
            MLP_D2 --> MLP_L3(Linear_64_32)
        end
        subgraph Output
            direction LR
            Item_Emb(Item Embedding_32_)
            L2_Norm((L2 Norm))
        end
        I_ID --> E_IID
        I_Genres --> E_Genres
        I_Year --> E_Year
        E_IID -->|"dim: 32"| MLP_Concat
        E_Genres -->|"dim: 32"| MLP_Concat
        E_Year -->|"dim: 8"| MLP_Concat
        MLP_Concat -->|"dim: 72"| MLP_L1
        MLP_L3 --> L2_Norm
        L2_Norm --> Item_Emb
    end
```

```mermaid
graph TD
    subgraph Training
        direction TB
        U_Features[User Features] --> User_Tower
        Pos_Item[Positive Item Features] --> Item_Tower
        Neg_Item[Negative Item Features] --> Item_Tower
        subgraph Model
            User_Tower(User Tower)
            Item_Tower(Item Tower)
        end
        User_Tower --> Anchor_Emb(Anchor Embedding)
        Item_Tower --"Positive"--> Pos_Emb(Positive Embedding)
        Item_Tower --"Negative"--> Neg_Emb(Negative Embedding)
        Ratings[Ratings Positive & Negative] --> Loss
        Anchor_Emb --> Loss(Dynamic Margin Loss)
        Pos_Emb --> Loss
        Neg_Emb --> Loss
    end
    subgraph Inference
        direction TB
        U_Features_Inf[User Features] --> User_Tower_Inf(User Tower)
        Candidate_Items[Candidate Item Features] --> Item_Tower_Inf(Item Tower)
        User_Tower_Inf --> User_Emb_Inf(User Embedding)
        Item_Tower_Inf --> Item_Emb_Inf(Item Embeddings)
        User_Emb_Inf --> Cosine((Cosine Similarity))
        Item_Emb_Inf --> Cosine
        Cosine --> Scores[Ranked Scores]
    end
```
