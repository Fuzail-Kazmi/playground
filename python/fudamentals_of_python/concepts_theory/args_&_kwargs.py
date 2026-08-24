# *args

# def add(*numbers):
#     print(numbers)

# add(10, 20)
# add(10, 20, 30)
# add(10, 20, 30, 40)

# def greet(name):
#     print(name)

# greet("Fuzail")

# Yahan:

# 1 parameter
# 1 argument

# 2 Parameters

# def info(name, age):
#     print(name)
#     print(age)

# info("Fuzail", 19)

# Yahan:

# 2 parameters
# 2 arguments

# Problem

# Agar mujhe numbers add karne hain:

# add(10, 20)

# phir:

# add(10, 20, 30)

# phir:

# add(10, 20, 30, 40)

# To kitne parameters banaunga?

# Har baar function change karna padega.

# Solution — *args
# def add(*numbers):
#     print(numbers)

# add(10, 20)

# Output:

# (10, 20)

# Notice:

# Tuple mila
# More Example
# def add(*numbers):
#     print(numbers)

# add(10, 20, 30, 40)

# Output:

# (10, 20, 30, 40)
# Important Rule
# def add(*numbers):

# Matlab:

# Jo bhi extra arguments aayengi
# unko tuple mein pack kar do

# Isliye numbers tuple hota hai.

# Loop With *args
# def add(*numbers):

#     total = 0

#     for number in numbers:
#         total = total + number

#     print(total)

# add(10, 20, 30)

# Output:

# 60
# Visual
# add(10, 20, 30)

# Python internally:

# numbers = (10, 20, 30)

# jaisa treat karta hai.

# Quiz 1

# def show(*data):
#     print(data)

# show("Ali", "Ahmed")

# ("Ali", "Ahmed")

# Quiz 2

# def show(*data):
#     print(len(data))

# show(10, 20, 30)
# 3

# Quiz 3

# Output?

# def total(*numbers):

#     result = 0

#     for number in numbers:
#         result = result + number

#     print(result)

# total(5, 10)
# 15

# Thinking Question

# Ye:

# def show(*data):

# mein *data ka actual purpose kya hai?

# Apni language mein explain karo:

# Without *args kya limitation thi?
# *args us problem ko kaise solve karta hai?

# def show(*data): ka purpose yeh hai kai jitny chahay utna arguments de or without *args ki limitation 2 parameters hogi q kai hum kya har bar new function banai ga is sai acha hai unlimited arguments kai hisab sai yeh 1 2 3 4 arguments kai hisab sai bhi *args de jis sai hum jitni chahai utni arguments de saktai hai 

# Quick Quiz

# Output?

# def show(*values):
#     print(values[1])

# show(10, 20, 30)
# 20

# Output?

# def show(*data):
#     print(type(data))

# show("A", "B")
# tuples

# **kwargs

# Ab socho:

# *args kya karta tha?

# add(10, 20, 30)

# ko tuple mein pack karta tha:

# (10, 20, 30)
# Dictionary Version
# def show(**data):
#     print(data)

# show(name="Fuzail", age=19)

# Output:

# {'name': 'Fuzail', 'age': 19}

# Notice:

# *args  -> Tuple
# **kwargs -> Dictionary
# Example
# def student(**info):
#     print(info)

# student(name="Ali", age=19, grade="A")

# Output:

# {
#     'name': 'Ali',
#     'age': 19,
#     'grade': 'A'
# }
# Access Values
# def student(**info):
#     print(info["name"])

# student(name="Ali", age=19)

# Output:

# Ali
# Loop
# def student(**info):

#     for key, value in info.items():
#         print(key, value)

# student(name="Ali", age=19)

# Output:

# name Ali
# age 19
# Memory Trick
# *args
# =
# Unlimited positional arguments
# =
# Tuple

# **kwargs
# =
# Unlimited keyword arguments
# =
# Dictionary

# Quiz 1

# Output?

# def show(**data):
#     print(data)

# show(name="Ali")
# {
#     name: "Ali"
# }

# Quiz 2

# Output?

# def show(**data):
#     print(data["age"])

# show(name="Ali", age=19)
# 19

# Quiz 3

# Output?

# def show(**data):
#     print(len(data))

# show(name="Ali", age=19, grade="A")
# 3

# Thinking Question

# Apni language mein explain karo:

# *args aur **kwargs mein kya difference hai?

# *args tuple kyun banta hai?

# **kwargs dictionary kyun banta hai?

# *args humaray variable ko tuple mai pack kr deta hai or hum args mai value deta hai 
# **kwargs humaray variable ko dictionary mai pack kr deta hai or hum kwargs mai key value dono deta hai 
# *args and **kwargs mai multiple aruguments dena kai liya lagatai hai 
# args tuples isliya banata hai q kai hum us ko value deta hai 
# kwargs dictionary isliya banata hai q kai hum us ko key value dono deta hai 