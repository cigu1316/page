from django.urls import path
from appservicios import views

urlpatterns = [   
    path('',views.servicios,name='servicios'),

]  



