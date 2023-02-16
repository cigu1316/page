from django.shortcuts import render ,HttpResponse
from django.http import HttpResponse

  
def home(request):
    
    return render(request,'appwev/home.html')

def servicios(request):
    
    return render(request,'appwev/servicios.html')

def tienda(request):
    
    return HttpResponse('tienda')

def blog(request):
    
    return HttpResponse('blog')

def contacto(request):
    
    return HttpResponse ('contacto')
