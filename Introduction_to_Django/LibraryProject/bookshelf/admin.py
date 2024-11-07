# bookshelf/admin.py
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Fields to display in the list view
    search_fields = ('title', 'author')  # Enable searching by title and author
    list_filter = ('publication_year',)  # Enable filtering by publication year

# Alternatively, you can register the model directly:
# admin.site.register(Book, BookAdmin)
