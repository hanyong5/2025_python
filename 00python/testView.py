import requests
from datetime import datetime,timedelta
from bs4 import BeautifulSoup
import time

url = 'http://finance.naver.com/item/sise_day.naver?code=005930'
headers = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'

data = []
today = datetime.today()
one_month_ago = today - timedelta(days=30)
response = requests.get("http://finance.naver.com/item/sise_day.naver?code=005930",headers=headers)
html = response.text
print(html)


# for page in range(1,5):
#     response = requests.get(f'{url}&page={page}',headers)
#     # print(f'{url}&page={page}')
#     html = response.text
#     soup = BeautifulSoup(html,"html.parser")
#     table = soup.find('table',class_="type2")
#     # rows = table.find_all('tr')
#     print(html)

