#!/usr/bin/env python

import numpy as np
import sys


def compute_Z(arr, centering=True, scaling=False):
    rows, columns = arr.shape
    Z_mat = np.zeros(shape=(rows, columns))
    a=[]
    tempArray = np.zeros(rows)
    #print tempArray
    for column in range(columns):        
        mean = np.mean(arr[:,column])
        std = np.std(arr[:,column])
        #tempArray = np.empty(0)
        
        if (centering == True):
            for element in arr[:,column]:             
                tempArray = np.append(tempArray, (element - mean))
                #print tempArray
        elif (scaling == True):
            for element in arr[:,column]:
                tempArray = np.append(tempArray, (element / std))
    
    tempArray= np.trim_zeros(tempArray, 'f')
    Z_mat = np.reshape(tempArray,(columns,rows))
    return Z_mat

def compute_covariance_matrix(Z):
    ZT=np.transpose(Z)
    cov = np.dot(Z,ZT)
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
    if k>0:
        projection_matrix=PCS.T[:,:k]

    else:
        projection_matrix = Z.dot(PCS[:, :var])
   
    Z_star = np.dot(projection_matrix.T, Z).T
    return Z_star