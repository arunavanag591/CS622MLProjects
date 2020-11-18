#!/usr/bin/env python

import numpy as np
import sys


def compute_Z(arr, centering=True, scaling=False):
    rows, columns = arr.shape
    Z_mat = np.zeros(shape=(rows, columns))
    tempArray = np.zeros(rows)
    for column in range(columns):        
        mean = np.mean(arr[:,column])
        std = np.std(arr[:,column])
        tempArray = np.empty(0)
        
        if (centering == True):
            for element in arr[:,column]:
                tempArray = np.append(tempArray, (element - mean))
        elif (scaling == True):
            for element in arr[:,column]:
                tempArray = np.append(tempArray, (element / std))

    Z_mat[:,column] = tempArray
    return Z_mat

def compute_covariance_matrix(Z):
    cov = np.cov(Z.T) / Z.shape[0]
    return cov
    
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