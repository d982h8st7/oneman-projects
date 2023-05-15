import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# options = Options()
# options.add_experimental_option('prefs', {
#     "download.default_directory": 'D:\for_project_files',  # 경로 설정
#     "download.prompt_for_download": False,  # 파일 다운로드 시 확인창 띄우지 않기
#     "download.directory_upgrade": True,
#     "plugins.always_open_pdf_externally": True
# })
#
# driver = webdriver.Chrome(options=options)
#
# # 가장 최신 게시글의 첨부파일 다운로드
# url = 'https://www.ync.ac.kr/kor/CMS/Board/Board.do?mCode=MN217&mgr_seq=26&mode=list&mgr_seq=26'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
#
#
# # 게시글 목록에서 가장 최신 게시글의 링크를 찾는 부분
# base_url = 'https://www.ync.ac.kr/kor/CMS/Board/Board.do'
# latest_post_path = soup.find('p', {'class': 'stitle'}).find('a').get('href')
# latest_post_link = urljoin(base_url, latest_post_path)
#
# driver.get(latest_post_link)
# time.sleep(2)
# item = driver.find_element(By.XPATH,'//*[@id="board-wrap"]/div[1]/div[2]/div/ul/li[1]/a')
# link = item.get_attribute('href')
# temp = requests.get(link)
#
# file = open("D:\\for_project_files\\yami.xlsx",'wb')
# file.write(temp.content)
# file.close()

data = pd.read_excel('yami.xlsx')  # 엑셀파일 저장
# 조식, 중식, 석식 구분값 추출
values1 = data.iloc[1, 0]  # 첫 번째 열('A'열)의 3행부터 7행까지 값
values2 = data.iloc[14, 0]  # 첫 번째 열('A'열)의 18행부터 20행까지 값
values3 = data.iloc[18, 0]  # 첫 번째 열('A'열)의 22행부터 26행까지 값
# values를 문자열로 변환하고, 각 값 사이에 줄 바꿈을 추가합니다.
values_str = values1
values_str1 = values2
values_str2 = values3

# 메모장에 저장합니다.
output_file_path = r'D:\for_project_files\output.txt'
with open(output_file_path, 'w') as f:
    f.write(values_str + '\n' + '\n' + values_str1 + '\n' + '\n' + values_str2)

menu_sec1 = data.iloc[1:7, 2].astype(str)  # 첫 번째 열('A'열)의 3행부터 7행까지 값
menu_sec2 = data.iloc[14:18, 2].astype(str)  # 첫 번째 열('A'열)의 18행부터 20행까지 값
menu_sec3 = data.iloc[18:24, 2].astype(str)  # 첫 번째 열('A'열)의 22행부터 26행까지 값
# values를 문자열로 변환하고, 각 값 사이에 줄 바꿈을 추가합니다.
menu_val1 = menu_sec1
menu_val2 = menu_sec2
menu_val3 = menu_sec3

print(menu_val1)
print(menu_val2)
print(menu_val3)

# 메모장에 저장합니다.
output_file_path = r'D:\for_project_files\output2.txt'
with open(output_file_path, 'w') as f:
    f.write(menu_val1 + '\n\n' + menu_val2 + '\n\n' + menu_val3)
