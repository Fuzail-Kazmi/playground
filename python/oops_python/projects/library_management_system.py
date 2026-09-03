# Final OOP Project — Library Management System

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self,library_name):
        self.library_name = library_name
        self.__books = []

    def view_book(self):
        for i,book in enumerate(self.__books,start=1):
            print(f"{i}. {book}")

    def add_book(self,book):
        self.__books.append(book)

    def __len__(self):
        return len(self.__books)


library = Library("XYZ Library")

while True:
    print("=== Menu List ===")
    print("1. Add Book")
    print("2. View Books")
    print("3. Total Books")
    print("4. Exit")
    try:
        select = int(input("Select What You Want: "))
    except ValueError:
        print("Invalid Input")
        
    if select == 1:
        title = input("Enter Your Book Name: ")
        author = input("Enter Your Book Author Name: ")
        book = Book(title=title,author=author)
        library.add_book(book)
        print("Book Add Sucessfully")

        pass

    elif select == 2:
        if len(library) > 0:
            library.view_book()
        else:
            print("No Books Available")
        pass

    elif select == 3:
        print(len(library))

        pass

    elif select == 4:
        print("exit")
        break
    