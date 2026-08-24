# Mini Challenge — Number Processor

# Given:

# numbers = [10, 20, 30, 40, 50]

# List comprehension use karke:

# [20, 40, 60, 80, 100]

# banao.

# Phir enumerate use karke print karo:

# 1 -> 20
# 2 -> 40
# 3 -> 60
# 4 -> 80
# 5 -> 100

# numbers = [10, 20, 30, 40, 50]
# number = [n * 2 for n in numbers]
# for i,r in enumerate(number,start=1):
#     print(f"{i} -> {r}")


# *args Practice
# def total(*numbers):

# Function banao jo jitne bhi numbers milen unka sum return kare.

# Example:

# total(10, 20)

# Output:

# 30

# Example:

# total(10, 20, 30, 40)

# Output:

# 100

# def total(*numbers):
#     num = 0
    
#     for numb in numbers:
#         num = num + numb
    
#     print(num)


# **kwargs Practice
# def show_student(**data):

# Call:

# show_student(
#     name="Fuzail",
#     age=19,
#     grade="A"
# )

# Output:

# name = Fuzail
# age = 19
# grade = A

# def show_student(**data):
#     for key,value in data.items():
#         print(f"{key} = {value}")
# show_student(name = "Fuzail",age = 19, grade = "A")