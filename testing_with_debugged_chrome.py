from selenium import webdriver
import datetime
import pandas as pd
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
    f.write(values_str + '\n\n\n\n' + '\n\n\n\n' + values_str1 + '\n\n\n' + '\n\n\n' + values_str2)

menu_sec1 = data.iloc[1:7, 2].astype(str)  # 첫 번째 열('A'열)의 3행부터 7행까지 값
menu_sec2 = data.iloc[14:18, 2].astype(str)  # 첫 번째 열('A'열)의 18행부터 20행까지 값
menu_sec3 = data.iloc[18:24, 2].astype(str)  # 첫 번째 열('A'열)의 22행부터 26행까지 값
# values를 문자열로 변환하고, 각 값 사이에 줄 바꿈을 추가합니다.
menu_val1 = ' \n'.join(menu_sec1.values)+'ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ'
menu_val2 = " \n".join(menu_sec2.values)+'ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ'
menu_val3 = " \n".join(menu_sec3.values)+'ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ'


# # 메모장에 저장합니다.
output_file_path = r'D:\for_project_files\output2.txt'
with open(output_file_path, 'w') as f:
    f.write(menu_val1 + '\n\n' + menu_val2 + '\n\n' + menu_val3)

a = datetime.datetime.now()



try:
    driver.get('https://everytime.kr/393849/')
    # time.sleep(40)
    driver.find_element(By.XPATH,'//a[@id="writeArticleButton"]').click()
    title = driver.find_element(By.CSS_SELECTOR, 'input.title')
    content = driver.find_element(By.XPATH,'//textarea[@class="smallplaceholder"]')
    main_contents = values_str + menu_val1 + '\n' + values_str1 + menu_val2 + '\n' + values_str2 + menu_val3 + '\n\n\n\n'

    additional_content = "crawling test with connecting everytime.kr with selenium.\n" \
                         "You can see the code source in https://github.com/d982h8st7/oneman-projects/tree/main/1\n"+a
    # 두 문자열을 결합
    title.send_keys('2023년 5월 16일 학식 메뉴')  # 실제 제목으로 변경해야 함
    content.send_keys(main_contents+additional_content)

    driver.find_element(By.XPATH,'//li[@class="submit"]').click()  # 실제 게시글 작성 버튼의 셀렉터로 변경해야 함
except Exception as e:
    print(str(e))