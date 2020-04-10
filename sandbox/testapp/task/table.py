import django_tables2 as tables
from sandbox.testapp.models import Task


class TaskTable(tables.Table):

    actions = tables.TemplateColumn(template_name='testapp/task/table_actions.html', orderable=False)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description'] + ['actions']
