Enron Data Set
---------------


1) Person Of Interest:
what is it?
 i) May be some person who were indited -> person charged with crime 
 ii) perosn who settled without admitting guilt .
 iii) Testified in exchange for immunity

 list of person of interest can be extracted from this article.
 "https://usatoday30.usatoday.com/money/industries/energy/2005-12-28-enron-participants_x.htm"


Accuracy <=> training set size 
-------------------------------

For 1000 test data, put 800 into training set and 200 (Y) into a test set 

Divide 800 into 4 data sets 4 * 200

Test all this 4 different data sets in the same 200 (Y) test sets
accuracy
^
|             x(80%) ^(82%)
|        x(70%)  
|
|   x(55%)
| 
 ----------------------> Training Set Size
   200   400  600   800

--> What is says is, if the training set size is increases the accuracy is more better.

Download and Extract Enron DataSet
----------------------------------

We had downloaded it earlier, however if you havn't download it from 
"https://www.cs.cmu.edu/~./enron/enron_mail_20150507.tar.gz"

