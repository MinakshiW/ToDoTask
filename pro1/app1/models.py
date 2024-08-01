from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=34)
    description = models.CharField(max_length=700)
    status = models.CharField(max_length=23, default='Created')
    deadline = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(auto_now=True)
