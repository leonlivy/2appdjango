from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.IntegerField()
    due_date = models.DateTimeField()
    status = models.CharField(max_length=20)


# Create your models here.
