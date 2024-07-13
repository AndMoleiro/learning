from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from icecream import ic
import time

options = Options()
options.add_argument("--disable-notifications")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)

driver.get("https://www.google.com")

# Handling cookies
try:
    reject_cookies_button = driver.find_element(By.XPATH, '//*[@id="W0wltc"]/div')
    reject_cookies_button.click()
    print("Cookie policy found and rejected")
except NoSuchElementException:
    print("No cookie policy found")

# send text to input box and trigger the search
input_box = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
google_query = "top 100 movies of all time"
print(f"Sending query - '{google_query}' - to input text box")
input_box.send_keys(google_query)

google_search_button = driver.find_element(
    By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]"
)
print("Triggering google search")
google_search_button.click()

# find imdb and select imdb result
imdb_result = driver.find_element(By.PARTIAL_LINK_TEXT, "imdb")
imdb_result.click()

# wait for the page to load
time.sleep(3)

# Handling privacy policy
try:
    reject_cookies_button = driver.find_element(
        By.XPATH, '//*[@id="__next"]/div/div/div[2]/div/button[1]'
    )
    reject_cookies_button.click()
    print("Privacy policy found and rejected")
except NoSuchElementException:
    print("No privacy policy found")


# Scroll to result number 50
scroll_height = driver.execute_script("return document.body.scrollHeight")
print("Scrolling to the end of page")
scroll_to_end_of_page = driver.execute_script(
    "window.scrollTo(0, document.body.scrollHeight)"
)

# Screenshots
time.sleep(3)
screenshot_path = "/Users/andremoleiro/Documents/Learning/learning-repo/web-scrapping/web_scrapping_projects/exercises"
full_screenshot_file_path = f"{screenshot_path}/full_screenshot.png"
poster_screenshot_file_path = f"{screenshot_path}/poster_screenshot.png"

print(f"Saving full screenshot to {full_screenshot_file_path}")
driver.save_screenshot(full_screenshot_file_path)

poster = driver.find_element(
    By.XPATH,
    '//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[2]/ul/li[50]/div/div/div/div[1]/div[1]/div/div[2]',
)

print(f"Saving poster to {poster_screenshot_file_path}")
poster.screenshot(poster_screenshot_file_path)
