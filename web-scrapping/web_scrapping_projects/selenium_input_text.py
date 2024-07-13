from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from icecream import ic

options = Options()
options.add_argument("--disable-notifications")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)

driver.get("https://www.google.com")

try:
    cookie = driver.find_element(By.XPATH, '//*[@id="W0wltc"]/div')
    cookie.click()
    print("Cookies found and rejected")
except:
    NoSuchElementException("No cookie policy")


input_box = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
input_box.send_keys("r ffxiv")
input_box.send_keys(Keys.ENTER)

# take screenshot
driver.save_screenshot("/Users/andremoleiro/Documents/Learning/learning-repo/web-scrapping/screenshot.png")
