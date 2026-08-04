class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Borrowed"
        print(f"Title: {self.title}, Author: {self.author}, Status: {status}")


class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def display(self):
        print(f"Patron: {self.name}")
        if self.borrowed_books:
            print("Borrowed Books:")
            for book in self.borrowed_books:
                print("-", book.title)
        else:
            print("No books borrowed.")


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Book '{title}' added successfully.")

    def register_patron(self, name):
        patron = Patron(name)
        self.patrons.append(patron)
        print(f"Patron '{name}' registered successfully.")

    def borrow_book(self, patron_name, book_title):
        patron = None
        book = None

        for p in self.patrons:
            if p.name == patron_name:
                patron = p
                break
            
        for b in self.books:
            if b.title == book_title:
                book = b
                break

        if patron is not None and book is not None:
            if book.available:
                book.available = False
                patron.borrowed_books.append(book)
                print(f"{patron_name} borrowed '{book_title}'.")
            else:
                print("Book is already borrowed.")
        else:
            print("Patron or Book not found.")

    def return_book(self, patron_name, book_title):
        patron = None

        for p in self.patrons:
            if p.name == patron_name:
                patron = p
                break

        if patron is not None:
            for book in patron.borrowed_books:
                if book.title == book_title:
                    book.available = True
                    patron.borrowed_books.remove(book)
                    print(f"{patron_name} returned '{book_title}'.")
                    return
            print("Book was not borrowed by this patron.")
        else:
            print("Patron not found.")

    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            book.display()


library = Library()
library.add_book("Python Programming", "John Smith")
library.add_book("Data Structures", "Alice Brown")
library.register_patron("Rahul")
library.register_patron("Priya")
library.borrow_book("Rahul", "Python Programming")
library.display_books()
library.return_book("Rahul", "Python Programming")
library.display_books()