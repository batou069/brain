| True Class | Classifier 1 | Outcome | Classifier 2 | Outcome | Classifier 3 | Outcome |
| ---------- | ------------ | ------- | ------------ | ------- | ------------ | ------- |
| 0          | 0.28         | TN      | 0.12         | TN      | 0.93         | FP      |
| 0          | 0.27         | TN      | 0.28         | TN      | 0.49         | TN      |
| 0          | 0.65         | FP      | 0.41         | TN      | 0.75         | FP      |
| 0          | 0.53         | FP      | 0.54         | FP      | 1            | FP      |
| 0          | 0.55         | FP      | 0.66         | FP      | 0.98         | FP      |
| 0          | 0.82         | FP      | 0.75         | FP      | 0.93         | FP      |
| 0          | 0.75         | FP      | 0.85         | FP      | 0.5          | FP      |
| 1          | 0.06         | FN      | 0.94         | TP      | 0.96         | TP      |
| 1          | 0.05         | FN      | 0.95         | TP      | 0.04         | FN      |
| 1          | 0.21         | FN      | 0.95         | TP      | 0.56         | TP      |

1) TP=0, FP=5, TN=2, FN=3 => TPR=0, FPR=5/7
2) TP=3, FP=4, TN=3, FN=0 => TPR=1/2, FPR=4/7
3) TP=2, FP=6, TN=1, FN=1 => TPR=2/3, FPR=6/7

True Positive Rate (TPR): $\text{TPR} = \frac{\text{TP}}{\text{TP} + \text{FN}}$ (Sensitivity)
False Positive Rate (FPR): $\text{FPR} = \frac{\text{FP}}{\text{FP} + \text{TN}}$

Plot TPR vs. FPR to form the ROC curve.

3. Maximum Precision

Precision: $\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}$
For each threshold $ t \in [0, 1] $:

Convert probabilities to binary predictions: if probability ≥ $ t $, predict 1; else, predict 0.
Compute precision for the resulting confusion matrix.


Maximum Precision: Take the highest precision value across all thresholds.
Note: Precision is undefined (or set to 0) if $\text{TP} + \text{FP} = 0$.
Outcome
4. Maximum F1 Score

F1 Score: $\text{F1} = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}$
For each threshold $ t $:

Compute precision (as above) and recall ($\text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}$).
Calculate the F1 score.


Maximum F1 Score: Take the highest F1 score across all thresholds.
Note: F1 is undefined (or set to 0) if $\text{Precision} + \text{Recall} = 0$.

Practical Implementation
Using Python with scikit-learn:
python