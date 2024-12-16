from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser,User
from rest_framework import generics, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    following=models.ManyToManyField('self',symmetrical=False)
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
    

class Like(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        unique_together = ('post', 'user')

    def __str__(self):
        return f'{self.user} likes {self.post}'
    
