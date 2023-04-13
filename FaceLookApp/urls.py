from django.urls import path
from FaceLookApp import views

# Importaciones para encontrar los archivos multimedia
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="Home"),
    path('tienda/', views.tienda, name="Tienda"),
    path('contacto/', views.contacto, name="Contacto"),
]

# Ruta para encontrar los archivos multimedia
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)