import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"

page = requests.get(url)
# print(page)

soup = BeautifulSoup(page.text, "lxml")
# print(soup)

# find

header = soup.find("header")
# print(header)


attr = soup.find("div", {"class": "container test-site"})
# print(attr)

price = soup.find("h4", {"class": "price float-end card-title pull-right"})
print(price)