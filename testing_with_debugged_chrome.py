from selenium import webdriver
import datetime
import pandas as pd
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time

now = datetime.now()

options = Options()
options.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
driver = webdriver.Chrome(service=Service('./chromedriver.exe'), options=options)



try:
    driver.get('https://everytime.kr/393849/')
    time.sleep(40)
    driver.find_element(By.XPATH,'//a[@id="writeArticleButton"]').click()
    upload_button = driver.find_element(By.CLASS_NAME, 'attach')
    title = driver.find_element(By.CSS_SELECTOR, 'input.title')
    content = driver.find_element(By.XPATH,'//textarea[@class="smallplaceholder"]')

    #upload_button.send_keys('C:\\Users\\User\\Desktop\\파이썬\\workingArea\\Project\\files\\5_17_menu.png')
    additional_content = "본 파이썬 코드는 자동으로 학교사이트에서 학식 엑셀파일을 크롤링, 데이터를 추출하여 사진으로 변환, \n 에타에 자동으로 올리는 파이썬 프로젝트입니다.\n" \
                         "학식자동알림ver1.2 코드의 원본은 \n https://github.com/d982h8st7/oneman-projects 에서 보실수있습니다. \n" \
                         "메뉴 데이터의 원본 컨텐츠의 저작권 귀속은 영남이공대학교에 있으며, \n본 코드를 인용, 개조하여 불이익이 발생시 \n코드제작자는 어떠한 책임도 지지않습니다. \n" \
                         "글 작성시각 :"+str(now)
    # 두 문자열을 결합     "
    title.send_keys(f"{str(now.date()+1)}일 학식메뉴")  # 실제 제목으로 변경해야 함
    content.send_keys(additional_content)
    time.sleep(10)
    driver.find_element(By.XPATH,'//li[@class="submit"]').click()  # 실제 게시글 작성 버튼의 셀렉터로 변경해야 함
except Exception as e:
    print(str(e))