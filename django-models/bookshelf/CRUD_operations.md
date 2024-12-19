#### Create Operation

# Python Command

from bookshelf.models import Book
# Creating a book Instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book.save()
print(book)

## Expected Output :  
>>> book
<Book: 1984>


#### Retrieve Operation
# Python Command
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

## Expected Output

1984 George Orwell 1949

#### Update Operation

# Python Command

book.title = "Nineteen Eighty-Four"
book.save()
## Expected Output

>>> book
<Book: Nineteen Eighty-Four>


#### Delete Operation
# Python Command
 
 from bookshelf.models import Book
 # Deleting the book instance
 book.delete()
 #verifying the deletion by retrieving all books
 books = Book.objects.all()
 print(books)
 ## Expected Output
 
 >>> books
 <QuerySet []>