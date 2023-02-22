from django.shortcuts import render , redirect
from .carro import carro
from apptienda.models import Producto


def agregar_producto(request,producto_id):
    carro=carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect("tienda")


def eliminar_producto(request,producto_id):
    carro=carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("tienda")

def restar_producto(request,producto_id):
    carro=carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.restar(producto=producto)
    return redirect("tienda")

def limpiar_carro(request,producto_id):
    carro=carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro,limpiar_carro()
    return redirect("tienda")

