# Perfect. Ab hum __str__() start karte hain.

# Problem

# Abhi agar tum ye code likho:

# class Student:

#     def __init__(self, name):
#         self.name = name


# student1 = Student("Fuzail")

# print(student1)

# Output kuch aisa aayega:

# <__main__.Student object at 0x7f8a...>

# Ya koi similar memory address.

# Sawal

# Tumhare khayal mein:

# print(student1)

# ko kaise pata chala kya print karna hai?

# Answer:

# Python internally ek special method call karta hai:

# __str__()

# Agar class ke andar __str__() nahi milta, to default ugly object representation print kar deta hai.

# Example
# class Student:

#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return f"Student Name: {self.name}"


# student1 = Student("Fuzail")

# print(student1)

# Output:

# Student Name: Fuzail
# Kya hua?

# Jab:

# print(student1)

# chala,

# Python ne internally:

# student1.__str__()

# call kiya.

# Aur jo string return hui usse print kar diya.

# Important

# __str__() ke andar:

# return

# hona chahiye.

# Ye:

# print(...)

# nahi karta.

# Galat:

# def __str__(self):
#     print(self.name)

# Sahi:

# def __str__(self):
#     return self.name
# Real Example
# class Student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"Student: {self.name}, Age: {self.age}"


# student1 = Student("Fuzail", 19)

# print(student1)

# Output:

# Student: Fuzail, Age: 19
# Quiz

# Code run kiye bina batao:

# class Student:

#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return f"Hello {self.name}"


# student1 = Student("Ali")

# print(student1)
# Q1

# Output kya hoga?

# Q2

# Jab:

# print(student1)

# chala,

# Python internally kis method ko call karega?

# Q3

# Agar hum __str__() method hata dein, to output kis type ka aayega?

# Apni language mein jawab do.