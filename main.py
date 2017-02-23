#!/usr/bin/env python

from os import name
from bs4 import BeautifulSoup
import requests

#url = raw_input("Url : ")
url = "azal.com/main.html"

def crawl(url):
    
    r = requests.get("http://"+url)
    data = r.text
    

    if(name == "nt"):
        soup = BeautifulSoup(data, "html.parser")
        li_parser = link(soup)
        #print(li_parser)
        get_item_link(li_parser)
        
    else:
        soup = BeautifulSoup(data, "lxml")
        link(soup)
        
        

 

def link(soup):
    page = 0
    y = []
    for l in soup.find_all("a"):
        li = l.get("href")
        #fp = open(url+".txt","a")
        #fp.write(li+"\n")
        #fp.close()
        y.append(li)
        #print(y)
        page += 1
    return y
    
    

   
            

def get_item_link(x):
    page = 0
    try:
        for i in x:
            r = requests.get(i)
            data = r.text
            soup = BeautifulSoup(data, "html.parser")
            print(soup)
            page += 1
    except KeyboardInterrupt:
        print("Exit !!!")
        


if __name__=="__main__":   
    crawl(url)
    #get_item_link()
