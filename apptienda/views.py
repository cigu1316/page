from django.shortcuts import render
from .models import Producto 
from .models import Categoria


def tienda(request):
    producto=Producto.objects.all()
      
    return render(request,"apptienda/tienda.html",{'producto':producto})
    
def producto(request):
    producto=Producto.objects.all()
    return render(request,"apptienda/producto.html",{'producto':producto})    

