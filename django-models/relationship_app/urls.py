# relationship_app/urls.py

from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Route for function-based view
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Route for class-based view
]
