class Book:
 def __init__(self, title, author):
  self.title = title
  self.author = author

    
class  EBook(Book):
   def __init__(self  , title, author , file_size):
       super().__init__(title, author)
       self.file_size = file_size


class PrintBook(Book): 
  def __init__(self   , title, author , page_count):
           super().__init__(title, author)
           self.page_count = page_count
   


class Book:
    def __init__(self, title, author):
        """Initialize a book with title and author."""
        self.title = title
        self.author = author


class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize an eBook with title, author, and file size."""
        super().__init__(title, author)
        self.file_size = file_size


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize a print book with title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count


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
            if isinstance(book, EBook):
                print(f"EBook: '{book.title}' by {book.author}, File Size: {book.file_size} MB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: '{book.title}' by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: '{book.title}' by {book.author}")


# Example usage
library = Library()

# Add some books
library.add_book(EBook("Digital Fortress", "Dan Brown", 2.5))
library.add_book(PrintBook("The Great Gatsby", "F. Scott Fitzgerald", 218))

# List books in the library
library.list_books()
