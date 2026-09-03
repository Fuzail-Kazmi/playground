# Composition.

# class Animal:
#     pass

# class Dog(Animal):
#     pass

# Yahan relation hai:

# Dog IS-A Animal

# Dog ek Animal hai.

# Composition

# Composition mein relation hota hai:

# Car HAS-A Engine

# Car engine nahi hai.

# Car ke paas engine hai.

# Real Example
# class Engine:

#     def start(self):
#         print("Engine Started")


# class Car:

#     def __init__(self):
#         self.engine = Engine()

# Yahan:

# self.engine = Engine()

# matlab:

# Car ke andar Engine object rakha gaya hai
# Use
# car1 = Car()

# car1.engine.start()

# Output:

# Engine Started
# Visual

# Inheritance:

# Animal
#    ↑
#  Dog

# Dog parent se inherit kar raha hai.

# Composition:

# Car
#  │
#  └── Engine

# Car ke andar Engine object hai.

# Real World Examples
# Car HAS-A Engine
# Computer HAS-A CPU
# House HAS-A Room
# Library HAS-A Books
# Student HAS-A Address

# Ye sab Composition hain.

# Inheritance vs Composition
# Inheritance
# Dog IS-A Animal
# Cat IS-A Animal
# Composition
# Car HAS-A Engine
# Computer HAS-A CPU
# Mini Quiz

# Code run kiye bina batao:

# class Engine:

#     def start(self):
#         print("Engine Started")


# class Car:

#     def __init__(self):
#         self.engine = Engine()


# car1 = Car()

# car1.engine.start()

# Q1
# Output kya hoga?
# Engine Started

# Q2
# self.engine = Engine()
# kya ek naya object create ho raha hai?
# yeha self ka use ho raha hai or 1 new object use ho raha hai 

# Q3
# Relation batao:
# Car IS-A Engine
# ya
# Car HAS-A Engine
# Car IS-A Engine ak inheritance method hai is mai hum whole class ko an argument leta hai jis sai child kai pass bhi parent ki ablity ajati hai or hum DRY code sai bach jatai hai Car HAS-A Engine ak composition method hai is mai hum parent ko child mai use tou krta hai yeh smj lo Computer HAS-A CPU Student HAS-A Address 

# Q4 (Thinking)
# Tumhare khayal mein:
# class Student
# class Address
# mein inheritance zyada logical hai ya composition?
# Aur kyun?
# is mai composition zayada logical hai q kai 1 Address kai multiple student bhi ho saktai hai 