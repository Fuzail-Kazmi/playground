# Chalo 👍 Ab Class Variable vs Instance Variable karte hain. Ye OOP mein important concept hai.

# Pehle ye code dekho:
# class Student:

#     school = "ABC School"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# Yahan:

# school = "ABC School"

# class variable hai.

# Aur:

# self.name
# self.age

# instance variables hain.

# Difference

# Socho 3 students hain:

# student1 = Student("Fuzail", 19)
# student2 = Student("Sara", 18)
# student3 = Student("Ali", 22)

# Har student ka:

# name → alag
# age  → alag

# Lekin:

# school → same

# Isliye:

# student1.name
# student2.name
# student3.name

# alag values dega.

# Lekin:

# student1.school
# student2.school
# student3.school

# teeno ke liye "ABC School" milega.

# Simple rule
# Instance Variable
# → har object ka apna data

# Class Variable
# → class ke objects ke liye shared/common data

# Tumhara Quiz

# Code run kiye bina batao:

# class Student:

#     school = "ABC School"

#     def __init__(self, name):
#         self.name = name


# student1 = Student("Fuzail")
# student2 = Student("Ali")

# print(student1.name)
# print(student2.name)

# print(student1.school)
# print(student2.school)

# 4 outputs kya honge?
# Fuzail
# Ali
# ABC School
# ABC School

# Aur ye bhi batao:

# name instance variable kyun hai aur school class variable kyun hai?
# name instance variable isliya hai kyu kai us ko hum self.name kr kai use use kr raah hai jis sai humay itna pata hota hai kai self har class kai object ki refer hoti hai tou is liya yeha srif object ka data hai jo or har object kai alag hota hai blueprint template same rehti hai or variable class jo hai wou hum na class mai direct varible bana kr diya hai jis sai humay pata hai yeh template ka part hoga means har object kai sath yeh bhi lazmi jai ga change nhi hoga 

# # Ab ek interesting challenge

# # Ab code dekho:

# class Student:

#     school = "ABC School"

#     def __init__(self, name):
#         self.name = name


# student1 = Student("Fuzail")
# student2 = Student("Ali")

# student1.school = "XYZ School"

# print(student1.school)
# print(student2.school)
# print(Student.school)
# # Batao 3 outputs kya honge?
# # XYZ School
# # ABC School
# # ABC School

# # Aur sabse important:

# # student1.school = "XYZ School" ke baad kya class variable change hua, ya sirf student1 ka data change hua?

# # Is question ko logically solve karo—ye class vs instance variables ko genuinely samajhne ka important point hai.