import django_tables2 as tables
from {{ app_model_module }} import {{ model_name }}


class {{ model_name }}Table(tables.Table):

    actions = tables.TemplateColumn(template_name='{{ template_path }}/table_actions.html', orderable=False)

    class Meta:
        model = {{ model_name }}
        fields = {{ model_fields|safe }} + ['actions']
