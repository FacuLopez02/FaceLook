from django.shortcuts import render
from .forms import contacto_form

# Create your views here.


def contacto(request):
    formulario = contacto_form()

    return render(request,'contacto/contacto.html',{'formulario':formulario})