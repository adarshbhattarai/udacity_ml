SVM
Support Vector Machine



Machine learns Non linear decision surface . Ex

             -----
 X          |     |
 Y          | SVM | -->LABEL
 X--> X2+Y2 |     |
             -----

 in z plane the circle is linear, calculation based on distance of radius. Points out of circle have higher z(radius) and the points inside the circle have lower z (radius) . 
 So, a linear line can be drawn to predict


   Z = X2 + Y2 
    |
    | ...  ...  . . . 
    |. . .  . .    . .
    | --------------------  <-- Seperation.
    | .  .  .  .   .
    | . .   .  . . .
    ------------------------- 

 Amazing!!

 Kernel 
 ______

X, Y 			----Kernel--> X1X2X3X4X5
Non Separable  					Separable

Non Linear Separation <----	    Solution


SVM->from sklearn.svm import SVC ## Support Vector Classifier
clf = SVC(kernel="linear", gamma = 1000)

kernel can be, linear, rbf, poly, sigmoid and +others
gamma has no effect of linear line ,
gamma - > defines how far the influence of a single training example reaches, 
			low value--> far , high value --> close,
			near value are only taken into consideration if gamma is high.
			Far values are also taken into consideration if gamma is low.
			when drawing a decision boundary
C -> Controls the tradeoff between smooth decision boundary and classifying training points correctly

               ---------
             /           \
            /             \
           /  STOP Over    \
           \   Fitting     /  -> Make the decision boundry as linear as possible.
            \             /
             \           /
               ---------  


Naive Bayes is great for text--it’s faster and generally gives better performance than an SVM for this particular problem. Of course, there are plenty of other problems where an SVM might work better. Knowing which one to try when you’re tackling a problem for the first time is part of the art and science of machine learning. In addition to picking your algorithm, depending on which one you try, there are parameter tunes to worry about as well, and the possibility of overfitting (especially if you don’t have lots of training data).

Our general suggestion is to try a few different algorithms for each problem. Tuning the parameters can be a lot of work, but just sit tight for now--toward the end of the class we will introduce you to GridCV, a great sklearn tool that can find an optimal parameter tune almost automatically.
