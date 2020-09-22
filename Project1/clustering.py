#!/usr/bin/env python
import numpy as np
import random
from scipy.spatial import distance
import math


def choose_range(X):
    
    minimum=np.min(X)
    maximum=np.max(X)
    if minimum == 0:
        minimum=+1
    return int(minimum), int(maximum)

def K_Means(X,K,mu):
    
    #when mu is empty generate random mu
    if len(mu)==0:        
        val1,val2=choose_range(X) #find the lowest and highest for not overshooting values
        mu=random.sample(range(val1,val2), K) #generate mu based on K
        mu=np.reshape(mu, (K,1)) #reshaping array to 2D array
        mu = mu[mu[:,0].argsort()] #sorting the array to find difference
        if((mu[-1] - mu[0])==1 or (mu[-1] - mu[0])==2): #handling exceptions of close clusters
            mu[-1]=+3
         
    #handing K value exceptions
    if (K == 0 or K < -1):
        raise Exception("K should be more than zero and positive")

    iterations =300
    for i in range(iterations):
        # classify based on the minimum distance.
        clustering = np.argmin(((X[:, :, None] - mu.T[None, :, :])**2).sum(axis=1), axis=1)
        # next, calculate the new centers for each cluster.
        new_mu = np.array([X[clustering == j, :].mean(axis=0) for j in range(K)])
                  
        if (new_mu == mu).all():
            break
        else:
            mu = new_mu
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
        clustering = np.argmin(((X[:, :, None] - mu.T[None, :, :])**2).sum(axis=1), axis=1)
        # averaging to find new cluster centers
        new_mu = np.array([X[clustering == j, :].mean(axis=0) for j in range(K)])
        
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

