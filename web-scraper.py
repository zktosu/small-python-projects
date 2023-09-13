import requests
from bs4 import BeautifulSoup
address = input("give the address to get the content: ")
r = requests.get("https://"+address)
soup = BeautifulSoup(r.text,'html.parser')
links = soup.find_all('a')
for link in links:
	print(link.get("href"))

