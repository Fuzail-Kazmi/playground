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
# Eating

# Q2: Dog ke andar eat() method nahi hai, phir dog.eat() kaise kaam kar raha hai?
# Dog Inheritance use kr raha hai like Dog kai parameter mai hum class ko as an arguemnt bhej rahy hai jis sai us ko Animal Class kai saray attributes sab already Dog Class mai bhi ajai bar bar code likhna na paray

# Q3: Is example mein:

# Animal = ?
# Dog = ?

# Apni language mein explain karo.

# Question no 3 smj nhi aya kya sawal hai yeh phr bhi mai bata deta hu aghr jawab question kai mutabik nhi ho tou question phr pooch lena khair Animal ak class hai or us kai andar ak method banaya hai eat kai naam ka ab Dog ak animal hai tou Dog ki ak class banai us mai Animal class ko inherit kr liya q kai animal koi bhi ho kuch cheezy tou same hoti hai like eat,sleep,walk so Dog kai andar Animal Class ko inherit kr liya or phr Dog class sai object banaya or eat wala method use kr liya 

