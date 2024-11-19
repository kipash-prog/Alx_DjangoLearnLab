import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query 1: Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        # Using objects.filter to get all books by the specific author
        books = Book.objects.filter(author=author)
        return [book.title for book in books]
    except Author.DoesNotExist:
        return f"No author found with name '{author_name}'"

# Query 2: List all books in a library
def list_all_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()  # Using the related_name 'books' from ManyToManyField in Library model
        return [book.title for book in books]
    except Library.DoesNotExist:
        return f"No library found with name '{library_name}'"

# Query 3: Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        # Using Librarian.objects.get with library as a filter
        librarian = Librarian.objects.get(library=library)
        return librarian.name
    except Library.DoesNotExist:
        return f"No library found with name '{library_name}'"
    except Librarian.DoesNotExist:
        return f"No librarian assigned to the library '{library_name}'"


# Sample function calls
if __name__ == "__main__":
    # Replace 'Author Name', 'Library Name' with actual names for testing
    print("Books by Author:", get_books_by_author("Author Name"))
    print("All Books in Library:", list_all_books_in_library("Library Name"))
    print("Librarian for Library:", get_librarian_for_library("Library Name"))
