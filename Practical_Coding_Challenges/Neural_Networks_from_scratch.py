'''
Fill in the code to your right which lets you give inputs, train the network, and keep track of the loss.

In this exercise, you will need to:
- Know the derivative of an activation function
- Be able to code out feedforward layers
- Be able to code out back-propagation
'''

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np

# Each row is a training example, each column is a feature  [X1, X2, X3]
#[Input code, X= ]
#[Input code, y= ]

# Activation function
#[Input code]

# Derivative of sigmoid
#[Input code]

# Class definition
class NeuralNetwork:
    def __init__(self, x,y):
        self.input = x
        self.weights1= np.random.rand(self.input.shape[1],4) # considering we have 4 nodes in the hidden layer
        self.weights2 = np.random.rand(4,1)
        self.y = y
        self.output = np. zeros(y.shape)

    def feedforward(self):
        #[Input code, self.layer1]
        #[Input code, self.layer2]
        return self.layer2

    def backprop(self):
        d_weights2 = np.dot([#Input code])
        d_weights1 = np.dot(#Input code], self.weights2.T *sigmoid_derivative(self.layer1))

        self.weights1 += d_weights1
        self.weights2 += d_weights2

    def train(self, X, y):
        self.output = self.feedforward()
        self.backprop()


NN = NeuralNetwork(X,y)
for i in range(1500): # trains the NN 1,000 times
    if i % 100 ==0:
        print ("for iteration # " + str(i) + "\n")
        print ("Input : \n" + str(X))
        print ("Actual Output: \n" + str(y))
        print ("Predicted Output: \n" + str(NN.feedforward()))
        print ("Loss: \n" + str(#[Input code, mean sum squared loss]
        )
        print ("\n")

    NN.train(X, y)
    
