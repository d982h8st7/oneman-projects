import pandas as pd

# 엑셀 파일 읽기
file = open("D:\\for_project_files\\yami.xlsx",'wb')
df = pd.read_excel('yami.xlsx',header=None)

# 조식, 중식, 석식 구분값 추출
values1 = df.iloc[2, 0]
values2 = df.iloc[15, 0]
values3 = df.iloc[19, 0]

# 해당 값들을 DataFrame으로 변환 (열 이름은 기존 데이터와 동일하게 설정)
values_df1 = pd.DataFrame({df.columns[0]: [values1]})
values_df2 = pd.DataFrame({df.columns[0]: [values2]})
values_df3 = pd.DataFrame({df.columns[0]: [values3]})

# 각 요일별로 저장
for i in range(1, 6):
    # 범위 추출
    df1 = df.iloc[0:7, i:i+1]   # 첫 번째 열('A'열)의 3행부터 7행까지 값
    df2 = df.iloc[14:18, i:i+1] # 첫 번째 열('A'열)의 18행부터 20행까지 값
    df3 = df.iloc[18:24, i:i+1] # 첫 번째 열('A'열)의 22행부터 26행까지 값


    # DataFrame을 하나로 결합
    new_df = pd.concat([values_df1, df1, values_df2, df2, values_df3, df3])

    # 새로운 엑셀 파일로 저장
    new_df.to_excel(f'D:/for_project_files/new_yami{i}.xlsx', index=False)
