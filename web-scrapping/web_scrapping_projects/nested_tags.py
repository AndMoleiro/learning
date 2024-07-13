import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"
page = requests.get(url)

soup = BeautifulSoup(page.text, "lxml")

boxes = soup.find_all("div", class_ = "col-md-4 col-xl-4 col-lg-4")[2]
pprint(boxes)

name = boxes.find("a")
pprint(name.text)