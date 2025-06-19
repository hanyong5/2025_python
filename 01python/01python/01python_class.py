
# class Account:
    
#     def __init__(self,name,amount):
#         self.balance = amount 
#         self.name = name

#     # def __init__(self):
#     #     self.balance = 10000
#     #     self.name = '홍길동'

#     def deposit(self,amount):
#         self.balance += amount
#         return self.balance
    
#     def withdraw(self,amount):
#         self.balance -= amount
#         return self.balance




# hong = Account("홍길동",10000) #초기값
# value=hong.deposit(1000)
# print(f'{hong.name}님의 현재잔액은 {value}원 입니다.')


# hong = Account()
# value=hong.deposit(1000)
# print(f'현재 통장 잔액은{hong.name} {value}원 입니다.')



class Account1:
    def __init__(self,name='무명',amount=0):
        self.name = name #public
        self.__balance = amount #private

    def deposit(self,amount):
        self.__balance += amount
        return self.__balance
    
    def withdraw(self,amount):
        self.__balance -= amount
        return self.__balance
    
    def get_balance(self):
        return self.__balance

# a1 = Account1()
# a1.name = '이순신'
# a1.balance = 10000

a1 = Account1("이순신",10000)
a1.deposit(1000)
print(f'{a1.name}님의 계좌의 금액은 {a1.get_balance()}원 입니다.')

