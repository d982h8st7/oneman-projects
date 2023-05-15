from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
driver = webdriver.Chrome(service=Service('D:\\task\\py\\1\\chromedriver.exe'), options=options)


try:
    driver.get('https://everytime.kr/393849/')
    # time.sleep(40)
    driver.find_element(By.XPATH,'//a[@id="writeArticleButton"]').click()
    title = driver.find_element(By.CSS_SELECTOR, 'input.title')
    content = driver.find_element(By.XPATH,'//textarea[@class="smallplaceholder"]')

    additional_content = "crawling test with connecting everytime.kr with selenium.\n" \
                         "You can see the code source in https://github.com/d982h8st7/oneman-projects/tree/main/1"
    # 두 문자열을 결합
    title.send_keys('2023년 5월 16일 학식 메뉴')  # 실제 제목으로 변경해야 함
    content.send_keys(additional_content)

    driver.find_element(By.XPATH,'//li[@class="submit"]').click()  # 실제 게시글 작성 버튼의 셀렉터로 변경해야 함
except Exception as e:
    print(str(e))