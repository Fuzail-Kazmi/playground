# map()

# map() ka kaam:

# Ek function ko
# list ke har item par apply karna

# Example:

# numbers = [1, 2, 3]

# Agar sab ko double karna ho:

# Without map:

# result = []

# for n in numbers:
#     result.append(n * 2)

# print(result)

# Output:

# [2, 4, 6]

# With map:

# numbers = [1, 2, 3]

# result = map(lambda x: x * 2, numbers)

# print(list(result))

# Output:

# [2, 4, 6]
# Formula
# map(function, iterable)

# Quiz 1

# numbers = [1, 2, 3]
# result = map(lambda x: x + 1, numbers)
# print(list(result))
# [2,3,4]


# Quiz 2

# names = ["ali", "ahmed"]
# result = map(lambda name: name.upper(), names)
# print(list(result))
# ['ALI','AHMED']


# Thinking Question

# Apni language mein explain karo:

# List Comprehension aur map() dono list ko transform karte hain.

# Phir map() ki zarurat kyun hai?

# Hint:

# Socho:

# [number * 2 for number in numbers]

# aur

# map(lambda x: x * 2, numbers)
# comprehension mai hum just one liner for loop chlatai hai with conditon and return value jab kai map mai hum function kai sath iteration krwatai hai jis sai function list kai har item pr apply hota hai 

# Quick Challenge

# numbers = [10, 20, 30]
# result = map(lambda x: x // 10, numbers)
# print(list(result))
# [1,2,3]


# words = ["python", "django"]
# result = map(len, words)
# print(list(result))
# [6,6]


# Thinking Question
# result = map(len, words)

# Yahan lambda use nahi hua.

# Apni language mein batao:

# Ye kaise kaam kar raha hai?
# len function har item par kaise apply ho raha hai?

# result = map(len,words)
# result = map function kai map mai 2 arguments ati hai function,iteration humnai first argument mai len ka function use kiya words pr iteration hwi har iteration meri list ki length mai lag gaya 

# filter()

# Map:

# Transform karta hai
# (change values)

# Filter:

# Select karta hai
# (keep/remove values)

# Example:

# numbers = [10, 15, 20, 25, 30]

# result = filter(
#     lambda x: x % 2 == 0,
#     numbers
# )

# print(list(result))

# Output:

# [10, 20, 30]

# Kyuki lambda:

# x % 2 == 0

# True ya False return karta hai.

# True:

# value rakh lo

# False:

# value hata do

# Quiz 1

# numbers = [1, 2, 3, 4, 5]
# result = filter(
#     lambda x: x > 3,
#     numbers
# )
# print(list(result))
# [4,5]


# Quiz 2

# names = ["Ali", "", "Ahmed", ""]
# result = filter(
#     lambda name: name != "",
#     names
# )
# print(list(result))
# [Ali,Ahmed]


# Thinking Question

# Apni language mein explain karo:

# map() aur filter() mein sabse bara difference kya hai?

# map() value ko change karta hai ya remove?

# filter() value ko change karta hai ya remove?

# map value ko change krta hai list kai har item pr apply krta hai filter value ko rakhta hai yeh remove krta hai based on condition true ho yeh false 

# numbers = [10, 15, 20, 25, 30]
# result = filter(
#     lambda x: x % 2 == 0,
#     numbers
# )
# print(list(result))

# numbers = [10, 15, 20, 25, 30]
# result = []
# for num in numbers:
#     if num % 2 == 0:
#         result.append(num)
# print(result)