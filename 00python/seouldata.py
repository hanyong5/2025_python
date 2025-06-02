import csv

file = open('seouldata2.csv','r',encoding='euc-kr')
data = csv.reader(file,delimiter=",")

for row in data:
    print(row)

file.close()