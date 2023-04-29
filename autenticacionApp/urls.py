from django.urls import path
from .views import view_registro, cerrar_sesion, loguearse

urlpatterns = [
    path('', view_registro.as_view(), name="Autenticacion"),
    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"),
    path('login', loguearse, name="login"),
]
