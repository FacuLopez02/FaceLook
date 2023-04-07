from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return render(request,'FaceLookApp/home.html')

def servicios(request):

    return render(request,'FaceLookApp/servicios.html')

def tienda(request):

    return render(request,'FaceLookApp/tienda.html')

def blog(request):

    return render(request,'FaceLookApp/blog.html')

def contacto(request):

    return render(request,'FaceLookApp/contacto.html')