#!/bin/python
from bs4 import BeautifulSoup
import requests

url = input("Enter a website to extract the URL's from: ")
response = requests.get("http://" +url)
data = response.text
soup = BeautifulSoup(data)

for link in soup.find_all('a'):
     print(link.get('href'))
