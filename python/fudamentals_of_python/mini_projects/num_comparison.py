# Mini Project — Number Comparison

def find_largest(x,y):
    if x > y:
        return x
    else:
        return y

num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))
result = find_largest(num1,num2)
print(f"First number is {num1}, Second number is {num2}")
print(f"the largest number was {result}")