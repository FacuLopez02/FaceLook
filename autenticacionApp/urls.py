from django.urls import path
from .views import view_registro

urlpatterns = [
    path('', view_registro.as_view(), name="Autenticacion"),
]
