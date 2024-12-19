from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # Ensure Library is imported
from .models import Library
from django.views.generic.detail import DetailView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Function-Based View to List All Books
def list_books(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})  # Render template with books

# Class-Based View to Display Details of a Specific Library
class LibraryDetailView(DetailView):
    model = Library  # Specify the model
    template_name = 'relationship_app/library_detail.html'  # Template to use
    context_object_name = 'library'  # Context variable for the template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # Add all books in the library to the context
        return context
