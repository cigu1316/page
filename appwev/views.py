from django.shortcuts import render 

def home(request):
        
    return render(request,'appwev/home.html')
       
def servicios(request):
      
    return render(request,'appwev/servicios.html')

def tienda(request):
    
    return render(request,'appwev/tienda.html')

def blog(request):
    
    return render(request,'appwev/blog.html')

def contacto(request):
    
    return render(request,'appwev/contacto.html')
