#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import numpy as np

# Each row is a training example, each column is a feature  [X1, X2, X3]
X=np.array(([0,0,1],[0,1,1],[1,0,1],[1,1,1]), dtype=float)
y=np.array(([0],[1],[1],[0]), dtype=float)

# Define useful functions

# Activation function
def sigmoid(t):
    return 1/(1+np.exp(-t))

# Derivative of sigmoid
def sigmoid_derivative(p):
    return p * (1 - p)

def loss(y, y_pred):
    return np.mean(np.square(y-y_pred))

# Class definition
class NeuralNetwork:

    def __init__(self, x,y):

        # Input Matrix
        self.x = x

        # First Layer Hidden parameters
        self.w1= np.random.rand(self.x.shape[1], 4) # considering we have 4 nodes in the hidden layer
        self.b1 = np.random.rand(1, 4)
        # Second Layer Hidden parameters - leads to the output
        self.w2 = np.random.rand(4,1)
        self.b2 = np.random.rand(1,1)

        # Output Labels
        self.y = y

    def feedforward(self):

        # First Layer
        # z1 = X*w1 + b1
        self.z1 = self.x @ self.w1 + self.b1

        # A_1 = sigmoid(Z_1)
        self.a1 = sigmoid(self.z1)

        # Second Layer
        self.z2 = self.a1 @ self.w2 + self.b2
        self.a2 = sigmoid(self.z2)

        return self.a2

    def backprop(self, lr):

        # Backprop for the first Layer

        # dL/da2 = -2 *(y - a2)
        d_a2 = -2*(self.y - self.a2)
        # dL/dz2 = (dL/da2) * (da2/dz2) = -2 *(y-a2)  * a2 * (1-a2)
        d_z2 = d_a2 * sigmoid_derivative(self.a2)
        # dL/dw2 = (dL/da2) * (da2/dz2) * (dz2/dw2) = a1.T @ (-2*(y-a2)  * a2 * (1-a2))
        d_w2 = self.a1.T @ d_z2
        d_b2 = np.mean(d_z2, axis=0, keepdims=True)

        # Backprop for the second Layer
        # dL/da1 = (dL/da2) * (da2/dz2) * (dz2/da1)
        d_a1 = d_z2 @ self.w2.T
        # dL/dz1 =  (dL/da2) * (da2/dz2) * (dz2/da1) * (da1/dz1)
        d_z1 = d_a1 * sigmoid_derivative(self.a1)
        # Take the mean of the Gradient of Z1 over the samples axis. Keep dims to get a (1,4) dim matrix.
        d_b1 = np.mean(d_z1, axis=0, keepdims=True)
        # dL/dw1 = (dL/da2) * (da2/dz2) * (dz2/da1) * (da1/dz1) * (dz1/dw1)
        d_w1 = self.x.T @ d_z1

        # Update the parameters - W1, W2, b1, b2.
        self.w2 -= (lr * d_w2)
        self.w1 -= (lr * d_w1)
        self.b2 -= (lr * d_b2)
        self.b1 -= (lr * d_b1)

    def train(self, lr):

        # Forward Prop
        self.output = self.feedforward()

        # Back Prop
        self.backprop(lr)

if __name__ == "__main__":

    NN = NeuralNetwork(X, y)
    for i in range(10000):  # trains the NN 1,000 times
        # Run one training cycle
        NN.train(lr=1)

        # Print metrics
        if i % 100 == 0:
            print(f"for iteration: {i}")
            print(f"Actual Output: {y}")
            print(f"Predicted Output: {NN.a2}" + str(NN.feedforward()))
            print(f"Loss: {loss(NN.y, NN.a2)}")  # mean sum squared loss
            print("\n")
