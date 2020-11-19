 
CS 622
Project 3
Arunava Nag

The project has developed and tested in Python2.7 environment
Summary of Implementation (Code is documented inside the python files)

1. Principal Component Analysis
===============================

1.1 COMPUTE_Z
-------------
1. The first function compute_Z, where the data is extracted and used to find the mean and standard deviation each element
2. Then it is appened to a temporary array. 
3. Two cases where centering and scaling are handed in this phase. TO NOTE: Here as given in question centering = True and Scaling=False is passed 
to the function as shown in the question, which may not allow the user to pass environment arguments.
4. Finally the transpose of the appended data is store in to the Zmatrix and returned

1.2 COMPUTER_COVARIANCE_MATRIX
------------------------------
1. The Z matrix from previous function is taken and passed transposed to get ZT. 
2. Later the they are multiplied to return covariance


1.3 FIND_PCS
------------
1. The covariance is used find the eigen values and vectors
2. The values are sorted and PCS and L is returned

1.4 PROJECT_DATA
----------------
1. Using the eigen vector projection matrix is found based on the value of k or cumulative variance
2. The dot product of the projection matrix with Z is found and transpose of that is returned as projection matrices.


2. Binary Classifcation
=======================

Note: I did not require the helper functions.
It only works for first three test cases

2.1 SVM_TRAIN_BRUTE
===================
1. This is the main function which takes in the data and segments the features and labels.
2. It is then passed to the function closest points which returns the closest points from origin
3. Taking which as support vectors they are passed to function getWB where the direction, and gamma is found.
4. Using those valuse W and B is calculated and returned.

This script could be further improved to handle more cases, by using the concepts of lines and perpendicular bisectors and slopes to fit more lines.
However all these are already defined under sklearn library and makes it extremely easy to find hyperplanes.

