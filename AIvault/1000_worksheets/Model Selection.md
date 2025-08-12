Leave-One-Out cross-validator:
- Provides train/test indices to split data in train/test sets. 
- Each sample is used once as a test set (singleton) while the remaining samples form the training set.

Leave-P-Out cross-validator:
- Provides train/test indices to split data in train/test sets. 
- This results in testing on all distinct samples of size p, while the remaining n - p samples form the training set in each iteration.

Leave P Group(s) Out cross-validator:
- Provides train/test indices to split data according to a third-party provided group. 
- This group information can be used to encode arbitrary domain specific stratifications of the samples as integers.
- For instance the groups could be the year of collection of the samples and thus allow for cross-validation against time-based splits.- 