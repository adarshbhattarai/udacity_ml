Chapter 6
----------

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

We had downloaded it earlier, however if you havn't download it. Download it from  
"https://www.cs.cmu.edu/~./enron/enron_mail_20150507.tar.gz"

Enron Mail Types of Data
------------------------

numerical   ==> Numbers
categorical ==> limited number of discrete values(category)
time series ==> temporal values(date, timestamp) 
text => words

Here, and in the rest of the quizzes in this part of the course, put a direct equivalence between temporal data and time series data. It should be noted that, technically, time series data is a special case of temporal data: not all data that has timestamps can be considered time series data. Time series data puts the temporal nature of the data first, and is concerned with the change in values of other variables over time. These relationships are gathered from measurements taken within a consistent frame, typically at regular intervals (e.g. hourly, daily, monthly). Simply because collected data has timestamps does not make it "time-series data". If the timestamps do not have a meaningful dependent relationship across data points, then this should not be considered time-series data in a broad sense.

Quiz 1) 
Salary info , why type of data is it? -> Numerical 

Quiz 2) 
Job title-> Categorical 
Quiz3)
Timestamps on emails-> Time series 
Quiz 4)
contents-> text
Quiz 5)
No of emails sent by a given person?->  Numerical 
Quiz 6)
To/From fields of emails  -> text

from enron dataset:
We are going to figure out who were the players , how much money were they making , who is sending emails to who, stuff like this.
We will navigate through data set and extract some informations J.


Mini-Project
--------------


"The Enron fraud is a big, messy and totally fascinating story about corporate malfeasance of nearly every imaginable type. The Enron email and financial datasets are also big, messy treasure troves of information, which become much more useful once you know your way around them a bit. We’ve combined the email and finance data into a single dataset, which you’ll explore in this mini-project."- Udacity


Getting started:



The aggregated Enron email + financial dataset is stored in a dictionary, where each key in the dictionary is a person’s name and the value is a dictionary containing all the features of that person.
The email + finance (E+F) data dictionary is stored as a pickle file, which is a handy way to store and load python objects directly. 
Use datasets_questions/explore_enron_data.py to load the dataset.

goto project/datasets_questions/explore_enron_data.py


Enron: The Smartest Guys in the Room - Watch this documentary

