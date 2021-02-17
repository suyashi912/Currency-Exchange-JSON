# Name : SUYASHI SINGHAL
# Roll No : 2019478
# Group : 9

import datetime
import urllib.request
link1 = "https://api.exchangeratesapi.io/latest"
link2 = "https://api.exchangeratesapi.io/2010-01-12"
link3 = "https://api.exchangeratesapi.io/history?start_at=2018-01-01&end_at=2018-09-01"


def getLatestRates():
        """
        Returns:
                a JSON string that is a response to a latest rates query.

                The Json string will have the attributes: rates, base and date (yyyy-mm-dd).
	"""
        url = urllib.request.urlopen(link1)
        data = url.read()
        d = str(data)
        return (d)
#urlopen() - Opens the given api as an object. It takes url of the webpage(latest rates query) as a string argument and returns a network object.
#read() - Reads the network object and returns the data as string.

def changeBase(amount, currency, desiredCurrency, date):
        """
        Parameters:
                amount: type int
                currency and desiredCurrency: type string (INR, USD, etc.)
                date : string “yyyy-mm-dd”
        Returns:
                a float value f.

	"""
        f = link2.rfind('/')
        #Editing the link to get data for specified date and currency
        link = link2[:f+1]+date+"?base="+currency
        url = urllib.request.urlopen(link)
        #Reading edited link of JSON and storing it as a string
        data1 = url.read()
        d = str(data1)
        B = d.find("}")
        d = d[:B+1]
        g = d.find(desiredCurrency)
        h = d.find(':',g)
        i = d.find(',',h)
        #value - it is the value of 1.0 original currency in terms of desired currency
        #net - it is the value of the amount of original currency in terms of desired currency 
        if(currency =="EUR" and desiredCurrency == "EUR"):
                value = 1.0
        else:
                value = float(d[h+1:i])
        net = amount*value
        return net

def printAscending(json):
        """ Output:
                the sorted order of the Rates 
                You don't have to return anything.

        Parameter:
                json: a json string to parse
        """
        url = urllib.request.urlopen(link1)
        #Reading link1 of JSON and storing it as a string
        data1 = url.read()
        json = str(data1)
        k = json.index(":")
        l = json.index("}")
        #converting sring into a dictionary using eval()
        d = eval(json[k+1:l+1])
        r = list()
        #converting dictionary into a list for sorting
        for x,y in d.items():
                a = [x,y]
                r.append(a)
        size = len(r)
        i = 0
        # sorting the list in ascending order
        while(i<size):
                for j in range(size-i-1):
                        if(r[j][1]>r[j+1][1]):
                                temp = r[j]
                                r[j] = r[j+1]
                                r[j+1] = temp
                i=i+1
        # printing the rates in ascending order using the sorted list 
        for k in range(size):
                print("1 EUR =",str(r[k][1]),str(r[k][0]))


def extremeFridays(startDate, endDate, currency):
        """
        Output:
                on which friday was currency the strongest and on which was it the weakest.
		You don't have to return anything.
		
	Parameters: 
                stardDate and endDate: strings of the form yyyy-mm-dd
                currency: a string representing the currency whose extremes you have to determine
        """

        p = link3.find("=")
        q = link3.index("=",p+1)
        e = link3.find("&")
        #Editing the link to get data for specified start date and end date
        l = link3[:p+1]+startDate+link3[e:q+1]+endDate
        url = urllib.request.urlopen(l)
        #Reading edited link of JSON and storing it as a string
        data1 = url.read()
        json2 = str(data1)
        lis = []
        # slicing the json string 
        x = json2.index("start_at")
        json2 = json2[:x]
        #date.fromisoformat() - returns a date corresponding to a date string in format "YYYY-MM-DD"(emitted by date.isoformat())
        start = datetime.date.fromisoformat(startDate)
        end = datetime.date.fromisoformat(endDate)
        day = datetime.timedelta(days=1)
        #loop going from start date to end date and checking for fridays
        #data for fridays is stored in the list 
        while(start!=end+day):
                x = datetime.date.isoformat(start)
                y = datetime.date.fromisoformat(str(start))
                if(x in json2 and y.weekday()==4):
                        m = json2.find(x)
                        C = json2.find(currency,m)
                        g = json2.find(":",C)
                        h = json2.find(",",C)
                        money = json2[g+1:h]
                        i = [x,money]
                        lis.append(i)
                start+=day
        size = len(lis)
        k = 0
        #sorting the list in ascending order
        while(k<size):
                for j in range(size-k-1):
                        if(lis[j][1]>lis[j+1][1]):
                                temp = lis[j]
                                lis[j] = lis[j+1]
                                lis[j+1] = temp
                k=k+1
        if(lis!=[]):
                print(currency,"was strongest on",lis[0][0]+". 1 Euro was equal to",lis[0][1],currency)
                print(currency,"was weakest on",lis[-1][0]+". 1 Euro was equal to",lis[-1][1],currency)
                
        else:
                print("No friday")
                

def findMissingDates(startDate, endDate):
        """
        Output:
                the dates that are not present when you do a json query from startDate to endDate
		You don't have to return anything.

	Parameters:
                stardDate and endDate: strings of the form yyyy-mm-dd
        """
        p = link3.find("=")
        q = link3.index("=",p+1)
        e = link3.find("&")
        #Editing the link to get data for specified start date and end date
        l = link3[:p+1]+startDate+link3[e:q+1]+endDate
        url = urllib.request.urlopen(l)
        #Reading edited link of JSON and storing it as a string
        data1 = url.read()
        json2 = str(data1)
        #slicing the json string 
        x = json2.index("start_at")
        json2 = json2[:x]
        start = datetime.date.fromisoformat(startDate)
        end = datetime.date.fromisoformat(endDate)
        day = datetime.timedelta(days=1)
        print("The following dates were not present:")
        #Loop is going from start date to end date and checking if the date is present in the json string or not
        #The ouput is inclusive of the start date and end date
        while(start!=end+day):
                x = datetime.date.isoformat(start)
                if(x not in json2):
                        print(x)
                start+=day
