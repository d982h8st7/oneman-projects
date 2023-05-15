import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
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

# 가장 최신 게시글의 첨부파일 다운로드
url = 'https://www.ync.ac.kr/kor/CMS/Board/Board.do?mCode=MN217&mgr_seq=26&mode=list&mgr_seq=26'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# 게시글 목록에서 가장 최신 게시글의 링크를 찾는 부분
base_url = 'https://www.ync.ac.kr'
latest_post_path = soup.find('p', {'class': 'stitle'}).find('a').get('href')
latest_post_link = urljoin(base_url, latest_post_path)

driver.get(latest_post_link)
file_link = driver.find_element('ul.board-view-filelist li a').get_attribute('href')
time.sleep(10)

# # 다운로드 받은 파일 읽기
# data = pd.read_excel('file.xlsx')
# data_to_post = data[['B', 'C', 'D', 'E', 'F']]  # 실제 엑셀 파일의 열 이름에 따라 수정해야 함
