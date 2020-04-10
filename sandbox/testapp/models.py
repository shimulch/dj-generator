from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)