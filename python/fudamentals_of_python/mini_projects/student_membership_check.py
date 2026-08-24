students = ["Fuzail","Hussain", "Ali", "Ahmed", "Sara"]
students = [s.lower() for s in students]
student = input("Enter Your Student Name: ").lower()

if student in students:
    print(f"{student} Enrolled")
else:
    print("Your Given Student Not Found")