#!/usr/bin/env python

import numpy as np
import sys
import matplotlib.pyplot as plt

# def distance_point_to_hyperplane(pt, w, b):
    
# def compute_margin(data, w, b):

# def svm_test_brute(w,b,x):

def calculateWB(vectors):
    w1 = vectors[:,0]
    w2 = vectors[:,1]
    y = vectors[:,2]
   
    
    
def closestpoints(points):
    dist=[]
    origin = np.array((0,0))     
    for i in range(len(points)):
        dist.append(np.linalg.norm(origin - points[i]))
        #dist.append(np.sqrt(np.sum(np.square(origin - points[i])))) 
    k = 2
    idx = np.argpartition(dist, k)[:k]
    return idx
    
# def find_largest_distance(point_pos, point_neg)
    
#     for i in range(len(point_pos)):
#         for j in range(len(point_neg)):
#             dist.append(np.linalg.norm(point_pos[i]-point_neg[j]))        

def svm_train_brute(data):
    
    rows, columns = data.shape 
    points_pos=np.zeros(shape=(5,2))
    points_neg=np.zeros(shape=(5,2))
    points_pos[:, 0], points_pos[:, 1] = data[0:5, 0], data[0:5, 1]
    points_neg[:, 0], points_neg[:, 1] = data[5:10, 0], data[5:10, 1]
    points[:, 0], points[:, 1] = data[:, 0], data[:, 1] #list containing only features
    dist = closestpoints(points)
    vectors = data[dist,]
   # w,b = calculateWB(vectors)
    margin = np.linalg.norm(a - b)
    gamma = margin/2
    print margin   
