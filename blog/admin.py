from blog.models import *
from blog.models import Post as MyPost
from django.contrib import admin

class MyPostAdmin(admin.ModelAdmin):

    model = MyPost
    list_display = ('aprobado', 'titulo', 'actualizado', 'votos', 'compartido')
    list_display_links = ('titulo',)
    search_fields = ['categoria', 'owner', 'titulo', 'mensaje']
    filter_horizontal = ['categoria','likes','alcance']
    list_filter = ['categoria', 'aprobado', 'creado', 'actualizado']
    ordering = ['aprobado','creado','actualizado','votos','compartido']




admin.site.register(MyPost, MyPostAdmin)
admin.site.register(CategoriaPost)
admin.site.register(Comentario)
admin.site.register(Imagen)















# Register your models here.
