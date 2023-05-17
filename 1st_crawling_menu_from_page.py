import datetime
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option('prefs', {
    "download.default_directory": r'D:\for_project_files',  # 경로 설정
    "download.prompt_for_download": False,  # 파일 다운로드 시 확인창 띄우지 않기
    })
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

driver = webdriver.Chrome(service=Service('D:\\task\\py\\1\\chromedriver.exe'), options=options)


# # 가장 최신 게시글의 첨부파일 다운로드
url = 'https://www.ync.ac.kr/kor/CMS/Board/Board.do?mCode=MN217&mgr_seq=26&mode=list&mgr_seq=26'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
#
#
# # 게시글 목록에서 가장 최신 게시글의 링크를 찾는 부분
base_url = 'https://www.ync.ac.kr/kor/CMS/Board/Board.do'
latest_post_path = soup.find('p', {'class': 'stitle'}).find('a').get('href')
latest_post_link = urljoin(base_url, latest_post_path)

driver.get(latest_post_link)
time.sleep(2)
item = driver.find_element(By.XPATH,'//*[@id="board-wrap"]/div[1]/div[2]/div/ul/li[1]/a')
link = item.get_attribute('href')
temp = requests.get(link)

file = open("D:\\for_project_files\\yami.xlsx",'wb')
file.write(temp.content)
file.close()

data = pd.read_excel('yami.xlsx')  # 엑셀파일 저장
