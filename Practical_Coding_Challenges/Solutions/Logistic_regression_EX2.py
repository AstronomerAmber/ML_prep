from sklearn import datasets
import numpy as np
import seaborn as sns
from sklearn.metrics import f1_score
from sklearn.preprocessing import normalize
from sklearn.utils import shuffle

class BinaryLogisticRegression:
  def __init__(self, lr=0.01, max_iter=1000, fit_intercept=True):
    self.lr = lr
    self.w = [] # needs input data to define size
    self.max_iter = max_iter
    self.threshold = 0.5
    self.fit_intercept = fit_intercept

  def fit(self, X, y):
    if self.fit_intercept:
      self._add_intercept(X)

    self.w = np.random.uniform(0, 1, X.shape[1])

    for _ in range(self.max_iter):
      h = np.dot(X, self.w)
      z = self._sigmoid(h)

      gradients = (np.dot(X.T, z - y)) / X.shape[0]

      self.w -= self.lr * gradients

  def _add_intercept(self, X):
    intercept = np.ones((X.shape[0], 1))
    X = np.concatenate((X, intercept), axis=1)

  def predict_prob(self, X):
    if self.fit_intercept:
      self._add_intercept(X)
    return self._sigmoid(np.dot(X, self.w))

  def predict(self, X):
    return self.predict_prob(X) >= self.threshold


  def _sigmoid(self, h):
    return 1 / (1 + np.exp(-h))

dataset = datasets.load_iris()
X = dataset.data[:,:2]
y = (dataset.target != 0) * 1

X = normalize(X)

X, y = shuffle(X, y)

blg = BinaryLogisticRegression(max_iter=30000, lr=0.1)
c = 0
blg.fit(X, y)
y_pred = blg.predict(X)
f1 = f1_score(y, y_pred)
print(f'w: {blg.w}, f1_score: {f1}')

X.shape

np.random.uniform(0, 1, 10)

h = X.dot(w)
h.shape

h[:10]

z = 1 / (1 + np.exp(h))
z.shape

z[:10]

dJdw = (X.T.dot(z - y)) / M_feats
print(dJdw.shape, '\n', dJdw[:10])
