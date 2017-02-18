#!/usr/bin/env python

from os import name
from bs4 import BeautifulSoup
import requests

#url = raw_input("Url : ")
url = "azalflooring.com"

# create a request 
r = requests.get("http://"+url)

# get the source page from html
data = r.text

# check the Os System if windows or Linux
if(name == "nt"):
    soup = BeautifulSoup(data, "html.parser")
else:
    soup = BeautifulSoup(data, "lxml")

# take all a link from this site
for link in soup.find_all("a"):
    print(link.get("href"))
