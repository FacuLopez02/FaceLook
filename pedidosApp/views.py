from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from pedidosApp.models import Pedido, LineaPedido
from carroApp.carro import Carro
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

# Create your views here.

@login_required(login_url="/autenticacion/login")
def procesar_pedido(request):

    pedido = Pedido.objects.create(user=request.user)
    carro = Carro(request)
    lineas_pedido=list()

    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(

            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido = pedido

        ))

    LineaPedido.objects.bulk_create(lineas_pedido)

    enviar_mail(
        pedido=pedido, 
        lineas_pedido=lineas_pedido, 
        nom_user = request.user.username,
        email_user = request.user.email
    )

    messages.success(request, "El pedido se realizó con éxito")

    return redirect("../tienda")

def enviar_mail(**kwargs):

    asunto = "Gracias por el pedido"
    mensaje = render_to_string("emails/pedido.html",{

        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "nom_user": kwargs.get("nom_user")
    })
    mensaje_texto = strip_tags(mensaje)
    from_email = "fl492279@gmail.com"
    to = kwargs.get("email_user")

    send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)