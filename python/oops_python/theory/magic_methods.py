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
# Hello Ali

# Q2
# Jab:
# print(student1)
# chala,
# Python internally kis method ko call karega?
# python internally __str__ method ko call karega or aghr python ko method na milay tou wo default ugly object dega 

# Q3
# Agar hum __str__() method hata dein, to output kis type ka aayega?
# Apni language mein jawab do.
# default ugly object


# class Student:

#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return self.name


# student1 = Student("Fuzail")
# student2 = Student("Ali")

# print(student1)
# print(student2)

# Q1
# Dono outputs kya honge?
# Fuzail
# Ali

# Q2
# return self.name
# mein self pehle kis object ko refer karega aur phir kis object ko?
# self current object ka instance hota hai mean wou class mai current object ko refer krta hai is mai student1 self ki jaga lega tou name Fuzail ho jai ga student2 mai Ali 

# __len__() Dunder Method

# Abhi tak tumne use kiya hai:

# numbers = [1, 2, 3]

# print(len(numbers))

# Output:

# 3

# Sawal:

# Python ko kaise pata chala ke list ki length 3 hai?

# Answer:

# Python internally:

# numbers.__len__()

# call karta hai.

# Example
# class Students:

#     def __init__(self):
#         self.names = ["Ali", "Ahmed", "Sara"]

#     def __len__(self):
#         return len(self.names)


# students = Students()

# print(len(students))

# Output:

# 3
# Kya hua?

# Jab:

# len(students)

# chala,

# Python ne internally:

# students.__len__()

# call kiya.

# Aur jo value return hui woh print kar di.

# Quiz

# Code run kiye bina batao:

# class Team:

#     def __init__(self):
#         self.players = ["A", "B", "C", "D"]

#     def __len__(self):
#         return len(self.players)


# team = Team()
# print(len(team))


# Q1
# Output kya hoga?
# 4

# Q2
# Jab:
# len(team)
# chala,
# Python internally konsa method call karega?
# python internally __len__ method use krai ga 

# Q3
# Agar __len__() method hata dein to:
# len(team)
# par kya hoga
# Apni language mein jawab do.
# Error raise krai ga TypeError: object of type 'Team' has no len() 

# __repr__() method.

# Tum abhi jaante ho:

# print(student)

# → __str__() call hota hai.

# Lekin Python mein ek aur dunder method hota hai:

# __repr__()

# Ye zyada tar developers/debugging ke liye hota hai.

# Example
# class Student:

#     def __init__(self, name):
#         self.name = name

#     def __repr__(self):
#         return f"Student('{self.name}')"


# student1 = Student("Fuzail")

# print(student1)

# Output:

# Student('Fuzail')
# Difference
# __str__()

# User-friendly

# def __str__(self):
#     return f"Student Name: {self.name}"

# Output:

# Student Name: Fuzail
# __repr__()

# Developer-friendly

# def __repr__(self):
#     return f"Student('{self.name}')"

# Output:

# Student('Fuzail')
# Interesting Point

# Agar class mein:

# __str__()

# nahi hai

# lekin:

# __repr__()

# hai

# to:

# print(student1)

# Python __repr__() use kar leta hai.

# Quiz

# Code run kiye bina batao:

# class Student:

#     def __init__(self, name):
#         self.name = name

#     def __repr__(self):
#         return f"Student('{self.name}')"


# student1 = Student("Ali")
# print(student1)

# Q1
# Output kya hoga?
# Student 'Ali'

# Q2
# Yahan __str__() nahi hai.
# To Python kis method ko use karega?
# python repr method ko use karega

# Q3
# Apni language mein batao:
# __str__()
# aur
# __repr__()
# difference tou mujha bhi smj nhi arha dono same he hai bss aghr str and repr dono hoto str ka result ko priority milti hai aghr str na ho tou us ki jaga repr use hojata hai 

