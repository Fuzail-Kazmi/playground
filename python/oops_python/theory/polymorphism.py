# Method Overriding kya hai?

# Simple:

# Child class parent ke existing method ko apne version se replace kar deti hai.

# Example:

# class Student:

#     def introduce(self):
#         print("I am a student")


# class CollegeStudent(Student):

#     def introduce(self):
#         print("I am a college student")

# Ab:

# student = Student()
# college_student = CollegeStudent()

# student.introduce()
# college_student.introduce()

# Output:

# I am a student
# I am a college student
# Yahan important kya hua?

# CollegeStudent ne Student se introduce() inherit kiya tha.

# Lekin CollegeStudent mein humne same naam ka method dobara bana diya:

# def introduce(self):

# To jab:

# college_student.introduce()

# chalta hai, Python child class ka method use karta hai.

# Real-world example

# Socho:

# Vehicle
#    ↓
# Car
#    ↓
# Bike

# Parent:

# class Vehicle:

#     def start(self):
#         print("Vehicle starts")

# Car apne tareeqe se start hoti hai:

# class Car(Vehicle):

#     def start(self):
#         print("Car starts with a key")

# Bike:

# class Bike(Vehicle):

#     def start(self):
#         print("Bike starts with a button")

# Same method:

# start()

# Lekin different behavior.

# Yehi method overriding hai.

# 🧠 Tumhara Quiz

# Code dekho:

# class Animal:

#     def sound(self):
#         print("Animal makes a sound")


# class Dog(Animal):

#     def sound(self):
#         print("Dog barks")


# animal = Animal()
# dog = Dog()

# animal.sound()
# dog.sound()

# Batao:

# Q1: Dono outputs kya honge?
# Animal makes a sound
# Dog barks

# Q2: Dog ne sound() ko override kiya ya inherit kiya?
# override

# Q3: Agar Dog ke andar sound() method hata dein, to dog.sound() kya karega?

# Animal makes a sound q kai dog phr apny parent sai inherit karai ga

# Ab next level: Polymorphism

# Naam thoda advanced lagta hai, lekin concept simple hai:

# Same method call, different objects → different behavior.

# Example:

# class Dog:
#     def sound(self):
#         print("Bark")


# class Cat:
#     def sound(self):
#         print("Meow")


# animals = [Dog(), Cat()]

# for animal in animals:
#     animal.sound()

# Output:

# Bark
# Meow

# Humne loop mein same:

# animal.sound()

# likha.

# Lekin object Dog ho to Bark, aur Cat ho to Meow.

# Ye polymorphism ka basic idea hai.

