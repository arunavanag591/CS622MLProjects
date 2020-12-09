
#Arunava Nag; CS 622 Project 4
#!/usr/bin/env python

import numpy as np
from sklearn.decomposition import PCA
from sklearn.tree import DecisionTreeClassifier as dt
from sklearn import tree
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import Perceptron
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
# from sklearn.metrics import f1_score
# from sklearn.metrics import precision_score
# from sklearn.metrics import precision_recall_fscore_support
# from sklearn.metrics import accuracy_score
import sys
import os
import random


def dt_train(X,Y):
  clf_dt = dt()
  clf_dt = clf_dt.fit(X,Y)

  # command line tree display
  # text_representation = tree.export_text(clf_dt)
  # print(text_representation)
  return clf_dt

def kmeans_train(X):
  kmeans = KMeans(n_clusters=2).fit(X)
  return kmeans

def knn_train(X,Y,K):
  clf = KNeighborsClassifier(n_neighbors=K)
  knn = clf.fit(X,Y)
  return knn

def perceptron_train(X,Y):
  clf = Perceptron(tol=1e-3, random_state=0)
  ppn_train = clf.fit(X,Y)
  return ppn_train

def nn_train(X,Y, hls):
  clf = MLPClassifier(solver='lbfgs', alpha=1e-3, hidden_layer_sizes=hls, random_state=1)
  nnt = clf.fit(X,Y)
  return nnt

def pca_train(X,K):
  pca = PCA(n_components=K)
  PCA_learned = pca.fit_transform(X)
  return PCA_learned
  
def pca_transform(X,pca):
  learned_val = pca
  #fiting data with learned values
  p = PCA()
  X_tf = p.fit(X,learned_val)
  return X_tf.components_


def svm_train(X,Y,k):
  clf = SVC(kernel=k)
  svm = clf.fit(X,Y)
  return svm

def model_test(X,model):
  clf = model.predict(X)
  return clf
  
def compute_F1(Y, Y_hat):
  TP = 0  #true positive
  FP = 0  #false positive
  FN = 0  #false negative
  
  # replacing zeros with -1 for later calculation
  for i in range(len(Y_hat)):
    if(Y_hat[i] == 0):
      Y_hat[i] = -1
  
  # calculate TP, FP, FN
  for i in range(len(Y)):
    if Y[i] == 1 and Y[i] == Y_hat[i]:
      TP = TP + 1 
    elif Y[i] == 1 and Y[i]!=Y_hat[i]:
      FP = FP + 1
    elif Y[i] == -1 and Y[i] != Y_hat[i]:
      FN = FN + 1

  Precision = TP / (TP+FP)
  Recall = TP / (TP+FN)
  # F1-measure
  F1 = (2 * Precision * Recall)/(Precision + Recall)

  # F1 = precision_recall_fscore_support(Y, Y_hat, average='binary')
  # F1 = accuracy_score(Y, Y_hat)
  # F1 = precision_score(Y, Y_hat, average='weighted')
  
  return F1
 




