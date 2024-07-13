import requests
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

# print(soup)

# Tags
# print(soup.header)

# Navigational Strings
# tag = soup.header.p.string
# print(tag)

# Attributes
tag = soup.header.a.attrs
tag_attr = tag['data-bs-toggle']
print(tag_attr)

# Comments