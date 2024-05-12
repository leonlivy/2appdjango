from django.db import models

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



