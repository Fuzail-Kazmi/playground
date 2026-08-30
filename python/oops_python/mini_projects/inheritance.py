# Challenge — College Student

# Parent class: Student

# Requirements:

# name attribute
# __init__(name)
# study() method → Student is studying
# Child class: CollegeStudent(Student)

# Requirements:

# semester attribute
# __init__(name, semester)
# super() use karke parent ka __init__() call karo
# attend_class() method → College student is attending class
# Object:
# student1 = CollegeStudent("Fuzail", 3)
# Phir ye output lao:
# Name: Fuzail
# Semester: 3
# Student is studying
# College student is attending class

class Student:

    def __init__(self,name):
        self.name = name
    
    def study(self):
        print("Student is Studying")

class CollegeStudent(Student):

    def __init__(self,name,semester):
        super().__init__(name)
        self.semester = semester
    
    def introduce(self):
        print(f"{self.name} is in {self.semester} Semester")
    
    def attend_class(self):
        print("College student is attending class")


student1 = CollegeStudent("Fuzail",4)
print(f"Student: {student1.name}")
print(f"Semester: {student1.semester}")
student1.study()
student1.introduce()
student1.attend_class()