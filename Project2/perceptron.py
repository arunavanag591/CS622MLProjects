#!/usr/bin/env python
import numpy as np

def train(X, label, weights):
    summation = np.dot(X, weights[1:]) + weights[0]
    return 1.0 if summation*label > 0.0 else 0.0

def perceptron_train(X,Y):
    weights = np.zeros(X.ndim + 1)
    iter = 10
    for _ in range(iter): 
        for data, label in zip(X, Y):
            prediction = train(data, label, weights)
            if prediction == 0:
                weights[1:] += (label - prediction) * data
                weights[0] += (label - prediction)
            else:
                continue
    return weights[1:] , weights[0]

        
def test(X, label, weights):
    summation = np.dot(X, weights[0:2]) + weights[2]
    return label if summation*label > 0.0 else 0.0

def perceptron_test(X,Y,w,b):
    weights = np.append(w, b)  
    labels = []
    correct = 0
    for data, label in zip(X, Y):
        labels.append(test(data, label, weights))
    
    for i in range(len(Y)):        
		if Y[i] == labels[i]:
			correct += 1  	
    return correct / float(len(Y))
    
    