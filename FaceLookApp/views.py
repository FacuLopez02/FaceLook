from django.shortcuts import render, HttpResponse
from serviciosApp.models import Servicio

# Create your views here.

def home(request):

    return render(request,'FaceLookApp/home.html')

def servicios(request):
    list_servicios = Servicio.objects.all()
    
    return render(request,'FaceLookApp/servicios.html',{"servicios": list_servicios})

def tienda(request):

    return render(request,'FaceLookApp/tienda.html')

def blog(request):

    return render(request,'FaceLookApp/blog.html')

def contacto(request):

    return render(request,'FaceLookApp/contacto.html')