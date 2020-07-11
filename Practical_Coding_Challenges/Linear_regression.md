Linear Regression
![](https://codesignal.s3.amazonaws.com/uploads/1594247060882/linearRegression2-3.png)


**Task**

Train a [linear regression model](https://towardsdatascience.com/linear-regression-using-python-ce21aa90ade6) from this [dataset](https://www.kaggle.com/aariyan101/usa-housingcsv). If you are not familiar with Kaggle you can also download the dataset [here](https://raw.githubusercontent.com/bcbarsness/machine-learning/master/USA_Housing.csv).


**Background**:

- Linear Regression is a way of predicting a response Y on the basis of a single predictor variable X. It is assumed that there is approximately a linear relationship between X and Y. Mathematically, we can represent this relationship as:
- Y ≈ ɒ + ß X + ℇ
- where ɒ and ß are two unknown constants that represent intercept and slope terms in the linear model and ℇ is the error in the estimation.

**Steps**:

- Start by taking the simplest possible example and alculate the regression with only two data points (price for dependent and number of rooms for independent).
- Then use price as the dependent variable and all others as independent variables.

- Functional statements
  - Function for train/test splitting
  - Function for fitting the model
  - Function for running prediction on the holdout (test) set
  - Function for outputting some analysis (organized text here is fine)

**Output**
- Lastly, print the RMSE (root mean squared error) of your results and the r2 value.
- r2 score—varies between 0 and 100%, if it is 100%, the two variables are perfectly correlated, i.e., with no variance at all. A low value would show a low level of correlation, meaning a regression model that is not valid, but not in all cases.

**BONUS STEPS**:
* Explore the correlation using Pearson Correlation Coefficient. If you want resources for this check out the [pandas implementation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.corr.html) or the [Wiki article](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient)
* Re-implement Seaborn's  [library for plotting pairwise relationships in a dataset](https://seaborn.pydata.org/generated/seaborn.pairplot.html)
