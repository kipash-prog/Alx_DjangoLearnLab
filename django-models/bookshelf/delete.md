# Delete Operation
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
