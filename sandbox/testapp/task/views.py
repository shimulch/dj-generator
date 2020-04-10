from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from sandbox.testapp.models import Task


class TaskListView(ListView):
    model = Task
    paginate_by = 25
    template_name = 'testapp/task/list.html'


class TaskCreateView(SuccessMessageMixin, CreateView):
    model = Task
    fields = ['id', 'title', 'description']
    template_name = 'testapp/task/create.html'
    success_url = reverse_lazy('testapp:task.list')
    success_message = 'Task %(title)s created successfully!'


class TaskUpdateView(SuccessMessageMixin, UpdateView):
    model = Task
    fields = ['id', 'title', 'description']
    template_name = 'testapp/task/update.html'
    success_url = reverse_lazy('testapp:task.list')
    success_message = 'Task %(title)s updated successfully!'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'testapp/task/detail.html'


class TaskDeleteView(SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'testapp/task/delete_confirm.html'
    success_url = reverse_lazy('testapp:task.list')
    success_message = 'Task %(title)s deleted successfully!'
