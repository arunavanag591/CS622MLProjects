#!/usr/bin/env python

import numpy as np
import sys


def compute_Z(X, centering=True, scaling=False):
    rows, columns = X.shape
    Z_mat = np.zeros(shape=(rows, columns))
    tempArray = np.zeros(rows)
    for column in range(columns):        
        mean = np.mean(X[:,column])
        std = np.std(X[:,column])
        tempArray = np.empty(0)
        
        if (centering == True):
            # print("Centering\n")
            for element in X[:,column]:
                tempArray = np.append(tempArray, (element - mean))
        elif (scaling == True):
            # print("Scaling\n")
            for element in X[:,column]:
                tempArray = np.append(tempArray, (element / std))

    Z_mat[:,column] = tempArray
    return Z_mat

def compute_covariance_matrix(Z):
    return np.cov(Z.T)
    
def find_pcs(COV):
    L, PCS = np.linalg.eig(COV)
    #sort in descending
    idx = L.argsort()[::-1]
    L = L[idx] 
    PCS = PCS[:,idx]    
    #PCS_norm = (PCS/np.linalg.norm(PCS))
    return L, PCS

def project_data(Z, PCS, L, k, var):
    L_dim=[]
    PCS_dim=[]
    if k>0:
        projection_matrix = (PCS.T[:][:k]).T
    else:
        projection_matrix = (PCS.T[:][:var]).T
   
    Z_star = np.dot(Z,projection_matrix)
    return Z_star