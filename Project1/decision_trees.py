#!/usr/bin/env python
import numpy as np
import random
from scipy.spatial import distance
import math as m

def total_entropy(Y):
    length=len(Y)
    zeros = np.count_nonzero(Y==0)
    ones = np.count_nonzero(Y==1)    
    total_entropy = -(zeros/length)*m.log2(zeros/length) - (ones/length)*m.log2(ones/length)
    return total_entropy
    
    
def DT_train_binary(X,Y,max_depth):



'''
def DT_test_binary(X,Y,DT)
def DT_make_prediction()
​
def DT_train_real()
​
def DT_test_real()
'''
