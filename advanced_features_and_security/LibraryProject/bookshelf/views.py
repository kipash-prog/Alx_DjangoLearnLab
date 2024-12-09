from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseForbidden
from .models import MyModel
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self,email,date_of_birth,profile_photo,password):
        if not email:
            raise ValueError("Email is required")
        email=self.normalize_email(email)
        user=self.model(
            email,
            date_of_birth=date_of_birth,
            profile_photo=profile_photo
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    class Meta:
        permissions = [
            ("can_view", "Can view user"),
            ("can_create", "Can create user"),
            ("can_edit", "Can edit user"),
            ("can_delete", "Can delete user"),
        ]
    def __str__(self):
        return self.email
    
    def create_superuser(self,email,date_of_birth,profile_photo,password=None):
        user=self.create_user(
            email,
            date_of_birth=date_of_birth,
            profile_photo=profile_photo,
            password=password
        )
        is_staff=True
        is_superuser=True
        
        user.save(using=self._db)
        
        return user

class CustomUser(AbstractUser):
    email=models.EmailField(unique=True)
    date_of_birth=models.DateField()
    profile_photo=models.ImageField(upload_to="profile_photos")
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    objects=CustomUserManager()
    
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["date_of_birth","profile_photo"]
    def __str__(self):
        return self.email

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # other fields...

    def __str__(self):
        return self.user.username
    
    
@permission_required('app_name.can_edit', raise_exception=True)
def edit_view(request, pk):
    instance = get_object_or_404(MyModel, pk=pk)
    if request.method == 'POST':
        instance.name = request.POST['name']
        instance.save()
        return redirect('success_url')
    return render(request, 'edit_template.html', {'instance': instance})

@permission_required('app_name.can_delete', raise_exception=True)
def delete_view(request, pk):
    instance = get_object_or_404(MyModel, pk=pk)
    instance.delete()
    return redirect('success_url')
