from django.urls import path
from django.urls import path
from apptienda import views

urlpatterns =[
    path('',views.tienda,name='tienda'),
    path('listar_producto/',views.listar_producto,name='listar_producto'),
    
                 ]