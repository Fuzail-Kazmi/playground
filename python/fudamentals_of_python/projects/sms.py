# Project: Student Result Management System
# Requirements

# User se lo:

# Student Name
# Student Marks
# Function 1
# check_grade(marks)

# Ye return kare:

# A
# B
# C
# D
# Fail
# Function 2
# show_result(name, marks, grade)

# Ye result display kare.

# Example:

# Student Name: Fuzail
# Marks: 85
# Grade: B
# Example Flow

# Input:

# Name: Fuzail
# Marks: 85

# Processing:

# grade = check_grade(85)

# returns:

# B

# Then:

# show_result("Fuzail", 85, "B")

# Output:

# Student Name: Fuzail
# Marks: 85
# Grade: B


def check_grade(marks):
    if marks < 0 or marks > 100:
        return 'Enter A Valid Marks'
    elif marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    else:
        return 'Fail'

def show_result(name,marks,grade):
    print(f"Name: {name}")
    print(f"Marks: {marks}")
    print(f"Grade: {grade}")

name = input("Enter Your Name: ")
marks = int(input("Enter your Marks To Check Your Grade: "))
grade = check_grade(marks)
result = show_result(name,marks,grade)
