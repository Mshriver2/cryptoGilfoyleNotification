import json
import http.client
import time
from playsound import playsound
from subprocess import call

print("Enter coin full name: ")

userCoin = input()

print("\nEnter time interval to monitor in mins: ")

userMins = input()

print("\nEnter percentage to monitor (whole numbers only): ")

userPercentage = input()

while 1==1:

    conn = http.client.HTTPSConnection("coingecko.p.rapidapi.com")

    headers = {
    	'x-rapidapi-key': "42156fcddamsh575c2daee92d80bp13270fjsna33ad3dea85d",
    	'x-rapidapi-host': "coingecko.p.rapidapi.com"
    	}

    conn.request("GET", "/simple/price?ids=%s&vs_currencies=usd&include_24hr_change=true" % (userCoin), headers=headers)

    res = conn.getresponse()
    data = res.read()

    jsonData = json.loads(data)

    cryptovalue1 = (jsonData[userCoin]["usd"])

    # sleeps for the users desired interval 
    time.sleep(int(userMins)*60)


    conn = http.client.HTTPSConnection("coingecko.p.rapidapi.com")

    headers = {
    	'x-rapidapi-key': "42156fcddamsh575c2daee92d80bp13270fjsna33ad3dea85d",
    	'x-rapidapi-host': "coingecko.p.rapidapi.com"
    	}

    conn.request("GET", "/simple/price?ids=%s&vs_currencies=usd&include_24hr_change=true" % (userCoin), headers=headers)

    res = conn.getresponse()
    data = res.read()

    jsonData = json.loads(data)

    cryptovalue2 = (jsonData[userCoin]["usd"])

    sumValues = cryptovalue2 / cryptovalue1

    increasePercent = (int(userPercentage) / 100) + 1.0

    decreasePercent = abs((int(userPercentage) / 100) - 1.0)


    if sumValues >= increasePercent:
        
        playsound("cash.wav")

        percentValue = round(((sumValues * 100) - 100), 3)
        speakText = '"Hello mother fucker, ' + userCoin + ' is up ' + str(percentValue) + ' percent in the last 30 mins"'

        #speaks information using espeak, shell must be set to True because it is not working in an emulated environment
        call('espeak '+speakText+' --stdout | paplay', shell=True)

        print("%s increased by %s percent in the last %s mins!" % (userCoin, percentValue, userMins))

    elif sumValues <= decreasePercent:
        
        playsound("suffer.wav")

        percentValue = round((1 - sumValues) * 100, 3)
        speakText = 'Hello mother fucker, " + userCoin + " is down " + str(percentValue) + " percent in the last 30 mins'

        #speaks information using espeak, shell must be set to True because it is not working in an emulated environment
        call('espeak '+speakText+' --stdout | paplay', shell=True)

        print("%s decreased by %s percent in the last %s mins!" % (userCoin, percentValue, userMins))

    else:
        print("%s did not increase or decrease by 1 percent+ in the last %s mins!\n" % (userCoin, userMins))

    print("sumValues equals %s" % (sumValues))
