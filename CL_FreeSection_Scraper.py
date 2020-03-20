from bs4 import BeautifulSoup
from datetime import datetime
import requests
import time
import smtplib
from config import *
 
Free_CL_URL = "https://newyork.craigslist.org/d/free-stuff/search/zip"

def crawlFree(pageval):
#crawls the free items section and parses HTML
 if pageval == 0:
  r = requests.get(Free_CL_URL).text
  soup = BeautifulSoup(r,'html.parser')
 else:
   r = requests.get(Free_CL_URL+"?s="+str(pageval)).text
   time.sleep(1)
   soup = BeautifulSoup(r, 'html.parser')
 return soup

def searchItems(input):
#in each page crawled from crawlFree , extract the titles, lower the character case and compare against search strings to append a result list 
 itemlist = []
 for i in input:
  TitleSplit = str(i.contents[0]).split()
  TitleSplit = str([TitleSplit.lower() for TitleSplit in TitleSplit])

  if "piano" in TitleSplit:
      print(str("\n"+i.contents[0]))
      itemlist.append(i.contents[0])
      print((i.attrs['href']))
      itemlist.append(i.attrs['href'])
  elif "tv" in TitleSplit:
      print(str("\n"+i.contents[0]))
      itemlist.append(i.contents[0])
      print((i.attrs['href']))
      itemlist.append(i.attrs['href'])
  elif "watch" in TitleSplit:
      print(str("\n"+i.contents[0]))
      itemlist.append(i.contents[0])
      print((i.attrs['href']))
      itemlist.append(i.attrs['href'])

 return itemlist

pageval = 0
totalist = []

while True:
 time.sleep(0.2)
 soup = crawlFree(pageval)
#crawl paege until you hit a page with the following text, signifing the end of the catagory
 if "search and you will find" and "the harvest moon wanes" in soup.text:
  print("\nEnd of Script")
  break
 else:
  print("\nSearching page " + str((int(pageval / 120))))
  links = soup.find_all('a', class_="result-title hdrlnk")
  itemlist = searchItems(links)
  totalist.append(itemlist)

  pageval += 120

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

#message compliation and delivery 
message = "Subject:CL Free Bot Report - "+str(len(totalist))+"\n\n"

for i in totalist:
     for i in i:
        message += str("\n"+str(i)+"\n")

s = smtplib.SMTP('smtp.office365.com', 587)
s.starttls()
s.login(sender_email, password)
s.sendmail(sender_email, reciver_email,message.encode("utf-8"))
print(message)
print("sent mail")
s.quit() 


