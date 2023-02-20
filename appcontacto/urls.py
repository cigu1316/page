from django.urls import path
from appcontacto import views

urlpatterns = [   
    
    path('',views.contacto,name='contacto'),
    
     ]   