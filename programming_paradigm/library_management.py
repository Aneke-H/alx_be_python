class Book:
    """A class representing a book in the library."""
    def __init__(self, title: str, author: str) -> None:
        """Initialize a book with a title and an author."""
        self.title = title
        self.author = author
        self._is_checked_out = False
        
    def check_out(self) -> bool:
        """Check out the book."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
        
        
    
    def return_book(self) -> bool:
        """Return the book."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False


class Library():
    """A class representing a library that manages books."""
    def __init__(self):
        """Initialize an empty library."""
        self._books = []
    
    def add_book(self, book: Book) -> None:
        """Add a book to the library."""
        self._books.append(book)
        
    def list_available_books(self) -> None:
        """List all available books in the library."""
        available_books = [book for book in self._books if not book._is_checked_out]
        for book in available_books:
            print(f"{book.title} by {book.author}")
        if not available_books:
            print("No available books.")
            
    
    def check_out_book(self, title: str) -> bool:
        """Check out a book by title."""
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book.check_out()
                # print(f"Checked out: {book.title}")
                return True
        # print(f"Book '{title}' is not available.")
        return False
    
    def return_book(self, title: str) -> bool:
        """Return a book by title."""
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book.return_book()
                # print(f"Returned: {book.title}")
                return True
        # print(f"Book '{title}' was not checked out.")
        return False    

