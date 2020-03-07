#!/usr/bin/env python3

<<<<<<< HEAD
#different arbitray change added
=======
#arbitrary change re-added
>>>>>>> 72c29f3c649c9a79b421b303074c519ed96ecb25

import requests
import xmltodict

url = "https://bankofcanada.ca/valet/observations/FXCADUSD/xml"

response = requests.request("GET", url)

#print (response.text)

pyxml = xmltodict.parse(response.text)

#print ("-----------------\n", data)

date = pyxml["data"]["observations"]["o"]

print (date)
print (type(date))
print (type(pyxml))
