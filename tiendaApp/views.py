from django.shortcuts import render
from .models import producto

# Create your views here.

def tienda(request):

    lista_productos = producto.objects.all()
    
    return render(request,'tienda/tienda.html',{'productos': lista_productos})