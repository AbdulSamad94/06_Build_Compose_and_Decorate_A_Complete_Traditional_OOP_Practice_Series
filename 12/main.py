class Book:
    total_books = 0

    def increment_book_count(self): 
        print("Incrementing book count...")
        Book.total_books += 1
        print(f"Total books: {Book.total_books}")

my_book = Book()
my_book.increment_book_count()
