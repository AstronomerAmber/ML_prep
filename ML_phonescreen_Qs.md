# ML Q & A interview prep:

## ML Algoritms + Basic ML

Q: What are the various types of ML? 

A: Supervised (labeled data) , Unsupervised (unlabeled data) , Reinforcement (using penalty and reward)

Q: What is your favorite algorithm? Is it used for classification or regression? (explain in under a minute)

A: Open-ended

Q: What is the difference between ML, DL and AI?

A: - AI involves machines that can perform tasks that are characteristic of human intelligence
ML is a way of achieving AI by “training” an algorithm so that it can learn data.
Deep learning is one of many approaches to machine learning, which uses Neural Networks that mimic the biological structure of the brain. 
Another difference is the feature extraction and classification are separate steps for ML but are a single NN for DL.

Q: Talk about a recent ML paper that you’ve read in 2 minutes.

A: Open-ended

Be able to explain the following metrics: Accuracy, Precision, Recall, and F1, TP, TN, FP, TN

Q: Explain how a ROC (Receiver operating characteristic) curve works.

The ROC curve is a graphical representation of the contrast between true positive rates and the false positive rate at various thresholds. It’s often used as a proxy for the trade-off between the sensitivity of the model (true positives) vs specificity (false positives). You want your model to get TPs faster than FPs, if there is the same rate of gettingTP as getting FP your model is useless.

Q: Explain TP/FP/FN/TN in a simple example:

A: - Fire alarm goes off + fire = TP
Fire alarm goes off + no fire = FP
Fire alarm doesn’t go off + fire = FN
Fire alarm doesn’t go off + no fire = TN

Q: What is Bayes Theorem?

A: Essentially Bayes Theorem gives you a probability of an event given what is known as prior knowledge, Prob = TP/ All positives(TP+FP).

Q: Why is “Naive” Bayes naive? 

A: NB makes the naive assumption that the features in a dataset are independent of each other, which isn’t applicable to real-world datasets.

Q: What is a decision tree and when would you choose to use one?

A: As the name suggests decision trees are tree-like model of decisions, they make relations between features easily interpretable. They can be used for both classification (classify passenger as survived or died) and regression (continuous values like price of a house) and don’t require any assumptions of linearity in the data.

Q: How are they pruned?

A: Pruning is what happens in decision trees when branches that have weak predictive power are removed in order to reduce the complexity of the model and increase the predictive accuracy of a decision tree model. Pruning can happen bottom-up and top-down, with approaches such as reduced error pruning and cost complexity pruning.

Reduced error pruning is perhaps the simplest version: replace each node. If it doesn’t decrease predictive accuracy, keep it pruned. While simple, this heuristic actually comes pretty close to an approach that would optimize for maximum accuracy.

Q: What is the difference between Gini Impurity and Entropy in a decision tree? 

A: While both are metrics to decide how to split a tree, Gini measurement is the probability of a random sample being classified correctly by randomly picking a label from the branch. In information theory Entropy is the measured lack of information in a system and you calculate gain by making a split. This delta entropy tells you about how the uncertainty about the label was reduced. Gini is more common because it doesn’t require the log calculations that Entropy takes.

Q: When will Entropy decrease in binary tree classification?

A: It decreases the closer we get to the leaf node.

Q: Why don’t we tend to use linear regression to model binary responses?

A: Linear regression prediction output is continuous, if you want to model binary results you should use logistic regression.

Q: What is the difference between hinge loss and log loss?

A: The hinge loss is used for "maximum-margin" classification, most notably for support vector machines. Logistic loss diverges faster than hinge loss. So, in general, it will be more sensitive to outliers. Hinge loss also penalizes wrong answers, as well as correct unconfident answers.

Q: How do linear and logistic regression differ in their error minimization techniques?

A: Linear regression uses ordinary least squares method to minimize the errors and arrive at a best possible fit, while logistic regression uses maximum likelihood method to arrive at the solution.

Q: What is more important model accuracy or model performance?

A: Model accuracy is actually a subset of model performance. For example, if you wanted to detect fraud in a massive dataset with a sample of millions, a more accurate model would most likely predict no fraud at all if only a vast minority of cases were fraud. However, this would be useless for a predictive model — a model designed to find fraud that asserted there was no fraud at all!

Q: What’s the difference between a generative and discriminative model?

A: Discriminative models are great for classification (SVM, NN, NLPs, facial recognition), they map high dimensional sensory input into a class. A generative models care how the data was generated and will learn will learn categories of data (chatbot, GANs).

Q: How does SVM and logistic regression differ?

A: They only differ in the loss function — SVM minimizes hinge loss while logistic regression minimizes logistic loss.

Q: What is an SVM? What do you do if your data is not linear? (kernel trick)

A: The objective of the support vector machine algorithm is to find the hyperplane that has the maximum margin in an N-dimensional space(N — the number of features) that distinctly classifies the data points. A kernel trick allows you to map your data to a higher dimensional feature space so you can fit a hyperplane. This is done by taking the vectors in the original space and returning the dot product of the vectors in the feature space.

Q: How do you turn the regularization (C) and gamma terms in SVMs?

A: High gamma values mean only data points close to the line are considered and a high C term means a smaller-margin around line (could overfit).

Q: Explain Dijkstra's algorithm? (Know how to use it).

A: Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph.

Q: How is KNN different from K-means clustering?

A: KNN or K-Nearest Neighbors is a supervised learning method technique used from classification or regression and does not require training. K-means is an unsupervised clustering algorithm fitting to K-clusters. 

Q: What is ensemble learning?

A: Ensemble techniques use a combination of learning algorithms to optimize better predictive performance. And they typically reduce overfitting in models. Ensembling techniques are further classified into Bagging and Boosting.

Q: What is the difference between bagging and boosting?

A: Both are ensemble models that use random sampling to reduce variance. Bagging models are built independently and better solves the problem of overfitting. Boosting builds on top of old models to create models with less bias, also weights the better performing examples higher, but may overfit. 

Q: How do you go from a decision tree to a random forest? To a Gradient Boosted Tree?

A: Bagging takes many uncorrelated learners to make a final model and it reduces error by reducing variance. Example of bagging ensemble are Random Forest models.

Boosting is an ensemble technique in which the predictors are not made independently, but sequentially in order to learn from the mistakes of the previous predictors. Gradient Boosted Trees are an example of boosting algorithm.

Q: Describe a hash table.

A: A hash table is a data structure like a dictionary in python. A key is mapped to certain values through the use of a hash function. They are often used for tasks such as database indexing.

Q: How do you deal with imbalanced data?

A: Collect more data, resample the dataset to correct for imbalances, try difference models or algorithms. 

## ML Validation

Q: Name two ways to evaluate the performance of a classification algorithm.

A: 1) Confusing Matrix ([TN,FP],[FN,TP]) 
     2) Accuracy (also AUC, F1, MAE, MSE)

Q: What’s the difference between Type I and Type II error?

A: Type I error is a false positive, while Type II error is a false negative.

Q: What is the difference between MSE and MAE?

A: MAE loss is more robust to outliers, but its derivatives are not continuous, making it inefficient to find the solution. MSE loss is sensitive to outliers, but gives a more stable and closed form solution (by setting its derivative to 0). Use MAE if you have a lot of anomalies in your dataset.

Q: Why do we need a cost function and which is the best cost to use in classification algorithms.

A: We need a cost function to optimize our weights for model performance and I would use the cost function Mean Squared Error and minimize the MSE to improve the accuracy of our classification model.

Q: How do you ensure you’re not overfitting with a model?

A: 1- Keep the model simpler: reduce variance by taking into account fewer variables and parameters, thereby removing some of the noise in the training data.
2- Use cross-validation techniques such as k-folds cross-validation.
3- Use regularization techniques such as LASSO that penalize certain model parameters if they’re likely to cause overfitting.

Q: Explain the cross-validation resampling procedure.

A: The general procedure is as follows:

1) Shuffle the dataset randomly.
2) Split the dataset into k groups
3) For each unique group:
Take the group as a hold out or test data set
Take the remaining groups as a training data set
Fit a model on the training set and evaluate it on the test set
Retain the evaluation score and discard the model
4)Combine evaluation scores into single average (CV error)
5)Repeat process for different model and choose the one w/ lowest CV error

Q: How does evaluating your model differ between using CV or bootstrapping? What is MC-CV?

A: CV tends to be less biased but K-fold CV has fairly large variance. On the other hand, bootstrapping (sampling with replacement) tends to drastically reduce the variance but gives more biased results (they tend to be pessimistic). "Monte Carlo CV" aka "leave-group-out CV" does many random splits of the data to reduce variance.

Q: What’s the trade-off between bias and variance?

A: Bias is due to overly simplistic assumptions while variance is error due to too much complexity in the learning algorithm you’re using. Bias leads to under-fitting your data and variance leads to overfitting your data. Essentially, if you make the model more complex and add more variables, you’ll lose bias but gain some variance — in order to get the optimally reduced amount of error, you’ll have to tradeoff bias and variance and try your best to minimize each.
(In machine learning/statistics as a whole, accuracy vs. precision is analogous to bias vs. variance).

Q: What cross-validation technique would you use on a time series dataset?

A: Instead of using standard k-folds cross-validation, you have to pay attention to the fact that a time series is not randomly distributed data — it is inherently ordered by chronological order. If a pattern emerges in later time periods for example, your model may still pick up on it even if that effect doesn’t hold in earlier years!

You’ll want to do something like forward chaining where you’ll be able to model on past data then look at forward-facing data.

fold 1 : training [1], test [2]
fold 2 : training [1 2], test [3]
fold 3 : training [1 2 3], test [4]
fold 4 : training [1 2 3 4], test [5]
fold 5 : training [1 2 3 4 5], test [6]

Q: What’s the difference between L1 and L2 regularization? How does it solve the problem of overfitting? Which regularizer to use and when?

A: When dealing with a large number of features we no longer want to use CV. Both L1 (Lasso Regression) and L2 (Ridge Regression) regularization techniques are used to address over-fitting and feature selection, the key difference between these two is the penalty term. Lasso Regression (Least Absolute Shrinkage and Selection Operator) adds “absolute value of magnitude” of coefficient while Ridge regression adds “squared magnitude” of coefficient as penalty term to the loss function. 
The key difference between these techniques is that Lasso is more binary/sparse and shrinks the less important feature’s coefficient to zero thus, removing some feature altogether and L2 regularization tends to spread error among all the term. L1 works well for feature selection in case we have a huge number of features.

## ML Stats

Q: What is a Fourier transform? And why do we use it.

A:  Given a smoothie, it’s how we find the recipe (in terms of superposition of symmetric functions). Fourier transforms are used to it’s a extract features from audio signals by converting a signal from time to frequency domain.

Q: What’s the difference between probability and likelihood?

A: For binomial distributions: Probability is the percentage that a success occur. Likelihood is the conditional probability, i.e. the probability that the above event will happen.

Q: What is the difference between PCA and t-SNE? What are their use cases?

A: Both methods are used for dimensionality reduction, but t-SNE tries to deconvolve relationships between neighbors in high-dimensional data to understand the underlying structure of the data. Principal component analysis first identifies the hyperplane that lies closest to the data, and then projects the data onto it. PCA preserves the maximum amount of variance and requires labels, but is much less computationally expensive than t-SNE.

Q: How do eigenvalues and eigenvectors relate to PCA?

A: Eigenvectors have corresponding eigenvalues and eigenvectors that have the largest eigenvalues will be the principal components (new dimensions of our data).

Q: What is Maximum Likelihood (MLE)?

A: Maximum likelihood estimation is a method that determines values for the parameters of a model. The parameter values are found such that they maximize the likelihood that the process described by the model produced the data that were actually observed.

Q: When are Maximum Likelihood and Least Squared Error equal?

A: For least squares parameter estimation we want to find the line that minimizes the total squared distance between the data points and the regression line. In maximum likelihood estimation we want to maximize the total probability of the data. When a Gaussian distribution is assumed, the maximum probability is found when the data points get closer to the mean value. Since the Gaussian distribution is symmetric, this is equivalent to minimizing the distance between the data points and the mean value.

### Sources: 
Astronomer Amber!
https://ml-cheatsheet.readthedocs.io/en/latest/forwardpropagation.html
Machine Learning Interview Questions and Answers | Machine Learning Interview Preparation | Edureka
https://www.springboard.com/blog/machine-learning-interview-questions/
https://machinelearningmastery.com/k-fold-cross-validation/
https://towardsdatascience.com/l1-and-l2-regularization-methods-ce25e7fc831c
https://towardsdatascience.com/support-vector-machine-vs-logistic-regression-94cc2975433f
https://towardsdatascience.com/probability-concepts-explained-maximum-likelihood-estimation-c7b4342fdbb1
https://medium.com/mlreview/gradient-boosting-from-scratch-1e317ae4587d
