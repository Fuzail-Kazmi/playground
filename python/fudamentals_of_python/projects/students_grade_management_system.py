# Project — Student Grade Management System

students = []

def add_student():
    name = input("Enter Your Name: ")
    marks = int(input("Enter Your Marks: "))
    grade = ''

    if marks < 0 or marks > 100:
        grade = "Invalid Marks"
    elif marks > 90:
        grade = "A+"
    elif marks > 80:
        grade = "A"
    elif marks > 70:
        grade = "B"
    elif marks > 60:
        grade = "C"
    else:
        grade = "Fail"

    students.append(name)
    students.append(marks)
    students.append(grade)


def view_students():
    keys = ["Name","Marks","Grade"]
    values = [student for student in students]
    student_report = dict(zip(keys, values))
    print(student_report)


def search_student():
    search = input("Search Student: ").lower()
    found = False
    for search in students[0]:
        found = True
        keys = ["Name","Marks","Grade"]
        values = [student for student in students]
        student_report = dict(zip(keys, values))
        print(student_report)
        break

    if not found:
        print("Student Not Found")
    else:
        print("Student Found")


while True:
    print("=== Menu List ===")
    print("1. For add student")
    print("2. For view student")
    print("3. For search student")
    print("4. For exit")
    try:
        select = int(input("Select What You Want: "))
    except ValueError:
        print("Invalid Input")
        
    if select == 1:
        add_student()

        pass

    elif select == 2:
        view_students()
        
        pass

    elif select == 3:
        search_student()

        pass

    elif select == 4:
        print("exit")
        break
    

