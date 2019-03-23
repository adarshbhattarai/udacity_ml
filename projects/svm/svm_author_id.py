#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

clf = SVC(kernel = "rbf", C=10000)

#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]
t0 = time()
clf.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"
t1 = time()
pred = clf.predict(features_test)
##checking the prediction for 10th data in training set
count=0

for i in pred:
	if i == 1 :
		count = count + 1;


print "Number of emails send by chris is", count

print "Total is ", len(pred)
print "Diff" , len(pred) - count		
print pred[10]
##checking the prediction for 10th data in training set

print pred[26]
##checking the prediction for 10th data in training set

print pred[50]
print "Prediction time:", round(time()-t1, 3), "s"
acc = accuracy_score(pred, labels_test)

print acc


#########################################################


