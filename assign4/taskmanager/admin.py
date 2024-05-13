from django.contrib import admin
from .models import Task, StatusUpdate

admin.site.register(Task)
admin.site.register(StatusUpdate)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'priority', 'due_date', 'status')

class StatusUpdateAdmin(admin.ModelAdmin):
    list_display = ('task', 'status', 'updated_at', 'user')

# Register your models here.
