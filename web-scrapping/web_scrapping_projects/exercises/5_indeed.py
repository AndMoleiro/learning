from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager

from selenium.common.exceptions import NoSuchElementException

from bs4 import BeautifulSoup
import pandas as pd

import time

from pprint import pprint

from tabulate import tabulate

options = ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)

WEBSITE = "https://pt.indeed.com/"

driver.get(WEBSITE)

time.sleep(2)

job_title_inbox = driver.find_element(By.CSS_SELECTOR, "#text-input-what")
job_title_inbox.send_keys("Data Analyst")

search_button = driver.find_element(
    By.CSS_SELECTOR, "#jobsearch > div > div.css-169igj0.eu4oa1w0 > button"
)
search_button.click()

WebDriverWait(driver=driver, timeout=5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#jobsearch-Main"))
)

offerings = set()

while True:
    soup = BeautifulSoup(driver.page_source, "lxml")

    time.sleep(1)

    # cookie policy
    try:
        reject_cookies_button = driver.find_element(
            By.CSS_SELECTOR,
            "#mosaic-desktopserpjapopup > div.css-g6agtu.eu4oa1w0 > button > svg",
        )
        driver.execute_script("arguments[0].scrollIntoView();", reject_cookies_button)
        reject_cookies_button.click()
        print(f"COOKIE POLICY FOUND AND REJECTED")
    except NoSuchElementException:
        pass

    job_listing_boxes = soup.find_all("li", class_="css-5lfssm eu4oa1w0")

    for box in job_listing_boxes:
        if not box.find(class_="mosaic mosaic-empty-zone nonJobContent-desktop"):

            header = job_title = company_name = job_location = job_type = salary = ""

            if header_html := box.find(class_="css-1hlnck6 e37uo190"):
                header = header_html.text

            job_title = box.find("span").get("title")
            company_name = box.find("span", {"data-testid": "company-name"}).text

            if job_location_html := box.find("div", class_="css-1p0sjhy eu4oa1w0"):
                job_location = job_location_html.text

            if job_type_html := box.find(class_="metadata css-5zy3wz eu4oa1w0"):
                job_type = job_type_html.text

            if salary_html := box.find(
                "div", class_="metadata salary-snippet-container css-5zy3wz eu4oa1w0"
            ):
                salary = salary_html.text

        offerings.add((header, job_title, company_name, job_location, job_type, salary))

    try:
        next_button_href = soup.find(
            "a", attrs={"data-testid": "pagination-page-next"}
        ).get("href")
        driver.get(WEBSITE + next_button_href)
    except AttributeError:
        print("attr")
        break
    except  NoSuchElementException:
        print("no element")
        break

headers = ["header", "job_title", "company_name", "job_location", "job_type", "salary"]

df = pd.DataFrame(columns=headers, data=offerings)

df.to_csv(
    "/Users/andremoleiro/Documents/Learning/learning-repo/web-scrapping/web_scrapping_projects/exercises/indeed.csv",
    index=False,
)
