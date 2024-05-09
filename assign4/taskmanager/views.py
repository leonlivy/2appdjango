from django.shortcuts import render
from .models import Task


#CRUD operations:

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'taskmanager/task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = Task.objects.get(id=pk)
    return render(request, 'taskmanager/task_detail.html', {'task': task})

def task_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        priority = request.POST['priority']
        due_date = request.POST['due_date']
        status = request.POST['status']
        task = Task.objects.create(title=title, description=description, priority=priority, due_date=due_date, status=status)
        return render(request, 'taskmanager/task_detail.html', {'task': task})
    return render(request, 'taskmanager/task_form.html')

def task_update(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        priority = request.POST['priority']
        due_date = request.POST['due_date']
        status = request.POST['status']
        task.title = title
        task.description = description
        task.priority = priority
        task.due_date = due_date
        task.status = status
        task.save()
        return render(request, 'taskmanager/task_detail.html', {'task': task})
    return render(request, 'taskmanager/task_form.html', {'task': task})

def task_delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return render(request, 'taskmanager/task_deleted.html')



