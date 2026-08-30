# OOP Mini Project 1

# Ab syntax enough ho gaya.

# Project:

# Student Profile System

# Requirements:

# Class: Student

# Attributes:

# name
# age

# Methods:

# introduce()

# Output:

# My name is Ali and I am 19 years old
# Create 3 Objects

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old")

student1 = Student("Fuzail",19)
student2 = Student("Sara",18)
student3 = Student("Ali",22)

student1.introduce()
student2.introduce()
student3.introduce()