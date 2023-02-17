
from django.shortcuts import render 
from appservicios.models import Servicio

      
def servicios(request):
    servicios = Servicio.objects.all()
    return render(request,'appservicios/servicios.html',{'servicio':servicios})
  