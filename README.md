# dj-generator
A lot of our time we spend on creating CURD in django. This project aims to generate boilerplate code to reduce our valuable time.

The django templating system is pretty powerful. We can make use of the power of templating tool to generate basic CURD given a model.

## Assumptions
This project assumes that you follow certain folder structure. That makes this project to stay as simple as possible.

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
python manage.py generate app.Model --template power
```

For example if you run following command -
```sybase
python manage.py generate testapp.Task --template power
```

It will create -
- CRUD python files under ``testapp/task`` folder.
- CRUD template files under ``testapp/templates/testapp/task`` folder.

