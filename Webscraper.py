# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Required libraries...
#pip install requests
#pip install bs4
#pip install html
#pip install lxml

#Import libraries
import requests
from bs4 import BeautifulSoup

header=[]
tdata=[]
source = requests.get("https://en.wikipedia.org/wiki/Social_media") #Source
soup = BeautifulSoup (source.content, 'lxml')
div = soup.find("div", attrs ={"class":"mw-parser-output"})
table= div.find_all(["table"], attrs ={"class":"wikitable sortable"})
#print(table)
caption = table[0].caption.text.strip()
print(caption)
body = table[0].find("tbody")
tr=body.find_all('tr')
for i in tr:
  str=i.find_all('th')
  for j in str:
    head=j.text.strip()
    header.append(head)
#print(header)

for i in tr:
  data=list()
  str=i.find_all('td')
  for j in str:
    bod=j.text.strip()
    #print(bod)
    data.append(bod)
    if(j==str[len(str)-1]):
      tdata.append(data)
#print(tdata)

#Code to save scraped data
import csv  

with open('socialMedia.csv', 'w') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    for data in tdata:
      writer.writerow(data)
    #print("Data saved")