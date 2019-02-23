def classify(features_train, labels_train):   
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier
    
    
    ### your code goes here!
    from sklearn.naive_bayes import GaussianNB
    clf=GaussianNB()
    clf.fit(features_train,labels_train)

    pred = clf.predict(features_test)
    

##now print the accuracy 
## accuracy = no of points classified correctly / all points (in test set)
## method 1 : write code that compares predictions to y_test , element_by_element
## methid 2 : sklearn accuracy . somthing on google 
 
    return clf
    
