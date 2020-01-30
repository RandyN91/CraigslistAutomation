from bs4 import BeautifulSoup
from datetime import datetime
import requests
import time
import smtplib

Free_CL_URL = "https://newyork.craigslist.org/d/free-stuff/search/zip"

def crawlFree(pageval):

 if pageval == 0:
  r = requests.get(Free_CL_URL).text
  soup = BeautifulSoup(r,'html.parser')
 else:
   r = requests.get(Free_CL_URL+"?s="+str(pageval)).text
   time.sleep(1)
   soup = BeautifulSoup(r, 'html.parser')
 return soup

def searchItems(input):
 itemlist = []
 for i in input:
  TitleSplit = str(i.contents[0]).split()
  TitleSplit = str([TitleSplit.lower() for TitleSplit in TitleSplit])
  #print(TitleSplit)
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
  elif "computer" in TitleSplit:
      print(str("\n"+i.contents[0]))
      itemlist.append(i.contents[0])
      print((i.attrs['href']))
      itemlist.append(i.attrs['href'])
  elif "boat" in TitleSplit:
      print(str("\n"+i.contents[0]))
      itemlist.append(i.contents[0])
      print((i.attrs['href']))
      itemlist.append(i.attrs['href'])
  elif "collection" in TitleSplit:
      print(str("\n"+i.contents[0]))
      itemlist.append(i.contents[0])
      print((i.attrs['href']))
      itemlist.append(i.attrs['href'])
  elif "antique" in TitleSplit:
      print(str("\n"+i.contents[0]))
      itemlist.append(i.contents[0])
      print((i.attrs['href']))
      itemlist.append(i.attrs['href'])
  elif "electronics" in TitleSplit:
      print(str("\n"+i.contents[0]))
      itemlist.append(i.contents[0])
      print((i.attrs['href']))
      itemlist.append(i.attrs['href'])
  elif "electric" in TitleSplit:
      print(str("\n"+i.contents[0]))
      itemlist.append(i.contents[0])
      print((i.attrs['href']))
      itemlist.append(i.attrs['href'])
  elif "truck" in TitleSplit:
      print(str("\n"+i.contents[0]))
      itemlist.append(i.contents[0])
      print((i.attrs['href']))
      itemlist.append(i.attrs['href'])
  elif "car" in TitleSplit:
      print(str("\n"+i.contents[0]))
      itemlist.append(i.contents[0])
      print((i.attrs['href']))
      itemlist.append(i.attrs['href'])
  elif "machine" in TitleSplit:
      print(str("\n"+i.contents[0]))
      itemlist.append(i.contents[0])
      print((i.attrs['href']))
      itemlist.append(i.attrs['href'])
  elif "instrument" in TitleSplit:
      print(str("\n"+i.contents[0]))
      itemlist.append(i.contents[0])
      print((i.attrs['href']))
      itemlist.append(i.attrs['href'])
  elif "old" in TitleSplit:
      print(str("\n"+i.contents[0]))
      itemlist.append(i.contents[0])
      print((i.attrs['href']))
      itemlist.append(i.attrs['href'])
  elif "jewelry" in TitleSplit:
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

 if "search and you will find" and "the harvest moon wanes" in soup.text:
  print("\nEnd of Script")
  s = smtplib.SMTP('smtp.office365.com', 587)
  s.starttls()
  s.login("randy.naraine@mail.citytech.cuny.edu", "g0$$iping")
  s.sendmail("randy.naraine@mail.citytech.cuny.edu", "randy.naraine64@gmail.com","Script Failure check Loops")
  break
 else:
  print("\nSearching page " + str((int(pageval / 120))))
  links = soup.find_all('a', class_="result-title hdrlnk")
  itemlist = searchItems(links)
  totalist.append(itemlist)

  pageval += 120

#print(totalist)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

message = "Subject: CL Free Scraper Bot Report "
message += str(current_time)+ \
              "\n"
for i in totalist:
    if i != []:
        for i in i:
         message += str(str(i)+"\n")
    else:
     message += str("No items found")

s = smtplib.SMTP('smtp.office365.com', 587)
s.starttls()
s.login("randy.naraine@mail.citytech.cuny.edu", "g0$$iping")
s.sendmail("randy.naraine@mail.citytech.cuny.edu", "randy.naraine64@gmail.com",message.encode('utf-8'))
print(message)
print("sent mail")
s.quit() 


