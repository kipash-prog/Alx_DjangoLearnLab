# Integrating Book Model with Django Admin

## Steps Taken:

1. **Registered the Book Model**:
   - Modified `bookshelf/admin.py` to include the Book model for the admin interface.
   - Used the `@admin.register(Book)` decorator to register the model.

2. **Customized the Admin Interface**:
   - Set up the admin display to show `title`, `author`, and `publication_year` in the list view.
   - Enabled searching by `title` and `author`.
   - Added filtering by `publication_year`.

## Code Snippet:

```python
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)
