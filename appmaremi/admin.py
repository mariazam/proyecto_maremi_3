from django.contrib import admin
from .models import *
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio']
    list_editable= ['precio']
    search_fields= ['nombre']
    list_filter= ['categoria']

admin.site.register(Categoria)
admin.site.register(Vendedor)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Contacto)
