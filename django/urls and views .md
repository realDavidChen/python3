## 1. create new django project
$ django-admin startproject myproject
> you can see the myproject inner include:
```
myproject:
|--manage.py 
|--myproject( this-folder-for-app-global-settings)/urls.py

```
myproject/urls.py example:

```
from django.contrib import admin
from django.urls import path, include

from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
  
]

```

## 2. create news app and add urls.py link

$ django-admin startapp home

> now your folder sctructure like this: 

```
myproject:
|--manage.py 
|--myproject/
|--home/

```

 in home/ folder, add new file: urls.py and add content:
 
 ```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('products/', views.products),
    path('blog/', views.blog),
   
    
]
 
 ```
 
 in home/views.py add content:
 
 
 ```
 
 from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('home')
def products(request):
    return HttpResponse('products')
def blog(request):
    return HttpResponse('blog')
 
 ```

## 3 run server

$ python manage.py runserver

open browser, and test it:

http://localhost:8000/products
http://localhost:8000/blog

### >> get django-admin help

$ django-admin

```

Type 'django-admin help <subcommand>' for help on a specific subcommand.

Available subcommands:

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    runserver
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

```
