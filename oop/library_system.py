class Book:
    """A class representing a book."""
    def __init__(self, title: str, author: str):
        """Initialize the book with a title and author."""
        self.title = title
        self.author = author
          
    
class EBook(Book):
    """A class representing an eBook, inheriting from Book."""
    def __init__(self, title: str, author: str, file_size: float):
        """Initialize the eBook with a title, author, and file size."""
        super().__init__(title, author)
        self.file_size = file_size
        
    

class PrintBook(Book):
    """A class representing a print book, inheriting from Book."""
    def __init__(self, title: str, author: str, page_count: int):
        """Initialize the print book with a title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count

class Library:
    """A class representing a library that contains books."""
    def __init__(self):
        """Initialize the library with an empty list of books."""
        self.books = []
    
    def add_book(self, book: Book):
        """Add a book to the library."""
        self.books.append(book)
        
    def list_books(self):
        """List all books in the library."""    
        for book in self.books:
            if isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            elif isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            else:
                print(f"Book: {book.title} by {book.author}")
        
    def __str__(self):
        """Return a string representation of the library."""
        pass
    
    def __repr__(self):
        """Return a detailed string representation of the library."""
        # return f"Library(books={self.books})" 
        pass  
    
    def __del__(self):
        """Destructor to clean up resources when the library is destroyed."""
        pass