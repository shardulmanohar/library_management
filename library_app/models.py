from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class AdminUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    publication_date = models.DateField()

    def __str__(self):
        return self.title
