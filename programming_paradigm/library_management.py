class Book:
    """Class to represent a book."""
    
    def __init__(self, title, author):
        self.title = title          # Public attribute for the title
        self.author = author        # Public attribute for the author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True  # Successfully checked out
        return False  # Already checked out

    def return_book(self):
        """Return the book, making it available again."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True  # Successfully returned
        return False  # Not checked out


class Library:
    """Class to represent a library."""
    
    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    return f"{title} has been checked out."
                else:
                    return f"{title} is already checked out."
        return f"{title} not found in the library."

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    return f"{title} has been returned."
                else:
                    return f"{title} was not checked out."
        return f"{title} not found in the library."

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book.title for book in self._books if not book._is_checked_out]
        return available_books if available_books else "No books available."


# Example usage
if __name__ == "__main__":
    library = Library()
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")

    library.add_book(book1)
    library.add_book(book2)

    print(library.list_available_books())  # ['1984', 'To Kill a Mockingbird']
    print(library.check_out_book("1984"))  # '1984 has been checked out.'
    print(library.list_available_books())  # ['To Kill a Mockingbird']
    print(library.return_book("1984"))      # '1984 has been returned.'
    print(library.list_available_books())  # ['1984', 'To Kill a Mockingbird']
