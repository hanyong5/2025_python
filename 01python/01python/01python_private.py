class Patient:
    def __init__(self,name):
        self.name = name
        self.__temp = 36.5 #private

    def set_temp(self,temp):
        if 35 <= temp <= 42:
            self.__temp = temp
            print(f'체온이 {temp}도로 설정되었습니다.')
        else:
            print('체온범위가 이상합니다.')

    def get_temp(self):
        return self.__temp
    

name = input("환자이름을 입력하세요")
patient = Patient(name)

try:
    temp = float(input("체온을 입력하세요"))
    patient.set_temp(temp)
except ValueError:
    print("온도 값 형식으로 입력하세요")

print(f'{patient.name}님의 현재 체온은 {patient.get_temp()} 도 입니다.')
