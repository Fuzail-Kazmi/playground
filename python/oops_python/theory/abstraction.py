# Abstraction


# Car
# Tum car drive karte ho.

# Tumhe pata hai:

# Start Button Dabao
# Brake Lagao
# Steering Ghumao

# Lekin:

# Fuel Injection System
# Engine Timing
# Spark Plug Logic

# ka implementation jaana zaruri nahi.

# Ye abstraction hai.

# Programming Mein

# Maan lo:

# class Animal:

# Har animal sound nikalta hai.

# Lekin:

# Dog → Woof
# Cat → Meow
# Cow → Moo

# Hum parent class mein ye force karna chahte hain:

# Har child ko sound() method banana hi padega

# Yahan Abstraction use hoti hai.

# Example
# from abc import ABC, abstractmethod

# class Animal(ABC):

#     @abstractmethod
#     def sound(self):
#         pass

# Ab:

# class Dog(Animal):

#     def sound(self):
#         print("Woof")

# Ye valid hai.

# Lekin agar:

# class Dog(Animal):
#     pass

# aur:

# dog = Dog()

# to Python error dega.

# Kyun?

# Kyuki:

# sound()

# implement nahi kiya.

# Abstraction Ka Main Purpose
# Blueprint bana do
# Rules define kar do
# Child classes ko force karo
# Visual
# Animal (Abstract)

#     sound()
#        ↑

# Dog
# Cat
# Cow

# Har child ko:

# sound()

# likhna padega.

# Quiz

# Code run kiye bina batao:

# from abc import ABC, abstractmethod

# class Animal(ABC):

#     @abstractmethod
#     def sound(self):
#         pass


# class Dog(Animal):

#     def sound(self):
#         print("Woof")


# dog = Dog()

# dog.sound()

# Q1
# Output kya hoga?
# Woof

# Q2
# Agar Dog ke andar:
# def sound(self):
# hata dein to object create hoga ya error aayega?
# Error ayga q kai abstract method blueprint create kr deta hai child ko force krta hai implementation kai liya 

# Q3
# Inheritance
# aur
# Abstraction
# mein basic difference kya lag raha hai?
# basic difference yehi hai kai abstraction child ko force krta hai implemntation kai liya jab kai Inheritence mai koi aesa scene nhi hai 