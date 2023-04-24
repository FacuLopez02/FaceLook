from django.db import models

# Create your models here.

class categoria_producto(models.Model):
    
    nombre = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = "categoriaProd"
        verbose_name_plural ="categoriasProd"
        
    def __str__(self):
        return self.nombre
    
class producto(models.Model):
    
    nombre = models.CharField(max_length=50)
    categorias = models.ForeignKey(categoria_producto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="tienda", null=True, blank=True)
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = "producto"
        verbose_name_plural ="productos"
        
    def __str__(self):
        return self.nombre