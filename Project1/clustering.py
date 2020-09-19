#!/usr/bin/env python
import numpy as np
import random
from scipy.spatial import distance
import math

def K_Means(X,K,mu):
    
    #when mu is empty generate random mu
    if len(mu)==0:
        mu = np.random.rand(2,1)
    #handing K value exceptions
    if (K == 0 or K < -1):
        raise Exception("K should be more than zero and positive")

    iterations =300
    for i in range(iterations):
        # classify based on the minimum distance.
        classifications = np.argmin(((X[:, :, None] - mu.T[None, :, :])**2).sum(axis=1), axis=1)
        # next, calculate the new centers for each cluster.
        new_mu = np.array([X[classifications == j, :].mean(axis=0) for j in range(K)])

        if (new_mu == mu).all():
            break
        else:
            mu = new_mu

          
    mu = np.array(mu , dtype=int)
    return mu
    

def K_Means_better(X, K):
    #choosing mu from the feature vector K
    mu = X[:K]
    if (K == 0 or K < -1):
        raise Exception("K should be more than zero and positive")

    iterations =300
    count = 0
    for i in range(iterations):
        # calculating minimum distance and clustering
        classifications = np.argmin(((X[:, :, None] - mu.T[None, :, :])**2).sum(axis=1), axis=1)
        # averaging to find new cluster centers
        new_mu = np.array([X[classifications == j, :].mean(axis=0) for j in range(K)])
        
        #performing several iterations to get the best mu
        if (new_mu == mu).all():
            count=count +1
            if (count==100):
                break
            else:
                continue
        else:
            mu = new_mu
   
    return mu
