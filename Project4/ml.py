
#Arunava Nag; CS 622 Project 4
#!/usr/bin/env python

import numpy as np
from sklearn.decomposition import PCA
from sklearn.tree import DecisionTreeClassifier as dt
from sklearn import tree
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.cluster import KMeans
import sys
import os
import random


def dt_train(X,Y):
  clf_dt = dt()
  # print(type(X))
  if isinstance(X, PCA):
    # X = X.explained_variance_ratio_
    #X = X.explained_variance_ratio_.reshape(-1,1)
    # print(X.ndim)
    # print(X[0])
    clf_dt = clf_dt.fit(X.components_, Y)
  else:
    clf_dt = clf_dt.fit(X,Y)

  # command line tree display
  # text_representation = tree.export_text(clf_dt)
  # print(text_representation)
  return clf_dt


def kmeans_train(X):
  kmeans = KMeans(n_clusters=2).fit(X)
  return kmeans
# def knn_train(X,Y,K):
# def perceptron_train(X,Y):
# def nn_train(X,Y, hls):


def pca_train(X,K):
  pca = PCA(n_components=K)
  PCA_learned = pca.fit_transform(X)
  return PCA_learned
  
def pca_transform(X,pca):
  learned_val = pca
  #fiting data with learned values
  p = PCA()
  X_tf = p.fit(X,learned_val)
  # print((X_tf.components_).ndim)
  #print(X_tf.explained_variance_ratio_)
  return X_tf.components_


# def svm_train(X,Y,k):

def model_test(X,model):
  #print(model)
  # if isinstance(model, tree.DecisionTreeClassifier):
  #   # X = X.explained_variance_ratio_
  #   # X = X.explained_variance_ratio_.reshape(-1,1)
  #   clf = model.predict(X.components_) 
  # else:
  #   clf = model.predict(X)
  clf = model.predict(X)
  return clf

  
def compute_F1(Y, Y_hat):
  # F1 = precision_score(Y, Y_hat, average=None, zero_division=1)
  TP = 0
  TN = 0
  FP = 0
  FN = 0
  for i in range(len(Y_hat)):
    if(Y_hat[i] == 0):
      Y_hat[i] = -1


  # print (Y_hat)
  for i in range(len(Y)):
    if Y[i] == 1 and Y[i] == Y_hat[i]:
      TP = TP + 1 
    elif Y[i] == -1 and Y[i] == Y_hat[i]:
      TN = TN + 1
    elif Y[i] == 1 and Y[i]!=Y_hat[i]:
      FP = FP + 1
    elif Y[i] == -1 and Y[i] == Y_hat[i]:
      FN = FN + 1

  P = TP / (TP+FP)
  R = TP / (TP+FN)
  F1 = (2*P*R)/(P+R)
  return F1
 




