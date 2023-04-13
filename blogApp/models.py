from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
        
    def __str__(self):
        return self.nombre
    
class Post(models.Model):
    
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='blog',null=True, blank=True) # Guarda las imagenes en una carpeta "blog" (la crea si no existe) y es un campo opcional
    autor = models.ForeignKey(User, on_delete=models.CASCADE) # Verifica que la eliminacion del usuario, tambien elimine todos sus posteos (eliminacion en cascada)
    categorias = models.ManyToManyField(Categoria) # Relacion Muchos a Muchos entre categorias y posteos
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='post'
        verbose_name_plural='posteos'
        
    def __str__(self):
        return self.titulo