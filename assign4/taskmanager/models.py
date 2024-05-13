from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    TASK_STATUS = [
        ('To Do', 'To Do'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done')
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.IntegerField()
    due_date = models.DateField()
    status = models.CharField(max_length=20,choices = TASK_STATUS, default='To Do')

class StatusUpdate(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=Task.TASK_STATUS)
    updated_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey( User, on_delete=models.CASCADE)

