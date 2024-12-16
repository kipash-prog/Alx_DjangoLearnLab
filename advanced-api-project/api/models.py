from django.db import models

# Create your models here.
class Book(models.Model):
    author=models.CharField(max_length=180)
    title=models.CharField(max_length=180)

class Author(models.Model):
    name=models.CharField(max_length=180)
    
