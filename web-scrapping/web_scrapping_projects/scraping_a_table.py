import requests
from bs4 import BeautifulSoup
import pandas as pd
from pprint import pprint

url = "https://www.worldometers.info/world-population/"

page = requests.get(url)
# print(page)

soup = BeautifulSoup(page.text, "lxml")
# print(soup)

table = soup.find(
    "table",
    class_="table table-striped table-bordered table-hover table-condensed table-list",
)
# print(table)

headers_list = table.find_all("th")
headers = [header.text for header in headers_list]

table_rows_nested = table.find_all("tr")[1:]

table_rows = list(
    map(lambda row: [cell.text for cell in row.find_all("td")], table_rows_nested)
)

df = pd.DataFrame(table_rows, columns=headers)
df.to_clipboard()
