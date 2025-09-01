---
tags:
  - article
  - ensemble_methods
  - boosting
  - gradient_boosting
  - adaboost
---
# Tree-based ensemble algorithms

**Ensemble algorithms and particularly those that utilize decision trees as weak learners have multiple advantages compared to other algorithms:**

> _Their algorithms are easy to understand and visualize: describing and sketching a decision tree is arguably easier than describing Support Vector Machines_
> 
> _They are non-parametric and don’t assume or require the data to follow a particular distribution: this will save you time transforming data to be normally distributed_
> 
> _They can handle mixed data types: categorical variables do not necessarily have to be one hot encoded_
> 
> _Multi-collinearity of features does not affect the accuracy and prediction performance of the model: features do not need to be removed or otherwise engineered to decrease the correlations and interactions between them_
> 
> _They are robust against overfitting: because they use many weak learners that underfit (high bias) and combine those predictions into a stronger learner, they reduce the overfitting (variance) of the model_
> 
> _They are relatively robust against outliers and noise: in general, they will handle noisy data (e.g. features with no effect on the target) or outliers (e.g. extreme values) well with little effect on the overall performance_
> 
> _Inputs do not need to be scaled: preprocessing and transforming the features with MinMaxScaler or StandardScaler are not necessary_
> 
> _They are computationally relatively inexpensive: compared to algorithms such as Support Vector Machines or neural networks they are faster_
> 
> _They usually perform much better than their weak learners: decision trees will be less accurate due to their high variance/overfitting compared with boosting and bagging algorithms_

# Boosting

_The general idea of Boosting just as well any other ensemble algorithm is to combine several weak learners into a stronger one. A weak learner refers to a learning algorithm that only predicts slightly better than randomly. The baseline of Boosting algorithms is to try predictors sequentially, where each subsequent model attempts to fix the errors of its predecessor._

**_That means:_**

> _The trees are grown sequentially_
> 
> _Each tree is grown using information from previously grown trees_
> 
> _It does not involve bootstrap sampling as in bagging_
> 
> _Family of weak learners should have a minimum correlation between them_

Zoom image will be displayed

![](https://miro.medium.com/v2/resize:fit:700/1*mbMYeMtEEL-gQ3AqB3hXTg.png)

Boosting Process

## Few important controlling parameters in Boosting with Decision Trees

> **_The number of trees B_** _— Unlike bagging and random forests, boosting can overfit if B is too large, although this overfitting tends to occur slowly if at all. We use cross-validation to select B._
> 
> **_The number d of splits in each tree_** _— It controls the complexity of the boosted ensemble. Often d = 1 works well, in which case each tree is a stump, consisting of a single split. In boosting, because the growth of a particular tree takes into account the other trees that have already been grown, smaller trees are typically sufficient._

## Types of Boosting Algorithms

_The two main boosting algorithms are Adaptive Boosting and Gradient Boosting. XGBoot, LightGBM and CatBoost are basically different implementations of Gradient Boosting._

# Adaptive Boosting

_Adaptive Boosting, or most commonly known AdaBoost, algorithm was first introduced by Freund & Schapire in 1995. It is sequentially growing decision trees as weak learners and_ ==_punishing the incorrectly predicted samples by assigning a larger weight to them after each round of prediction_==_. This way, the algorithm is learning from previous mistakes. The final prediction is the weighted majority vote (or weighted median in case of regression problems)_

> _After training a classifier at any level,_ **_ada-boost assigns weight to each training item._** _Misclassified item is assigned higher weight so that it appears in the training subset of next classifier with higher probability._
> 
> _After each classifier is trained,_ **_a weight is assigned to the classifier_** _as well based on accuracy. More accurate classifier is assigned higher weight so that it will have more impact in final outcome._

Zoom image will be displayed

![](https://miro.medium.com/v2/resize:fit:700/1*1OFxuHyf4mrzpGGZAhVmEg.png)

AdaBoosting

## Algorithm steps

Initialize the weights of samples for the first round as w = 1/m, where m is the number of samples)

**For t in T rounds:**

> **_Step 1.)_** _Grow a weak learner (decision tree stump) using the distribution p that does the best job classifying the collection of samples; return hypothesis h with prediction values for each example in the data_
> 
> **_Step 2.)_** _Calculate Total Error and Amount of say (classifier weights)_
> 
> **_Step 3.)_** _Calculate Beta_
> 
> **_Step 4.)_** _Update the weight vector of the samples to w = w*Beta so that predictions with poor performance will have higher a weight and predictions with better performance will have a lower weight_
> 
> **_Step 5.)_** _Calculate distribution p by normalizing the weight vector w_

**Consider an example of 10 Samples, initial weight for each sample will be 1/10= 0.1**

## Step 1.)

Weak Learner — Decision tree stump is build with the feature for which Gini index is the lowest

> _Calculate the_ **_Gini score_** _for sub-nodes, using formula sum of squares of probability for success(i.e. “Correct”) and failure(i.e. “Incorrect”)_ **_(p² +q²)_**
> 
> _Calculate the_ **_Gini Index_** _for a split, using_ **_(1- weighted Gini score of each node of that split)_**_._

10 Samples -

**Feature 1 —** left node — 4 correct, 2 incorrect, right node —3 correct, 1 incorrect

![](https://miro.medium.com/v2/resize:fit:577/1*YSD_xIbbxpLZSr50OK1IMg.png)

Gini for left node = ((4/6)_(4/6))+((2/6)_(2/6))=0.55. Gini for right node = ((3/4)_(3/4))+((1/4)_(1/4)) = 0.625 Weighted Gini Index for feature 1 =1- ((6/10)_0.55+(4/10)_0.625) = 0.42

**Feature 2** — left node —4 correct, 0 incorrect, right node — 4 correct, 2 incorrect.

![](https://miro.medium.com/v2/resize:fit:599/1*OzyfVhUZ9_jvasTNa_ZpsQ.png)

Weighted Gini Index for feature 2 = 0.27

So decision stump will be made with feature 2 as the gini index for feature 2 is the lowest.

## Step 2

**Total Error**

The Total Error for a stump is the **sum of the weights associated with the incorrectly classified samples.**

**10 Samples:** **Feature 2** — left node — 4 correct, 0 incorrect, right node — 4 correct, 2 incorrect.

Total Error for stump with feature 2 :- It made 2 errors i.e `2*1/10=0.2`.

Note:- Because all the sample’s weight is added up to 1, Total Error will always be between 0 and 1. **0 indicates perfect stump, 1 indicates horrible stump.**

Amount of Say

**1/2 * ln((1- total error)/total error)**

With learning rate introduced, Amount of say will be -> learning_rate multiply `( 1/2 * ln((1- total error)/total error))`

Amount of say for stump with feature 2 is `[1/2 ln(4)] = 0.69`.

## Step 3

**Calculate Beta**

For **incorrectly** classified samples -> Beta = **exp(Amount of say)**

For **correctly** classified samples -> Beta = **exp(-Amount of say)**

## Step 4

**Updating Weights**

New Sample Weight = **Sample Weight * Beta**

There are two misclassified samples, Here sample weight of both sample is 0.1 and the amount of say is 0.69. New Sample Weight for both sample = 0.1 * exp(0.69) = 0.1 (1.99) = 0.2

There are eight correctly classified samples, Here sample weight of all theses samples is 1/10 and the amount of say is 0.69 New Sample Weight = 0.1 * exp(-0.69) = 0.1(0.5) = 0.05 for all the 8 samples

## Step 5

**Normalizing weights and Creating new distribution**

If we add up the New Sample Weights, **2*0.2 + 8*(0.05)= 0.8.** So we divide each sample weight with 0.8 to get the normalized values. Now we consider Normalized Weights as New Sample Weights

New weights will be — 0.06, 0.06, 0.06, **0.25**, 0.06, 0.06, **0.25**, 0.06

Hence the weights of misclassified samples is increased from 0.1 to 0.25 so that they have more chance of being selected multiple times in the next iteration. Before building the next stump, we need to create a new dataset. Here we pick random numbers between 0 and 1 and select the samples for next iteration, here we use sample weights like a distribution.

## Output

Imagine there are 4 stumps ( Trees ) are created by the AdaBoost algorithm. Out of 4 stumps, 2 stumps are classified the test sample as as category 1, and the other 2 stumps classified the test sample as category 2.

These are the Amount of Say for these stumps are 0.69+0.6 = 1.29, and the Amount of Say of the other 2 stumps are 0.41+0.82=1.23.

Ultimately, **category 1** **will be the output because of the larger Amount of Say(1.29).**

# Pros of AdaBoost:

- Relatively robust to overfitting in low noise datasets
- AdaBoost has only a few hyperparameters that need to be tuned to improve model performance
- Easy to understand and to visualize

# Cons of AdaBoost:

- The drawback of AdaBoost is that it is easily defeated by noisy data, the efficiency of the algorithm is highly affected by outliers as the algorithm tries to fit every point perfectly.
- Compared to random forests and XGBoost, AdaBoost performs worse when irrelevant features are included
- AdaBoost is not optimized for speed

```python
from sklearn.ensemble import AdaBoostClassifier  
from sklearn import datasets  
from sklearn.model_selection import train_test_split  
from sklearn import metricsiris = datasets.load_iris()  
X = iris.data  
y = iris.target  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)abc = AdaBoostClassifier(n_estimators=50,learning_rate=1)  
# Train Adaboost Classifer  
model = abc.fit(X_train, y_train)#Predict the response for test dataset  
y_pred = model.predict(X_test)print(“Accuracy:”,metrics.accuracy_score(y_test, y_pred))  
# Accuracy: 0.9210526315789473abc.feature_importances_  
# array([0.  , 0.  , 0.46, 0.54])
```

## Using Different Base Learners

```python
from sklearn.svm import SVC  
svc=SVC(probability=True, kernel='linear')  
abc =AdaBoostClassifier(n_estimators=50, base_estimator=svc,learning_rate=1)model = abc.fit(X_train, y_train)  
y_pred = model.predict(X_test)  
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))  
#Accuracy: 0.9473684210526315
```

## Hyper-parameters

**base_estimators:** specifies the base type estimator, i.e. the algorithm to be used as base learner. default = DecisionTreeClassifier(max_depth=1).

**n_estimators:** The maximum number of estimators at which boosting is terminated. default = 50

**learning_rate:** Learning rate shrinks the contribution of each classifier by learning_rate. There is a trade-off between learning_rate and n_estimators. default=1.

**random_state:** makes the model’s output replicable. default=None

**loss:** It is only for regressor.The loss function to use when updating the weights after each boosting iteration. {‘linear’, ‘square’, ‘exponential’}, default=’linear’

# Gradient Boosting

_As the name suggests, Gradient Boosting means Gradient Descent + Boosting. This is another very popular Boosting algorithm whose work basis is just like what we’ve seen for AdaBoost.The difference lies in what it does with the underfitted values of its predecessor. Contrary to AdaBoost, which tweaks the instance weights at every interaction, this method tries to_ **_fit the new predictor to the residual errors made by the previous predictor_**_._

Gradient boosting re-defines boosting as a numerical optimization problem where the objective is to **minimize the loss function** of the model by adding weak learners using a **gradient-descent like procedure**.

As gradient boosting is based on minimizing a loss function, different types of loss functions can be used resulting in a flexible technique that can be applied to **regression, multi-class classification, etc.**

## Cost optimization

This algorithm optimize a cost function over function space by iteratively choosing a function (weak hypothesis) that points in the negative gradient direction.

**Input Data:** Consider the below 10 samples as input

![](https://miro.medium.com/v2/resize:fit:364/1*clB_T7rORfZ5v_PrWZbqcw.png)

**Step 1.** F0(x) (initial estimator) gives the predictions from the first stage of our model with x as input and y as output.

Calculate the residuals i.e. error (y-F0(x)).

Zoom image will be displayed

![](https://miro.medium.com/v2/resize:fit:700/1*Udz9SXvz9QaEMEeBG9-0jQ.png)

**Step 2.** We can use the residuals from F0(x) to create h1(x). h1(x) will be a regression tree which will try and reduce the residuals from the previous step. The output of h1(x) won’t be a prediction of y; instead, it will help in predicting the successive function F1(x) which will bring down the residuals.

![](https://miro.medium.com/v2/resize:fit:385/1*AFOyhdlSAOBbYeklVF1ObQ.png)

Zoom image will be displayed

![](https://miro.medium.com/v2/resize:fit:699/1*IPKn1TXD6FgpZ6Lh5UMSsA.png)

The additive model h1(x) computes the mean of the residuals (y — F0) at each leaf of the tree. The boosted function F1(x) is obtained by summing F0(x) and h1(x). This way h1(x) learns from the residuals of F0(x) and suppresses it in F1(x).

**Step 3.** Residuals from the boosted output i.e (y-F1(x)) will be used to create next tree h2(x) and the boosted output will be F2(x) obtained by summing F1(x) and h2(x).

**This process is repeated until the error function does not change, or the maximum limit of the number of estimators is reached.**

In General, we can say that:

![](https://miro.medium.com/v2/resize:fit:258/1*Ahvo0sDlpA_wWQPkQlFn0A.png)

Or, equivalently

Zoom image will be displayed

![](https://miro.medium.com/v2/resize:fit:168/1*MvuiZy0EroII5rfBfly_Lw.png)

![](https://miro.medium.com/v2/resize:fit:220/1*HNeJTzwlN89uoBZ23Hjw_Q.png)

Hence the residuals for a given model are the negative gradients of the [mean squared error (MSE)](https://en.wikipedia.org/wiki/Mean_squared_error) loss function and the process is similar to the process of the gradient descent algorithm.

**Gradient boosting does not modify the sample distribution as weak learners train on the remaining residual errors of a strong learner (i.e, pseudo-residuals).**

```
from sklearn.ensemble import GradientBoostingClassifier  
clf = GradientBoostingClassifier()clf.fit(X_train,y_train)  
y_pred = clf.predict(X_test)  
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))  
#Accuracy: 0.9210526315789473
```

## Hyper-parameters

**loss:** {‘deviance’, ‘exponential’}, default=’deviance’ loss function to be optimized. ‘deviance’ refers to deviance (= logistic regression) for classification with probabilistic outputs. For loss ‘exponential’ gradient boosting recovers the AdaBoost algorithm.

**learning_rate:** float, default=0.1 learning rate shrinks the contribution of each tree by learning_rate. There is a trade-off between learning_rate and n_estimators.

**n_estimators:** int, default=100 The number of boosting stages to perform. Gradient boosting is fairly robust to over-fitting so a large number usually results in better performance.

**subsample:** float, default=1.0 The fraction of samples to be used for fitting the individual base learners.

**criterion:** {‘friedman_mse’, ‘mse’, ‘mae’}, default=’friedman_mse’ The function to measure the quality of a split.

**min_samples_split:** int or float, default=2 The minimum number of samples required to split an internal node.

If int, then consider min_samples_split as the minimum number.

If float, then min_samples_split is a fraction and ceil(min_samples_split * n_samples) are the minimum number of samples for each split.

**min_samples_leaf:** int or float, default=1 The minimum number of samples required to be at a leaf node.

**max_depth:** int, default=3 maximum depth of the individual regression estimators.

**min_impurity_decrease:** float, default=0.0 A node will be split if this split induces a decrease of the impurity greater than or equal to this value.

**init:** estimator or ‘zero’, default=None An estimator object that is used to compute the initial predictions. init has to provide fit and predict_proba. If ‘zero’, the initial raw predictions are set to zero. By default, a DummyEstimator predicting the classes priors is used.

**max_features:** {‘auto’, ‘sqrt’, ‘log2’}, int or float, default=None The number of features to consider when looking for the best split:

If int, then consider max_features features at each split.

If float, then max_features is a fraction and int(max_features * n_features) features are considered at each split.

If ‘auto’, then max_features=sqrt(n_features).

If ‘sqrt’, then max_features=sqrt(n_features).

If ‘log2’, then max_features=log2(n_features).

If None, then max_features=n_features.

**Choosing max_features < n_features leads to a reduction of variance and an increase in bias.**

# XGBoost

_Extreme Gradient Boosting is an advanced implementation of the Gradient Boosting. This algorithm is designed to “push the extreme of the computation limits of machines to provide a scalable , portable and accurate library.”. Moreover, It includes a variety of regularization which reduces overfitting and improves overall performance._

**Parallel Processing**

Xgboost doesn’t run multiple trees in parallel like you noted, you need predictions after each tree to update gradients.

The parallelisation happens during the construction of each trees, at a very low level. Each independent branches of the tree are trained separately.

## Finding Best Split

The key challenge in training a GBDT is the process of finding the best split for each leaf. When naively done, this step requires the algorithm to go through every feature of every data point. The computational complexity is thus O(n{data}n{features}).

**Histogram-based methods** Often, small changes in the split don’t make much of a difference in the performance of the tree. Histogram-based methods take advantage of this fact by grouping features into a set of bins and perform splitting on the bins instead of the features. This is equivalent to sub-sampling the number of splits that the model evaluates. Since the features can be binned before building each tree, this method can greatly speed up training, reducing the computational complexity to O(n{data}n{bins}).

## Pros of XGB:

- Regularized Gradient Boosting with both L1 and L2 regularization.
- Implements parallel processing being much faster than GB.
- Allows users to define custom optimisation objectives and evaluation criteria adding a whole new dimension to the model.
- Has an in-built routine to handle missing values.
- Makes splits up to the max_depth specified and then starts pruning the tree backwards and removes splits beyond which there is no positive gain.
- Allows a user to run a cross-validation at each iteration of the boosting process and thus it is easy to get the exact optimum number of boosting iterations in a single run.

## Cons of XGB:

- XGBoost is more difficult to understand, visualize and to tune compared to AdaBoost and random forests. There is a multitude of hyperparameters that can be tuned to increase performance.
- It cannot handle categorical features by itself, it only accepts numerical values similar to Random Forest. Therefore one has to perform various encodings like label encoding, mean encoding or one-hot encoding before supplying categorical data to XGBoost.

```python
# XGBoost  
from xgboost import XGBClassifier  
clf = XGBClassifier()  
clf.fit(X_train,y_train)  
y_pred = clf.predict(X_test)  
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))  
#Accuracy: 0.9210526315789473
```

## Hyper-parameters

**eta:** [default=0.3, alias: learning_rate], range: [0,1]

**gamma:** [default=0, alias: min_split_loss], range: [0,∞]

Minimum loss reduction required to make a further partition on a leaf node of the tree. The larger gamma is, the more conservative the algorithm will be.

**max_depth:** [default=6], range: [0,∞]

Maximum depth of a tree. Increasing this value will make the model more complex and more likely to overfit. Beware that XGBoost aggressively consumes memory when training a deep tree.

**min_child_weight:** [default=1], range: [0,∞]

Minimum sum of instance weight (hessian) needed in a child. If the tree partition step results in a leaf node with the sum of instance weight less than min_child_weight, then the building process will give up further partitioning.

**subsample:** [default=1], range: (0,1]

Subsample ratio of the training instances. Setting it to 0.5 means that XGBoost would randomly sample half of the training data prior to growing trees. and this will prevent overfitting. Subsampling will occur once in every boosting iteration.

**colsample_bytree, colsample_bylevel, colsample_bynode:** [default=1], range of (0, 1]

This is a family of parameters for subsampling of columns.

- **colsample_bytree** is the subsample ratio of columns when constructing **each tree**. Subsampling occurs once for every tree constructed.
- **colsample_bylevel** is the subsample ratio of columns for each level. Subsampling occurs once for **every new depth level** reached in a tree. Columns are subsampled from the set of columns chosen for the current tree.
- **colsample_bynode** is the subsample ratio of columns for **each node (split)**. Subsampling occurs once every time a new split is evaluated. Columns are subsampled from the set of columns chosen for the current level.

_colsample_by parameters work cumulatively. For instance, the combination {‘colsample_bytree’:0.5, ‘colsample_bylevel’:0.5, ‘colsample_bynode’:0.5} with 64 features will leave 8 features to choose from at each split._

**lambda:** [default=1, alias: reg_lambda]

L2 regularization term on weights. Increasing this value will make model more conservative.

**alpha:** [default=0, alias: reg_alpha]

L1 regularization term on weights. Increasing this value will make model more conservative.

**tree_method:** string [default= auto]

The tree construction algorithm used in XGBoost.

- **auto:** Use heuristic to choose the fastest method.
- **exact:** Exact greedy algorithm. Enumerates all split candidates. For small dataset, exact greedy (exact) will be used.
- **approx:** Approximate greedy algorithm using quantile sketch and gradient histogram.
- **hist:** Faster histogram optimized approximate greedy algorithm.
- **gpu_hist:** GPU implementation of hist algorithm.

For larger dataset, approximate algorithm (approx) will be chosen. It’s recommended to try hist and gpu_hist for higher performance with large dataset. (gpu_hist)has support for external memory.

**scale_pos_weight:** [default=1]

Control the balance of positive and negative weights, useful for unbalanced classes. A typical value to consider: sum(negative instances) / sum(positive instances).

**max_bin:** [default=256]

Maximum number of discrete bins to bucket continuous features.Only used if tree_method is set to hist.

Increasing this number improves the optimality of splits at the cost of higher computation time.

**predictor:** [default=`auto`]

The type of predictor algorithm to use. Provides the same results but allows the use of GPU or CPU.

- auto: Configure predictor based on heuristics.
- cpu_predictor: Multicore CPU prediction algorithm.
- gpu_predictor: Prediction using GPU. Used when tree_method is gpu_hist. When predictor is set to default value auto, the gpu_hist tree method is able to provide GPU based prediction without copying training data to GPU memory. If gpu_predictor is explicitly specified, then all data is copied into GPU, only recommended for performing prediction tasks.

# Light GBM

- Uses a novel technique of Gradient-based One-Side Sampling (GOSS) to filter out the data instances for finding a split value
- Can also handle categorical features by taking the input of feature names.
- It does not convert to one-hot coding, and is much faster than one-hot coding (One hot encoding has issues of sparsity and curse of dimensionality).

# Cat Boost

- No need to externally encode categorical variables.
- Use one-hot encoding for all features with number of different values less than or equal to the one_hot_max_size (parameter) value
- If nothing is passed in cat_features argument, CatBoost will treat all the columns as numerical variables.
- Catboost deals with categorical features by, “generating random permutations of the dataset and for each sample computing the average label value for the sample with the same category value placed before the given one in the permutation”.
- They also process the data with GPU acceleration, and do feature discretization into a fixed number of bins (128 and 32).

[

Boosting

](https://medium.com/tag/boosting?source=post_page-----e7d2dbc4e4ca---------------------------------------)

[

Gradient Boosting

](https://medium.com/tag/gradient-boosting?source=post_page-----e7d2dbc4e4ca---------------------------------------)

[

Adaboost

](https://medium.com/tag/adaboost?source=post_page-----e7d2dbc4e4ca---------------------------------------)

[

Xgboost

](https://medium.com/tag/xgboost?source=post_page-----e7d2dbc4e4ca---------------------------------------)

[

Extreme Gradient Boosting

](https://medium.com/tag/extreme-gradient-boosting?source=post_page-----e7d2dbc4e4ca---------------------------------------)

[

![Divya Gera](https://miro.medium.com/v2/resize:fill:96:96/0*CNhn7q41GwLsI5my)



](https://medium.com/@divyagera2402?source=post_page---post_author_info--e7d2dbc4e4ca---------------------------------------)

[

## Written by Divya Gera

](https://medium.com/@divyagera2402?source=post_page---post_author_info--e7d2dbc4e4ca---------------------------------------)

[33 followers](https://medium.com/@divyagera2402/followers?source=post_page---post_author_info--e7d2dbc4e4ca---------------------------------------)

·[6 following](https://medium.com/@divyagera2402/following?source=post_page---post_author_info--e7d2dbc4e4ca---------------------------------------)

Senior Data Scientist at VMware

## No responses yet

[](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page---post_responses--e7d2dbc4e4ca---------------------------------------)

![Laurent Flaster](https://miro.medium.com/v2/resize:fill:32:32/0*HzJwlL0JyTJ7C-rN.)

Laurent Flaster

﻿

## More from Divya Gera

![Encoding Categorical Data and Dummy Variable Trap in Regression](https://miro.medium.com/v2/resize:fit:679/253d1ac7271c0a7cc8f41cd8f9de7fb7148297ef9c17b11e085fd6559557c22b)

[

![Divya Gera](https://miro.medium.com/v2/resize:fill:20:20/0*CNhn7q41GwLsI5my)



](https://medium.com/@divyagera2402?source=post_page---author_recirc--e7d2dbc4e4ca----0---------------------efa8a10a_99ed_44e9_9f78_c3f2c09baefd--------------)

[

Divya Gera

](https://medium.com/@divyagera2402?source=post_page---author_recirc--e7d2dbc4e4ca----0---------------------efa8a10a_99ed_44e9_9f78_c3f2c09baefd--------------)

[

## Encoding Categorical Data and Dummy Variable Trap in Regression

### Today’s world is full of data and data can be either in quantitative (numerical) or qualitative (categorical) form. The statistics or…



](https://medium.com/@divyagera2402/encoding-categorical-data-and-dummy-variable-trap-in-regression-830f728c1382?source=post_page---author_recirc--e7d2dbc4e4ca----0---------------------efa8a10a_99ed_44e9_9f78_c3f2c09baefd--------------)

Jul 5, 2019

[

](https://medium.com/@divyagera2402/encoding-categorical-data-and-dummy-variable-trap-in-regression-830f728c1382?source=post_page---author_recirc--e7d2dbc4e4ca----0---------------------efa8a10a_99ed_44e9_9f78_c3f2c09baefd--------------)

[

33







](https://medium.com/@divyagera2402/encoding-categorical-data-and-dummy-variable-trap-in-regression-830f728c1382?source=post_page---author_recirc--e7d2dbc4e4ca----0---------------------efa8a10a_99ed_44e9_9f78_c3f2c09baefd--------------)

![Data journey from acquisition to feeding it into a model — Steps from Data Cleaning, Handling, EDA…](https://miro.medium.com/v2/resize:fit:679/0*LzsxkTtqkFtq_rSD.jpeg)

[

![Divya Gera](https://miro.medium.com/v2/resize:fill:20:20/0*CNhn7q41GwLsI5my)



](https://medium.com/@divyagera2402?source=post_page---author_recirc--e7d2dbc4e4ca----1---------------------efa8a10a_99ed_44e9_9f78_c3f2c09baefd--------------)

[

Divya Gera

](https://medium.com/@divyagera2402?source=post_page---author_recirc--e7d2dbc4e4ca----1---------------------efa8a10a_99ed_44e9_9f78_c3f2c09baefd--------------)

[

## Data journey from acquisition to feeding it into a model — Steps from Data Cleaning, Handling, EDA…

### I am going to discuss summary of Data journey which starts after acquiring the data till being fed to a model. There are multiple steps…



](https://medium.com/@divyagera2402/data-journey-from-acquiring-it-to-feeding-it-in-a-model-steps-from-data-cleaning-handling-eda-4eacf9d316f1?source=post_page---author_recirc--e7d2dbc4e4ca----1---------------------efa8a10a_99ed_44e9_9f78_c3f2c09baefd--------------)

Jul 19, 2020

[

](https://medium.com/@divyagera2402/data-journey-from-acquiring-it-to-feeding-it-in-a-model-steps-from-data-cleaning-handling-eda-4eacf9d316f1?source=post_page---author_recirc--e7d2dbc4e4ca----1---------------------efa8a10a_99ed_44e9_9f78_c3f2c09baefd--------------)

[

13







](https://medium.com/@divyagera2402/data-journey-from-acquiring-it-to-feeding-it-in-a-model-steps-from-data-cleaning-handling-eda-4eacf9d316f1?source=post_page---author_recirc--e7d2dbc4e4ca----1---------------------efa8a10a_99ed_44e9_9f78_c3f2c09baefd--------------)

![Basic fundaments of Text Extraction from images](https://miro.medium.com/v2/resize:fit:679/253d1ac7271c0a7cc8f41cd8f9de7fb7148297ef9c17b11e085fd6559557c22b)

[

![Divya Gera](https://miro.medium.com/v2/resize:fill:20:20/0*CNhn7q41GwLsI5my)



](https://medium.com/@divyagera2402?source=post_page---author_recirc--e7d2dbc4e4ca----2---------------------efa8a10a_99ed_44e9_9f78_c3f2c09baefd--------------)

[

Divya Gera

](https://medium.com/@divyagera2402?source=post_page---author_recirc--e7d2dbc4e4ca----2---------------------efa8a10a_99ed_44e9_9f78_c3f2c09baefd--------------)

[

## Basic fundaments of Text Extraction from images

### The image content is classified into two categories: perceptual content and semantic content. Perceptual contents include colors, shapes…



](https://medium.com/@divyagera2402/basic-fundaments-of-text-extraction-from-images-548ebe2fb4a5?source=post_page---author_recirc--e7d2dbc4e4ca----2---------------------efa8a10a_99ed_44e9_9f78_c3f2c09baefd--------------)

Oct 14, 2018

[

](https://medium.com/@divyagera2402/basic-fundaments-of-text-extraction-from-images-548ebe2fb4a5?source=post_page---author_recirc--e7d2dbc4e4ca----2---------------------efa8a10a_99ed_44e9_9f78_c3f2c09baefd--------------)

[

16

](https://medium.com/@divyagera2402/basic-fundaments-of-text-extraction-from-images-548ebe2fb4a5?source=post_page---author_recirc--e7d2dbc4e4ca----2---------------------efa8a10a_99ed_44e9_9f78_c3f2c09baefd--------------)

[

1







](https://medium.com/@divyagera2402/basic-fundaments-of-text-extraction-from-images-548ebe2fb4a5?source=post_page---author_recirc--e7d2dbc4e4ca----2---------------------efa8a10a_99ed_44e9_9f78_c3f2c09baefd--------------)

[

See all from Divya Gera

](https://medium.com/@divyagera2402?source=post_page---author_recirc--e7d2dbc4e4ca---------------------------------------)

## Recommended from Medium

![What are Decision Trees, Random Forest and Gradient Boosting Models?](https://miro.medium.com/v2/resize:fit:679/0*iiWqoqRh_3m8zvux)

[

![Damini Vadrevu](https://miro.medium.com/v2/resize:fill:20:20/1*aZoSPQCTS09ntMEqG4A_cg.jpeg)



](https://medium.com/@daminivadrevu?source=post_page---read_next_recirc--e7d2dbc4e4ca----0---------------------5af3e097_10ce_46d4_a36a_a6f82e673b71--------------)

[

Damini Vadrevu

](https://medium.com/@daminivadrevu?source=post_page---read_next_recirc--e7d2dbc4e4ca----0---------------------5af3e097_10ce_46d4_a36a_a6f82e673b71--------------)

[

## What are Decision Trees, Random Forest and Gradient Boosting Models?

### An all about Ensemble.



](https://medium.com/@daminivadrevu/what-are-decision-trees-random-forest-and-gradient-boosting-models-02cf3925af0e?source=post_page---read_next_recirc--e7d2dbc4e4ca----0---------------------5af3e097_10ce_46d4_a36a_a6f82e673b71--------------)

Mar 26

[

](https://medium.com/@daminivadrevu/what-are-decision-trees-random-forest-and-gradient-boosting-models-02cf3925af0e?source=post_page---read_next_recirc--e7d2dbc4e4ca----0---------------------5af3e097_10ce_46d4_a36a_a6f82e673b71--------------)

[

6







](https://medium.com/@daminivadrevu/what-are-decision-trees-random-forest-and-gradient-boosting-models-02cf3925af0e?source=post_page---read_next_recirc--e7d2dbc4e4ca----0---------------------5af3e097_10ce_46d4_a36a_a6f82e673b71--------------)

![10 ML Algorithms Every Data Scientist Should Know — Part 1](https://miro.medium.com/v2/resize:fit:679/1*lPuRae1B1MhOHoFeszuZvw.jpeg)

[

![Learning Data](https://miro.medium.com/v2/resize:fill:20:20/1*2h_G6zLH23eg9t6lkN_sZg.jpeg)



](https://medium.com/learning-data?source=post_page---read_next_recirc--e7d2dbc4e4ca----1---------------------5af3e097_10ce_46d4_a36a_a6f82e673b71--------------)

In

[

Learning Data

](https://medium.com/learning-data?source=post_page---read_next_recirc--e7d2dbc4e4ca----1---------------------5af3e097_10ce_46d4_a36a_a6f82e673b71--------------)

by

[

Rita Angelou

](https://medium.com/@ritaaggelou?source=post_page---read_next_recirc--e7d2dbc4e4ca----1---------------------5af3e097_10ce_46d4_a36a_a6f82e673b71--------------)

[

## 10 ML Algorithms Every Data Scientist Should Know — Part 1

### I understand well that machine learning might sound intimidating. But once you break down the common algorithms, you’ll see they’re not.



](https://medium.com/learning-data/10-ml-algorithms-every-data-scientist-should-know-part-1-2deced7f325f?source=post_page---read_next_recirc--e7d2dbc4e4ca----1---------------------5af3e097_10ce_46d4_a36a_a6f82e673b71--------------)

Jun 10

[

](https://medium.com/learning-data/10-ml-algorithms-every-data-scientist-should-know-part-1-2deced7f325f?source=post_page---read_next_recirc--e7d2dbc4e4ca----1---------------------5af3e097_10ce_46d4_a36a_a6f82e673b71--------------)

[

16







](https://medium.com/learning-data/10-ml-algorithms-every-data-scientist-should-know-part-1-2deced7f325f?source=post_page---read_next_recirc--e7d2dbc4e4ca----1---------------------5af3e097_10ce_46d4_a36a_a6f82e673b71--------------)

![Understand skip-trigram in a one-layer attention-only transformer with Pytorch](https://miro.medium.com/v2/resize:fit:679/1*81Wc39qY4tRUI8pLYZYQUg.png)

[

![Manyi](https://miro.medium.com/v2/resize:fill:20:20/1*PRRJs0q0QzXuHtHYKUh-Mg.jpeg)



](https://medium.com/@manyi.yim?source=post_page---read_next_recirc--e7d2dbc4e4ca----0---------------------5af3e097_10ce_46d4_a36a_a6f82e673b71--------------)

[

Manyi

](https://medium.com/@manyi.yim?source=post_page---read_next_recirc--e7d2dbc4e4ca----0---------------------5af3e097_10ce_46d4_a36a_a6f82e673b71--------------)

[

## Understand skip-trigram in a one-layer attention-only transformer with Pytorch

### The classic Anthropic’s paper “A Mathematical Framework for Transformer Circuits” looked into the functions of one-layer attention-only…



](https://medium.com/@manyi.yim/understand-skip-trigram-in-a-one-layer-attention-only-transformer-with-pytorch-4f47eb8d42c0?source=post_page---read_next_recirc--e7d2dbc4e4ca----0---------------------5af3e097_10ce_46d4_a36a_a6f82e673b71--------------)

Jul 15

[](https://medium.com/@manyi.yim/understand-skip-trigram-in-a-one-layer-attention-only-transformer-with-pytorch-4f47eb8d42c0?source=post_page---read_next_recirc--e7d2dbc4e4ca----0---------------------5af3e097_10ce_46d4_a36a_a6f82e673b71--------------)

![Logistic Regression Explained: ML Coding for Interviews](https://miro.medium.com/v2/resize:fit:679/0*rbSrwwSTfT20sOr1.png)

[

![Nailing the AI ML Interview](https://miro.medium.com/v2/resize:fill:20:20/1*ekTFdrRzc-bOUGCy5tvs1A.jpeg)



](https://medium.com/nailing-the-ai-ml-interview?source=post_page---read_next_recirc--e7d2dbc4e4ca----1---------------------5af3e097_10ce_46d4_a36a_a6f82e673b71--------------)

In

[

Nailing the AI ML Interview

](https://medium.com/nailing-the-ai-ml-interview?source=post_page---read_next_recirc--e7d2dbc4e4ca----1---------------------5af3e097_10ce_46d4_a36a_a6f82e673b71--------------)

by

[

Dr. R. Li

](https://medium.com/@Dr.R.B.LI?source=post_page---read_next_recirc--e7d2dbc4e4ca----1---------------------5af3e097_10ce_46d4_a36a_a6f82e673b71--------------)

[

## Logistic Regression Explained: ML Coding for Interviews

### When training a machine learning model, choosing the right loss function is critical to ensuring effective learning. In linear regression…



](https://medium.com/nailing-the-ai-ml-interview/selection-of-the-loss-functions-for-logistic-regression-ed2077f7075e?source=post_page---read_next_recirc--e7d2dbc4e4ca----1---------------------5af3e097_10ce_46d4_a36a_a6f82e673b71--------------)

Mar 8

[

](https://medium.com/nailing-the-ai-ml-interview/selection-of-the-loss-functions-for-logistic-regression-ed2077f7075e?source=post_page---read_next_recirc--e7d2dbc4e4ca----1---------------------5af3e097_10ce_46d4_a36a_a6f82e673b71--------------)

[

2







](https://medium.com/nailing-the-ai-ml-interview/selection-of-the-loss-functions-for-logistic-regression-ed2077f7075e?source=post_page---read_next_recirc--e7d2dbc4e4ca----1---------------------5af3e097_10ce_46d4_a36a_a6f82e673b71--------------)

![From Black Box to Fair Lending: Explaining Credit Risk Models with SHAP](https://miro.medium.com/v2/resize:fit:679/1*rJcX0q8c-yBR2oq3x5ui0A.png)

[

![Rahul Nair](https://miro.medium.com/v2/resize:fill:20:20/0*5qta69hTK-De5sbB)



](https://medium.com/@nair.rahul90?source=post_page---read_next_recirc--e7d2dbc4e4ca----2---------------------5af3e097_10ce_46d4_a36a_a6f82e673b71--------------)

[

Rahul Nair

](https://medium.com/@nair.rahul90?source=post_page---read_next_recirc--e7d2dbc4e4ca----2---------------------5af3e097_10ce_46d4_a36a_a6f82e673b71--------------)

[

## From Black Box to Fair Lending: Explaining Credit Risk Models with SHAP

### Why your AI’s ‘why’ is critical for banks, regulators, and customers.



](https://medium.com/@nair.rahul90/from-black-box-to-fair-lending-explaining-credit-risk-models-with-shap-fe1643559402?source=post_page---read_next_recirc--e7d2dbc4e4ca----2---------------------5af3e097_10ce_46d4_a36a_a6f82e673b71--------------)

Jul 7

[](https://medium.com/@nair.rahul90/from-black-box-to-fair-lending-explaining-credit-risk-models-with-shap-fe1643559402?source=post_page---read_next_recirc--e7d2dbc4e4ca----2---------------------5af3e097_10ce_46d4_a36a_a6f82e673b71--------------)

![Master Hyperparameter Tuning in Machine Learning](https://miro.medium.com/v2/resize:fit:679/0*qqtfc-vs3-BYuDp2)

[

![Towards AI](https://miro.medium.com/v2/resize:fill:20:20/1*JyIThO-cLjlChQLb6kSlVQ.png)



](https://medium.com/towards-artificial-intelligence?source=post_page---read_next_recirc--e7d2dbc4e4ca----3---------------------5af3e097_10ce_46d4_a36a_a6f82e673b71--------------)

In

[

Towards AI

](https://medium.com/towards-artificial-intelligence?source=post_page---read_next_recirc--e7d2dbc4e4ca----3---------------------5af3e097_10ce_46d4_a36a_a6f82e673b71--------------)

by

[

Kuriko Iwai

](https://medium.com/@kuriko-iwai?source=post_page---read_next_recirc--e7d2dbc4e4ca----3---------------------5af3e097_10ce_46d4_a36a_a6f82e673b71--------------)

[

## Master Hyperparameter Tuning in Machine Learning

### Explore strategies and practical implementation on tuning an ML model to achieve the optimal performance



](https://medium.com/towards-artificial-intelligence/mastering-hyperparameter-tuning-in-machine-learning-252ce466b472?source=post_page---read_next_recirc--e7d2dbc4e4ca----3---------------------5af3e097_10ce_46d4_a36a_a6f82e673b71--------------)

Jul 3

[

](https://medium.com/towards-artificial-intelligence/mastering-hyperparameter-tuning-in-machine-learning-252ce466b472?source=post_page---read_next_recirc--e7d2dbc4e4ca----3---------------------5af3e097_10ce_46d4_a36a_a6f82e673b71--------------)

[

361

](https://medium.com/towards-artificial-intelligence/mastering-hyperparameter-tuning-in-machine-learning-252ce466b472?source=post_page---read_next_recirc--e7d2dbc4e4ca----3---------------------5af3e097_10ce_46d4_a36a_a6f82e673b71--------------)

[

4







](https://medium.com/towards-artificial-intelligence/mastering-hyperparameter-tuning-in-machine-learning-252ce466b472?source=post_page---read_next_recirc--e7d2dbc4e4ca----3---------------------5af3e097_10ce_46d4_a36a_a6f82e673b71--------------)

[

See more recommendations

](https://medium.com/?source=post_page---read_next_recirc--e7d2dbc4e4ca---------------------------------------)

[

Help

](https://help.medium.com/hc/en-us?source=post_page-----e7d2dbc4e4ca---------------------------------------)

[

Status

](https://medium.statuspage.io/?source=post_page-----e7d2dbc4e4ca---------------------------------------)

[

About

](https://medium.com/about?autoplay=1&source=post_page-----e7d2dbc4e4ca---------------------------------------)

[

Careers

](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----e7d2dbc4e4ca---------------------------------------)

[

Press

](mailto:pressinquiries@medium.com)

[

Blog

](https://blog.medium.com/?source=post_page-----e7d2dbc4e4ca---------------------------------------)

[

Privacy

](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----e7d2dbc4e4ca---------------------------------------)

[

Rules

](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----e7d2dbc4e4ca---------------------------------------)

[

Terms

](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----e7d2dbc4e4ca---------------------------------------)

[

Text to speech

](https://speechify.com/medium?source=post_page-----e7d2dbc4e4ca---------------------------------------)