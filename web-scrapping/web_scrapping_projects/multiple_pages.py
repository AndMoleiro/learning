import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.airbnb.com/s/Honolulu--Oahu--Hawaii--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2024-08-01&monthly_length=3&monthly_end_date=2024-11-01&price_filter_input_type=0&channel=EXPLORE&query=Honolulu%2C%20Oahu%2C%20Hawaii%2C%20United%20States&place_id=ChIJTUbDjDsYAHwRbJen81_1KEs&date_picker_type=calendar&checkin=2024-07-10&checkout=2024-07-17&source=structured_search_input_header&search_type=user_map_move&drawer_open=false&search_mode=regular_search&price_filter_num_nights=7&ne_lat=21.307616039899717&ne_lng=-157.81147926441656&sw_lat=21.2776922409539&sw_lng=-157.90568983816263&zoom=15.463623223590126&zoom_level=15&search_by_map=true&federated_search_session_id=6196a3f2-d1e0-47e3-8e29-e910c7b316c1&pagination_search=true&cursor=eyJzZWN0aW9uX29mZnNldCI6MCwiaXRlbXNfb2Zmc2V0IjowLCJ2ZXJzaW9uIjoxfQ%3D%3D"

page = requests.get(url)
print(page)

soup = BeautifulSoup(page.text, "lxml")
# print(soup)

df = pd.DataFrame(
    {"Links": [""], "Title": [""], "Details": [""], "Price": [""], "Rating": [""]}
)

while True:

    postings = soup.find_all("div", class_="_8ssblpx")
    for post in postings:
        try:
            link = post.find("a", class_="gjo10").get("href")
            link_full = "https://airbnb.ca" + link
            title = post.find("a", class_="gjfo10").get("aria-label")
            price = post.find("span", class_="_1p7iugi").text
            rating = post.find("span", class_="1'fy1f8").text
            details = post.find_all("div", class_="kqh46o")[0].text
            df = df.append(
                {
                    "Links": link_full,
                    "Title": title,
                    "Details": details,
                    "Price": price,
                    "Rating": rating,
                },
                ignore_index=True,
            )
        except:
            pass

    next_page = soup.find("a", {"aria-label": "Next"}).get("href")
    url = f"https://airbnb.ca" + next_page
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "lxml")
