import tkinter as tk
from tkinter import ttk, messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from random import uniform
import os
from dotenv import load_dotenv
import pyperclip

load_dotenv()

def r_sleep(min_sec=2, max_sec=5):
    wait_time = uniform(min_sec, max_sec)
    print(f'{wait_time:.2f}초 대기중')
    time.sleep(wait_time)

class EmailSender:
    def __init__(self, root):
        self.root = root
        self.root.title("네이버 메일 자동화 프로그램")
        self.root.geometry("500x600")
        
        # 스타일 설정
        style = ttk.Style()
        style.configure('TLabel', padding=5)
        style.configure('TEntry', padding=5)
        style.configure('TButton', padding=5)
        
        # 프레임 생성
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 입력 필드
        ttk.Label(main_frame, text="네이버 아이디:").grid(row=0, column=0, sticky=tk.W)
        self.naver_id = ttk.Entry(main_frame, width=40)
        self.naver_id.grid(row=0, column=1, padx=5, pady=5)
        self.naver_id.insert(0, os.getenv("NAVER_ID", ""))
        
        ttk.Label(main_frame, text="네이버 비밀번호:").grid(row=1, column=0, sticky=tk.W)
        self.naver_pw = ttk.Entry(main_frame, width=40, show="*")
        self.naver_pw.grid(row=1, column=1, padx=5, pady=5)
        self.naver_pw.insert(0, os.getenv("NAVER_PW", ""))
        
        ttk.Label(main_frame, text="받는 사람 이메일:").grid(row=2, column=0, sticky=tk.W)
        self.receiver_email = ttk.Entry(main_frame, width=40)
        self.receiver_email.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(main_frame, text="제목:").grid(row=3, column=0, sticky=tk.W)
        self.subject = ttk.Entry(main_frame, width=40)
        self.subject.grid(row=3, column=1, padx=5, pady=5)
        
        ttk.Label(main_frame, text="내용:").grid(row=4, column=0, sticky=tk.W)
        self.body = tk.Text(main_frame, width=40, height=10)
        self.body.grid(row=4, column=1, padx=5, pady=5)
        
        # 전송 버튼
        send_button = ttk.Button(main_frame, text="메일 전송", command=self.send_email)
        send_button.grid(row=5, column=0, columnspan=2, pady=20)
        
    def send_email(self):
        try:
            # Chrome 옵션 설정
            options = webdriver.ChromeOptions()
            options.add_argument('--start-maximized')
            driver = webdriver.Chrome(options=options)
            
            # 네이버 로그인
            driver.get("https://nid.naver.com/nidlogin.login")
            r_sleep()
            
            # 아이디 입력
            id_input = driver.find_element(By.ID, "id")
            pyperclip.copy(self.naver_id.get())
            id_input.click()
            id_input.send_keys(Keys.CONTROL, 'v')
            r_sleep()
            
            # 비밀번호 입력
            pw_input = driver.find_element(By.ID, "pw")
            pyperclip.copy(self.naver_pw.get())
            pw_input.click()
            pw_input.send_keys(Keys.CONTROL, 'v')
            r_sleep()
            
            # 로그인 클릭
            login_btn = driver.find_element(By.ID, "log.login")
            login_btn.click()
            r_sleep()
            
            # 메일 작성 페이지로 이동
            driver.get("https://mail.naver.com/write")
            r_sleep()
            
            # 받는 사람 입력
            mail_email = driver.find_element(By.ID, 'recipient_input_element')
            pyperclip.copy(self.receiver_email.get())
            mail_email.click()
            mail_email.send_keys(Keys.CONTROL, 'v')
            r_sleep()
            
            # 제목 입력
            mail_title = driver.find_element(By.ID, 'subject_title')
            pyperclip.copy(self.subject.get())
            mail_title.click()
            mail_title.send_keys(Keys.CONTROL, 'v')
            r_sleep()
            
            # 본문 입력
            iframe = driver.find_element(By.CSS_SELECTOR, ".editor_body iframe")
            driver.switch_to.frame(iframe)
            
            mail_body = driver.find_element(By.CLASS_NAME, 'workseditor-content')
            pyperclip.copy(self.body.get("1.0", tk.END))
            mail_body.click()
            mail_body.send_keys(Keys.CONTROL, 'v')
            r_sleep()
            
            # iframe 나오기
            driver.switch_to.default_content()
            
            # 전송 버튼 클릭
            send_btn = driver.find_element(By.CLASS_NAME, 'button_write_task')
            send_btn.click()
            r_sleep()
            
            messagebox.showinfo("성공", "이메일이 성공적으로 전송되었습니다!")
            driver.quit()
            
        except Exception as e:
            messagebox.showerror("오류", f"이메일 전송 실패: {str(e)}")
            if 'driver' in locals():
                driver.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = EmailSender(root)
    root.mainloop() 