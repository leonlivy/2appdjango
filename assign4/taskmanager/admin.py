from django.contrib import admin
from .models import Task

admin.site.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'priority', 'due_date', 'status')

# Register your models here.
