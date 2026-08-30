# Mini Project — Student Management OOP

# Class Student banao.

# Requirements:

# name
# age
# school → class variable
# introduce() method
# show_school() method
# 3 students ke objects
# Har student ka naam/age different
# School same ho

# Student: Fuzail
# Age: 19
# School: ABC School

# Student: Ali
# Age: 22
# School: ABC School


class Student:
    school = "ABC School"

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Student: {self.name}")
        print(f"Age: {self.age}")
        print(f"School: {self.school}")
        print("-------------------------")

    

student1 = Student("Fuzail",19)
student2 = Student("Sara",18)
student3 = Student("Ali",20)

student1.introduce()
student2.introduce()
student3.introduce()