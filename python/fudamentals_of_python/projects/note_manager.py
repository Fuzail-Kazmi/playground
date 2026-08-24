# Next Project — Notes Manager

# Requirements:

# Menu
# 1. Add Note
# 2. View Notes
# 3. Search Note

# Option 1
# Add note to notes.txt

# Option 2
# Show all notes

# Option 3
# Ask keyword
# Search in notes.txt
# Print:
# Found
# or
# Not Found

# Concepts
# Functions
# Conditions
# File Handling
# Strings

# user_note = input("Add Note: ").lower()

# with open('notes.txt','a') as file:
#     file.write(user_note + '\n')
#     print("Note add successfully")

# with open('notes.txt','r') as file:
#     note = file.readlines()
#     print(note)

# user_search = input("Search Keyword Note: ").lower()

# for keyword in note:
#     if user_search in keyword:
#         print("Note Found")
#     else:
#         print("Note Not Found")


# while True:
#     print("=== Menu List ===")
#     print("1. For add note")
#     print("2. For view note")
#     print("3. For search note")
#     print("4. For exit")
#     select = int(input("Select What You Want: "))
    
#     if select == 1:
#         user_note = input("Add Note: ").lower()

#         with open('notes.txt','a') as file:
#             file.write(user_note + '\n')
#             print("Note add successfully")
        
#         pass
#     elif select == 2:
#         with open('notes.txt','r') as file:
#             note = file.readlines()
        
#         for i,n in enumerate(note,start=1):
#             print(f"{i}. {n.strip()}")
        
#         pass
#     elif select == 3:
#         user_search = input("Search Keyword Note: ").lower()
#         found = False

#         with open('notes.txt','r') as file:
#             note = file.readlines()

#         for i,keyword in enumerate(note,start=1):
#             if user_search in keyword:
#                 found = True
#             print(f"{i}. {keyword}")
        
#         if found != True:
#             print("Note Not Found")
#         else:
#             print("Note Found")
        

#         pass
#     elif select == 4:
#         print("exit")
#         break
    


def add_note(user_note):
    with open('notes.txt','a') as file:
        file.write(user_note + '\n')
        print("Note add successfully")

def view_notes():
    with open('notes.txt','r') as file:
        note = file.readlines()
        
    for i,n in enumerate(note,start=1):
        print(f"{i}. {n.strip()}")

def search_note(user_search):
    found = False

    with open('notes.txt','r') as file:
        note = file.readlines()

    for i,keyword in enumerate(note,start=1):
        if user_search in keyword.lower():
            found = True
            print(f"{i}. {keyword.strip()}")
    
    if found != True:
        print("Note Not Found")
    else:
        print("Note Found")

while True:
    print("=== Menu List ===")
    print("1. For add note")
    print("2. For view note")
    print("3. For search note")
    print("4. For exit")
    try:
        select = int(input("Select What You Want: "))
    except ValueError:
        print("Invalid Input")
        
    if select == 1:
        user_note = input("Add Note: ").lower()
        add_note(user_note)

        pass

    elif select == 2:
        view_notes()
        
        pass

    elif select == 3:
        user_search = input("Search Keyword Note: ").lower()
        search_note(user_search)

        pass

    elif select == 4:
        print("exit")
        break
    

