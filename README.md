
Learning Objectives: 

1\. String operations in python. 

2\. Basic knowledge about JSON. Making URL queries and reading their output. 3. Basic sorting algorithms. 

4\. The concept of importing various modules in python. 

5\. Introduction to Currency Exchange Service. 

6\. Testing using unittest 

For this assignment, you have to access the data of currency exchange rates from the open source website https://exchangeratesapi.io/. You can access the data using the APIs (Application Programming Interfaces) given on the website. 

The data received will be in the form of JSON representation as shown below: 

{ 

 "base": "EUR", 

 "date": "2018-04-08", 

 "rates": { 

 "CAD": 1.565, 

 "CHF": 1.1798, 

 "GBP": 0.87295, 

 "SEK": 10.2983, 

 "EUR": 1.092, 

 "USD": 1.2234, 

 ... 

 } 

} 

Following are the APIs to use for this assignment. Click on these links to see what a JSON actually looks like. 

1\. https://api.exchangeratesapi.io/latest 

2\. https://api.exchangeratesapi.io/2010-01-12 

3\. https://api.exchangeratesapi.io/history?start_at=2018-01-01  &end_at=2018-09-01 

Note: Date Format : yyyy-mm-dd

If you enter an invalid query, you will get the following response: 

{"error":"time data 'message' does not match format '%Y-%m-%d'"} 

Python provides us with various sets of pre-defined functions which we can directly call to perform tasks. Such a set of functions is called a module. In order to use these functions, you will have to import it's corresponding module first. 

To get the data from the given APIs through python script, we use urllib.request module of python. You can use the following functions: 

1\. urlopen() : Opens the given api as an object. It takes URL of the webpage as an argument as string. It returns a network object for reading purposes. 2. read() : Reads the network object and returns the data as a string. Example : 

url = urllib.request.urlopen("https://api.exchangeratesapi.io/latest")  data = url.read() 

1\. Tasks 

For this task, maintain a file a1.py and implement the functions described below. Your primary goal in this assignment is to use the currency exchange service to write the following function: 

1.1. Latest Currency Exchange Rates Query 

Implement the following function: 

def getLatestRates(): 

""" Returns: a JSON string that is a response to a latest rates  query. 

The JSON string will have the attributes rates, base and date  (yyyy-mm-dd). 

"""

2\. Processing the Data 

Once you have implemented getLatestRates() correctly, you have the currency exchange data in the form of a string. Now you have to process it and apply String module functions (you don't need to import any modules for this) to perform the following tasks. 

In case you want to learn more about JSON data type you can refer to the guide on using json module to process the data encoded in JSON. However you will be using only String module functions for your work on this assignment. 

http://docs.pythonguide.org/en/latest/scenarios/json/ 

Note: You need to process the response using only string operation. Module json can not be used in this assignment. 

Task 1 

For this task, you have to use the second link to read the JSON and store the result as a string. Using this string, you have to implement the following function that takes the amount, original currency, desired currency and date and converts the amount of original currency to the desired currency on the specified date. 

You would have to edit the link in order to procure the data for the specified date. 

def changeBase(amount, currency, desiredCurrency, date):  # amount is of type int 

# currency and desiredCurrency are of type string (INR, USD  etc.) 

 # date is string "yyyy-mm-dd" 

 # return type is float 

For example, if 1 GBP = 100 INR, a function call of changeBase(250, "INR", "GBP", "2010-10-25") returns 2.5 (since 250 INR was equal to 2.5 GBP on 25th October 2010). 

Similarly, if 1 USD = 80 INR, a function call of changeBase(100, "INR", "USD", "2010-10-25") returns 1.25.

Task 2 

For this task, first, you have to get the json string of latest rates (using the first link) and then print them in ascending order based on the rates. 

def printAscending(json): 

""" Output: the sorted order of the Rates 

Parameter json: a json string to parse 

You don't have to return anything. 

""" 

A sample output is: 

![](https://lh6.googleusercontent.com/ym6R0Q5W4b5QfzqxNXxgNk49EXXXNpQlszcsdtF14OjpNzxg_pZcANoianyCYZma6zrmKLfYDsABdLhJwjUSQOzEP-QHw2j0Ak30rWrVx-_MfM5qthnsCNe-z8GlH63zRjdm_1-d)Task 3 

For this task, you will have to import datetime module of python. Using some functions of this module, you can get the day of the week on a particular date. For instance, the following code generates an output of 3. (Monday is 0, Tuesday is 1 and so on). This means that 15th August 2019 was a Thursday. 

import datetime 

date = datetime.datetime(2019, 8, 15) 

print(date.weekday())

Yow will be provided with a startDate and an endDate as strings (a sample date is: "2019-09-23" which represents 23rd September 2019. 

You have to edit the third link so as to get data ranging from startDate to endDate. Once you have this data, you have to tell that among all the Fridays that are present there, on which of them was a particular currency strongest and on which one was it the weakest. 

def extremeFridays(startDate, endDate, currency): 

""" Output: on which friday was currency the strongest   and on which was it the weakest 

 You don't have to return anything. 

 Parameters: stardDate and endDate are strings of   the form yyyy-mm-dd 

 currency is also a string representing the currency   whose extremes you have to determine 

""" 

Sample output is for the function call extremeFridays("2017-01-01", "2017-12-31", "INR") is: 

![](https://lh5.googleusercontent.com/ad3qoildTS8dDUD9PoXmy0bqDLODppsbd2QOLiWmWaRU8wkAD-dl8qn7cinbuIO-OTcwY1hJHTKwoHiZNlzyTqoXbD3-ooMREOZuc5CZhOGO1ZOCyw_eeJ6Q9ZbDu-S_9CXp9jqd)Note that both the dates in the above output are Fridays. 

Task 4 

Observe that when you retrieve data from link 2, all the dates in the given range are not present. Some dates are absent. In this task, you have to print the valid dates that are not present in the given range.

def findMissingDates(startDate, endDate): 

""" Output: the dates that are not present when you 

 do a json query from startDate to endDate 

 Parameters: stardDate and endDate are strings of   the form yyyy-mm-dd 

""" 

A sample output is: 

![](https://lh6.googleusercontent.com/9MIHz0IqdC3o5zIAPstH_wjA0-q2GHytKK5CjhR8ySepRHisXZSIP9GbsOgTrQGXFJkn8ATjDg6aFI-AWZPRyIJ6unEui9aoO7kMzVfAujN5JUs132U0ASY0Jq4KR1yg8CTi9HI5)3\. Testing 

Once you have correctly implemented the above functions, you have to test whether the code you have written is correct or not. 

You can do that by using the unittest module of python. To make things simple, you only have to test the changeBase function. A skeleton code has been provided to you and your job is to add multiple assert statements (you can add assertEqual, assertAlmostEqual, assertTrue etc. of your choice) to make sure that your function is working correctly. 

General Instructions 

1\. You must include your name and roll number as comments in both the files. 2. You must not change the name or input parameters of any function, you just have to write your code according to these parameters. You are free to make helper functions if you wish so. 

3\. Make sure the testcases you write are exhaustive (they must cover all the corner cases). You run the testing file in the same manner as any other python script

(python3 filename.py) 

4\. Your output should be in the same format as shown in the screenshots attached.
