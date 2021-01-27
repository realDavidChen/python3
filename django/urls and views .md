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

 in home/ folder, add new file: urls.py and add content like this:
 
 ```
from django.urls import path
from . import views



urlpatterns = [
    path('', views.home),
    path('products/', views.products),
    path('blog/', views.blog),
   
    
]
 
 ```


