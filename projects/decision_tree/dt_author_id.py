#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#Quiz 2) Number of features in data
#the data is organized into a numpy 
#array where the number of rows is the 
#number of data points and the number of 
#columns is the number of features
print len(features_train[0])
#Ans : 3785

#Quiz 3)
#go into ../tools/email_preprocess.py, and find the line of code that looks like this:
#selector = SelectPercentile(f_classif, percentile=10)
#Change percentile from 10 to 1 , and rerun dt_author_id.py. What's the number of features now?
#Ans : 379

#Quiz 4) Accuracy when percentile is 1%
# Ans: 0.963594
#########################################################
### your code goes here ###
##Finding the accuracy
##first get the decision tree classifier(DecisionTreeClassifier). with minimum sample split of 40
#1. Quiz ) Calculate Accuracy
# Ans: 0.974
from sklearn import tree
clf = tree.DecisionTreeClassifier(min_samples_split=50)
clf.fit(features_train,labels_train)
accuracy = clf.score(features_test,labels_test)

print accuracy

#########################################################


