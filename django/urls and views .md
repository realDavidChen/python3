## basic in myproject/urls.py  setting example:

```
from django.contrib import admin
from django.urls import path

from django.http import HttpResponse

def home(request):
    return HttpResponse('home page')

def contact(request):
    return HttpResponse('Please contact to me')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('about/', contact),
   
    
]

```
