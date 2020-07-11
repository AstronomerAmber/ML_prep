import csv
import random
import math
import operator
import pandas as pd

class Dataloader:
    def __init__(self, iris_path):
        self.data = pd.read_csv(iris_path)
        self.data.columns = ['Sepal_length', 'Sepal_width', 'Petal_length','Petal_width', 'label']
        self.length = len(self.data)
        self.to_num()
        self.feature, self.label = self.get_feature_label()
        self.normalize()

    def to_num(self):
        self.data = self.data.apply(pd.to_numeric)

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


class KNN:
    def __init__(self, iris_path='./iris.csv'):
        self.dataloader = Dataloader(iris_path)
        self.train, self.val = self.dataloader.train_val_split()

    def predict(self, k, data):
        self.min_cand = ((self.train['feature'] - data) ** 2).sum(axis=1).argsort().iloc[:k]
        label = self.train['label'].iloc[self.min_cand]
        prediction = label.value_counts().index[0]
        return prediction

    def get_accuracy(self, k):
        correct = 0.0
        length = len(self.val['label'])
        for i in range(length):
            prediction = self.predict(k, self.val['feature'].iloc[i])
            correct += float(prediction == self.val['label'].iloc[i])

        return correct/length


if __name__ == '__main__':
    k = input("Choose the number of k for KNN: ")
    k = int(k)
    knn = KNN()
    print(knn.get_accuracy(k))
