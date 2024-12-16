from rest_framework import generics, filters
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters import rest_framework as django_filters  # Correct import for filtering

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Adding filtering, searching, and ordering capabilities
    filter_backends = [django_filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author__name', 'publication_year']  # Filtering by title, author, and publication_year
    search_fields = ['title', 'author__name']  # Enabling search functionality on title and author's name
    ordering_fields = ['title', 'publication_year']  # Allow ordering by title and publication_year
