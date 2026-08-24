# names = ["Ali", "Ahmed", "Sara"]
# grades = ["A", "B", "A+"]

# for i in range(len(names)):
#     print(names[i], grades[i])

# ZIP
# for name, grade in zip(names, grades):
#     print(name, grade)

# zip() Kya Karta Hai?
# List 1 ka first item
# +
# List 2 ka first item

# phir

# List 1 ka second item
# +
# List 2 ka second item
# Match kar deta hai.

# names = ["Ali", "Ahmed"]

# ages = [19, 22]

# for name, age in zip(names, ages):
#     print(name, age)

# Important

# Agar lengths different hon:

# names = ["Ali", "Ahmed", "Sara"]

# ages = [19, 22]
# for name, age in zip(names, ages):
#     print(name, age)

# Output:

# Ali 19
# Ahmed 22

# ⚠️ Zip shortest list tak chalta hai.

# "Sara" skip ho jayegi.

# Quiz 1

# names = ["A", "B", "C"]
# numbers = [1, 2, 3]
# for name, number in zip(names, numbers):
#     print(name, number)

# A 1
# B 2
# C 3

# Quiz 2

# cities = ["Karachi", "Lahore"]
# countries = ["Pakistan", "Pakistan"]
# for city, country in zip(cities, countries):
#     print(city, country)

# Karachi Pakistan
# Lahore Pakistan

# Quiz 3
# Output?

# names = ["Ali", "Ahmed", "Sara"]
# ages = [19, 22]
# for name, age in zip(names, ages):
#     print(name, age)

# Ali 19
# Ahmed 22

# Thinking Question
# Ye:

# for i in range(len(names)):
#     print(names[i], grades[i])

# aur

# for name, grade in zip(names, grades):
#     print(name, grade)

# same kaam kyun karte hain?

# for i in range(len(names))
#     print(name[i], grades[i])
# is mai hum name ki list ki length pr loop run kr rahy hai or length ki index kai hisab sai value print ho rahi hai 

# for name, grade in zip(names, grades):
#     print(name, grade)
# is mai bhi same yehi ho raha hai mghr zip humay khud sai 2 value deta hai jo is trha chlta hai list 1 ka first item + list 2 ka second item list 1 ka first item + list 2 ka second item