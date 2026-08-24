# Lists Final Project
# Student Search System

# Requirements:

# 1. Empty list banao
# 2. User se 5 student names lo
# 3. List mein store karo
# 4. User se search name lo
# 5. Check karo name list mein hai ya nahi
# 6. Found → Student Found
# 7. Nahi → Student Not Found

# Bonus

# Case-insensitive search.

students = []

user = students.append(input("Enter Your Student Name: "))
user = students.append(input("Enter Your Student Name: "))
user = students.append(input("Enter Your Student Name: "))
user = students.append(input("Enter Your Student Name: "))
user = students.append(input("Enter Your Student Name: "))

students = [s.lower() for s in students]

print(students)

user_search = input("Enter Your Search Student Name: ").lower()
if user_search in students:
    print(f"Student {user_search} Found")
else:
    print(f"Student {user_search} Not Found")