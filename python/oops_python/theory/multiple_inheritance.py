# Multiple Inheritance

# Ab tak tumne inheritance aise dekhi:

# class Animal:
#     pass

# class Dog(Animal):
#     pass

# Yahan:

# Dog → 1 Parent

# Isko Single Inheritance kehte hain.

# Multiple Inheritance

# Ab socho:

# class Father:
#     pass

# class Mother:
#     pass

# class Child(Father, Mother):
#     pass

# Yahan:

# Child
#  ↑    ↑
# Father Mother

# Child ke paas 2 parents hain.

# Isko Multiple Inheritance kehte hain.

# Example
# class Father:

#     def skill1(self):
#         print("Driving")


# class Mother:

#     def skill2(self):
#         print("Cooking")


# class Child(Father, Mother):
#     pass


# child = Child()

# child.skill1()
# child.skill2()

# Output:

# Driving
# Cooking
# Kya hua?

# Child ne inherit kiya:

# Father → skill1()
# Mother → skill2()

# Isliye Child dono methods use kar sakta hai.

# Real Life Example
# SmartPhone

# HAS:
# Calling Features
# Camera Features

# Ya:

# StudentAthlete

# Student Features
# Athlete Features

# Kabhi kabhi ek class ko multiple sources se behavior chahiye hota hai.

# Problem

# Agar dono parents mein same method ho to?

# Example:

# class Father:

#     def introduce(self):
#         print("Father")


# class Mother:

#     def introduce(self):
#         print("Mother")


# class Child(Father, Mother):
#     pass

# Ab:

# child = Child()
# child.introduce()

# Kya print hoga?

# Yahin se next topic:

# MRO
# (Method Resolution Order)

# aata hai.

# Python decide karta hai:

# Pehle Father check karo
# Phir Mother
# Rule (abhi ke liye)
# class Child(Father, Mother):

# Python generally:

# Left → Right

# order mein parents check karta hai.

# To:

# child.introduce()

# Output:

# Father

# hoga.

# Quiz

# Code run kiye bina batao:

# class A:

#     def hello(self):
#         print("A")


# class B:

#     def world(self):
#         print("B")


# class C(A, B):
#     pass


# obj = C()

# obj.hello()
# obj.world()

# Q1
# Pehla output kya hoga?
# A

# Q2
# Doosra output kya hoga?
# B

# Q3
# C ke paas apna koi method nahi.
# Phir bhi:
# obj.hello()
# obj.world()
# kaise chal rahe hain?
# C Mulitple Inhertience use kr raha hai apny parent classes sai method inherit kr raha hai

# Q4 (Thinking)
# class C(A, B):
# ki jagah:
# class C(B, A):
# likh dein,
# to hello() aur world() chalne par koi farq padega ya nahi?
# nhi padega q kai hum obj.hello() phely call kr raha hai baad mai obj.world call kr rahy hai 