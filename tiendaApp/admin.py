from django.contrib import admin
from .models import categoria_producto, producto

# Register your models here.
class categoria_prod_admin(admin.ModelAdmin):
    
    readonly_fields=('created','updated')
    

class prod_admin(admin.ModelAdmin):
    
    readonly_fields=('created','updated')


admin.site.register(categoria_producto, categoria_prod_admin)
admin.site.register(producto, prod_admin)