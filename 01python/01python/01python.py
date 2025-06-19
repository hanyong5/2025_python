balance = 0
balance1 = 0

def deposit(amount):
    # balance = 1000
    global balance
    balance += amount
    return balance

def withdraw(amount):
    global balance
    balance -= amount
    return balance

def deposit1(amount):
    # balance = 1000
    global balance1
    balance1 += amount
    return balance1

def withdraw1(amount):
    global balance1
    balance1 -= amount
    return balance1

print("춘식입금 : ",deposit(1000))
print("춘식출금 : ",withdraw(500))


print("길동입금 : ",deposit1(2000))
print("길동출금 : ",withdraw1(500))

print("춘식계좌 : ",balance)
print("길동계좌 : ",balance1)


class Account:
    def __init__(self):
        self.balance = 0
    
    def deposit(self,amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self,amount):
        self.balance -= amount
        return self.balance
    
print("---"*20)

hong = Account()
print("홍입금 : ",hong.deposit(10000))
print("홍출금 : ",hong.withdraw(1000))
print("홍출금 : ",hong.withdraw(1000))
print("홍출금 : ",hong.withdraw(1000))
print("홍계좌",hong.balance)
print("---"*20)

han = Account()
print("한입금 : ",han.deposit(10000))
print("한출금 : ",han.withdraw(9000))




