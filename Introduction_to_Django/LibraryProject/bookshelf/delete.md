from bookshelf.models import Book

book.delete()

# Confirm deletion by trying to retrieve all books
Book.objects.all()
