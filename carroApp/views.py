from django.shortcuts import render
from .carro import Carro
from tiendaApp.models import producto
from django.shortcuts import redirect

# Create your views here.

def agregar_producto (request, producto_id):
    
    carro = Carro(request)
    
    producto_aux = producto.objects.get(id=producto_id)
    
    carro.agregar(producto_aux)
    
    return redirect("Tienda")

def eliminar_producto (request, producto_id):
    
    carro = Carro(request)
    
    producto_aux = producto.objects.get(id=producto_id)
    
    carro.eliminar(producto_aux)
    
    return redirect("Tienda")

def restar_producto (request, producto_id):
    
    carro = Carro(request)
    
    producto_aux = producto.objects.get(id=producto_id)
    
    carro.restar_producto(producto_aux)
    
    return redirect("Tienda")

def limpiar (request, producto_id):
    
    carro = Carro(request)
    
    carro.limpiar_carro()
    
    return redirect("Tienda")