from django.urls import path
from . import views


urlpattern = [
    path('tasks/', views.TaskListView.as_view(), name='task.list'),
    path('tasks/create/', views.TaskCreateView.as_view(), name='task.create'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task.detail'),
    path('tasks/<int:pk>/update/', views.TaskUpdateView.as_view(), name='task.update'),
    path('tasks/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task.delete'),
]