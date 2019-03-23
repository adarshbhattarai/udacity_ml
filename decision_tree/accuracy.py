import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData
from classifyDT import classify

import numpy as np
import pylab as pl

from classifyDT import classify
from sklearn.metrics import accuracy_score

features_train, labels_train, features_test, labels_test = makeTerrainData()



#################################################################################


########################## DECISION TREE #################################



#### your code goes here
clf = classify(features_train,labels_train)
pred= clf.predict(features_test)


acc =  accuracy_score(pred,labels_test) ### you fill this in!
### be sure to compute the accuracy on the test set

print acc
    
def submitAccuracies():
  return {"acc":round(acc,3)}

