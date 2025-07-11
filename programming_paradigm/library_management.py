class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_checked_out(self):
        return self._is_checked_out
    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Checked out: {book.title}")
                else:
                    print(f"Book '{title}' is already checked out.")
                return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Returned: {book.title}")
                else:
                    print(f"Book '{title}' was not checked out.")
                return
        print(f"Book '{title}' not found in the library.")

    def list_available_books(self):
        available_books = [book for book in self._books if not book.is_checked_out()]
        if not available_books:
            print("No available books in the library.")
            return
        for book in available_books:
            print(book)
    