from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
driver.get("https://mail.naver.com/write")
r_sleep()



def read_mail_content():
    with open('mailtext.txt','r',encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    to_email = lines[0].split(':')[1]
    to_title = lines[1].split(':')[1]
    to_body = lines[2].split(':')[1]

    return to_email,to_title,to_body

to_mail,to_title,to_body = read_mail_content()


mail_email = driver.find_element(By.ID,'recipient_input_element')
pyperclip.copy(to_mail)
mail_email.click()
mail_email.send_keys(Keys.CONTROL,'v')
r_sleep()


mail_title = driver.find_element(By.ID,'subject_title')
pyperclip.copy(to_title)
mail_title.click()
mail_title.send_keys(Keys.CONTROL,'v')
r_sleep()


# iframe 들어감
iframe = driver.find_element(By.CSS_SELECTOR,".editor_body iframe")
driver.switch_to.frame(iframe)

mail_body = driver.find_element(By.CLASS_NAME,'workseditor-content')
pyperclip.copy(to_body)
mail_body.click()
mail_body.send_keys(Keys.CONTROL,'v')
r_sleep()

# iframe 나옴
driver.switch_to.default_content()

# 버튼클릭
send_btn = driver.find_element(By.CLASS_NAME,'button_write_task')
send_btn.click()
r_sleep()


# input('텍스입력')