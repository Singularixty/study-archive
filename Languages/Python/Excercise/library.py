# OOP exercise 2
class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False
        
    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"Book {self.title} checked out")
        else:
            print(f"Book {self.title} was already checked out")

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            print(f"Book {self.title} returned")
        else:
            print(f"Book {self.title} was not checked out")

    def __str__(self):
        status = "Checked out" if self.is_checked_out else "Available"
        return f"{self.title} by {self.author} ({status})"
    
class Library():
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"Book {book_name} has been added to library")

    def check_out_book(self, book_name):
        for book in self.books:
            if book == book_name:
                book.check_out()
                return
            print(f"Book {book_name} not found in the library")

    def return_book(self, book_name):
        for book in self.books:
            if book == book_name:
                book.return_book()
                return
            print(f"Book {book_name} not found in the library")

    def list_books(self):
        print("-"*50)
        for book in self.books:
            print(book)
        print("-"*50)

my_library = Library("Singular Library")
book1 = Book("To Kill a Mockingbird", "Harper Lee")
book2 = Book("1984", "George Orwell")
my_library.add_book(book1)
my_library.add_book(book2)
my_library.list_books()
#my_library.check_out_book("1984")
#my_library.list_books()
#my_library.return_book("1984")
#my_library.list_books()