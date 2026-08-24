# Important Concepts
# open()
# file = open("data.txt", "w")

# Meaning:

# data.txt file open karo
# w = write mode
# write()
# file.write("Hello")

# Meaning:

# Hello file mein save karo
# close()
# file.close()

# Meaning:

# File band karo
# Changes save kar do

# Quick Quiz 1

# Output file content?
# file = open("test.txt", "w")
# file.write("A")
# file.write("B")
# file.write("C")
# file.close()
# ABC


# Quick Quiz 2

# Output file content?
# file = open("test.txt", "w")
# file.write("A\n")
# file.write("B\n")
# file.write("C")
# file.close()
# A
# B
# C



# Thinking Question

# Apni language mein batao:

# print() aur file.write() mein sabse bada difference kya hai?

# print("Hello")

# aur

# file.write("Hello")

# Dono "Hello" likhte hain.

# yes you right but print humay console mai result show krta hai jis ko srif hum he dekh saktai hai code run kr kai jab kai file.write() yeh 1 file bana ta hai us mai write kr deta hai jis kka data store hota hai or store he rehta hai its mean data temporarly nhi hota print ki trha

# Quick Quiz

# Agar file mein:

# Ali
# Ahmed
# Sara

# save hai.

# To:

# file = open("students.txt", "r")
# data = file.read()
# print(data)
# file.close()
# Ali
# Ahmed 
# Sara


# Thinking Question
# Apni language mein batao:
# w mode aur r mode mein kya difference hai?
# w means kai write r means kai read 

# Quick Quiz

# File mein pehle se:

# Ali

# save hai.

# Code:

# file = open("students.txt", "a")
# file.write("\nAhmed")
# file.close()
# yeh given data ko students.txt file mai add kr dai ga

# Thinking Question

# Apni language mein batao:

# w aur a mode mein sabse bara difference kya hai?

# Hint:

# w = ?
# a = ?

# w = write kro 
# a = append kro 
# write krna sai yeh hoga kai andar koi bhi content ho wou replace ho jai ga jab kai append sai jo content file mai hai wou rahy ga or diya gai content append ho jai ga 

# Quiz 1

# with open("test.txt", "w") as file:
#     file.write("Hello")
# Hello

# Quiz 2

# with open("test.txt", "a") as file:
#     file.write("Python")

# Agar file mein pehle:

# Hello

# hai.

# Final content kya hoga?

# HelloPython

# Thinking Question

# Apni language mein batao:

# with open() ka sabse bara faida kya hai?

# Normal open() + close() ke muqable mein.

# with open() ka sabse bara faida yeh kai hum python ko bolta hai is file ko open kro kaam khatam hota he file krlo automation yeh bhoat important hai q kai open() + close() mai manually kaam krna par raha tha or close sai phely kisi line of code mai error ajai tou file close he nhi hogi tou with open() is the best way to read,write,append like play to file

# Quick Quiz

# Agar file mein:

# Apple
# Banana
# Orange

# hai.

# To:

# with open("fruits.txt", "r") as file:
#     data = file.readlines()

# print(data)

# ["Apple\n","Banana\n","Orange"]

# Thinking Question

# Apni language mein batao:

# read() aur readlines() mein sabse bara difference kya hai?

# read srif file ko read krta hai like strings wagera ko mghr readlines() humari strings ko list convert kr deta hai jo humaray task todo apps jaisi application kai andar fayda mand sabit hoga