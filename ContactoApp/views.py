from django.shortcuts import render
from .forms import contacto_form
from django.shortcuts import redirect

# Create your views here.


def contacto(request):
    formulario = contacto_form()
    
    if request.method=="POST":
        
        formulario = contacto_form(data = request.POST)
        
        if formulario.is_valid():
            
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")
            
            return redirect("/contacto/?valido")
            
    

    return render(request,'contacto/contacto.html',{'formulario':formulario})