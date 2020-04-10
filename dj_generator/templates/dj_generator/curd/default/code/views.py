from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from {{ app_model_module }} import {{ model_name }}


class {{ model_name }}ListView(ListView):
    model = {{ model_name }}
    paginate_by = 25
    template_name = '{{ template_path }}/list.html'


class {{ model_name }}CreateView(CreateView):
    model = {{ model_name }}
    fields = {{ model_fields|safe }}
    template_name = '{{ template_path }}/create.html'
    success_url = reverse_lazy('{{ model_name|slugify }}.list')


class {{ model_name }}UpdateView(UpdateView):
    model = {{ model_name }}
    fields = {{ model_fields|safe }}
    template_name = '{{ template_path }}/update.html'
    success_url = reverse_lazy('{{ model_name|slugify }}.list')


class {{ model_name }}DetailView(DetailView):
    model = {{ model_name }}
    template_name = '{{ template_path }}/detail.html'


class {{ model_name }}DeleteView(DeleteView):
    model = {{ model_name }}
    template_name = '{{ template_path }}/delete_confirm.html'
    success_url = reverse_lazy('{{ model_name|slugify }}.list')
