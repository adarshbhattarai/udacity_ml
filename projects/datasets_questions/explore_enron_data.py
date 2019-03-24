#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

#1) How many data points (people) are in the dataset? 146
no_of_dataset = len(enron_data)
print no_of_dataset

########################################################################################
########################################################################################

#2) For each person, how many features are available?
first_person = enron_data.keys()[0]
first_person_features = enron_data.get(first_person)
no_of_features = len(first_person_features)
print no_of_features


########################################################################################
########################################################################################


"""
3) The 'poi' feature records whether the person is a person of interest
according to our definition. How many POIs are there in the E+F dataset?
In other words, count the number of entries in the dictionary where  data[person_name]["poi"]==1

Ans-> 18
"""
count=0
for name,data in enron_data.iteritems():
	if data["poi"]==1:
		count +=1
		#print name


print count


########################################################################################
########################################################################################

"""
4) 
We compiled a list of all POI names 
(in ../final_project/poi_names.txt) and associated email 
addresses (in ../final_project/poi_email_addresses.py).

How many POIs were there total? 
(Use the names file, not the email addresses, 
since many folks have more than one address and a few didnt work for Enron, so we dont have their emails.)

Ans=> 35
"""

poi_names = open("../final_project/poi_names.txt","r")
print sum(1 for line in  poi_names)


########################################################################################
########################################################################################

"""
5)
As you can see, we have many of the POIs in our E+F dataset, but not all of them. 
Why is that a potential problem?

We will return to this later to explain how a POI could end up not being in the Enron E+F dataset,
so you fully understand the issue before moving on.

Ans)
There are a few things you could say here, 
but our main thought is about having enough data to really learn the patterns. 
 In general, more data is always better--only 
 having 18 data points doesn't give you that many examples to learn from.
"""

########################################################################################
########################################################################################


"""
6)
Like any dict of dicts, individual people/features can be accessed like so:

enron_data['LASTNAME FIRSTNAME']['feature_name']
or, sometimes 
enron_data['LASTNAME FIRSTNAME MIDDLEINITIAL']['feature_name']

What is the total value of the stock belonging to James Prentice?

Ans -> 1095040
"""
print enron_data['PRENTICE JAMES']['total_stock_value']


########################################################################################
########################################################################################

#7) How many email messages do we have from Wesley Colwell to persons of interest?
#Ans->11
print enron_data['COLWELL WESLEY']["from_this_person_to_poi"]

#8)Whats the value of stock options exercised by Jeffrey K Skilling?
#He Funcking earns a fucking lot {'salary': 1111258}
#Ans-> 'exercised_stock_options': 19250000
print enron_data['Skilling Jeffrey K'.upper()]['total_stock_value']
#

"""
#9)
Which of these schemes was Enron not involved in?

involved     ->selling assets to shell companies at the end of each month, and buying them back at the beginning of the next month to hide accounting losses
involved     ->causing electrical grid failures in California
Not Involved ->illegally obtained a government report that enabled them to corner the market on frozen concentrated orange juice futures
Not Involved ->conspiring to give a Saudi prince expedited American citizenship
Involved     ->a plan in collaboration with Blockbuster movies to stream movies over the internet

"""
#Who was the CEO -> Skilling Jeffrey K
#board of director ->LAY KENNETH L
#CFO? Andrew Fastow
##print enron_data['LAY KENNETH L'.upper()]
"""
Of these three individuals (Lay, Skilling and Fastow), who took home the most money (largest value of 'total_payments' feature)?
How much money did that person get?

103559793 LAY KENNETH L
"""
max_per="FASTOW ANDREW S,LAY KENNETH L,Skilling Jeffrey K"
max_money=0;
max_person_name=""
for data in max_per.split(","):
	money = enron_data[data.upper()]['total_payments']
	if( max_money <  money ):
		max_money=money
		max_person_name=data

print max_money,max_person_name		





########################################################################################
########################################################################################

##10
#For nearly every person in the dataset, not every feature has a value. How is it denoted when a feature doesn't have a well-defined value?
#Ans-> NaN

##11_
#How many folks in this dataset have a quantified salary? What about a known email address?
#95, 111

quantified_salary_count=0
known_email_count=0;
for name,data in enron_data.iteritems():
	if data["salary"]!='NaN':
		quantified_salary_count +=1
	if data["email_address"] !='NaN':
		known_email_count +=1	


print quantified_salary_count,known_email_count



########################################################################################
########################################################################################
"""
A python dictionary can't be read directly 
into an sklearn classification or regression algorithm;
 instead, it needs a numpy array or a list of lists 
 (each element of the list (itself a list) is a data point, 
 and the elements of the smaller list are the features of that point).

We've written some helper functions (featureFormat() and targetFeatureSplit() in tools/feature_format.py) 
that can take a list of feature names and the data dictionary, and return a numpy array.

In the case when a feature does not have a value for a particular person,
 this function will also replace the feature value with 0 (zero).

"""

import sys

sys.path.append('../tools')

import feature_format 

#def featureFormat( dictionary, features, remove_NaN=True, remove_all_zeroes=True, remove_any_zeroes=False, sort_keys = False):

#first_person = enron_data.keys()[0]

features=enron_data[first_person].keys()
remove_email_address=features.pop(len(features)-2)

helper=feature_format.featureFormat(enron_data,features,1,1,0,0)
#print helper




########################################################################################
########################################################################################
#12
#How many people in the E+F dataset (as it currently exists) have "NaN" for their total payments? 
#What percentage of people in the dataset as a whole is this?
#ans-> 14.38%
#13
#How many POIs in the E+F dataset have "NaN" for their total payments? What percentage of POI's as a whole is this?
#0%
#14
#If a machine learning algorithm were to use total_payments as a feature,
# would you expect it to associate a 'NaN' value with POIs or non-POIs?
#ans->non-poi ==> 0%

#15
#If you added in, say, 10 more data points which were all POI's, and put "NaN" for the total payments for those folks, 
#the numbers you just calculated would change.
#What is the new number of people of the dataset? What is the new number of folks with "NaN" for total payments?
#Ans->31,156

#16
#What is the new number of POI's in the dataset?  ANs -> prevPoi + 10 =>18+10=28 
#What is the new number of POI's with NaN for total_payments? =>10

#17
#Once the new data points are added, 
#do you think a supervised classification algorithm might interpret 
#"NaN" for total_payments as a clue that someone is a POI? => Yes



NaN_tpayment_count=0
POI_NAN_CNT=0
for name,data in enron_data.iteritems():
	if data["total_payments"]=='NaN':
		if data["poi"]:
			POI_NAN_CNT+=1
		NaN_tpayment_count +=1
				
totalSize=len(enron_data)

print float(NaN_tpayment_count*100)/totalSize
print float(POI_NAN_CNT*100)/totalSize
print "Total Payment with nan  is" 
print NaN_tpayment_count + 10
print "Total Size is" 
print totalSize +10



########################################################################################
########################################################################################




"""
Adding in the new POI's in this example, 
none of whom we have financial information for, 
has introduced a subtle problem, that our lack of financial 
information about them can be picked up by an algorithm as a 
clue that they're POIs. Another way to think about this is that 
there's now a difference in how we generated the data for our two 
classes--non-POIs all come from the financial spreadsheet, 
while many POIs get added in by hand afterwards. 
That difference can trick us into thinking we have better
performance than we do--suppose you use your POI detector to decide whether a new,
unseen person is a POI, and that person isn't on the spreadsheet. 
Then all their financial data would contain "NaN"
but the person is very likely not a POI (there are many more non-POIs than POIs in the world, 
and even at Enron)--you'd be likely to accidentally identify them as a POI, though!

This goes to say that, when generating or augmenting a dataset,
you should be exceptionally careful if your data are coming 
from different sources for different classes.
It can easily lead to the type of bias or mistake that we showed here. 
There are ways to deal with this, for example, you wouldn't have to worry 
about this problem if you used only email data--in that case, 
discrepancies in the financial data wouldn't matter because financial features aren't being used.
There are also more sophisticated ways of estimating how much of an effect 
these biases can have on your final answer; those are beyond the scope of this course.

For now, the takeaway message is to be very careful about introducing
features that come from different sources depending on the class! 
It's a classic way to accidentally introduce biases and mistakes.
"""

