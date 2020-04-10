try:
    from sandbox.testapp.task import urls

    app_name = 'testapp'
    urlpatterns = urls.urlpattern
except Exception as _:
    urlpatterns = []