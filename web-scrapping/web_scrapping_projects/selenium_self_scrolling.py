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
input_box.send_keys("giraffe")
input_box.send_keys(Keys.ENTER)

google_images = driver.find_element(
    By.XPATH, '//*[@id="hdtb-sc"]/div/div/div[1]/div/div[2]/a/div'
)
google_images.click()

# self scrolling

# check max page height
# scroll_height = driver.execute_script("return document.body.scrollHeight")

# scroll to max height
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    break

# wait until condition

element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.ID, "cnt"))
