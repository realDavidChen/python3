
![](https://raw.githubusercontent.com/realDavidChen/python3/main/django/images/Controller-in-Django.png)


# method one(recommend): link to templates folder


## Basic sctructure map

```
myproject
  |---settings.py
  |---urls.py
home
  |---urls.py
  |---views.py
templates
  |----home.html
  |----blog.html

```
> please follow under 3 step to config urls

### 1. myproject(settings.py urls.py)
          

settings.py

```

TEMPLATES = [
    {    
    'DIRS': ['templates'],  
    },
    ]

```
urls.py

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))
    
]


```

### 2. home(urls.py views.py)

urls.py

```
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home')
]
```
views.py

```
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')


```
### 3 templates

home.html
```
<h1>this is home page</h1>
```

or create any page you want, like: blog.html, products.html etc.



================================================================================
================================================================================

# method two: link url to models

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

## 3.test urls and run server

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
