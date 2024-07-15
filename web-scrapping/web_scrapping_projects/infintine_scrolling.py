import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import pandas as pd
from pprint import pprint

options = ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)

driver.get("https://www.nike.com/nl/en/w/mens-sale-trousers-tights-2kq19z3yaepznik1")

# Handling cookie policy
time.sleep(3)

cookie_buttons = {
    "performance_button": '//*[@id="8cdd41d5-d916-4d3e-b75e-89ebec9787e9-declineLabel"]',
    "experiences_button": '//*[@id="5b258c22-cdcb-429c-8e19-61d5944a3231-declineLabel"]',
    "advertising_button": '//*[@id="94469303-c7b1-40be-9acb-dbb32d42d1d7-declineLabel"]',
    "confirm_choices_button": '//*[@id="modal-root"]/div[2]/div/div/div/div/section/div[1]/div[2]/div/div[10]/button',
}

try:
    print("Cookie Policy found")
    for button_name, xpath in cookie_buttons.items():
        button = driver.find_element(By.XPATH, xpath)
        driver.execute_script("arguments[0].scrollIntoView();", button)
        print(f"Clicking in {button_name}")
        time.sleep(1)
        button.click()

    print("Cookie Policy rejected")

except:
    NoSuchElementException("No cookie policy")

# Scrolling
while True:
    print("Scrolling")
    current_height = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script(f"window.scrollTo(0, {current_height})")

    time.sleep(2)

    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == current_height:
        break

    current_height = new_height

# Soup
soup = BeautifulSoup(driver.page_source, "lxml")

cards = soup.find_all("div", class_="product-card__body")

product_details = []

for card in cards:
    if card.find("div", class_="product-card__messaging accent--color"):
        sustainable_materials = True
    else:
        sustainable_materials = False
    product_name = card.find("div", class_="product-card__title").text
    product_type = card.find("div", class_="product-card__subtitle").text
    number_colours_available = int(
        card.find("div", class_="product-card__product-count").text.split(" ")[0]
    )
    current_price = card.find(
        "div", class_="product-price is--current-price css-1ydfahe"
    ).text
    previous_price = card.find(
        "div", class_="product-price nl__styling is--striked-out css-0"
    ).text

    product_details.append(
        (
            sustainable_materials,
            product_name,
            product_type,
            number_colours_available,
            previous_price,
            current_price,
        )
    )

    # DF
    df_headers = [
        "sustainable_materials",
        "product_name",
        "product_type",
        "number_colours_available",
        "previous_price",
        "current_price",
    ]

    df = pd.DataFrame(columns=df_headers, data=product_details)

    df.to_clipboard()

pprint(df)
