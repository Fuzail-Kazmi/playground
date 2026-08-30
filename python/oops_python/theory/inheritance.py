# 1. Inheritance kya hai?

# Simple language mein:

# Ek class doosri class ke attributes aur methods ko reuse kar sakti hai.

# Example:

# class Student:
#     def introduce(self):
#         print("I am a student")


# class CollegeStudent(Student):
#     pass

# Yahan:

# Student          → Parent Class
# CollegeStudent   → Child Class

# CollegeStudent, Student se inherit kar rahi hai.

# Ab:

# student = CollegeStudent()

# student.introduce()

# Output:

# I am a student

# Humne CollegeStudent ke andar introduce() likha hi nahi, phir bhi wo method available hai.

# Kyun?

# Kyuki CollegeStudent ne Student se inherit kiya hai.

# Real-world example

# Socho:

# Animal
#   ↓
# Dog
#   ↓
# Cat

# Animal mein common cheezein:

# eat()
# sleep()

# Dog aur Cat dono ko ye cheezein chahiye.

# Har class mein dobara:

# eat()
# sleep()

# likhne ki zarurat nahi.

# Parent class mein common functionality rakho aur child classes inherit kar lo.

# Ye code reuse / DRY ka important use case hai.

# Quiz 1

# Code dekho:

# class Animal:

#     def eat(self):
#         print("Eating")


# class Dog(Animal):
#     pass


# dog = Dog()

# dog.eat()
# Questions:

# Q1: Output kya hoga?

# Q2: Dog ke andar eat() method nahi hai, phir dog.eat() kaise kaam kar raha hai?

# Q3: Is example mein:

# Animal = ?
# Dog = ?

# Apni language mein explain karo.

# class Animal:

#     def eat(self):
#         print("Eating")

# class Dog(Animal):
#     pass

# dog = Dog()
# dog.eat()