# Module Kya Hota Hai?

# Simple language mein:

# Ek Python file = Ek Module

# Example:

# math_utils.py
# def add(a, b):
#     return a + b

# def sub(a, b):
#     return a - b

# Ye poori file ek module hai.

# Import Karna

# Agar same folder mein:

# main.py
# import math_utils

# print(math_utils.add(10, 20))

# Output:

# 30
# Specific Function Import
# from math_utils import add

# print(add(10, 20))

# Output:

# 30
# Multiple Imports
# from math_utils import add, sub
# Alias
# import math_utils as mu

# print(mu.add(10, 20))

# Output:

# 30
# Built-in Modules

# Python ke ready-made modules:

# import random
# import math
# import os

# Examples:

# import random

# print(random.randint(1, 10))
# import math

# print(math.sqrt(25))

# Output:

# 5.0
# Quick Quiz

# Q1
# import math

# print(math.sqrt(16))

# Output?

# 4.00

# Q2
# from math import sqrt

# print(sqrt(81))

# Output?

# 9.00

# Q3 (Thinking)

# Difference batao:

# import math

# math.sqrt(25)

# aur

# from math import 

# sqrt(25)

# Dono ka result same hai.

# Phir syntax mein difference kya hai?

# math.sqrt() and sqrt() dono mai koi difference nhi dono he number ka square root nikl tai hai or floot mai result return krta hai ab ap socho gai dono ko alag alag tareeka sai use ho raha hai math.sqrt() and sqrt() tou in mai just import ka differce hai hum kr rahy hai import math math.sqrt() means kai math ko leaoo is file mai or hum phr math.sqrt kr rahy hai kai math kai andar sqrt function hai wou yeha use hoga or isi tarha from math import sqrt() its means kai math kai andar sai import kro or hum phr nechay direct function use kr rahy hai sqrt() bas import differce hai baki dono work same he krta hai ap import math kro yeh from math import use kro 

# from calculator import

# if __name__ == "__main__":
#     print("Calculator Method Starting")

# print(__name__)

# Ab Last Important Module Concept
# __name__

# Quiz:

# Maan lo file hai:

# calculator.py
# print("Calculator Started")

# Aur hum run karte hain:

# python calculator.py

# Output:

# Calculator Started

# Normal.

# Ab calculator.py mein ye add karte hain:

# print(__name__)

# Question:

# Agar hum directly calculator.py run karein to output kya hoga?

# Calulator Started
# __main__

# Second Question

# File:

# # calculator.py

# print(__name__)

# Aur:

# # main.py

# import calculator

# Ab:

# python main.py

# chalaya.

# Question:

# Ab calculator.py ke andar __name__ ki value kya hogi?

# calculator

# Thinking Question

# Ye kyun useful ho sakta hai?

# Hint:

# Kabhi kabhi hum chahte hain:

# Agar file direct run ho:
#     kuch code chale

# Agar file import ho:
#     wo code na chale

# Bas in 3 sawalon ka jawab do.

# yar yeh useful ka mujha nhi pata q kai mujha yeh smj tak nhi arha hai or baki upr jo 2 jawab diya code run kr kai diya q kai mujha is method ka naam nhi pata kya yeh dunder method hai or yeh q zaruri hai matlab is ka usecase kya hai 