# Problem

# Maan lo humare paas:

# class BankAccount:

#     def __init__(self, balance):
#         self.__balance = balance

# Ab balance private-style hai:

# account = BankAccount(1000)

# Ye kaam nahi karega:

# print(account.__balance)

# Error aayegi.

# Old Style Solution (Getter Method)

# Java/C++ background wale log aksar aisa karte hain:

# class BankAccount:

#     def __init__(self, balance):
#         self.__balance = balance

#     def get_balance(self):
#         return self.__balance

# Use:

# account = BankAccount(1000)

# print(account.get_balance())

# Output:

# 1000

# Kaam to sahi hai.

# Lekin Python mein ye thoda verbose lagta hai.

# Pythonic Solution → @property
# class BankAccount:

#     def __init__(self, balance):
#         self.__balance = balance

#     @property
#     def balance(self):
#         return self.__balance

# Use:

# account = BankAccount(1000)

# print(account.balance)

# Output:

# 1000

# Notice:

# account.balance

# Hum method call nahi kar rahe:

# account.balance()

# ❌ Nahi

# Bas:

# account.balance

# ✅

# Python internally:

# def balance(self):

# ko call kar deta hai.

# Why useful?

# User ko lagta hai:

# account.balance

# ek normal attribute hai.

# Lekin actually class control kar rahi hoti hai ke value kaise return ho.

# Yani:

# Outside
#    ↓
# account.balance
#    ↓
# @property method
#    ↓
# __balance
# Real Benefit

# Maan lo baad mein tum validation add karna chaho.

# Tum bahar wala code change nahi karte:

# account.balance

# same rehta hai.

# Andar implementation badal sakte ho.

# Quiz

# Code dekho:

# class BankAccount:

#     def __init__(self, balance):
#         self.__balance = balance

#     @property
#     def balance(self):
#         return self.__balance


# account = BankAccount(5000)

# print(account.balance)

# Q1
# Output kya hoga?
# 5000

# Q2

# Ye:

# account.balance
# attribute access lag raha hai.
# Lekin actually Python kis method ko call kar raha hai?
# python property methos ko call kr raha hai is sai hum function ko bina paranthesis kai access kr saktai hai

# Q3

# Agar:
# print(account.__balance)
# likhen to kya hoga aur kyun?
# print account.__balance krta hai tou syntax error ay ga q kai python mai private label element access ksi controller kai through handle hota hai aghr hum directly access krna chahai tou possible tou hai mghr best way nhi hai account._BankAccount__balance krai gai tou balance ki amount ajai gi 

# Ab next level: Read-only vs Writable Property

# @property
# def balance(self):

# Yeh read-only property hai.

# account.balance

# kar sakte ho.

# Lekin:

# account.balance = 5000

# karoge to error aayegi.

# Kyun?

# Kyuki humne sirf getter banaya hai.

# Setter nahi banaya.

# Mini Challenge

# class BankAccount:

#     def __init__(self, balance):
#         self.__balance = balance

#     @property
#     def balance(self):
#         return self.__balance


# account = BankAccount(1000)

# account.balance = 5000
# Questions

# Q1: Kya ye code chalega ya error aayega?
# error ay ga

# Q2: Agar error aayega to kyun?
# yeh overwrite kr raha hai jab kai hum nai read only method use kra hai getter ka use kra hai 

# Q3: Tumhare khayal mein agar hum chahen ke:

# account.balance = 5000

# allow ho,

# to Python ko kis cheez ki zarurat hogi?

# aghr yeh code workable banana hai tou python ko setter ki need hogi jis sai yeh code chl jai  