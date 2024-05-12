from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.task_list), name='task_list'),
    path('task/<int:pk>/', login_required(views.task_detail), name='task_detail'),
    path('task/new/', login_required(views.task_create), name='task_create'),
    path('task/<int:pk>/edit/', login_required(views.task_update), name='task_update'),
    path('task/<int:pk>/delete/', login_required(views.task_delete), name='task_delete'),
]
