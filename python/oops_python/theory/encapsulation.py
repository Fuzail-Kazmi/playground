# Encapsulation kya hai?

# Simple words mein:

# Class ke data ko directly bahar se access/change karne ke bajaye class ke methods ke through control karna.

# Real-world example: Bank Account

# Tum bank account ka balance directly random jagah se change nahi karna chahte:

# account.balance = -50000

# Instead class khud decide karegi ke balance kaise change ho sakta hai.

# Python mein basic example
# class BankAccount:

#     def __init__(self, balance):
#         self._balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount

#     def show_balance(self):
#         print(self._balance)

# Use:

# account = BankAccount(1000)

# account.deposit(500)
# account.show_balance()

# Output:

# 1500

# Yahan:

# self._balance

# mein _ ek convention hai jo indicate karta hai:

# "Ye internal/protected data hai; normally class ke bahar directly manipulate nahi karna chahiye."

# ⚠️ Important: Python mein _balance technically completely private nahi hota. Ye Java/C++ jaisa strict access control nahi hai.

# Ab actual problem samjho

# Agar hum simply:

# self.balance = balance

# rakh dein, to user directly:

# account.balance = -50000

# kar sakta hai.

# Lekin method ke through:

# account.deposit(500)

# class validation laga sakti hai.

# Yani class ke paas control aa gaya.

# 🧠 Tumhara Quiz

# Code dekho:

# class BankAccount:

#     def __init__(self, balance):
#         self._balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount

#     def show_balance(self):
#         print(self._balance)


# account = BankAccount(1000)

# account.deposit(500)
# account.show_balance()


# Q1
# Output kya hoga?
# 1500

# Q2
# _balance mein _ kyun lagaya gaya?
# yeh isliya lagaya hai q kai hum bata rahy hai kai yeha encapsulation use hoga yeh 1 protected value hai jisay koi bhi bahar sai change na karai is ko srif koi private attribute he change ho sakai 

# Q3
# Agar:
# account.deposit(-200)
# karen, to balance kya hoga aur kyun?
# nhi hoga q kai hum na validation lagai hai kai koi bhi number jo deposit value ho wo 0 sai bari ho tab he deposit ho

# Q4 — Thinking
# deposit() method ke through balance change karna direct:
# account._balance = ...
# se better kyun ho sakta hai?
# q kai yeh ak protect way hai _balance ki value update krna kai liya 

# Ab ek important distinction

# Abhi humne:

# self._balance

# dekha.

# Python mein single underscore _ aur double underscore __ different concepts hain.

# Single underscore
# self._balance

# ➡️ Convention: internal/protected-style

# Double underscore
# self.__balance

# ➡️ Python name mangling karta hai; ye stronger encapsulation mechanism hai.

# Pehle difference
# self._balance

# Single _ → Python convention hai: "ye internal data hai, normally directly access mat karo."

# self.__balance

# Double __ → Python name mangling karta hai. Iska purpose class ke internal attribute ko accidental direct access se protect karna hai.

# Example
# class BankAccount:

#     def __init__(self, balance):
#         self.__balance = balance

#     def show_balance(self):
#         print(self.__balance)


# account = BankAccount(1000)

# account.show_balance()

# Output:

# 1000

# Lekin:

# print(account.__balance)

# normally kaam nahi karega, kyunki __balance name-mangled hai.