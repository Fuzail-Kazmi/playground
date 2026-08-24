# Mini Project — Student Report System

# Requirements:

# students = ["Ali", "Ahmed", "Sara"]
# grades = ["A", "B", "A+"]

# Task:

# zip() use karo
# enumerate(start=1) use karo
# Output:
# Ali - A
# Ahmed - B
# Sara - A+

# Bonus:

# students = [student.lower() for student in students]

# use karke names lowercase karo.

students = ["Ali", "Ahmed", "Sara"]
grades = ["A", "B", "A+"]
students = [student.lower() for student in students]

# for s,g in zip(students,grades):
#     print(f"{s} - {g}")

for i, (s, g) in enumerate(zip(students, grades), start=1):
    print(f"{i}. {s} - {g}")