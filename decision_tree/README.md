Chapter 3
-----------

Decision Trees
---------------

Decision Trees use trick to let you do non linear decision making with simple linear decision surface. 

Ex.
Aasthu loves to swimming. Can she swim?
 			
 			
 			Sun
			^
			|  *  * *. * * .  .  .. 
			| *    * * * * . . .  . 
			| *  * * * * *.  . .  .
			|   *     *   *  *  * 
			| * *  *  * *   *   *
			| * * *    * *   * *
			 ---------------------> Temperature


			 Desicision Tree Allows you to ask multiple questions

			 isHighTemperature?
			  Yes/No

			  No ->  X
			  Yes -> Sunny ? No -> X | Yes -> can swim.



Min Samples Split =2 (default)
cannot split tree if the node value is 1. Overfits

Entropy
-------
Controls how DT decides where to split the data
definition: measure of impurity in a bunch of examples
in self driving example we considered bumpiness now a new variable is added speed limit.
If speed limit is enforced, everything is gonna be slow,  if it is not in effect, you can go fast if terrain is good.

So, if speed limit is taken into consideration, Speed limit has more purity in driving fast and slow
Grade
^
|.		!   .
|	.	!.      .      <--- Drives Slow
|	.	!	.
|X	X	! .   .
|	X	!	
-------------------> Speed limit enforced 

Entropy is the opposite of purity
All examples are in same class -> Entropy =0
Examples are evenly spread between classes, Entropy =1.0 (Maximal value)


Formula for Entropy
--------------------

entropy = Summation -E Pilog2(Pi)   -> Pi is the fraction of examples that are given in class i
 					i

 					So, sum over all the classes that are available


Ex: 1.1
 grade bumpiness speedlimit? speedOfVechile
 steep  bumpy		Yes			Slow
 Steep  smooth		Yes			Slow
 flat	bumpy		No 			Fast
 steep	smooth		No			Fast

 SpeedOfVechile -> ssff 
 how many nodes are slow -> 2
 How many examples? 4
 Pi-> fraction of slow examples -> 2/4 -> 0.5	
 Pfast -> 2/4 -> 0.5
 Entropy of Pi -> -(0.5*-1 + 0.5*-1 ) =1        (log2(1/2) -> -1)  
 Maximally impure state


 Information Gain
--------------------

information gain = entropy(parent) - [weighted average] entropy(children)

decision tree algorithm : maximizes information gain

Now, for the ex 1.1 above, the entropy was 1.
Now let's use information gain to decide which variable to use when splitting

-----------------------------------------------------------------------------------------	
-----------------------------------------------------------------------------------------

	1) Information gain on grade:
	Based On Grade:  
		
		parent node ssff -->SPlit based on grade, which will be steep and flat-> 
			 			ssff
			 	steep 		 flat		
			 		ssf    f --> Entropy 0 Everything will be fast here
  in ssf P(slow) = 2/3, P(fast) = 1/3
  Entropy = -2/3 log(2/3) - 1/3 log(1/3) =0.918
  			entropyOfChildren = 3/4 * 0.918(Entropy with ssf) + 1/4 * 0 (Entropy in flat branch)
  							= 0.688				... (i)		

>>> import math
>>> x=math.log(2/float(3),2)
>>> y=math.log(1/float(3),2)
>>> -2/float(3)*x - 1/float(3)*y
0.9182958340544896

Information Gain = Entropy of parent - WEIGHTED Sum of entropy of children
					= 1 - 0.688    ... from (i)
					=0.311 (Information Gain for a split in grade)

-----------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------

Based on Bumpyness

	Entropy Of Children -> sf(bumpy) = P(slow) 1/2, P(fast)=1/2   = -1/2*log(1/2) -1/2*log(1/2) = 1 
						-> sf(smooth) = P(slow) 1/2, P(fast)=1/2  = 1 similar as above
						Information Gain = 1 - 2/4*1 - 2/4*1
										 = 1-1=0

-----------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------

Based on Speed Limit
	Information gain = 1 perfect purity --> ss  ff ==> Entropy =0. 1- 0 -0 = 1

-----------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------

Bias Variance
--------------

A high bias machine learning algorithm is the one that practically ignores the data. It has no capacity to learn anything.  It is called bias. A bias car would be one that we can train, and no matter which way we train it, it doesnt do anything differently.
That is bad in ML but we can go to other extreme that is extremely perceptive to data, and it can only replicate it has seen before. That is extremely high variance algorithm.

The problem with it is, it will reach very poorly in situations it hasn't seen before because it doesn't have right bias to generalize new stuff. 

In reality we want something middle. We want an algorithm that has authority to generalize. But still very open to listen to data. 
Many such algorithm exists so, turn a knob to make it bias or it can be high variance.
Art of tilting that knob is the art of making machine learning amazing. 

--Sebastian Thrun


-----------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------





