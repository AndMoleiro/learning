import requests
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'

# check if we can scrape it (200 -> can, 400 -> can't)
page = requests.get(url)
print(page)


# get the html, convert it to text and then parse it back into html
soup = BeautifulSoup(page.text, 'lxml')
print(soup)

# Find

