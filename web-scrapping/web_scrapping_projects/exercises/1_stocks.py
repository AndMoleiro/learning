"""
Go to https://www.marketwatch.com/investing/stock/aapl?mod=search_symbol and scrape:
    - current stock price
    - closing price
    - 52 week range of the prices (min, max)
    - analyst ratings (avg)
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

# 1 - Import the url into python

url = "https://www.marketwatch.com/investing/stock/msft"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-GB,en;q=0.6",
    "Cookie": "zero-chakra-ui-color-mode=light-zero; AMP_MKTG_8f1ede8e9c=JTdCJTIycmVmZXJyZXIlMjIlM0ElMjJodHRwcyUzQSUyRiUyRnd3dy5nb29nbGUuY29tJTJGJTIyJTJDJTIycmVmZXJyaW5nX2RvbWFpbiUyMiUzQSUyMnd3dy5nb29nbGUuY29tJTIyJTdE; AMP_8f1ede8e9c=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI1MjgxOGYyNC05ZGQ3LTQ5OTAtYjcxMC01NTY0NzliMzAwZmYlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzA4MzgxNTQ4ODQzJTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTcwODM4MjE1NTQ2MCUyQyUyMmxhc3RFdmVudElkJTIyJTNBNiU3RA==",
}

page = requests.get(url, headers=headers)
# Check if scrappable -> Response [200]
print(page)

soup = BeautifulSoup(page.text, "lxml")
# print(soup)

current_price = soup.find("bg-quote", class_="value").text

closing_price = soup.find("td", class_="table__cell u-semi").text

price_range_outer = soup.find_all("div", class_="range__header")[2]
price_range_inner = price_range_outer.find_all(class_="primary")
price_range = f"{price_range_inner[0].text} - {price_range_inner[1].text}"

analyst_ratings = soup.find("li", class_="analyst__option active").text

print(f"current_price: {current_price}")
print(f"closing_price: {closing_price}")
print(f"price_range: {price_range}")
print(f"analyst_ratings: {analyst_ratings}")