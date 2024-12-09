from django import forms
from django.conf import settings

user = settings.AUTH_USER_MODEL



class ExampleForm(forms.Form):
    # Add any fields you need for your example form
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Email Address')
    message = forms.CharField(widget=forms.Textarea, label='Your Message')

    # Optional: Add custom validation for any of the fields
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError('Name must be at least 3 characters long')
        return name


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ['username', 'email', 'date_of_birth']

from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']

    # Example of additional validation
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError('This field cannot be empty')
        if len(title) < 3:
            raise forms.ValidationError('Title should be at least 3 characters long')
        return title
