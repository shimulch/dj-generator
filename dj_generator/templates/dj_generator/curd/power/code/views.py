from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django_tables2 import SingleTableView

from {{ app_model_module }} import {{ model_name }}
from . import forms
from . import table


class {{ model_name }}ListView(LoginRequiredMixin, PermissionRequiredMixin, SingleTableView):
    model = {{ model_name }}
    table_class = table.{{ model_name }}Table
    template_name = '{{ template_path }}/list.html'
    permission_required = '{{ app_label|add:".view_"|add:model_name_slug }}'


class {{ model_name }}CreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = {{ model_name }}
    form_class = forms.{{ model_name }}CreateForm
    template_name = '{{ template_path }}/create.html'
    success_url = reverse_lazy('{{ routes.list }}')
    success_message = '{{ model_name }} %({{ model_fields.1 }})s created successfully!'
    permission_required = '{{ app_label|add:".create_"|add:model_name_slug }}'


class {{ model_name }}UpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = {{ model_name }}
    form_class = forms.{{model_name}}UpdateForm
    template_name = '{{ template_path }}/update.html'
    success_url = reverse_lazy('{{ routes.list }}')
    success_message = '{{ model_name }} %({{ model_fields.1 }})s updated successfully!'
    permission_required = '{{ app_label|add:".change_"|add:model_name_slug }}'


class {{ model_name }}DetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = {{ model_name }}
    template_name = '{{ template_path }}/detail.html'
    permission_required = '{{ app_label|add:".view_"|add:model_name_slug }}'


class {{ model_name }}DeleteView(LoginRequiredMixin, SuccessMessageMixin, PermissionRequiredMixin, DeleteView):
    model = {{ model_name }}
    template_name = '{{ template_path }}/delete_confirm.html'
    success_url = reverse_lazy('{{ routes.list }}')
    success_message = '{{ model_name }} %({{ model_fields.1 }})s deleted successfully!'
    permission_required = '{{ app_label|add:".delete_"|add:model_name_slug }}'