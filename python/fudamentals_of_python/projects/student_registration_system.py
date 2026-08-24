# Project 1 — Student Registration System

# Requirements:

# User se student name lo
# students.txt mein save karo
# Append mode use karo
# Har student new line mein save ho
# Success message print karo
# Save karne ke baad saare students bhi print karo

# Example:

# Enter Student: Ali

# Output:

# Student Saved Successfully

# Students:
# Ali
# Ahmed
# Sara
# Condition

# Is project mein:

# with open()

# use karna hai.

# import os 
# path = os.getcwd()
# print(path)

# name = input("Enter Student: ")

# with open('student.txt','a') as file:
#     file.write(name + '\n')

#     print("Student Saved Successfully")


with open('student.txt','r') as file:
    data = file.readlines()

print("Students:")

for student in data:
    print(student.strip())


# print("Students:")
# data = [s for s in data]
# print(data)

# print("Students:")
# string = "\n".join(data)
# print(string)