#!/usr/bin/env python
import numpy as np
import math
import scipy.spatial

def KNN_test(X_train,Y_train,X_test,Y_test,K):
    dst=[]
    True_Pos=0
    True_Neg=0
    False_Pos=0
    False_Neg=0
    sum_label=[]
    for j in range (0,len(X_test)):
      for i in range (0,len(X_train)):
        d=scipy.spatial.distance.euclidean([X_train[i]],X_test[j])
        dst.append(d)

    dst=np.array_split(np.array(dst), len(X_test))
    A=np.where(dst[1] == dst[1].min())[0:2]
    A=[]
    for r in range(0,len(X_test)):
      a=dst[r].argsort()[:K]
      A.append(a)
        
    for w in range (0,len(X_test)):
      count=0
      for e in range (0,K):
        s=(Y_train[A[w][e]])
        count=count+s
      if count==0:
        count='take more points'
      elif count<0:
        count=-1
      elif count>0:
        count=1
      sum_label.append(count)

    for u in range (0,len(sum_label)):
      if sum_label[u]==Y_test[u] and sum_label[u]==1:
        True_Pos+=1
      elif sum_label[u]==Y_test[u] and sum_label[u]==-1:
        True_Neg+=1
      elif sum_label[u]!=Y_test[u] and sum_label[u]==1:
        False_Pos+=1
      elif sum_label[u]!=Y_test[u] and sum_label[u]==-1:
        False_Neg+=1

    accuracy=(True_Pos + True_Neg)/float(True_Pos + True_Neg + False_Pos + False_Neg)
    return(accuracy)

def choose_K(X_train,Y_train,X_test,Y_test):
    acc=[]
    true_pos=0
    true_neg=0
    false_pos=0
    false_neg=0
    for K in range(1,len(X_test)):
      dst=[]
      for j in range (0,len(X_test)):
        for i in range (0,len(X_train)):
          d=scipy.spatial.distance.euclidean([X_train[i]],X_test[j])
          dst.append(d)

      dst=np.array_split(np.array(dst), len(X_test))
      A= np.where(dst[1] == dst[1].min())[0:2]
      A=[]
      
      for r in range(0,len(X_test)):
        a=dst[r].argsort()[:K]
        A.append(a)

      sum_label=[]
      for w in range (0,len(X_test)):
        count=0
        for e in range (0,K):
          s=(Y_train[A[w][e]])
          count=count+s
        if count==0:
          count='take more points'
        elif count<0:
          count=-1
        elif count>0:
          count=1
        sum_label.append(count)   
      
      for u in range (0,len(sum_label)):
        if sum_label[u]==Y_test[u] and sum_label[u]==1:
          true_pos+=1
        elif sum_label[u]==Y_test[u] and sum_label[u]==-1:
          true_neg+=1
        elif sum_label[u]!=Y_test[u] and sum_label[u]==1:
          false_pos+=1
        elif sum_label[u]!=Y_test[u] and sum_label[u]==-1:
          false_neg+=1

      Acc=(true_pos + true_neg)/float(true_pos + true_neg + false_pos + false_neg)
      acc.append(Acc)
      
      max_accuracy=np.where(acc==np.max(acc))+np.ones(len(np.where(acc==np.min(acc))))

    return(max_accuracy)

	


