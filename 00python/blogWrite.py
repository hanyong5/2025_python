import os
from dotenv import load_dotenv
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



load_dotenv()

driver = webdriver.Chrome()
driver.get("https://nid.naver.com/nidlogin.login")
time.sleep(1)

id = driver.find_element(By.ID, "id")
pyperclip.copy(os.getenv("NAVER_ID"))
id.click()
id.send_keys(Keys.CONTROL + "v")

pw = driver.find_element(By.ID, "pw")
pyperclip.copy(os.getenv("NAVER_PW"))
pw.click()
pw.send_keys(Keys.CONTROL + "v")


login_btn = driver.find_element(By.ID, "log.login")
login_btn.click()
time.sleep(3)

driver.get('https://blog.naver.com/GoBlogWrite.naver')
time.sleep(10)

# 타이핑 속도 설정
TYPE_DELAY = 0.1  # 초 단위

# 입력할 제목과 내용을 외부 파일에서 읽어오기
with open('blog/blog_content.txt', 'r', encoding='utf-8') as f:
    title_text = f.readline().strip() + "\n" + f.readline().strip()  # 첫 두 줄을 제목으로 읽기
    body_text = f.read()  # 나머지 내용을 본문으로 읽기

# 이미지 파일 경로
image_paths = [
    "images/travel_moment.jpg",  # 첫 번째 이미지
    "images/community.jpg"       # 두 번째 이미지
]

# 1. iframe 전환
driver.switch_to.frame(driver.find_element(By.ID, "mainFrame"))
time.sleep(2)

# 2. 팝업 닫기 (.se-popup-button-cancel)
try:
    cancel_btn = driver.find_element(By.CLASS_NAME, "se-popup-button-cancel")
    cancel_btn.click()
    print("팝업 취소 버튼 클릭됨")
    time.sleep(1)
except:
    print("팝업 없음 (se-popup-button-cancel)")

# 3. 도움말 닫기 (.se-help-panel-close-button)
try:
    help_close_btn = driver.find_element(By.CLASS_NAME, "se-help-panel-close-button")
    help_close_btn.click()
    print("도움말 닫기 버튼 클릭됨")
    time.sleep(1)
except:
    print("도움말 없음 (se-help-panel-close-button)")

# 4. 제목 입력
title_input = driver.find_element(By.CSS_SELECTOR, ".se-section-documentTitle")
title_input.click()
actions = ActionChains(driver)
for char in title_text:
    actions.send_keys(char).perform()
    time.sleep(TYPE_DELAY)

# # 5. 본문 입력
content_area = driver.find_element(By.CSS_SELECTOR, ".se-section-text")
content_area.click()
actions = ActionChains(driver)

# 가운데 정렬 및 폰트 크기 설정
# actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()  # 전체 선택
# time.sleep(1)
# actions.key_down(Keys.CONTROL).send_keys('e').key_up(Keys.CONTROL).perform()  # 가운데 정렬
# time.sleep(1)
# actions.key_down(Keys.CONTROL).send_keys('2').key_up(Keys.CONTROL).perform()  # 폰트 크기 20으로 설정
# time.sleep(1)

# 본문 입력
for char in body_text:
    actions.send_keys('\n' if char == '\n' else char).perform()
    time.sleep(TYPE_DELAY)


    

# 6. 저장 버튼 클릭
save_button = driver.find_element(By.CLASS_NAME, "save_btn__bzc5B")
save_button.click()
print("✅ 글 저장 완료!")



















