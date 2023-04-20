from django.shortcuts import render
from .forms import contacto_form
from django.shortcuts import redirect
from django.core.mail import send_mail

# Create your views here.


def contacto(request):
    formulario = contacto_form()
    
    if request.method=="POST":
        
        formulario = contacto_form(data = request.POST)
        
        if formulario.is_valid():
            
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")
            try:
                send_mail("Mail de "+nombre, contenido + "\n\n" + "Responder a: " + email, 'fl492279@gmail.com', ['fl492279@gmail.com'])
                return redirect("/contacto/?valido")
            
            except:
                return redirect("/contacto/?no_valido")
            
    

    return render(request,'contacto/contacto.html',{'formulario':formulario})