# Mini Project 1 — Notes Saver

# Requirements:

# 1. User se note lo
# 2. notes.txt file open karo
# 3. Append mode use karo
# 4. Note save karo
# 5. Message print karo:
#    Note Saved Successfully

# Example:

# User enters:

# Learn Python OOP

# File:

# Learn Loops
# Learn Functions
# Learn Python OOP
# Hint

# Structure kuch is tarah hoga:

# note = input("Enter Your Note: ")
# file = open('note.txt','a')
# file.write(note + '\n')
# file.close()

# file = open('note.txt', 'r')
# data = file.read()
# print(data)
# file.close()

# print("Note Saved Successfully")

# Next Challenge

# Student Notes Search

# Requirements:

# notes.txt read karo
# User se keyword lo
# Check karo keyword file mein hai ya nahi
# Agar hai:
# Note Found
# Nahi hai:
# Note Not Found

# Hint:

# Tum already ye concept jaante ho:

# if keyword in data:

search = input("Search Your Note: ").lower()
file = open('note.txt','r')
data = file.read().lower()
if search in data:
    print("Note Found")
else:
    print("Note Not Found")
file.close()