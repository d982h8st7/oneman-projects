import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

# 가장 최신 게시글의 첨부파일 다운로드
url = 'https://www.ync.ac.kr/kor/CMS/Board/Board.do?mCode=MN217&mgr_seq=26&mode=list&mgr_seq=26'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# 게시글 목록에서 가장 최신 게시글의 링크를 찾는 부분
base_url = 'https://www.ync.ac.kr'
latest_post_path = soup.find('p', {'class': 'stitle'}).find('a').get('href')
latest_post_link = urljoin(base_url, latest_post_path)

# 가장 최신 게시글 페이지로 이동
response = requests.get(latest_post_link)
soup = BeautifulSoup(response.text, 'html.parser')

# 첨부파일 URL을 찾는 부분
file_url = soup.find('a', {'title': '새창내려받기'}).get('href')

# 첨부파일을 다운로드하는 부분
response = requests.get(file_url)
with open('file.xlsx', 'wb') as f:
    f.write(response.content)

# 다운로드 받은 파일 읽기
data = pd.read_excel('file.xlsx')
data_to_post = data[['B', 'C', 'D', 'E', 'F']]  # 실제 엑셀 파일의 열 이름에 따라 수정해야 함
