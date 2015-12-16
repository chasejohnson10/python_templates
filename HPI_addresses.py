import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.hpitx.com/portfolio?limit=54')

r.content

soup = BeautifulSoup(r.content)

soup.prettify() 

soup.find_all("p", class_="prop-address")

for address in soup.find_all("p", class_="prop-address"):
	print address
	
