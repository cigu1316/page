from django.shortcuts import render 
from appservicios.models import Servicio


def home(request):
    return render(request,'appwev/home.html')
       
def servicios(request):
    servicio=Servicio.objects.all
    return render(request,'appwev/servicios.html',{'servicio':servicio})

    

def tienda(request):
    
    return render(request,'appwev/tienda.html')

def blog(request):
    
    return render(request,'appwev/blog.html')

def contacto(request):
    
    return render(request,'appwev/contacto.html')
