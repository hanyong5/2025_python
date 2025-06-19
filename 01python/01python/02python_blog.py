from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


import time
from random import uniform
import os
from dotenv import load_dotenv
import pyperclip

load_dotenv()

def r_sleep(min_sec=2,max_sec=5):
    wait_time = uniform(min_sec,max_sec)
    print(f'{wait_time:.2f}초 대기중')
    time.sleep(wait_time)



options=webdriver.ChromeOptions()
options.add_argument('--start-maximized')
driver = webdriver.Chrome(options=options)

driver.get("https://nid.naver.com/nidlogin.login")
# print(uniform(2,5))

r_sleep()


NAVER_ID = os.getenv("NAVER_ID")
NAVER_PW = os.getenv("NAVER_PW")


# 아이디넣기
id_input = driver.find_element(By.ID,"id")
pyperclip.copy(NAVER_ID)
id_input.click()
id_input.send_keys(Keys.CONTROL,'v')
r_sleep()

# 비밀번호 입력
pw_input = driver.find_element(By.ID, "pw")
pyperclip.copy(NAVER_PW)
pw_input.click()
pw_input.send_keys(Keys.CONTROL, 'v')
r_sleep()

# 로그인 클릭
login_btn = driver.find_element(By.ID, "log.login")
login_btn.click()
r_sleep()

# 페이지이동
driver.get("https://blog.naver.com/GoBlogWrite.naver")
r_sleep()


iframe = driver.find_element(By.ID,'mainFrame')
driver.switch_to.frame(iframe)
r_sleep()


try:
    pop_cancle_btn = driver.find_element(By.CLASS_NAME,'se-popup-button-cancle')
    pop_cancle_btn.click()
    print("팝업있음")
    r_sleep()
except:
    print("팝업없음")

try:
    help_cancle_btn = driver.find_element(By.CLASS_NAME,'se-help-panel-close-button')
    help_cancle_btn.click()
    print("help있음")
    r_sleep()
except:
    print("help없음")


# 입력내용
title_text = "안녕하세요, 여행을 사랑하는 모든 분들께!"
body_text = (
    "설레는 발걸음으로 시작되는 여행의 순간들, 낯선 거리에서 마주치는 예상치 못한 만남들, "
    "그리고 새로운 문화와 풍경 속에서 느끼는 감동을 이 공간에 담아보려 합니다. "
    "여행은 단순한 이동이 아닌, 나를 발견하고 세상을 더 넓게 바라보는 소중한 시간이라고 생각합니다.\n"
    "앞으로 제가 경험한 특별한 순간들과 여행 팁을 여러분과 나누며, 함께 성장하는 여행 커뮤니티를 만들어가길 희망합니다. "
    "여러분의 발자국도 이 여정에 함께해주세요!"
)

TYPE_DELAY = 0.1

try:
    title_input = driver.find_element(By.CSS_SELECTOR,'div.se-section-documentTitle')
    # pyperclip.copy(title_text)
    title_input.click()

    # title_input.send_keys(Keys.CONTROL,'v')
    actions = ActionChains(driver)
    # actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

    for char in title_text:
        actions.send_keys(char).perform()
        time.sleep(TYPE_DELAY)


    r_sleep()
except:
    print("paragraph없음")


try:
    content_input = driver.find_element(By.CSS_SELECTOR,'div.se-section-text')
    content_input.click()
    actions = ActionChains(driver)

    for char in body_text:
        actions.send_keys('\n' if char == '\n' else char).perform()
        time.sleep(TYPE_DELAY)


    r_sleep()
except:
    print("body없음")


save_button = driver.find_element(By.CLASS_NAME,'save_btn__bzc5B')
save_button.click()
print('글저장 완료')
r_sleep()

input('텍스입력')