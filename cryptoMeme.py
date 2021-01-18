import json
import http.client
import time
from playsound import playsound

while 1==1:

    conn = http.client.HTTPSConnection("coingecko.p.rapidapi.com")

    headers = {
    	'x-rapidapi-key': "42156fcddamsh575c2daee92d80bp13270fjsna33ad3dea85d",
    	'x-rapidapi-host': "coingecko.p.rapidapi.com"
    	}

    conn.request("GET", "/simple/price?ids=dogecoin&vs_currencies=usd&include_24hr_change=true", headers=headers)

    res = conn.getresponse()
    data = res.read()

    jsonData = json.loads(data)

    cryptovalue1 = (jsonData["dogecoin"]["usd"])

    time.sleep(600)


    conn = http.client.HTTPSConnection("coingecko.p.rapidapi.com")

    headers = {
    	'x-rapidapi-key': "42156fcddamsh575c2daee92d80bp13270fjsna33ad3dea85d",
    	'x-rapidapi-host': "coingecko.p.rapidapi.com"
    	}

    conn.request("GET", "/simple/price?ids=dogecoin&vs_currencies=usd&include_24hr_change=true", headers=headers)

    res = conn.getresponse()
    data = res.read()

    jsonData = json.loads(data)

    cryptovalue2 = (jsonData["dogecoin"]["usd"])

    sumValues = cryptovalue2 / cryptovalue1

    if sumValues >= 1.01:
        print("Dogecoin increased by 1%+ in the last 30 mins!")
        playsound("cash.wav")
    elif sumValues <= 0.99:
        print("Dogecoin decreased by 1%+ in the last 30 mins!")
        playsound("suffer.wav")
    else:
        print("Dogecoin did not increase or decrease by 1%+ in the last 30 mins!")

    print("sumValues equals %s" % (sumValues))

