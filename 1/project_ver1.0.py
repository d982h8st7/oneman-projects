import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

# 가장 최신 게시글의 첨부파일 다운로드
url = 'https://www.ync.ac.kr/kor/CMS/Board/Board.do?mCode=MN217&mgr_seq=26&mode=list&mgr_seq=26'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# 게시글 목록에서 가장 최신 게시글의 링크를 찾는 부분
latest_post_link = soup.find('p', {'class': 'stitle'}).find('a').get('?mCode=MN217&mgr_seq=26&mode=view&mgr_seq=26&board_seq=95902')

# 가장 최신 게시글 페이지로 이동
response = requests.get(latest_post_link)
soup = BeautifulSoup(response.text, 'html.parser')

# 첨부파일 URL을 찾는 부분
file_url = soup.find('a', {'title': '새창내려받기'}).get('/kor/ajx_json/UploadMgr/downloadRun.do?qcode=Qm9hcmQsNDEzNDMsWQ==')

# 첨부파일을 다운로드하는 부분
response = requests.get(file_url)
with open('file.xlsx', 'wb') as f:
    f.write(response.content)

# 다운로드 받은 파일 읽기
data = pd.read_excel('file.xlsx')
data_to_post = data[['B', 'C', 'D', 'E', 'F']]  # 실제 엑셀 파일의 열 이름에 따라 수정해야 함

# Everytime에 로그인하고 게시글 작성
driver = webdriver.Chrome('')  # 실제 드라이버 파일의 경로로 변경해야 함
driver.get('https://everytime.kr/login')
username = driver.find_element_by_name('userid')
password = driver.find_element_by_name('password')

username.send_keys('your_username')  # 실제 아이디로 변경해야 함
password.send_keys('your_password')  # 실제 비밀번호로 변경해야 함

driver.find_element_by_xpath('//input[@type="submit"]').click()  # 실제 로그인 버튼의 셀렉터로 변경해야 함
driver.get('https://everytime.kr/393849/write')

title = driver.find_element_by_name('title')
content = driver.find_element_by_name('content')

# 본문 내용 추가

additional_content = "추가적으로 넣을 본문 내용입니다."
# 두 문자열을 결합

final_content = data_to_post.to_string() + "\n" + additional_content

title.send_keys('your_title')  # 실제 제목으로 변경해야 함

content.send_keys(final_content)

driver.find_element_by_xpath('//input[@type="submit"]').click()  # 실제 게시글 작성 버튼의 셀렉터로 변경해야 함

