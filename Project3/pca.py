
#Arunava Nag; CS 622 Project 3
#!/usr/bin/env python

import numpy as np
import sys


def compute_Z(arr, centering=True, scaling=False):
    rows, columns = arr.shape
    Z_mat = np.zeros(shape=(rows, columns))
    a=[]
    tempArray = np.zeros(rows)
   
    for column in range(columns):        
        mean = np.mean(arr[:,column])
        std = np.std(arr[:,column])        
        if (centering == True):
            for element in arr[:,column]:             
                tempArray = np.append(tempArray, (element - mean))
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
    idx = L.argsort()[::-1]
    L = L[idx] 
    PCS = PCS[:,idx]
    return L, PCS

def project_data(Z, PCS, L, k, var):
    if k>0:
        projection_matrix=PCS.T[:,:k]
    elif var>0:
        projection_matrix=PCS.T[:,:k]
   
    Z_star = np.dot(projection_matrix.T, Z).T
    return Z_star
