from django.contrib import admin
from django.urls import path
from django.urls.conf import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('appwev.urls')),
    path('servicios/',include('appservicios.urls')),
    path('blog/',include('appblog.urls')),
    
]

