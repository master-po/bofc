#!/usr/bin/env python3

#arbitrary code for git testing

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
