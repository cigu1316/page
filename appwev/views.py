from django.shortcuts import render 


def home(request):
    return render(request,'appwev/home.html')
       
def tienda(request):
    
    return render(request,'appwev/tienda.html')

