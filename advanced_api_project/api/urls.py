from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList

router = DefaultRouter()
router.register(r'books_all', BookList, basename='book_all')

urlpatterns = [
    # Remove the direct mapping of BookList using as_view()
    # path('books/', BookList.as_view(), name='book-list'),  # This line is not needed
    # Include the router URLs for viewsets (all CRUD operations)
    path('', include(router.urls)),  # This includes all routes registered with the router
]