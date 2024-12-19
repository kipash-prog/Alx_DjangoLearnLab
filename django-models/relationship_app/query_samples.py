from .models import Author, Book, Library, Librarian
from django.core.exceptions import ObjectDoesNotExist

# Query all books by a specific author
author_name = "Gashu"
try:
    author = Author.objects.get(name=author_name)  # Get the author object first
    books_by_author = Book.objects.filter(author=author)  # Then filter books by the author
    print(f"Books by {author_name}: {books_by_author}")
except ObjectDoesNotExist:
    print(f"Author with name '{author_name}' does not exist.")

# List all books in a specific library
library_name = "Some Library Name"  # Replace with actual library name
try:
    library = Library.objects.get(name=library_name)  # Get the library object by name
    books_in_library = library.books.all()
    print(f"Books in {library_name}: {books_in_library}")
except ObjectDoesNotExist:
    print(f"Library with name '{library_name}' does not exist.")

# Retrieve the librarian for a specific library
try:
    librarian = Librarian.objects.get(library=library)  # Get the librarian associated with the library
    print(f"Librarian of {library_name}: {librarian}")
except ObjectDoesNotExist:
    print(f"Librarian for library '{library_name}' does not exist.")
