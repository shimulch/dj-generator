from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django_tables2 import SingleTableView

from sandbox.testapp.models import Task
from . import forms
from . import table


class TaskListView(LoginRequiredMixin, PermissionRequiredMixin, SingleTableView):
    model = Task
    table_class = table.TaskTable
    template_name = 'testapp/task/list.html'
    permission_required = 'testapp.view_task'


class TaskCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Task
    form_class = forms.TaskCreateForm
    template_name = 'testapp/task/create.html'
    success_url = reverse_lazy('testapp:task.list')
    success_message = 'Task %(title)s created successfully!'
    permission_required = 'testapp.create_task'


class TaskUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = forms.TaskUpdateForm
    template_name = 'testapp/task/update.html'
    success_url = reverse_lazy('testapp:task.list')
    success_message = 'Task %(title)s updated successfully!'
    permission_required = 'testapp.change_task'


class TaskDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Task
    template_name = 'testapp/task/detail.html'
    permission_required = 'testapp.view_task'


class TaskDeleteView(LoginRequiredMixin, SuccessMessageMixin, PermissionRequiredMixin, DeleteView):
    model = Task
    template_name = 'testapp/task/delete_confirm.html'
    success_url = reverse_lazy('testapp:task.list')
    success_message = 'Task %(title)s deleted successfully!'
    permission_required = 'testapp.delete_task'