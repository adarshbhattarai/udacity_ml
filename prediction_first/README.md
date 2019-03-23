
Naive Bayes Algorithm

python - Udacity Tutorial  Intro To Maching Learning

Supervised learning 

750 Dataset, Goal is to draw decision boundry out of scattered plot 


Getting Started with sklearn 

Google sklearn Naive Bayes 

Gaussian Naive Bayes

-- https://scikit-learn.org/stable/modules/naive_bayes.html

https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html


From Example on documentation 
-----------------------------

>>> import numpy as np
>>> X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
>>> Y = np.array([1, 1, 1, 2, 2, 2])
>>> from sklearn.naive_bayes import GaussianNB
>>> clf = GaussianNB()
>>> clf.fit(X, Y)
GaussianNB(priors=None, var_smoothing=1e-09)
>>> print(clf.predict([[-0.8, -1]]))
[1]
>>> clf_pf = GaussianNB()
>>> clf_pf.partial_fit(X, Y, np.unique(Y))
GaussianNB(priors=None, var_smoothing=1e-09)
>>> print(clf_pf.predict([[-0.8, -1]]))
[1]

#Go to folder
Command+Shift+G 




Adarsh
