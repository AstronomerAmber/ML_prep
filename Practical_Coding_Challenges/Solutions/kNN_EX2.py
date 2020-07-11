import csv
import random as rn
import math
import operator
import pandas as pd

#%% Solution
class KNN() :
    def __init__(self, data) :
        self.data = data
        self.data = self.processData(data)
        self.splitData(data, .8)

    def processData(self, data) :
        for col in data.columns[:-1] :
            data[col] = (data[col] - data[col].min())
            data[col] = data[col] / data[col].max()
        return data

    def splitData(self, data, trn_percent) :
        trnNum = int(len(data) * trn_percent)
        self.trnData = data.sample(trnNum)
        self.valData = data.drop(self.trnData.index)

    def predict(self, k, data, point) :
        dists = []
        for i, row in data.iterrows() :
            a = row.values[:4]
            b = point.values[:4]
            dist = self.dist(a,b)
            dists.append(dist)
        data['dist'] = dists

        data = data.sort_values(by=['dist'])
        closest = data[:k].label.value_counts()
        result = closest.argmax()
        return result

    def dist(self, a, b) :
        total = 0
        for i in range(len(a)) :
            total += math.pow(a[i]-b[i], 2)
        math.sqrt(total)
        return total

def loadData() :
    # 0 setosa	1 versicolor 2 virginica
    data = pd.read_csv('iris.csv')
    data.columns = ['seplen', 'sepwid', 'petlen', 'petwid', 'label']
    return data

#%% Testing
data = loadData()
knn = KNN(data)

correct = 0
for i in range(len(knn.valData)) :
    result = knn.predict(5, knn.trnData, knn.valData.iloc[i])
    if result == knn.valData.iloc[i].label :
        correct += 1

print('Accuracy: %.3f%%' % (correct / len(knn.valData)))
