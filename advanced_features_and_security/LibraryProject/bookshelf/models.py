from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, profile_photo, password=None):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, date_of_birth=date_of_birth, profile_photo=profile_photo)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, profile_photo, password=None):
        user = self.create_user(email, date_of_birth, profile_photo, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    profile_photo = models.ImageField(upload_to="profile_photos")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth', 'profile_photo']

    class Meta:
        permissions = [
            ("can_view", "Can view user"),
            ("can_create", "Can create user"),
            ("can_edit", "Can edit user"),
            ("can_delete", "Can delete user"),
        ]

    def __str__(self):
        return self.email
