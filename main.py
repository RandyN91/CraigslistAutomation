import bs4
from bs4 import BeautifulSoup
import requests

CL_URL = 'https://newyork.craigslist.org'

r = requests.get(CL_URL).text

soup = BeautifulSoup(r,'html.parser')

print(soup)

