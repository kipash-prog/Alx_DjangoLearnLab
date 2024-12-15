# Delete Operation

Command:
```python
from bookshelf.models import Book
book = Book.objects.get(id=1)  # Assuming the book with id=1 exists
book.delete()
Book.objects.all()  # to confirm deletion
