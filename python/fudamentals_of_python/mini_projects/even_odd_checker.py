# Mini Project — Even/Odd Checker

def checker(x):
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number: "))
result = checker(num)
print(num)
print(result)
print(f"Your Number was {num}, and its an {result} Number")