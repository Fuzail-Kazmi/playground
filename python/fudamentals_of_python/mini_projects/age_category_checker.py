# Project 2

# Age Category Checker

# Requirements:

# 0-12   Child
# 13-17  Teen
# 18-59  Adult
# 60+    Senior

# Bonus:

# Age = -5

# user sai age lo
# check kro age valid hai yeh nhi
# aghr age 0-12 hai tou child
# aghr age 13-17 hai tou teen
# aghr age 18-59 hai tou adult
# aghr age 60+ hai tou senior

# age = int(input("Enter Your Age: "))

# if age >= 0: 
#     if age <= 12:
#         print(f"Your Age is {age} so your a Child")
#     elif age <= 17:
#         print(f"Your Age is {age} so your a Teen")
#     elif age <= 59:
#         print(f"Your Age is {age} so your a Adult")
#     else:
#         print(f"Your Age is {age} so your a Senior")
# else:
#     print("Enter A Valid Age")

# Bonus Challenge

# Ek function banao:

# check_age(age)

# Agar:

# 0-12   → Child
# 13-17  → Teen
# 18-59  → Adult
# 60+    → Senior

# To function category return kare.

# Phir:

# result = check_age(19)
# print(result)

# Output:
# Adult

def check_age(age):
    if age >= 0: 
        if age <= 12:
            return "Child"
        elif age <= 17:
            return "Teen"
        elif age <= 59:
            return "Adult"
        else:
            return "Senior"
    else:
        return 'Please Enter A Valid Age'

age = int(input("Enter Your Age: "))
result = check_age(age)
print(result)