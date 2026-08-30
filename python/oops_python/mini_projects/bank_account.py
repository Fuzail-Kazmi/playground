# Mini Challenge — Bank Account

# Khud class banao:

# BankAccount

# Requirements:

# __init__(balance)
# _balance attribute
# deposit(amount)
# withdraw(amount)
# show_balance()

# Rules:
# deposit:

# amount 0 se greater ho → balance increase
# warna → "Invalid Deposit"

# withdraw:

# amount 0 se greater ho aur balance se kam/equal ho → balance decrease
# warna → "Invalid Withdrawal"

# Phir:

# account = BankAccount(1000)

# deposit 500
# withdraw 200
# show balance

# Expected balance:

# 1300

# import time

# class BankAccount:
#     def __init__(self,bank,branch,balance):
#         self.bank = bank
#         self.branch = branch
#         self._balance = balance
    
#     def deposit(self,amount):
#         if amount > 0:
#             self._balance += amount
#         else:
#             print("Invalid Deposit")

#     def withdraw(self,amount):
#         if amount > 0 and amount <= self._balance:
#             self._balance -= amount
#         else:
#             print("Invalid Withdrawal")

#     def show_balance(self):
#         print(time.ctime())
#         print(f"Bank Name: {self.bank} Bank")
#         print(f"Branch Name: {self.branch} Branch")
#         print(f"Your Balance: Rs.{self._balance}")
#         time.sleep(1)
    
# person1 = BankAccount('Meezan','North Karachi',1000)
# person1.show_balance()
# person1.deposit(500)
# person1.show_balance()
# person1.withdraw(200)
# person1.show_balance()

# 🧠 Challenge

# BankAccount

# Requirements:

# __balance use karo
# deposit(amount) method
# show_balance() method
# Deposit sirf tab ho jab amount > 0
# Invalid amount par "Invalid Deposit" print karo

# Phir:

# account = BankAccount(1000)

# account.deposit(500)
# account.show_balance()

# Expected:

# 1500
# Bonus

# Try karo:

# print(account.__balance)

class BankAccount:
    def __init__(self,balance):
        self.__balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid Deposit")

    def show_balance(self):
        print(self.__balance)
    

person1 = BankAccount(1000)
person1.show_balance()
person1.deposit(500)
person1.show_balance()
# print(person1._BankAccount__balance)