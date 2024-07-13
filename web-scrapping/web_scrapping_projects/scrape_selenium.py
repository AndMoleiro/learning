from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from icecream import ic

options = Options()
options.add_experimental_option("detach", False)
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)

driver.get("https://www.goat.com/sneakers")

prices = [
    driver.find_element(
        By.XPATH,
        f'//*[@id="grid-body"]/div/div[1]/div[{str(i)}]/a/div[1]/div[2]/div/div/span',
    ).text
    for i in range(1, 10)
]

ic(prices)
