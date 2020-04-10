from django import forms
from {{ app_model_module }} import {{ model_name }}


class {{ model_name }}CreateForm(forms.ModelForm):

    class Meta:
        model = {{ model_name }}
        fields = {{ model_fields|safe }}


class {{model_name}}UpdateForm(forms.ModelForm):

    class Meta:
        model = {{model_name}}
        fields = {{model_fields| safe}}
