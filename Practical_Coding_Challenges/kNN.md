Implement k-Nearest Neighbors (kNN) in Python from scratch, you may ONLY use:

import csv
import random
import math
import operator
import pandas

Use the [Iris dataset](https://codesignal.s3.amazonaws.com/uploads/1594240000429/iris.csv) + your classifier to achieve at least 90% accuracy.

The Iris Flower Dataset involves predicting the flower species given measurements of iris flowers.

It is a multiclass classification problem. The number of observations for each class is balanced.

There are 150 observations with 4 input variables and 1 output variable.
The variable names are as follows:
* Sepal length in cm.
* Sepal width in cm.
* Petal length in cm.
* Petal width in cm.

Remember kNN is supervised, so you are calculating distances from points in your test set to  ‘k’ nearest neighbors in your training set.

For a refresher on kNN, [checkout](https://www.edureka.co/blog/k-nearest-neighbors-algorithm/).

kNN:
* K nearest neighbors or KNN Algorithm is a simple algorithm which uses the entire dataset in its training phase. Whenever a prediction is required for an unseen data instance, it searches through the entire training dataset for k-most similar instances and the data with the most similar instance is finally returned as the prediction.
* The k in kNN algorithm represents the number of nearest neighbor points which are voting for the new test data’s class.

![](https://codesignal.s3.amazonaws.com/uploads/1594240458880/KNN-Classification.gif)

Functional Steps:
function 0: Load a CSV file (done for you)
function 1: Convert string column to integer (done for you)
function 2: Find the min and max values for each column
function 3: Rescale dataset columns to the range 0-1
function 4: Split a dataset into k-folds (implement this if there is time at the end)
function 5: Calculate the accuracy percentage
function 6: Evaluate an algorithm using a cross-validation split
function 7: Calculate the Euclidean distance between two vectors
function 8: Locate the most similar neighbors
function9: Make a prediction with neighbors
function10: kNN Algorithm

**Note**: This CS practical needs to have at least one class (kNN), but there should be a second class to load the data.

then...

**Test the kNN on the Iris Flowers dataset to achieve >90% accuracy.**
