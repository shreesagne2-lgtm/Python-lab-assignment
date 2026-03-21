class Book:
    def __init__(self, title):
        self.title = title
        self.available = True


class Member:
    def __init__(self, name):
        self.name = name


class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Enter book title: ")
        book = Book(title)
        self.books.append(book)
        print("Book added successfully")

    def display_books(self):
        for book in self.books:
            status = "Available" if book.available else "Lent"
            print(book.title, "-", status)

    def lend_book(self):
        title = input("Enter book title to lend: ")
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print("Book lent successfully")
                return
        print("Book not available")

    def return_book(self):
        title = input("Enter book title to return: ")
        for book in self.books:
            if book.title == title:
                book.available = True
                print("Book returned successfully")
                return
        print("Book not found")


lib = Library()

while True:
    print("\n1.Add Book")
    print("2.Lend Book")
    print("3.Return Book")
    print("4.Display Books")
    print("5.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        lib.add_book()
    elif choice == 2:
        lib.lend_book()
    elif choice == 3:
        lib.return_book()
    elif choice == 4:
        lib.display_books()
    elif choice == 5:
        break
    else:
        print("Invalid choice")