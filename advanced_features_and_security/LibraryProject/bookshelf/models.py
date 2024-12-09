from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
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
    
    
    def create_superuser(self,email,date_of_birth,profile_photo,password):
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
    
    objects=CustomUserManager()
    
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["date_of_birth","profile_photo"]
    def __str__(self):
        return self.email
    