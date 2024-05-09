from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm


#CRUD operations:

def task_list(request):
    tasks = Task.objects.all()
    tasks.order_by('-priority') #looked from stack social flow. - from hgihest to lowest. 
    return render(request, 'taskmanager/task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = Task.objects.get(id=pk)
    return render(request, 'taskmanager/task_detail.html', {'task': task})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return render(request, 'taskmanager/task_detail.html', {'task': task})
    else:
        form = TaskForm()
    return render(request, 'taskmanager/task_form.html', {'form': form})

def task_update(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            return render(request, 'taskmanager/task_detail.html', {'task': task})
    else:
        form = TaskForm(instance=task)
def task_delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return render(request, 'taskmanager/task_deleted.html')



