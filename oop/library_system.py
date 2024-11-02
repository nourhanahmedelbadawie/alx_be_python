class Book:
    def __init__(self, title, author):
        """Initialize a book with title and author."""
        self.title = title
        self.author = author

    def __str__(self) -> str:
        """Return a string representation of the book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize an eBook with title, author, and file size."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self) -> str:
        """Return a string representation of the eBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"  # Use KB


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize a print book with title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self) -> str:
        """Return a string representation of the print book."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Initialize a library with an empty list of books."""
        self.books = []  # List to store book instances

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook instance to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of each book in the library."""
        if not self.books:
            print("The library is empty.")
            return
        
        for book in self.books:
            print(book)  # This will use the __str__ method of each book


# Example usage
if __name__ == "__main__":
    library = Library()

    # Add some books
    library.add_book(Book("Pride and Prejudice", "Jane Austen"))
    library.add_book(EBook("Snow Crash", "Neal Stephenson", 500))
    library.add_book(PrintBook("The Catcher in the Rye", "J.D. Salinger", 234))

    # List books in the library
    library.list_books()
