from bs4 import BeautifulSoup
import requests
import pandas as pd
from tabulate import tabulate
from tqdm import tqdm

DOMAIN = "https://www.carpages.ca"

url = "https://www.carpages.ca/used-cars/search/?num_results=50&category_id=6&p=1"

page = requests.get(url)
print(page)

soup = BeautifulSoup(page.text, "lxml")
# print(soup)

listings = soup.find_all("div", class_="t-flex t-gap-6 t-items-start t-p-6")

listings_data = []

for i in tqdm(range(0, 15)):
    for listing in listings:
        title = listing.find("a").get("title")
        colour = listing.find("span", class_="t-text-sm t-font-bold").text

        # if there is a sale on the car
        if listing.find("div", class_="tag tag--milli"):
            price = listing.find(
                "span", class_="t-font-bold t-text-xl t-text-primary"
            ).get_text(strip=True)
        else:
            price = listing.find("span", class_="t-font-bold t-text-xl").get_text(
                strip=True
            )

        listings_data_tupple = (title, colour, price)
        listings_data.append(listings_data_tupple)

    next_page_url = soup.find("a", {"title": "Next Page"}).get("href")
    next_page_url_full = DOMAIN + next_page_url
    page = requests.get(next_page_url_full)
    soup = BeautifulSoup(page.text, "lxml")

df = pd.DataFrame(columns=["title", "colour", "price"], data=listings_data)
print(tabulate(df, headers="keys", showindex=False, tablefmt="simple_grid"))
