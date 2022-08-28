# Django REST Framework
The Django REST Framework is a powerful and flexible tool for building Web APIs.
##### source: [Django REST Framework](https://www.django-rest-framework.org/)

### Implementing the REST Framework
* Set up your Django project like any other Django project.
  * In the command line in your .venv:  
    `python -m pip install djangorestframework~=3.13.0`
  * In settings.py, add under `INSTALLED_APPS:`  
    `rest_framework`
  * In the command line:  
    `python manage.py startapp apis`
  * In settings.py, add under `INSTALLED_APPS`:  
    `apis.apps.ApisConfig`
  * In the project urls.py file, add:  
    `path("api/", include("apis.urls")),`
  * In the application urls.py file, add:
    `from .views import BookAPIView` (where "Book" would 
    be the name of your application)  
    `path("", BookAPIView.as_view(), name="book_list"),` 
  * Update the apis/views.py file to include the queryset and 
    serializer_class:  
    `queryset = Book.objects.all()`  
    `serializer_class = BookSerializer`
  * Add a new file called "apis/serializers.py" with the following in it:  
    from rest_framework import serializers
    ```
    from books.models import Book
    
    class BookSerializer(serializers.ModelSerializer):
        class Meta:
            model = Book
            fields = ("title", "subtitle", "author", "isbn")
    ```
    