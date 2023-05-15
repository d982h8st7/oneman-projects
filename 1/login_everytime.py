from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option('prefs', {
    "download.default_directory": 'D:\for_project_files',  # 경로 설정
    "download.prompt_for_download": False,  # 파일 다운로드 시 확인창 띄우지 않기
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
})

driver = webdriver.Chrome(options=options)

driver.get('https://everytime.kr/393849/')
cookies = driver.get_cookies()
time.sleep(40)
driver.get('https://everytime.kr/393849/')
time.sleep(5)
driver.find_element(By.XPATH,'//a[@id="writeArticleButton"]').click()
title = driver.find_element(By.XPATH,'//input[@title=title]')
content = driver.find_element(By.XPATH,'//textarea[@name=text]')




# 본문 내용 추가
time.sleep(5)
additional_content = "crawling test with connecting everytime.kr with selenium.\n" \
                     "You can see the code source in https://github.com/d982h8st7/oneman-projects/tree/main/1"
# 두 문자열을 결합

# final_content = data_to_post.to_string() + "\n" + additional_content

title.send_keys('crawling_title')  # 실제 제목으로 변경해야 함
content.send_keys(additional_content)
driver.find_element(By.XPATH,'//li[@class="submit"]').click()  # 실제 게시글 작성 버튼의 셀렉터로 변경해야 함