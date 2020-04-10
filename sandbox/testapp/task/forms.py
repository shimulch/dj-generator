from django import forms
from sandbox.testapp.models import Task


class TaskCreateForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['id', 'title', 'description']


class TaskUpdateForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['id', 'title', 'description']
