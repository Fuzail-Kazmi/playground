# Mini Project 1
# Smart Calculator

# Requirements:
# User se 2 numbers lo
# User se operation lo
# +
# /
# Result show karo
# Bonus

# Division by zero handle karo.

# mera result ay ga 3 + 3 = 6
# mai sari value user sai le lu
# value_1 = 3
# operator = +
# value = 2
# result mai sab is tarha bhej na hai value_1 then operator then value_2


# value_1 = int(input("enter your value: "))
# operator = input("enter your operator: ")
# value_2 = int(input("enter your value that operate for: "))

# if operator == "+":
#     result = value_1 + value_2
#     print(f"value_1 + value_2 = {result}")
# elif operator == "-":
#     result = value_1 - value_2
#     print(f"value_1 - value_2 = {result}")
# elif operator == "*":
#     result = value_1 * value_2
#     print(f"value_1 * value_2 = {result}")
# elif operator == "/":
#     if value_2 != 0:
#         result = value_1 / value_2
#         print(f"value_1 / value_2 = {result}")
#     else:
#         print("Error Divide by zero")
# else:
#     print("Invalid Operator")

# Mini Project (Functions)
# Calculator Function

# Requirements:

# Ek function banao jo 2 numbers le.
# Function un numbers ko add kare.
# Result return kare.
# Bahar result ko variable mein store karo.
# Result print karo.
# Example

# Input:

# 5
# 3

# Output:

# 8

# def Calculate(x,y):
#     result = x + y
#     return result

# val1 = int(input("Enter Your First Number: "))
# val2 = int(input("Enter Your Second Number: "))
# result = Calculate(val1,val2)
# print(result)

# Mini Project — Safe Calculator
# Requirements:

# User se 2 numbers lo
# User se operator lo
# +, -, *, /
# Use try-except
# Agar invalid number aaye:
# Invalid Input
# Agar divide by zero ho:
# Cannot Divide By Zero
# Otherwise result print karo


try:
    num1 = int(input("enter your value 1st value: "))
    num2 = int(input("enter your value 2nd value: "))
    operator = input("enter your operator: ")

    if operator == "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")    

    elif operator == "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")

    elif operator == "*":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")

    elif operator == "/":
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid Input")

except ValueError:
    print("Invalid Input")

except ZeroDivisionError:
    print("Cannot Divide By Zero")    

finally:
    print("Calculation Done")