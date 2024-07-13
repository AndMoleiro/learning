import requests
from bs4 import BeautifulSoup
import pprint
import re
import pandas as pd


url = "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"
page = requests.get(url)

soup = BeautifulSoup(page.text, "lxml")

price = soup.find_all("h4", {"class": "price float-end card-title pull-right"})[6:]
# pprint.pprint(price)

a = soup.find_all("a", class_="title")
# pprint.pprint(a)

# multiple tags
multi = soup.find_all(["h4", "p"])
# pprint.pprint(multi)

# string tags
stringtag = soup.find_all(string="Iphone")
# pprint.pprint(stringtag)

# string tags with re
retag = soup.find_all(string=re.compile("Nok"))
# pprint.pprint(retag)

# class with re
reclass = soup.find_all("p", class_=re.compile("review-count"))
# pprint.pprint(reclass)

# class with re and limit
relimit = soup.find_all("p", class_=re.compile("review-count"), limit=3)
# pprint.pprint(relimit)

# create a table

product_name = soup.find_all("a", class_="title")
# pprint.pprint(product_name)

price = soup.find_all("h4", class_="price float-end card-title pull-right")
# pprint.pprint(price)

reviews = soup.find_all("p", class_="review-count float-end")
# pprint.pprint(reviews)

description = soup.find_all("p", class_="description card-text")
# pprint.pprint(description)


product_name_list = [i.text for i in product_name]
price_list = [i.text for i in price]
review_list = [i.text for i in reviews]
description_list = [i.text for i in description]

"""pprint.pprint(product_name_list)
pprint.pprint(price_list)
pprint.pprint(review_list)
pprint.pprint(description_list)"""

table = pd.DataFrame(
    {
        "product_name": product_name_list,
        "price": price_list,
        "reviews": review_list,
        "description": description_list,
    }
)

table.to_clipboard()

print(table)
