from django.urls import path
from . import views


urlpattern = [
    path('{{ model_name_plural|slugify }}/', views.{{ model_name }}ListView.as_view(), name='{{ model_name|slugify }}.list'),
    path('{{ model_name_plural|slugify }}/create/', views.{{ model_name }}CreateView.as_view(), name='{{ model_name|slugify }}.create'),
    path('{{ model_name_plural|slugify }}/<int:pk>/', views.{{ model_name }}DetailView.as_view(), name='{{ model_name|slugify }}.detail'),
    path('{{ model_name_plural|slugify }}/<int:pk>/update/', views.{{ model_name }}UpdateView.as_view(), name='{{ model_name|slugify }}.update'),
    path('{{ model_name_plural|slugify }}/<int:pk>/delete/', views.{{ model_name }}DeleteView.as_view(), name='{{ model_name|slugify }}.delete'),
]