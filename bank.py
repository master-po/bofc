#!/usr/bin/env python3

import requests
import xmltodict
import urllib.request
import ssl

url = "https://bankofcanada.ca/valet/observations/FXCADUSD/xml"
date = "2020-02-20"

context = ssl._create_unverified_context() #adding this to skip the SSL validation
file = urllib.request.urlopen(url, context=context) #open url
data = file.read() #contains data from the URL
data_xml =xmltodict.parse(data)

for item in data_xml['data']['observations']['o']:
   #print(item['@d'] + " => " + item['v']['#text'])
   if(item['@d'] == date):
      print("Conversion rate for " + date + " is " + item['v']['#text'])
   
   