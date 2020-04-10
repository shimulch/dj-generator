# dj-generator
This project aims to generate boilerplate code to reduce our valuable time.

The django templating system is (pretty) powerful. We can make use of the power of templating tool to generate repetitive code to save time.

## Assumptions
This project assumes that you would not mind to use folder structure. That makes this project to stay as simple as possible.

## Installation
Install from pypy -
```sybase
pip install dj-generator
```
Add to ``INSTALLED_APPS`` in your ``settings.py``
```python
INSTALLED_APPS = [
    ...,
    
    'dj_generator'
]
```
## Usage
Pattern -
```sybase
python manage.py generate app.Model --template default
```

For example if you run following command -
```sybase
python manage.py generate testapp.Task --template default
```

It will create -
- CRUD python files under ``testapp/task`` folder.
- CRUD template files under ``testapp/templates/testapp/task`` folder.

Now, all you need to do is to load urls from nested directory to your app's ``urls.py``
For our example, content of ``testapp\url.py`` will be -
```python
...
from sandbox.testapp.task import urls as task_urls

app_name = 'testapp'
urlpatterns = []

urlpatterns += task_urls.urlpattern
```
Now you have full working CRUD for ``Task`` model

## Supported templates
Currently it has two different template for boilerplate code.

### default

Default is a bare bone template without any plugin or authentication. It generates following files for a model -
```sybase
app_dir
---- model_name
-------- __init__.py
-------- urls.py
-------- views.py
---- ...
---- templates
-------- app_name
------------ model_name
---------------- create.html
---------------- update.html
---------------- detail.html
---------------- delete_confirm.html
---------------- list.html
```

### power

Power generates forms, tables from django-tables2, authentication and permission. It generates following files for a model -
```sybase
app_dir
---- model_name
-------- __init__.py
-------- urls.py
-------- views.py
-------- forms.py
-------- table.py
---- ...
---- templates
-------- app_name
------------ model_name
---------------- create.html
---------------- update.html
---------------- detail.html
---------------- delete_confirm.html
---------------- list.html
---------------- table_actions.html

```
