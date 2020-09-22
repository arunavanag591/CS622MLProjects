import numpy as np
import math
import scipy.spatial
# import random.randint

def KNN_test(X_train,Y_train,X_test,Y_test,K):

	DD=[]
	D=[]
	for j in range (0,len(X_test)):
		for i in range (0,len(X_train)):
			d=scipy.spatial.distance.euclidean([X_train[i]],X_test[j])
			D.append(d)

	
	D=np.array_split(np.array(D), len(X_test))
	A= np.where(D[1] == D[1].min())[0:2]
	A=[]
	
	for r in range(0,len(X_test)):
		a=D[r].argsort()[:K]
		A.append(a)

	S=[]
	ss=[]
	
	for w in range (0,len(X_test)):
		SUM=0
		for e in range (0,K):
			s=(Y_train[A[w][e]])

			SUM=SUM+s

		if SUM==0:
			SUM='take more points'
		elif SUM<0:
			SUM=-1
		elif SUM>0:
			SUM=1
		S.append(SUM)

	TP=0
	TN=0
	FP=0
	FN=0
	for u in range (0,len(S)):
		if S[u]==Y_test[u] and S[u]==1:
			TP+=1
		elif S[u]==Y_test[u] and S[u]==-1:
			TN+=1
		elif S[u]!=Y_test[u] and S[u]==1:
			FP+=1
		elif S[u]!=Y_test[u] and S[u]==-1:
			FN+=1

	Acc=(TP + TN)/float(TP + TN + FP + FN)
	return(Acc)

def choose_K(X_train,Y_train,X_test,Y_test):
	
	acc=[]
	for K in range(1,len(X_test)):

		DD=[]
		D=[]
		for j in range (0,len(X_test)):
			for i in range (0,len(X_train)):
				d=scipy.spatial.distance.euclidean([X_train[i]],X_test[j])
				D.append(d)

		D=np.array_split(np.array(D), len(X_test))
		A= np.where(D[1] == D[1].min())[0:2]
		A=[]
		
		for r in range(0,len(X_test)):
			a=D[r].argsort()[:K]
			A.append(a)

		S=[]
		ss=[]
		
		for w in range (0,len(X_test)):
			SUM=0
			for e in range (0,K):
				s=(Y_train[A[w][e]])
				
				SUM=SUM+s

			if SUM==0:
				SUM='take more points'
			elif SUM<0:
				SUM=-1
			elif SUM>0:
				SUM=1
			S.append(SUM)
				
		TP=0
		TN=0
		FP=0
		FN=0
		for u in range (0,len(S)):
			if S[u]==Y_test[u] and S[u]==1:
				TP+=1
			elif S[u]==Y_test[u] and S[u]==-1:
				TN+=1
			elif S[u]!=Y_test[u] and S[u]==1:
				FP+=1
			elif S[u]!=Y_test[u] and S[u]==-1:
				FN+=1

		Acc=(TP + TN)/float(TP + TN + FP + FN)
		acc.append(Acc)
		print(Acc)
		accmax=np.where(acc==np.max(acc))+np.ones(len(np.where(acc==np.min(acc))))

	return(accmax)

	







