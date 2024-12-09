markdown
Copy code
# CRUD Operations for Book Model

Command to Create:
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
Expected Output:



<Book: 1984>
Command to Retrieve:


book = Book.objects.get(id=1)  # assuming id=1 is your book's id
print(book)  # This will display all attributes of the book
Expected Output:


Book(id=1, title="1984", author="George Orwell", publication_year=1949)
Command to Update:

book.title = "Nineteen Eighty-Four"
book.save()
book
Expected Output:


<Book: Nineteen Eighty-Four>
Command to Delete:


book.delete()
Book.objects.all()  # to confirm deletion
Expected Output:


<QuerySet []>
