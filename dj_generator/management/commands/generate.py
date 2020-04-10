from django.core.management.base import BaseCommand, CommandError
from django.template import engines
from django.template.loader import render_to_string
from django.apps import apps
from django.conf import settings
from django.utils.text import slugify
import os


class Command(BaseCommand):
    help = 'Generate different good things that speeds up development'

    def add_arguments(self, parser):
        parser.add_argument('model_name', nargs='?', help="Model to work with")
        parser.add_argument('--template', nargs='?', help="Witch template to use")
        parser.add_argument('--code-out', nargs='?', help="Where to put generated code.")
        parser.add_argument('--template-out', nargs='?', help="Where to put generated template")
        parser.add_argument('--force', action='store_true', help="Override if file exists!")

    def handle(self, *args, **options):
        app_label, model_name = options['model_name'].rsplit('.', 1)
        template = options['template']
        code_out_path = options['code_out']
        template_out_path = options['template_out']
        force = options['force']

        if not template:
            template = 'default'

        app_config = apps.get_app_config(app_label)
        app_module = app_config.module.__name__
        app_model_module = app_config.models_module.__name__
        model_cls = apps.get_model(app_label, model_name)
        model_fields = [field.name for field in model_cls._meta.fields]

        relative_generated_template_path = '/'.join(map(lambda x: slugify(x), options['model_name'].split('.')))

        if not code_out_path:
            code_out_path = os.path.join(app_config.path, slugify(model_name))

        if not template_out_path:
            template_out_path = os.path.join(app_config.path, 'templates', relative_generated_template_path)

        code_tpl_names, template_tpl_names = self.get_templates(template)

        context = {
            'model_cls': model_cls,
            'model_fields': model_fields,
            'app_label': app_label,
            'app_module': app_module,
            'app_model_module': app_model_module,
            'model_name': model_name,
            'model_name_plural': model_cls._meta.verbose_name_plural,
            'template_path': relative_generated_template_path
        }

        if len(code_tpl_names) > 0:
            if not os.path.exists(code_out_path):
                os.makedirs(code_out_path)
            self.generate_files(code_out_path, code_tpl_names, context, force)

        if len(template_tpl_names) > 0:
            if not os.path.exists(template_out_path):
                os.makedirs(template_out_path)
            self.generate_files(template_out_path, template_tpl_names, context, force)

    def get_template_dirs(self):
        """
        Find all available filesystem and app template directories.
        :return: []
        """
        template_dirs = []
        for engine in engines.all():
            for template_loader in engine.engine.template_loaders:
                template_dirs += template_loader.get_dirs()
        return template_dirs

    def get_templates(self, generator_template):
        """
        List of code templates and template templates, given a generator template
        :param generator_template:
        :return: [], []
        """
        template_dirs = self.get_template_dirs()
        code_tpl_names = []
        template_tpl_names = []
        for template_dir in template_dirs:
            generator_template_path = os.path.join(template_dir, 'dj_generator', 'curd', generator_template)
            if os.path.exists(generator_template_path):
                code_tpl_dir = os.path.join(generator_template_path, 'code')
                template_tpl_dir = os.path.join(generator_template_path, 'templates')
                if os.path.exists(code_tpl_dir):
                    code_tpl_names += [{
                        'file_name': f,
                        'template_name': f'dj_generator/curd/{generator_template}/code/{f}'
                    } for f in os.listdir(code_tpl_dir) if os.path.isfile(os.path.join(code_tpl_dir, f))]
                if os.path.exists(template_tpl_dir):
                    template_tpl_names += [{
                        'file_name': f,
                        'template_name': f'dj_generator/curd/{generator_template}/templates/{f}'
                    } for f in os.listdir(template_tpl_dir) if os.path.isfile(os.path.join(template_tpl_dir, f))]

        return code_tpl_names, template_tpl_names

    def generate_files(self, code_out_path, code_tpl_names, context, force=False):
        """
        Given input file list, output directory and context, render templates and write to file
        :param code_out_path:
        :param code_tpl_names:
        :param context:
        :return:
        """
        for template in code_tpl_names:
            rendered = render_to_string(template['template_name'], context=context)
            file_name = os.path.join(code_out_path, template['file_name'])
            exists = os.path.exists(file_name)
            if not exists or force:
                if exists:
                    self.stdout.write(self.style.WARNING(f'File {file_name} already exists! Overriding'))
                with open(file_name, 'w') as f:
                    f.write(rendered)
            else:
                self.stdout.write(self.style.WARNING(f'File {file_name} already exists! Skipping'))
