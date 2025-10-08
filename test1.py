from django.db import models
from django.contrib.auth.models import User
import uuid

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)

class Author(models.Model):
    bio = models.TextField()
    books = models.ManyToManyField(Book)
    user = models.OneToOneField(User, on_delete=models.CASCADE)