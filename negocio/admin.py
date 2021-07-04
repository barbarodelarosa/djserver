from django.contrib import admin

from negocio.models import Negocio as MyNegocio
from negocio.models import Producto as MyProducto
from negocio.models import *


class MyNegocioAdmin(admin.ModelAdmin):
    model = MyNegocio

    list_display = ('aprobado','nombre', 'actualizado', 'pais','provincia','municipio','votos', 'compartido')
    list_display_links = ('aprobado','nombre', 'actualizado')
    search_fields = ['categoria', 'owner', 'nombre', 'descripcion', 'pais','provincia','municipio']
    filter_horizontal = ['categoria','seguidores']
    list_filter = ['categoria', 'aprobado', 'creado', 'pais','provincia','municipio','actualizado']
    ordering = ['aprobado','creado','actualizado','votos','compartido', 'nombre']
    date_hierarchy = 'creado'
    raw_id_fields = ('owner',)



class MyProductoAdmin(admin.ModelAdmin):
    model = MyProducto

    list_display = ('aprobado', 'nombre', 'precio','actualizado', 'votos', 'compartido')
    list_display_links = ('nombre', 'actualizado')
    search_fields = ['categoria', 'owner', 'nombre', 'descripcion']
    filter_horizontal = ['categoria']
    list_filter = ['categoria', 'aprobado', 'creado', 'actualizado']
    ordering = ['aprobado', 'creado', 'actualizado', 'votos', 'compartido', 'nombre', 'precio']
    date_hierarchy = 'creado'
    raw_id_fields = ('owner',)




admin.site.register(CategoriaNegocio)
admin.site.register(MyNegocio, MyNegocioAdmin)

admin.site.register(CategoriaProducto)
admin.site.register(MyProducto, MyProductoAdmin)
admin.site.register(Seguidor)
admin.site.register(Galeria)


# Register your models here.
