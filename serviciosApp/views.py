from django.shortcuts import render
from .models import Servicio

# Create your views here.

def servicios(request):
    list_servicios = Servicio.objects.all()
    
    return render(request,'servicios/servicios.html',{"servicios": list_servicios})