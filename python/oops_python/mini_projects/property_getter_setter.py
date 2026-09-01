class Student:
    def __init__(self,marks):
        self.__marks = marks
    
    @property
    def student_marks(self):
        return self.__marks

    @student_marks.setter
    def student_marks(self,updated_marks):
        if updated_marks >= 0 and updated_marks <= 100:
            self.__marks = updated_marks

        else:
            print("Invalid Marks")

student_marks = int(input("Enter Your Marks: "))
student1 = Student(marks=student_marks)
print(student1.student_marks)

student1.student_marks = int(input("Enter Your Marks: "))
print(student1.student_marks)

