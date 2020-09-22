Decision Tree:
=============
DT TRAIN BINARY

>Total entropy is calculated
> Then the columns are used for calculating the information gain to get the first split, and the process is repeated for the getting the next splits 
by setting the depth of the tree to be 3
> Finally it is stored in a dictory and output is returned

Nearest Neighbors:
=================
KNN TEST 

>The input numpy arrays are taken into containeers with labels.
>Euclidean distances are computed between various points and the closest points are collected 
>The sum of the labels are calculated to find the total result for negative or positive classes.
>Accuracy is calculated based on the true positives and negatives and false positives and negatives predictions.

CHOOSE K 

>Same data handling done as above, however the goal of this function is to generate the best K for the most accuracy.
>Once the closest points are found as above, the accuracy is calculated over different K values
>Highest accuracy of the K is returned from those values.


Clustering:
==========

KMEANS CLUSTERING
Part 1: Where mu is defined

>The input vectors are taken and classified using the numpy library
>Once classified the minimum distances are found and stored in numpy array
>Check for if mu is equal to previous mu, if yes breaks returns as a value of the function


Part 2: Where mu is not defined

>Check for if the mu is passed as an input 
> If not generate using np.random.sample with a range between the highest and lowest values 
  to avoid nan values. Too far mu will lead to nan values as the distance will be closest to the smaller value always
  This step ensures there is a good distribution among the clusters
> Following this step same as above for clustering.

Exceptions Handled:

> Mu is generated based on size of K
> Mu generation range should not have zero , as it leads to nan values. The data was sorted and the min and max was used
to generate the mu values. If minimum was zero it was added to 1.
> The generated mu was reshaped to 2D array and also close mu values or similar mu values were tackled through
simple if statements
>Additionally K values were selected and checked for wether negative or 0 to throw exceptions.


KMEANS CLUSTERING AND GENERATING THE BEST MU 

Mu was selected from the data feature vection and clusters were formed using above approach,
following which the mu was checked with previous mu for several iterations. (submitting with 300 iterations, tested until 10000)
This made sure the mu has converged.