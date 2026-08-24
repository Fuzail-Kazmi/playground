# Grade System
# Requirements

# Input:

# Marks

# Output:

# 90-100 = A
# 80-89  = B
# 70-79  = C
# 60-69  = D
# Below 60 = Fail

# Edge Cases
# -10
# 150

# user sai marks lo
# check kro marks valid hai yeh nhi
# aghr age 90-100 hai tou A
# aghr age 80-89 hai tou B
# aghr age 70-79 hai tou C
# aghr age 60-69 hai tou D
# Below 60 hai tou Fail

# marks = int(input("Enter your Marks To Check Your Grade: "))


# if marks > 100:
#     print("Enter A Valid Marks")
# elif marks >= 90:
#     print(f"Your Marks was {marks}, you got an 'A'")
# elif marks >= 80:
#     print(f"Your Marks was {marks}, you got an 'B'")
# elif marks >= 70:
#     print(f"Your Marks was {marks}, you got an 'C'")
# elif marks >= 60:
#     print(f"Your Marks was {marks}, you got an 'D'")
# elif marks >= 0:
#     print(f"Your Marks was {marks}, you got 'Fail'")
# else:
#     print("Enter A Valid Marks")

def check_grade(marks):
    if marks > 100:
        return 'Enter A Valid Marks'
    elif marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    elif marks >= 0:
        return "Fail"
    else:
        return 'Enter A Valid Marks'

marks = int(input("Enter your Marks To Check Your Grade: "))
result = check_grade(marks)
print(result)