CS 622
Project 4
Arunava Nag

The project has developed and tested in Python3.8.5 and Python3.6.9 environment. The F1 measure answers vary across python versions.
Summary of Implementation (Code is documented inside the python files).

1. Utilities
=============

1.1 GENERATE_VOCAB
------------------
1. This function selects files from positive and negative folder based on the max_files parameter. 
2. After which it picks up all the words from every file in every line and store them as sets, based on if they are repeating 
equal or more than min count.
3. The vocab is then cleaned for special characters and br tags
4. Here filtering of the vocabulary could be done using a for loop but that increases the file complexity significantly,
hence a counter is imported alternatively to filter repeating words.

Note: Commented code for generating the files randomly is also present in the script

1.2 CREATE_WORD_VECTOR
------------------------------
1. Takes a filename and vocab list as input.
2. Uses sklearn countvectorizer to generate vector for every file based on vocab.

1.3 LOAD_DATA
------------
1. Uses the max file check conditions as generate-vocab and then uses create word vector to generate a vectorized list for positive
reviews and negative reviews.
2. This is then appeneded to one X vector with its corresponding labels.


2. Ml
------

2.1 PCA AND PCA_TRANSFORM
--------------------------
1. PCA is computed using sklearn pca functions and then sent for transforming with train vector and learned values for 
dimensionality reduction
2. It returns PCA component values.

2.2 ALL THE ML CLASSIFIERS
--------------------------
1. For all the classifiers such as decision tree, kmeans, knn, perceptron, neural network and and svm, sklearn functions have been
used to fit it for train data and labels and returned with the learned values. Hyperparamters are explored to get the best F1 measure.

2.3 MODEL TEST
--------------
1. Here all the learnt values from the Ml classifiers are tested and using sklearn predict function against the test data.

2.4 COMPUTE F1
--------------
1. In this function the labels generated versus the original labels are taken as input.
2. The generated labels and all expressed in either 1 or -1.
3. Using the true values and predicted values, F1-measure is calculated manually for consistency. Sklearn f1_score and precision 
score have been tested as well, however the end confidence keeps wavering between values.
4. The manual calculations are of Recall and Precision is verified with sklearn.precision_recall_fscore_support function.
5. Finally F1 measure is given out as final output for all the classfiers.