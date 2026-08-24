# List Comprehension

# [expression for item in iterable]

# numbers = [1, 2, 3, 4]

# result = [number * 2 for number in numbers]

# print(result)

# [expression for item in iterable]

# Q1

# Output kya hoga?
# numbers = [1, 2, 3, 4, 5]
# result = [number * 3 for number in numbers]
# print(result)

# [3,6,9,12,15]

# Q2
# Output?
# numbers = [1, 2, 3, 4, 5, 6]
# result = [number for number in numbers if number > 3]
# print(result)

# [4,5,6]

# Q3 — Thinking
# Ye:
# result = [number * 2 for number in numbers]
# aur ye:
# result = []
# for number in numbers:
#     result.append(number * 2)
# same result kyun dete hain?

# result = [number * 2 for number in numbers] its means kai mera result variable kai andar number * 2 or number kaha sai arhaa hhai wou araha hai numbers pr loop laga kr for number in numbers tou meri numbers ki value * 2 hojai tou is sai har iteration kai baad meri new value banai gi jo direct result varable kai andar store ho jai gi 
# result = []
# for number in numbers:
#     result.append(number * 2)
# is mai bhi same yehi ho raha hai bas is ko hum 1 line mai krna kai bajai zayda line of code mai kr rahy hai or dono ka kaam same hai hum result variable kai andar sab append kra rahy hai after the for loop so both ways are perfect upr wala bss one line hai advance hai 

# Mini Challenge 1

# names = ["Ali", "Ahmed", "Sara"]
# result = [name.lower() for name in names]
# print(result)
# ['ali','ahmed','sara']

# Mini Challenge 2

# numbers = [10, 15, 20, 25, 30]
# result = [number for number in numbers if number % 2 == 0]
# print(result)
# [10,20,30]

# Mini Challenge 3

numbers = [1, 2, 3, 4]
result = [n + 10 for n in numbers]
print(result)
