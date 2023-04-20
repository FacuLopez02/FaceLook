from django.db import models

# Create your models here.

class categoria_producto(models.Model):
    
    nombre_cat = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = "categoria_producto"
        verbose_name_plural ="categorias_productos"
        
    def str(self):
        return self.nombre
    
class producto(models.Model):
    
    nombre_prod = models.CharField(max_length=50)
    categorias = models.ForeignKey(categoria_producto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="tienda", null=True, blank=True)
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "producto"
        verbose_name_plural ="productos"