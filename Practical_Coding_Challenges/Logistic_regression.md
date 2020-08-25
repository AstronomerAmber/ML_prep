# -*- coding: utf-8 -*-

**Binary Logistic Regression**
Implement binary logistic regression and apply it to iris datasets

- Check [here](https://medium.com/@martinpella/logistic-regression-from-scratch-in-python-124c5636b8ac) for source
- original colab [notebook]https://colab.research.google.com/drive/1_lAj1Fe3CxDdxps4Ooojpyb4SNYoEn9o

BLR is a function that given a sample with `N` features will combine them together linearly and return a number between 0 and 1 which is to be considered the probability that that sample belongs to the positive class.

The formula for obtaining the output for one sample is the following:

First the input features of one sample needs to be multiplied by some weights that output a number

> `h = x_i * w`

w is a vector of size `N x 1`
h is a number

to have the probability

> `sigmoid(h) = y_pred = z = 1 / (1 + exp(-h)) `

We will need this once the weights have been trained. However for the update we need the loss and its derivative wrt the weights

The loss for BLR is Binary Cross Entropy and is expressed as

> `BCE = J = -1/M * sum(y_true_i * log(y_pred_i) + (1 - y_true_i) * log(1 - y_pred_i))`

NB this is for a set of `M` samples with `N` features

and the derivative with respect to the weights is
> `dJ(w)/dw = 1/M X^T (z - y) = 1/M X^T (1 / (1 + exp(-XW)) - y)`

and finally the update is

> `w = w - lr dJ(w)/dw`

These are the basic algorithm and functions to be implemented the extra things you should pay attention to are
- [x] add bias
- [ ] stop condition based on the difference with the previous loss and max_iterations
- [x] add threshold
