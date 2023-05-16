from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_experimental_option('debuggerAddress', '127.0.0.1:9222')

try:
    driver = webdriver.Chrome(service=Service('./chromedriver.exe'), options=options)
    wait = WebDriverWait(driver, 10)

    driver.get('https://everytime.kr/393849/')
    print("Page loaded successfully!")

except Exception as e:
    print("An error occurred:", e)
