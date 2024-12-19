# Create Operation

# Python Command

from bookshelf.models import Book
# Creating a book Instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book.save()
print(book)

## Expected Output :  
>>> book
<Book: 1984>