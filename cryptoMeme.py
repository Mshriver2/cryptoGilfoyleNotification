import json
import http.client
import time
from playsound import playsound
import subprocess
from subprocess import call

print("Enter coin full name: ")

userCoin = input()

print("\nEnter time interval to monitor in mins: ")

userMins = input()

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

    if sumValues >= 1.001:
        print("%s increased by 1 percent+ in the last %s mins!" % (userCoin, userMins))
        playsound("cash.wav")

        percentValue = (sumValues * 100) - 100

        bashCommand = 'Hello mother fucker, " + userCoin + " is down " + str(percentValue) + " percent in the last 30 mins'

        call(["espeak", bashCommand, "--stdout | paplay"])

        # plays voice audio
        # process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        # output, error = process.communicate()

    elif sumValues <= 0.999:
        print("%s decreased by 1 percent+ in the last %s mins!" % (userCoin, userMins))
        playsound("suffer.wav")

        percentValue = (1 - sumValues) * 100
        bashCommand = 'Hello mother fucker, " + userCoin + " is down " + str(percentValue) + " percent in the last 30 mins'


        call(["espeak", bashCommand, "--stdout | paplay"])
        # plays voice audio
        #process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        #output, error = process.communicate()
    else:
        print("%s did not increase or decrease by 1 percent+ in the last %s mins!\n" % (userCoin, userMins))

    print("sumValues equals %s" % (sumValues))

