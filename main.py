#!/usr/bin/env python

from os import name
from bs4 import BeautifulSoup
import requests
import urllib3.contrib.pyopenssl
import certifi
import urllib3

#For SSL Certificate
urllib3.contrib.pyopenssl.inject_into_urllib3()
http = urllib3.PoolManager(cert_reqs="CERT_REQUIRED",ca_certs=certifi.where())

#url = raw_input("Url : ")
search = str(raw_input("What do you want to search in Google : "))

def crawl(search):
    try:
        page = 0
        while True :
            r = http.request("GET","https://www.google.com/search?q={}&start={}0&*".format(search,page))
            data = r.data
            
            if(name == "nt"):
                soup = BeautifulSoup(data, "html5lib")
                #print(soup)
                link(soup)
            else:
                soup = BeautifulSoup(data, "lxml")
                #print(soup)
                link(soup)
            print("For page : {}".format(page))
            page += 1
            
           
    except KeyboardInterrupt:
        print("Exit!!!")
    
        

        
def link(soup):
   
    try:
        
        for l in soup.find_all("h3",{"class":"r"}):
            for x in l.findAll("a"):
                y = x.get("href")
                print(y)
                link_to_crawl = http.request("GET","https://www.google.com{}".format(y))
                print(link_to_crawl.status)
                #data = link_to_crawl.data
                #soup = BeautifulSoup(data, "html5lib")
                #for x in soup.findAll("a"):
                   # y = x.get("href")
                    #print(y)
           
           
            
    except KeyboardInterrupt:
        print("Exit!!!")
        
    
    
  

if __name__=="__main__":
    
    
    crawl(search)
    
