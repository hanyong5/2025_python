
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
from datetime import datetime

browser = webdriver.Chrome()
url = "https://www.naver.com"

# browser에서 url 열기
browser.get(url)
print(browser.title)

browser.find_element(By.ID, 'query').click()
browser.find_element(By.ID, 'query').send_keys("날씨") # 검색어 입력
browser.find_element(By.CLASS_NAME,'btn_search').click()

time.sleep(2)
data = browser.find_element(By.CLASS_NAME, 'temperature_text').text

print(data)



# 현재 날짜와 시간 가져오기
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 데이터프레임 생성
df = pd.DataFrame({
    'datetime': [current_time],
    'temperature': [data]
})

# CSV 파일이 존재하면 추가, 없으면 새로 생성
try:
    existing_df = pd.read_csv('data.csv')
    updated_df = pd.concat([existing_df, df], ignore_index=True)
    updated_df.to_csv('data.csv', index=False)
except FileNotFoundError:
    df.to_csv('data.csv', index=False)

print(f"데이터가 저장되었습니다: {current_time}, {data}")

