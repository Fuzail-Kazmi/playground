# Mini Project 1 — Student Record System

# Requirements:

# student = {}

# User se lo:

# Name
# Age
# Grade

# Store karo dictionary mein:

# {
#     "name": ...,
#     "age": ...,
#     "grade": ...
# }

# Phir print karo:

# Student Record


# Name: Fuzail
# Age: 19
# Grade: A

# Bonus Challenge

# Dictionary:

# student = {
#     "name": "Ali",
#     "age": 19,
#     "grade": "A"
# }

# .items() use karke output lao:

# name = Ali
# age = 19
# grade = A

student = {}

name = input("Enter Your Name: ")
age = int(input("Enter Your age: "))
grade = input("Enter Your grade: ")

student["Name"] = name
student["Age"] = age
student["Grade"] = grade

print("Student Record")

for key,value in student.items():
    print(f"{key}: {value}")



# Mini Quiz

# Code:

# student = {
#     "name": "Ali",
#     "age": 19
# }


# student["grade"] = "A"
# del student["age"]

# Final dictionary kya hogi?

# name:Ali
# grade: A