import csv
import random
import math
import pandas as pd
import numpy as np
import scipy.linalg as la
from sklearn.metrics import mean_squared_error, r2_score

class Dataloader:
    def __init__(self, path):
        self.data = pd.read_csv(path)
        self.length = len(self.data)
        self.drop_address()
        self.feature, self.label = self.get_feature_label()
        self.normalize()
        self.pad_data()
        self.n_feature = len(self.feature.iloc[0])

    def drop_address(self):
        self.data = self.data.drop(columns=['Address'])

    def normalize(self):
        self.feature = (self.feature-self.feature.min()) / (self.feature.max()-self.feature.min())

    def train_val_split(self, pval=0.3):
        slice = math.floor(self.length*pval)
        ind = [i for i in range(self.length)]
        random.shuffle(ind)
        train = {'feature':self.feature.iloc[ind[slice:]], 'label':self.label.iloc[ind[slice:]]}
        val = {'feature':self.feature.iloc[ind[:slice]], 'label':self.label.iloc[ind[:slice]]}
        return train, val

    def get_feature_label(self):
        feature = self.data.iloc[:,:-1]
        label = self.data.iloc[:,-1]
        return feature, label

    def pad_data(self):
        bias = [1] * self.length
        self.feature['bias'] = bias
        self.label['bias'] = bias


class LinearRegression:
    def __init__(self, path='USA_Housing.csv'):
        self.dataloader = Dataloader(path)
        self.train, self.val = self.dataloader.train_val_split()
        self.coef = np.zeros(self.dataloader.n_feature)

    def fit(self):
        x_train = self.train['feature'].values
        y_train = self.train['label'].values
        self.coef = np.linalg.pinv(x_train.T @ x_train) @ x_train.T @ y_train

    def predict(self, data):
        return np.dot(data, self.coef)

    def get_rmse(self):
        y_pred = self.predict(self.val['feature'].values)
        y = self.val['label'].values
        return np.sqrt((np.sum((y_pred - self.val['label'].values)**2)/len(y)))
    def get_sklearn_rmse(self):
        y_pred = self.predict(self.val['feature'].values)
        y = self.val['label'].values
        return np.sqrt(mean_squared_error(y, y_pred)*len(y))
        #return la.norm(y_pred - y) #The Frobenius norm
    def get_R2(self):
        y_pred = self.predict(self.val['feature'].values)
        return r2_score(self.val['label'].values,y_pred)


if __name__ == '__main__':
    lr = LinearRegression()
    lr.fit()
    print('RMSE [sklearn]:', lr.get_sklearn_rmse())
    print('RMSE:', lr.get_rmse())
    print('R2:', lr.get_R2())
