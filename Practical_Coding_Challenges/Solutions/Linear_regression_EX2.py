from typing import Tuple
import numpy as np
import pandas as pd
import random


def get_data(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)


def train_test_split(data: pd.DataFrame, split_ratio: float, y_col_name: str) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:

    indexes = list(data.index)

    num_train_samples = int(len(data) * split_ratio)
    train_indexes = random.sample(indexes, num_train_samples)
    test_indexes = [i for i in indexes if i not in train_indexes]

    train_set = data.iloc[train_indexes]
    y_train, x_train = train_set[y_col_name], train_set.drop(
        y_col_name, axis=1)

    test_set = data.iloc[test_indexes]
    y_test, x_test = test_set[y_col_name], test_set.drop(y_col_name, axis=1)

    return x_train, y_train, x_test, y_test


class LinearRegression:
    def __init__(self):
        # intiialize intercepts for linear regression
        self.B0 = None
        self.B1 = None
        self.coefficients = None

    def predict(self, input_data):
        # return sum(self.B1 * input_data + self.B0)
        input_data = self._concatenate_ones(input_data)
        return self.coefficients.dot(input_data)

    def _concatenate_ones(self, X):
        # concatenate a column of ones to X, this is for the bias term in linear regression
        if len(X.shape) == 1:
            ones = np.ones((1))
            return np.concatenate((ones, X), 0)
        else:
            ones = np.ones(shape=X.shape[0]).reshape(-1, 1)
            return np.concatenate((ones, X), 1)

    def fit(self, x_train, y_train):
        x_train = self._concatenate_ones(x_train)

        self.coefficients = np.linalg.inv(x_train.T.dot(x_train)).dot(x_train.T).dot(y_train)

def generate_dataset_simple(beta, n, std_dev):
    # Generate x as an array of `n` samples which can take a value between 0 and 100
    x = np.random.randn(n, 5) * 100
    # Generate the random error of n samples, with a random value from a normal distribution, with a standard
    # deviation provided in the function argument
    e = np.random.randn(n) * std_dev
    # Calculate `y` according to the equation discussed
    y = x.dot(beta.T) + e
    return x, y

def main():
    split_ratio = 0.8
    y_col_name = 'Price'

    data = get_data('USA_Housing.csv')
    # drop the Address column as only focused on numerical columns for now
    data = data.drop('Address', axis=1)
    x_train, y_train, x_test, y_test = train_test_split(
        data, split_ratio, y_col_name)

    x_train = x_train.values
    y_train = y_train.values
    x_test = x_test.values
    y_test = y_test.values

    # test using simple dataset
    # x, y = generate_dataset_simple(np.array([10]*5), 32, 100)
    # # Take the first 40 samples to train, and the last 10 to test
    # x_train = x[:-10]
    # y_train = y[:-10]

    # x_test = x[-10:]
    # y_test = y[-10:]

    lr = LinearRegression()
    lr.fit(x_train, y_train)

    mean_squared_error = []
    for i, x_row in enumerate(x_test):
        y_pred = lr.predict(x_row)
        squared_error = (y_test[i] - y_pred)**2
        mean_squared_error.append(squared_error)

    mean_squared_error = np.sqrt(sum(mean_squared_error) / len(y_test))
    print(f'RMSE: {mean_squared_error}')
    # print(f'Coefficients: {lr.B0}, {lr.B1}')


    ### Use SKLEARN to baseline model ###
    from sklearn.linear_model import LinearRegression as LinearRegression_Sklearn
    reg = LinearRegression_Sklearn().fit(x_train, y_train)

    mean_squared_error = []
    for i, x_row in enumerate(x_test):
        y_pred = reg.predict(x_row.reshape(1, -1))
        squared_error = (y_test[i] - y_pred)**2
        mean_squared_error.append(squared_error)

    mean_squared_error = np.sqrt(sum(mean_squared_error) / len(y_test))
    print(f'RMSE [sklearn]:: {mean_squared_error}')
    # print(f'Coefficients: {reg.coef_}')

if __name__ == '__main__':
    main()
