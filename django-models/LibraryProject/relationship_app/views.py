from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Book, UserProfile
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required


# Register view
class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'relationship_app/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after registration
            return redirect('home')  # Redirect to the home page or another page after registration
        return render(request, 'relationship_app/register.html', {'form': form})


# Function-based view to list all books with their authors
def list_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    context = {
        'books': books,
    }
    return render(request, 'relationship_app/list_books.html', context)


# Class-based view to display details for a specific library with all its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # Get all books related to the library
        return context


# Role-based access views

def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'


# Admin view - accessible only to 'Admin' users
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


# Librarian view - accessible only to 'Librarian' users
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


# Member view - accessible only to 'Member' users
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# View to add a book
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        Book.objects.create(title=title, author=author, description=description)
        return redirect('book_list')  # Redirect to the book list after adding a new book
    return render(request, 'relationship_app/add_book.html')

# View to edit a book
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.description = request.POST.get('description')
        book.save()
        return redirect('book_list')
    return render(request, 'relationship_app/edit_book.html', {'book': book})

# View to delete a book
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('book_list')
