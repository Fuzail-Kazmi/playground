# Sabse pehle: self vs cls

# Ab tak tum mostly ye dekhte aaye ho:

# class Student:

#     def __init__(self, name):
#         self.name = name

# Yahan:

# self
# ↓
# current object

# Example:

# student1 = Student("Fuzail")
# student2 = Student("Ali")

# self kabhi student1 ko refer karega, kabhi student2 ko.

# Class Variable Example
# class Student:

#     school = "ABC School"

# Ye variable kisi object ka nahi.

# Ye poori class ka hai.

# Problem

# Agar hume class-level data ke saath kaam karna ho to?

# Example:

# class Student:

#     school = "ABC School"

# Aur hum school change karna chahte hain.

# @classmethod
# class Student:

#     school = "ABC School"

#     @classmethod
#     def change_school(cls, new_school):
#         cls.school = new_school

# Yahan:

# cls
# ↓
# Student class

# Use:

# Student.change_school("XYZ School")

# Ab:

# print(Student.school)

# Output:

# XYZ School
# Kya ho raha hai?

# Instance method:

# def introduce(self):

# Object ke saath kaam karta hai.

# Class method:

# @classmethod
# def change_school(cls):

# Class ke saath kaam karta hai.

# Visual
# Student Class
# │
# ├── school
# │
# ├── student1
# ├── student2
# └── student3

# self

# student1

# ya

# student2

# ko refer karta hai.

# cls

# Student

# ko refer karta hai.

# Quiz

# Code run kiye bina batao:

# class Student:

#     school = "ABC School"

#     @classmethod
#     def change_school(cls, name):
#         cls.school = name


# student1 = Student()

# Student.change_school("XYZ School")

# print(Student.school)
# print(student1.school)

# Q1
# Pehla output kya hoga?
# ABC School

# Q2
# Doosra output kya hoga?
# XYZ School

# Q3
# cls.school = name

# kis cheez ko update kar raha hai?
# Class Variable

# Q4 (Thinking)
# change_school()
# ko @classmethod banana zyada logical hai ya normal instance method?
# i think classmethod its very useful q kai yeh class ko target krta hai object ko nhi tou jaisa class mai koi class ka variabel ho jo har student kai object mai use ho or hum globally apni class mai sai us varible ko update kr sakai

# Instance Method
# def introduce(self):

# self use karta hai.

# Current object ke data ke saath kaam karta hai.

# Class Method
# @classmethod
# def change_school(cls):

# cls use karta hai.

# Class ke data ke saath kaam karta hai.

# Static Method

# Ab socho hume koi aisa function chahiye:

# check_pass_marks(marks)

# Jo:

# Object ka data use nahi karta
# Class ka data use nahi karta

# Sirf calculation karta hai.

# Example:

# marks >= 40

# to Pass

# warna Fail

# Example
# class Student:

#     @staticmethod
#     def check_pass(marks):

#         if marks >= 40:
#             return "Pass"

#         return "Fail"

# Use:

# print(Student.check_pass(70))
# print(Student.check_pass(20))

# Output:

# Pass
# Fail
# Notice

# Method ke andar:

# self

# nahi hai.

# Aur:

# cls

# bhi nahi hai.

# Sirf:

# marks

# hai.

# Kyun banaya?

# Ye function class ke andar logically belong karta hai:

# Student
#     ↓
# check_pass()

# Lekin usse object ya class data ki zarurat nahi.

# Real Difference
# Instance Method
# student1.introduce()

# Uses:

# self
# Class Method
# Student.change_school()

# Uses:

# cls
# Static Method
# Student.check_pass()

# Uses:

# Neither self nor cls
# Visual
# Instance Method
#       ↓
# Object Data

# Class Method
#       ↓
# Class Data

# Static Method
#       ↓
# Independent Utility Function
# Quiz

# Code run kiye bina batao:

# class Calculator:

#     @staticmethod
#     def add(a, b):
#         return a + b


# print(Calculator.add(10, 20))

# Q1
# Output kya hoga?
# 30

# Q2
# Ye method:
# add()
# self use kar raha hai?
# nhi

# Q3
# add()
# cls use kar raha hai?
# nhi

# Q4 (Thinking)

# check_pass()
# add()
# calculate_tax()
# jaisi cheezein @staticmethod kyun banai ja sakti hain?
# yeh isliya banai ja sakti hai q kai in cheezo mai intence hona zaruri nhi tabhi yeh bina kisi class or object intence kai ban sakti hai staticmethod ka use kr kai 

# Ab tum teenon compare kar sakte ho
# class Example:

#     def instance_method(self):
#         pass

#     @classmethod
#     def class_method(cls):
#         pass

#     @staticmethod
#     def static_method():
#         pass

# Instance Method
# self
# ↓
# Current Object

# Class Method
# cls
# ↓
# Current Class

# Static Method
# No self
# No cls