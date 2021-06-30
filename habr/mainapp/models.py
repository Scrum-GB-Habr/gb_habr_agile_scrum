from django.db import models
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Contact(models.Model):
    title = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    message_description = models.TextField(max_length=50)
