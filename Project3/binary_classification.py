#!/usr/bin/env python

import numpy as np
import sys
import matplotlib.pyplot as plt

# def distance_point_to_hyperplane(pt, w, b):
# def compute_margin(data, w, b):
# def svm_test_brute(w,b,x):



def getWB(vectors):
    rows,column = vectors.shape
    arr = np.zeros(shape=(rows,2))
    arr[:, 0], arr[:, 1] = vectors[:, 0], vectors[:, 1]
    direction = arr[0]-arr[1]
    gamma = (np.linalg.norm(arr[0] - arr[1]))/2
    norm_dir=(np.sqrt(np.square(direction[0])+np.square(direction[1])))
    w = (direction/norm_dir)*gamma
    b = -1 - np.dot(w,arr[1])
    return w,b

    
def closestpoints(points):
    dist=[]
    origin = np.array((0,0))     
    for i in range(len(points)):
        dist.append(np.linalg.norm(origin - points[i]))
        #dist.append(np.sqrt(np.sum(np.square(origin - points[i])))) 
    k = 2
    idx = np.argpartition(dist, k)[:k]
    return idx
    
def svm_train_brute(data):
    
    rows, columns = data.shape 
    points = np.zeros(shape=(rows, 2))
    points_pos=np.zeros(shape=(5,2))
    points_neg=np.zeros(shape=(5,2))
    points_pos[:, 0], points_pos[:, 1] = data[0:5, 0], data[0:5, 1]
    points_neg[:, 0], points_neg[:, 1] = data[5:10, 0], data[5:10, 1]
    points[:, 0], points[:, 1] = data[:, 0], data[:, 1] #list containing only features
    dist = closestpoints(points)
    
    vectors = data[dist,]
    w,b = getWB(vectors)
    return w,b,vectors