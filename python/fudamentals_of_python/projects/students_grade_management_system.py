# Project — Student Grade Management System

students = []

def add_student():
    student_info = []
    name = input("Enter Your Name: ").lower()
    marks = int(input("Enter Your Marks: "))
    grade = ''

    if marks < 0 or marks > 100:
        grade = "Invalid Marks"
    elif marks > 90:
        grade = "a+"
    elif marks > 80:
        grade = "a"
    elif marks > 70:
        grade = "b"
    elif marks > 60:
        grade = "c"
    else:
        grade = "fail"

    student_info.append(name)
    student_info.append(marks)
    student_info.append(grade)

    keys = ["name","marks","grade"]
    values = [student for student in student_info]
    student_report = dict(zip(keys, values))
    students.append(student_report)


def view_students():
    print("Students:")
    if len(students) <= 0:
        print("No Record")
    else:
        for index, student in enumerate(students, start=1):
            print(f"{index}. {student}")

def search_student():
    search = input("Search Student: ").lower()
    found = False
    for i,keyword in enumerate(students,start=1):
        student = ''.join(keyword["name"]).lower()
        if search in student.lower():
            found = True
            print(f"{i}. {keyword}")
            break
    
    if found != True:
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
    

