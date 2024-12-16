from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class SocialMediaUser(AbstractUser):
    bio=models.TextField(blank=True,null=True)
    profile_picture=models.ImageField(upload_to='images')
    following=models.ManyToManyField('self',symmetrical=False)
    
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='social_media_users',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='social_media_users',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
    
    def __str__(self):
        return self.username

    
    