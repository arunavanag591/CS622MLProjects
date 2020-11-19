
#Arunava Nag; CS 622 Project 3
#!/usr/bin/env python

import numpy as np
import sys
import matplotlib.pyplot as plt

def getWB(vectors):
    
    rows,column = vectors.shape
    arr = np.zeros(shape=(rows,3))
    support_vectors = np.zeros(shape=(rows,3))      
    labels=vectors[:,2]                             #array containing labels
    if labels[0]==1 and labels[1]==-1:              #always keep the positive label vector in position 0
        arr[0] =vectors[0]
        arr[1] = vectors[1]
    else:
        arr[0] =vectors[1]
        arr[1] = vectors[0]
        
    support_vectors=arr
    arr = arr[:,[0,1]]                              #drop label column
    #calculate direction, gamma
    direction = arr[0]-arr[1]
    gamma = (np.linalg.norm(arr[0] - arr[1]))/2
    norm_dir=(np.sqrt(np.square(direction[0])+np.square(direction[1])))
    #get weight and bias
    w = (direction/norm_dir)*(1/gamma)
    b = -1 - np.dot(w,arr[1])
    return w,b,support_vectors

    
def closestpoints(points):
    dist=[]
    origin = np.array((0,0))     
    for i in range(len(points)):
        dist.append(np.linalg.norm(origin - points[i])) #computing distance 
    k = 2
    idx = np.argpartition(dist, k)[:k]                  #sorting by distance
    return idx
    
def svm_train_brute(data):
    
    rows, columns = data.shape 
    points = np.zeros(shape=(rows, 2))
    points[:, 0], points[:, 1] = data[:, 0], data[:, 1] #list containing only features
    dist = closestpoints(points)                        #get index to closest points to origin
    vectors = data[dist,]                               #get closes points
    w,b,S = getWB(vectors)                              #get weight , bias and Support vectors
    return w,b,S