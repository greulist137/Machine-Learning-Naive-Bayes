#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
from sklearn.naive_bayes import GaussianNB
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.metrics import accuracy_score


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

gnb = GaussianNB()


gnb.fit(features_train, labels_train)
print("Prediction")
predictions = gnb.predict(features_test)
print(predictions)
print('Accuracy')
print(accuracy_score(labels_test, predictions))

