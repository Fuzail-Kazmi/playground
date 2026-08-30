class Student:

    def __init__(self, name):
        self.name = name

# Yahan:

# self.name = name

# mein left wala self.name aur right wala name alag alag cheezein hain.

# Tumhare khayal mein dono mein kya difference hai? 🤔

# self.name = name is mai self.name hai is ka matlab hai mera current object ka name yeh refrence hai uski self har current object ki refrense hota hai jo us current object ko define krta hai tou tabhi yeha hum na likha __init__ kai andar kai jab bhi humara code run ho tou yeh khud chlta hai tou run hota hai mera object name hai wou us mai store ho jai 

# Maan lo:

# class Student:

#     def __init__(self, name):
#         self.name = name

# Aur:

# student1 = Student("Ali")

# Jab ye line chalti hai:

# Student("Ali")

# to conceptually Python kuch aisa karta hai:

# __init__(student1, "Ali")

# Yani:

# self = student1
# name = "Ali"

# Ab line execute hoti hai:

# self.name = name

# To Python dekhta hai:

# Right Side
# name

# Ye parameter hai.

# Value:

# "Ali"
# Left Side
# self.name

# Ye object ke andar attribute bana raha hai.

# Yani:

# student1.name = "Ali"

# Result:

# student1.name

# ab store karta hai:

# "Ali"
# Simple Formula
# self.name = name

# ka matlab:

# Object ke andar name attribute banao
# =
# Jo value parameter mein aayi hai usko store karo
# Real Example
# student1 = Student("Ali")
# student2 = Student("Ahmed")

# To:

# student1.name = "Ali"
# student2.name = "Ahmed"

# Dono same class se bane hain.

# Lekin har object apna alag data rakhta hai.

# Isi liye self important hai.

# Ek Chhota Quiz

# Predict karo:

# class Student:
#     def __init__(self, name):
#         self.name = name

# student1 = Student("Ali")

# print(student1.name)

# # Output: Ali

# # self is code mai student1 ki refer kr raha hai def __init__(student1,Ali)

# class Student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# student1 = Student("Ali", 19)

# print(student1.name)
# print(student1.age)

# # Questions
# # Output kya hoga?
# # Ali
# # 19

# # Object ke andar kitne attributes bane?
# # 2 attributes hai 

# # Ye line:
# # student1 = Student("Ali", 19)

# # chalne par self.name = name aur self.age = age ke baad object ke andar kya data store hoga?
# # self.name = Ali self.age = 19

# Next Challenge

# class Student:

#     def __init__(self, name):
#         self.name = name

#     def introduce(self):
#         print(f"Hi, I am {self.name}")

# student1 = Student("Ali")
# student2 = Student("Ahmed")

# student1.introduce()
# student2.introduce()

# Ali
# Ahmed
# Hi, I am Ali
# Hi, I am Ahmed

# Aur ek aur sawal:

# student1 aur student2 ek hi class se bane hain.

# Phir bhi dono ka data alag kaise hai?

# yeh hum Student Class kai blueprint sai 2 object bana rahy hai student1 and student2 kai naam ka or data alag isliya hai hum self ka use kr rahy hai jo current object ko refer kr deta hai jab student1 Ali hai tou upr self mai jab us ka code run hwa tou current object student1 tha tabhi Ali aya or jaisi he code student2 pr gaya tou current object kai hisab sai us ka result Ahmed 